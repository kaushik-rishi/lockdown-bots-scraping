# ---------------------------------------------------------------------------- #
#                               Import Statements                              #
# ---------------------------------------------------------------------------- #

import datetime  # for filenames
import requests  # for making requests and scraping the html
from bs4 import BeautifulSoup  # for parsing
import lxml
import os  # for directory paths and args
import sys
import argparse
import pandas as pd  # for writing into csv files and saving the data
import sys  # For utlitly
from tabulate import tabulate

# For the spinners
from Spinner.spinner import Spinner
# from Spinner.spinnerEasy import Spinner

# Handling JSON files
import json
from JSON_handling.json_utils import *  # load_from_DB and save_to_DB

URL = 'https://www.mohfw.gov.in/'
DB_NAME = 'database.json'
headers = ['active', 'cured', 'deaths', 'totalconf']


def print_menu():
    print('-'*40, 'Covid 19 Reporter', '-'*40, end='\n\n')
    with open('main menu.txt', 'r') as fp:
        for line in fp:
            print(line.strip())
    print('-'*100)


def get_table():
    try:
        resp = requests.get(URL)
        html = resp.content
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('table')
        with open('debug.html', 'w') as fp:
            fp.write(str(table))
        return table
    except:
        return None


def turn_into_dict(table):
    if table is None:
        return None

    tbody = table.find('tbody')

    rows = tbody.findAll('tr')
    rows = rows[:-6]

    information = dict()

    info_each = {
        'active': 0,
        'cured': 0,
        'deaths': 0,
        'totalconf': 0,
    }

    for eachrow in rows:
        alltds = eachrow.findAll('td')
        state = alltds[1].text
        alltds = [td.text for td in alltds][2:]
        for pair in zip(headers, alltds):
            info_each[pair[0]] = int(pair[1])

        information[state] = info_each
    # return info_each
    return information


if __name__ == '__main__':
    # print_menu()

    # choice = input('Enter a choice => ')
    table = get_table()
    cur_info = turn_into_dict(table)

    if os.path.exists() == False:
        with open('database.json', 'w') as fp:
            pass

    past_info = load_frm_DB(DB_NAME)

    for states in cur_info.keys():
        if states not in past_info:
            print('New State Added')
