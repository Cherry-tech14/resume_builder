import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: Gemini API key not found.")

else:
    client = genai.Client(api_key=api_key)

    for attempt in range(3):
        try:
            print(f"Attempt {attempt + 1}: Connecting to Gemini...", flush=True)

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents="Write a short professional summary for a beginner Python developer."
            )

            print("\nAI Generated Summary:")
            print(response.text)
            break

        except errors.ServerError as error:
            if error.code == 503 and attempt < 2:
                print("Gemini is busy. Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Gemini server error:", error)
                break

        except Exception as error:
            print("Gemini API error:", error)
            break