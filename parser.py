from bs4 import BeautifulSoup
import requests
import config
import re


class Parser:
    def __init__(self):
        self.URL = config.URL
        self.HEADERS = {
            'accept - Language': 'ru - RU, ru; q = 0.9, en - US; q = 0.8, en; q = 0.7',
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like  Gecko) Chrome / 91.0.4472.124 Safari / 537.36'

        }

    def get_soup(self):
        response = requests.get(self.URL)
        try:
            response.raise_for_status()
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except requests.HTTPError:
            print('Не удалось получить данные')

    def get_json_data(self):
        json_data = []
        soup = self.get_soup()
        posts = soup.find_all('div', class_='post_top')
        print(len(posts))
        for post in posts:
            print("**********************************")
            taglist = post.find('h2', class_='taglist')
            tags_in_post = post.find_all('b')
            tags_mas = []
            for tags in tags_in_post:
                tags_mas.append(f'#{tags.text}'.replace(u'\xa0', u''))
            print(tags_mas)

            post_image_link = post.find('a', class_=['prettyPhotoLink', 'video_gif_source', 'youtube-player'])

            link = ''
            if post_image_link:
                link = post_image_link.attrs['href']
            print(link)
            print("-----------------------------------")


page = Parser().get_json_data()
