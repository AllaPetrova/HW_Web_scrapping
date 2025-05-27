

import random
import time

import bs4
import requests
from fake_headers import Headers


KEYWORDS = ['дизайн', 'фото', 'web', 'python']


def generate_headers():

    headers = Headers(os="win", browser="chrome").generate()


response = requests.get("https://habr.com/ru/articles/", headers=generate_headers())
main_page_html = response.text
main_page_soup = bs4.BeautifulSoup(main_page_html, features="lxml")
tm_arcticles_list_tag = main_page_soup.find("div", class_="tm-articles-list")

article_tags = tm_arcticles_list_tag.find_all("article")

articles_parsed = []

for article_tag in article_tags:
    h2_tag = article_tag.find("h2")
    a_tag = h2_tag.find("a")
    time_tag = article_tag.find("time")


    article_link = a_tag["href"]
    article_link = f'https://habr.com/{article_link}'
    article_pub_time = time_tag["datetime"]
    article_header = a_tag.text

    article_page_response = requests.get(article_link, headers=generate_headers())
    article_page_html = article_page_response.text
    article_page_soup = bs4.BeautifulSoup(article_page_html, features='lxml')
    article_body_tag = article_page_soup.find("div", id="post-content-body")
    article_body = article_body_tag.text.strip()

    for keyword in KEYWORDS:
        if keyword in article_body or keyword in article_header:
            print(f"{article_pub_time} – {article_header} – {article_link}")

