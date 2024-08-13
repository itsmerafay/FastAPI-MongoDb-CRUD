from pymongo import MongoClient

# Connects to mongo db server
client = MongoClient("mongodb+srv://rafay:rafay@cluster0.livrjof.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


db = client.todo_db
collection_name = db["todo_collection"]
