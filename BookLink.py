from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re


def getData(url,tag=None,key=None,value=None):
    try:
        html = urlopen(url)
        #incase of Forbidden HTTPError message use below code
        #req = Request(url)
        #html = urlopen(req)
    except HTTPError as e:
        print("Http error -->"+e.msg)
        return None

    try:
        bsObject = BeautifulSoup(html, "html.parser")
        #dont bring links outside of given div
        data = bsObject.find(tag, {key:value}).find_all("a", attrs={'href': re.compile("^http://"),'href': re.compile("^https://")})

        #bring all links for given tags in given url
        #data = bsObject.find_all("a", attrs={'href': re.compile("^http://"),'href': re.compile("^https://")})

    except AttributeError as e:
        print("Attribute error")
        return None

    return data


def get_data_from_site(site_name,site_url,tag=None,key=None,value=None):

    data = getData(site_url,tag,key,value)

    if data is None:
        print("Data was not found")
    else:
        print(f"Links collected = {len(data)}, website = \"{site_name}\"")
        for link in data:
            print(link.get_text() + " -->> " + link['href'])

get_data_from_site("Programming-book.com","https://www.programming-book.com/","div","id","navigation")


