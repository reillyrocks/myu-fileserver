from fastapp.api.v2.services.response_handler.subway_response import SubwayResponseHandler
from fastapp.api.v2.services.schemas.subway.subway_schema import SubwayTrain, StopTime


def get_train_stop_northerblvd(train_id) -> list[StopTime]:
    handler = SubwayResponseHandler()
    trains = handler.create_trains()
    wanted = []
    for train in trains:
        if train.route_id == "R":
            print(train)
            for stop in train.stop_time_update:
                if stop.stop_id.count(train_id) > 0:
                    wanted.append(stop)
    return wanted
