from .data import catdata
import requests as r
import random

base_url = "https://api.thecatapi.com/v1/images/search"



class cat:
    def __init__(self):
        self.d = catdata()
        self.base_url = base_url


    def get(self, tags=None):
        if tags is None:
            url = self.base_url

        else:
            url = self.d.specify(tags)

        if url is None:
            url = base_url
            print('no such cat')
        else:
            pass

        page = r.get(url)
        page_dict = page.json()[0]
        image = page_dict.get('url')

        return image
