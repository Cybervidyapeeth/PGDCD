import json
import urllib.request
from urllib.parse import quote_plus
from anon_browser import AnonBrowser


class ReconPerson:
    def __init__(self, first_name, last_name, job='', social_media=None):
        if social_media is None:
            social_media = {}
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media

    def __repr__(self):
        return f'{self.first_name} {self.last_name} has job {self.job}'

    def get_social(self, media_name):
        return self.social_media.get(media_name)

    @staticmethod
    def query_twitter(query):
        query = quote_plus(query)
        results = []
        browser = AnonBrowser()
        response = browser.open(f'http://search.twitter.com/search.json?q={query}')
        json_objects = json.load(response)

        for result in json_objects['results']:
            new_result = {
                'from_user': result['from_user_name'],
                'geo': result.get('geo', None),
                'tweet': result['text']
            }
            results.append(new_result)

        return results


if __name__ == '__main__':
    ap = ReconPerson('Boondock', 'Saint')
    print(ap.query_twitter('from:th3j35t3r since:2010-01-01 include:retweets'))
