import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("network_intrusion.csv")

# -------------------------------
# Preprocessing
# -------------------------------
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# -------------------------------
# Models
# -------------------------------
dt = DecisionTreeClassifier()
rf = RandomForestClassifier(n_estimators=100)

dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

y_pred_dt = dt.predict(X_test)
y_pred_rf = rf.predict(X_test)

# -------------------------------
# Metrics
# -------------------------------
acc_dt = accuracy_score(y_test, y_pred_dt)
acc_rf = accuracy_score(y_test, y_pred_rf)

print("Decision Tree Accuracy:", acc_dt)
print("Random Forest Accuracy:", acc_rf)

# -------------------------------
# 1. Accuracy Comparison Plot
# -------------------------------
models = ["Decision Tree", "Random Forest"]
accuracies = [acc_dt, acc_rf]

plt.figure()
plt.bar(models, accuracies)
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.show()

# -------------------------------
# 2. Confusion Matrix Plot
# -------------------------------
cm_dt = confusion_matrix(y_test, y_pred_dt)
cm_rf = confusion_matrix(y_test, y_pred_rf)

plt.figure()
plt.imshow(cm_dt)
plt.title("Decision Tree Confusion Matrix")
plt.colorbar()
plt.show()

plt.figure()
plt.imshow(cm_rf)
plt.title("Random Forest Confusion Matrix")
plt.colorbar()
plt.show()

# -------------------------------
# 3. Feature Importance (RF)
# -------------------------------
importances = rf.feature_importances_

plt.figure()
plt.bar(range(len(importances)), importances)
plt.title("Feature Importance (Random Forest)")
plt.xlabel("Feature Index")
plt.ylabel("Importance")
plt.show()












logs = ["login", "fail", "fail", "fail", "success"]

if logs.count("fail") > 2:
    print("Intrusion Detected!")
else:
    print("Normal Activity")
