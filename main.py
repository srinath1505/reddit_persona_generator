
import argparse
from scraper import scrape_user_content
from persona import generate_persona
from utils import extract_username, save_output
import os
from tqdm import tqdm

def process_user(url):
    username = extract_username(url)
    posts, comments = scrape_user_content(username)
    persona = generate_persona(username, posts, comments)
    save_output(username, persona)
    print(f"[✓] Saved persona for {username}")

def main():
    parser = argparse.ArgumentParser(description="Reddit Persona Generator")
    parser.add_argument("-u", "--user", help="Reddit user profile URL")
    parser.add_argument("-f", "--file", help="Path to file containing list of profile URLs")
    args = parser.parse_args()

    urls = []
    if args.user:
        urls = [args.user]
    elif args.file and os.path.exists(args.file):
        with open(args.file, 'r') as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]

    if not urls:
        print("No valid input provided. Use -u or -f.")
        return

    for url in tqdm(urls, desc="Processing Users"):
        process_user(url)

if __name__ == "__main__":
    main()
