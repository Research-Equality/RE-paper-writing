---
name: paper-memory-ledger
description: Maintain a persistent project memory file for a paper, including venue choices, writing preferences, experiment conclusions, artifact locations, and unresolved decisions across sessions. Use when paper work spans multiple sessions and repeated clarification wastes time.
argument-hint: [paper-project]
---

# Paper Memory Ledger

Use this skill when a paper project needs continuity across sessions, revisions, or collaborators.

## When to Use

- The same paper is being drafted over many sessions
- Venue constraints, claim framing, or experiment conclusions keep getting re-established from scratch
- The team wants a single memory file that records stable project facts without re-reading old threads

For one-session compaction, use `paper-session-compaction`.
For experiment-to-report handoff, use `experiment-report-bridge`.

## Workflow

### Step 1: Create the Ledger
- Store the ledger in a project-local path such as `memory/paper-memory.md`.
- Start with explicit placeholders rather than filling gaps from memory.
- Use a stable section structure so later updates stay mergeable.

### Step 2: Record Only Durable Facts
- Save target venue, draft status, core contribution, accepted terminology, figure/table locations, and experiment conclusions that are already real.
- Capture writing preferences and team conventions only when they are stable enough to matter later.
- Do not record speculative ideas as if they were decisions.

### Step 3: Update Immediately on Key Changes
- When the venue changes, a claim is downgraded, a major experiment concludes, or a reviewer requirement becomes binding, update the ledger.
- Keep entries concise and additive; merge rather than duplicate.
- Record dates for major experiment or revision milestones.

### Step 4: Read Before Restarting Work
- Review the ledger at the start of a new session before asking repeated clarification questions.
- Use it to restore project context, not to replace reading the current draft.
- If the ledger conflicts with the draft, fix the ledger or the draft immediately.

## References

- `references/ledger-template.md`: suggested section structure for project memory
- `references/update-triggers.md`: what belongs in the ledger and what does not

## Rules

- Only store stable facts, not passing brainstorms.
- Record experiment conclusions only when the evidence exists.
- Keep unknown fields explicit instead of guessing.
- The ledger should reduce repeated clarification, not become a second draft.

## Related Skills

- Upstream: [research-planning](../research-planning/), [venue-submission-strategy](../venue-submission-strategy/), [experiment-report-bridge](../experiment-report-bridge/)
- Downstream: [ml-paper-writing](../ml-paper-writing/), [paper-revision](../paper-revision/), [paper-session-compaction](../paper-session-compaction/)
- See also: [paper-evidence-verifier](../paper-evidence-verifier/), [reporting-guidelines-check](../reporting-guidelines-check/)
