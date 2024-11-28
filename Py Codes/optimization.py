import random
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Ширина и дължина на учебната зала в метри
classroom_width = 7
classroom_length = 5

# Брой точки за достъп до Wi-Fi
num_app = 5

# Големина на популацията от различни разпределения на точките за достъп
population_size = 12

# Брой поколения, през които ще се извършва оптимизацията
generations = 10

# Скорост на мутация - вероятността за случайно изменениена позицията на точка при генериране на ново поколение
mutation_rate = 0.1


# функция за изчисляване на силата на сигнала
def calculate_signal_strength(ap_x, ap_y, point_x, point_y):
    distance = np.sqrt((ap_x - point_x) ** 2 + (ap_y - point_y) ** 2)
    return 1 / (distance + 1)  # Обратен модел на разстоянието


# Функция за визуализация на началните случайни точки и крайното разпределение на точките за достъп
def visualize_initial_and_final(classroom_width, classroom_length, initial_population, final_population):
    plt.figure(figsize=(15, 6))

    # Изобразяване на началните случайни точки с номера в черно
    for i, (x, y) in enumerate(initial_population):
        plt.text(x, y, str(i + 1), color="black", fontsize=8, ha="center", va="center")
    plt.scatter(*zip(*initial_population), color="red", marker="o",
                label="Начална позиция на точките за достъп до Wi-Fi")

    # Изобразяване на крайното разпределение на точките за достъп с номера в черно
    for i, (x, y) in enumerate(final_population):
        plt.text(x, y, str(i + 1), color="black", fontsize=8, ha="center", va="center")
    plt.scatter(*zip(*final_population), color="blue", marker="o",
                label="Финална позиция на точките за достъп до Wi-Fi")

    plt.xlabel("Ширина на учебна зала (м)")
    plt.ylabel("Дължина на учебна зала (м)")
    plt.title("Начало и крайно разпределение на точките за достъп")
    plt.legend()
    plt.show()


# Функция за динамично визуализиране на промените в разположението на точките за достъп и фитнес резултатите през поколенията
def visualize_dynamic_changes(classroom_width, classroom_length, population, fitness_scores):
    for generation in range(len(population)):
        plt.figure(figsize=(15, 6))

        # Начертаване на топлинната карта за текущото поколение
        plt.subplot(1, 2, 1)
        ap_placements = population[generation]
        x = np.linspace(0, classroom_width, 100)
        y = np.linspace(0, classroom_length, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        for ap_x, ap_y in ap_placements:
            Z += calculate_signal_strength(ap_x, ap_y, X, Y)
        plt.pcolormesh(X, Y, Z, shading="auto", cmap="viridis")
        plt.colorbar(label="Сила на сигнала")
        for i, (x, y) in enumerate(ap_placements):
            plt.text(x, y, str(i + 1), color="black", fontsize=8, ha="center", va="center")
        plt.scatter(*zip(*ap_placements), color="red", marker="o", label="Разпределение на точките за достъп")
        plt.xlabel("Ширина на учебна зала (м)")
        plt.ylabel("Дължина на учебна зала (м)")
        plt.title(f"Сила на Wi-Fi сигнала и разпределение на точките за достъп (Поколение {generation + 1})")
        plt.legend()

        # Изобразяване на графиката на фитнеса за всички поколения
        plt.subplot(1, 2, 2)
        plt.plot(range(1, generation + 2), fitness_scores[:generation + 1], marker="o")
        plt.xlabel("Поколение")
        plt.ylabel("Резултат от фитнеса")
        plt.title("Резултат от фитнеса за различните поколения")

        plt.tight_layout()
        plt.show()


# Инициализирайте популацията със случайни разпределения на точките за достъп
initial_population = [(random.uniform(0, classroom_width), random.uniform(0, classroom_length)) for _ in
                      range(population_size)]
population = [initial_population.copy()]

# Променливи за проследяване на най-доброто решение и резултатите фитнеса
best_solution = None
best_fitness = float("-inf")
all_fitness_scores = []

# оптимизационен цикъл на генетичния алгоритъм:
for generation in range(generations):
    # Оценка на фитнеса на всеки индивид в популацията
    fitness_scores = []
    for ap_x, ap_y in population[generation]:
        coverage = 0
        for point_x in range(classroom_width):
            for point_y in range(classroom_length):
                coverage += calculate_signal_strength(ap_x, ap_y, point_x, point_y)
        fitness_scores.append(coverage)

    # Актуализация на най-доброто решение ако е намерено
    if max(fitness_scores) > best_fitness:
        best_solution = population[generation][fitness_scores.index(max(fitness_scores))]
        best_fitness = max(fitness_scores)

    # Запазване на всички резултати от фитнеса
    all_fitness_scores.append(max(fitness_scores))

    # Избор на родители на база на резултатите от фитнеса
    selected_parents = random.choices(population[generation], weights=fitness_scores, k=population_size)

    # Създаване на потомдтво чрез кръстосване
    offspring = []
    for _ in range(population_size):
        parent1, parent2 = random.sample(selected_parents, 2)
        crossover_x = random.choice([parent1[0], parent2[0]])
        crossover_y = random.choice([parent1[1], parent2[1]])
        offspring.append((crossover_x, crossover_y))

    # Прилагане на мутация
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            offspring[i] = (random.uniform(0, classroom_width), random.uniform(0, classroom_length))

    # Замяна на старото население с ново поколение
    population.append(offspring)

# Извеждане на най-доброто решение и неговия фитнес
print("Най-добро разпределение на точките за достъп:", best_solution)
print("Най-добро покритие:", best_fitness)
