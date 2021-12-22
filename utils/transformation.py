import pandas as pd

def check_if_no_empty_data(dfs):
    """
    Function to check if the formats are valid
    """
    no_empty_data = {}

    # Check if 
    for key in dfs:
        if dfs[key].empty:
            print(f'No data in dataframe {key}')
        else:
            no_empty_data[key] = dfs[key]

    # We can set the primary key here
    for key in no_empty_data:
        no_empty_data[key].index.name='id'
    
    # Handle null values
    for key in no_empty_data:
        if no_empty_data[key].isnull().values.any():
            # We could handle this in multiple ways
            # Here we would replace, but an exception could be raised
            no_empty_data[key].fillna('no-value', inplace=True)
    
    return no_empty_data

