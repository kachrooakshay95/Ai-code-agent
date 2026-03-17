from fastapi import FastAPI
from openai import AzureOpenAI

app = FastAPI()

client = AzureOpenAI(
    api_key="DD0sXc2FYavIm2jLWkEWOwkfgkKgcX4PTupZElbdhrhoRIV9btw3JQQJ99CCACfhMk5XJ3w3AAABACOGpyDF",
    api_version="2024-02-15-preview",
    azure_endpoint="https://ai-code-agent-openai.openai.azure.com/openai/deployments/gpt-code-agent/chat/completions?api-version=2025-01-01-preview"
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