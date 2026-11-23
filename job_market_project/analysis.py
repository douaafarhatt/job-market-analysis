
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. PROJECT PATHS
# --------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "visualizations"

OUTPUT_DIR.mkdir(exist_ok=True)

jobs = pd.read_csv(PROJECT_DIR / "job_postings.csv")
skills = pd.read_csv(PROJECT_DIR / "job_skills.csv")

# --------------------------------
# 2. HELPER FUNCTIONS
# --------------------------------

def save_chart(filename):
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

def extract_skills(data):
    return (
        data["job_skills"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
        .str.lower()
    )

# --------------------------------
# 3. TOP 10 JOB TITLES
# --------------------------------

top_jobs = jobs["job_title"].value_counts().head(10)

print("\nTop 10 Job Titles:")
print(top_jobs)

top_jobs.sort_values().plot(kind="barh", figsize=(10, 6))

plt.title("Top 10 Most Common Job Titles")
plt.xlabel("Number of Job Postings")
plt.ylabel("Job Title")

save_chart("top_job_titles.png")

# --------------------------------
# 4. TOP 10 OVERALL SKILLS
# --------------------------------

all_skills = extract_skills(skills)
skill_counts = all_skills.value_counts()

top_skills = skill_counts.head(10)

print("\nTop 10 Skills:")
print(top_skills)

top_skills.sort_values().plot(kind="barh", figsize=(10, 6))

plt.title("Top 10 Most Requested Skills")
plt.xlabel("Number of Skill Mentions")
plt.ylabel("Skill")

save_chart("top_skills.png")

# --------------------------------
# 5. DATA SCIENCE SKILLS
# --------------------------------

data_science_skills = [
    "python",
    "sql",
    "data analysis",
    "machine learning",
    "data visualization",
    "r",
    "data science",
    "statistics",
    "tableau",
    "power bi",
    "deep learning"
]

ds_skills = (
    skill_counts[skill_counts.index.isin(data_science_skills)]
    .sort_values()
)

print("\nData Science Skills:")
print(ds_skills)

ds_skills.plot(kind="barh", figsize=(10, 6))

plt.title("Demand for Data Science Skills")
plt.xlabel("Number of Skill Mentions")
plt.ylabel("Skill")

save_chart("data_science_skills.png")

# --------------------------------
# 6. DATA CAREER CATEGORIES
# --------------------------------

job_categories = {
    "Data Engineer": "data engineer",
    "Data Analyst": "data analyst",
    "Data Scientist": "data scientist",
    "Machine Learning": "machine learning",
    "Data Architect": "data architect"
}

category_counts = {}

for category, keyword in job_categories.items():
    category_counts[category] = jobs["job_title"].str.contains(
        keyword,
        case=False,
        na=False
    ).sum()

category_series = pd.Series(category_counts).sort_values()

print("\nCareer Categories:")
print(category_series)

category_series.plot(kind="barh", figsize=(10, 6))

plt.title("Data Career Categories")
plt.xlabel("Number of Job Postings")
plt.ylabel("Career Category")

save_chart("career_categories.png")

# --------------------------------
# 7. SKILLS BY CAREER
# --------------------------------

career_keywords = {
    "data_analyst": "data analyst",
    "data_engineer": "data engineer",
    "data_scientist": "data scientist"
}

for career, keyword in career_keywords.items():

    career_jobs = jobs[
        jobs["job_title"].str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

    career_links = career_jobs["job_link"]

    career_skills = skills[
        skills["job_link"].isin(career_links)
    ]

    extracted = extract_skills(career_skills)
    top_career_skills = extracted.value_counts().head(10)

    print(f"\nTop Skills for {career.replace('_', ' ').title()}:")
    print(top_career_skills)

    if not top_career_skills.empty:

        top_career_skills.sort_values().plot(
            kind="barh",
            figsize=(10, 6)
        )

        plt.title(
            f"Top 10 Skills for {career.replace('_', ' ').title()} Jobs"
        )
        plt.xlabel("Number of Skill Mentions")
        plt.ylabel("Skill")

        save_chart(f"{career}_skills.png")

# --------------------------------
# 8. FINAL SUMMARY
# --------------------------------

print("\n" + "=" * 50)
print("JOB MARKET ANALYSIS - FINAL SUMMARY")
print("=" * 50)

print("\nNumber of job postings:", len(jobs))

print("\nTop 5 overall skills:")
print(skill_counts.head(5))

print("\nCareer categories:")
print(category_series)

print("\nMain observations:")
print("1. Python and SQL are important skills in data-related jobs.")
print("2. Data Analyst roles emphasize analysis and visualization.")
print("3. Data Engineer roles emphasize engineering technologies.")
print("4. Data Scientist roles emphasize machine learning and statistics.")

print("\nCharts saved successfully in:", OUTPUT_DIR)