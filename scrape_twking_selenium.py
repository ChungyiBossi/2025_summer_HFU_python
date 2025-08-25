# 先模擬爬小說王
# (1) import webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # 找不到的例外狀況
from selenium.webdriver.common.by import By # DOM Tree 節點類型
driver = webdriver.Chrome()
driver.get("https://www.twking.org/")

booktops = driver.find_elements(By.CLASS_NAME, "booktop")
for booktop in booktops:
    books = booktop.find_elements(By.TAG_NAME, "p")
    for book in books:
        try: 
            book_a = book.find_element(By.TAG_NAME, "a")
            print('\t', book_a.text, book_a.get_attribute('href'))
        except NoSuchElementException: # 例外處理，處理找不到的情況
            print(book.text)

driver.quit() # 關掉瀏覽器