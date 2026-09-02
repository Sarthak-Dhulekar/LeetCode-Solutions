import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    count_products = product['product_key'].nunique()
    count_grouping_customer = customer.groupby('customer_id', as_index = False)['product_key'].nunique()
    result = count_grouping_customer[count_grouping_customer['product_key'] == count_products]
    return result[['customer_id']]