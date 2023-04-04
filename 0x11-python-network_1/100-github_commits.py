#!/usr/bin/python3
"""Displays the top 10 recent commits for a GitHub repository
specified as an argument.
"""
import sys
import requests


if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
    else:
        commits = r.json()
        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author}")
