import requests
import bs4
import time
import csv
import re
import random
import pync
import os
import sys
from datetime import datetime

def fetch(user_agent, notifications):
    headers = {'User-Agent': user_agent}
    with open('amazon.csv', newline='') as datafile:
        data = csv.reader(datafile)
        output = ''
        with open('amazon.txt', 'a') as dataFile:
            dataFile.writelines('\n\n{:^53}\n\n'.format(datetime.now().strftime("  %d-%m-%Y %H:%M:%S  ")))
        for product in data:
            try:
                url = 'https://www.amazon.in/dp/' + product[0]
                offer_url = 'https://www.amazon.in/gp/offer-listing/' + product[0]
                req = requests.get(url, headers=headers)
                soup = bs4.BeautifulSoup(req.text, 'lxml')
                tag = soup.find(id='priceblock_ourprice')
                print(tag)
                price = int(re.sub('[^\d.]','',tag.text)[:-3])
                req1 = requests.get(offer_url, headers=headers)
                soup1 = bs4.BeautifulSoup(req1.text, 'lxml')
                tag1 = soup1.find('span', {'class':'olpOfferPrice'})
                price1 = int(re.sub('[^\d.]','',tag1.text.split('Rs. ')[1])[:-3])
                buy_within = int(product[2])
                buy_within1 = int(product[3])
                delivery_date = soup.find(id='ddmDeliveryMessage')
                print(price, price1, tag)
           #     if(product[0] == 'B084B8VXM3'):
           #         if len(delivery_date.text) > 1:
           #             pync.notify('*Available Now*\n{} | {}'.format(product[1], price), open=url)
           #             y = os.fork()
           #             if y==0:
           #                 os.system('osascript amazon.scpt +918149736237 "' + url + '"')
           #                 os.system('./facetime.applescript lalitmunne9@hotmail.com')
                    

                if price < buy_within or price1 < buy_within:
                    pync.notify('***STEAL DEAL***\n{} | {}'.format(product[1], price), open=url)
                    x = os.fork()
                    if x==0:
                        os.system('osascript amazon.scpt +918149736237 "' + url + '"')
                        os.system('./facetime.applescript lalitmunne9@hotmail.com')
                        os.exit()
                    with open('amazon.txt', 'a') as dataFile:
                        dataFile.writelines('***STEAL DEAL***\n{:>40}:{:6}\n'.format(product[1], price))
                else:
                    with open('amazon.txt', 'a') as dataFile:
                        dataFile.writelines('{:>40}:{:6}{:6}\n'.format(product[1],price, buy_within))
                    if price < buy_within1 or price1 < buy_within1:
                        pync.notify('#Buy Within\n{}({})'.format(price, buy_within1), title=product[1])
                    else: 
                        if notifications == 'show':
                            pync.notify('{}({})'.format(price, buy_within), title=product[1])
                time.sleep(2)
            except:
                try:
                    req1 = requests.get(offer_url, headers=headers)
                    soup1 = bs4.BeautifulSoup(req1.text, 'lxml')
                    tag1 = soup1.find('span', {'class':'olpOfferPrice'})
                    price1 = int(re.sub('[^\d.]','',tag1.text.split('Rs. ')[1])[:-3])
                    buy_within = int(product[2])
                    buy_within1 = int(product[3])
                    if price1 < buy_within:
                        pync.notify('***STEAL DEAL***\n{:40}:{:6}'.format(product[1], price1), open=url)
                        y = os.fork()
                        if y==0:
                            os.system('osascript amazon.scpt lalitmunne9@hotmail.com "' + url + '"')
                            os.system('./facetime.applescript lalitmunne9@hotmail.com')
                            os.exit()
                        with open('amazon.txt', 'a') as dataFile:
                            dataFile.writelines('***STEAL DEAL***\n{:>40}:{:6}\n'.format(product[1], price1))
                    else: 
                        with open('amazon.txt', 'a') as dataFile:
                            dataFile.writelines('{:>40}:{:6}{:6}\n'.format(product[1],price1, buy_within))
                        if price1 < buy_within1:
                            pync.notify('#Buy Within\n{}({})'.format(price1, buy_within1), title=product[1])
                        else:
                            if notifications == 'show':
                                pync.notify('{}({})'.format(price1, buy_within), title=product[1])

                except:
                    with open('amazon.txt', 'a') as dataFile:
                        dataFile.writelines('{:>40}: {:-^11}\n'.format(product[1], ''))
                    if notifications == 'show':
                        pync.notify('Not Available', title=product[1])
                    continue
                continue


user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

if len(sys.argv) > 1:
    fetch(random.choice(user_agent_list), sys.argv[1])
else:
    fetch(random.choice(user_agent_list), '')
sys.exit()

