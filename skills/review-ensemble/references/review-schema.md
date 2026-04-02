# Review Schema

The AI Scientist review loop uses a structured review object with these fields:

- `Summary`
- `Strengths`
- `Weaknesses`
- `Originality` from 1 to 4
- `Quality` from 1 to 4
- `Clarity` from 1 to 4
- `Significance` from 1 to 4
- `Questions`
- `Limitations`
- `Ethical Concerns` as boolean
- `Soundness` from 1 to 4
- `Presentation` from 1 to 4
- `Contribution` from 1 to 4
- `Overall` from 1 to 10
- `Confidence` from 1 to 5
- `Decision` as `Accept` or `Reject`

## Score Intent

- `Soundness`: are the claims actually supported?
- `Presentation`: can a reviewer follow the paper without guesswork?
- `Contribution`: is the work worth sharing with the target community?
- `Confidence`: how certain is the reviewer about the assessment?

The schema is useful because it forces review output into revision-ready buckets instead of loose prose.
