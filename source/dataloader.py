import json
from station import Charging_station

class Station_data_loader:
    @staticmethod
    def check_station_data(data):
        required = {
            "station_id",
            "name",
            "latitude",
            "longitude",
            "city",
            "charger_type",
            "available"
        }

        if not isinstance(data,dict):
            raise ValueError("Each station must be a dictionary")

        if not required.issubset(data):
            raise ValueError("Station data is missing some fields")

        latitude = float(data["latitude"])
        longitude = float(data["longitude"])

        if not -90 <= latitude <= 90:
            raise ValueError("latitude must be between -90 and 90")
        if not -180 <= longitude <= 180:
            raise ValueError("longitude must be between -180 and 180")
        if not isinstance(data["available"],bool):
            raise ValueError("Availability must be true or false")

        return True

    @staticmethod
    def _create_station(data):
        Station_data_loader.check_station_data(data)

        return Charging_station(
        station_id=data["station_id"],
        name=data["name"],
        latitude=float(data["latitude"]),
        longitude=float(data["longitude"]),
        city=data["city"],
        charger_type=data["charger_type"],
        available=data["available"]
        )

    @staticmethod
    def load_json(filepath):
        with open(filepath,"r",encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data,list):
            raise ValueError("JSON must contain a list of station")
        else:
            stations = []

            for record in data:
                station = Station_data_loader._create_station(record)
                stations.append(station)

            return stations
                