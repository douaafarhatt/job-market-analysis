# job-market-analysis
# Job Market Analysis

## Project Overview

This project explores the job market for data-related careers using Python and data analysis techniques.

The goal is to identify in-demand job roles, understand the skills employers are looking for, and explore the technical skills associated with different careers in the data field.

## Project Objectives

- Explore job opportunities in the data industry.
- Identify the most frequently appearing data-related job titles.
- Analyze the technical skills required for different positions.
- Compare skill requirements across data-related careers.
- Extract insights that can help students and beginners understand the data job market.

## Dataset Overview

The project uses two datasets:

- **job_postings.csv:** Contains 12,217 job postings with 15 columns.
- **job_skills.csv:** Contains job-related skill information, with 12,217 records and 2 columns.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter / VS Code

## Initial Findings

Some of the most frequently appearing job titles in the dataset include:

| Job Title | Number of Postings |
|---|---:|
| Data Analyst | 1,888 |
| Data Engineer | 1,753 |
| Data Scientist | 809 |
| Machine Learning | 803 |
| Data Architect | 357 |

Some frequently requested skills include:

- **Data Analyst:** Data Analysis, SQL, Data Visualization, Python, Tableau.
- **Data Engineer:** Python, SQL, Spark, Java, AWS.
- **Data Scientist:** Python, Machine Learning, SQL, R.

## Project Structure

```text
job_market_project/
│
├── job_market_project/
│   └── analysis.py
│
├── job_postings.csv
├── job_skills.csv
├── job_summary.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/douaafarhatt/job-market-analysis.git
```

2. Navigate to the project folder:

```bash
cd job-market-analysis
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate it on Windows:

```bash
.venv\Scripts\activate
```

5. Install the required libraries:

```bash
pip install -r requirements.txt
```

6. Make sure the dataset files are available in the project root directory, then run:

```bash
python job_market_project/analysis.py
```

## Project Status

Ongoing — This project is being developed as part of my Data Science learning journey.

## Author

**Douaa Farhat**

Data Science Student | Interested in Data Analysis, Machine Learning, and Artificial Intelligence.

[GitHub Profile](https://github.com/douaafarhatt)