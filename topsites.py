#!/usr/bin/env python
from __future__ import print_function
# python topsites.py MM 10 MM.tsv
from bs4 import BeautifulSoup
import requests
import sys
from math import ceil
import datetime
import codecs

BASE_URL='http://www.alexa.com/topsites/countries;%d/%s'
delimiter = '\t'

if __name__ == '__main__':
    
    if len(sys.argv) != 4:
        sys.stderr.write('Usage: COUNTRY-CODE TOP-N OUTPUTE-FILE\n')
        sys.exit(1)
    
    country_code = sys.argv[1].upper()
    number = int(sys.argv[2])
    file_name = sys.argv[3]


    page_numbers = int(ceil(number/25.0))

    with codecs.open(file_name, "w", "utf-8") as f:
        for page_num in range(0, page_numbers): 
            response = requests.get(BASE_URL % (page_num, country_code))  
            now = datetime.datetime.now()
            now_prn = now.isoformat()
            
            soup = BeautifulSoup(response.text, 'lxml')
            bullets = soup.find_all('li', {'class':'site-listing'})
        
            for bullet in bullets:
                items = bullet.find_all('div')
                rank = items[0].get_text().strip()
                site = items[1].p.get_text().strip()
                print (delimiter.join([country_code, rank, site, now_prn]), file=f)

