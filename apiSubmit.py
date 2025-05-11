import requests
url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON'"
access_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IlJFRzEyMzQ3IiwibmFtZSI6Ik1vaGQgVW1hciBBbnNhcmkiLCJlbWFpbCI6InVtYXJhbnNhcmkyMjA0NTdAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYyNTQ5LCJleHAiOjE3NDY5NjM0NDl9.JYM0I5krOUCbNQJOxMUVmJ1iqfJlAVzlYZF32TgBw3c"
final_query = """
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
    d.DEPARTMENT_NAME
FROM 
    PAYMENTS p
JOIN 
    EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN 
    DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE 
    DAY(p.PAYMENT_TIME) <> 1
ORDER BY 
    p.AMOUNT DESC
LIMIT 1;
"""
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}
body = {
    "finalQuery": final_query
}
response = requests.post(url, json=body, headers=headers)
print("Status Code:", response.status_code)
print("Response Body:", response.text)