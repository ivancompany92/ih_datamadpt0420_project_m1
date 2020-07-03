import pandas as pd
from sqlalchemy import create_engine


# acquisition functions

def sql_engine(query, path):
    # we introduce the path and the query to get the data from the .db file

    engine = create_engine(f'sqlite:///{path}')
    data = pd.read_sql_query(query, engine)
    return data


def acquire(path):
    print('Starting the data capture in the .db database...')
    query = """
                            SELECT country_info.country_code,
                            career_info.normalized_job_code,
                            personal_info.age
                            FROM poll_info 
                            JOIN personal_info 
                            ON poll_info.uuid = personal_info.uuid 
                            JOIN career_info 
                            ON poll_info.uuid = career_info.uuid 
                            JOIN country_info 
                            ON poll_info.uuid = country_info.uuid
                            """
    df_data_raw = sql_engine(query, path)
    print('Finished capturing data in the .db database.')
    return df_data_raw
