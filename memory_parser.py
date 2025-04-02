import os

def load_memory(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def save_memory(filepath, memory):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(memory))

def forget_last_session(filepath):
    memory = load_memory(filepath)
    if not memory:
        return
    # Remove from the last user input backward
    for i in range(len(memory) - 1, -1, -1):
        if memory[i].startswith("You: "):
            memory = memory[:i]
            break
    save_memory(filepath, memory)

def parse_memory_file(filepath, aggressive=False):
    memory = load_memory(filepath)

    if aggressive and len(memory) > 20:
        # Keep only the last 10 exchanges if aggressive
        new_memory = []
        user_turns = 0
        for line in reversed(memory):
            if line.startswith("You:"):
                user_turns += 1
            new_memory.insert(0, line)
            if user_turns >= 10:
                break
        memory = new_memory
    elif len(memory) > 100:
        # Light trimming: keep last 100 lines max
        memory = memory[-100:]

    save_memory(filepath, memory)
# need to change all of this to JSON 