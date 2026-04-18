# Quick Start Guide

Welcome to the **AI Engineering Partner** framework. This guide will help you set up your professional environment in minutes, even if you've never written a line of code.

## 1. Installation

1. **Open your Terminal** (on Mac, press `Command + Space` and type "Terminal").
2. **Navigate to your project folder** or create a new one.
3. **Run the installer script** from this repository:

   ```bash
   curl -sSL https://raw.githubusercontent.com/lufermalgo/ai-for-non-developers/main/cli/install.sh | bash
   ```

   *Note: This script will ask you which AI tool you are using (Antigravity, Claude Code, etc.) to configure the rules correctly.*

## 2. Your First Action

Open your AI assistant in the project folder and start the conversation. You don't need to fill out forms. Just tell your story:

> "I have an idea for an app that helps home gardeners track their plants. I don't know anything about programming, but I know how I want it to look. Can we start planning?"

## 3. What to Expect

The AI will automatically perform the following steps:

1. **Discovery**: It will ask you 2-3 key questions to understand the scope.
2. **Infrastructure**: It will create the `.aind/` directory to store your project's context, vision, and technical progress, keeping your project root clean.
3. **Execution**: It will start building, showing you progress and asking for feedback only when necessary.

## 4. Key Rules for the Product Owner (You)

* **Trust the Engineer**: The AI knows the best languages and tools for your project. Let it choose.
* **Focus on the "Wait"**: If the AI finishes a task, test it. If it doesn't work, tell it what's wrong, not how to fix it.
* **Check the Logs**: If you're curious about progress, look at the `.aind/tasks.md` file in your project.

## 5. Supported Platforms

This framework works best with assistants that can:

1. Read and write files directly.
2. Run commands in your terminal (with your permission).
3. Maintain a "long-term memory" of the project.

**Are you ready? Let's build something amazing.**
