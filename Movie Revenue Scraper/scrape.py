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

# for writing into csv files and saving the data
import pandas as pd
import csv

# For the spinners
# from Spinner.spinner import Spinner
from Spinner.spinner import Spinner
from Spinner.spinnerEasy import SpinnerEasy


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


def get_money(dollar):
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

def make_csv(rows_list, headers):
    df = pd.DataFrame(rows_list, columns=headers)
    df.to_csv('movies.csv', index=False)
    # os.chdir('./data')
    # print(os.getcwd())


if __name__ == '__main__':

    # start_year = 2017
    # end_year = 2020

    HEADERS = ['Rank', 'Release Group', 'Worldwide',
               'Domestic ($)', 'Domestic %', 'Foriegn ($)', 'Foriegn %']

    start_year = int(input('Enter the start year you want to parse from : '))
    end_year = int(input('Enter the year until which you want to parse : '))

    # with Spinner():
    # rows_list = parse(get_URL(2020))
    # make_csv(rows_list, HEADERS)
    for year in range(start_year, end_year+1):

        if year > 2020:
            print(f'Year Index Out of Range ')
            print(f'Still i have parse till {year-1}')
            break

        print(f'Extracting Data From {year}\'s Box Office Collections ...')
        with SpinnerEasy():
            rows_list = parse(get_URL(year))
        print(f'Done Extracting {year}\'s Box Office Collections ...')
        print('\n')

        print(f'Storing {year}\'s Box Office Collections into a CSV file')
        with SpinnerEasy():
            rows_list = parse(get_URL(year))
        print(f'Done Storing {year}\'s Box Office Collections into a CSV file')
