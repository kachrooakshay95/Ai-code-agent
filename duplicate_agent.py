from config import client, MODEL_NAME
import ast

def is_valid_python(code):
    try:
        ast.parse(code)   # tries to parse code
        return True       # valid syntax
    except:
        return False      # syntax error

def duplicate_removal_agent(payload):
    code = payload["code"]

    prompt = f"""
You are a senior software engineer.

Analyze the code and:
- Identify duplicate or repeated logic
- Refactor the code to remove duplication
- Extract reusable functions where needed

IMPORTANT RULES:
- Do NOT change functionality
- Keep the same behavior
- Keep the same language
- Improve readability
- Return ONLY the improved code (no explanation)

Code:
{code}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an expert in code optimization."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    if is_valid_python(result):
        return result
    else:
        return code