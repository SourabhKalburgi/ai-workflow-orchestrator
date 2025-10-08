# src/database/db_service.py

import os
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
posts_collection = db["posts"]

def save_post(data: dict):
    """Save a formatted post to MongoDB"""
    data["created_at"] = datetime.utcnow()
    result = posts_collection.insert_one(data)
    return str(result.inserted_id)

def get_recent_posts(limit=5):
    """Retrieve recent posts"""
    return list(posts_collection.find().sort("created_at", -1).limit(limit))

def get_posts_by_topic(topic: str):
    """Retrieve posts filtered by topic"""
    return list(posts_collection.find({"topic": topic}).sort("created_at", -1))

