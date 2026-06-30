import sqlite3
import random
from models.citizen import Citizen
from data.dsa import (
    merge_sort_income,
    merge_sort_health,
    merge_sort_happiness,
    bubble_sort_income,
    selection_sort_income,
    insertion_sort_income
)
from data.analytics import (
    get_age_distribution,
    get_education_distribution,
    get_employment_distribution,
    get_income_distribution,
    get_health_distribution,
    get_happiness_distribution
)
from data.search import (
    binary_search_citizen,
    linear_search_citizen,
    search_by_age,
    search_by_income,
    search_by_education,
    search_by_employment_status,
    filter_by_income_threshold,
    filter_senior_citizens,
    filter_graduates
)
from data.performance import (
    compare_sorting_algorithms,
    compare_search_algorithms
)
from reports.report_generator import (
    generate_report,
    generate_analytics_report
)
from visualization.graphs import (
    generate_age_distribution_chart,
    generate_education_distribution_chart,
    generate_employment_distribution_chart,
    generate_income_distribution_chart,
    generate_health_distribution_chart,
    generate_happiness_distribution_chart,
    generate_top_richest_chart,
    generate_top_healthiest_chart,
    generate_top_happiest_chart,
    generate_dashboard
)
from ui.console_ui import (
    print_banner,
    print_success,
    print_info,
    print_warning,
    print_error,
    print_heading,
    print_search_menu,
    print_statistics,
    print_top_table,
    print_population_report,
    print_database_insights
)
import csv
def display_citizens(results):
    if not results:
        print_error("No citizens found.")
        return
    print_heading("SEARCH RESULTS")
    print("┌──────┬─────┬──────────────────┬────────────┬───────────────┬────────┬───────────┐")
    print("│ ID   │Age  │ Education        │ Income     │ Employment    │ Health │ Happiness │")
    print("├──────┼─────┼──────────────────┼────────────┼───────────────┼────────┼───────────┤")
    for citizen in results:
        print(f"│{citizen.citizen_id:^6}│{citizen.age:^5}│{citizen.education:^18}│₹{citizen.income:^10}│{citizen.employment_status:^15}│{citizen.health_score:^8}│{citizen.happiness_score:^11}│")
    print("└──────┴─────┴──────────────────┴────────────┴───────────────┴────────┴───────────┘")
    print_success(f"Total Citizens Found : {len(results)}")
def generate_population():
    population = []
    citizen_income_data = []
    for citizen_id in range(1, 1001):
        age = random.randint(18, 70)
        if age <= 22:
            employment_status = "Student"
            experience_years = 0
        elif age <= 30:
            employment_status = random.choice(
                ["Employed", "Unemployed"]
            )
            experience_years = random.randint(0, 8)
        else:
            employment_status = random.choice(
                ["Employed", "Unemployed"]
            )
            experience_years = random.randint(
                5,
                age - 22
            )
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
    return population
print_banner()
print_success("Program Started")
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
population = generate_population()
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
    
print_success(f"Population Generated : {len(population)} Citizens")    
cursor.execute("SELECT COUNT(*) FROM population")
total_population = cursor.fetchone()[0]
print_success(f"Database Records : {total_population}")
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
print_heading("POPULATION ANALYTICS")
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
generate_age_distribution_chart(age_distribution)
generate_education_distribution_chart(education_distribution)
generate_employment_distribution_chart(employment_distribution)
generate_income_distribution_chart(income_distribution)
generate_health_distribution_chart(health_distribution)
generate_happiness_distribution_chart(happiness_distribution)
print_statistics(
    "AGE DISTRIBUTION",
    age_distribution
)
print_statistics(
    "EDUCATION DISTRIBUTION",
    education_distribution
)
print_statistics(
    "EMPLOYMENT DISTRIBUTION",
    employment_distribution
)
print_statistics(
    "INCOME DISTRIBUTION",
    income_distribution
)
print_statistics(
    "HEALTH DISTRIBUTION",
    health_distribution
)
print_statistics(
    "HAPPINESS DISTRIBUTION",
    happiness_distribution
)
merge_sorted = merge_sort_income(population)    
print("Sorting Algorithms Comparison")
print("-----------------------------")
print("Bubble Sort     : O(n²)")
print("Selection Sort  : O(n²)")
print("Insertion Sort  : O(n²)")
print("Merge Sort      : O(n log n)")
print()
print("Recommended Algorithm : Merge Sort")
print("Reason : Faster and more efficient for large datasets.")
population_by_id = sorted(
    population,
    key=lambda citizen: citizen.citizen_id
)
sorting_performance = compare_sorting_algorithms(
    population,
    bubble_sort_income,
    selection_sort_income,
    insertion_sort_income,
    merge_sort_income
)
print()
print("Sorting Performance Analysis")
print("----------------------------")
for algorithm, execution_time in sorting_performance.items():
    print(f"{algorithm:<20}: {execution_time:.6f} seconds")
    search_performance = compare_search_algorithms(
    population,
    population_by_id,
    linear_search_citizen,
    binary_search_citizen,
    500
)
print()
print("Search Performance Analysis")
print("---------------------------")
for algorithm, execution_time in search_performance.items():
    print(f"{algorithm:<20}: {execution_time:.6f} seconds")
sorted_citizens = merge_sort_income(population)
print_top_table(
    "TOP 10 RICHEST CITIZENS",
    sorted_citizens,
    "income"
)
sorted_health = merge_sort_health(population)
print_top_table(
    "TOP 10 HEALTHIEST CITIZENS",
    sorted_health,
    "health_score"
)
sorted_happiness = merge_sort_happiness(population)
generate_top_richest_chart(sorted_citizens)
generate_top_healthiest_chart(sorted_health)
generate_top_happiest_chart(sorted_happiness)
generate_dashboard()
print_top_table(
    "TOP 10 HAPPIEST CITIZENS",
    sorted_happiness,
    "happiness_score"
)
print_population_report(
    total_population,
    student_count,
    employed_count,
    unemployed_count,
    average_income,
    average_health,
    average_happiness
)
while True:
    print_search_menu()
    choice = input("\nEnter your choice: ")
    if choice == "1":
        try:
            search_id = int(input("Enter Citizen ID: "))
        except ValueError:
            print_error("Please enter a valid Citizen ID.")
            continue
        found = binary_search_citizen(
            population_by_id,
            search_id
        )
        if found:
            print_heading("CITIZEN DETAILS")
            print("┌───────────────────────────────────────────────┐")
            print(f"│ Citizen ID      : {found.citizen_id:<27}│")
            print(f"│ Age             : {found.age:<27}│")
            print(f"│ Gender          : {found.gender:<27}│")
            print(f"│ Education       : {found.education:<27}│")
            print(f"│ Income          : ₹{found.income:<26}│")
            print(f"│ Employment      : {found.employment_status:<27}│")
            print(f"│ Experience      : {found.experience_years} Years{'':<19}│")
            print(f"│ Health Score    : {found.health_score:<27}│")
            print(f"│ Happiness Score : {found.happiness_score:<27}│")
            print("└───────────────────────────────────────────────┘")
        else:
            print_error("Citizen Not Found.")
    elif choice == "2":
        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print_error("Please enter a valid Age.")
            continue
        results = search_by_age(
            population,
            age
        )
        display_citizens(results)
    elif choice == "3":
        try:
            income = int(input("Enter Income: "))
        except ValueError:
            print_error("Please enter a valid Income.")
            continue
        results = search_by_income(
            population,
            income
        )
        display_citizens(results)
    elif choice == "4":
        education = input(
            "Enter Education (School/Graduate/Post Graduate): "
        )
        results = search_by_education(
            population,
            education
        )
        display_citizens(results)
    elif choice == "5":
        status = input(
            "Enter Employment Status (Student/Employed/Unemployed): "
        )
        results = search_by_employment_status(
            population,
            status
        )
        display_citizens(results)
    elif choice == "6":
        try:
            minimum_income = int(
                input("Enter Minimum Income: ")
            )
        except ValueError:
            print_error("Please enter a valid Minimum Income.")
            continue
        results = filter_by_income_threshold(
            population,
            minimum_income
        )
        display_citizens(results)
    elif choice == "7":
        results = filter_senior_citizens(
            population
        )
        display_citizens(results)
    elif choice == "8":
        results = filter_graduates(
            population
        )
        display_citizens(results)
    elif choice == "9":
        print_info("Exiting Search & Filter Menu...")
        break
    else:
        print_error("Invalid choice. Please try again.") 
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
print_success("CSV Export Successful")    
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
for citizen in sorted_citizens[:10]:
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
for citizen in sorted_health[:10]:
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
for citizen in sorted_happiness[:10]:
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
print_success("Top Citizens CSV Exported")
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
print_success("Top Earners DB Export Complete")    
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
print_success(
    "Top Healthiest DB Export Complete"
)
print()
cursor.execute("""
SELECT MAX(income)
FROM population
""")
highest_income = cursor.fetchone()[0]
cursor.execute("""
SELECT MIN(income)
FROM population
""")
lowest_income = cursor.fetchone()[0]
cursor.execute("""
SELECT employment_status,
       ROUND(AVG(income), 2)
FROM population
GROUP BY employment_status
""")
income_stats = cursor.fetchall()
print_database_insights(
    highest_income,
    lowest_income,
    income_stats
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
print_success("Database Insights Report Generated")   
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
print_success(
    "Database Summary CSV Exported"
) 
print_info("Creating report...")
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
print_success("Analytics Summary CSV Exported")
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
print_success("Reports Generated Successfully")
connection.commit()
connection.close()