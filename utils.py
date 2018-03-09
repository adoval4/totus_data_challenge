import json
import pandas as pd

# -------------------------
# HERLPER FUNCTIONS

def print_pretty_json(data):
    print json.dumps(data, indent=2, sort_keys=True)

def pop_columns_which_name_contains(dataframe, partial_key):   
    columns_to_pop = [ k for k in dataframe.columns if partial_key in k ]
    # pop out columns form emit
    for col in columns_to_pop:
        _ = dataframe.pop(col)
    return dataframe