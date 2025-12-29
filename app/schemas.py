from pydantic import BaseModel
from datetime import datetime
from typing import Any, Dict, Optional

class EventIn(BaseModel):
    type: str
    timestamp: datetime
    player_id: Optional[str]
    guild_id: Optional[str]
    details: Dict[str, Any]
