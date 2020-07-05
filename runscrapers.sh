# cd ./Movie\ Revenue\ Scraper
# python scrape.py

# cd ./Code\ Forces\ Utility
# python scrape.py

# cd ./COVID19-News
# python scrape.py

if [[ "$1" == '--movie' ]]; then
	#statements
	cd ./Movie\ Revenue\ Scraper
	python scrape.py
	# cd ..
elif [[ "$1" == '--movie-async' ]]; then
	#statements
	cd ./Movie\ Revenue\ Scraper
	python async_scrape.py
	# cd ..
elif [[ "$1" == '--cf' ]]; then
	#statements
	cd ./Code\ Forces\ Utility
	python scrape.py
	# cd ..
elif [[ "$1" == '--covid' ]]; then
	#statements
	cd ./COVID19-News
	python scrape.py
	# cd ..
# elif [[ "$1" == '--covid-news' ]]; then
# 	#statements
# 	cd ./COVID19-News
# 	python news.py
# 	# cd ..
elif [[ "$1" == '--help' ]]; then
	#statements
	cat mainmenu.txt
fi
