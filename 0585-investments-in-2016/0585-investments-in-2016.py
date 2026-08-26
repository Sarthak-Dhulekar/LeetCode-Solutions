import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    tiv_2015_count = insurance['tiv_2015'].duplicated(keep = False)
    unique_location = insurance[['lat', 'lon']].duplicated(keep = False)
    condition = (tiv_2015_count == True) & (unique_location == False)
    result = insurance.loc[condition]
    total_sum = round(result['tiv_2016'].sum(), 2)
    return pd.DataFrame({'tiv_2016': [total_sum]})