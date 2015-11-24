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


def tuple_to_list(tuplist):
    """Converts list of tuples to single list.
    
    Converts regular expression output to list.
    
    Args:
        tuplist: A list of tuples, each tuple containg 2 values.
    Returns:
        A list containing the combined values within each individual tuple.
    """
    newList = []
    for tupl in tuplist:
        combined_string = ""
        for item in tupl:
            combined_string += item
        newList.append(combined_string)
    return newList
