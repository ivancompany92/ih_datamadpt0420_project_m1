import pandas as pd


# reporting the csv results

def save_df(df_data):
    df_data.to_csv('./data/results/data_project_m1.csv', index=False, sep=',')
    print('DF save in the folder: data/results')
