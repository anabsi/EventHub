from database import EVENTS_DB
from models import Event

def add_event(data: dict):
    event = Event.create(data)
    EVENTS_DB.append(event)
    return event

def filter_events(type=None, player_id=None, guild_id=None):
    results = EVENTS_DB
    if type:
        results = [e for e in results if e.type == type]
    if player_id:
        results = [e for e in results if e.player_id == player_id]
    if guild_id:
        results = [e for e in results if e.guild_id == guild_id]
    return results
