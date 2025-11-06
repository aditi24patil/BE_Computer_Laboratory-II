# ------------------------------------------------------------
# Simple Genomic Data Classification using ML Models
# ------------------------------------------------------------

# Import required libraries
import numpy as np                     # For numerical computations and creating random data
import pandas as pd                    # For handling tabular data (not used much here, but good to include)
from sklearn.model_selection import train_test_split   # For splitting data into training and testing sets
from sklearn.ensemble import RandomForestClassifier    # Random Forest model
from sklearn.svm import SVC                            # Support Vector Machine model
from sklearn.metrics import accuracy_score             # To calculate model accuracy
import matplotlib.pyplot as plt                        # For plotting graph

# ------------------------------------------------------------
# Step 1: Create a Simulated Genomic Dataset
# ------------------------------------------------------------

np.random.seed(42)          # Fix random seed for reproducibility (same random values every time)
X = np.random.rand(1000, 10)  # Generate 1000 samples, each with 10 gene marker values (features)
y = np.random.randint(0, 2, 1000)  # Generate labels (0 or 1), representing two classes (e.g., healthy/diseased)

# ------------------------------------------------------------
# Step 2: Split Dataset into Training and Testing Sets
# ------------------------------------------------------------

# 70% for training, 30% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ------------------------------------------------------------
# Step 3: Train a Random Forest Classifier
# ------------------------------------------------------------

rf = RandomForestClassifier(n_estimators=100, random_state=42)  # Create Random Forest model with 100 trees
rf.fit(X_train, y_train)      # Train model using training data
rf_pred = rf.predict(X_test)  # Predict labels for test data
rf_acc = accuracy_score(y_test, rf_pred)  # Calculate accuracy score

# ------------------------------------------------------------
# Step 4: Train a Support Vector Machine (SVM) Classifier
# ------------------------------------------------------------

svm = SVC(kernel='linear')    # Create SVM model using linear kernel
svm.fit(X_train, y_train)     # Train SVM model
svm_pred = svm.predict(X_test) # Predict test data
svm_acc = accuracy_score(y_test, svm_pred)  # Calculate accuracy score

# ------------------------------------------------------------
# Step 5: Print Accuracy Results
# ------------------------------------------------------------

print("Random Forest Accuracy:", round(rf_acc, 3))  # Print Random Forest accuracy (rounded to 3 decimals)
print("SVM Accuracy:", round(svm_acc, 3))           # Print SVM accuracy

# ------------------------------------------------------------
# Step 6: Visual Comparison using Bar Graph
# ------------------------------------------------------------

models = ["Random Forest", "SVM"]    # List of model names
accuracies = [rf_acc, svm_acc]       # List of accuracy scores

plt.bar(models, accuracies, color=['green', 'orange'])  # Plot bar graph of model accuracies
plt.ylabel("Accuracy")             # Label for Y-axis
plt.title("Model Comparison for Genomic Classification")  # Title of the graph
plt.show()                         # Display the plot
