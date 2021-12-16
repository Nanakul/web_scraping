import bs4
import requests


def first_url():
    # Get the title of a website.
    url = 'https://candor.co/guides/salary-negotiation'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    web_title = soup.select('title')
    print(web_title[0].getText())

    # Grabbing a class
    web_class = soup.select('.toc')[0]

    # for loop to grab all text within the toc class
    for item in web_class:
        print(item.text)


def second_url():
    # Grabbing an image (using new website than above)
    d4_url = 'https://en.wikipedia.org/wiki/Diablo_IV'
    second_response = requests.get(d4_url)
    second_soup = bs4.BeautifulSoup(second_response.text, 'lxml')
    d4_first_img = second_soup.select('.thumbimage')[0]
    d4_first_src_url = d4_first_img['src']
    print(d4_first_src_url)


if __name__ == '__main__':
    # first_url()
    second_url()