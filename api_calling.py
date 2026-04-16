from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def issue_generator(images, options):
    prompt = f"Debug the code and explain the possible issue. No solutions"
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt],
    )

    return response.text
    
    
def solution_generator(images, options):
    prompt = f"Debug the code and provide {options} only. Provide explanation only if it says solution with code."
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt],
    )

    return response.text