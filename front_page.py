import requests
from grab_token import grab_token

BASE = "https://q.utoronto.ca/api/v1"
TOKEN = grab_token()
headers = {"Authorization": f"Bearer {TOKEN}"}

params = {
    "enrollment_state[]": ["active"],
    "per_page": 100
}
r = requests.get(f"{BASE}/courses", headers=headers, params=params)

if r.status_code != 200:
    print("Error:", r.status_code, r.text)
    exit()

courses = r.json()

for course in courses:
    id = course.get("id")
    name = course.get("name") or course.get("course_code")
    print(id,  name)
