# ---------------------------------------------------------------------------- #
#                               Import Statements                              #
# ---------------------------------------------------------------------------- #

# for parsing
from bs4 import BeautifulSoup
import lxmlKz

# for making requests and scraping the html
import requests

# for database management
import sqlite3

# for multithreading
import concurrent.futures

# for directory paths
import os

# for arguments
import sys
import datetime

# for writing into csv files and saving the data
import pandas as pd

# For utlitly
import sys

# For the spinners
from Spinner.spinner import Spinner
# from Spinner.spinnerEasy import Spinner


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

    return ""


def get_user(username):

    user_url = f"https://codeforces.com/profile/{username}"
    return user_url


def get_friend(id):
    """
    Returns a div with all the user information => if not found returns None
    """

    url = get_user(id)
    html = get_HTML(url)
    soup = BeautifulSoup(html)
    user_box = soup.find('div', class_='userbox')
    try:


if __name__ == '__main__':

    # create a connection and initialise a cursor
    # this will create a new database is one with that name does not exist

    print('Estabilishing Connection to the database ...')
    with Spinner():
        conn = sqlite3.connect('friends.db')
        # creating a cursor object
        c = conn.cursor()
    print('Connection Estabilished')

    """
        UserBox
            - title-photo
            - info
                - div.badge
                - div.main-info
                    - div.user-rank (->span.xxx -> content(Text ✔))
                    - h1 - a - spans - text
                - ul
                    - li*5
                    - 
    """

    print('Hello World')
