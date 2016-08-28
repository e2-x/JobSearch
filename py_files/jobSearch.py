import webbrowser
import os

from bs4 import BeautifulSoup
from selenium import webdriver

# job_input = input('Enter the job title: ')
job_input = 'software engineer'
job_input = job_input.replace(" ", "+")

# loc_input = input('Enter the location (City,State): ')
loc_input = 'bridgeport,ct'
loc_input = loc_input.replace(",", "%2C+")

# New url with user inputs
searchUrl = 'http://www.indeed.com/jobs?q=' + job_input + '&l=' + loc_input

# Goto webpage using headless browser
browser = webdriver.PhantomJS()
browser.get(searchUrl)

# let's parse our html
soup = BeautifulSoup(browser.page_source, "html.parser")

# Finds the results list
#find_job_titles = soup.find_all(attrs={'class': 'row result'})

# Find job title/company name/location/ href
#for row in soup.find_all(attrs={"class": "result"}):
find_job_titles = soup.find_all(attrs={'data-tn-element': 'jobTitle'})
company_list = {}
job_title = []
company_name = []
job_url = []
list_jobs = []
i = 0
global_html = """<!DOCTYPE html><html><head></head><body>"""

indeed_html = """<div><p style="padding-left:50px;padding-top:50px">Indeed Results</p><ul>"""

endHtml = """</ul></div></body></html>"""

#Indeed loop
print("Indeed Results")
for row in find_job_titles:

    div_ = row.find_previous('div')
    company_ = div_.select('.company')
    location_ = div_.select('.location')
    job_title = row.attrs['title']
    job_url = row.attrs['href']
    loc = row.location_

    for comp in company_:

        company_name = comp.text.lstrip().replace('\n', '')
        company_list[job_title] = job_title
        company_list[company_name] = company_name
        company_list[job_url] = "http://www.indeed.com" + job_url

        for loc in location_:

            list_jobs = """<li><a href=""" + company_list[job_url] + """ target="_blank">""" + company_list[
                job_title] + """</a>""" + " - " + company_list[company_name] + " - " + loc.text + """</li>"""
            indeed_html += list_jobs
            #print(list_jobs)
    i += 1


#Monster results
#print("Monster Results")

#CB results
#print("Career Builder Results")

#Dice results
#print("Dice Results")

# Create html
path = os.path.abspath('jobSearch.html')

url = 'file://' + path

find_job_span = soup.select('span.company')

with open(path,'w') as f:

    f.write(indeed_html + endHtml)
#f.close()

webbrowser.open(url)