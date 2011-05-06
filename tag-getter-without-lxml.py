#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import sys
import urllib
import urllib2

        
def get_texts_by_web(url, tag, attr, **kwargs):
    baseurl = "http://www.twigraphy.org/api/tag-getter"

    kwargs.update({
        'url': url,
        'tag': tag,
        'attr': attr,
        })
    
    url = '?'.join((baseurl, urllib.urlencode(kwargs)))
    #print url
    
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    return f.read()

def create_xpath(tag, attr):
    xpath = "//"
    xpath += tag
    if not attr == "":
        xpath += "[@"
        attr,value = attr.split("=")
        xpath += attr
        xpath += "=\"" + value + "\"]"
    #print "Created Xpath: " + xpath
    return xpath

if __name__ == "__main__":
    argv_len = len(sys.argv)
    if not (argv_len == 3 or argv_len == 4):
        print "Usage: python tag-getter.py URL TAG [ATTR]"
        exit()
    
    url = sys.argv[1].lower()
    tag = sys.argv[2].lower()
    if argv_len == 4:
        attr = sys.argv[3].lower()
    else:
        attr = ""
    text = get_texts_by_web(url, tag, attr)
    text_list = text.split('\n')
    i = 1
    for t in text_list[8:-4]: # remove needless tags
        if not t.split():
            continue
        print t
        i += 1
        


