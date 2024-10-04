
def calculate_total_distance(n):
    distance = 10
    total_distance = 0 

    for day in range(n):
        total_distance += distance 
        distance += distance * 0.1

    return total_distance