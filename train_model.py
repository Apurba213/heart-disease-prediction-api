
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 1. Load dataset
df = pd.read_csv("data/heart.csv")

# 2. Separate input and target
X = df.drop("target", axis=1)
y = df["target"]

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 4. Create ML pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=2000))
])

# 5. Train model
model.fit(X_train, y_train)

# 6. Evaluate model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model accuracy:", accuracy)

# 7. Save model
joblib.dump(model, "model/heart_model.joblib")

print("Model saved successfully!")
