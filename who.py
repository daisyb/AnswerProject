import bs4, re, urllib2, utils

def check_caps(text):
    """Finds most common string with 2-3 words beginning with capitol letters.
    
    Args:
        text: A string of text to search.
    Returns:
        The most common string with the pattern
        capitol followed by lower case followed by space
        repeated 2-3 times.
    """
    pattern="([A-Z][a-z]*\s[A-Z][a-z]*)(\s[A-Z][a-z]*)?"
    result = tuple_to_list(re.findall(pattern,text))
    name = utils.most_common_value(result)
    #^function that tallys values and list and returns most common
    return name

def tuple_to_list(tuplist):
    """Converts list of tuples to single list.
    
    Converts regular expression output to list.
    
    Args:
        tuplist: A list of tuples, each tuple containg 2 values.
    Returns:
        A list containing the combined values within each individual tuple.
    """
    newList = []
    for item in tuplist:
        val = item[0] + item[1]
        newList.append(val)
    return newList

def find_name(url_list):
    """Finds most common name used in the html for a list of urls.
    
    Reads each url in urlList calls checkCaps on each and returns
    the name most used in each website.

    Args:
        urlList: A list of strings containing urls.
    Returns:
        A string containg the most common name.
    """
    names = []
    for url in url_list:
        try:
            page = utils.read_page(url)
        except urllib2.HTTPError as e:
            #occurs if sitre denies access
            print e
        names.append(check_caps(page))
    print names
    return utils.most_common_value(names)

#Test
q2 = "who played spiderman?"
results = utils.get_web_results(q2)
print find_name(results)
