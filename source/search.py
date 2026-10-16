from math import sqrt
from kd_tree import KDtree

class StationManager:
    def __init__(self,kd_tree):
        self.kd_tree = kd_tree

    def find_nearest_station(self,latitude,longitude,limit = 5):
        if limit < 1 :
            raise ValueError ("Limit should be at least 1")

        stations = self.kd_tree.get_all_station()

        stations.sort(
            key = lambda station: sqrt(
                (station.latitude - latitude) **2
            + (station.longitude - longitude) **2
        ))

        return stations[:limit]

    def filter_by_city(self,city):
        results = []
        for station in self.kd_tree.get_all_station():
            if station.city.casefold() == city.casefold():
                results.append(station)
        return results
    
    def filter_by_charger_type(self,charger_type):
        results = []
        for station in self.kd_tree.get_all_station():
            if station.charger_type.casefold() == charger_type.casefold():
                results.append(station)
        return results

    def filter_availability(self):
        results = []
        for station in self.kd_tree.get_all_station():
            if station.available:
                results.append(station)
        return results
    