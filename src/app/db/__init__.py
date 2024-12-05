from pymongo import MongoClient

from app.conf import settings

client = MongoClient(
    settings.MONGO_DB_URI,
)
db = client["form_templates"]
