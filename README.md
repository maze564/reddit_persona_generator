# reddit_persona_generator
Reddit Persona Generator is a Python-based tool that scrapes a Reddit user’s posts and comments, and uses a free LLM (like Mistral-7B via OpenRouter.ai) to generate a structured user persona. The persona includes traits such as interests, personality, habits, and demographic guesses — with citations from the user's content.

# 🧠 Reddit Persona Generator

Welcome to the **Reddit Persona Generator** — a Python-based AI-powered tool that reads between the lines of Reddit users and builds an intelligent persona profile using a Large Language Model (LLM).

This project was built as part of an **AI/LLM Engineer Internship Assignment** and showcases practical skills in API integration, natural language processing, and generative AI.

---

## 🚀 What It Does

Given a Reddit username, the tool:

1. **Scrapes** their public posts and comments using the Reddit API.
2. **Analyzes** their behavior and language using an LLM (via OpenRouter.ai).
3. **Generates** a structured persona including:
   - Interests & Hobbies
   - Personality Traits
   - Tone & Behavior
   - Demographic Guesses (age range, profession)
   - Cited examples from their content
Output:
- `kojied_persona.txt` file containing a detailed profile based on their Reddit activity.

---

## 🧰 Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
| `praw`         | Reddit API client (to fetch posts/comments) |
| `requests`     | To call OpenRouter.ai’s LLM API |
| `OpenRouter.ai`| Provides free access to powerful open-source LLMs like Mistral |
| `Mistral-7B-Instruct` | Chosen model for persona generation |

---

## 📦 Installation

Clone the repository and install required packages:

```bash
git clone https://github.com/your-username/reddit-persona-generator.git
cd reddit-persona-generator
pip install -r requirements.txt
