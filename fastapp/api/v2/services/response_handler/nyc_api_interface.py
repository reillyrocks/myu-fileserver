from typing import List

from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests
from pydantic import BaseModel


# Function to convert a FeedEntity to a JSON-like dictionary
def feed_entity_to_json_dict(feed_entity: gtfs_realtime_pb2.FeedEntity) -> dict:
    return MessageToDict(feed_entity, including_default_value_fields=True, preserving_proto_field_name=True)


def convert_nyc_response(pydantic_object: BaseModel):
    url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace"
    api_key = "oL1ryDzgab8YfJyQn4Jc46338O7AyF5P7khip8zC"
    headers = {"x-api-key": api_key}

    r = requests.get(url, headers=headers)

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(r.content)

    entity_list = []
    for entity in feed.entity:
        entity_list.append(pydantic_object.parse_obj(feed_entity_to_json_dict(entity)))
    return entity_list
