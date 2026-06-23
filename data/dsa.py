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