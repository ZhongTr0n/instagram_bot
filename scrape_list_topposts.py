import csv
import re
import numpy as np
from bs4 import BeautifulSoup
import requests
import pandas as pd

import csv

url = "https://www.instagram.com/explore/tags/shanghai/"
r = requests.get(url).text                           # Go to website
soup = BeautifulSoup(r, "lxml")
print(type(soup))

p = soup.find_all('script')
paragraphs = []
for x in p:
    paragraphs.append(str(x))

pattern = re.compile(r'shortcode":"([a-zA-Z]+)"')

list_pic_id = []

for i in paragraphs:
    matches = pattern.finditer(i)
    for match in matches:
        list_pic_id.append((match.group(1)))

print(list_pic_id)

for i in list_pic_id:
    print(i)
