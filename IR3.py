#IR 3 - Email filtering
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("D:\\BE\\spam.csv")


print("Columns:", data.columns.tolist())
print("Sample rows:")
print(data.head())

# Clean labels and messages
data['Category'] = data['Category'].astype(str).str.strip().str.lower()
data['Message'] = data['Message'].astype(str)

# Keep only rows where label is ham/spam
data = data[data['Category'].isin(['ham', 'spam'])].copy()

# Numeric label
data['Category_num'] = data['Category'].map({'ham': 0, 'spam': 1})

# Drop missing/empty messages
data = data[data['Message'].str.strip() != ''].dropna(subset=['Message', 'Category_num'])

# Train/test split with stratify to keep class proportions
X_train, X_test, y_train, y_test = train_test_split(
    data['Message'],
    data['Category_num'],
    test_size=0.25,
    random_state=42,
    stratify=data['Category_num']
)

# Vectorize
vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)

# Step 7: Test on New Emails
sample_emails = [
    "Congratulations! You have won a $1000 Walmart gift card. Click here to claim now!",
    "Hey, are we still meeting for lunch today?",
    "Your Amazon order has been shipped successfully."
]

sample_vec = vectorizer.transform(sample_emails)
predictions = model.predict(sample_vec)

print("\n🔍 Sample Email Predictions:")
for email, label in zip(sample_emails, predictions):
    print(f"Email: {email}\n→ {'SPAM' if label == 1 else 'HAM'}\n")
