#!/usr/bin/env python3
import googlesearch as gs 
import requests
import string
from lxml import html
from bs4 import BeautifulSoup

def chat_query(ques,index=0):
    search_urls=list(gs.search(query=ques,tld='com',lang='en',num=3,start=0,stop=3,pause=1))
    #print(search_urls)
    page=requests.get(search_urls[index])
    tree=html.fromstring(page.content)
    #print(page)
    #print(tree)
    soup=BeautifulSoup(page.content,features='lxml')
    #print(soup)
    detail=soup.findAll('p')
    intermediateText=''
    for element in detail:
        intermediateText+='\n'+''.join(element.findAll(text=True))
    intermediateText=intermediateText.replace('\n','')
    #print(intermediateText)
    firstSentence=intermediateText.split('.')
    #print(firstSentence)
    firstSentence=firstSentence[0].split('?')[0]
    #print(firstSentence)
    chars_without_whitespace=firstSentence.translate(
        {
            ord(c): None for c in string.whitespace
        }
    )
    if len(firstSentence)>0:
        return firstSentence
    else:
        return 'No results'





