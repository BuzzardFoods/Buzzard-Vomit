# 🧠 Buzzard Vomit

Buzzard Vomit is a locally run Python-based AI assistant project codenamed **Buzzai**. Inspired by *Accelerando's* Manfred Macx, the goal of Buzzai is to create a lightweight, privacy-focused virtual assistant that works in tandem with **LM Studio**, a local LLM frontend, to simulate memory, perform tasks, etc.

This project is part of a broader vision: to build a virtual companion that understands your habits, keeps track of your goals, and becomes smarter over time — all without sending data to the cloud.

---

## What It Does

- **LM Studio Integration:**  
  Buzzai sends prompts to a local LLM through LM Studio, using its API for fast and private local inference.

- **Simulated Memory System:**  
  Stores sessions with ~~selective memory parsing. Memory is condensed into a base profile and fact archive~~ to simulate long-term context and evolution.

- **Python CLI Core:**  
  Lightweight CLI interface for issuing commands, receiving replies, and managing memory in real-time.

- **Debug Mode & Instruction Handling:**  
  Easily toggle debug mode or use commands like `forget last` to manage context dynamically.

---

##  Planned Features

-  **Window/Program Reading**  
  Allow Buzzai to detect open windows, read selected text, and reply appropriately.

-  **Android Messaging Bridge**  
  Two-way communication with Buzzai using an Android phone for mobile command-and-control.

-  **Smarter Memory Parser**  
  Fine-tuned logic to selectively remember facts, forget junk, and auto-condense at the end of each session.

-  **Text-to-Speech / Voice Command Module**  
  Future additions for full verbal interaction, hands-free usage.

-  **Personality Profiles**  
  Add swappable “modes” or AI personas depending on task or user preference.

---

##  Easier Alternatives

If you're just looking to get LLM responses without custom memory logic:

- **LM Studio (Standalone)**  
  Great GUI to run LLMs locally, without needing to build a wrapper like Buzzai.

- **ChatGPT + Memory**  
  Use OpenAI’s built-in memory (with Plus plan) for automatic context handling and ease of use.

- **Mycroft AI**  
  Voice assistant project with plug-and-play modules (now somewhat outdated but hackable).

- **Auto-GPT or AgentGPT**  
  For those who want goal-based LLM automation without writing Python scripts.

## Buzzard Vomit exists so Buzz can tinker, I am posting it on Github to learn more about how Github works!

