from db_config import connect_func
def connect():
    db = connect_func('car_DB')
    collection = db.CarDetails
    data_list = collection.find({}, {'_id':False})
    return data_list

