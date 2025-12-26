# Необхідно написати програму на Python,
# яка використовує два підходи —
# жадібний алгоритм та алгоритм динамічного програмування
# для розв’язання задачі вибору їжі
# з найбільшою сумарною калорійністю в межах обмеженого бюджету.

# Кожен вид їжі має вказану вартість і калорійність.
# Дані про їжу представлені у вигляді словника,
# де ключ — назва страви,
# а значення — це словник з вартістю та калорійністю.

# Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
# Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті


def greedy_algorithm(menu_items, budget):
    """Жадібний алгоритм для вибору страв з максимальною калорійністю в межах бюджету."""

    # Обчислюємо співвідношення калорій до вартості для кожної страви
    items_sorted_by_ratio = sorted(menu_items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    print("Items sorted by calories/cost ratio:")
    for sorted_item in items_sorted_by_ratio:
        print(f"\t{sorted_item[0]}: calories/cost ratio = {sorted_item[1]['calories'] / sorted_item[1]['cost']:.2f}")

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item_name, info_dict in items_sorted_by_ratio:
        item_cost = info_dict["cost"]
        item_calories = info_dict["calories"]

        if total_cost + item_cost <= budget:
            selected_items.append(item_name)
            total_cost += item_cost
            total_calories += item_calories

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    """Алгоритм динамічного програмування для вибору страв з максимальною калорійністю в межах бюджету."""

    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]  # Ініціалізація таблиці DP
    item_list = list(items.items())  # Перетворення словника в список для індексації

    for i in range(1, n + 1):  # Ітеруємо по кожному предмету в item_list
        item, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)  # Вибираємо максимум між включенням та виключенням предмета
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items = []
    for i in range(n, 0, -1):  # Відстежуємо вибрані предмети
        if dp[i][w] != dp[i - 1][w]:  # Якщо значення змінилося, предмет був включений
            item, info = item_list[i - 1]
            selected_items.append(item)  # Додаємо предмет до вибраних
            w -= info["cost"]  # Зменшуємо залишковий бюджет

    total_cost = 0  # Обчислюємо загальну вартість вибраних предметів
    for item in selected_items:
        total_cost += items[item]["cost"]

    total_calories = dp[n][budget]  # Загальна калорійність - це максимальне значення в таблиці DP

    return selected_items, total_cost, total_calories


if __name__ == "__main__":

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    print("\nItems to choose from:")
    for item in items:
        print(f"\t{item}: cost = {items[item]['cost']}, calories = {items[item]['calories']}")

    budget = 100

    print("\nGreedy Algorithm Selection:")
    greedy_selection, greedy_cost, greedy_calories = greedy_algorithm(items, budget)

    print("Selected Items:", greedy_selection)
    print("Total Cost:", greedy_cost)
    print("Total Calories:", greedy_calories)

    dp_selection, dp_cost, dp_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming Selection:")
    print("Selected Items:", dp_selection)
    print("Total Cost:", dp_cost)
    print("Total Calories:", dp_calories)
