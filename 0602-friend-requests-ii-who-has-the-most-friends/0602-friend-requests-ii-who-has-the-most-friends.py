import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    all_ids = pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']])
    max_count = all_ids.value_counts()
    count_df = max_count.reset_index()
    count_df.columns = ['id', 'num']
    return count_df.head(1)