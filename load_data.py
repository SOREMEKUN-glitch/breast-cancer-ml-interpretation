import pandas as pd
from sklearn.datasets import load_breast_cancer

# load dataset from sklearn
data = load_breast_cancer()

# convert to dataframe
df = pd.DataFrame(data.data, columns=data.feature_names)

# add target column
df["target"] = data.target

# preview
print(df.head())
print("Shape:", df.shape)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

print("\nTarget distribution:")
print(df["target"].value_counts())

# features (everything except target)
X = df.drop("target", axis=1)

# target (only diagnosis)
y = df["target"]

print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LogisticRegression

# create model
model = LogisticRegression(max_iter=5000)

# train the model
model.fit(X_train, y_train)
# predict diagnosis for unseen patients
y_pred = model.predict(X_test)

print(y_pred[:10])
print(y_test[:10].values)

# Evaluating the model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification report:")
print(classification_report(y_test, y_pred))

#  Coefficient code
import pandas as pd
print('='*50)
print('Coefficient code')
print('='*50)

coefficients = pd.Series(model.coef_[0], index=X.columns)
coefficients = coefficients.sort_values()

print(coefficients.tail(10))

# visualization
import matplotlib.pyplot as plt

print("✅ Reached plotting section")

# get coefficients
coefficients = pd.Series(model.coef_[0], index=X.columns)

# select top 10 most important features
top_features = coefficients.abs().sort_values(ascending=False).head(10).index
top_coefficients = coefficients[top_features]

# create figure
fig, ax = plt.subplots(figsize=(8,5))
top_coefficients.sort_values().plot(kind="barh", ax=ax)

ax.set_title("Most Influential Measurements in Prediction")
ax.set_xlabel("Coefficient Value")

plt.tight_layout()

# save clean PNG
plt.savefig("feature_importance.png", format="png", dpi=300)

# close figure completely (important)
plt.close(fig)

print("✅ Saved feature_importance.png")

