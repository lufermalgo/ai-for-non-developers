# REVIEW_MODE.md

## Purpose

Produce code that can survive review by senior engineers.

## Review Expectations

Optimize for:

- readability
- modularity
- naming clarity
- maintainability
- consistency
- low surprise factor
- reasonable scalability
- explicit error handling
- testability
- minimal technical debt

## Before Finalizing

Check for:

- unnecessary complexity
- duplicated logic
- hidden side effects
- poor naming
- tight coupling
- dead code
- regression risk
- broken contracts
- weak validation

## Diff Quality

Prefer clean, reviewable changes.

- small diffs
- focused scope
- no unrelated edits
- preserve style of repo

## If Tradeoff Exists

Prefer maintainability over cleverness.
Prefer clarity over micro-optimization unless performance is required.