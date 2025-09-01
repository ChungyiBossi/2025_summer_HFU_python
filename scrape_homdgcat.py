
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

# 蒐集細節Link
cards = driver.find_elements(By.CLASS_NAME,'avatar-card')
print(len(cards))
card_links = list()
for card in cards:
    href = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    card_links.append(href) # 收集連結


# 擷取細部資料
for link in card_links:
    driver.get(link)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "sbp")
        ))
    try:
        # 技能資訊(sbp x n)
        skill_info = []
        skill_blocks = driver.find_elements(By.CSS_SELECTOR, "p[style*='margin-bottom: 12px']")
        for skill_block in skill_blocks:
            sbps = skill_block.find_elements(By.CLASS_NAME, "sbp")
            texts = [sbp.text for sbp in sbps if sbp.text != ''] # 過濾空字串
            skill_info.append(" ".join(texts)) # 合併字串
        # 技能描述(sd)
        skill_describe = [describe.text for describe in driver.find_elements(By.CLASS_NAME, "sd")]
    except NoSuchElementException:
        print("此卡片沒有技能區塊")

    print("卡片連結: ", link)
    print(f"技能資訊 {len(skill_info)}: ", skill_info)
    print(f"技能描述 {len(skill_describe)}: ", skill_describe)

    print("="*50)