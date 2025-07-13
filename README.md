Reddit User Persona Generator - GitHub README

📌 Features
- ✅ Scrapes Reddit posts and comments from any public profile
- ✅ Supports batch processing of multiple usernames
- ✅ Builds a structured user persona with:
- Demographics
- Personality (MBTI & tone)
- Motivations & frustrations
- Goals, habits, and direct citations
- ✅ Uses Gemini LLM (Google Generative AI) for insight generation
- ✅ Fully PEP-8 compliant and documented

📂 Directory Structure
reddit_persona_generator/
├── main.py                # Entry point, CLI parser
├── scraper.py             # Scrapes Reddit profile
├── persona.py             # 🔥 Detailed persona prompt 
├── utils.py               # Helper methods
├── usernames.txt          # List of Reddit URLs for batch mode
├── output/                # Output text files for each persona( Sample outputs are given for 2 users)
├── .env                   # Environment file for API keys
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

⚙️ Installation
1. Clone this repo:

git clone https://github.com/srinath1505/reddit_persona_generator.git
cd reddit_persona_generator

2. Install Python packages:

pip install -r requirements.txt

3. Set up Gemini API:

- Go to https://makersuite.google.com/app/apikey
- Copy your API key and add it to `.env`:

GEMINI_API_KEY=your_real_key_here

🚀 Usage
👉 Single user mode:

python main.py -u https://www.reddit.com/user/kojied/

👉 Batch mode:

Put profile URLs (one per line) in `usernames.txt`, then run:

python main.py -f usernames.txt

🧠 LLM Integration
Uses the Gemini model:
models/gemini-1.5-flash-latest

🛠 Technologies Used
- Python 3.10+
- Google Generative AI (Gemini)
- BeautifulSoup + Requests (for scraping)
- dotenv + argparse + tqdm

👨‍💻 Author
Srinath Selvakumar
📫 LinkedIn | GPT, LLMs, Robotics & Healthcare AI
📜 License
This project is for evaluation purposes only and not intended for production use.
