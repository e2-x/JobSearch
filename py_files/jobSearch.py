# Import bs4
from bs4 import BeautifulSoup
import requests

# Get the html form requested page
html = requests.get('http://www.indeed.com/')
#
htmlText = html.text
indeed_soup = BeautifulSoup(htmlText, "html.parser")


# tag.string.replace_with('Hello there')
# print(indeed_soup.title)
indeed_div = indeed_soup.div
indeed_div_contents = indeed_div.contents[5]


indeed_div_contents_list = indeed_div_contents.find_all('div')
# html_div = indeed_soup.find_all('div')
# div_content = html_div.contents
# print(indeed_div)

print(indeed_div_contents_list[6].contents)
#print(type(soup))

# print(soup.prettify()[10000:15000])
# print('-----------------')


