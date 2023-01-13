from deta import Deta
from operator import itemgetter

key = "d0excjil_3hjrn4nfG3A7uwWffGykx1bLoYcvC1pW"
deta = Deta(key)
carousel = "carousel"
info = "info"
event = "event"
team = "team"


def get_carousel():
    db = deta.Base(carousel)
    results = db.fetch()
    return results.items


def get_about():
    db = deta.Base(info)
    results = db.fetch({"type": "about"})
    return results.items[0]


def get_main_events():
    db = deta.Base(event)
    results = db.fetch({"main": True})
    results = results.items
    data = {
        "events": results,
        "title": "Our Events",
        "subtitle": "Lead Future Together",
    }
    return data


def get_main_team():
    db = deta.Base(team)
    results = db.fetch({"main": True})
    return {
        "members": results.items,
        "main": True,
        "subtitle": "Energy Club Co-ordinators",
    }


def get_team():
    db = deta.Base(team)
    results = db.fetch()
    results = sorted(results.items, key=itemgetter("deg"))
    return {
        "members": results,
        "main": False,
        "subtitle": "Energy Club Members",
    }


def get_single_event(name: str):
    db = deta.Base(event)
    results = db.fetch({"title": name})
    results = results.items[0] if results.count > 0 else None
    if results is None:
        return None
    elif results["flagship"] == True:
        sub_events = db.fetch({"parent_event": results["title"], "sub_event": True})
        sub_events = sub_events.items
        return {"event": results, "sub_event": sub_events}
    else:
        return {"event": results}


def get_all_events():
    db = deta.Base(event)
    results = db.fetch()
    return results.items


# db = deta.Base(event)
# db.put(
#     {
#         "name": "xyz",
#         "designation": "co-ordinator",
#         "insta": "id",
#         "img_link": "https",
#         "main": True,
#         "deg":1
#     }
# )
# db.put(
#     {
#         "title": "def",
#         "subtitle": "def",
#         "description":'def',
#         "img_link": "https",
#         "reg_link": "https",
#         "main": True,
#         "flagship": True,
#         "sub_event": True,
#         "parent_event":"abc",
#     },
# )
