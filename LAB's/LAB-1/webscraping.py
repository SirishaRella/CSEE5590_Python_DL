import requests
from bs4 import BeautifulSoup

#getting the URL content
html_doc = requests.get('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')

#scrapping website using BeautifulSoup
soup = BeautifulSoup(html_doc.text, 'html.parser')
data = soup.find('table')
data = data.find('tbody')

#Digit flag
flag = 0
#saving results in text-file
with open("state-capitals.txt", "w", encoding="utf-8") as f:
    for row in data.find_all('tr')[2:]:
        items = row.find_all('td')
        f.write("State: " + row.th.a.string + "-" + row.td.string)
        for i in items[2].text:
            if i.isdigit():
                flag = 1
        if flag == 1:
            f.write("Capitals: " + items[1].text)
        else:
            f.write("Capitals: " + items[1].text + "," + items[2].text)








