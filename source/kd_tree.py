from station import Charging_station

class KDnote:
    def __init__(self,station,axis):
        self.station = station
        self.axis = axis
        self.left = None
        self.right = None

class KDtree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,station):
        if self.root == None:
            self.root = KDnote(station,0)
        else:
            self._insert_recursive(self.root,station)

        self.size += 1

    def _insert_recursive(self,node,station):
        axis = node.axis

        new_value = station.coordinates()[axis]
        node_value = node.station.coordinates()[axis]

        if new_value < node_value :
            if node.left == None:
                node.left = KDnote(station,1-axis)
            else:
                self._insert_recursive(node.left,station)

        else:
            if node.right == None:
                node.right = KDnote(station,1 - axis)
            else:
                self._insert_recursive(node.right,station)

    def search(self,latitude,longitude):
        coordinates = (latitude,longitude)
        return self._search_recursive(self.root,coordinates)

    def _search_recursive(self,node,coordinates):
        if node == None:
            return None

        if node.station.coordinates() == coordinates :
            return node.station

        axis = node.axis

        if coordinates[axis] < node.station.coordinates()[axis]:
            return self._search_recursive(node.left,coordinates)
        else:
            return self._search_recursive(node.right,coordinates)

    def range_search(self,min_lat,max_lat,min_lon,max_lon):
        results = []

        self._range_search_recursive(self.root,min_lat,max_lat,min_lon,max_lon,results
        )

        return results

    def _range_search_recursive(self,node,min_lat,max_lat,min_lon,max_lon,results):
        if node == None:
            return

        station = node.station
        lat = station.latitude
        lon = station.longitude

        if min_lat <= lat <= max_lat and min_lon <= lon <= max_lon:
            results.append(station)

        axis = node.axis 
        split_value = station.coordinates()[axis]

        if axis == 0:
            if min_lat <= split_value:
                self._range_search_recursive(node.left,min_lat,max_lat,min_lon,max_lon,results)
            if max_lat >= split_value:
                self._range_search_recursive(node.right,min_lat,max_lat,min_lon,max_lon,results)

        else:
            if min_lon <= split_value :
                self._range_search_recursive(node.left,min_lat,max_lat,min_lon,max_lon,results)
            if max_lon >= split_value:
                self._range_search_recursive(node.right,min_lat,max_lat,min_lon,max_lon,results)

    def get_size(self):
        return self.size

    def get_all_station(self):
        results = []
        self._collect_station(self.root,results)
        return results

    def _collect_station(self,node,results):
        if node == None:
            return 

        results.append(node.station)
        self._collect_station(node.left,results)
        self._collect_station(node.right,results)
