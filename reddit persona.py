import praw
import requests
import re
import os

# === Reddit API credentials === cant provide the api credentials
REDDIT_CLIENT_ID = ""
REDDIT_SECRET = ""
REDDIT_USER_AGENT = " for example cilent id"

# === OpenRouter API Key ===
OPENROUTER_API_KEY =" cant display due to privacy reason"
MODEL = "mistralai/mistral-7b-instruct" 

# === Initialize Reddit API ===
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    check_for_async=False
)

def extract_username(url):
    match = re.search(r'reddit\.com\/user\/([^\/]+)', url)
    return match.group(1) if match else None

def fetch_reddit_data(username, limit=50):
    user = reddit.redditor(username)
    posts = []
    comments = []

    try:
        for post in user.submissions.new(limit=limit):
            posts.append(f"[POST] {post.title}\n{post.selftext}")

        for comment in user.comments.new(limit=limit):
            print("[COMMENT]:", comment.body)
            comments.append(f"[COMMENT] {comment.body}")

    except Exception as e:
        print("❌ Error fetching data:", e)

    return posts, comments

def build_persona_with_openrouter(posts, comments):
    content = "\n".join(posts + comments)

    prompt = f"""
You are a personality analyst. Based on the following Reddit posts and comments, build a user persona. Include characteristics, interests, values, tone, habits, and any demographic guesses. Cite at least one post/comment per trait.

Content:
{content}
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("❌ LLM Error:", response.status_code, response.text)
        return "Error: Could not generate persona."

def save_to_txt(username, persona):
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"✅ Persona saved to {filename}")

def main():
    url = "https://www.reddit.com/user/kojied/"
    username = extract_username(url)

    if not username:
        print("❌ Invalid Reddit URL.")
        return

    posts, comments = fetch_reddit_data(username)
    if not posts and not comments:
        print("⚠️ No data found for user.")
    else:
        persona = build_persona_with_openrouter(posts, comments)
        save_to_txt(username, persona)

if __name__ == "__main__":
    main()
