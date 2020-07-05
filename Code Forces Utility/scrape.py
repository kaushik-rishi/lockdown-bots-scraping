# ---------------------------------------------------------------------------- #
#                               Import Statements                              #
# ---------------------------------------------------------------------------- #

# for parsing
from pprint import pprint
from bs4 import BeautifulSoup
import lxml

# for making requests and scraping the html
import requests

# for database management
import sqlite3

# for directory paths
import os

# for arguments
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


# ---------------------------------------------------------------------------- #
#                 Fuctions that are extracting the data of user                #
# ---------------------------------------------------------------------------- #


def get_info_img(id):
    """
    Returns a list of 2 elements
        - div containing user information
        - div containing user photo
    """

    url = get_user(id)
    html = get_HTML(url)
    soup = BeautifulSoup(html, 'lxml')

    try:
        userbox = soup.find('div', class_='userbox')
        title_photo = userbox.find('div', class_='title-photo')
        info = userbox.find('div', class_='info')

    except:
        # happens when the handle is invalid

        title_photo = None
        info = None

    return [info, title_photo]


def get_information_dict(info):
    """
    Parses the division of information returned by get_info_img and turns it into a dictionary
    and returns the dictionary
    {
        'rating':---,
        'contribution':---,
        'friends':---,
        'lastseen': ---,
        'registered': ---
    }
    """

    # grabbing the list of details
    ul = info.find('ul')

    # splitting them into list items
    lis = ul.findAll('li')

    # extrcating the text from the list items
    lis_text = []

    for li in lis:
        lis_text.append(li.text.strip())

    lis_text = lis_text[:-2]  # removing the blog and contribution

    # dicitonary to be filled
    information = {
        'rating': 0,
        'contribution': 0,
        'friends': 0,
        'lastseen': '',
        'registered': ''
    }

    # formatting and filling the dicitonary
    for li in lis_text:

        temp = li.split(':')

        temp[0] = temp[0].strip()  # key
        temp[1] = temp[1].strip()  # value

        if temp[0] == 'Contest rating':
            temp[0] = 'rating'
            temp[1] = int(temp[1][:4])

        if temp[0] == 'Contribution':
            temp[0] = 'contribution'
            temp[1] = int(temp[1])

        if temp[0] == 'Friend of':
            temp[0] = 'friends'
            temp[1] = int(temp[1].split(' ')[0])

        if temp[0] == 'Last visit':
            temp[0] = 'lastseen'

        if temp[0] == 'Registered':
            temp[0] = 'registered'

        information[temp[0]] = temp[1]

    return information  # returns a dictionary of information


def get_img_bytes(title_photo):
    """
    Takes the title-photo division and exrats the image
    and returns the binary data (BLOB) that can be either stored or 
    written into a jpeg file (open in wb mode)
    """

    img_url = 'https:'+title_photo.find('img')["src"]
    img_resp = requests.get(img_url)
    profile_pic = img_resp.content

    return profile_pic


# Page Structure
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
"""

# Data Extraction Example
"""    
    with open('pp.jpg', 'wb') as fp:
    fp.write(img_bytes)
    pprint(information)

"""


def get_from_db(id):
    print(c)


def download_sub(subid, contestid):
    url = f"https://codeforces.com/contest/{contestid}/submission/{subid}"


if __name__ == '__main__':

    # printing the menu
    with open('menu.txt', 'r') as fp:
        print(fp.read())

    choice = input(' => ')

    conn = sqlite3.Connection('friends.db')
    c = conn.cursor()

    id = input()

    print('Trying to fetch Users Profile from host : codeforces.com ...')

    with Spinner():
        [info, title_photo] = get_info_img(id)
    if info is None or title_photo is None:
        print('Invalid Handle')
        # continue

    img_bytes = get_img_bytes(title_photo)
    information = get_information_dict(info)
