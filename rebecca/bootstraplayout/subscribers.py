from pyramid.events import subscriber
from . import helpers


@subscriber("pyramid.events.BeforeRender")
def register_globals(event):
    event["h"] = helpers
