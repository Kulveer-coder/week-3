import seaborn as sns
import pandas as pd


# update/add code below ...
# Load the Bellevue Almshouse dataset.
df_bellevue = pd.read_csv(
    "https://raw.githubusercontent.com/melaniewalsh/"
    "Intro-Cultural-Analytics/master/book/data/"
    "bellevue_almshouse_modified.csv"
)
def fibonacci(n):
    # Stop the recursion when n reaches 0 or 1.
    if n <= 1:
        return n

    # Add the previous two Fibonacci numbers.
    return fibonacci(n - 1) + fibonacci(n - 2)



def to_binary(n):
    # Stop the recursion when n is less than 2.
    if n < 2:
        return n

    # Convert the remaining number and add the last binary digit.
    return to_binary(n // 2) * 10 + n % 2
def task_1():
    # Make a copy so the original data is not changed.
    data = df_bellevue.copy()

    # Treat incorrect gender codes as missing values.
    data.loc[~data["gender"].isin(["m", "w"]), "gender"] = pd.NA
    print("Invalid gender values were treated as missing.")

    # Sort columns from least missing values to most missing values.
    missing_values = data.isna().sum().sort_values(kind="stable")

    return missing_values.index.tolist()


def task_2():
    # Make a copy so the original data is not changed.
    data = df_bellevue.copy()

    # Get the year from the admission date.
    data["year"] = pd.to_datetime(data["date_in"]).dt.year

    # Count the total number of admissions for each year.
    admissions = (
        data.groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )

    return admissions


def task_3():
    # Make a copy so the original data is not changed.
    data = df_bellevue.copy()

    # Treat incorrect gender codes as missing values.
    data.loc[~data["gender"].isin(["m", "w"]), "gender"] = pd.NA
    print("Invalid gender values were excluded from the averages.")

    # Find the average age for each gender.
    average_age = data.groupby("gender")["age"].mean()

    return average_age


def task_4():
    # Explain a messy data issue in the profession column.
    print(
        "Some profession values contain marital-status descriptions "
        "such as married, spinster, and widow."
    )

    # Find the five most common values in the profession column.
    common_professions = (
        df_bellevue["profession"]
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return common_professions


