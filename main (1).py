import math
from sport_module import calculate_total_distance 
def calculate_z(m):
    if m >= 0: 
        z = 1 / (math.sqrt(m) + 2)
        return z
    else:
        return "Помилка: m повинно бути невід'ємним числом"
if __name__ == "__main__":
    m = float(input("Введіть число m для обчислення z: "))
    z = calculate_z(m)
    print(f"Результат обчислення z: {z:.2f}")
    n = int(input("Введіть кількість днів n для обчислення шляху спортсмена: "))
    total_distance = calculate_total_distance(n)
    print(f"Сумарний шлях спортсмена за {n} днів: {total_distance:.2f} км")
