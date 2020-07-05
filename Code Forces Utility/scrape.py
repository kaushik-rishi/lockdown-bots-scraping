# ---------------------------------------------------------------------------- #
#                               Import Statements                              #
# ---------------------------------------------------------------------------- #

# for parsing
from pprint import pprint
from bs4 import BeautifulSoup
import lxml

import requests  # for making requests and scraping the html
import os  # for directory paths
from tabulate import tabulate  # for making tables

# for html unescaping >= Python 3.5:
from html import unescape

# for handling json
from JSON_handling.json_utils import *

# For the spinners
# from Spinner.spinner import Spinner
from Spinner.spinnerEasy import Spinner


BASE_DIR = os.getcwd()
DB_NAME = 'database.json'
TABLE_HEADERS = ['Username', 'Rating', 'Friends', 'Last Seen', 'Registered']


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
            temp[1] = int(''.join(temp[1][:4].split(',')))

        if temp[0] == 'Contribution':
            temp[0] = 'contribution'
            temp[1] = int(temp[1])

        if temp[0] == 'Friend of':
            temp[0] = 'friends'
            temp[1] = int(''.join((temp[1].split(' ')[0]).split(',')))

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


def download_sub(subid, contestid):
    """
        download the submission based on contest id and submission id
    """
    url = f"https://codeforces.com/contest/{contestid}/submission/{subid}"

    try:
        os.makedirs('Downloaded Submissions')
    except:
        pass

    os.chdir('Downloaded Submissions')

    try:
        soup = BeautifulSoup(get_HTML(url), 'lxml')
        code = soup.find('pre', {"id": "program-source-text"}).text
        code = unescape(code)
        filename = f'{contestid} - {subid}.cpp'
        with open(filename, 'w') as fp:
            fp.write(code)
    except Exception as e:
        print('Please enter correct contest id and submission id')

    os.chdir(BASE_DIR)

# ---------------------------------------------------------------------------- #
#                             Altering the database                            #
# ---------------------------------------------------------------------------- #


def update():
    """
        updates the database with new ratings contribution changes and display them
    """
    data = load_frm_DB(DB_NAME)

    for frnd in data:
        old_frnd = data[frnd]
        cur_frnd = get_information_dict(get_info_img(frnd)[0])
        if old_frnd == cur_frnd:
            continue

        data[frnd] = cur_frnd
        for key in old_frnd:
            if old_frnd[key] != cur_frnd[key]:
                print(key, end=' : ')
                print(old_frnd[key], end=' -> ')
                print(cur_frnd[key])

    save_to_DB(data, DB_NAME)


def addFrnd(id):
    """
        adds a friend to the database
    """

    data = load_frm_DB(DB_NAME)

    if id in data.keys():
        print(f'{id} was aldready been added')
        return
    try:
        each_dict = get_information_dict(get_info_img(id)[0])
        data[id] = each_dict
    except:
        print('No such User exists')
        return
    save_to_DB(data, DB_NAME)
    print(f'{id} added')


def removeFrnd(id):
    """
        removes a friend from the database
    """

    data = load_frm_DB(DB_NAME)
    if id not in data.keys():
        print(f'{id} no longer exists in the database')
        return
    del data[id]
    save_to_DB(data, DB_NAME)


def show_table():
    """
        prints the data in tabulated forms
    """

    info = load_frm_DB(DB_NAME)
    to_tabulate = []  # list of id, all props

    for each_frnd in info.keys():

        l = []
        l.append(each_frnd)

        for prop in info[each_frnd]:
            l.append(info[each_frnd][prop])

        to_tabulate.append(l)

    print(tabulate(to_tabulate, headers=TABLE_HEADERS, tablefmt='psql'))


# 🌈
if __name__ == '__main__':

    if os.path.exists(DB_NAME) == False or len(open('database.json', 'r').read().strip()) == 0:
        with open(DB_NAME, 'w') as fp:
            fp.write('{}')  # empty database

    # printing the menu
    with open('menu.txt', 'r') as fp:
        print(fp.read())

    while True:
        choice = input(' => ')

        if choice == 'q':
            exit()

        elif choice == 'u':
            update()

        elif choice == 'gall':
            show_table()

        elif len(choice) > 2 and choice[0] == 'g':
            id = choice.split(' ')[1]

            print('Trying to fetch Users Profile from host : codeforces.com ...')

            profile_found = False

            with Spinner():
                [info, title_photo] = get_info_img(id)
                if info is None or title_photo is None:
                    print('Invalid Handle')
                    # continue
                else:
                    profile_found = True
                    img_bytes = get_img_bytes(title_photo)
                    information = get_information_dict(info)
                    print(tabulate(
                        [[k,information[k]] for k in information ],
                        headers = ['Username', f'{id}']
                    ))

            if profile_found:
                pp = input('Want to Download his profile photo (Y/N) ?')
                if pp == 'Y':
                    try:
                        os.makedirs('Profile Photos')
                    except:
                        pass

                    os.chdir('Profile Photos')
                    with open(f'{id}.jpg', 'wb') as fp:
                        fp.write(img_bytes)

                    os.chdir(BASE_DIR)

        elif choice == 'a':
            id = input('ID of the friend you want to add : ')
            addFrnd(id)

        elif choice == 'r':
            id = input('ID of the friend you want to remove : ')
            removeFrnd(id)

        elif choice == 'd':
            cid = input('contest id : ')
            sid = input('submission id : ')
            download_sub(sid, cid)

        else:
            print('Wrong Choice Dude')
