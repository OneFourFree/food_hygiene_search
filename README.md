# Find Restaurants by Hygiene Rating
This site makes it really simple to find up to date food hygiene ratings for restaurants in your area. Especially useful as apps like JustEat make it difficult to do so.

A recent article from the BBC outlines just how many unhygienic restaurants may be operating on food delivery platforms. https://www.bbc.co.uk/news/uk-45888709

# Installation
1) Download/clone this repository:

		$ git clone
		$ cd food_hygiene_search

2) Create a virtualenv and activate it:

		$ virtualenv env
		$ source env/bin/activate

3) Install the required dependencies

		$ pip install -r requirements.txt

4) Import the MySQLDB
5) Rename .env.example and add your configuration details
6) Run app

		$ python run.py

To see your application, access this url in your browser:

	http://localhost:5000
