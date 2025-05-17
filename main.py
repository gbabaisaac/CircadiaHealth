from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from datetime import datetime, date, timedelta
from typing import Optional, List
import httpx, os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
USE_AI = os.getenv("USE_AI", "true").lower() == "true"

# --- Models ---
class UserProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    dob: date
    baby_name: str
    baby_dob: date
    baby_gender: str

class Journal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userprofile.id")
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Sleep(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userprofile.id")
    timestamp: datetime
    sleep_duration: float
    hrv: Optional[float] = None

class Prompt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userprofile.id")
    date: date
    text: str

class BabyMetric(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userprofile.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    weight: Optional[float] = None
    height: Optional[float] = None
    feeding_amount: Optional[float] = None
    feeding_time: Optional[float] = None
    nap_start: Optional[datetime] = None
    nap_end: Optional[datetime] = None

class MomMetric(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="userprofile.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    weight: Optional[float] = None
    height: Optional[float] = None
    pumping_time: Optional[float] = None
    feeding_time: Optional[float] = None

# --- Database ---
DATABASE_URL = "sqlite:///circadia.db"
engine = create_engine(DATABASE_URL, echo=False)
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# --- App ---
app = FastAPI(title="CircadiaCare Backend")

@app.get("/", summary="Health Check")
def read_root():
    return {"message": "CircadiaCare backend alive!"}

@app.get("/daily-wellness")
async def get_daily_wellness_tips(user_id: int, session: Session = Depends(get_session)):
    if not USE_AI:
        return {
            "tips": [
                "Take 10 minutes to do something just for yourself.",
                "Drink a full glass of water and stretch.",
                "Celebrate one small win from your day."
            ]
        }
    raise HTTPException(500, detail="AI mode not supported in current configuration.")

@app.get("/baby-tips")
async def get_ai_baby_tips(user_id: int, session: Session = Depends(get_session)):
    if not USE_AI:
        return {
            "tips": [
                "Burp your baby after every feeding.",
                "Maintain a calm and dim environment before naps.",
                "Keep track of diaper changes to monitor health."
            ]
        }
    raise HTTPException(500, detail="AI mode not supported in current configuration.")

@app.get("/tips")
async def get_tips(user_id: int):
    if not USE_AI:
        return {
            "tips": [
                "Avoid caffeine after 2pm.",
                "Try a relaxing bedtime routine.",
                "Wake up at the same time every day."
            ]
        }
    raise HTTPException(500, detail="AI mode not supported in current configuration.")

@app.get("/journal/prompt")
async def get_prompt(user_id: int, date: Optional[str] = None):
    if not USE_AI:
        return {
            "prompt": "What are you most grateful for today, and why?"
        }
    raise HTTPException(500, detail="AI mode not supported in current configuration.")

@app.get("/summary")
def get_summary(user_id: int):
    if not USE_AI:
        return {
            "summary": "Over the past few days, you've maintained a steady sleep routine and journaled consistently. Keep up the great work and remember to prioritize self-care."
        }
    raise HTTPException(500, detail="AI mode not supported in current configuration.")

@app.get("/risk")
def get_risk(user_id: int):
    if not USE_AI:
        return {
            "avg_sleep_3d": 5.2,
            "at_risk": False
        }
    raise HTTPException(500, detail="AI mode not supported in current configuration.")
