from agent import code_review_agent
from refactoring_agent import refactor_code_agent
from duplicate_agent import duplicate_removal_agent
from parameterization_agent import parameterization_agent

def orchestrate_agents(payload):
    data = payload.copy()
    steps = []

    # Step 1: Review
    review = code_review_agent(data)

    final_code = data["code"]

    # Step 2: Decision-based execution
    issues = review.get("issues", [])

    issue_types = [issue["type"] for issue in issues]

    # 🔹 Refactor if long function
    if "LONG_FUNCTION" in issue_types:
        final_code = refactor_code_agent({**data, "code": final_code})

    # 🔹 Remove duplicates
    if "DUPLICATE_CODE" in issue_types:
        final_code = duplicate_removal_agent({**data, "code": final_code})
        steps.append("duplicate_agent")

    # 🔹 Parameterize
    if "HARDCODED_VALUE" in issue_types:
        final_code = parameterization_agent({**data, "code": final_code})
        steps.append("parameterization_agent")

    print("ISSUES:", issues)
    print("ISSUE TYPES:", issue_types)
    print("STEPS:", steps)

    return {
        "review": review,
        "execution_path": steps,
        "final_code": final_code
    }