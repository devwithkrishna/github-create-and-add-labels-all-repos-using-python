import os
import requests
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
    print(response_json)

def main():
    """ To test the script"""
    load_dotenv()
    org_name = os.getenv('ORGANIZATION')
    list_repos_in_org(org_name=org_name)

if __name__ == "__main__":
    main()
