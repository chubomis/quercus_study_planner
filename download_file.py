import requests
import os

def download_file(url, folder_name, file_name, headers):
    file_path = f"{folder_name}/{file_name}"

    resp = requests.get(url, headers=headers)
    with open(file_path, "wb") as f:
        f.write(resp.content)
        print("Saved as: ", file_name)