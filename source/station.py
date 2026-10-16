class Charging_station:
    def __init__(self,station_id,name,latitude,longitude,city,charger_type,available):
        self.station_id = station_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.charger_type = charger_type
        self.available = available

    def coordinates(self):
        return (self.latitude , self.longitude)

    def __str__(self):
        return (
            f"City = {self.city} | Name = {self.name} |"
            f"Lat = {self.latitude} | Long = {self.longitude}"
        )

