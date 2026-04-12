print("=== Detection Brainstorm System ===")

print("\nChoose Detection Application:")
print("1. Face Unlock")
print("2. Security Surveillance")
print("3. Self-Driving Cars")
print("4. Attendance System")
print("5. Medical Analysis")

choice = input("\nEnter your choice (1-5): ")

print("\n--- Result ---")

if choice == "1":
    print("Face Unlock: Detects face to unlock mobile securely.")
elif choice == "2":
    print("Security Surveillance: Detects suspicious activity using cameras.")
elif choice == "3":
    print("Self-Driving Cars: Detects vehicles, people, and traffic signals.")
elif choice == "4":
    print("Attendance System: Uses face detection to mark attendance.")
elif choice == "5":
    print("Medical Analysis: Detects diseases from medical images.")
else:
    print("Invalid choice")

print("\n--- Smart System Design ---")

print("System: Face Recognition Attendance")
print("Steps:")
print("1. Capture image")
print("2. Detect face")
print("3. Match with database")
print("4. Mark attendance automatically")
