
import requests
from bs4 import BeautifulSoup

def scrape_user_content(username):
    base_url = f"https://www.reddit.com/user/{username}/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    posts, comments = [], []

    for kind in ["posts", "comments"]:
        url = f"{base_url}{kind}/"
        try:
            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")
            elements = soup.find_all("p")
            content = [el.text.strip() for el in elements if el.text.strip()]
            if kind == "posts":
                posts.extend(content)
            else:
                comments.extend(content)
        except Exception as e:
            print(f"[!] Error scraping {kind} for {username}: {e}")

    return posts, comments
