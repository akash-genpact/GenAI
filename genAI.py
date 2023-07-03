import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

api_key = os.getenv("API_KEY")
# Set up your API key

# Set the API endpoint and parameters
url = "https://api.deepai.org/api/text-generator"
headers = {
    "api-key": api_key,
    "Content-Type": "application/x-www-form-urlencoded",
}
data = {
    "text": "what is hi",
}

# Send the request
response = requests.post(url, headers=headers, data=data)

# Process the response
if response.status_code == 200:
    result = response.json()
    generated_text = result["output"]
    print("Generated Text:")
    print(generated_text)
else:
    print("Error:", response.status_code)
    print(response.text)
