import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_bird_strike_dataset.csv")

# Impact Force Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Impact_Force"], bins=30)

plt.title("Impact Force Distribution")
plt.xlabel("Impact Force")
plt.ylabel("Frequency")

plt.savefig("../results/impact_force_distribution.png")
plt.close()

# Risk Level Distribution
risk_counts = df["Risk_Level"].value_counts()

plt.figure(figsize=(6,4))
risk_counts.plot(kind="bar")

plt.title("Risk Level Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Count")

plt.savefig("../results/risk_level_distribution.png")
plt.close()

print("Graphs generated successfully!")