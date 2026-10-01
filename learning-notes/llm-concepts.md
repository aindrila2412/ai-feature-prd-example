# LLM and Agentic AI: Learning Notes

> **Learning notes, not expertise claims.** These are my own concise study notes written to support product thinking about AI features. They are simplified, may be incomplete, and are not based on any employer or client work. Check primary documentation for anything you rely on.

## Language models in one paragraph

A large language model (LLM) predicts likely next tokens given text so far. This makes it good at drafting, summarising, and rephrasing, and means it can sound confident while being wrong ("hallucination"). It does not "look things up" unless connected to a tool or data source.

## Prompting

- Be specific about the task, the audience, and the output format.
- Give context and, where helpful, one or two examples.
- Tell the model what to do when information is missing ("say you do not know").
- Iterate: change one thing at a time and compare outputs on the same test inputs.

## Tool use (function calling)

A model can be given a list of tools (for example "search help centre", "get event date"). It outputs a request to call a tool with arguments; the application runs it and returns the result; the model continues. The application, not the model, executes tools, so permissions and validation belong in the application.

## Agents and loops

An "agent" is usually a loop: **observe → decide → act (tool) → observe**, until a stop condition. Practical concerns: limit the number of steps, log every action, ask a human before irreversible actions, and handle tool failures. The tiny [`mock_agent.py`](mock_agent.py) shows this loop with plain rules and no model.

## Retrieval-augmented generation (RAG)

1. Split trusted documents into chunks.
2. Given a question, retrieve the most relevant chunks (keyword or embedding search).
3. Put them in the prompt and ask the model to answer **only** from them, with citations.

RAG reduces, but does not remove, wrong answers. Quality depends on content freshness and retrieval quality. Include a "no answer" path.

## Evaluation

- Build a small test set of realistic inputs with expected outcomes.
- Score on correctness, groundedness (is every claim in the source?), tone, and safety.
- Use human review early; automated or model-based grading can help later but needs checking.
- Track results over time so changes to prompts or content can be compared.

## Risks to plan for

| Risk | Example | Common mitigation |
|---|---|---|
| Inaccurate output | Confident wrong answer | Citations, human review, "no answer" path |
| Privacy | Personal data in prompts | Minimise data; check provider terms |
| Bias | Uneven quality across topics or groups | Test across groups; monitor |
| Over-reliance | Reviewers stop checking | Sampling audits, training |
| Prompt injection | Text in a document tries to give the model orders | Treat retrieved text as data; limit tool permissions |
| Cost and latency | Slow or expensive calls | Measure; set budgets |

## How this connects to the PRD example

The [PRD](../docs/01-prd.md) applies these ideas to a fictional feature: retrieval with citations, human approval, a "no suggestion" path, and an [evaluation plan](../docs/07-evaluation-plan.md).

## Things I am still learning

- Practical differences between retrieval methods
- Building automated evaluation I can trust
- How teams decide acceptable error rates
