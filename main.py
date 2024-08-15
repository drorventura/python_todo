import asyncio

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import json

from warmly_repository import put_activities, delete_activity, bulk_insert, get_activities, get_last_id, \
    get_collection

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def on_startup():
    model = get_collection()
    if model.count_documents({}) == 0:
        with open('database.json') as f:
            data = json.load(f)
            documents = [{"id": int(key), "description": value} for key, value in data.items()]
            bulk_insert(documents)


@app.get("/")
async def root(request: Request):
    loop = asyncio.get_running_loop()
    try:
        data = await loop.run_in_executor(None, get_activities)
        return templates.TemplateResponse("todolist.html", {"request": request, "tododict": data})
    except asyncio.CancelledError:
        return {"error": "Request was cancelled before completion"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


@app.get("/delete/{id}")
async def delete_todo(request: Request, id: str):
    delete_activity(id)
    return RedirectResponse("/", 303)


@app.post("/add")
async def add_todo(newtodo: str = Form(...)):
    last_id = get_last_id()
    new_id = last_id + 1
    new_activity = {"id": new_id, "description": newtodo}
    inserted_id = put_activities(new_activity)
    return RedirectResponse("/", 303)


@app.get("/migrate")
async def migrate(request: Request):
    with open('database.json') as f:
        data = json.load(f)
        documents = [{"id": int(key), "description": value} for key, value in data.items()]
        result = bulk_insert(documents)
    return RedirectResponse("/", 303)
