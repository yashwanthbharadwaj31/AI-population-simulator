def merge_sort_income(citizens):
    if len(citizens) <= 1:
        return citizens
    middle = len(citizens) // 2
    left = merge_sort_income(citizens[:middle])
    right = merge_sort_income(citizens[middle:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].income > right[j].income:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result    
def merge_sort_health(citizens):
    if len(citizens) <= 1:
        return citizens
    middle = len(citizens) // 2
    left = merge_sort_health(citizens[:middle])
    right = merge_sort_health(citizens[middle:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].health_score > right[j].health_score:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result  
def merge_sort_happiness(citizens):
    if len(citizens) <= 1:
        return citizens
    middle = len(citizens) // 2
    left = merge_sort_happiness(citizens[:middle])
    right = merge_sort_happiness(citizens[middle:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].happiness_score > right[j].happiness_score:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result  
def bubble_sort_income(citizens):
    sorted_citizens = citizens.copy()
    n = len(sorted_citizens)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_citizens[j].income < sorted_citizens[j + 1].income:
                sorted_citizens[j], sorted_citizens[j + 1] = (
                    sorted_citizens[j + 1],
                    sorted_citizens[j]
                )
                swapped = True
        if not swapped:
            break
    return sorted_citizens
def selection_sort_income(citizens):
    sorted_citizens = citizens.copy()
    n = len(sorted_citizens)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if sorted_citizens[j].income > sorted_citizens[max_index].income:
                max_index = j
        sorted_citizens[i], sorted_citizens[max_index] = (
            sorted_citizens[max_index],
            sorted_citizens[i]
        )
    return sorted_citizens
def insertion_sort_income(citizens):
    sorted_citizens = citizens.copy()
    for i in range(1, len(sorted_citizens)):
        current = sorted_citizens[i]
        j = i - 1
        while (
            j >= 0 and
            sorted_citizens[j].income < current.income
        ):
            sorted_citizens[j + 1] = sorted_citizens[j]
            j -= 1
        sorted_citizens[j + 1] = current
    return sorted_citizens