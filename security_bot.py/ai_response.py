# ai_response.py
import re
import google.generativeai as genai

def clean_text_for_speech(text):
    # Remove markdown formatting like **bold**, *italics*, `code`, and bullet points
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"`(.*?)`", r"\1", text)
    text = re.sub(r"[•*]", " ", text)
    return text.strip()

def friday_ai_response(prompt: str) -> str:
    try:
        api_key = "AIzaSyDl1PaqSwCjBWr_OojVWvhKX1DGex9dKII"
        genai.configure(api_key=api_key)

        # Use the supported Gemini model
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)

        # Clean the text for speech output
        cleaned_response = clean_text_for_speech(response.text)
        return cleaned_response

    except Exception as e:
        return f"Something went wrong: {e}"
