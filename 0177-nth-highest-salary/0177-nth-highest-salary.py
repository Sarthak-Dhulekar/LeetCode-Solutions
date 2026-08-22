import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    emp_salary = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if N <= 0 or N > len(emp_salary):
        gitNthHighestSalary = None
    else:
        gitNthHighestSalary = emp_salary.iloc[N - 1]

    return pd.DataFrame({f'getNthHighestSalary({N})': [gitNthHighestSalary]})