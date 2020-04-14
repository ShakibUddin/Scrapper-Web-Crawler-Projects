from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_data(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsobj = BeautifulSoup(html,"html.parser")
        data=bsobj.find_all("p")#find_all() returns a list of <p> tags...#find() returns only the first occurrence of <p> tag
    except AttributeError as e:
        return None

    return data


data=get_data("https://www.who.int/health-topics/coronavirus#tab=tab_1")#url

if data == None:
    print("Data could not be found")
else:
    for line in data:  # as data is a list i need to loop through to convert each tag to text
        print(line.get_text())

