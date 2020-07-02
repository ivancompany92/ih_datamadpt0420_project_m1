import requests
from bs4 import BeautifulSoup
import re


# wrangling functions

def get_countries():
    print('Starting to get countries in the web site...')
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('td')

    list_countries_raw = []
    for country_raw in table:
        list_countries_raw.append(country_raw.text)

    print('Finished the list of countries in the web site...')
    return list_countries_raw


def clean_countries_web(list_countries_raw):
    print('Starting cleaning the countries list...')
    countries = []
    for country in list_countries_raw:
        first_change = re.sub('\n', '', country)
        second_change = re.sub('^ ', '', first_change)
        try:
            if second_change[0] == '(':
                second_change = second_change[1:3]
        except:
            continue
        countries.append(second_change)

    countries_library = {}
    for i in range(1, 57, 2):
        countries_library[f'{countries[i]}'] = countries[i - 1]

    print('Finished cleaning the countries library...')
    return countries_library


def clean_countries(df_data, countries):
    print('Starting cleaning the countries on the df...')

    count = 0
    for country in df_data['country_code']:
        if country == 'GB':
            df_data.loc[count, 'country_code'] = 'UK'
        elif country == 'GR':
            df_data.loc[count, 'country_code'] = 'EL'
        count += 1

    count_2 = 0
    for country in df_data['country_code']:
        df_data.loc[count_2, 'country_code'] = countries[country]
        count_2 += 1

    df_data.rename({'country_code': 'Country'}, axis=1, inplace=True)
    print('Finished cleaning countries on the df...')
    return df_data


def choice_country(df_complete, country):
    if country == 'All':
        return df_complete
    else:
        df_country = df_complete[df_complete['Country'] == f'{country}'].reset_index()
        df_country.drop(['index'], axis=1, inplace=True)
        return df_country


def clean_years(df_data):
    print('Starting cleaning the years on the df...')
    df_data['age'] = df_data['age'].str.replace(r'[a-zA-Z]', '')

    df_data['age'] = df_data['age'].astype(int)

    count = 0
    for i in df_data['age']:
        if i > 1000:
            df_data.loc[count, 'age'] = 2016 - i
        count += 1
    df_data.rename({'age': 'Age'}, axis=1, inplace=True)
    print('Finished cleaning years on the df...')
    return df_data


def title_jobs_API(data):
    print('Starting to get job titles in the API ...')
    jobs_id = data['normalized_job_code'].unique()

    json_api_id = []
    for i in jobs_id:
        response = requests.get(f'http://api.dataatwork.org/v1/jobs/{i}')
        json_api = response.json()
        json_api_id.append(json_api)
    print('Finished the list of job titles in the API ...')
    return json_api_id


def clean_jobs(df_data, titles_jobs):
    print('Starting cleaning the jobs on the df...')
    count = 0
    for code in df_data['normalized_job_code']:
        for job in titles_jobs:
            if (job.get('uuid') == code) and (code is not None):
                df_data.loc[count, 'normalized_job_code'] = job.get('title')
        count += 1

    df_data.rename({'normalized_job_code': 'Job Title'}, axis=1, inplace=True)
    print('Finished cleaning jobs on the df...')
    return df_data


def none_jobs_change(df_data):
    print('Starting cleaning the NONE jobs on the df...')
    count = 0
    for code in df_data['Job Title']:
        if code is None:
            df_data.loc[count, 'Job Title'] = 'Jobless'
        count += 1

    print('Finished cleaning NONE jobs on the df...')
    return df_data


def none_jobs_eliminate(df_data):
    df_data.dropna(inplace=True)
    df_data.reset_index(inplace=True)
    df_data.drop('index', axis=1, inplace=True)
    return df_data


def wrangle(dat, country, jobless):
    countries_web_raw = get_countries()
    library_countries_clean = clean_countries_web(countries_web_raw)
    dat_clean_countries = clean_countries(dat, library_countries_clean)
    filter_country = choice_country(dat_clean_countries, country)
    dat_clean_years = clean_years(filter_country)
    get_titles_jobs = title_jobs_API(dat_clean_years)
    dat_clean_jobs = clean_jobs(dat_clean_years, get_titles_jobs)
    if jobless == 'Y':
        dat_clean_none_jobs = none_jobs_change(dat_clean_jobs)
        return dat_clean_none_jobs
    else:
        dat_delete_none_jobs = none_jobs_eliminate(dat_clean_jobs)
        return dat_delete_none_jobs
