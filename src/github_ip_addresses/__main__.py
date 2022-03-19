import os
import json
import requests


def writer(json_data, lists):
    for l in lists:
        f = open("lists/" + l + ".txt", "a")

        for i in json_data[l]:
            f.write(i + "\n")
        f.close()


def main():
    api_url = "https://api.github.com/meta"
    lists = ["hooks", "web", "api", "git", "packages", "pages", "importer", "actions", "dependabot"]

    if not os.path.exists('lists/'):
        os.mkdir('lists/')

    response = requests.get(api_url)
    json_data = json.loads(response.text)
    writer(json_data, lists)


if __name__ == '__main__':
    main()
