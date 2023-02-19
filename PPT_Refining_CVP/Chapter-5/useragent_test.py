import mechanicalsoup


def test_user_agent(url, user_agent):
    browser = mechanicalsoup.StatefulBrowser(user_agent=user_agent)
    browser.open(url)

    source_code = browser.get_current_page()
    print(source_code)


if __name__ == '__main__':
    _url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
    _user_agent = 'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01'

    test_user_agent(_url, _user_agent)
