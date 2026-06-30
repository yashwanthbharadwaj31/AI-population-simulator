from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    print(Fore.CYAN + "=" * 70)
    print(Fore.CYAN + "             AI POPULATION SIMULATOR")
    print(Fore.CYAN + "=" * 70)
    print()

def print_success(message):
    print(Fore.GREEN + "[SUCCESS] " + Style.RESET_ALL + message)

def print_info(message):
    print(Fore.CYAN + "[INFO] " + Style.RESET_ALL + message)

def print_warning(message):
    print(Fore.YELLOW + "[WARNING] " + Style.RESET_ALL + message)

def print_error(message):
    print(Fore.RED + "[ERROR] " + Style.RESET_ALL + message)

def print_heading(title):
    print()
    print(Fore.MAGENTA + "=" * 70)
    print(Fore.MAGENTA + title.center(70))
    print(Fore.MAGENTA + "=" * 70)
def print_search_menu():
    print()
    print(Fore.BLUE + "╔════════════════════════════════════════════════════╗")
    print(Fore.BLUE + "║               SEARCH & FILTER MENU                 ║")
    print(Fore.BLUE + "╠════════════════════════════════════════════════════╣")
    print(Fore.BLUE + "║ 1. Search by Citizen ID                            ║")
    print(Fore.BLUE + "║ 2. Search by Age                                   ║")
    print(Fore.BLUE + "║ 3. Search by Income                                ║")
    print(Fore.BLUE + "║ 4. Search by Education                             ║")
    print(Fore.BLUE + "║ 5. Search by Employment Status                     ║")
    print(Fore.BLUE + "║ 6. Filter by Minimum Income                        ║")
    print(Fore.BLUE + "║ 7. Filter Senior Citizens                          ║")
    print(Fore.BLUE + "║ 8. Filter Graduates                                ║")
    print(Fore.BLUE + "║ 9. Exit                                            ║")
    print(Fore.BLUE + "╚════════════════════════════════════════════════════╝")
def print_statistics(title, data):
    print_heading(title)
    print("┌──────────────────────────────────────────────────┐")
    for key, value in data.items():
        print(f"│ {key:<30} : {str(value):>10} │")
    print("└──────────────────────────────────────────────────┘")       
def print_top_table(title, citizens, field):
    print_heading(title)
    print("┌──────┬─────┬────────────────┬──────────────┐")
    print("│ ID   │ Age │ Employment     │ Value        │")
    print("├──────┼─────┼────────────────┼──────────────┤")

    for citizen in citizens[:10]:
        value = getattr(citizen, field)
        if field == "income":
            value = f"₹{value}"
        print(
            f"│{citizen.citizen_id:^6}"
            f"│{citizen.age:^5}"
            f"│{citizen.employment_status:^16}"
            f"│{str(value):^14}│"
        )

    print("└──────┴─────┴────────────────┴──────────────┘")
def print_population_report(
    total_population,
    students,
    employed,
    unemployed,
    average_income,
    average_health,
    average_happiness
):
    print_heading("POPULATION REPORT")
    print("┌──────────────────────────────────────────────────────┐")
    print(f"│ Total Population   : {total_population:<18}│")
    print(f"│ Students          : {students:<18}│")
    print(f"│ Employed          : {employed:<18}│")
    print(f"│ Unemployed        : {unemployed:<18}│")
    print(f"│ Average Income    : ₹{average_income:<17}│")
    print(f"│ Average Health    : {average_health:<18}│")
    print(f"│ Average Happiness : {average_happiness:<18}│")
    print("└──────────────────────────────────────────────────────┘")
def print_database_insights(highest_income, lowest_income, income_stats):
    print_heading("DATABASE INSIGHTS")
    print("┌──────────────────────────────────────────────────┐")
    print(f"│ Highest Income : ₹{highest_income:<24}│")
    print(f"│ Lowest Income  : ₹{lowest_income:<24}│")
    print("├──────────────────────────────────────────────────┤")
    print("│ Income By Employment Status                     │")
    print("├──────────────────────────────────────────────────┤")
    for status, income in income_stats:
        print(f"│ {status:<18}: ₹{income:<18}│")
    print("└──────────────────────────────────────────────────┘")    
