def get_age_distribution(population):
    age_distribution = {
        "18-25": 0,
        "26-40": 0,
        "41-60": 0,
        "60+": 0
    }
    for citizen in population:
        if citizen.age <= 25:
            age_distribution["18-25"] += 1
        elif citizen.age <= 40:
            age_distribution["26-40"] += 1
        elif citizen.age <= 60:
            age_distribution["41-60"] += 1
        else:
            age_distribution["60+"] += 1
    return age_distribution
def get_education_distribution(population):
    education_distribution = {
        "School": 0,
        "Graduate": 0,
        "Post Graduate": 0
    }
    for citizen in population:
        education_distribution[
            citizen.education
        ] += 1
    return education_distribution
def get_employment_distribution(population):
    employment_distribution = {
        "Student": 0,
        "Employed": 0,
        "Unemployed": 0
    }
    for citizen in population:
        employment_distribution[
            citizen.employment_status
        ] += 1
    return employment_distribution
def get_income_distribution(population):

    income_distribution = {
        "Low Income": 0,
        "Middle Income": 0,
        "High Income": 0,
        "Very High Income": 0
    }

    for citizen in population:
        if citizen.income < 30000:
            income_distribution["Low Income"] += 1
        elif citizen.income < 60000:
            income_distribution["Middle Income"] += 1
        elif citizen.income < 90000:
            income_distribution["High Income"] += 1
        else:
            income_distribution["Very High Income"] += 1
    return income_distribution
def get_health_distribution(population):
    health_distribution = {
        "Healthy": 0,
        "Average": 0,
        "At Risk": 0
    }
    for citizen in population:
        if citizen.health_score >= 80:
            health_distribution["Healthy"] += 1
        elif citizen.health_score >= 60:
            health_distribution["Average"] += 1
        else:
            health_distribution["At Risk"] += 1
    return health_distribution
def get_happiness_distribution(population):
    happiness_distribution = {
        "Happy": 0,
        "Neutral": 0,
        "Unhappy": 0
    }
    for citizen in population:
        if citizen.happiness_score >= 80:
            happiness_distribution["Happy"] += 1
        elif citizen.happiness_score >= 60:
            happiness_distribution["Neutral"] += 1
        else:
            happiness_distribution["Unhappy"] += 1
    return happiness_distribution