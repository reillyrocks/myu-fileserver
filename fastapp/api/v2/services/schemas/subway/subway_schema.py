from datetime import datetime

from pydantic import BaseModel
from typing import List, Optional


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
    stop_time_update: Optional[List[StopTime]]

    # Vehicle
    current_stop_sequence: Optional[int]
    stop_id: Optional[str]
    current_status: Optional[str]
    timestamp: Optional[datetime]

    # Alert
    informed_entity: Optional[List[str]]
    header_text: Optional[str]

