import os
import argparse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from anon_browser import AnonBrowser

def mirror_images(tgt_url, dest_dir):
    ab = AnonBrowser()
    ab.anonymize()
    try:
        ab.open(tgt_url)
    except Exception as e:
        print(f'[!] Error opening target URL.\n'
              f'{"":>3}[-] {str(e)}')
        return

    html = str(ab.get_current_page())
    soup = BeautifulSoup(html, 'html.parser')
    image_tags = soup.find_all('img')

    if not os.path.isdir(dest_dir):
        print(f'[!] Destination directory does not exist: {dest_dir}')
        return

    for image in image_tags:
        src_url = image['src']
        src_parsed = urlparse(src_url)
        filename = os.path.basename(src_parsed.path)
        filename = os.path.join(dest_dir, filename.replace('/', '_'))
        if not filename:
            continue

        try:
            data = ab.open(src_url).read()
        except Exception as e:
            print(f'[!] Error retrieving image from URL.\n'
                  f'{"":>3}[-] URL: {src_url}\n'
                  f'{"":>3}[-] {str(e)}')
            continue

        try:
            with open(filename, 'wb') as save:
                print(f'[+] Saving {str(filename)}')
                save.write(data)
        except Exception as e:
            print(f'[!] Error saving image to disk.\n'
                  f'{"":>3}[-] Filename: {filename}\n'
                  f'{"":>3}[-] {str(e)}')
            continue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 image_mirror.py TARGET_URL DESTINATION_DIR')
    parser.add_argument('tgt_url', type=str, metavar='TARGET_URL',
                        help='specify the target url')
    parser.add_argument('-d', type=str, metavar='DESTINATION_DIR',
                        required=True, help='specify the destination directory')
    args = parser

# To run the code, open your terminal and navigate to the directory where 
# the "image_mirror.py" file is stored. Then run the following command:

# python3 image_mirror.py [TARGET_URL] -d [DESTINATION_DIR]
