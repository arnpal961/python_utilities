from settings import MONGO_HOST, MONGO_PORT
from pymongo import MongoClient

client = MongoClient(MONGO_HOST, MONGO_PORT)