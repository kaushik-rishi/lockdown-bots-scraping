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

# -------------------------------------------------------------------------- #
import sys
sys.stdout = open('output.txt', 'w')

SERVICE_URL = "https://www.boxofficemojo.com/year/world"
BASE_DIR = os.path.dirname(__file__)


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


def return_HTML(url):
    """ 
    Utility Function that takes in the URL and returns the response's html directly if the status code is 200
    """

    respone = requests.get(url)

    if respone.status_code == 200:
        html_response = respone.content
        return html_response

    # return None
    return ""


# if __name__ == '__main__':

# with spinner.Spinner():
# with Spinner():
#     main_html = return_HTML(SERVICE_URL)
#     main_soup = BeautifulSoup(main_html, 'lxml')

#     # there is only one table in the whole page
#     tables = main_soup.findAll('table')[0]
#     table_rows = tables.findAll('tr')
#     # print(table_rows[0])
#     for tr in table_rows:
#         """
#         try:
#             tds = tr.findAll('td')
#             for td in tds:
#                 print(td.text, end='     ')
#             print('\n\n')
#         except:
#             continue
#         """
#         tds = tr.findAll('td')
#         for td in tds:
#             print(td.text, end='     ')
#         print('\n\n')
    # uncomment if you want to save this as a html file
    """
    with open('box_table.html', 'w') as fp:
        fp.write(str(table[0]))
    """


main_html = return_HTML(SERVICE_URL)
main_soup = BeautifulSoup(main_html, 'lxml')

# there is only one table in the whole page
tables = main_soup.findAll('table')[0]
table_rows = tables.findAll('tr')
# print(table_rows[0])
for tr in table_rows:
    """
    try:
        tds = tr.findAll('td')
        for td in tds:
            print(td.text, end='     ')
        print('\n\n')
    except:
        continue
    """
    tds = tr.findAll('td')
    for td in tds:
        print(td.text, end='     ')
    print('\n\n')

"""

scroll_table = main_soup.select('.imdb-scroll-table')[0]

"""
