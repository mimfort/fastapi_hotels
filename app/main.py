from fastapi import FastAPI,Query,Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
app = FastAPI()

app.include_router(router_bookings )
class Shotel(BaseModel):
    address : str
    start : int
    name : str

class HotelAdress:
    def __init__(self,location: str,
         date_start: Optional[date],
         date_finish: Optional[date],
         stars: Optional[int] = Query(default=None,ge=1,le=5)):
        self.location = location
        self.stars = stars
        self.date_start = date_start
        self.date_finish = date_finish



@app.get("/hotels/",response_model=list[Shotel])
def root(search_args : HotelAdress = Depends()
         ):
    hotels = [
        {"address":"Ул Флотская д.6",
         "start":5,
         "name":"Elion"}
    ]
    return hotels

class Sbooking(BaseModel):
    room_id : int
    date_from : date
    date_to : date


@app.post("/bookings")
def add_bookings(booking:Sbooking):
    pass