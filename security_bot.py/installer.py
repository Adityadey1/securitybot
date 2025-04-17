# import dns.resolver
# print("✅ Pandas is installed and working!")

# import pandas as pd

# file_path = r"E:\mycode\AI.py\rockyou.txt"

# # Read passwords and store in a list
# with open(file_path, "r", encoding="latin-1") as file:
#     passwords = list(set(file.read().splitlines()))  # Remove duplicates

# # Filter out short passwords (less than 4 characters)
# cleaned_passwords = [pwd for pwd in passwords if len(pwd) >= 4]

# print(f"Total passwords after cleaning: {len(cleaned_passwords)}")
# import string

# # Feature extraction function
# def extract_features(password):
#     length = len(password)
#     digits = sum(c.isdigit() for c in password)
#     uppercase = sum(c.isupper() for c in password)
#     special_chars = sum(c in string.punctuation for c in password)
#     return [length, digits, uppercase, special_chars]

# # Convert passwords to feature vectors
# password_features = [extract_features(pwd) for pwd in cleaned_passwords]

# # Create a DataFrame
# df = pd.DataFrame(password_features, columns=["Length", "Digits", "Uppercase", "SpecialChars"])

# print(df.head())  # Show first few rows
# # Function to assign strength labels
# def label_strength(password):
#     length, digits, uppercase, special_chars = extract_features(password)

#     if length <= 6 and digits == 0 and special_chars == 0:
#         return 0  # Weak
#     elif length >= 10 and digits > 0 and uppercase > 0 and special_chars > 0:
#         return 2  # Strong
#     else:
#         return 1  # Moderate

# # Apply labels
# labels = [label_strength(pwd) for pwd in cleaned_passwords]

# # Add labels to DataFrame
# df["Strength"] = labels

# print(df["Strength"].value_counts())  # Check class distribution
# from sklearn.model_selection import train_test_split

# # Split data (80% training, 20% testing)
# X_train, X_test, y_train, y_test = train_test_split(df[["Length", "Digits", "Uppercase", "SpecialChars"]], df["Strength"], test_size=0.2, random_state=42)

# print(f"Training data: {X_train.shape}, Testing data: {X_test.shape}")
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # Initialize and train the model
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Test the model
# y_pred = model.predict(X_test)

# # Evaluate accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Gemini Key:", os.getenv("AIzaSyDl1PaqSwCjBWr_OojVWvhKX1DGex9dKII"))



