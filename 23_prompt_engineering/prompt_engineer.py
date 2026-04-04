print("=== Prompt Quality Analyzer ===")

prompt = input("Enter your prompt: ").lower()

score = 0

# simple checks
if len(prompt) > 20:
    score += 1

if "detailed" in prompt or "step by step" in prompt:
    score += 1

if "example" in prompt or "format" in prompt:
    score += 1

print("\n--- Analysis ---")

if score == 3:
    print("Strong Prompt ✅")
elif score == 2:
    print("Good Prompt 👍")
else:
    print("Weak Prompt ❌")