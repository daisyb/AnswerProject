from google import search
from bs4 import BeautifulSoup
from collections import Counter
import urllib2

def get_web_results(query):
    """Retrieves list of 20 urls from google based on query.

    Args:
       query: A string containg a google query.

    Returns:
       A list of urls
    """
    results = search(query,num=20,start=0,stop=10)
    rlist = []
    for r in results:
        rlist.append(r)
    return rlist

def read_page(url):
    """Reads a url and returns parsed html.
    
    Args:
        url: A string containg a valid url.

    Returns:
        A string containg the text of the webpage
        referenced by url
    """
    req = urllib2.urlopen(url)
    page = req.read()
    soup = BeautifulSoup(page, 'html.parser')
    return soup.get_text()

def most_common_value(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]
