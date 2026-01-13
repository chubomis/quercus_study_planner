import requests
from bs4 import BeautifulSoup
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

# for course in courses:
#     id = course.get("id")
#     name = course.get("name") or course.get("course_code")
#     print(id,  name)

csc311_id = 416373

csc311_r = requests.get(f"{BASE}/courses/{csc311_id}/front_page", 
                        headers=headers)
csc311_page = csc311_r.json()
html = csc311_page["body"]

soup = BeautifulSoup(html, "lxml")

table = soup.find("table")

rows = table.find_all("tr")


for row in rows:
    cells = row.find_all("td")
    cell_text = [cell.get_text(strip=True) for cell in cells]
    print(cell_text)