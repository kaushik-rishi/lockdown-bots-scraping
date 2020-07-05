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
HEADERS = ['active', 'cured', 'deaths', 'totalconf']
TABLE_HEADERS = ['state/union territory',
                 'active', 'cured', 'deaths', 'totalconf']


def print_menu():
    print('-'*40, 'Covid 19 Reporter', '-'*40, end='\n\n')
    with open('menu.txt', 'r') as fp:
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

    for eachrow in rows:
        info_each = {
            'active': 0,
            'cured': 0,
            'deaths': 0,
            'totalconf': 0,
        }
        alltds = eachrow.findAll('td')
        state = alltds[1].text
        alltds = [td.text for td in alltds][2:]
        for pair in zip(HEADERS, alltds):
            info_each[pair[0]] = int(pair[1])

        information[state] = info_each
    # return info_each
    from pprint import pprint
    pprint(information)
    return information


def update():
    table = get_table()
    cur_info = turn_into_dict(table)

    past_info = load_frm_DB(DB_NAME)

    for state in cur_info.keys():

        alter = []
        if state not in past_info:
            print('New State Added')
            print(tabulate(
                # [list(k, v) for k, v in cur_info[state].iteritems()],
                list(map(list, cur_info[state].items())),
                headers=HEADERS
            ))
            print('\n\n\n')
        else:
            prev_st = past_info[state]
            curr_st = cur_info[state]

            for key in prev_st:
                # (header, previous, current) => value
                if prev_st[key] != curr_st[key]:
                    alter.append((key, prev_st[key], curr_st[key]))

            for tup in alter:
                print(tup[0], end=' : ')
                print(tup[1], end=' => ')
                print(tup[2])
    save_to_DB(cur_info, DB_NAME)


def show_table():
    update()
    info = load_frm_DB(DB_NAME)
    to_tabulate = []  # list of state, all props

    l = []
    for each_state in info.keys():
        l.append(each_state)
        for prop in info[each_state]:
            l.append(info[each_state][prop])

        to_tabulate.append(l)

    # print(tabulate(l, headers=TABLE_HEADERS))


def status_state(state):

    information = load_frm_DB(DB_NAME)

    notfound = True

    for states in information:
        if states == state:
            s_info = information[state]
            notfound = False
            # print(tabulate(
            #     # [list(k, v) for k, v in s_info.iter],
            #     headers=TABLE_HEADERS
            # ))

    if notfound:
        print('No such State Found')


# 🌈
if __name__ == '__main__':

    if os.path.exists('database.json') == False:
        with open('database.json', 'w') as fp:
            fp.write('{}')
            pass

    """print_menu()
    choice = ''
    while(True):
        choice = input('Enter Choice => ')

        if choice == 'q':
            exit()
        elif choice == 'u':
            update()
        elif choice == 't':
            show_table()
        elif len(choice) >= 2 and choice[0] == 's':
            choice = choice.split(' ')
            print(choice)
            state = choice[1]
            status_state(state)
        else:
            print('Wrong Option Please Try Again')"""
    update()
