import pandas as pd
import random
data = []
for i in range(20):
    study_hours = random.randint(1, 10)
    marks = study_hours * 10 + random.randint(-5, 5)
    data.append({
        "StudyHours": study_hours,
        "Marks": marks
    })
df = pd.DataFrame(data)
print("\nGenerated Dataset:\n")
print(df)
df.to_csv("study_hours_vs_marks.csv", index=False)
print("\nDataset saved as study_hours_vs_marks.csv")
print("\nFeature: StudyHours")
print("Label: Marks")
print("\nRelationship:")
print("More study hours generally lead to higher marks.")