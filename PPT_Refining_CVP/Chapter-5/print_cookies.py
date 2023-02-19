import mechanicalsoup
import http.cookiejar

def print_cookies(url):
    browser = mechanicalsoup.StatefulBrowser()
    cookie_jar = http.cookiejar.CookieJar()
    browser.set_cookiejar(cookie_jar)
    browser.open(url)

    for cookie in cookie_jar:
        print(cookie.__dict__)

if __name__ == '__main__':
    _url = 'http://www.google.com/'
    print_cookies(_url)
