import requests
from typing import Dict


def git_repos_stars_by_url(url: str) -> Dict:

    res = requests.get(url)
    if res.status_code == 404:
        result = {'Error': 'User has no repositories'}
    else:
        repos = res.json()

        while 'next' in res.links.keys():
            res = requests.get(res.links['next']['url'])
            repos.extend(res.json())

        data = {}
        for item in repos:
            data[item['name']] = int(item['stargazers_count'])

        result = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

    return result
