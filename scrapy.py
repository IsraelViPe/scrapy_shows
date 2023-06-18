import requests
from bs4 import BeautifulSoup


def get_html_soup(url):
    page = requests.get(url)
    html_content = page.text
    soup = BeautifulSoup(html_content, "html.parser")

    return soup


def get_next_shows_info(soup):
    next_shows_info = []

    for post in soup.find_all("article"):
        infos = {}

        infos["artist"] = post.select("h1 a")[0].text

        infos["date"] = post.find(
            "div", class_="jet-listing-dynamic-field__content"
        ).text

        infos["link"] = post.select("h1 a")[0]["href"]

        next_shows_info.append(infos)

    return next_shows_info
