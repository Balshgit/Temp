from django.urls import path
from server.apps.main.views import search_git_data, git_result

app_name = 'main'

urlpatterns = [
    path('', search_git_data, name='search'),
    path('refresh', git_result, name='result'),
]
