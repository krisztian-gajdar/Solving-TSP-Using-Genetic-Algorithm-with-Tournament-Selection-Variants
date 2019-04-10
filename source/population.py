from tour import Tour

class Population:
    #'initialise' hamis lesz, ha nem kell tour-okat létrehozni
    def __init__(self, population_size, graph, initialise=True):
        self.tours = []

        for _ in range(0, population_size):
            newTour = Tour(graph.number_of_cities())
            self.tours.append(newTour)
        if initialise:
            for tour in self.tours:
                tour.generate_individual(graph)
    
    def get_tour(self, tour_index):
        return self.tours[tour_index]
    
    def get_fittest(self):
        fittest = self.tours[0]
        for tour in self.tours:
            if tour.get_fitness() > fittest.get_fitness():
                fittest = tour
        return fittest
    
    def get_population_size(self):
        return len(self.tours)

    def save_tour(self, index, tour):
        self.tours[index] = tour