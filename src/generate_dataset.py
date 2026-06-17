import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

bird_weight = np.random.uniform(0.5, 8.0, n)  # kg
aircraft_speed = np.random.uniform(150, 350, n)  # km/h

# Physics-based impact force
impact_force = 0.5 * bird_weight * (aircraft_speed ** 2)

risk = []

for force in impact_force:
    if force < 15000:
        risk.append("Low")
    elif force < 50000:
        risk.append("Medium")
    else:
        risk.append("High")

df = pd.DataFrame({
    "Bird_Weight": bird_weight,
    "Aircraft_Speed": aircraft_speed,
    "Impact_Force": impact_force,
    "Risk_Level": risk
})

df.to_csv("../data/bird_strike_dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())