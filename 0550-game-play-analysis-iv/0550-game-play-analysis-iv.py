import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['1st_login'] = activity.groupby('player_id')['event_date'].transform('min')
    activity['next_date'] = activity['1st_login'] + pd.to_timedelta(1, unit = 'D')
    count_adjesent = activity.loc[activity['event_date'] == activity['next_date']]
    numerator = count_adjesent['player_id'].nunique()
    denominator = activity['player_id'].nunique()
    final_fraction = round(numerator / denominator, 2)
    return pd.DataFrame({'fraction': [final_fraction]})