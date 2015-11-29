import re, urllib2
from google import search
from bs4 import BeautifulSoup
from collections import Counter

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
    data = Counter(lst).most_common(1)
    return data[0][0]

def tuple_to_list(tuplist,check_places):
    """Converts list of tuples to single list.
    
    Converts regular expression output to list. Gets rid of stop words.
    If check_places is true also checks if values are contained in
    places.txt
    
    Args:
        tuplist: A list of tuples, each tuple containg 2 values.
        check_places: boolean, if true check values against places.txt

    Returns:
        A list containing the combined values within each individual tuple.
    """
    f = open("stopwords.txt", "r")
    stop = f.read()
    f.close()
    if check_places:
        f = open("places.txt","r");
        places = f.read()
        f.close()
    newList = []
    for tupl in tuplist:
        combined_string = ""
        n = 1
        for item in tupl:
            #checks for stop words
            if item.lower() not in stop:
                if check_places:
                    if item in places:
                    #makes words in places.txt more likely
                        n = 5
                combined_string += item
        if combined_string != "":
            while n > 0:
                newList.append(combined_string)
                n -= 1
    return newList

def check_names(text):
    """Checks text for name pattern.

    Args:
        text: A string of text to search

    Returns:
        The most common string with the pattern
        capitol followed by lower case followed by space
        repeated 2-3 times.
    """
    pattern = "([A-Z][a-z][a-z]*\s[A-Z][a-z]*)(\s[A-Z][a-z][a-z]*)?"
    result = tuple_to_list(re.findall(pattern,text),False)
    if len(result) == 0:
        return [""]
    return most_common_value(result)

def check_places(text):
    """Checks text for name pattern.

    Args:
        text: A string of text to search

    Returns:
        The most common string with the pattern
        capitol followed by lower case
        repeated 1-3 times.
    """
    pattern = "([A-Z][a-z][a-z]*)(\s[A-Z][a-z]*)?(\s[A-Z][a-z]*)?"
    result = tuple_to_list(re.findall(pattern,text),True)
    if len(result) == 0:
        return [""]
    return most_common_value(result)

def noun_list(query, question_type):
    """Finds most value in the query results based on the question_type.

    Searches the query results from get_web_results for the pattern
    matching the question_type.

    Args:
        query: A string containing a who search query.
        question_type: A string containing either who, where, or when

    Returns:
        A list of results.
    """
    url_list = get_web_results(query)
    names = []
    for url in url_list:
        try:
            page = read_page(url)
        except (urllib2.HTTPError, urllib2.URLError) as e:
            #occurs if site denies access
            print e
        name = ""
        if "who" == question_type:
            name = check_names(page)
        if "where" == question_type:
            name = check_places(page)
        names.append(name)
    return names

def find_name(query, question_type):
    """Finds most common name in results from query.
    
    Args:
        query: string with a question
        questiontype: string containing who

    Return:
        String containg a name (hopefully)
    """
    nl = noun_list(query, question_type)
    for noun in nl:
        if noun.lower() in query.lower():
            nl.remove(noun)
    return most_common_value(nl)

def find_place(query, question_type):
    """Finds most common place in results from query.
    
    Args:
        query: string with a question
        questiontype: string containing where

    Return:
        String containg a place (hopefully)
    """
    nl = noun_list(query, question_type)
    return most_common_value(nl)
