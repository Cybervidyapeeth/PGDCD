
import mechanicalsoup


def test_proxy(url, proxy):
    browser = mechanicalsoup.StatefulBrowser()
    browser.session.proxies = proxy
    browser.open(url)

    source_code = browser.get_current_page()
    print(source_code)


if __name__ == '__main__':
    
    _url = 'https://google.com/'
    hide_me_proxy = {'http': '105.29.64.217:80'}

    test_proxy(_url, hide_me_proxy)
