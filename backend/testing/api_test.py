import requests
import json

url = 'http://127.0.0.1:5000/recommend'
headers = {'Content-Type': 'application/json'}
data = {"message": "Hello, I'm looking for a movie recommendation. I enjoy films that are both thrilling and thought-provoking..."}

response = requests.post(url, headers=headers, data=json.dumps(data))

print('Status Code:', response.status_code)
print('Response Body:', response.text)  # This will print the raw response body

# Only try to decode the response if it's successful and not empty
if response.status_code == 200 and response.text:
    print(response.json())
else:
    print('Failed to get a valid JSON response.')
