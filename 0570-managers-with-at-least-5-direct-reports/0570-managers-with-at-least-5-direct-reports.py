import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    count = employee['managerId'].value_counts()
    winning_manager = count[count >= 5].index
    result = employee['id'].isin(winning_manager)
    condition = employee.loc[result]
    return pd.DataFrame({'name': condition['name']})