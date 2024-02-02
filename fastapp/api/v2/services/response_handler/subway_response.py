from typing import List

from pydantic_core import ValidationError

from fastapp.api.v2.services.response_handler.nyc_api_interface import convert_nyc_response
from fastapp.api.v2.services.response_handler.utils import SubwayUtil
from fastapp.api.v2.services.schemas.subway.subway_response_schema import Train, Vehicle, TripUpdate, SubwayEntity
from fastapp.api.v2.services.schemas.subway.subway_schema import SubwayTrain


class SubwayResponseHandler:

    # Method to zip together and link trip_updates, alerts and vehicles into one object (using the same trip_id)
    def zip_response_trains(self, train_lines) -> List[Train]:
        nyc_response_entities: List[SubwayEntity] = convert_nyc_response(train_lines, SubwayEntity)
        train_id_dict = {}
        for entity in nyc_response_entities:
            if isinstance(entity.vehicle, Vehicle):
                # If the train exists. that means a trip was added to the dict
                if train_id_dict.get(entity.vehicle.trip.trip_id):
                    train_id_dict[entity.vehicle.trip.trip_id].vehicle = entity.vehicle
                else:
                    # If the train doesn't exist the add it to the already existing vehicle
                    train = Train(id=entity.vehicle.trip.trip_id)
                    train.vehicle = entity.vehicle
                    train_id_dict[entity.vehicle.trip.trip_id] = train

            if isinstance(entity.trip_update, TripUpdate):
                if train_id_dict.get(entity.trip_update.trip.trip_id):
                    train_id_dict[entity.trip_update.trip.trip_id].trip_update = entity.trip_update
                else:
                    train = Train(id=entity.trip_update.trip.trip_id)
                    train.trip_update = entity.trip_update
                    train_id_dict[entity.trip_update.trip.trip_id] = train
        return list(train_id_dict.values())

    def create_trains(self, train_lines) -> list[SubwayTrain]:
        trains = self.zip_response_trains(train_lines)
        subway_trains = []
        su = SubwayUtil()
        for train in trains:
            try:
                subway_trains.append(SubwayTrain(
                    id=train.id,
                    route_id=train.trip_update.trip.route_id,
                    start_time=train.trip_update.trip.start_time,
                    start_date=train.trip_update.trip.start_date,
                    stop_time_update=train.trip_update.model_dump().get("stop_time_update", []),
                    current_stop_sequence=train.vehicle.current_stop_sequence,
                    stop_id=train.vehicle.stop_id,
                    current_status=train.vehicle.current_status,
                    timestamp=su.get_est_datetime(train.vehicle.timestamp),

                    # Need to handle None values for this
                    # informed_entity=train.alert.informed_entity,
                    # header_text=train.alert.header_text,
                ))
            except AttributeError as e:
                raise Exception(f"AttributeError= None value when accessing values to create subway_trains {e}")
            except TypeError as e:
                raise Exception(f"TypeError= None value for 'arrival' or 'departure' Time - failing the est adjusting {e}")
            except ValidationError as e:
                raise Exception(f"ValdiationError for train {train}. Exception {e}")
        return subway_trains
