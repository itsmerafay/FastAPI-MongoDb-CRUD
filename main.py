from fastapi import FastAPI
from typing import Union
from pymongo.mongo_client import MongoClient    
from routes.route import router

app = FastAPI()

app.include_router(router)