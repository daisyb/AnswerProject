import bs4, re

def checkCaps(q):
    pattern="[A-Z][a-z]*\s[A-Z][a-z]*"
    result = re.findall(pattern,q)
    return result

q1= "Name Middle Last Other"
print checkCaps(q1)
