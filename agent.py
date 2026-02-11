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
    except Exception as e:
        return None, f"Unexpected error while loading input: {str(e)}"


def validate_data_types(data):
    try:
        if not isinstance(data["name"], str):
            return False, "Invalid data type for name"

        if not isinstance(data["email"], str):
            return False, "Invalid data type for email"

        if not isinstance(data["age"], int):
            return False, "Age must be an integer"

        if not isinstance(data["experience_years"], int):
            return False, "Experience years must be an integer"

        if not isinstance(data["role_applied"], str):
            return False, "Invalid data type for role_applied"

        return True, None

    except KeyError as e:
        return False, f"Missing required field: {str(e)}"
    except Exception as e:
        return False, f"Unexpected validation error: {str(e)}"


def evaluate_input(data):
    try:
        missing_fields = [
            field for field in REQUIRED_FIELDS
            if field not in data or data[field] in [None, ""]
        ]

        if missing_fields:
            return {
                "decision": "ESCALATE",
                "reason": "Missing required fields",
                "details": missing_fields
            }

        valid, validation_error = validate_data_types(data)
        if not valid:
            return {
                "decision": "ESCALATE",
                "reason": validation_error
            }

        if data["age"] < 18:
            return {
                "decision": "REJECT",
                "reason": "Candidate is under minimum age requirement"
            }

        if data["experience_years"] < 0:
            return {
                "decision": "ESCALATE",
                "reason": "Experience years cannot be negative"
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

    except Exception as e:
        return {
            "decision": "ESCALATE",
            "reason": f"Unexpected evaluation error: {str(e)}"
        }


def run_agent(input_file):
    data, error = load_input(input_file)

    if error:
        return {
            "decision": "ESCALATE",
            "reason": error
        }

    return evaluate_input(data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide input file path")
        sys.exit(1)

    result = run_agent(sys.argv[1])