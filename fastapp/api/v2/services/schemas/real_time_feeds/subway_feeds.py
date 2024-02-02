from enum import Enum

from fastapp.api.v2.services.schemas.subway.subway_trains import SubwayTrains


class SubwayEndpointsGroups(str, Enum):
    ACE = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace"
    BDFM = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm"
    NQRW = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
    G = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g"
    JZ = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz"
    L = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l"
    SIR = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si"
    NUM = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"


subway_endpoint_relationship: {SubwayTrains, SubwayEndpointsGroups} = {
    SubwayTrains.A: SubwayEndpointsGroups.ACE,
    SubwayTrains.C: SubwayEndpointsGroups.ACE,
    SubwayTrains.E: SubwayEndpointsGroups.ACE,

    SubwayTrains.B: SubwayEndpointsGroups.BDFM,
    SubwayTrains.D: SubwayEndpointsGroups.BDFM,
    SubwayTrains.F: SubwayEndpointsGroups.BDFM,
    SubwayTrains.M: SubwayEndpointsGroups.BDFM,

    SubwayTrains.N: SubwayEndpointsGroups.NQRW,
    SubwayTrains.Q: SubwayEndpointsGroups.NQRW,
    SubwayTrains.R: SubwayEndpointsGroups.NQRW,
    SubwayTrains.W: SubwayEndpointsGroups.NQRW,

    SubwayTrains.G: SubwayEndpointsGroups.G,

    SubwayTrains.J: SubwayEndpointsGroups.JZ,
    SubwayTrains.Z: SubwayEndpointsGroups.JZ,

    SubwayTrains.L: SubwayEndpointsGroups.L,
    SubwayTrains.SIR: SubwayEndpointsGroups.SIR,

    SubwayTrains.ONE: SubwayEndpointsGroups.NUM,
    SubwayTrains.TWO: SubwayEndpointsGroups.NUM,
    SubwayTrains.THREE: SubwayEndpointsGroups.NUM,
    SubwayTrains.FOUR: SubwayEndpointsGroups.NUM,
    SubwayTrains.FIVE: SubwayEndpointsGroups.NUM,
    SubwayTrains.SIX: SubwayEndpointsGroups.NUM,
    SubwayTrains.SEVEN: SubwayEndpointsGroups.NUM,
}


# Both below work
# get_train_endpoints(["R","N","C"])
# get_train_endpoints([SubwayTrains.R,SubwayTrains.N,SubwayTrains.C])
def get_train_endpoints(list_of_trains: list[SubwayTrains]) -> set[str]:
    train_endpoints: set[str] = set()
    for train in list_of_trains:
        train_endpoints.add(subway_endpoint_relationship.get(train).value)
    return train_endpoints

