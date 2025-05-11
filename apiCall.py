import requests
url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
payload = {
    "name": "Mohd Umar Ansari",
    "regNo": "REG12347",
    "email": "umaransari220457@acropolis.in"
}
response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response Body:", response.json())