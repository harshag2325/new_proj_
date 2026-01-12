from pymongo import MongoClient

def connect_func(database_name):
    try:
        uri = "mongodb://localhost:27017/"
        client = MongoClient(uri)

        client.admin.command("ping")
        print("Connected successfully")
        db = client[database_name]
        return db
    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)