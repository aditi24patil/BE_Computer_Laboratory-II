# Simple Inverted Index for Document Retrieval
# Aim: To find documents that contain the given query words

# Step 1: Create a small collection of documents
docs = {
    1: "Heart disease prevention and healthy diet",
    2: "Spam emails contain phishing links",
    3: "Exercise reduces heart risk"
}

# Step 2: Build the inverted index (word → document IDs)
index = {}  # empty dictionary to store word-to-document mapping

# Loop through each document
for doc_id, text in docs.items():
    # Convert text to lowercase and split into words
    for word in text.lower().split():
        # Add document ID to the word entry in the index
        # setdefault() ensures the word key exists, and .add(doc_id) adds the current doc ID
        index.setdefault(word, set()).add(doc_id)

# Step 3: Take a query from the user
query = input("Enter query: ").lower().split()  # convert query to lowercase and split into words

# Step 4: Find documents that contain all query words
result = set(docs.keys())  # start with all document IDs
for word in query:
    # Keep only those document IDs that contain the word
    result &= index.get(word, set())

# Step 5: Print the result
print("Documents found:", result)
