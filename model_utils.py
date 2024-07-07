import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier as gbc
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# Load your dataset
df = pd.read_csv("C:/Users/win10/Downloads/archive/The_Cancer_data_1500_V2.csv")

# Drop any null values if present
df = df.dropna()

# Define X and y
X, y = df.drop("Diagnosis", axis=1), df["Diagnosis"]

# Split data into training and testing sets
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate Gradient Boosting Classifier
model = gbc(random_state=42)
model.fit(Xtrain, ytrain)
ypred = model.predict(Xtest)

# Calculate metrics
gbc_acc = accuracy_score(ytest, ypred) * 100
gbc_precision = precision_score(ytest, ypred, average='weighted')
gbc_recall = recall_score(ytest, ypred, average='weighted')
gbc_f1 = f1_score(ytest, ypred, average='weighted')

# Print metrics
print(f"GradientBoostingClassifier Accuracy: {gbc_acc:.2f}%")
print(f"GradientBoostingClassifier Precision: {gbc_precision:.2f}")
print(f"GradientBoostingClassifier Recall: {gbc_recall:.2f}")
print(f"GradientBoostingClassifier F1 Score: {gbc_f1:.2f}\n")

# Save the trained model using pickle
model_filename = 'gbc_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

# Load the model back from the pickle file
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Test loading the model by making predictions (optional)
# Example usage:
# ypred_loaded = loaded_model.predict(Xtest)
# Check performance metrics if needed
