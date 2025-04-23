import subprocess

def ask_mistral(prompt):
    try:
        process = subprocess.Popen(
            ["ollama", "run", "mistral"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8'
        )

        stdout, stderr = process.communicate(input=prompt, timeout=60)

        if stderr:
            return f"⚠️ Error: {stderr.strip()}"
        return stdout.strip()

    except subprocess.TimeoutExpired:
        return "⚠️ Mistral took too long to respond. Try a shorter prompt or check your system."
    except Exception as e:
        return f"❌ Error talking to Mistral: {str(e)}"

if __name__ == "__main__":
    print("🧠 Smart Business Hub – Mistral Chat\n(Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = ask_mistral(user_input)
        print("Mistral:", response)
