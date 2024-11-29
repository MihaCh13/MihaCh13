import random
import matplotlib.pyplot as plt
import numpy as np


"""
To install the required libraries, run the following commands in the terminal:
pip install numpy
pip install matplotlib
"""


# Classroom size
classroom_width = 7
classroom_length = 5

# Wi-Fi access points
num_app = 5

# Population size
population_size = 12

# Number of generations
generations = 10

# Mutation rate (0.1 = 10%)
mutation_rate = 0.1

# Function to calculate the signal strength in a specific point
def calculate_signal_strength(_ap_x, _ap_y, _point_x, _point_y):
    distance = np.sqrt((_ap_x - _point_x) ** 2 + (_ap_y - _point_y) ** 2)

    # Reverse model of the distance
    return 1 / (distance + 1)


# Function to calculate the visualization of the initial and final positions of the access points
def visualize_initial_and_final(init_population, final_population):
    plt.figure(figsize=(15, 6))

    # Visualization of the initial positions with black numbers
    for i, (x, y) in enumerate(init_population):
        plt.text(x, y, str(i), color='black', fontsize=8, ha='center', va='center')

    plt.scatter(*zip(*init_population), color='red', marker='o', label='Initial Wi-Fi access points')

    # Visualization of the final positions with black numbers
    for i, (x, y) in enumerate(final_population):
        plt.text(x, y, str(i), color='black', fontsize=8, ha='center', va='center')

    plt.xlabel('Width of the classroom [m]')
    plt.ylabel('Length of the classroom [m]')
    plt.title('Initial and Final Wi-Fi Access Points locations')
    plt.legend()
    plt.show()


# Function to visualize dynamic changes
def visualize_dynamic_changes(classroom_w, classroom_l, curr_population, fitness_score):
    for current_gen in range(generations):
        plt.figure(figsize=(15, 6))

        # Heatmap of the current generation
        plt.subplot(1, 2, 1)

        ap_placements = curr_population[generations]
        x = np.linspace(0, classroom_w, 100)
        y = np.linspace(0, classroom_l, 100)

        X, Y = np.meshgrid(x, y)
        Z = np.zeros(X.shape)

        for app_x, app_y in ap_placements:
            Z += calculate_signal_strength(app_x, app_y, X, Y)

        plt.pcolormesh(X, Y, Z, shading='auto', cmap='viridis')
        plt.colorbar(label='Signal Strength')

        for i, (x, y) in enumerate(ap_placements):
            plt.text(x, y, str(i + 1), color='black', fontsize=8, ha='center', va='center')

        plt.scatter(*zip(*ap_placements), color='red', marker='o', label='Access Points Distribution')
        plt.xlabel('Width of the classroom [m]')
        plt.ylabel('Length of the classroom [m]')
        plt.title(f'Wi-Fi signal strength and distribution of access points in generation {current_gen + 1}')
        plt.legend()

        # Fitness score for all generations
        plt.subplot(1, 2, 2)
        plt.plot(range(1, current_gen + 2), fitness_score[:current_gen + 1], marker='o')
        plt.xlabel('Generations')
        plt.ylabel('Fitness Score')
        plt.title(f'Fitness Score for all generations')

        plt.tight_layout()
        plt.show()


# Initial population with random access points
initial_population = [(random.uniform(0, classroom_width), random.randint(0, classroom_length)) for _ in range(population_size)]
population = [initial_population.copy()]

# Variable to store best solutions
best_solution = None
best_fitness = float('-inf')
all_fitness_scores = []


# Optimization cycle for the genetic algorithm
for generation in range(generations):
    # Calculate the fitness score for each individual in the population
    fitness_scores = []

    for ap_x, ap_y in population[generation]:
        current_score = 0

        for point_x in range(classroom_width):
            for point_y in range(classroom_length):
                current_score += calculate_signal_strength(ap_x, ap_y, point_x, point_y)

        fitness_scores.append(current_score)

    # Store the best solution
    if max(fitness_scores) > best_fitness:
        best_solution = population[generation][fitness_scores.index(max(fitness_scores))]
        best_fitness = max(fitness_scores)

    # Save all fitness scores
    all_fitness_scores.append(max(fitness_scores))

    # Selection of parents for the next generation
    selected_parents = random.choices(population[generation], weights=fitness_scores, k=population_size)

    # Generate offspring with mutation
    offspring = []

    for _ in range(population_size):
        parent1, parent2 = random.sample(selected_parents, 2)

        crossover_x = random.uniform(parent1[0], parent2[0])
        crossover_y = random.uniform(parent1[1], parent2[1])

        offspring.append((crossover_x, crossover_y))

    # Apply mutation
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            offspring[i] = (random.uniform(0, classroom_width), random.uniform(0, classroom_length))

    # Add offspring to the population
    population.append(offspring)


# Print results
print(f"Best solution: {best_solution}")
print(f"Best fitness score: {best_fitness}")


# Visualize the initial and final positions of the access points
visualize_initial_and_final(initial_population, population[-1])


# Visualize dynamic changes
visualize_dynamic_changes(classroom_width, classroom_length, population, all_fitness_scores)


# Trajectory of the population
trajectory_scores = []

for gen in range(generations + 1):
    distances = [np.linalg.norm(np.array(point) - np.array(best_solution)) for point in population[gen]]
    trajectory_scores.append(np.mean(distances))

# Visualization of the trajectory of the population
plt.figure(figsize=(10, 6))
plt.plot(range(generations + 1), trajectory_scores, marker='o')
plt.xlabel('Generation')
plt.ylabel('Mean distance to the best solution')
plt.title(f'Population trajectory')
plt.show()

# Visualization of the similarity
plt.figure(figsize=(10, 6))
plt.plot(range(1, generations + 1), all_fitness_scores, marker='o')
plt.xlabel('Generation')
plt.ylabel('Best fitness score')
plt.title(f'Similarity graph')
plt.show()
