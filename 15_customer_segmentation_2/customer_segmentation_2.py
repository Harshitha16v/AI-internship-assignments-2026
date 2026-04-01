import numpy as np
from sklearn.cluster import KMeans
print("=== Customer Segmentation System ===")
data = np.array([
    [25, 30000, 40],
    [30, 50000, 60],
    [22, 20000, 20],
    [35, 80000, 90],
    [28, 45000, 70],
    [40, 90000, 95],
    [23, 25000, 30]
])
model = KMeans(n_clusters=3, random_state=0)
model.fit(data)
age = int(input("Enter Age: "))
income = int(input("Enter Annual Income: "))
spending = int(input("Enter Spending Score (1-100): "))
group = model.predict([[age, income, spending]])
print("\n--- Result ---")
print("Cluster Number:", group[0])
if group[0] == 0:
    print("Customer Type: Budget Customer")
    print("Behavior: Low income & low spending")
elif group[0] == 1:
    print("Customer Type: Regular Customer")
    print("Behavior: Balanced income & spending")
else:
    print("Customer Type: Premium Customer")
    print("Behavior: High income & high spending")
print("----------------------")
