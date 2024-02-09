from datetime import date

from fastapi import FastAPI
from fastapi_cache.decorator import cache
from pydantic import BaseModel
import logging

from app.services.agify import Agify
from .cache import load_cache

app = FastAPI()
agify = Agify("https://api.agify.io/")

logger = logging.getLogger(__name__)


## Request data validation

class AgeRequest(BaseModel):
    name: str


## Startup actions

@app.on_event('startup')
async def startup_event():
    await load_cache()


## Views

@app.get("/api")
def home():
    return {"message": "Hello World"}

@cache(expire=60)
@app.post("/api/human_age")
async def human_age(requestData: AgeRequest):
    name = requestData.name
    try:
        response = agify.retrieve(name)
        age = int(response.get("age", 0))
    except Exception as e:
        logger.error(e)
        return {"error": "An error occurred"}
    
    # calculate year of birth from age
    current_year = date.today().year
    dob = current_year - age

    return {"name": name, "age": age, "date_of_birth": dob}