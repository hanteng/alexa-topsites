#!/usr/bin/env python
from __future__ import print_function
# python topsites_list_countries.py topsits_list_countries.tsv
from bs4 import BeautifulSoup
import requests
import sys
from math import ceil
import datetime
import codecs

BASE_URL='http://www.alexa.com/topsites/countries'
delimiter = '\t'

#debug '''
if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: specify outputfile (required)\n')
        sys.exit(1)
    file_name = sys.argv[1]

#debug '''

#def exe_script(): #debug
#file_name = "topsits_list_countries.tsv" #debug

    with codecs.open(file_name, "w", "utf-8") as f:
        now = datetime.datetime.now()
        now_prn = now.isoformat()

        response = requests.get(BASE_URL )  
        soup = BeautifulSoup(response.text , 'lxml')
        div = soup.find('div', {'class':'categories top'})

        for ul in div.contents:
            for row in ul.contents:
                c_code=''
                c_name=''
                try:
                    c_code = row.a.get("href").split('countries/')[1]
                    c_name = row.a.getText()
                except:
                    c_code = ''
                    c_name = ''

                if c_code != '' and c_name != '':
                    print ('{c}{d}{n}{d}{t}'.format(c=c_code, n=c_name, t=now_prn, d=delimiter), file=f)

#exe_script() #debug    
