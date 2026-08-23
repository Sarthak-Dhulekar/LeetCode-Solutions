import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['next_num'] = logs['num'].shift(-1)
    logs['next_next_num'] = logs['num'].shift(-2)
    condition = (logs['num'] == logs['next_num']) & (logs['num'] == logs['next_next_num'])
    result = logs.loc[condition, 'num'].drop_duplicates()
    return pd.DataFrame({"ConsecutiveNums": result})