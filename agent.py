from config import client, MODEL_NAME
import json

def code_review_agent(payload):
    code = payload["code"]

    prompt = f"""
You are a senior software engineer performing a professional code review.

Analyze the code and identify:
- Long functions (>50 lines)
- Hardcoded values
- Duplicate logic
- Poor naming conventions
- Missing error handling

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

    # Ensure JSON output
    try:
        return json.loads(result)
    except:
        return {"error": "Invalid JSON", "raw_output": result}