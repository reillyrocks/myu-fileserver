from datetime import datetime

from pydantic import BaseModel, Field, root_validator
from typing import List, Optional


class TripDescriptor(BaseModel):
    trip_id: str
    route_id: str
    start_time: str
    start_date: str


class StopTimeUpdate(BaseModel):
    stop_id: str
    arrival: datetime
    departure: datetime

    @root_validator(pre=True)
    def flatten(cls, values):
        est_offset = -5 * 60 * 60
        datetime.utcfromtimestamp(1705901357 + est_offset)
        return {
            "arrival": datetime.utcfromtimestamp(int(values.get("arrival", {}).get("time", None)) + est_offset),
            "departure": datetime.utcfromtimestamp(int(values.get("departure", {}).get("time", None)) + est_offset),
            "stop_id": values.get("stop_id", 0),
        }


class TripUpdate(BaseModel):
    trip: TripDescriptor
    stop_time_update: List[StopTimeUpdate]


class Vehicle(BaseModel):
    trip: TripDescriptor
    current_stop_sequence: Optional[int]
    stop_id: Optional[str]
    current_status: Optional[str]
    timestamp: Optional[int]


class Alert(BaseModel):
    informed_entity: Optional[List[str]] = None
    header_text: Optional[str] = None


class SubwayEntity(BaseModel):
    # id: str = Field(..., description="The entity's unique identifier")
    is_deleted: bool = False
    trip_update: Optional[TripUpdate] = None
    vehicle: Optional[Vehicle] = None
    alert: Optional[Alert] = None


# This is a train with TripUpdates and a vehicle
class Train(BaseModel):
    id: str
    trip_update: Optional[TripUpdate] = None
    vehicle: Optional[Vehicle] = None
    alert: Optional[Alert] = None
