# PRD: Suggested Answers for New-Member Questions (FICTIONAL SAMPLE)

> **Fictional product and sample data.** "CommunityHub" is an invented community platform. This PRD is a personal practice document. It does not describe any real product, employer, or client, and every number marked *assumption* or *hypothesis* is invented for illustration.

| Field | Value |
|---|---|
| Product | CommunityHub (fictional) |
| Feature | Suggested Answers: AI-drafted replies to common new-member questions, reviewed by a human moderator before posting |
| Author | Aindrila Das (practice document) |
| Status | Draft v0.1 |
| Last updated | 2026-10-01 |

## 1. Background and problem

In the fictional CommunityHub, new members often ask the same ten or so questions (how to join a channel, where events are listed, how to report a problem). Volunteer moderators answer them by hand, so answers can be slow and uneven.

*Assumption (to validate):* a meaningful share of first-week questions are repeats of questions already answered in the help centre.

## 2. Goals and non-goals

### Goals

- Help moderators answer repeat questions faster, using approved help-centre content.
- Keep a human in control of what gets posted.
- Measure whether new members get a first answer sooner and rate it helpful.

### Non-goals (this release)

- Fully automatic posting without human review.
- Answering questions that need judgement (conduct reports, account disputes).
- Supporting languages other than English.

## 3. Users and needs

| User | Need | Notes |
|---|---|---|
| New member | A quick, correct first answer | Fictional persona "Sam", joined this week |
| Volunteer moderator | Less repetitive typing; control over the final text | Persona "Priya" (fictional), 3 hours a week |
| Community manager | Visibility of quality and risks | Persona "Jordan" (fictional) |

## 4. Proposed solution (summary)

1. When a new-member question arrives, the system retrieves the most relevant help-centre articles.
2. A language model drafts a short reply that cites those articles. (Concept notes: [RAG and prompting](../learning-notes/llm-concepts.md).)
3. The moderator sees the draft with its sources, then edits, approves, or rejects it.
4. Approved replies are posted; rejections and edits are logged as feedback.
5. If no relevant article is found, the system says so and offers no draft.

## 5. Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Draft a reply using only retrieved help-centre content | Must |
| FR-2 | Show source article links with every draft | Must |
| FR-3 | Moderator can approve, edit, or reject; nothing posts without approval | Must |
| FR-4 | When confidence is low or no source is found, show "no suggestion" | Must |
| FR-5 | Log approve / edit / reject outcomes | Should |
| FR-6 | Moderators can flag a draft as wrong or unsafe | Should |
| NFR-1 | Draft appears within a target time agreed with engineering (*hypothesis: under 10 seconds*) | Should |
| NFR-2 | Do not send personal data beyond what is needed to the model provider | Must |

User stories and acceptance criteria: [04-user-stories-acceptance-criteria.md](04-user-stories-acceptance-criteria.md).

## 6. Success metrics

Defined in [05-metrics-and-okrs.md](05-metrics-and-okrs.md). Targets there are **hypotheses**, not results.

## 7. Risks and mitigations

See [06-risks-and-dependencies.md](06-risks-and-dependencies.md). Headline risks: incorrect answers, over-trust by moderators, privacy, and bias in what content gets retrieved.

## 8. Dependencies

- Help-centre content is current and approved.
- Engineering capacity for retrieval and the moderator review screen.
- A decision on the model provider and data-handling terms.

## 9. Rollout plan

| Phase | Scope | Exit criteria |
|---|---|---|
| 0. Content audit | Review help-centre coverage | Gaps listed and owned |
| 1. Internal pilot | A few moderators, shadow mode (drafts not posted) | Review quality sample is acceptable |
| 2. Limited beta | One community, human approval required | Metrics reviewed against hypotheses |
| 3. Wider release | Decision after beta review | Go / no-go recorded |

## 10. Open questions

- Which help-centre articles are authoritative when two disagree?
- What is the acceptable error rate for suggested drafts, and who decides?
- How should members be told that an answer was AI-assisted?
- What is the retention period for the feedback logs?

## 11. Appendix: links

- [Roadmap](02-roadmap.md)
- [RICE prioritisation](03-prioritization-rice.md)
- [Evaluation plan](07-evaluation-plan.md)
