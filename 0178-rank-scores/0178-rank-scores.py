import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    ranking = scores['score'].rank(method = 'dense', ascending = False)
    return pd.DataFrame({'score': scores['score'], 'rank': ranking}).sort_values(by = 'score', ascending = False)