from car_service import services
from fastapi import FastAPI

app = FastAPI()
ser = services()

@app.get("/")
def read_root():
    return {"Welcome to car details"}

@app.get("/show_all")
def read():
    if ser.get_data() is not None:
        return ser.get_data()
    return {"Data not found"}

@app.get("/getCarById/{id}")
def read_item(id: int):
    if ser.get_certain_data(id) is not None:
        return ser.get_certain_data(id)
    return {"Data not found"}

@app.get("/addcar/{name}/{milege}/{model}/{id}/{color}")
def add_car(name:str, milege:float, model:str, id:int, color:str):
    if ser.create_car(name, milege, model, id, color):
        return {"Car is created"}
    return {"Car is not created"}

@app.get("/modifyCar/{id}/{type}/{val}")
def modify_car(id:int, type: str, val: int | str | float):
    if ser.modify_car(id, type, val):
        return {"Car is Updated"}
    return {"Car is not Updated"}

@app.get("/deleteCar/{id}")
def delete_car(id: int):
    if ser.delete_car(id):
        return {"Car is Deleted"}
    return {"Car is not deleted"}

