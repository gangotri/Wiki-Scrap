from fastapi import FastAPI
import db
import modals

import scraper

app = FastAPI()


@app.get("/")
async def root():
    
    return {"message": "Hello World"}



@app.get("/scrapPage")
def scapPage(path: str):
    soup = scraper.parseUrl(path)
    pageTitle = scraper.getTitle(soup)
    scrapText = scraper.getDescription(soup)
    data = {"title": pageTitle, "description": scrapText}
    if(db.get_one(pageTitle)):
        data = db.update(pageTitle, data)
    else:
        data = db.create(data)
    
    return {"message": "Successful", "Scrap text": scrapText}