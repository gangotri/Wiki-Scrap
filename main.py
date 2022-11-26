from fastapi import FastAPI
import db
import modals

import scraper

app = FastAPI()


@app.get("/")
async def root():
    print(scraper.getTitle())
    print(scraper.getList())
    return {"message": "Hello World"+scraper.getTitle()}

@app.get("/all")
def all():
    data = db.all()
    return {"data": data}



@app.get("/scrapPage")
def create(path: str):
    print("************************")
    print(path)
    soup = scraper.parseUrl(path)
    pageTitle = scraper.getTitle(soup)
    data = {"title": pageTitle, "description": scraper.getDescription(soup)}
    if(db.get_one(pageTitle)):
        data = db.update(pageTitle, data)
    else:
        data = db.create(data)
    
    return {"inserted": True, "inserted_id": data}