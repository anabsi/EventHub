from collections import Counter
from database import EVENTS_DB

def get_player_stats(player_id: str):
    events = [e for e in EVENTS_DB if e.player_id == player_id]
    if not events:
        return None
    return {
        "player_id": player_id,
        "total_events": len(events),
        "event_types": dict(Counter(e.type for e in events)),
        "last_activity": max(e.timestamp for e in events),
        "guilds_related": list({e.guild_id for e in events if e.guild_id}),
    }

def get_guild_stats(guild_id: str):
    events = [e for e in EVENTS_DB if e.guild_id == guild_id]
    if not events:
        return None
    return {
        "guild_id": guild_id,
        "total_events": len(events),
        "event_types": dict(Counter(e.type for e in events)),
        "players_involved": list({e.player_id for e in events if e.player_id}),
    }

def get_top_players(limit=5):
    ranking = Counter(e.player_id for e in EVENTS_DB if e.player_id)
    return [
        {"player_id": p, "total_events": c}
        for p, c in ranking.most_common(limit)
    ]

def get_solo_clear_award():
    solo_clears = Counter()
    for e in EVENTS_DB:
        if e.type == "DUNGEON_CLEAR":
            members = e.details.get("party_members", [])
            if len(members) == 1:
                solo_clears[e.player_id] += 1

    return [
        {"player_id": player, "total_solo_clears": total}
        for player, total in solo_clears.items()
    ]
