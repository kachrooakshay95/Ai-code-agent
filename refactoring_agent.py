from config import client, MODEL_NAME

def refactor_code_agent(payload):
    code = payload["code"]

    prompt = f"""
You are a senior software engineer specializing in code refactoring.

Refactor the following code with these goals:
- Break long functions into smaller reusable functions
- Improve readability and structure
- Remove redundant logic if possible
- Keep the functionality EXACTLY the same

IMPORTANT RULES:
- Do NOT change the logic
- Do NOT remove necessary functionality
- Keep the same language
- Return ONLY the improved code (no explanation)

Code:
{code}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an expert code refactoring assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content