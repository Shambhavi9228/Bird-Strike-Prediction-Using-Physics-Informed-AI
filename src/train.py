import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/cleaned_bird_strike_dataset.csv")

# Features
X = df[["Bird_Weight", "Aircraft_Speed", "Impact_Force"]]

# Target
le = LabelEncoder()
y = le.fit_transform(df["Risk_Level"])

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
plt.imshow(cm)

plt.title("Confusion Matrix")
plt.colorbar()

plt.savefig("../results/confusion_matrix.png")
plt.close()

print("Model training completed successfully!")