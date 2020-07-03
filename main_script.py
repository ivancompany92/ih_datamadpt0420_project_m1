import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre


def argument_parser():
    countries_list = ['All', 'Belgium', 'Greece', 'Lithuania', 'Portugal', 'Bulgaria', 'Spain',
                      'Luxembourg', 'Romania', 'Czechia', 'France', 'Hungary', 'Slovenia', 'Denmark',
                      'Croatia', 'Malta', 'Slovakia', 'Germany', 'Italy', 'Netherlands', 'Finland',
                      'Estonia', 'Cyprus', 'Austria', 'Sweden', 'Ireland', 'Latvia', 'Poland',
                      'United Kingdom']

    unknown_list = ['Y', 'N']

    parser = argparse.ArgumentParser(description='Set analysis type')
    parser.add_argument("-p", "--path", type=str, dest='path', required=True, help="Indicate the path to the survey "
                                                                                   "data file")
    parser.add_argument("-c", "--country", type=str, choices=countries_list, required=True, dest='country',
                        help="You must indicate a country to obtain your results")
    parser.add_argument("-u", "--unknown", type=str, choices=unknown_list, dest='unknown', default='Y',
                        help="You can indicate whether you want to get results from people whose work is unknown or "
                             "not.")

    args = parser.parse_args()
    return args


def main(path, country, unknown):
    print('Starting Pipeline...')
    df_with_dates_raw = mac.acquire(path)
    df_with_dates_clean = mwr.wrangle(df_with_dates_raw, country, unknown)
    df_analyze = man.analyze(df_with_dates_clean)
    mre.save_df(df_analyze, country, unknown)

    print(f'The results of the country -{country}- are: ')
    print(df_analyze)
    print('Finished Pipeline')


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments.path, arguments.country, arguments.unknown)
