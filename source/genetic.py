from random import randint, random
from population import Population
from tour import Tour

class GeneticAlg:
    def __init__(self, mutation_rate, tournament_size, elistism, tour_size):
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elistism = elistism
        self.tour_size = tour_size


    def tournament_selection(self, population, graph):
        tournament = Population(self.tournament_size, graph, False)
        for i in range(0, self.tournament_size):
            randomIndex = randint(0,population.get_population_size()-1)
            tournament.save_tour(i, population.get_tour(randomIndex))
        fittest = tournament.get_fittest()
        return fittest
    
    #megcserélek 2 várost az útban mutáció esélye szerint
    def mutate(self, tour):
        for tour_index, city in enumerate(tour.get_tour_list()):
            if random() < self.mutation_rate:
                second_tour_index = randint(0, tour.get_tour_size()-1)
                second_city = tour.get_city(second_tour_index)
                tour.set_city(tour_index, second_city)
                tour.set_city(second_tour_index, city)

    def crossover(self, parent1, parent2):
        child = Tour(self.tour_size)
        start_pos = randint(0, parent1.get_tour_size()-1)
        end_pos = randint(0, parent1.get_tour_size()-1)
        # parent1 egy részét hozzáadjuk
        for i in range (0, child.get_tour_size()):
            if (start_pos < end_pos and i > start_pos and i < end_pos):
                child.set_city(i, parent1.get_city(i))
            elif (start_pos > end_pos):
                if (not (i < start_pos and i > end_pos)):
                    child.set_city(i, parent1.get_city(i))
        # parent2 betölti a maradékot
        for i in range (0, parent2.get_tour_size()):
            if (not child.contains_city(parent2.get_city(i))):
                for j in range (0, child.get_tour_size()):
                    if (child.get_city(j) == None):
                        child.set_city(j, parent2.get_city(i))
                        break
        return child

    def evolve_population(self, population, graph):
        new_population = Population(population.get_population_size(), graph, False)
        elistism_offset = 0
        if self.elistism:
            new_population.save_tour(0, population.get_fittest())
            elistism_offset = 1
        # gyerek generálása, ha az elitism igaz, akkor azt tobvábbmentjük
        for i in range (elistism_offset, population.get_population_size()):
            parent1 = self.tournament_selection(population, graph)
            parent2 = self.tournament_selection(population, graph)
            child = self.crossover(parent1, parent2)
            new_population.save_tour(i, child)
        # mutáció
        for i in range (elistism_offset, population.get_population_size()):
            self.mutate(new_population.get_tour(i))
        
        return new_population