import bs4
import requests


def new_release():
    """This function will grab the book name and respective price."""
    bn_url = 'https://www.barnesandnoble.com/b/books/_/N-1fZ1sZ29Z8q8?Nrpp=20&page={}'
    bn_req = requests.get(bn_url.format(1))
    bn_soup = bs4.BeautifulSoup(bn_req.text, 'lxml')
    