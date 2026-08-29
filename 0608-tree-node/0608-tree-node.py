import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    parante_node = tree['p_id'].dropna().unique()
    def condition(row):
        if pd.isna(row['p_id']):
            return 'Root'
        elif row['id'] in parante_node:
            return 'Inner'
        else:
            return 'Leaf'

    tree['type'] = tree.apply(condition, axis = 1)
    return tree[['id', 'type']]