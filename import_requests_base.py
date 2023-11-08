import requests

SNYK_TOKEN = "bfb65030-ed70-4515-a7a4-7b83deb286ac"
BASE_URL = "https://api.snyk.io/rest"
ORG_ID = "28a25d20-bb8b-42c9-be21-3815eb36930d" #**change per org
integrationId = "6ae66424-cfdc-4b2a-b18b-a6a408b291fd" #change per org 
branch = "master"


def get_projects_page(next_url):

    # Add "next url" on to the BASE URL
    url = BASE_URL + next_url

    headers = {
        'Accept': 'application/vnd.api+json',
        'Authorization': f'{SNYK_TOKEN}'
    }

    return requests.request("GET", url, headers=headers)

next_url = f"/orgs/{ORG_ID}/targets?version=2023-09-14%7Ebeta&origin=azure-repos"
import_url = f"https://api.snyk.io/v1/org/{ORG_ID}/integrations/{integrationId}/import"

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
    # for each all_projects in array, get the displayName (format is usually repo/name) and split it to pass into the import API
    display_name=(project['attributes']['displayName'])
    splitName = display_name.split('/')
    if len(splitName) >= 2:
        owner = splitName[1] 
        name = splitName[0]
    else:
        print("invalid / format for the repo ")

    request_data= { #body to post 
        'target': {
         'owner': owner,
         'name': name,
         'branch': branch
        }
    }
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'{SNYK_TOKEN}'
    }

    response = requests.post(import_url, headers=headers, json=request_data)

    if response.status_code == 200 or 201:
        print("Request was successful. Importing " + name)
    # Process the API response data if needed
        response_data = response.json()
        print("Response Data:", response_data)
    else:
        print(f"Request failed with status code: {response.status_code}")