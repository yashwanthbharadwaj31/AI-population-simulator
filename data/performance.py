import time
def measure_execution_time(function, data):
    start_time = time.perf_counter()
    function(data)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time
def compare_sorting_algorithms(
    population,
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort
):
    results = {}
    results["Bubble Sort"] = measure_execution_time(
        bubble_sort,
        population.copy()
    )
    results["Selection Sort"] = measure_execution_time(
        selection_sort,
        population.copy()
    )
    results["Insertion Sort"] = measure_execution_time(
        insertion_sort,
        population.copy()
    )
    results["Merge Sort"] = measure_execution_time(
        merge_sort,
        population.copy()
    )
    return results
def compare_search_algorithms(
    population,
    population_by_id,
    linear_search,
    binary_search,
    search_id
):
    results = {}
    results["Linear Search"] = measure_execution_time(
        lambda data: linear_search(data, search_id),
        population
    )
    results["Binary Search"] = measure_execution_time(
        lambda data: binary_search(data, search_id),
        population_by_id
    )
    return results