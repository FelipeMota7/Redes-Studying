import sys

import requests
from bs4 import BeautifulSoup

TO_CRAWL = []
CRAWLED = set()


def request(url):
    header = {""}
    try:
        response = requests.get(url, headers=header)
        return response.text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass


def get_links(html):
    links = []
    try:
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.find_all("a", href=True)
        for tag in tags_a:
            link = tag["href"]
            if link.startswith("http"):
                links.append(link)

        return links
    except:
        pass


def crawl():
    while 1:
        if TO_CRAWL:
            url = TO_CRAWL.pop()

            html = request(url)
            if html:
                links = get_links(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)

                print("Crawling {}".format(url))

                CRAWLED.add(url)
            else:
                CRAWLED.add(url)
        else:
            print("Done")
            break


if name == "main":
    url = sys.argv[1]
    TO_CRAWL.append(url)
    crawl()
