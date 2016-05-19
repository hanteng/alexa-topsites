#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import sys
from math import ceil

BASE_URL='http://www.alexa.com/siteinfo/{s}'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: site name\n')
        sys.exit(1)
    
    site_name = sys.argv[1].lower()
    delimiter = '\t'


    response = requests.get(BASE_URL.format(s=site_name))
    soup = BeautifulSoup(response.text , 'lxml')
    table = soup.find('table', {'id':'demographics_div_country_table'})


    for row in table.tbody.contents:
        c_code=''
        p_visitor=''
        try:
            c_code = row.a.get("href").split('countries/')[1]
            p_visitor = row.span.contents[0]
        except:
            c_code = ''
            p_visitor = ''
        if c_code != '' and p_visitor != '':
            print ('{s}{d}{c}{d}{p}'.format(s=site_name, c=c_code, d=delimiter, p=p_visitor))
