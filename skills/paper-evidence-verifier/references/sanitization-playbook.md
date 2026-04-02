# Sanitization Playbook

When the verifier finds unsupported values, use these recovery actions.

## Tables

- Replace unsupported result cells with `---` or another explicit placeholder
- Do not silently swap in a guess
- Skip sanitization for pure hyperparameter tables or derived-statistics tables when those values are not supposed to be in the raw metric registry

## Prose

- Remove unsupported exact numbers
- Rewrite to qualitative language only if the qualitative statement is still supported
- If the claim itself is unsupported, delete the sentence instead of weakening it cosmetically

## Conditions and Baselines

- Remove condition names that never existed in the experiment run
- Align paper terminology to the actual whitelist of condition names used in the results

## Best Practice

- Prefer generating result tables directly from verified summaries
- Feed the verified tables into the writing process as immutable artifacts
- Keep the experiment summary that represents the promoted best or final run as the only ground-truth source
