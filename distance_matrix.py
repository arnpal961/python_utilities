import sys
import csv
import pickle
import googlemaps
from copy import deepcopy
from itertools import product
from collections import defaultdict
from settings import CALIFORNICATION
from settings import MAP_API_KEY

def get_distance_matrix(api_key):
    pass

if __name__ == "__main__":
    with open(CALIFORNICATION, "r") as fd:
        reader = csv.reader(fd)
        locations = list(map(lambda x: x[1], reader))[1:]
    locations_copy = deepcopy(locations)
    locations_dict = defaultdict(list)
    for loc in locations:
        locations_copy.remove(loc)
        if len(locations_copy) > 0:
            location_chunks = [locations_copy[x:x+25] for x in range(0, len(locations_copy), 25)]
            locations_dict[loc].extend(location_chunks)
    

    gmap_client = googlemaps.Client(key=MAP_API_KEY)
    
    count = 0
    distance_matrix_list = []
    for orig, dests in locations_dict.items():
        for dest in dests:
            matrix = gmap_client.distance_matrix([orig], dest)
            distance_matrix_list.append(matrix)
            count += 1
            sys.stdout.write("\rTotal requests made => %d" %(count))

    distance_list = [] 
    for matrix in distance_matrix_list: 
        city1 = matrix['origin_addresses'][0] 
        for city2, res in zip(matrix['destination_addresses'],matrix['rows'][0]['elements']): 
            dct = {"place1": city1, "place2": city2} 
            del res["status"] 
            dct.update(res) 
            distance_list.append(dct) 

    with open("data_dir/distance_matrix.pkl", "wb") as fd: 
        pickle.dump(distance_list, fd)