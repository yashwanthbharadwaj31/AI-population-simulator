def generate_report(
    count,
    student_count,
    employed_count,
    unemployed_count,
    average_income,
    average_health,
    average_happiness,
    age_distribution,
    education_distribution,
    employment_distribution
):
    report_file = open(
        "reports/population_report.txt",
        "w"
    )
    report_file.write("AI POPULATION REPORT\n")
    report_file.write("====================\n\n")
    report_file.write(
        f"Total Population: {count}\n"
    )
    report_file.write(
        f"Students: {student_count}\n"
    )
    report_file.write(
        f"Employed: {employed_count}\n"
    )
    report_file.write(
        f"Unemployed: {unemployed_count}\n"
    )
    report_file.write(
        f"Average Income: {average_income}\n"
    )
    report_file.write(
        f"Average Health Score: {average_health}\n"
    )
    report_file.write(
        f"Average Happiness Score: {average_happiness}\n"
    )
    report_file.write("\n")
    report_file.write("AGE DISTRIBUTION\n")
    report_file.write("----------------\n")

    for group, value in age_distribution.items():
        report_file.write(
            f"{group}: {value}\n"
        )

    report_file.write("\n")
    report_file.write("EDUCATION DISTRIBUTION\n")
    report_file.write("----------------------\n")

    for education, value in education_distribution.items():
        report_file.write(
            f"{education}: {value}\n"
        )

    report_file.write("\n")
    report_file.write("EMPLOYMENT DISTRIBUTION\n")
    report_file.write("-----------------------\n")

    for status, value in employment_distribution.items():
        report_file.write(
            f"{status}: {value}\n"
        )
                    
    report_file.close()
def generate_analytics_report(
    age_distribution,
    education_distribution,
    employment_distribution,
    income_distribution,
    health_distribution,
    happiness_distribution
):
    analytics_file = open(
        "reports/analytics_report.txt",
        "w"
    )
    analytics_file.write(
        "ANALYTICS REPORT\n"
    )
    analytics_file.write(
        "================\n\n"
    )
    analytics_file.write(
        "AGE DISTRIBUTION\n"
    )
    analytics_file.write(
        "----------------\n"
    )
    for group, value in age_distribution.items():
        analytics_file.write(
            f"{group}: {value}\n"
        )
    analytics_file.write("\n")
    analytics_file.write(
        "EDUCATION DISTRIBUTION\n"
    )
    analytics_file.write(
        "----------------------\n"
    )
    for education, value in education_distribution.items():
        analytics_file.write(
            f"{education}: {value}\n"
        )
    analytics_file.write("\n")
    analytics_file.write(
        "EMPLOYMENT DISTRIBUTION\n"
    )
    analytics_file.write(
        "-----------------------\n"
    )
    for status, value in employment_distribution.items():
        analytics_file.write(
            f"{status}: {value}\n"
        )
    analytics_file.write("\n")
    analytics_file.write(
    "INCOME DISTRIBUTION\n"
)
    analytics_file.write(
    "-------------------\n"
)
    for income, value in income_distribution.items():
        analytics_file.write(
        f"{income}: {value}\n"
    )
    analytics_file.write("\n")
    analytics_file.write(
    "HEALTH DISTRIBUTION\n"
)
    analytics_file.write(
    "-------------------\n"
)
    for health, value in health_distribution.items():
        analytics_file.write(
        f"{health}: {value}\n"
    )    
    analytics_file.write("\n")
    analytics_file.write(
    "HAPPINESS DISTRIBUTION\n"
)
    analytics_file.write(
    "----------------------\n"
)
    for happiness, value in happiness_distribution.items():
        analytics_file.write(
        f"{happiness}: {value}\n"
    )
    analytics_file.write("\n")
    analytics_file.write(
    "SMART INSIGHTS\n"
)
    analytics_file.write(
    "--------------\n"
)
    largest_age_group = max(
    age_distribution,
    key=age_distribution.get
)
    largest_education_group = max(
    education_distribution,
    key=education_distribution.get
)
    largest_employment_group = max(
    employment_distribution,
    key=employment_distribution.get
)
    analytics_file.write(
    f"Most Common Age Group: {largest_age_group}\n"
)
    analytics_file.write(
    f"Most Common Education: {largest_education_group}\n"
)
    analytics_file.write(
    f"Most Common Employment Status: {largest_employment_group}\n"
)
    analytics_file.close()