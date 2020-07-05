# Web-Scraping-Project
**Web scraping project for IIITS - IOTA Hackathon**

# Setup
----
> You could also setup a virtual environment for this
```bash
cd <project directory>
pip install -r requirements.txt
```


## **Web Scraper 1 : Movie Revenue scraper**
----
- Scrapes the https://www.boxofficemojo.com/ website
- Collects the data from **1977 to 2020** on users choice

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
    ./runscrapers --movie-async
  ```
  - To run the multi threading code
  ```bash
    cd <project directory>
    ./runscrapers --movie
  ```

