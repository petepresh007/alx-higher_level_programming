#!/usr/bin/python3
"""
a module to print commits from a github user
"""
import sys
import requests


if __name__ == "__main__":
    resp_name = sys.argv[1]
    owner_name = sys.argv[2]
    params = {'per_page': 10}
    res = requests.get(
            f"https://api.github.com/repos/{owner_name}/{resp_name}/commits",
            params=params
            )

    if res.status_code == 200:
        commits = res.json()
        for commit in commits:
            sha = commit["sha"]
            author = commit["commit"]["author"]["name"]
            print(f"{sha}: {author}")
    else:
        print(None)
