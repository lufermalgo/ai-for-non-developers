# Product Owner Prompting Guide

To get the most out of your **AI Engineering Partner**, you need to stop thinking like a "coder" and start thinking like a **Product Owner**.

## The Golden Rule

**Describe the problem, the goal, and the experience. Never describe the code.**

---

## 1. Defining New Features

Instead of giving technical instructions, describe the user's journey.

* **Bad:** "Add a database field for 'age' and an input in the HTML."
* **Good:** "We need to know the user's age to customize the content recommendations. Make sure the registration flow captures this smoothly."

## 2. Managing Technical Errors

When something breaks, don't try to debug it yourself. Report the "symptoms."

* **Bad:** "I think you need to import the library in line 15."
* **Good:** "The 'Submit' button isn't doing anything when I click it. Can you check the logs and see what's happening?"

## 3. Guiding the Aesthetic

Use descriptive words about the "feel" of the application.

* **Bad:** "Make the hex color #0000FF and use Arial font."
* **Good:** "The design should feel professional, like a modern banking app. Use a dark mode with subtle neon accents."

## 4. The "Command List"

Your AI understands specific "high-level" commands that trigger autonomous behaviors:

* **"Replan"**: Use this when the AI is stuck. It forces a pause and a new strategy.
* **"Audit"**: Ask the AI to audit its own code for security or token efficiency.
* **"Explain like I'm a founder"**: If you don't understand what's happening, use this to get a business-level summary.

## 5. Token Efficiency Tips

You don't need to worry about the technical details, but you can help save your credits:

* **Batch your feedback**: Instead of sending 5 short messages, send one message with 5 points.
* **Trust the `task.md`**: You don't need to ask "What's next?" every time. The AI updates the task list automatically.

---

**Remember:** You are the visionary. Your Engineering Partner is here to handle the complexity.
