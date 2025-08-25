# (1) 安裝漂亮湯
# pip install Beautifulsoup4

# (2) 安裝 requests
# pip install requests

# (3) 匯入requests 和 BeautifulSoup
import requests
from bs4 import BeautifulSoup

# (4) 請求目標網頁
url = "https://www.twking.org/"
response = requests.get(url) # 使用 GET 方法請求網頁
response.encoding = 'utf-8' # 設定編碼為 utf-8，否則會看到亂碼
print("HTML 字串：", len(response.text)) # 取得網頁的 HTML 內容
print("狀態碼： ", response.status_code) # 取得 HTTP 狀態碼(三碼數字)

# (5) 解析 HTML
soup = BeautifulSoup(response.text, 'html.parser') # 使用 html.parser 解析 HTML
booktops = soup.find_all('div', class_='booktop') # 找出所有 class 為 booktop 的 div 標籤
print("排行榜的數量： ", len(booktops)) # 印出找到的 booktop 數量

for booktop in booktops:
    books = booktop.find_all('p') # 沒有其他的屬性值
    for book in books:
        if book.find('a'): # 確保有 a 標籤
            print('\t', book.text, book.find('a')['href']) # 印出書名和連結
        else:
            print(book.text)