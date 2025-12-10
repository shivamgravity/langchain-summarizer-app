import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Text Summarizer",
    description="A simple API that uses Groq/Llama-3 to summarize text.",
    version="1.0.0"
)

# Initialize LLM
try:
    llm = ChatGroq(model="llama-3.1-8b-instant")
except Exception as e:
    print(f"Error initializing LLM: {e}")

# Define the Prompt Template
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Summarize the following text concisely in 3-5 sentences."),
    ("human", "{text}")
])

# Create the Chain
chain = summary_prompt | llm

# Define Request Model
class SummaryRequest(BaseModel):
    text: str

# Define Response Model
class SummaryResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummaryResponse)
async def summarize_text(request: SummaryRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text field cannot be empty")
    
    try:
        # Invoke the chain
        response = chain.invoke({"text": request.text})
        return {"summary": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)