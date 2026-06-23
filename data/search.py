def binary_search_citizen(
    population_by_id,
    search_id
):
    left = 0
    right = len(population_by_id) - 1
    while left <= right:
        middle = (left + right) // 2
        if (
            population_by_id[middle].citizen_id
            == search_id
        ):
            return population_by_id[middle]
        elif (
            population_by_id[middle].citizen_id
            < search_id
        ):
            left = middle + 1
        else:
            right = middle - 1
    return None