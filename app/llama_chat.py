import subprocess

def ask_mistral(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            encoding='utf-8',
            timeout=90  # long enough for good responses
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "⚠️ Mistral took too long to respond. Try a shorter prompt or check your system."
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    print("🧠 Smart Business Hub – Mistral Chat\n(Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = ask_mistral(user_input)
        print("Mistral:", response)
