import pathlib
import csv
from typing import Optional

from pydantic import Basemodel, model_validator

class StationModel(Basemodel):
    gtfs_stop_id: Optional[str]
    stop_name: Optional[str]


class StationCSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_models(self):
        models = {}
        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    models[row['GTFS Stop ID']] = StationModel(gtfs_stop_id=row['GTFS Stop ID'],
                                                               stop_name=row['Stop Name'])
                except Exception as e:
                    print(f"Error getting gtfs stop id {e}")
                    raise e
        return models

class StationDataReader:
    def __init__(self):
        parent_dir = pathlib.Path(__file__).parent
        reader = StationCSVReader(f'{parent_dir}/docs/MTA_Subway_Stations.csv')
        self.models = reader.read_models()

    def get_station(self, station_id):
        if station_id in self.models:
            model = self.models[station_id].stop_name
        else:
            model = "UNKNOWN"
        return model