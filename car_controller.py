from car_service import services
from fastapi import FastAPI

app = FastAPI()
ser = services()

@app.get("/")
def read_root():
    return {"Welcome to car details"}

@app.get("/show_all")
def read():
    return ser.get_data()

@app.get("/getCarById/{id}")
def read_item(id: int):
    pass

@app.post("/addcar")
def add_car():
    pass

@app.put("/modifyCar/{id}")
def modify_car():
    pass

@app.delete("/deleteCar")
def delete_car():
    pass

