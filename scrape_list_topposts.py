import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import mysql.connector


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
    

# FEED TO SQL DATABASE

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="internet",
  database="Instagram"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES (%s, %s, %s, %s, %s);"
vals = (1000, 'Misses', 'Python', 'Shanghai', 'China')

mycursor.execute(sql, vals)

mydb.commit()


sql_search = "SELECT COUNT(*) FROM Persons WHERE LastName = 'Miste';"
mycursor.execute(sql_search)
row = mycursor.fetchall()
print(row[0][0])


'''

x = conn.cursor()
x.execute("SELECT *  FROM anooog1")
x.execute (" INSERT INTO anooog1 VALUES ('%s','%s') ", (188,90))
row = x.fetchall()

  '''












