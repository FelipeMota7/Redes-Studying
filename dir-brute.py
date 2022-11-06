import requests

url = "http://g1.com.br"
with open("wordlist.txt", "r") as file:
    wordlist = file.readlines()

for word in wordlist:

    url_final = "{}/{}".format(url, word)

    response = requests.get(url_final)
    code = response.status_code
    if code != 400:
        print("{} == {}".format(url_final, code))