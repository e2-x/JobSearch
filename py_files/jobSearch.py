import webbrowser
import os

from bs4 import BeautifulSoup
from selenium import webdriver

# job_input = input('Enter the job title: ')
job_input = 'software engineer'
job_input = job_input.replace(" ", "+")

# loc_input = input('Enter the location (City,State): ')
loc_input = 'bridgeport,ct'
loc_input = loc_input.replace(",","%2C+")

# New url with user inputs
searchUrl = 'http://www.indeed.com/jobs?q=' + job_input + '&l=' + loc_input

# Goto webpage using headless browser
browser = webdriver.PhantomJS()
browser.get(searchUrl)

# let's parse our html
soup = BeautifulSoup(browser.page_source, "html.parser")

# Finds the results list
#find_job_titles = soup.find_all(attrs={'class': 'row result'})

i = 0
# Find job title/company name/location/ href
#for row in soup.find_all(attrs={"class": "result"}):
find_job_titles = soup.find_all(attrs={'data-tn-element': 'jobTitle'})
company_list = {}
job_title = []
company_name = []
for row in find_job_titles:
    div_ = row.find_previous('div')
    company_ = div_.select('.company')
    job_title = row.attrs['title']

    for comp in company_:

        company_name = comp.text.lstrip().replace('\n', '')
        #company_list.insert(i, company_name)

        company_list[job_title] = company_name
        print(job_title, " - ", company_name)

    i = i + 1


# Create html
path = os.path.abspath('jobSearch.html')
message = """<html><head></head><body><p>Indeed Results</p></body></html>"""

url = 'file://' + path

find_job_span = soup.select('span.company')

with open(path,'w') as f:

    f.write(message)
#f.close()

webbrowser.open(url)