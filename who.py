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
    result = utils.tuple_to_list(re.findall(pattern,text))
    if len(result) == 0:
        return [""]
    name = utils.most_common_value(result)
    #^function that tallys values and list and returns most common
    return name

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
            #occurs if site denies access
            print e
        names.append(check_caps(page))
    return utils.most_common_value(names)

#Test
q2 = "who invented the lightbulb?"
results = utils.get_web_results(q2)
print find_name(results)
