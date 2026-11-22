import pandas as pd
import matplotlib.pyplot as plt

jobs = pd.read_csv("job_postings.csv")

top_jobs = jobs["job_title"].value_counts().head(10)

print(top_jobs)

top_jobs.plot(kind="bar")

plt.title("Top 10 Most Common Job Titles")
plt.xlabel("Job Title")
plt.ylabel("Number of Job Postings")

plt.tight_layout()
plt.show()
skills = pd.read_csv("job_skills.csv")
print(skills.shape)
print(skills.columns)
print(skills.head())
all_skills = skills["job_skills"].dropna().str.split(",").explode()
all_skills = all_skills.str.strip().str.lower()
print(all_skills.value_counts().head(20))
import matplotlib.pyplot as plt
top_skills = all_skills.value_counts().head(10)
top_skills.sort_values().plot(kind= "barh")
plt.title("Top 10 Skills in Job Postings")
plt.xlabel("Number of Job Postings")
plt.ylabel("Skill")
plt.tight_layout()
plt.show()
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

skill_counts = all_skills.value_counts()

for skill in data_science_skills:
    print(skill, ":", skill_counts.get(skill, 0))
    

ds_skills = skill_counts[
    skill_counts.index.isin(data_science_skills)
].sort_values(ascending=True)

ds_skills.plot(kind="barh")

plt.title("Data Science Skills in Job Postings")
plt.xlabel("Number of Job Postings")
plt.ylabel("Skill")

plt.tight_layout()
plt.show()


data_jobs = jobs[
    jobs["job_title"].str.contains(
        "data|analyst|scientist|machine learning|business intelligence",
        case=False,
        na=False
    )
]

print("\nNumber of Data-related jobs:", len(data_jobs))

print("\nTop Data-related job titles:")
print(data_jobs["job_title"].value_counts().head(20))

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

print("\nJob Categories:")
for category, count in category_counts.items():
    print(category, ":", count)
    
category_series = pd.Series(category_counts).sort_values()

category_series.plot(kind="barh")

plt.title("Data Career Categories in Job Postings")
plt.xlabel("Number of Job Postings")
plt.ylabel("Career Category")

plt.tight_layout()
plt.show()


analyst_jobs = jobs[
    jobs["job_title"].str.contains("data analyst", case=False, na=False)
]

analyst_links = analyst_jobs["job_link"]

analyst_skills = skills[
    skills["job_link"].isin(analyst_links)
]

analyst_all_skills = (
    analyst_skills["job_skills"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .str.lower()
)

print("\nTop skills for Data Analyst jobs:")
print(analyst_all_skills.value_counts().head(15))

engineer_jobs = jobs[
    jobs["job_title"].str.contains("data engineer", case=False, na=False)
]

engineer_links = engineer_jobs["job_link"]

engineer_skills = skills[
    skills["job_link"].isin(engineer_links)
]

engineer_all_skills = (
    engineer_skills["job_skills"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .str.lower()
)

print("\nTop skills for Data Engineer jobs:")
print(engineer_all_skills.value_counts().head(15))


scientist_jobs = jobs[
    jobs["job_title"].str.contains("data scientist", case=False, na=False)
]

scientist_links = scientist_jobs["job_link"]

scientist_skills = skills[
    skills["job_link"].isin(scientist_links)
]

scientist_all_skills = (
    scientist_skills["job_skills"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .str.lower()
)

print("\nTop skills for Data Scientist jobs:")
print(scientist_all_skills.value_counts().head(15))


print("\n" + "=" * 50)
print("JOB MARKET ANALYSIS - FINAL SUMMARY")
print("=" * 50)

print("\nDataset:")
print("12,217 job postings")
print("15 job-posting columns")


print("\nTop overall skills:")
print("Python: 4810")
print("SQL: 4619")
print("Data Analysis: 3293")
print("Machine Learning: 2684")
print("Data Visualization: 2330")

print("\nCareer categories:")
for category, count in category_counts.items():
    print(category, ":", count)

print("\nMain conclusions:")
print("1. Python and SQL are highly demanded across data careers.")
print("2. Data Analyst roles strongly emphasize analysis, SQL and visualization.")
print("3. Data Engineer roles emphasize engineering, cloud and big-data technologies.")
print("4. Data Scientist roles emphasize Python, machine learning, statistics and data science.")
