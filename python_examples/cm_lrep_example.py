import sys
import requests

__api_url = "http://localhost:9090/api/v1"


def print_repositories(repositories):
    line = "{0} {1} {2}"
    for repo in repositories:
        print(line.format(repo["repId"]["id"],
                          repo["name"],
                          repo["server"]))


def get_repositories():
    url = __api_url + "/repos"
    req = requests.get(url)
    if req.status_code is 200:
        return req.json()
    print("The repository list could not be retrieved.", file=sys.stderr)
    exit(-1)


def main():
    try:
        print_repositories(get_repositories())
    except requests.RequestException as e:
        print(e)
        exit(-1)


if __name__ == "__main__":
    main()