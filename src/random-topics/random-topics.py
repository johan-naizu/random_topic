import html5lib
import requests
from bs4 import BeautifulSoup
def get_topic():
    url="https://www.conversationstarters.com/generator.php"
    output=requests.get(url)
    soup = BeautifulSoup(output.content, 'html5lib')
    topics=soup.find("div", {"id": "random"})
    return topics.contents[1]
