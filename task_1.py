import pulp

# Створення задачі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

# Цільова функція
model += lemonade + fruit_juice, "Total_Products"

# Обмеження
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "LemonJuice_Constraint"
model += 2 * fruit_juice <= 40, "FruitPuree_Constraint"

# Рішення задачі
model.solve()

# Вивід результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade produced: {pulp.value(lemonade)}")
print(f"Fruit Juice produced: {pulp.value(fruit_juice)}")
