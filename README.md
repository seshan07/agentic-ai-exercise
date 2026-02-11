Agentic AI Practical Exercise

What the agent does
This agent evaluates a structured input file representing a form submission.
It validates completeness, checks data types, applies business rules, and makes a decision with a clear explanation.

How it makes decisions
The agent uses deterministic rules:

- Missing required fields result in escalation
- Invalid JSON or missing file results in escalation
- Incorrect data types result in escalation
- Underage candidates are rejected
- Negative experience values result in escalation
- Less than 1 year of experience results in review
- Valid and complete inputs are accepted

Each decision includes a clear reason explaining why the decision was made.

Error handling and escalation
The agent is designed to fail safely and never crash.
It escalates instead of acting when:

- Input file is not found
- JSON format is invalid
- Required fields are missing
- Data types are incorrect
- Experience value is negative
- Any unexpected runtime error occurs

This ensures predictable and safe behavior.

Test cases included

Positive test case:
input.json

Negative test cases:
negative_missing_field.json
negative_wrong_type.json
negative_underage.json
negative_negative_experience.json

These test cases simulate real-world failure scenarios to validate robustness.

Assumptions

- Input is provided as a JSON file
- Rules are deterministic and static
- No external systems or APIs are used
- The agent is responsible only for validation and decision-making

Design explanation

The solution intentionally uses a simple rule-based structure instead of complex frameworks.
This makes the decision logic transparent, easy to review, and predictable.

The focus of the implementation is clarity, safe escalation, and structured agent behavior rather than complexity.

Trade-offs

- No machine learning or LLM integration
- Static rule definitions
- No configuration layer
- No logging framework

These were intentionally excluded to maintain simplicity and clarity.

Possible improvements

- Configurable rules from external file
- Structured logging
- Unit testing framework
- Confidence scoring
- Optional LLM-based reasoning for borderline review cases

Summary

This implementation demonstrates structured agent design, explicit decision boundaries, defensive programming, negative test coverage, and safe escalation handling. The emphasis is clarity, reliability, and ownership of system behavior.