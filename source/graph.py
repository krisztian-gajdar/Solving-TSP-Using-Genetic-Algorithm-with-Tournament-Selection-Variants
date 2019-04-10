from city import City

class Graph:
    def __init__(self):
        self.cities_to_visit = []
        self.cities_file_count = 0

    def add_city(self, city):
        self.cities_to_visit.append(city)
    
    def get_city(self, index):
        return self.cities_to_visit[index]
    
    def number_of_cities(self):
        return len(self.cities_to_visit)

    #beolvas egy file-t, aminek első sora a csúcsok száma
    #sorok a csúcsokat jelentik, space-el elváálasztva x és y koordináták
    def init_with_coordinates_file(self, input_path):
        input_file = open(input_path, "r")
        self.cities_file_count = int(input_file.readline())
        for index, line in enumerate(input_file):
            coord_list = line.split(" ")
            coord_list[1] = coord_list[1].split("\n")[0]
            new_city = City(int(coord_list[0]), int(coord_list[1]), index)
            self.add_city(new_city)
        input_file.close()
