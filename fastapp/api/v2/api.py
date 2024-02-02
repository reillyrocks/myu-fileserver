from fastapi import APIRouter

from fastapp.api.v2.services.schemas.subway.subway_schema import StopTime, TrainStopInfo, SubwayTrain
from fastapp.api.v2.services.stop_finder import get_train_stop_northern_blvd, get_train_stops, get_trains_raw

subway_router = APIRouter(
    prefix="/subway",
)


@subway_router.get("/get_train/{train}")
async def get_train(train) -> list[SubwayTrain]:
    return get_train_stops(train)


@subway_router.get("/get_full_api_line/{train}")
async def get_full_api_line(train) -> list[SubwayTrain]:
    return get_trains_raw(train)


@subway_router.get("/get_northern_blvd/")
async def get_northern_blvd() -> TrainStopInfo:
    train_id = "G16"
    return get_train_stop_northern_blvd(train_id)


@subway_router.get("/test/")
async def test() -> str:
    return "yup"
