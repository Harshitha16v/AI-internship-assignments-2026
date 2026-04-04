print("=== Break the AI Experiment ===")

prompt = input("Enter tricky prompt: ")
response = input("Enter AI response: ")

print("\n--- Analysis ---")

# simple check
if "wrong" in response.lower() or "confused" in response.lower():
    print("Result: AI got confused ❌")
else:
    print("Result: AI handled it well ✅")

print("\nPrompt Used:", prompt)
print("AI Response:", response)
print("\nTry different prompts to see how the AI responds!")
