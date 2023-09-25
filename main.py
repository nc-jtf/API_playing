# This is a sample Python script.
import json


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_top_worldnew():
    import requests
    from flask import Flask, jsonify

    # Define the URL and query parameters for the Reddit API request
    url = "https://www.reddit.com/r/worldnews/top.json"
    params = {
        "t": "day",  # Top posts of the day
        "limit": 10  # Number of posts to fetch
    }

    # Set the User-Agent header to identify the script
    headers = {"User-Agent": "MyScript/0.1"}

    # Send the API request and parse the JSON response
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)

    # Print the titles of the top posts
    for post in data["data"]["children"]:
        print(post["data"]["title"])
    return jsonify(data["data"]["children"])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("nothing")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
