# Documentation

Welcome to the AI for Non-Developers documentation. Here you'll find guides and examples to help you get the most out of this framework.

## Getting Started

- **[Quickstart](quickstart.md)** – Set up the framework and run your first project
- **[Prompting Guide](prompting-guide.md)** – How to communicate with AI effectively (the product owner way)

## Concepts & Patterns

- **[CLAUDE_EXAMPLE.md](CLAUDE_EXAMPLE.md)** – Example CLAUDE.md file showing best practices for Claude Code projects
- **[NATURAL_PROMPTS.md](NATURAL_PROMPTS.md)** – How to phrase requests naturally, not technically
- **[LOW_TOKEN_WORKFLOWS.md](LOW_TOKEN_WORKFLOWS.md)** – Strategies to maximize efficiency with your AI tool

## Specialized Workflows

- **[FOUNDER_MODE.md](FOUNDER_MODE.md)** – For founders and product-focused leaders
- **[REVIEW_MODE.md](REVIEW_MODE.md)** – How to review and validate AI-generated work

## Project Structure

After running the installer, your project will have:

```
your-project/
├── .aind/              # AI agent state (auto-generated)
│   ├── context.md      # Project vision and decisions
│   ├── roadmap.md      # Milestones and progress
│   ├── tasks.md        # Current work items
│   ├── lessons.md      # Learnings and patterns
│   └── handover.md     # Session handoff info
├── specs/              # Feature specifications
├── CLAUDE.md           # Your AI instructions (customize this)
└── README.md           # Your project README
```

## Tips for Success

1. **Invest in your CLAUDE.md** – The better you define your preferences and constraints, the better the AI works.
2. **Use `.aind/`** – Check `tasks.md` and `context.md` to understand project state.
3. **Be a product owner** – Focus on the "what" and "why," let the AI handle the "how."
4. **Review before deploying** – Always read generated code and test before using it.

## Need Help?

- Check the [main README](../README.md) for project overview
- Review [CONTRIBUTING.md](../CONTRIBUTING.md) to understand how to contribute
- Open an [issue on GitHub](https://github.com/lufermalgo/ai-for-non-developers/issues) with questions

---

**Ready to build?** Clone the repo and run `./cli/install.sh` to get started!
