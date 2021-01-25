from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from server.apps.main.tasks import github_result
from server.apps.main.forms import SearchForm
from django.views.decorators.http import require_http_methods
from django.conf import settings
from celery.result import AsyncResult
from server.apps.main.models import Task_ID


@require_http_methods(['GET'])
def index(request: HttpRequest) -> HttpResponse:

    return render(request, 'index.html', {'form': SearchForm, })


@require_http_methods(['GET'])
def git_result(request: HttpRequest) -> HttpResponse:

    message = ''
    task_id = Task_ID.objects.last().task_id
    data = AsyncResult(task_id)
    if data.ready():
        result = data.get()

    return render(request, 'result.html', {'data': result,
                                           'message': message})


def search_git_data(request: HttpRequest) -> HttpResponse:

    message = ''

    if request.method == 'POST':

        name = request.POST.get('git_nickname')
        url = settings.GIT_API_URL + str(name) + '/repos?per_page=1000&page=1'

        message = "results not ready please wait"
        result = github_result.delay(url)
        task_id = result.task_id
        Task_ID.objects.create(task_id=task_id)

    return render(request, 'result.html', {'data': result,
                                           'message': message})
