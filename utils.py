import google, urllib2, bs4, re

def get_WebResults(q):
    results = google.search(q,num=10,start=0,stop=10)

    rlist = []
    for r in results:
        rlist.append(r)

    return rlist
