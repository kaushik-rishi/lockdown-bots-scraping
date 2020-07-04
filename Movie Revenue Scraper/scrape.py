# ---------------------------------------------------------------------------- #
#                               Import Statements                              #
# ---------------------------------------------------------------------------- #

# for filenames
import datetime

# for making requests and scraping the html
import requests

# for parsing
from bs4 import BeautifulSoup
import lxml

# for directory paths
import os

# for arguments
import sys

# for writing into csv files and saving the data
import pandas as pd
import csv

# For the spinners
# from Spinner.spinner import Spinner
from Spinner.spinner import Spinner
# from Spinner.spinnerEasy import Spinner


# For utlitly
import sys
# sys.stdout = open('output.txt', 'w')

# -------------------------------------------------------------------------- #

# SERVICE_URL = f"https://www.boxofficemojo.com/year/world/{start_year}/"

# base directory of the python program file
BASE_DIR = os.path.dirname(__file__)


# ---------------------------------------------------------------------------- #
#                               Utility Functions                              #
# ---------------------------------------------------------------------------- #

def urlJoin(service, attach):
    """
    Joins the urls
    """

    if service[len(service)-1] == '/':
        service = service[:len(service)-1]
    if attach[0] == '/':
        attach = attach[1:]
    joined = service+'/'+attach
    return joined


def get_HTML(url):
    """
    Utility Function that takes in the URL and returns the response's html directly if the status code is 200
    """

    response = requests.get(url)

    if response.status_code == 200:
        html_response = response.content
        return html_response

    # return None
    return ""


def get_URL(year=2020):

    ret_url = f"https://www.boxofficemojo.com/year/world/{year}/"
    return ret_url


def get_money(dollar):  # currently not used in program => can be used for data analysis
    """
    converts $123,123,123(string) to 123123123(int)
    """

    return int(''.join(dollar[1:].split(',')))


# ---------------------------------------------------------------------------- #
#                               Parsing Function                               #
# ---------------------------------------------------------------------------- #

def parse(SERVICE_URL):

    main_html = get_HTML(SERVICE_URL)  # html of main file
    main_soup = BeautifulSoup(main_html, 'lxml')

    # there is only one table in the whole page
    tables = main_soup.findAll('table')[0]
    table_rows = tables.findAll('tr')
    # print(table_rows[0])

    # this is going to ba a list of lists
    rows_list = []

    for tr in table_rows:

        row = []

        try:
            tds = tr.findAll('td')

            for td in tds:
                # print(td.text, end='     ')
                row.append(td.text)

            # print('\n\n')

        except:
            continue

        rows_list.append(row)

    # removing the headers row
    rows_list = rows_list[1:]
    return rows_list


# ---------------------------------------------------------------------------- #
#              Making DataFrames and CSV Files from the movie data             #
# ---------------------------------------------------------------------------- #

def make_csv(rows_list, headers, file_name):
    df = pd.DataFrame(rows_list, columns=headers)

    df.to_csv(f'data/{file_name}-Box Office Collections.csv', index=False)
    # os.chdir('./data')
    # print(os.getcwd())


# ---------------------------------------------------------------------------- #
#                   Parse and Save as csv(for MULTITHREADING)                  #
# ---------------------------------------------------------------------------- #

def parse_and_save(year):
    print(f'Extracting Data From {year}\'s Box Office Collections ...')
    # with Spinner():
    with Spinner():
        rows_list = parse(get_URL(year))
    print(f'Done Extracting {year}\'s Box Office Collections ...')
    print('\n')

    print(f'Storing {year}\'s Box Office Collections into a CSV file')
    # with Spinner():
    with Spinner():
        make_csv(rows_list, HEADERS, year)
    print(f'Done Storing {year}\'s Box Office Collections into a CSV file')
    print('\n')

    print('-'*60)
    print()


if __name__ == '__main__':

    # for the csv file that we will be creating
    HEADERS = ['Rank', 'Release Group', 'Worldwide',
               'Domestic ($)', 'Domestic %', 'Foriegn ($)', 'Foriegn %']

    print('Data Available from 1977 to 2020')
    print()

    start_year = int(input('Enter the start year you want to parse from : '))
    end_year = int(input('Enter the year until which you want to parse : '))

    if start_year > end_year:
        print('for now im swapping the start year and end year')
        t = start_year
        start_year = end_year
        end_year = t

    if end_year < 1977:
        print('Data Not available At all')
        sys.exit("Invalid Ranges")

    if end_year > 2020:
        print('Sorry Future data is not Available -_-')
        print('Will be scraping only till 2020')
        end_year = 2020

    if start_year < 1977:
        print('Data Available only from 1977')
        print('Will be scraping from 1977')
        start_year = 1977

    """
    # for scraping a single file
    with Spinner():
    rows_list = parse(get_URL(2020))
    make_csv(rows_list, HEADERS)
    """
    for year in range(start_year, min(end_year, 2020)+1):
        parse_and_save(year)

"""
        print(f'Extracting Data From {year}\'s Box Office Collections ...')
        # with Spinner():
        with Spinner():
            rows_list = parse(get_URL(year))
        print(f'Done Extracting {year}\'s Box Office Collections ...')
        print('\n')

        print(f'Storing {year}\'s Box Office Collections into a CSV file')
        # with Spinner():
        with Spinner():
            make_csv(rows_list, HEADERS, year)
        print(f'Done Storing {year}\'s Box Office Collections into a CSV file')
        print('\n')

        print('-'*60)
        print()
"""
