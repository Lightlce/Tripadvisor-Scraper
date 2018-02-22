#'''Trip Advisor Scraper'''

from lxml import html
import requests
import json
import json,re
from dateutil import parser as dateparser
from time import sleep

tripadvisor_url = 'https://ww.tripadvisor.com.sg/'+
page = requests.get('https://www.tripadvisor.com.sg/Hotel_Review-g294265-d302294-Reviews-Pan_Pacific_Singapore-Singapore.html')
tree = html.fromstring(page.content)

#This will create a list of reviews:
buyers = tree.xpath('//div[@class="partial_entry"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
print buyers
