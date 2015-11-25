import bs4, re, urllib2, utils

def check_pattern(text,pattern):
    """Find most common instance of pattern in text.
    
    Args:
        text: A string of text to search.
        pattern: A regular expression to search the text with.
    Returns:
        The most common string with the pattern
        capitol followed by lower case followed by space
        repeated 2-3 times.
    """
    result = utils.tuple_to_list(re.findall(pattern,text))
    if len(result) == 0:
        return [""]
    name = utils.most_common_value(result)
    #^function that tallys values and list and returns most common
    return name

def check_names(text):
    p = "([A-Z][a-z]*\s[A-Z][a-z]*)(\s[A-Z][a-z]*)?"
    return check_pattern(text,p)

def check_places(text):
    p = "([A-Z][a-z][a-z]*)(\s[A-Z][a-z]*)?(\s[A-Z][a-z]*)?"
    return check_pattern(text,p)

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
    url_list = utils.get_web_results(query)
    names = []
    for url in url_list:
        try:
            page = utils.read_page(url)
        except urllib2.HTTPError as e:
            #occurs if site denies access
            print e
        name = check_places(page)
        if "who" == question_type:
            name = check_names(page)
        if "where" == question_type:
            name = check_places(page)
        names.append(name)
    return names

def find_name(query, question_type):
    nl = noun_list(query, question_type)
    return utils.most_common_value(nl)

def find_place(query, question_type):
    nl = noun_list(query, question_type)
    return utils.most_common_value(nl)

#Test
q2 = "who invented ice cream?"
q3 = "where is mt. everest?"
print find_name(q2,"who")
#print find_name(q3,"where")
