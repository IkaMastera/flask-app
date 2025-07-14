import os
import requests

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_pull_requests(state):
    """
    Example of return:
    [
        {"title": "Add useful stuff", "num": 56, "link": "https://github.com/boto/boto3/pull/56"},
        {"title": "Fix something", "num": 57, "link": "https://github.com/boto/boto3/pull/57"},
    ]
    """

    url = "https://api.github.com/repos/boto/boto3/pulls"
    params = {
        "state": state,
        "per_page": 100
    }

    response = requests.get(url, headers=HEADERS, params=params)
    pr_list = []

    if response.status_code == 200:
        for pr in response.json():
            pr_list.append({
                "title": pr.get("title"),
                "num": pr.get("number"),
                "link": pr.get("html_url")
        })

    return pr_list