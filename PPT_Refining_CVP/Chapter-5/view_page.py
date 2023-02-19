import mechanicalsoup


def view_page(url):
  
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)

    source_code = browser.get_current_page()
    print(source_code)


if __name__ == '__main__':
    view_page('https://google.com/')

