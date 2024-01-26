import requests
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import DecodeError
from google.transit import gtfs_realtime_pb2
from pydantic import BaseModel

from fastapp.core.settings import get_settings


# Function to convert a FeedEntity to a JSON-like dictionary
def feed_entity_to_json_dict(feed_entity: gtfs_realtime_pb2.FeedEntity) -> dict:
    return MessageToDict(feed_entity, including_default_value_fields=True, preserving_proto_field_name=True)


def convert_nyc_response(pydantic_object: BaseModel):
    url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
    headers = {"x-api-key": get_settings().secret_key}

    try:
        r = requests.get(url, headers=headers)

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(r.content)

    except DecodeError:
        raise Exception("print bad request :(")


    entity_list = []
    for entity in feed.entity:
        entity_list.append(pydantic_object.model_validate(feed_entity_to_json_dict(entity)))
    return entity_list
