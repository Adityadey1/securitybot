from dotenv import load_dotenv
import os
import google.generativeai as genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Debug print to check if API key is loaded
print("Gemini Key:", os.getenv("GEMINI_API_KEY"))

# Step 3: Configure Gemini with the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Step 4: Initialize the model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Step 5: Send a prompt to the model
response = model.generate_content("Hello Gemini! What can you do?")

# Step 6: Print the response
print("AI Response:", response.text)
