import bs4
import requests


def new_release():
    """This function will grab the book name and respective price."""
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)AppleWebKit/537.36 (KHTML, '
                             'like Gecko)Chrome/96.0.4664.110 Safari/537.36',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                         '*/*;q=0.8,application/'}
    bn_url = 'https://www.barnesandnoble.com/b/books/_/N-1fZ1sZ29Z8q8?Nrpp=20&page={}'
    bn_resp = requests.get(bn_url.format(1), headers=HEADERS)
    bn_soup = bs4.BeautifulSoup(bn_resp.text, 'lxml')

    # Grab the title.
    book_title = bn_soup.select('.product-shelf-title product-info-title pt-xs')
    print(len(book_title))


if __name__ == '__main__':
    new_release()
