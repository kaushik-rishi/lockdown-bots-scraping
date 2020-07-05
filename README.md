# Web-Scraping-Project
**Web scraping project for IIITS - IOTA Hackathon**

# Setup
----
> You could also setup a virtual environment for this
```bash
cd <project directory>
pip install -r requirements.txt
```

### The utlity tool is executed using bash script
```bash
cd <project directory>
./runscrapers.sh --help
```
to display possible options

## **Web Scraper 1 : Movie Revenue scraper 🎥**
----
- Scrapes the https://www.boxofficemojo.com/ website
- Collects the data from **1977 to 2020** on users choice
- Main Reason of choosing this website is it has no API Support so this scraping tool can be extended to give all (nearly 😁) the functionalities of API

#### Working :
    - Extracts the data using bs4 and requests
    - saves it into a pandas data frame
    - then saves it into a CSV file
    - all the files are stored in the data/ folder inside the movie scraping folder 
    - First i implemented it using normal asynchronous code
    - But Launching multiple downloads all at once was a I/O Bound task So i could use multi threading in it
    - When i used multi threading Speeds increased 10 times(not exaggerating)
    - you can see yourself
  - to run the normal download code
  ```bash
    cd <project directory>
    ./runscrapers.sh --movie-async
  ```
  - To run the multi threading code
  ```bash
    cd <project directory>
    ./runscrapers.sh --movie
  ```


## **Web Scraper 2 : Code Forces Stalker and Scraper 💻**
----
- Scrapes the https://codeforces.com/ website
- can download the c++ submissions of other users onto the local machine and profile photos of others
- has a database of users where the ratings, contribution, friends, id and other data is stored
- you can update the database to see who's rating has changed or who's online now
- view all the data as a table
- add a friend to the database , remove a friend from the database

#### Working :
    - Extracts the data using bs4 and requests
    - As the data is extremely less instead of using **SQLITE3** (😉that would make the program slower)i have used JSON file as a database
    - Adding and removing the friends was done using load and dump methods of JSON
    - all the files are stored in the Submissions/ folder and Profile Photos/ folder inside the codeforces utility folder
    - There was neither a CPU bound nor a I/O bound task so did not use multithreading or multiprocessing
    - you can see by executing yourself
    - Used the tabulate python module to create tables
  - To run the script
  ```bash
    cd <project directory>
    ./runscrapers.sh --cf
  ```

## **Web Scraper 3 : COVID-19 NEWS Assist 🦠**
----
- Scrapes the https://www.mohfw.gov.in/ website
- has a database of all the states with details like active, cured cases, deaths, total confirmed
- update the database and show all the changes since the last update
- prints a table of all the cases and states
- can get the particular states details

#### Working :
    - Extracts the data using bs4 and requests
    - As the data is extremely less instead of using SQLITE3 (😉that would make the program slower)i have used JSON file as a database
    - Adding and removing the friends was done using load and dump methods of JSON
    - There was neither a CPU bound nor a I/O bound task so did not use multithreading or multiprocessing
    - Used the tabulate python module to create tables
    - you can see by executing yourself
    - To run the script
  ```bash
    cd <project directory>
    ./runscrapers.sh --covid
  ```

### Further things that can be done
- ## Box Office Collections Project
  
      - We could have compared the world movie revenue all over years using matplotlib
      - See the increase in Harry potter movie revenues and plot them and try predicting new revenues

- ## Codeforces Scraping project
      - We could have plotted all the friends ratings on a bar graph 
      - 🎊(important) : We could have used slack webhook integration to get notifications when any of our friends goes online or does a submission (😉 Competition Dude)
- ## COVID-19 Project
      - Used seaborn and plotted a Heat Map 🗺 all over the India with covidcases/population ration
      - Used winnotify python library to get a notification for your Home states corona virus updates on your windows 10 machine (😒 embarassed windows user)

- ## Periodic Checking
      - I have tried to setup the python program of covid 19 to run every 5 minutes on my windows machine but i was'nt successful due to time constrains
      - Having made an excuse for that we could have setup crontab on linux/mac systems so that the 2nd and 3rd projects run every X minutes

---
---
### Conclusion :
- Web Scraping alone has very little uses
- But when data analysis is done on it or
- When you integrate a notification system for it
- It becomes extremely powerful 😎
- Another advantage of web scraping is to collect data from websites with no API Support
