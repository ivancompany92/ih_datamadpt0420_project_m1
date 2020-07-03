import pandas as pd


# reporting the csv results

def save_df(df_data, country, unknown):
    # we save the results in the folder data/results

    df_data.to_csv(f'./data/results/data_project_m1_{country}_{unknown}.csv', index=False, sep=',')
    print(f'DF save in the folder: data/results  with the name: data_project_m1_{country}_{unknown}.csv')
