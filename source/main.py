from kd_tree import KDtree
from dataloader import Station_data_loader
from search import StationManager

stations = Station_data_loader.load_json("E:\\python\\EV project\\data\\stations.json")
kd_tree = KDtree()

for station in stations:
    kd_tree.insert(station)

print(f"Total station loaded : ", kd_tree.get_size())

manager = StationManager(kd_tree)


def coordinates_search():
    latitude = float(input("Enter the latitude"))
    longitude = float(input("Enter the longitude"))
    station = kd_tree.search(latitude,longitude)
    if station is not None:
        print(station)
    else:
        print("There is no station in the particular coordinates")

def range_search():
    min_lat = float(input("Input minimum latitude : "))
    max_lat = float(input("Input maximum latitude : "))
    min_lon = float(input("Input minimum longitude : "))
    max_lon = float(input("Input maximum longitude : "))
    reslts = kd_tree.range_search(min_lat,max_lat,min_lon,max_lon)

    for station in reslts:
        print(station)

def city_search():
    cityname = input("Enter the city name : ")
    city_station = manager.filter_by_city(cityname)
    if len(city_station) > 0 :
        for station in city_station:
            print(station)
    else:
        print("No station found")

def avilability():
    available_stations = manager.filter_availability()
    if len(available_stations) > 0 :
        for station in available_stations :
            print(station)
    else:
        print("No station available rn ")

def nearest_station():
    latitude = float(input("Enter ur latitude : "))
    longitude = float(input("Enter ur longitude : "))
    limit = int(input("Enter your limit of station : "))

    nearest_stations = manager.find_nearest_station(latitude,longitude,limit)

    for station in nearest_stations:
        print(station)


def main():
    while True:

        print("1 - search statioin by coordinates .")
        print("2 - search stations by range . ")
        print("3 - filter stations by city . ")
        print("4 - available staions within range . ")
        print("5 - find nearest station .")
        print("6 - exit ")

        userinput = int(input("Select your want (1-5) : "))

        if userinput == 1:
            coordinates_search()
        elif userinput == 2:
            range_search()
        elif userinput == 3:
            city_search()
        elif userinput == 4:
            avilability()
        elif userinput == 5:
            nearest_station()
        elif userinput == 6:
            break
        else:
            return 
   

if __name__ == "__main__":
    main()


