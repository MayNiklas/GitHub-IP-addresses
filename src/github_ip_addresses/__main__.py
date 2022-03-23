import os
import json
import requests


def get(json_data,list):
    result = []
    for i in json_data[list]:
        result.append(i)
    return(result)

def writer(json_data, lists):

    if not os.path.exists('lists/'):
        os.mkdir('lists/')

    for l in lists:
        result = get(json_data,l)
        f = open("lists/" + l + ".txt", "a")
        for i in result:
            f.write(i + "\n")
            print(i)
        f.close()

def main():
    api_url = "https://api.github.com/meta"
    lists = ["hooks", "web", "api", "git", "packages", "pages", "importer", "actions", "dependabot"]

    response = requests.get(api_url)
    json_data = json.loads(response.text)
    
    writer(json_data, lists)


if __name__ == '__main__':
    main()
