#Trip Advisor Reviews Scraper
#Written by Lightlce Copyright 2018

from lxml import html
from lxml import etree
import requests
import unicodecsv as csv
import sys
import nltk
#Supress warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Pan_Pacific_Singapore Tripadvisor URL segments
tripadvisor_MAIN_url = 'https://www.tripadvisor.com.sg/'
tripadvisor_HOTEL_urlA = 'Hotel_Review-g294265-d302294-Reviews-or'
tripadvisor_HOTEL_urlB = '-Pan_Pacific_Singapore-Singapore.html'

#User Agent headers
#Get more headers: https://udger.com/resources/ua-list/browser-detail?browser=Chrome
header = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4'
headers = {'User-agent': header}

def Hotel_url(ReviewNum):
    return tripadvisor_MAIN_url+tripadvisor_HOTEL_urlA+ReviewNum+tripadvisor_HOTEL_urlB

def scrapeTo(PageNum):
    review_data = []
    for i in range(0,(PageNum)*5,5):
        global subject_xpath
        global review_xpath
        global name_xpath
        global date_xpath
        global location_xpath
        Hotel = Hotel_url(str(i))

        #HTML page
        page = requests.get(Hotel,headers = headers,verify=False)
        tree = html.fromstring(page.content)
        reviews = tree.xpath('//div[@class="review-container"]')

            #This will create a list of reviews:
        for review in reviews:
            subject_xpath = review.xpath('.//span[@class="noQuotes"]/text()')
            review_xpath = review.xpath('.//div[@class="ui_column is-9"]/div[2]/div/p[@class="partial_entry"]/text()')
            name_xpath = review.xpath('.//div[@class="info_text"]/div/text()')
            date_xpath = review.xpath('.//span[@class="ratingDate"]/text()')
            location_xpath = review.xpath('.//div[@class="info_text"]//strong/text()') # if review.xpath('.//div[@class="info_text"]//strong/text()') else ''

            subject = ''.join(subject_xpath) if subject_xpath else None
            review_entry = ''.join(review_xpath) if review_xpath else None
            name = ''.join(name_xpath) if name_xpath else None
            date = ''.join(date_xpath) if date_xpath else None
            location = ''.join(location_xpath).encode('utf-8').replace(u"\u2018", "'").replace(u"\u2019", "'") if location_xpath else ""

            data = {
            'subject' : subject,
            'review' : review_entry,
            'name' : name,
            'date' : date,
            'location' : location
            }

            review_data.append(data)

        #Progress bar:
        sys.stdout.write('\r')
        sys.stdout.write("%d%% Scraping..." % ((float(i)+5)/float(PageNum*5)*100))
        sys.stdout.flush()
        #print review_data

    return review_data

if __name__ == '__main__':
    reviews = scrapeTo(10)

    with open("Reviews Test.csv","wt+") as csvfile:
        reviewtable = csv.writer(csvfile,encoding='utf-8',delimiter=",")
        reviewtable.writerow(['Subject','Name','Review','Time','Location'])
        for review in reviews:
            reviewtable.writerow([
            review['subject'],
            review['name'],
            review['review'],
            review['date'],
            review['location']
            ])

    sys.stdout.write('\r')
    sys.stdout.write('Initial Scraping Completed! File saved as \'Reviews Test.csv\'')
    sys.stdout.flush()
