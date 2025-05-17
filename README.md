# CircadiaCare Backend

This is the backend API for CircadiaCare — a wellness and parenting assistant that helps new parents track sleep, baby metrics, and generate wellness insights using OpenAI.

---

## 🧠 Features

- Create & retrieve user profiles
- Record & fetch journal entries
- Track sleep, baby, and mom metrics
- Get:
  - ✅ Daily wellness tips
  - ✅ Baby care tips
  - ✅ Journal prompts
  - ✅ Self-care summaries
  - ✅ Risk scoring
- Fallback logic when AI is unavailable (e.g. no OpenAI quota)

---

## 🚀 Tech Stack

- **FastAPI** (Python)
- **SQLModel** (SQLAlchemy + Pydantic)
- **SQLite** (default DB)
- **OpenAI API** (optional)
- `.env`-based config with `USE_AI=true|false`

---

## 📦 Installation

```bash
git clone https://github.com/your-username/circadia_backend.git
cd circadia_backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
