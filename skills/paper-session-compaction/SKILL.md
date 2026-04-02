---
name: paper-session-compaction
description: Compact long paper-writing or revision sessions into a continuation brief that preserves decisions, evidence status, artifact paths, and unresolved TODOs so work can resume safely after context overflow or long iterations.
argument-hint: [thread-or-draft-state]
---

# Paper Session Compaction

Use this skill when a paper-writing session has become too long to keep fully in context, but you still need a reliable handoff into the next session.

## When to Use

- A long drafting or revision thread risks context overflow
- The conversation already contains many settled decisions, file paths, and open issues
- You want to resume later without re-reading the full session or re-asking the same questions

For persistent cross-session facts, use `paper-memory-ledger`.
For manuscript revision itself, use `paper-revision`.

## Workflow

### Step 1: Separate Stable From Active Context
- Keep the current working target, latest draft file, and unresolved reviewer questions visible.
- Compact older settled discussion instead of compressing the newest live conflict.
- Preserve exact paths, IDs, and labels that later steps depend on.

### Step 2: Write the Continuation Brief
- Summarize only the information that the next session truly needs:
  - current paper state
  - locked decisions
  - evidence and artifact status
  - unresolved risks
  - next actions
- Include what was not changed, not only what was changed.

### Step 3: Preserve Handoff Artifacts
- Keep links or paths to the current draft, figures, tables, scorecards, and rebuttal notes.
- If earlier chat history is offloaded elsewhere, point to that location explicitly.
- Record token savings or compaction scope only as metadata, not as the main summary.

### Step 4: Resume Safely
- Start the next session from the continuation brief plus the latest files.
- Re-open only the relevant source files instead of replaying the entire chat.
- If there is ambiguity after compaction, surface it immediately instead of guessing.

## References

- `references/continuation-brief.md`: recommended compaction summary schema
- `references/when-to-compact.md`: triggers, risks, and recovery rules

## Rules

- Do not compress away unresolved disagreements or TODOs.
- Preserve exact artifact paths, citation decisions, and venue assumptions.
- Compaction should reduce tokens, not remove accountability.
- Treat the continuation brief as a handoff document, not a vague recap.

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [latex-writeup-loop](../latex-writeup-loop/), [paper-revision](../paper-revision/)
- Downstream: [self-review](../self-review/), [review-ensemble](../review-ensemble/)
- See also: [paper-memory-ledger](../paper-memory-ledger/), [manuscript-scorecard](../manuscript-scorecard/)
