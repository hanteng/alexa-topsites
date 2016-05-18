#Alexa Top Sites Scraper

This script does not use the official [Alexa API](http://docs.aws.amazon.com/AlexaTopSites/latest/) but is a page scraper. Anyone looking for a robust solution should use the official API since all page scrapers are fragile to page changes.

###Requirements
The [Requests](http://docs.python-requests.org/) and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) libraries are required.

###Usage
```python
python topsites.py COUNTRY-CODE TOP-N
```

- COUNTRY-CODE: should be the 2 character [ISO_3166-1 style](http://en.wikipedia.org/wiki/ISO_3166-1)
- TOP-N: the number of top sites to fetch
- Results are a space separated RANK, URL pair per line

Example
```
./python topsites.py MM 500 > MM.tsv
```

Output
MM.tsv
```
MM	1	Google.com
MM	2	Facebook.com
MM	3	Google.com.mm
MM	4	Youtube.com
MM	5	Wikipedia.org
MM	6	Amazon.com
MM	7	Blogspot.com
MM	8	Pcloud.com
MM	9	Channelmyanmar.com
....
MM	500	3dcreature.com
```
