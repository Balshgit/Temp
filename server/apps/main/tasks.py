from server.celery_app import app
from typing import Dict
from server.apps.main.utils.commands import git_repos_stars_by_url
from django.shortcuts import render
from django.http import HttpResponse


@app.task
def github_result(url: str) -> Dict:

    result = git_repos_stars_by_url(url)

    return result
