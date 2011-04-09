#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import sys
import urllib2
import lxml.html
        
def get_texts(url, tag):
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.HTTPError, e:
        # If returned 404
        #print e.read()
        print "404 Not Found" + BR
        return
        
    root = lxml.html.fromstring(html)
    anchors = root.xpath(tag)

    text_list = []
    for a in anchors:
        text = lxml.html.tostring(a, method='text', encoding='utf-8')
        #print text.strip('\t\n')
        text_list.append(text.strip('\t\n'))
    if not text_list:
        text = "There are no tags in this page."
        text_list.append(text)
    return text_list

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
    xpath = create_xpath(tag, attr)
    text_list = get_texts(url, xpath)
    for t in text_list:
        print t
    
