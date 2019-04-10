from graph import Graph
from population import Population
from genetic import GeneticAlg

FILES_LIST = ["5", "10", "20", "50", "100"]
POPULATION_SIZE = 50
MUTATION_RATE = 0.1
TOURNAMENT_SIZES = [1, 2, 10]
ELITISM = True
MAX_EVOLVE_ITERATIONS = 1000
NUMBER_OF_CONFIRMATIONS = 100

for test in FILES_LIST:
    for tsize in TOURNAMENT_SIZES:    
        for x in range(20):
            FILE_PATH = f"../test_files/points-{test}.txt"
            graph = Graph()
            graph.init_with_coordinates_file(FILE_PATH)
            population = Population(population_size=POPULATION_SIZE, graph=graph)
            algorithm = GeneticAlg(MUTATION_RATE, tsize, ELITISM, graph.number_of_cities())
            last_result = 0
            result = 0
            confirmations = 0
            for i in range(0, MAX_EVOLVE_ITERATIONS):
                last_result = result
                result = population.get_fittest().get_distance()
                if last_result == population.get_fittest().get_distance():
                    confirmations += 1
                else:
                    confirmations = 0
                if confirmations == NUMBER_OF_CONFIRMATIONS:
                    break
                population = algorithm.evolve_population(population, graph)
                print(f'{i}/{MAX_EVOLVE_ITERATIONS} distance:{population.get_fittest().get_distance()}')
            print(f'distance: {population.get_fittest().get_distance()}')
            print(f'path: {population.get_fittest().get_tour_list()}')
            
            #print(last_result, file=open("last.txt", "a"))
            #print(i-1, file=open("iter.txt", "a"))
        #print("#", file=open("last.txt", "a"))
        #print("#", file=open("iter.txt", "a"))
    #print("@", file=open("last.txt", "a"))
    #print("@", file=open("iter.txt", "a"))