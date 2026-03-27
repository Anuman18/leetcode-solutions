import requests
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("LEETCODE_USERNAME")

url = "https://leetcode.com/graphql"

query = {
    "query": """
    query recentAcSubmissions($username: String!) {
        recentAcSubmissionList(username: $username) {
            title
            titleSlug
            timestamp
        }
    }
    """,
    "variables": {
        "username": username
    }
}

res = requests.post(url, json=query)
data = res.json()

submissions = data["data"]["recentAcSubmissionList"]

for sub in submissions:
    print(sub["title"], sub["titleSlug"])