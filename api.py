from github import Github
import datetime
import urllib3
import requests
import os


owner = os.environ.get("OWNER")
password = os.environ.get("PASSWORD")


g = Github(owner,password)

def get_pull_requests(start_date:str, end_date:str, repo_name:str):
    repo = g.get_repo(f"Umuzi-org/{repo_name}")
    pulls = repo.get_pulls(state='all', sort='created', base='master')
    for pr in pulls:
        if pr.created_at.date() == start_date and pr.closed_at.date() == end_date:
            print("Dates created and closed at the same day")
        else:
            print("Dates created and closed at different days")
            pull_requests = {
                "Date created" : pr.created_at,
                "Date updated" :pr.updated_at,
                "Date Merged" : pr.merged_at,
                "Date Closed" : pr.closed_at,
                "repo" : pr.review_comments,
                }

            print(pull_requests)
    return "Dates created and closed at the same day"
        
if __name__ == "__main__":
    started_date = datetime.datetime(2020, 6, 30, 9, 33, 9)
    closed_date = datetime.datetime(2020, 7, 1, 8, 1, 31)
    print(get_pull_requests(started_date.date(),closed_date.date(),"Magdalene-Selokela-190-rabbitmq"))

