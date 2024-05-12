import pandas as pd 
import numpy as np 

def filter_attributes(df):
    attributes = ['Det', 'Dec', 'Com', 'Cnt', 'Tea', 'Nat']

    filtered_df = df

    for i in attributes:
        filtered_df = filtered_df[filtered_df[i] > 12]


    return filtered_df

def find_player(position, upper_value, low_value, df):
    attributes = ['Det', 'Dec', 'Com', 'Cnt', 'Tea', 'Nat']
    result_df = filter_attributes(df)
    result_df = df[(df['Value'] <= upper_value) & (df['Value'] >= low_value)]

    if position != " ":
        result_df = result_df[result_df['Position'].str.contains(position)]

    result_df = result_df.sort_values(attributes, ascending=False)
    result_df = result_df.iloc[:10]
    return result_df

