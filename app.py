import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables (API Key)
load_dotenv()

app = FastAPI(
    title="LangChain Text Summarizer",
    description="A full-stack AI application using FastAPI, LangChain, and Groq."
)

# Mount the 'static' folder
# This allows the HTML file to load the CSS file.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the Frontend at the Root URL
@app.get("/")
def read_root():
    return FileResponse("static/index.html")

# Initialize the LLM (using Groq for speed/free tier)
try:
    llm = ChatGroq(model="llama-3.1-8b-instant")
except Exception as e:
    print(f"Error initializing LLM: {e}")

# Define the Prompt Template
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Summarize the following text concisely under 100 words."),
    ("human", "{text}")
])

# Create the LangChain Pipeline
chain = summary_prompt | llm

# Data Models
class SummaryRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

# API Endpoints

@app.post("/summarize", response_model=SummaryResponse)
async def summarize_text(request: SummaryRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    try:
        # Run the chain
        response = chain.invoke({"text": request.text})
        return {"summary": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)