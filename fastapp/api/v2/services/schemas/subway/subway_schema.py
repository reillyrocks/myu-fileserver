from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class StopTime(BaseModel):
    stop_id: str
    arrival: datetime
    departure: datetime


class SubwayTrain(BaseModel):
    id: str
    # Descriptor
    route_id: Optional[str]
    start_time: Optional[str]
    start_date: Optional[str]

    #Trip Update
    stop_time_update: List[StopTime]

    # Vehicle
    current_stop_sequence: Optional[int]
    stop_id: Optional[str]
    current_status: Optional[str]
    timestamp: Optional[datetime]

    # Alert
    informed_entity: Optional[List[str]] = None
    header_text: Optional[str] = None

