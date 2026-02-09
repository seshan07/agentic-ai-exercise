Agentic AI Practical Exercise

What the agent does
This agent evaluates a structured input file representing a form submission.
It checks completeness, validates basic rules, and makes a decision.

How it makes decisions
The agent uses deterministic rules:
- Missing required fields result in escalation
- Invalid inputs result in escalation
- Business rules decide accept, review, or reject
Each decision includes a clear reason.

Assumptions
- Input is provided as a JSON file
- Rules are simple and deterministic
- No external systems are called

Where it may fail
- Rules are static and not learned
- Complex or subjective decisions are not supported
- Does not handle large-scale inputs

Improvements with more time
- Configurable rules
- Logging and monitoring
- Integration with an LLM for nuanced reasoning
- Confidence scoring 
