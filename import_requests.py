import requests

SNYK_TOKEN = "bfb65030-ed70-4515-a7a4-7b83deb286ac"
ORG_ID = "0ebb9084-0c7b-4362-9a45-880e038d6284"
BASE_URL = "https://api.snyk.io/rest"


def get_projects_page(next_url):

    # Add "next url" on to the BASE URL
    url = BASE_URL + next_url

    headers = {
        'Accept': 'application/vnd.api+json',
        'Authorization': f'token {SNYK_TOKEN}'
    }

    return requests.request("GET", url, headers=headers)


next_url = f"/orgs/{ORG_ID}/targets?version=2023-09-14%7Ebeta"

all_projects = []

while next_url is not None:
    res = get_projects_page(next_url).json()

    if 'next' in res['links']:
        next_url = res['links']['next']
    else:
        next_url = None

    # add to list
    all_projects.extend(res['data'])

    
for project in all_projects:
    # import here
    print(project['id'])