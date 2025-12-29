from datetime import datetime
from pydantic import BaseModel
from typing import Any, Dict
import uuid

class Event(BaseModel):
    id: str
    timestamp: datetime
    type: str
    player_id: str | None
    guild_id: str | None
    details: Dict[str, Any]

    @staticmethod
    def create(data: dict):
        return Event(
            id=str(uuid.uuid4()),
            timestamp=data["timestamp"],
            type=data["type"],
            player_id=data.get("player_id"),
            guild_id=data.get("guild_id"),
            details=data.get("details", {}),
        )
