# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Nayan and Megha, Congratulations on your first deployment through ci/cd pipeline using gitactions on EC2.",
           "Thankyou Note": "Thanks to KANAK who adviced us to do it :)"}
