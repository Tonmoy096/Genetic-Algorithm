import random


def fitness(selected_batsmen, avg_runs, target_run):
    total_runs = sum(avg_runs[i] for i in range(
        len(selected_batsmen)) if selected_batsmen[i])
    return 1 if total_runs == target_run else 0


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(selected_batsmen, mutation_rate):
    for i in range(len(selected_batsmen)):
        if random.random() < mutation_rate:
            # Flip 0 to 1 or 1 to 0
            selected_batsmen[i] = 1 - selected_batsmen[i]
    return selected_batsmen


def create_population(num_batsmen, population_size):
    population = []
    for _ in range(population_size):
        selected_batsmen = [random.choice([0, 1]) for _ in range(num_batsmen)]
        population.append(selected_batsmen)
    return population


def genetic_algorithm(num_batsmen, avg_runs, target_run, population_size, max_iterations, mutation_rate):
    population = create_population(num_batsmen, population_size)
    for generation in range(max_iterations):
        fitness_scores = [fitness(selected_batsmen, avg_runs, target_run)
                          for selected_batsmen in population]

        # Check if the target run is achieved
        if 1 in fitness_scores:
            best_individual_index = fitness_scores.index(1)
            best_individual = population[best_individual_index]
            return best_individual

        # Check if all fitness scores are 0, meaning no valid combination is found
        if all(score == 0 for score in fitness_scores):
            return None

        selected_parents = random.choices(
            population, weights=fitness_scores, k=population_size)

        next_generation = []
        for i in range(0, population_size, 2):
            parent1 = selected_parents[i]
            parent2 = selected_parents[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])

        population = next_generation

    # If the target run is not achieved, return None
    return None


def main():
    num_batsmen, target_run = map(int, input().split())

    avg_runs = []
    for _ in range(num_batsmen):
        name, avg_run = input().split()
        avg_runs.append(int(avg_run))

    population_size = 100
    max_iterations = 1000
    mutation_rate = 0.1

    result = genetic_algorithm(
        num_batsmen, avg_runs, target_run, population_size, max_iterations, mutation_rate)

    if result is None:
        print("No valid combination found.")
    else:
        print("Players and their selection:")
        for i in range(num_batsmen):
            print(
                f"{avg_runs[i]} - {'Selected' if result[i] == 1 else 'Not Selected'}")

        print("Selected batsman array:", "".join(str(x) for x in result))


if __name__ == "__main__":
    main()
