from random import shuffle

# A population ezekeből épül fel, egy utat reprezentál
class Tour:
    def __init__(self, tour_size):
        self.tour = []
        self.fitness = 0
        self.distance = 0
        #allokáció
        for i in range(0, tour_size):
            self.tour.append(None)

    # Random tour létrehozása
    def generate_individual(self, graph):
        for city_index in range(0, graph.number_of_cities()):
            self.set_city(city_index, graph.get_city(city_index))
        shuffle(self.tour)
    
    def get_tour_size(self) -> int:
        return len(self.tour)
    
    def get_city(self, index: int):
        return self.tour[index]

    def set_city(self, index, city):
        self.tour[index] = city
        # módosítás esetén újra kell számolni a fitness-t
        self.fitness = 0
        self.distance = 0

    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = 1/self.get_distance()
        return self.fitness
    
    def get_distance(self):
        if self.distance == 0:
            distance = 0
            for city_index, city in enumerate(self.tour):
                if city_index + 1 < len(self.tour):
                    distance += city.distanceTo(self.tour[city_index+1])
                else:
                    distance += city.distanceTo(self.tour[0])
            self.distance = distance
        return self.distance
    
    def contains_city(self, city):
        return city in self.tour
    
    def get_tour_list(self) -> list:
        return self.tour
        
