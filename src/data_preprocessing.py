import pandas as pd

df = pd.read_csv("../data/bird_strike_dataset.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nRisk Distribution:")
print(df["Risk_Level"].value_counts())

df.to_csv("../data/cleaned_bird_strike_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")