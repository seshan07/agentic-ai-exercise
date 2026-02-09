import json
import sys

REQUIRED_FIELDS = ["name", "email", "age", "experience_years", "role_applied"]

def load_input(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data, None
    except FileNotFoundError:
        return None, "Input file not found"
    except json.JSONDecodeError:
        return None, "Invalid JSON format"

def evaluate_input(data):
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in data or data[field] in [None, ""]:
            missing_fields.append(field)

    if missing_fields:
        return {
            "decision": "ESCALATE",
            "reason": "Missing required fields",
            "details": missing_fields
        }

    if data["age"] < 18:
        return {
            "decision": "REJECT",
            "reason": "Candidate is under minimum age requirement"
        }

    if data["experience_years"] < 1:
        return {
            "decision": "REVIEW",
            "reason": "Insufficient experience for role"
        }

    return {
        "decision": "ACCEPT",
        "reason": "All requirements satisfied"
    }

def run_agent(input_file):
    data, error = load_input(input_file)
    if error:
        return {
            "decision": "ESCALATE",
            "reason": error
        }

    decision_output = evaluate_input(data)
    return decision_output

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide input file path")
        sys.exit(1)

    result = run_agent(sys.argv[1])
    print(json.dumps(result, indent=2))
