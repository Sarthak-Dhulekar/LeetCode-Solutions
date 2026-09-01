import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat['id'] = np.where(seat['id'] % 2 == 0, 
                          seat['id'] - 1,
                          np.where(seat['id'] == len(seat), seat['id'], seat['id'] + 1))
    seat = seat.sort_values(by = 'id')
    return seat