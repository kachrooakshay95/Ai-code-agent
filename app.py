from fastapi import FastAPI
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()
api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

client = AzureOpenAI(
    api_key,
    api_version,
    azure_endpoint
)

@app.post("/review")
def review_code(code: str):
    response = client.chat.completions.create(
        model="gpt-code-agent",
        messages=[
            {"role": "system", "content": "You are a senior software engineer."},
            {"role": "user", "content": f"Review this code:\n{code}"}
        ]
    )

    return {"review": response.choices[0].message.content}