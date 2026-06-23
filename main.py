import sqlite3
import random
from models.citizen import Citizen
from data.dsa import (
    merge_sort_income,
    merge_sort_health,
    merge_sort_happiness
)
from data.analytics import (
    get_age_distribution,
    get_education_distribution,
    get_employment_distribution,
    get_income_distribution,
    get_health_distribution,
    get_happiness_distribution
)
from data.search import binary_search_citizen
from reports.report_generator import (
    generate_report,
    generate_analytics_report
)
import csv
print("Program Started")
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS population")
cursor.execute("""
CREATE TABLE IF NOT EXISTS population (
    citizen_id INTEGER PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    education TEXT,
    income INTEGER,
    employment_status TEXT,
    experience_years INTEGER,
    health_score INTEGER,
    happiness_score INTEGER
)
""")
population = []
citizen_income_data = []
for citizen_id in range(1, 1001):
    age =  random.randint(18,70)
    if age <= 22:
        employment_status = "Student"
        experience_years = 0
    elif age <=30:
        employment_status = random.choice([
            "Employed",
            "Unemployed"
        ])    
        experience_years = random.randint(0, 8)
    else:
        employment_status = random.choice([
            "Employed",
            "Unemployed"
        ])    
        experience_years = random.randint(5, age - 22)
    income = 15000 + (experience_years * 2500)
    income += random.randint(-5000, 5000)
    if income < 15000:
         income = 15000
    citizen = Citizen(
    citizen_id,
    age,
    random.choice(["Male", "Female"]),
    random.choice([
        "School",
        "Graduate",
        "Post Graduate"
    ]),
    income,
    employment_status,
    experience_years,
    random.randint(50, 100),
    random.randint(40, 100)
)
    population.append(citizen)
    citizen_income_data.append(
    (
        citizen.citizen_id,
        citizen.income
    )
)
for citizen in population:
    cursor.execute(
        """
        INSERT INTO population
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            
        citizen.citizen_id,
        citizen.age,
        citizen.gender,
        citizen.education,
        citizen.income,
        citizen.employment_status,
        citizen.experience_years,
        citizen.health_score,
        citizen.happiness_score
)
        )
    
print()
print(
    "Population Generated:",
    len(population),
    "Citizens"
)    
cursor.execute("SELECT COUNT(*) FROM population")
total_population = cursor.fetchone()[0]
print("Database Records:", total_population)
cursor.execute("""
SELECT COUNT(*)
FROM population
WHERE employment_status = 'Employed'
""")
employed_count = cursor.fetchone()[0]
cursor.execute("""
SELECT COUNT(*)
FROM population
WHERE employment_status = 'Unemployed'
""")
unemployed_count = cursor.fetchone()[0]
cursor.execute("""
SELECT COUNT(*)
FROM population
WHERE employment_status = 'Student'
""")
student_count = cursor.fetchone()[0]
cursor.execute("""
SELECT AVG(income)
FROM population
""")
average_income = round(cursor.fetchone()[0], 2)
cursor.execute("""
SELECT AVG(health_score)
FROM population
""")
average_health = round(cursor.fetchone()[0], 2)
cursor.execute("""
SELECT AVG(happiness_score)
FROM population
""")
average_happiness = round(cursor.fetchone()[0], 2)
print()
print("Population Analytics")
print("--------------------")
print("Employed Citizens:", employed_count)
print("Unemployed Citizens:", unemployed_count)
print("Average Income:", average_income)
print("Average Health Score:", average_health)
print("Average Happiness Score:", average_happiness)
age_distribution = get_age_distribution(
    population
)
education_distribution = (
    get_education_distribution(
        population
    )
)
employment_distribution = (
    get_employment_distribution(
        population
    )
)
income_distribution = (
    get_income_distribution(
        population
    )
)
health_distribution = (
    get_health_distribution(
        population
    )
)
happiness_distribution = (
    get_happiness_distribution(
        population
    )
)
print()
print("Age Distribution")
print("----------------")
for group, count in age_distribution.items():
    print(group, ":", count)
print()
print("Education Distribution")
print("----------------------")
for education, count in education_distribution.items():
    print(education, ":", count)
print()
print("Employment Distribution")
print("-----------------------")
for status, count in employment_distribution.items():
    print(status, ":", count)    
print()
print("Income Distribution")
print("-------------------")

for income_group, count in income_distribution.items():
    print(
        income_group,
        ":",
        count
    )
print()
print("Health Distribution")
print("-------------------")

for health_group, count in health_distribution.items():
    print(
        health_group,
        ":",
        count
    )    
print()
print("Happiness Distribution")
print("----------------------")

for happiness_group, count in happiness_distribution.items():
    print(
        happiness_group,
        ":",
        count
    )        
print()
print("Top 5 Richest Citizens")
print("----------------------")
sorted_citizens = merge_sort_income(population)
for citizen in sorted_citizens[:5]:
    print(
    "ID:", citizen.citizen_id,
    "| Age:", citizen.age,
    "| Status:", citizen.employment_status,
    "| Income:", citizen.income
)
print()
print("Top 5 Healthiest Citizens")
print("-------------------------")
sorted_health = merge_sort_health(population)
for citizen in sorted_health[:5]:
    print(
        "ID:", citizen.citizen_id,
        "| Age:", citizen.age,
        "| Status:", citizen.employment_status,
        "| Health:", citizen.health_score
    )
sorted_happiness = merge_sort_happiness(population)
print()
print("Top 5 Happiest Citizens")
print("-------------------------")
for citizen in sorted_happiness[:5]:
    print(
        "ID:", citizen.citizen_id,
        "| Age:", citizen.age,
        "| Status:", citizen.employment_status,
        "| Happiness:", citizen.happiness_score
    )
print("========================================")
print("POPULATION REPORT")
print("========================================")
print("Total Population:", total_population)
print("Students:", student_count)
print("Employed:", employed_count)
print("Unemployed:", unemployed_count)
print("Average Income:", average_income)
print("Average Health Score:", average_health)
print("Average Happiness Score:", average_happiness)
print("========================================")  
print("Sample Citizens") 
print()
for citizen in population[:5]:
    print(
        citizen.citizen_id,
        citizen.age,
        citizen.employment_status,
        citizen.health_score,
        citizen.happiness_score
    )
print()
print("Binary Search Test")
print("------------------")
population_by_id = sorted(
    population,
    key=lambda citizen: citizen.citizen_id
)
while True:
    search_id = int(input("Enter Citizen ID: "))
    found_citizen = binary_search_citizen(
    population_by_id,
    search_id
)
    if found_citizen:
        print()
        print("Citizen Found")
        print("-------------")
        print("ID:", found_citizen.citizen_id)
        print("Age:", found_citizen.age)
        print("Income:", found_citizen.income)
        print("Status:", found_citizen.employment_status)
        print("Gender:", found_citizen.gender)
        print("Education:", found_citizen.education)
        print("Experience:", found_citizen.experience_years)
        print("Health Score:", found_citizen.health_score)
        print("Happiness Score:", found_citizen.happiness_score)
    else:
        print()
        print("Citizen Not Found")
    print()
    choice = input(
        "Search another citizen? (y/n): "
    )
    if choice.lower() != "y":
        break
print()
print("Exporting Population Data...")
csv_file = open(
    "exports/population_data.csv",
    "w",
    newline=""
)
writer = csv.writer(csv_file)
writer.writerow([
    "Citizen ID",
    "Age",
    "Gender",
    "Education",
    "Income",
    "Employment Status",
    "Experience Years",
    "Health Score",
    "Happiness Score"
])
for citizen in population:
    writer.writerow([
        citizen.citizen_id,
        citizen.age,
        citizen.gender,
        citizen.education,
        citizen.income,
        citizen.employment_status,
        citizen.experience_years,
        citizen.health_score,
        citizen.happiness_score
    ])
csv_file.close()
print("CSV Export Successful")    
top_csv = open(
    "exports/top_citizens.csv",
    "w",
    newline=""
)
writer = csv.writer(top_csv)
writer.writerow([
    "Rank",
    "Category",
    "Citizen ID",
    "Age",
    "Employment Status",
    "Value"
])
rank = 1
for citizen in sorted_citizens[:5]:
    writer.writerow([
    rank,
    "Richest",
    citizen.citizen_id,
    citizen.age,
    citizen.employment_status,
    citizen.income
])
    rank += 1
rank = 1
for citizen in sorted_health[:5]:
    writer.writerow([
    rank,
    "Healthiest",
    citizen.citizen_id,
    citizen.age,
    citizen.employment_status,
    citizen.health_score
])
    rank += 1
rank = 1
for citizen in sorted_happiness[:5]:
    writer.writerow([
    rank,
    "Happiest",
    citizen.citizen_id,
    citizen.age,
    citizen.employment_status,
    citizen.happiness_score
])
    rank += 1
top_csv.close()
print("Top Citizens CSV Exported")
print()
print("Exporting Top Earners From Database...")
cursor.execute("""
SELECT citizen_id,
       age,
       income,
       employment_status
FROM population
ORDER BY income DESC
LIMIT 10
""")
top_earners = cursor.fetchall()
top_earners_csv = open(
    "exports/top_earners_db.csv",
    "w",
    newline=""
)
writer = csv.writer(top_earners_csv)
writer.writerow([
    "Citizen ID",
    "Age",
    "Income",
    "Employment Status"
])
for citizen in top_earners:
    writer.writerow(citizen)
top_earners_csv.close()
print("Top Earners DB Export Complete")    
print()
print("Exporting Top Healthiest From Database...")
cursor.execute("""
SELECT citizen_id,
       age,
       health_score,
       employment_status
FROM population
ORDER BY health_score DESC
LIMIT 10
""")
top_healthiest = cursor.fetchall()
health_csv = open(
    "exports/top_healthiest_db.csv",
    "w",
    newline=""
)
writer = csv.writer(health_csv)
writer.writerow([
    "Citizen ID",
    "Age",
    "Health Score",
    "Employment Status"
])
for citizen in top_healthiest:
    writer.writerow(citizen)
health_csv.close()
print(
    "Top Healthiest DB Export Complete"
)
print()
print("Database Insights")
print("-----------------")
cursor.execute("""
SELECT MAX(income)
FROM population
""")
highest_income = cursor.fetchone()[0]
print(
    "Highest Income:",
    highest_income
)
cursor.execute("""
SELECT MIN(income)
FROM population
""")
lowest_income = cursor.fetchone()[0]
print(
    "Lowest Income:",
    lowest_income
)
cursor.execute("""
SELECT employment_status,
       ROUND(AVG(income), 2)
FROM population
GROUP BY employment_status
""")
income_stats = cursor.fetchall()
print()
print("Income By Employment Status")
print("---------------------------")
for row in income_stats:
    print(
        row[0],
        ":",
        row[1]
    )
insights_file = open(
    "reports/database_insights.txt",
    "w"
)    
insights_file.write(
    "DATABASE INSIGHTS\n"
)
insights_file.write(
    "=================\n\n"
)
insights_file.write(
    f"Highest Income: {highest_income}\n"
)
insights_file.write(
    f"Lowest Income: {lowest_income}\n\n"
)
insights_file.write(
    "Income By Employment Status\n"
)
insights_file.write(
    "---------------------------\n"
)
for row in income_stats:
    insights_file.write(
        f"{row[0]} : {row[1]}\n"
    )
insights_file.close()
print()
print(
    "Database Insights Report Generated"
)   
summary_csv = open(
    "exports/database_summary.csv",
    "w",
    newline=""
)
writer = csv.writer(summary_csv)
writer.writerow([
    "Metric",
    "Value"
])
writer.writerow([
    "Total Population",
    total_population
])
writer.writerow([
    "Students",
    student_count
])
writer.writerow([
    "Employed",
    employed_count
])
writer.writerow([
    "Unemployed",
    unemployed_count
])
writer.writerow([
    "Average Income",
    average_income
])
writer.writerow([
    "Average Health",
    average_health
])
writer.writerow([
    "Average Happiness",
    average_happiness
])
writer.writerow([
    "Highest Income",
    highest_income
])
writer.writerow([
    "Lowest Income",
    lowest_income
])
summary_csv.close()
print(
    "Database Summary CSV Exported"
) 
print("Creating report...")
analytics_csv = open(
    "exports/analytics_summary.csv",
    "w",
    newline=""
)
writer = csv.writer(
    analytics_csv
)
writer.writerow([
    "Category",
    "Group",
    "Count"
])
for group, count in income_distribution.items():
    writer.writerow([
        "Income",
        group,
        count
    ])
for group, count in health_distribution.items():
    writer.writerow([
        "Health",
        group,
        count
    ])
for group, count in happiness_distribution.items():
    writer.writerow([
        "Happiness",
        group,
        count
    ])
analytics_csv.close()
print(
    "Analytics Summary CSV Exported"
)
generate_report(
    total_population,
    student_count,
    employed_count,
    unemployed_count,
    average_income,
    average_health,
    average_happiness,
    age_distribution,
    education_distribution,
    employment_distribution
)
generate_analytics_report(
    age_distribution,
    education_distribution,
    employment_distribution,
    income_distribution,
    health_distribution,
    happiness_distribution
)
print()
print("Report Generated Successfully")    
connection.commit()
connection.close()