# 🤖 AI-Driven LinkedIn Post Generator

> Effortless professional content from your daily workflow.
![image](https://github.com/user-attachments/assets/3342867f-b26f-46ef-b222-8bce638a57d4)

---

## 🚀 What Is This?

This tool helps you craft high-quality LinkedIn posts based on what you do — automatically.

Whether you're writing code or working on a project, it can suggest and generate smart, relevant content to share with your network.

---

## 🧠 Phase I: Code-Aware Post Generator

The first phase focuses on devs — by analyzing your code changes, it can generate:

- ✨ Project updates
- 🛠️ Build logs or debugging insights
- 🧪 Feature launch posts

Powered by Gemini 2.0 Flash and Flask.

---

## 🛠️ Tech Stack

- **AI Engine**: Gemini 2.0 Flash API
- **Backend**: Flask (Phase I), Django REST planned
- **Frontend**: Coming soon (React-based UI in Phase II)
- **Environment**: `.env` + `python-dotenv`

---

## 📦 How to Run (Phase I)

```bash
git clone https://github.com/Geekboieyash/LinkedIn-Agent.git
cd LinkedIn-Agent
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Then run:

```bash
python run.py
```

Your app will be live at:  
📍 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧭 What’s Coming (Sneak Peek)

- 📋 AI-generated post drafts from browser activity
- 📈 Post performance tracking
- 🔥 Trending topic suggestions
- 💡 Smart prompt templates
- 🎯 Personalized tone / writing goals

---

## 💬 Contribute or Follow

Phase I is open-source — feel free to fork and build with it.  
Later phases will be shared as they stabilize.
Demo Video on youtube: https://youtu.be/TYZh1qEm1rk

---

## ⚖️ License

MIT — free for personal + commercial use. Just don’t resell it without changes 😉

---

> ✍️ Built for devs, by a dev — to help you share your work without overthinking it.

---
## Project Structure

```
project_root/
├── api/                       # New: FastAPI app core
│   ├── main.py                # FastAPI app instance
│   ├── routes/                # Moved from project root
│   │   └── linkedin_routes.py
│   ├── services/              # Moved from project root
│   │   └── linkedin_post.py
│   ├── schemas/               # New: Pydantic request/response models
│   └── deps.py                # (Optional) for dependency injection
│
├── ai_core/                   # Renamed from models/
│   └── gemini.py              # Gemini/LLM logic stays here
│
├── utils/                     # Keep as-is
├── templates/                 # Keep if you're rendering HTML (optional)
├── config.py                  # Keep for settings/env mgmt
├── .env
├── requirements.txt
└── frontend/                  # Create new React app here

```
