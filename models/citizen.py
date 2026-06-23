class Citizen:
    def __init__(
    self,
    citizen_id,
    age,
    gender,
    education,
    income,
    employment_status,
    experience_years,
    health_score,
    happiness_score
):
        self.citizen_id = citizen_id
        self.age = age
        self.gender = gender
        self.education = education
        self.income = income
        self.employment_status = employment_status
        self.experience_years = experience_years
        self.health_score = health_score
        self.happiness_score = happiness_score
    def display(self):
        print(
            self.citizen_id,
            self.age,
            self.gender,
            self.education,
            self.income
        )