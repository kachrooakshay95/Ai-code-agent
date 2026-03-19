from config import client, MODEL_NAME
import ast

def is_valid_python(code):
    try:
        ast.parse(code)   # tries to parse code
        return True       # valid syntax
    except:
        return False      # syntax error

def parameterization_agent(payload):
    code = payload["code"]

    prompt = f"""
You are a senior software engineer.

Your task is to strictly refactor the code by removing hardcoded values.

Instructions:
- Identify ALL hardcoded values such as:
  - numbers (except 0, 1)
  - strings
  - URLs
  - configuration values
- Convert them into named constants
- Place constants at the TOP of the file
- Use UPPERCASE names for constants

STRICT RULE:
- You MUST perform parameterization if any hardcoded value exists
- Do NOT return the same code unless absolutely no hardcoding exists

Return ONLY updated code (no explanation)

Code:
{code}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an expert in clean and maintainable code."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    if is_valid_python(result):
        return result
    else:
        return {
            "error": "Invalid Python generated",
            "raw_output": result
        }