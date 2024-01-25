from fastapi import APIRouter

from fastapp.api.v2.services.schemas.subway.subway_schema import SubwayTrain, StopTime
from fastapp.api.v2.services.stop_finder import get_train_stop_northerblvd

subway_router = APIRouter(
    prefix="/subway",
)


@subway_router.get("/get_train/")
async def get_train() -> list[StopTime]:
    train_id = "G16"
    return get_train_stop_northerblvd(train_id)


@subway_router.get("/test/")
async def test() -> str:
    return "yup"
