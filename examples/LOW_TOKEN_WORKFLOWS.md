# LOW_TOKEN_WORKFLOWS.md

## Core Rule

One session = one main objective.

## Bug Fix Workflow

1. Infer likely root cause
2. Inspect smallest relevant scope
3. Apply minimal safe fix
4. Self-check
5. Return concise test request

## Feature Workflow

1. Infer intent
2. Reuse existing patterns
3. Build smallest complete version
4. Self-check
5. Return validation request

## Refactor Workflow

1. Identify exact pain
2. Keep behavior unchanged
3. Improve structure only where needed
4. Self-check
5. Return done

## Debug Workflow

1. Rank top likely causes
2. Validate highest probability first
3. Fix
4. Re-test

## Large Repo Workflow

- search before opening files
- inspect narrow scope first
- avoid scanning entire repo
- reuse prior context
- skip irrelevant directories

## Session Reset Workflow

When task changes significantly:

1. Summarize decisions
2. Start fresh session
3. Continue with clean scope