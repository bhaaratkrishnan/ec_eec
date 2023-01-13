from fastapi import FastAPI, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db import (
    get_carousel,
    get_about,
    get_main_events,
    get_main_team,
    get_team,
    get_single_event,
    get_all_events,
)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", name="home")
async def home(request: Request):
    context = {
        "request": request,
        "carousel": get_carousel(),
        "about": get_about(),
        "cards": get_main_events(),
        "team": get_main_team(),
    }

    return templates.TemplateResponse("index.html", context=context)


@app.get("/team", name="team")
async def team_members(request: Request):
    context = {"request": request, "team": get_team()}
    return templates.TemplateResponse("team.html", context=context)


@app.get("/event/{event_name}", name="single_event")
async def single_event(request: Request, event_name: str):
    context = {
        "request": request,
    }
    event = get_single_event(name=event_name)
    if event is None:
        # if no event is found
        return templates.TemplateResponse("404.html", context=context)

    if event["event"]["flagship"] == False:
        # if event is normal
        context["event"] = event["event"]
        return templates.TemplateResponse("single_event.html", context=context)
    # if event is flagship
    context["event"] = event["event"]
    title = "Events in " + event["event"]["title"]
    context["cards"] = {
        "events": event["sub_event"],
        "subtitle": title,
        "more_event": False,
    }
    return templates.TemplateResponse("flagship_event.html", context=context)


@app.get("/event", name="events")
async def events(request: Request):
    context = {
        "request": request,
    }
    context["cards"] = {
        "title": "Our Events",
        "subtitle": "Lead Future Together",
        "more_event": False,
        "events": get_all_events(),
    }
    return templates.TemplateResponse("events.html", context=context)


@app.get("/contact", name="contact")
async def contact_us(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("contact.html", context=context)


# @app.post("/")
# async def upload(file: UploadFile = File(...)):
#     content = await file.read()
#     content = base64.b64encode(content)
#     with open(file.filename, "wb") as newfile:
#         newfile.write(content)
#     imagekit.upload_file(
#         file=content,
#         file_name=file.filename,
#         options=image_options,
#     )
#     return {"file": file.filename}
