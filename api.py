from github import Github
import urllib3
import requests
import secrets

from secrets import username
from secrets import password


g = Github(username,password)

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)