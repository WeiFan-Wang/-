import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def search(self, queryStr):
queryStr = urllib2.quote(queryStr)
url = 'https://www.books.com.tw/web/books/' % queryStr
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()
results = self.extractSearchResults(html)

resp = requests.get('<self.extractSearchResults(html)>')
soup = BeautifulSoup(resp.text, 'html.parser')

catalog = soup.find(class_='mod_b type02_l001-1 clearfix')
catalogList = catalog.find_all('a')
catalogDict = dict()
for c in catalogList:
    title = c.text
    href = c.get('href')
    href = href.split('&')[0]
    catalogDict[title] = href

df = pd.DataFrame(columns=['類型', '書名', '作者', '優惠價'])

    books = soup.find(class_='mod_a clearfix')
    items = books.find_all(class_='item')


    for i, item in enumerate(items):
        if i == 20:
            break
        time.sleep(60)

# 取得書名
        book_name = item.find('img').get('alt')

# 取得作者        
        if item.find_all('li')[0].text[0:2] == '作者':
            book_author = item.find_all('li')[0].find('a').text
        else:
            book_author = ""

# 取得價格
        book_price = item.find_all('b')[-1].text

# 存入dataframe
        df.loc[len(df)+1] = None
        df.iloc[-1]['類型'] = title
        df.iloc[-1]['書名'] = book_name
        df.iloc[-1]['作者'] = book_author
        df.iloc[-1]['優惠價'] = book_price

# 轉出csv檔
df.to_csv('booksScraper.csv')
