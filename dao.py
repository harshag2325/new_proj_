from db_config import connect_func
db = connect_func('car_DB')
collection = db.CarDetails
def connect():
    data_list = collection.find({}, {'_id':False})
    return data_list

def get_connection_insert(name, milege, model, id, color):
    post_id = collection.insert_one({"Color": color, "Milege":milege, "Model": model, "Name": name, "Id":id})
    
    if post_id is not None:
        return True
    return False
def get_connection_update(id, type, val):
    post_id = collection.update_one({"id" : id}, {"$set":{type:val}})
    if post_id is not None:
        return True
    return False
def get_connection_delete(id):
    post_id = collection.delete_one({"id": id})
    if post_id is not None:
        return True
    return False
