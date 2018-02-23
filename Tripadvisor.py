#'''Trip Advisor Scraper'''

from lxml import html
from lxml import etree
import requests
import json
import json,re
from dateutil import parser as dateparser
from time import sleep

tripadvisor_MAIN_url = 'https://www.tripadvisor.com.sg/'

def tripadvisor_FULL_url(Hotel_ID):
    return tripadvisor_MAIN_url+Hotel_ID


Hotel = tripadvisor_FULL_url('Hotel_Review-g294265-d302294-Reviews-Pan_Pacific_Singapore-Singapore.html')

header = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4'
headers = {'User-agent': header}

#https://udger.com/resources/ua-list/browser-detail?browser=Chrome
page = requests.get(Hotel,headers = headers,verify=False)
tree = html.fromstring(page.content)


#This will create a list of reviews:
buyers = tree.xpath('//div[@class="partial_entry"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

tree = etree.tostring(tree, pretty_print=True, method="html")

print buyers
print tree
