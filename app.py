from fastapi import FastAPI


app = FastAPI()

richest_people_list={
    "Elon Musk": "280 Billion USD",
    "Jeff Bezos": "290 Billion USD"
}


@app.get("/richest-people")
def richest_people():
    return richest_people_list