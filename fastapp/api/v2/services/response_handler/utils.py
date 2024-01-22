from datetime import datetime

SUBWAY_STOP_DOC_LOCATION = "fastapp/api/v2/services/response_handler/docs/MTA_Subway_Stations_20240121.csv"
SUBWAY_STOP_DOC = None

class SubwayUtil:
    def get_est_datetime(self, unixtime) -> datetime:
        if unixtime is None:
            return None
        est_offset = -5 * 60 * 60
        return datetime.utcfromtimestamp(int(unixtime) + est_offset)


    def get_stop_id(self):
        if SUBWAY_STOP_DOC:
            return SUBWAY_STOP_DOC
