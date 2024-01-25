from datetime import datetime

from pydantic import BaseModel, Field, model_validator
from typing import List, Optional

from fastapp.api.v2.services.response_handler.utils import SubwayUtil


class TripDescriptor(BaseModel):
    trip_id: str
    route_id: str
    start_time: str
    start_date: str


class StopTimeUpdate(BaseModel):
    stop_id: str
    arrival: datetime
    departure: datetime

    @model_validator(mode='before')
    def set_datetime(cls, values):
        su = SubwayUtil()
        values['arrival'] = su.get_est_datetime(values.get("arrival", {}).get("time", 0))
        values['departure'] = su.get_est_datetime(values.get("departure", {}).get("time", 0))
        return values


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
