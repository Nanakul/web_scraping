import bs4
import requests

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

# Grabbing an image (using new website than above)
second_url = 'https://en.wikipedia.org/wiki/Diablo_IV'
second_response = requests.get(second_url)
second_soup = bs4.BeautifulSoup(second_response.text, 'lxml')
second_web_first_image = second_soup.select('.thumbinner')[0]
print(second_web_first_image)