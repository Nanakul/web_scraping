import bs4
import requests

# Get the title of a website.
url = 'https://candor.co/guides/salary-negotiation'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'lxml')
web_title = soup.select('title')
print(web_title[0].getText())

# Grabbing a class
web_class = soup.select('.toc')

# for loop to grab all text within the toc class
for item in web_class:
    print(item.text)
