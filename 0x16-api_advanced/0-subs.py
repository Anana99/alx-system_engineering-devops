#!/usr/bin/python3
'''this module contains the function number_of_subscribers
'''
import requests

def top_ten(subreddit):
    # Construct the API URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Make the API request
    response = requests.get(url, headers={"User-Agent": "Reddit API Client"})

    # Check if the subreddit exists
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(f"- {title}")
    else:
        print("None")
