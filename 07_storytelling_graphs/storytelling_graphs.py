import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G"],
    "StudyHours": [2, 4, 5, 6, 3, 7, 8],
    "Marks": [50, 65, 70, 80, 60, 90, 95]
}
df = pd.DataFrame(data)
# -------- BAR CHART --------
plt.figure(figsize=(6,4))
plt.bar(df["Student"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()
# -------- PIE CHART --------
plt.figure(figsize=(6,4))
plt.pie(df["StudyHours"], labels=df["Student"], autopct="%1.1f%%")
plt.title("Study Hours Distribution")
plt.show()
# -------- HISTOGRAM --------
plt.figure(figsize=(6,4))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
print("\nData Story:")
print("Students who study more hours tend to score higher marks.")
print("The histogram shows most marks are between 60 and 90.")
print("This suggests a positive relationship between study time and performance.")