#'''Trip Advisor Scraper'''

from lxml import html
from lxml import etree
import requests

tripadvisor_MAIN_url = 'https://www.tripadvisor.com.sg/'

def tripadvisor_FULL_url(Hotel_ID):
    return tripadvisor_MAIN_url+Hotel_ID

#for i in range(1,1339*5,stop)
Hotel = tripadvisor_FULL_url('Hotel_Review-g294265-d302294-Reviews-or1-Pan_Pacific_Singapore-Singapore.html')

#User Agent headers
#Get more headers: https://udger.com/resources/ua-list/browser-detail?browser=Chrome
header = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4'
headers = {'User-agent': header}

#HTML page
page = requests.get(Hotel,headers = headers,verify=False)
tree = html.fromstring(page.content)

#This will create a list of reviews:
subject_xpath = tree.xpath('//span[@class="noQuotes"]/text()')
review_xpath = tree.xpath('//p[@class="partial_entry"]/text()')
name_xpath = tree.xpath('//div[@class="info_text"]/div/text()')
date_xpath = tree.xpath('//span[@class="ratingDate"]/text()')
location_xpath = tree.xpath('//div[@class="userLoc"]/strong/text()')

print subject_xpath[0]
print review_xpath[0]
print name_xpath[0]
print date_xpath[0]
print location_xpath[0]
#for row in subject.findAll('span'):
#    print row.prettify()
#print tree
