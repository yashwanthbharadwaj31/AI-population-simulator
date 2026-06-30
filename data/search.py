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
def search_by_age(
    population,
    age
):
    results = []
    for citizen in population:
        if citizen.age == age:
            results.append(citizen)
    return results
def search_by_income(
    population,
    income
):
    results = []
    for citizen in population:
        if citizen.income == income:
            results.append(citizen)
    return results
def search_by_education(
    population,
    education
):
    results = []
    for citizen in population:
        if citizen.education.lower() == education.lower():
            results.append(citizen)
    return results
def search_by_employment_status(
    population,
    employment_status
):
    results = []
    for citizen in population:
        if (
            citizen.employment_status.lower()
            == employment_status.lower()
        ):
            results.append(citizen)
    return results
def filter_by_income_threshold(
    population,
    minimum_income
):
    results = []
    for citizen in population:
        if citizen.income >= minimum_income:
            results.append(citizen)
    return results
def filter_senior_citizens(
    population
):
    results = []
    for citizen in population:
        if citizen.age >= 60:
            results.append(citizen)
    return results
def filter_graduates(
    population
):
    results = []
    for citizen in population:
        if citizen.education.lower() == "graduate":
            results.append(citizen)

    return results