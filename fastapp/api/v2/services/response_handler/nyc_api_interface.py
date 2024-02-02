import requests
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import DecodeError
from google.transit import gtfs_realtime_pb2
from pydantic import BaseModel

from fastapp.api.v2.services.schemas.real_time_feeds.subway_feeds import get_train_endpoints
from fastapp.api.v2.services.schemas.subway.subway_trains import SubwayTrains
from fastapp.core.settings import get_settings


# Function to convert a FeedEntity to a JSON-like dictionary
def feed_entity_to_json_dict(feed_entity: gtfs_realtime_pb2.FeedEntity) -> dict:
    return MessageToDict(feed_entity, including_default_value_fields=True, preserving_proto_field_name=True)


def call_mta_endpoint(endpoint) -> requests.Response:
    headers = {"x-api-key": get_settings().secret_key}
    try:
        r = requests.get(endpoint, headers=headers)
    except Exception:
        raise Exception("failure to submit endpoint")
    return r


def convert_nyc_response(train_list: list[SubwayTrains], pydantic_object: BaseModel):

    entity_list = []
    # Get the endpoints for the trains, and then loop through them.
    endpoints = get_train_endpoints(train_list)
    for endpoint in endpoints:
        response = call_mta_endpoint(endpoint)
        try:
            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(response.content)

        except DecodeError:
            raise Exception("print bad request :(")

        for entity in feed.entity:
            entity_list.append(pydantic_object.model_validate(feed_entity_to_json_dict(entity)))

    return entity_list
