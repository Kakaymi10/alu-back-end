#!/usr/bin/python3
import sys
import requests  # Import the requests library to make HTTP requests

def number_of_subscribers(subreddit):
    # Construct the API endpoint URL using the subreddit name
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    
    # Set a custom User-Agent in the HTTP headers to avoid any Too Many Requests errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Send a GET request to the API and save the response
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # If the response is OK, extract the subscriber count from the JSON data and return it
        data = response.json()  # Convert the JSON data to a Python dictionary
        return data['data']['subscribers']  # Access the 'subscribers' key in the 'data' dictionary
    else:
        # If the response is not OK, return 0
        return 0

