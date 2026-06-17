bird_weight = float(input("Enter Bird Weight (kg): "))
aircraft_speed = float(input("Enter Aircraft Speed (km/h): "))

impact_force = 0.5 * bird_weight * (aircraft_speed ** 2)

print(f"\nImpact Force: {impact_force:.2f}")

if impact_force < 15000:
    risk = "Low"
elif impact_force < 50000:
    risk = "Medium"
else:
    risk = "High"

print(f"Predicted Risk Level: {risk}")