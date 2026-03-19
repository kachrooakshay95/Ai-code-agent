from fastapi import FastAPI
from agent import code_review_agent
from pydantic import BaseModel
from refactoring_agent import refactor_code_agent
from duplicate_agent import duplicate_removal_agent
from parameterization_agent import parameterization_agent

app = FastAPI()

class CodeRequest(BaseModel):
    file_name: str
    language: str
    code: str

@app.get("/")
def home():
    return {"message": "AI Code Quality Agent is running"}

@app.post("/review")
def review_code(payload: dict):
    result = code_review_agent(payload)
    return result

@app.post("/refactor")
def refactor_code(payload: CodeRequest):
    result = refactor_code_agent(payload.dict())
    return {"refactored_code": result}

@app.post("/remove-duplicates")
def remove_duplicates(payload: CodeRequest):
    result = duplicate_removal_agent(payload.dict())
    return {"optimized_code": result}

@app.post("/parameterize")
def parameterize_code(payload: CodeRequest):
    result = parameterization_agent(payload.dict())
    return {"optimized_code": result}