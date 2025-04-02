import os
from memory_parser import (
    load_memory,
    save_memory,
    forget_last_session,
    parse_memory_file
)
from openai_interface import get_response

MEMORY_FILE = "memory.txt"
SYSTEM_PROMPT_FILE = "system_prompt.txt"

def get_system_prompt():
    if not os.path.exists(SYSTEM_PROMPT_FILE):
        return "You are Buzz, an AI assistant. You respond briefly and accurately."
    with open(SYSTEM_PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()

def set_system_prompt(new_prompt):
    with open(SYSTEM_PROMPT_FILE, "w", encoding="utf-8") as f:
        f.write(new_prompt.strip())

def main():
    print("Welcome to Buzzai (LM Studio Mode).")
    memory = load_memory(MEMORY_FILE)

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting Buzzai...")
            break

        if user_input.startswith("!set_system:"):
            new_prompt = user_input.split("!set_system:", 1)[1].strip()
            set_system_prompt(new_prompt)
            print("System prompt updated.")
            continue

        if user_input == "!forget_last":
            forget_last_session(MEMORY_FILE)
            print("Last session forgotten.")
            memory = load_memory(MEMORY_FILE)
            continue

        if user_input == "!forget_session":
            save_memory(MEMORY_FILE, [])
            print("Entire session forgotten.")
            memory = []
            continue

        # Only store input if it's not a command
        if not user_input.startswith("!"):
            memory.append(f"User: {user_input}")

        # Force system prompt into the top of the context
        system_prompt = get_system_prompt()
        filtered_memory = [line for line in memory if not line.startswith("!")]
        prompt = f"{system_prompt}\n\n### Conversation\n" + "\n".join(filtered_memory) + "\nBuzz:"

        # print("\n=== FINAL PROMPT SENT TO MODEL ===\n")
        # print(prompt)
        # print("\n=================================\n")

        response = get_response(prompt)
        print("Buzzai:", response.strip())

        memory.append(f"Buzz: {response.strip()}")
        save_memory(MEMORY_FILE, memory)
        parse_memory_file(MEMORY_FILE, aggressive=False)

if __name__ == "__main__":
    main()
