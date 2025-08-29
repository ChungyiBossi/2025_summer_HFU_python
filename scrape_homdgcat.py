
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.common.exceptions import NoSuchElementException # 找不到的例外狀況
from selenium.webdriver.common.by import By # DOM Tree 節點類型
import time
url = 'https://homdgcat.wiki/sr/char'
driver = webdriver.Chrome()
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class,'avatar-card')]")
    ))

# cards = driver.find_elements(By.XPATH, "//div[contains(@class,'avatar-card')]")
# five_stars_cards = driver.find_element(By.XPATH, "//div[contains(@class,'avatar-card') and contains(@class,'rar-5')]")
cards = driver.find_elements(By.CLASS_NAME,'avatar-card')
print(len(cards))
card_links = list()
for card in cards:
    href = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    card_links.append(href) # 收集連結
