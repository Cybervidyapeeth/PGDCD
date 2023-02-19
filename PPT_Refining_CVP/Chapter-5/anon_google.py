import json
import argparse
import urllib.parse
import requests


class GoogleResult:
    def __init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def __repr__(self):
        return self.title


def google(search_term, api_key, cx):
    search_term = urllib.parse.quote_plus(search_term)
    url = f'https://www.googleapis.com/customsearch/v1?q={search_term}&key={api_key}&cx={cx}'
    response = requests.get(url)
    objects = response.json()
    results = []

    for result in objects['items']:
        url = result['link']
        title = result['title']
        text = result['snippet']
        new_gr = GoogleResult(title, text, url)
        results.append(new_gr)

    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 anon_google.py KEYWORDS API_KEY CX')
    parser.add_argument('kwords', type=str, metavar='KEYWORDS',
                        help='specify the keyword(s) for a Google search')
    parser.add_argument('api_key', type=str, metavar='API_KEY',
                        help='specify your API key for the Google Search API')
    parser.add_argument('cx', type=str, metavar='CX',
                        help='specify the cx value for your Custom Search Engine')
    args = parser.parse_args()
    keywords = args.kwords
    api_key = args.api_key
    cx = args.cx

    print(google(keywords, api_key, cx))


'''

This code uses the requests module to make API requests, and takes three command line 
arguments: KEYWORDS, API_KEY, and CX. Make sure to replace API_KEY with your Google Search API key and 
CX with your Custom Search Engine ID.

'''