from pymongo import MongoClient
from decouple import config
import asyncio


MONGO_URI = config("MONGO_URI")

DB_CLIENT = config("DB_CLIENT")

client = MongoClient(MONGO_URI)  # Подключение к MongoDB
db = client[DB_CLIENT]  # Название базы данных
logs_collection = db["logs"]  # Название коллекции
users_collection = db["users"]  # Коллекция для пользователей


def serialize_dict(doc):
    return {**doc, "_id": str(doc["_id"])}


def serialize_list(docs):
    return [serialize_dict(doc) for doc in docs]

