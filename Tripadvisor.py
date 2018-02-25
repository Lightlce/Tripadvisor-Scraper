#'''Trip Advisor Scraper'''

from lxml import html
from lxml import etree
import requests
import csv
#Supress warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#Pan_Pacific_Singapore Tripadvisor URL segments
tripadvisor_MAIN_url = 'https://www.tripadvisor.com.sg/'
tripadvisor_HOTEL_urlA = 'Hotel_Review-g294265-d302294-Reviews-or'
tripadvisor_HOTEL_urlB = '-Pan_Pacific_Singapore-Singapore.html'

#Initialisations
subject_xpath = []
review_xpath = []
name_xpath = []
date_xpath = []
location_xpath = []

#User Agent headers
#Get more headers: https://udger.com/resources/ua-list/browser-detail?browser=Chrome
header = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4'
headers = {'User-agent': header}

def Hotel_url(PageNum):
    return tripadvisor_MAIN_url+tripadvisor_HOTEL_urlA+PageNum+tripadvisor_HOTEL_urlB

def scrapeTo(PageNum):
    for i in range(0,(PageNum)*5,5):
        Hotel = Hotel_url(str(i))

        #HTML page
        page = requests.get(Hotel,headers = headers,verify=False)
        tree = html.fromstring(page.content)

        #This will create a list of reviews:
        global subject_xpath
        subject_xpath += tree.xpath('//span[@class="noQuotes"]/text()')
        global review_xpath
        review_xpath += tree.xpath('//p[@class="partial_entry"]/text()')
        global name_xpath
        name_xpath += tree.xpath('//div[@class="info_text"]/div/text()')
        global date_xpath
        date_xpath += tree.xpath('//span[@class="ratingDate"]/text()')
        global location_xpath
        location_xpath += tree.xpath('//div[@class="userLoc"]/strong/text()')

if __name__ == '__main__':
    scrapeTo(2)

    with open("Reviews Test.csv","wb+") as csvfile:
        reviewtable = csv.writer(csvfile,delimiter=",",quotechar='"')
        reviewtable.writerow(['Subject','name','review','time','location'])
        i = 0
        for row in subject_xpath:
            reviewtable.writerow([row,name_xpath[i],review_xpath[i],date_xpath[i],location_xpath[i]])
            i += 1

    print 'Scraping Test Completed! File saved as \'Reviews Test.csv\''
