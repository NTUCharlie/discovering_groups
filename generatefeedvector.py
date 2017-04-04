import feedparser
import re

def getwordcounts(url):
    d=feedparser.parse(url)
    wc={}
    for e in d.entries:
        if 'summary' in e: summary=e.summary
        else: summary=e.description
        words=getwords(e.title+' '+summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word]+=1
    return d.feed.title, wc

def getwords(html):
    txt=re.compile(r'<[^>]+>').sub('',html)#remove all html tags
    words=re.compile(r'[^A-Z^a-z]+').split(txt)#split all words by nonalpha characters
    return [word.lower() for word in words if word!='']# convert to lower case

apcount={}
wordcounts={}

i=0
with open('/home/charlie/discovering_groups/feedlist.txt','r') as file:
    for feedurl in file.readlines():
        print(feedurl)
        i=i+1
        #title,wc=getwordcounts(feedurl)

print(i)




