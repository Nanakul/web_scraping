import bs4
import requests


def first_url():
    """Practicing grabbing the title and class of a website."""
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
    """Practicing Grabbing an image and downloading it to our computer."""
    d4_url = 'https://en.wikipedia.org/wiki/Diablo_IV'
    second_response = requests.get(d4_url)
    second_soup = bs4.BeautifulSoup(second_response.text, 'lxml')
    d4_first_img = second_soup.select('.thumbimage')[0]
    d4_first_src_url = requests.get('https:' + d4_first_img['src'])
    d4_first_contents = d4_first_src_url.content
    
    # Open the image file on computer
    f = open('d4_classes.jpg', 'wb')
    f.write(d4_first_contents)
    f.close()


def third_url():
    """Practicing scraping multiple things off multiple pages."""
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

    # Grab all 2 star books with corresponding titles on the the first page.
    book_req = requests.get(base_url.format(1))
    book_soup = bs4.BeautifulSoup(book_req.text, 'lxml')
    products = book_soup.select('.product_pod')
    # Print statement to see if there are correct number of products per page
    print(len(products))

    two_star_books = []

    # Loop to iterate through all the pages on the website.
    for i in range(1, 51):
        scraped_url = base_url.format(i)
        scraped_req = requests.get(scraped_url)
        scraped_soup = bs4.BeautifulSoup(scraped_req.text, 'lxml')
        books = scraped_soup.select('.product_pod')

        # Loop to iterate through all books on the page.
        for book in books:
            if len(book.select('.star-rating.Two')) != 0:
                book_title = book.select('a')[1]['title']
                two_star_books.append(book_title)
    
    print(len(two_star_books))
    for x in two_star_books:
        print(x)

if __name__ == '__main__':
    # first_url()
    # second_url()
    third_url()