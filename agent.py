from config import client, MODEL_NAME
import json

def code_review_agent(payload):
    code = payload["code"]

    prompt = f"""
You are a senior software engineer performing a professional code review.

Use ONLY these issue types:
- LONG_FUNCTION
- DUPLICATE_CODE
- HARDCODED_VALUE
- NAMING
- ERROR_HANDLING

Return ONLY valid JSON in this format:

{{
  "issues": [
    {{
      "type": "",
      "description": "",
      "line": "",
      "severity": "LOW | MEDIUM | HIGH",
      "suggestion": ""
    }}
  ],
  "summary": {{
    "total_issues": number,
    "high": number,
    "medium": number,
    "low": number
  }}
}}

Code:
{code}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a strict code reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    result = response.choices[0].message.content
    cleaned = clean_json_output(result)

    # Ensure JSON output
    try:
        return json.loads(cleaned)
    except:
        return {"error": "Invalid JSON", "raw_output": result}
    
def clean_json_output(text):
    text = text.strip()

    if "'''" in text:
        parts = text.split("'''")
        if len(parts) > 1:
            text = parts[1]

    if text.lower().startswith("json"):
        text = text[4:]

    return text.strip()