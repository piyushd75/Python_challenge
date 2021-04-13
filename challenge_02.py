import requests

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
r = requests.get(url)
r = r.text

from bs4 import BeautifulSoup as BS
from bs4 import Comment
soup = BS(r, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for c in comments:
    print(c)
    c.extract()

dict ={}
for character in c:
    if character in dict:
        dict[character]+=1
    else:
        dict[character]=1

string = ""
for key in dict:
    if dict.get(key) == 1:
        string += key
print(string)
