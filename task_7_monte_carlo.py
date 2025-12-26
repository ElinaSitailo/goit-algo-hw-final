# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
# Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках.
# Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

# На основі проведених імітацій створіть графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
# Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def monte_carlo_dice_simulation(num_simulations):
    """Імітація кидків двох кубиків та обчислення ймовірностей сум."""
    sum_counts = {i: 0 for i in range(2, 13)}  # Ініціалізація лічильника для сум від 2 до 12

    for _ in range(num_simulations):
        die1 = np.random.randint(1, 7)  # Кидок першого кубика
        die2 = np.random.randint(1, 7)  # Кидок другого кубика
        total = die1 + die2
        sum_counts[total] += 1  # Підрахунок суми

    probabilities = {}
    for sum_value in range(2, 13):
        probability = sum_counts[sum_value] / num_simulations
        probabilities[sum_value] = probability

    return probabilities


def analytical_probability(sum_value):
    """Обчислення аналітичної ймовірності для заданої суми при киданні двох кубиків."""
    if sum_value < 2 or sum_value > 12:
        return 0.0

    # Кількість способів отримати кожну суму
    ways = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}

    total_outcomes = 36  # Загальна кількість можливих результатів при киданні двох кубиків
    return ways[sum_value] / total_outcomes


def compare_simulation_with_analytical(probabilities):
    """Порівняння ймовірностей з симуляції з аналітичними ймовірностями."""
    print("Сума\tІмітація\tАналітична\tРізниця (%)")
    for sum_value in range(2, 13):
        sim_prob = probabilities[sum_value]
        anal_prob = analytical_probability(sum_value)
        difference = abs(sim_prob - anal_prob) / anal_prob * 100 if anal_prob != 0 else 0
        print(f"{sum_value}\t{sim_prob:.4f}\t\t{anal_prob:.4f}\t\t{difference:.2f}")


def plot_probabilities(probabilities):
    """Побудова графіка ймовірностей сум."""
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color="skyblue")
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.xticks(sums)
    plt.ylim(0, max(probs) * 1.1)
    plt.grid(axis="y")
    plt.show()


if __name__ == "__main__":
    num_simulations = 1000000  # Кількість імітацій
    probabilities = monte_carlo_dice_simulation(num_simulations)
    compare_simulation_with_analytical(probabilities)
    plot_probabilities(probabilities)
