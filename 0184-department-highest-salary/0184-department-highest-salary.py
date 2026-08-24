import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merge = employee.merge(department, left_on = 'departmentId', right_on = 'id')
    merge['max_salary'] = merge.groupby('departmentId')['salary'].transform('max')
    condition = merge['salary'] == merge['max_salary']
    result =  merge.loc[condition]
    return pd.DataFrame({'department': result['name_y'], 'employee': result['name_x'], 'salary': result['salary']})