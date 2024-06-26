from fastapp.api.v2.services.response_handler.station_data_reader import StationDataReader
from fastapp.api.v2.services.response_handler.subway_response import SubwayResponseHandler
from fastapp.api.v2.services.schemas.subway.subway_schema import TrainStopInfo, SubwayTrain, TrainStop
from fastapp.api.v2.services.schemas.subway.subway_trains import SubwayTrains


def make_stop(stop_id):
    sdr = StationDataReader()
    try:
        train_stop = TrainStopInfo(
            station_name=sdr.get_station((stop_id[:3])),
            direction=stop_id[-1].upper(),
            stop_id=stop_id,
        )
    except Exception:
        raise Exception("FINDING STOP FAIL")
    return train_stop


def get_train_stop_northern_blvd(stop_id) -> TrainStopInfo:
    handler = SubwayResponseHandler()
    trains = handler.create_trains([SubwayTrains.R, SubwayTrains.E, SubwayTrains.F])
    trains_hitting_stop = []
    for train in trains:
        for stop in train.stop_time_update:
            if stop_id in stop.gtfs_id:
                trains_hitting_stop.append((train, stop))

    the_stop = make_stop(stop_id)
    for wanted_train in trains_hitting_stop:
        if "N" in wanted_train[1].direction:
            the_stop.trains.append(
                TrainStop(
                    id=wanted_train[0],
                    route_id=wanted_train[0].route_id,
                    north=wanted_train[1]
                )
            )
        if "S" in wanted_train[1].direction:
            the_stop.trains.append(
                TrainStop(
                    id=wanted_train[0].id,
                    route_id=wanted_train[0].route_id,
                    south=wanted_train[1]
                )
            )
    return the_stop


def get_train_stops(train_name) -> list[SubwayTrain]:
    handler = SubwayResponseHandler()
    trains = handler.create_trains(train_name)
    wanted_trains = []
    for train in trains:
        if train_name == train.route_id:
            wanted_trains.append(train)
    return wanted_trains


def get_trains_raw(train_name) -> list[SubwayTrain]:
    handler = SubwayResponseHandler()
    return handler.create_trains(train_name)
