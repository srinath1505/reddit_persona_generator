
import os

def extract_username(url):
    return url.strip("/").split("/")[-1]

def save_output(username, content):
    os.makedirs("output", exist_ok=True)
    with open(f"output/{username}.txt", "w", encoding="utf-8") as f:
        f.write(content)
