
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Use updated Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def generate_persona(username, posts, comments):
    data = "\n".join(posts + comments)
    prompt = f"""You are a professional user research analyst. Based on the following Reddit posts and comments, generate a detailed user persona in structured form including:

1. **Name** (guess a likely pseudonym or keep it as Reddit username)
2. **Demographics**:
    - Age (approximate)
    - Occupation
    - Marital/Relationship Status
    - Location (approximate, if detectable)
    - Personality Archetype (e.g., The Creator, The Explorer)

3. **Personality Traits**:
    - Use MBTI dimensions (Introvert/Extrovert, Intuition/Sensing, Feeling/Thinking, Judging/Perceiving)
    - Additional traits like tone (sarcastic, optimistic, intellectual), communication style, etc.

4. **Behavior & Habits**:
    - Online habits (e.g., subreddits active in, times of day they post)
    - Content type they engage with
    - How they express opinions or seek help

5. **Motivations**:
    - What drives this user to engage with Reddit?
    - What are they trying to learn, solve, or express?

6. **Frustrations**:
    - Pain points and recurring issues they complain about or show emotional response to

7. **Goals & Needs**:
    - Short-term and long-term goals inferred from posts
    - Any recurring asks or interests

8. **Quote**:
    - A direct quote from one of the user's posts/comments that summarizes their personality or motivation

9. **Citations**:
    - For each key trait or insight, cite the related posts/comments (summarize or quote briefly)

Reddit Activity:
{data}
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating persona: {e}"
