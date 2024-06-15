import os
import requests
import random
from dotenv import load_dotenv

def list_repos_in_org(org_name: str):
    """
    list all repos in github organization
    :param org_name:
    :return:
    """
    # GitHub endpoint for listing repos under an organization
    repo_url = f"https://api.github.com/orgs/{org_name}/repos"
    # print(f"github api endpoint url {repo_url}")

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url=repo_url, headers=headers)
    response_json = response.json()
    # print(response_json)

    repo_names = []

    for repo in response_json:
        print(repo['name'])
        repo_names.append(repo['name'])

    print(f'Listing Public repos in {org_name} completed')
    return repo_names

def create_new_label(repo_names: list[str], org_name: str):
    """
    create new labels in github
    :return:
    """
    colors = ["#d954a0", "#9067b6", "#c6ff00", "#2f562a", "#0036ff", "#ff8f38", "#ff3845", "#814e51", "#743747",
              "#90395d", "#e3a89e", "#00ff21", "#1f2937", "#111827", "#ff9da4", "#c67b9e", "#f89ac6", "#876baa",
              "#588550", "#ff4500", "#d4c5aa", "#c3d5aa", "#ff1493", "#ffb82e", "#23284e", "#7b8f7e", "#0034c3",
              "#000032", "#00002e", "#00002a", "#000025", "#00001d", "#000013", "#ff99cc", "#80008e", "#ffeef7",
              "#bcd7ff", "#cfe5fd", "#f1e7f7", "#ffeef7", "#bcd7ff", "#bee6ff"]

    color1 = random.choice(colors)
    color2 = random.choice(colors)
    color3 = random.choice(colors)
    color4 = random.choice(colors)
    for repository in repo_names:
        api_endpoint=f'https://api.github.com/repos/{org_name}/{repository}/labels'

        headers =  {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28"
        }

        data1 = {
            "name": "pip dependencies",
            "description": "python package manager",
            "color": color1.replace("#", "")
            }

        data2 = {
                "name": "pip-package",
                "description": "python package manager",
                "color": color2.replace("#", "")
            }

        data3 = {
            "name": "jenkins",
            "description": "jenkins ci cd",
            "color" : color3.replace("#", "")
        }

        data4 = {
            "name": "docker",
            "description": "docker",
            "color": color4.replace("#", "")
        }

        response1 = requests.post(url=api_endpoint,  headers=headers, json=data1)
        status_code1 = response1.status_code
        response2 =  requests.post(url=api_endpoint, headers=headers, json=data2)
        status_code2 = response2.status_code
        response3 = requests.post(url=api_endpoint, headers=headers, json=data3)
        status_code3 = response3.status_code
        response4 = requests.post(url=api_endpoint, headers=headers, json=data4)
        status_code4 = response4.status_code
        response1_json =response1.json()
        # print(response1_json)
        response2_json =response2.json()
        # print(response2_json)
        response3_json =response3.json()
        response4_json =response4.json()


    # data 1
        if status_code1 == 201:
            print(f'New label {data1["name"]} created for repository - {repository}')
        elif status_code1 == 404:
            print(f'Resource not found')
        elif status_code1 == 422:
            print(f"{response1_json['message']}. {response1_json['errors'][0]['resource']} {response1_json['errors'][0]['field']} {data1['name']} {response1_json['errors'][0]['code']} in the repository {repository}")
            # print(f'Validation failed, or the endpoint has been spammed')
        else:
            print('Something is wrong. Please try again')
    # data2
        if status_code2 == 201:
            print(f'New label {data2["name"]} created for repository - {repository}')
        elif status_code2 == 404:
            print(f'Resource not found')
        elif status_code2 == 422:
            print(f"{response2_json['message']}. {response2_json['errors'][0]['resource']} {response2_json['errors'][0]['field']} {data2['name']} {response2_json['errors'][0]['code']} in the repository {repository}")
            # print(f'Validation failed, or the endpoint has been spammed')
        else:
            print('Something is wrong. Please try again')
    # data3
        if status_code3 == 201:
            print(f'New label {data3["name"]} created for repository - {repository}')
        elif status_code3 == 404:
            print(f'Resource not found')
        elif status_code3 == 422:
            print(f"{response3_json['message']}. {response3_json['errors'][0]['resource']} {response3_json['errors'][0]['field']} {data3['name']} {response3_json['errors'][0]['code']} in the repository {repository}")
            # print(f'Validation failed, or the endpoint has been spammed')
        else:
            print('Something is wrong. Please try again')
    # data4

        if status_code4 == 201:
            print(f'New label {data4["name"]} created for repository - {repository}')
        elif status_code4 == 404:
            print(f'Resource not found')
        elif status_code4 == 422:
            print(f"{response4_json['message']}. {response4_json['errors'][0]['resource']} {response4_json['errors'][0]['field']} {data4['name']} {response4_json['errors'][0]['code']} in the repository {repository}")
            # print(f'Validation failed, or the endpoint has been spammed')
        else:
            print('Something is wrong. Please try again')

def main():
    """ To test the script"""
    load_dotenv()
    org_name = os.getenv('ORGANIZATION')
    repo_names = list_repos_in_org(org_name=org_name)
    create_new_label(repo_names=repo_names, org_name=org_name)


if __name__ == "__main__":
    main()
