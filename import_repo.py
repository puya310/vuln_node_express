import requests
import time

SNYK_TOKEN = "" #your snyk API token (account settings on snyk UI)
ORG_ID = "0ebb9084-0c7b-4362-9a45-880e038d6284" #Org ID (this will need to be done/run for each org)
integrationId = "eaaa6bcc-6dcb-4154-af50-bd8a8b4615a0" #SCM integrationID (get from integration page)
branch = "master" #set the default branch to monitor (main/master, which is what Snyk monitors by default)

#takes displayName attribute from target_url endpoint and feeds it into the import_url api
#considerations: branch 
target_url = f"https://api.snyk.io/rest/orgs/{ORG_ID}/targets?version=2023-09-14%7Ebeta&origin=azure-repos"
import_url = f"https://api.snyk.io/v1/org/{ORG_ID}/integrations/{integrationId}/import"

all_targets = []

headers = {
    'Accept': 'application/vnd.api+json',
    'Authorization': f'{SNYK_TOKEN}'
    }
res = requests.request("GET", target_url, headers=headers).json()
all_targets.extend(res['data'])

    
for project in all_targets:
    # for each all_targets, get the displayName (format is usually repo/name) and split it to pass into the import API
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
    time.sleep(3)

    if response.status_code == 200 or 201:
        print("Request was successful. Importing " + name)
        print(display_name)
    # Process the API response data if needed
        response_data = response.json()
        print("Response Data:", response_data)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(dis)