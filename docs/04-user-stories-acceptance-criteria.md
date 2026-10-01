# User Stories and Acceptance Criteria (FICTIONAL SAMPLE)

> Fictional product, fictional personas. Format: *As a [user], I want [capability] so that [benefit].* Criteria use Given / When / Then.

## User stories

### US-1: Review a suggested answer

As a **volunteer moderator**, I want to see a drafted reply with its sources so that I can check it before it is posted.

#### Acceptance criteria (US-1)

1. Given a new-member question with a relevant help article, when I open it, then I see a drafted reply and at least one source link.
2. Given a draft, when I choose Approve, then the reply is posted under my name and the outcome is logged.
3. Given a draft, when I edit and approve, then the edited text is posted and the edit is logged.
4. Given a draft, when I choose Reject, then nothing is posted and I can optionally say why.
5. Nothing is posted without an explicit moderator action.

### US-2: No guess when sources are missing

As a **moderator**, I want the system to say it has no suggestion when it cannot find a source so that I am not given a made-up answer.

#### Acceptance criteria (US-2)

1. Given a question with no relevant article above the agreed threshold, then the screen shows "No suggestion" and no draft text.
2. The "no suggestion" case is logged with the question category.
3. Given a conduct-related question (report, harassment), then no draft is produced and the item is routed to a human.

### US-3: Flag a bad draft

As a **moderator**, I want to flag a draft as wrong or unsafe so that the team can fix the cause.

#### Acceptance criteria (US-3)

1. Given a draft, when I click Flag, then I choose a reason (incorrect, outdated, unsafe, other).
2. Flagged drafts appear in a weekly review list for the community manager.
3. A flagged draft cannot be posted without being edited first.

### US-4: See how it is going

As a **community manager**, I want a weekly summary of drafts shown, approved, edited, rejected, and flagged so that I can judge quality and decide what to improve.

#### Acceptance criteria (US-4)

1. Given one week of activity, then the summary shows counts for each outcome.
2. The summary lists the top five unanswered topics (no-suggestion cases).
3. The summary shows no personal data beyond what moderators already see.

## Definition of done (sample)

- Acceptance criteria demonstrated in a walkthrough
- Tests written for the main flows
- Privacy and content review completed for the story
- Documentation updated
