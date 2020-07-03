import pandas as pd


# analysis functions
def group_age(df_data):
    # we obtain the age group to which each participant of the survey belongs

    print('We introduce the age group of each participant on the df.')
    count = 0
    for i in df_data['Age']:
        if i < 26:
            df_data.loc[count, 'Age group'] = '14_25'
        elif i > 39:
            df_data.loc[count, 'Age group'] = '40_65'
        else:
            df_data.loc[count, 'Age group'] = '26_39'
        count += 1

    return df_data


def quantity_per_job(df_data):
    # We grouped the participants by age range and job title for each country.
    # We obtain the quantity of each group and introduce it on the DF.

    print('Starting to group by title job and age group,and getting the amount...')
    df_with_quantity = df_data.groupby(['Country', 'Job Title', 'Age group']).count()
    df_with_quantity.columns = ['Quantity']
    df_with_quantity.reset_index(inplace=True)
    print('Finished the grouping by job and age group, and the amount of each grouping.')
    return df_with_quantity


def percentage_per_job(df_data):
    # We obtain the percentage of each group of participants (by age group and job title)
    # compared to the total for the country.
    # If the user put all the countries ('All'), the percentage is over the total of all countries.

    print('Starting to get the percentage that represents the quantity over the global...')
    df_with_only_percentage = (df_data[['Quantity']] / df_data[['Quantity']].sum()) * 100
    df_with_only_percentage = df_with_only_percentage.round(2)
    df_with_only_percentage.columns = ['Percentage']
    print('Finished obtaining the percentage that represents the quantity over the global.')
    return df_with_only_percentage


def merge_df(df_1, df_2):
    # We join two DF into one

    df_merge = pd.merge(df_1, df_2, left_index=True, right_index=True)
    return df_merge


def analyze(df):
    dat_classify_group_age = group_age(df)
    dat_grouped_job_age_quantity = quantity_per_job(dat_classify_group_age)
    df_with_percentage_quantity = percentage_per_job(dat_grouped_job_age_quantity)
    dat_merge_quantity_percentage = merge_df(dat_grouped_job_age_quantity, df_with_percentage_quantity)
    return dat_merge_quantity_percentage
