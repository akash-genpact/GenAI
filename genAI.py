import requests

# Set up your API key
api_key = "50cb01a0-0553-48da-bf72-48e7ba853673"

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
