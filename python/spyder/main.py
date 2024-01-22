"""
This program to fetch domain (based on keyword) urls from the targeted url
"""

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import sys

visited_urls = set()


def spyder_urls(url, key_word):
    try:
        response = requests.get(url)
    except KeyboardInterrupt:
        sys.stderr.write("Program terminated by user\n")
        exit(2)
    except:
        print(f"Request Failed {url}")
        return

    if response.status_code == 200:
        content = BeautifulSoup(response.content, "html.parser")

        # Pick <a> tags
        a_tags = content.find_all("a")
        links = []

        # Loop a_tags
        for a_tag in a_tags:
            link = a_tag.get("href")
            if link is not None or link != "":
                links.append(link)

        # Loop links
        for link in links:
            if link not in visited_urls:
                visited_urls.add(link)
                url_join = urljoin(url, link)
                if key_word in url_join:
                    print("url_join -->", url_join)
                    spyder_urls(url_join, key_word)
            else:
                pass


target_url = input("Enter target URL: ")
target_key_word = input("Enter target KEYWORD: ")
spyder_urls(target_url, target_key_word)
