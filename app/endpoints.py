from fastapi import APIRouter, HTTPException
from schemas import EventIn
from event_service import add_event, filter_events
from stats_service import (
    get_player_stats,
    get_guild_stats,
    get_top_players,
    get_solo_clear_award,
)

router = APIRouter()

@router.post("/events")
def create_event(event: EventIn):
    return add_event(event.dict())

@router.get("/events")
def list_events(type: str | None = None, player_id: str | None = None, guild_id: str | None = None):
    return filter_events(type, player_id, guild_id)

@router.get("/stats/player/{player_id}")
def player_stats(player_id: str):
    stats = get_player_stats(player_id)
    if not stats:
        raise HTTPException(status_code=404, detail="Player not found")
    return stats

@router.get("/stats/guild/{guild_id}")
def guild_stats(guild_id: str):
    stats = get_guild_stats(guild_id)
    if not stats:
        raise HTTPException(status_code=404, detail="Guild not found")
    return stats

@router.get("/stats/ranking/players")
def ranking(limit: int = 5):
    return get_top_players(limit)

@router.get("/stats/awards/solo-clear")
def solo_clear_award():
    return get_solo_clear_award()
