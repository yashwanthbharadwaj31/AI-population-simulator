import matplotlib.pyplot as plt


# =====================================================
# AGE DISTRIBUTION
# =====================================================

def generate_age_distribution_chart(age_distribution):

    labels = list(age_distribution.keys())
    values = list(age_distribution.values())

    plt.figure(figsize=(9,5))

    bars = plt.bar(
        labels,
        values,
        color="royalblue",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 3,
            str(height),
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

    plt.title(
        "Age Distribution of Citizens",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Age Groups", fontsize=12)
    plt.ylabel("Number of Citizens", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/age_distribution.png",
        dpi=300
    )

    plt.close()


# =====================================================
# EDUCATION DISTRIBUTION
# =====================================================

def generate_education_distribution_chart(education_distribution):

    labels = list(education_distribution.keys())
    values = list(education_distribution.values())

    plt.figure(figsize=(9,5))

    bars = plt.bar(
        labels,
        values,
        color="forestgreen",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 3,
            str(height),
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

    plt.title(
        "Education Distribution",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Education Level", fontsize=12)
    plt.ylabel("Number of Citizens", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/education_distribution.png",
        dpi=300
    )

    plt.close()


# =====================================================
# EMPLOYMENT DISTRIBUTION
# =====================================================

def generate_employment_distribution_chart(employment_distribution):

    labels = list(employment_distribution.keys())
    values = list(employment_distribution.values())

    plt.figure(figsize=(9,5))

    bars = plt.bar(
        labels,
        values,
        color="darkorange",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 3,
            str(height),
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

    plt.title(
        "Employment Distribution",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Employment Status", fontsize=12)
    plt.ylabel("Number of Citizens", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/employment_distribution.png",
        dpi=300
    )

    plt.close()
# =====================================================
# INCOME DISTRIBUTION
# =====================================================

def generate_income_distribution_chart(income_distribution):

    labels = list(income_distribution.keys())
    values = list(income_distribution.values())

    plt.figure(figsize=(9,5))

    bars = plt.bar(
        labels,
        values,
        color="mediumpurple",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 3,
            str(height),
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

    plt.title(
        "Income Distribution",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Income Groups", fontsize=12)
    plt.ylabel("Number of Citizens", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/income_distribution.png",
        dpi=300
    )

    plt.close()


# =====================================================
# HEALTH DISTRIBUTION
# =====================================================

def generate_health_distribution_chart(health_distribution):

    labels = list(health_distribution.keys())
    values = list(health_distribution.values())

    plt.figure(figsize=(9,5))

    bars = plt.bar(
        labels,
        values,
        color="crimson",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 3,
            str(height),
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

    plt.title(
        "Health Distribution",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Health Score Range", fontsize=12)
    plt.ylabel("Number of Citizens", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/health_distribution.png",
        dpi=300
    )

    plt.close()


# =====================================================
# HAPPINESS DISTRIBUTION
# =====================================================

def generate_happiness_distribution_chart(happiness_distribution):

    labels = list(happiness_distribution.keys())
    values = list(happiness_distribution.values())

    plt.figure(figsize=(9,5))

    bars = plt.bar(
        labels,
        values,
        color="gold",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 3,
            str(height),
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

    plt.title(
        "Happiness Distribution",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Happiness Score Range", fontsize=12)
    plt.ylabel("Number of Citizens", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/happiness_distribution.png",
        dpi=300
    )

    plt.close()    
# =====================================================
# TOP 10 RICHEST CITIZENS
# =====================================================

def generate_top_richest_chart(sorted_citizens):

    labels = [str(c.citizen_id) for c in sorted_citizens[:10]]
    values = [c.income for c in sorted_citizens[:10]]

    plt.figure(figsize=(10,5))

    bars = plt.bar(
        labels,
        values,
        color="purple",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 1000,
            str(int(height)),
            ha="center",
            fontsize=8,
            rotation=90
        )

    plt.title(
        "Top 10 Richest Citizens",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Citizen ID")
    plt.ylabel("Income")

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/top_10_richest.png",
        dpi=300
    )

    plt.close()


# =====================================================
# TOP 10 HEALTHIEST CITIZENS
# =====================================================

def generate_top_healthiest_chart(sorted_health):

    labels = [str(c.citizen_id) for c in sorted_health[:10]]
    values = [c.health_score for c in sorted_health[:10]]

    plt.figure(figsize=(10,5))

    bars = plt.bar(
        labels,
        values,
        color="forestgreen",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 1,
            str(int(height)),
            ha="center",
            fontsize=9,
            fontweight="bold"
        )

    plt.title(
        "Top 10 Healthiest Citizens",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Citizen ID")
    plt.ylabel("Health Score")

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/top_10_healthiest.png",
        dpi=300
    )

    plt.close()


# =====================================================
# TOP 10 HAPPIEST CITIZENS
# =====================================================

def generate_top_happiest_chart(sorted_happiness):

    labels = [str(c.citizen_id) for c in sorted_happiness[:10]]
    values = [c.happiness_score for c in sorted_happiness[:10]]

    plt.figure(figsize=(10,5))

    bars = plt.bar(
        labels,
        values,
        color="gold",
        edgecolor="black"
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 1,
            str(int(height)),
            ha="center",
            fontsize=9,
            fontweight="bold"
        )

    plt.title(
        "Top 10 Happiest Citizens",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Citizen ID")
    plt.ylabel("Happiness Score")

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    plt.savefig(
        "visualization/charts/top_10_happiest.png",
        dpi=300
    )

    plt.close()    
import matplotlib.image as mpimg


# =====================================================
# ANALYTICS DASHBOARD
# =====================================================

def generate_dashboard():

    charts = [
        ("Age Distribution", "visualization/charts/age_distribution.png"),
        ("Education Distribution", "visualization/charts/education_distribution.png"),
        ("Employment Distribution", "visualization/charts/employment_distribution.png"),
        ("Income Distribution", "visualization/charts/income_distribution.png"),
        ("Health Distribution", "visualization/charts/health_distribution.png"),
        ("Happiness Distribution", "visualization/charts/happiness_distribution.png"),
        ("Top 10 Richest", "visualization/charts/top_10_richest.png"),
        ("Top 10 Healthiest", "visualization/charts/top_10_healthiest.png"),
        ("Top 10 Happiest", "visualization/charts/top_10_happiest.png"),
    ]

    fig, axes = plt.subplots(3, 3, figsize=(22, 16))

    fig.suptitle(
        "AI Population Simulator - Analytics Dashboard",
        fontsize=24,
        fontweight="bold"
    )

    for ax, (title, path) in zip(axes.flat, charts):

        image = mpimg.imread(path)

        ax.imshow(image)

        ax.set_title(
            title,
            fontsize=14,
            fontweight="bold"
        )

        ax.axis("off")

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    plt.savefig(
        "visualization/charts/dashboard.png",
        dpi=300
    )

    plt.close()    