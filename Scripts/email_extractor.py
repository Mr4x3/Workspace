#!/usr/bin/python3
import sys
import re
import subprocess
from urllib.request import urlopen
from collections import defaultdict
import argparse
import string
import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser
from html.parser import HTMLParseError
import urllib.robotparser
import http.client

def getPage(url):
    try:
        f = urllib.request.urlopen(url)
        page = ""
        for i in f.readlines():
            page += i.decode('ISO-8859-1')
        date = f.headers['Last-Modified']
        if date == None:
            date = (0, 0, 0)
        else:
            date = date[:3]
        f.close()
        return (page, date, f.url)
    except urllib.error.URLError as detail:
        pass
        return (None, (0,0,0), "")

def joinUrls(baseUrl, newUrl):
    helpUrl, fragment = urllib.parse.urldefrag(newUrl)
    return urllib.parse.urljoin(baseUrl, helpUrl)

def getRobotParser(startUrl):
	rp = urllib.robotparser.RobotFileParser()
	robotUrl = urllib.parse.urljoin(startUrl, "/robots.txt")
	page, date, url = getPage(robotUrl)

	if page == None:
	    return None
	rp.parse(page)
	return rp

class MyHTMLParser(HTMLParser):
    def __init__(self, pageMap, redirects, baseUrl, maxUrls, blockExtensions, robotParser):
        HTMLParser.__init__(self)
        self.pageMap = pageMap
        self.redirects = redirects
        self.baseUrl = baseUrl
        self.server = urllib.parse.urlsplit(baseUrl)[1] # netloc in python 2.5
        self.maxUrls = maxUrls
        self.blockExtensions = blockExtensions
        self.robotParser = robotParser
    def hasBlockedExtension(self, url):
        p = urllib.parse.urlparse(url)
        path = p[2].upper() # path attribute
        for i in self.blockExtensions:
            if path.endswith(i):
                return 1
        return 0
    def handle_starttag(self, tag, attrs):
        if len(self.pageMap) >= self.maxUrls:
            return
        if (tag.upper() == "BASE"):
            if (attrs[0][0].upper() == "HREF"):
                self.baseUrl = joinUrls(self.baseUrl, attrs[0][1])
        if (tag.upper() == "A"):
            url = ""
            for attr in attrs:
                if (attr[0].upper() == "REL") and (attr[1].upper().find('NOFOLLOW') != -1):
                    return
                elif (attr[0].upper() == "HREF") and (attr[1].upper().find('MAILTO:') == -1):
                    url = joinUrls(self.baseUrl, attr[1])
            if url == "": return
            if urllib.parse.urlsplit(url)[1] != self.server:
                return
            if self.hasBlockedExtension(url) or self.redirects.count(url) > 0:
                return
            if (self.robotParser != None) and not(self.robotParser.can_fetch("*", url)):
                return
            if not(url in self.pageMap):
                self.pageMap[url] = ()

def getUrlToProcess(pageMap):
    for i in list(pageMap.keys()):
        if pageMap[i] == ():
            return i
    return None

def parsePages(startUrl, maxUrls, blockExtensions):
    pageMap = {}
    pageMap[startUrl] = ()
    redirects = []
    robotParser = getRobotParser(startUrl)
    while True:
        url = getUrlToProcess(pageMap)
        if url == None:
            break
        print(" ", url)
        page, date, newUrl = getPage(url)
        if page == None:
            del pageMap[url]
        elif url != newUrl:
            print(newUrl)
            del pageMap[url]
            pageMap[newUrl] = ()
            redirects.append(url)
        else:
            pageMap[url] = date
            parser = MyHTMLParser(pageMap, redirects, url, maxUrls, blockExtensions, robotParser)
            try:
                parser.feed(page)
                parser.close()
            except HTMLParseError:
                pass
            except UnicodeDecodeError:
                pass
    return pageMap

def grab_email(text):
    found = []
    mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
    for line in text:
        found.extend(mailsrch.findall(line))
    u = {}
    for item in found:
        u[item] = 1
    return list(u.keys())

def urltext(url):
    viewsource = urlopen(url).readlines()
    return viewsource

def crawl_site(url, limit):
    return parsePages(url, limit, 'None')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help = True)
    parser = argparse.ArgumentParser(description= 'Web Email Extractor')
    parser.add_argument('-l','--limit', action="store", default=100, dest= "limit", type= int, help='-l numUrlsToCrawl')
    parser.add_argument('-u','--url', action="store" ,dest= "url", help='-u http://sitename.com')
    myarguments = parser.parse_args()
    emails = defaultdict(int)
    for url in crawl_site(myarguments.url, myarguments.limit):
        for email in grab_email(urltext(url)):
            if email not in emails:
                print("cry"+ email)
            emails[email] += 1
