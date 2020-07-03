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
from Spinner.spinnerEasy import Spinner


# For utlitly
import sys
sys.stdout = open('output.txt', 'w')

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

    respone = requests.get(url)

    if respone.status_code == 200:
        html_response = respone.content
        return html_response

    # return None
    return ""


def get_URL(year=2020):

    ret_url = f"https://www.boxofficemojo.com/year/world/{year}/"
    return ret_url

# ---------------------------------------------------------------------------- #
#                               Parsing Function                               #
# ---------------------------------------------------------------------------- #


def parse():

    main_html = get_HTML(SERVICE_URL)  # html of main file
    main_soup = BeautifulSoup(main_html, 'lxml')

    # there is only one table in the whole page
    tables = main_soup.findAll('table')[0]
    table_rows = tables.findAll('tr')
    # print(table_rows[0])
    for tr in table_rows:

        try:
            tds = tr.findAll('td')
            for td in tds:
                print(td.text, end='     ')
            print('\n\n')

        except:
            continue


s
if __name__ == '__main__':

    start_year = 2017
    end_year = 2020

    HEADERS = ['Worldwide', 'Domestic', 'Domestic %', 'Foriegn', 'Foriegn %']

    with Spinner():
        parse()
