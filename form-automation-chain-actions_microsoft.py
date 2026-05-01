from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()
driver.get("https://forms.office.com/...")

time.sleep(1)

body = driver.find_element(By.TAG_NAME, "body")
time.sleep(2)
actions = ActionChains(driver)
actions.send_keys(Keys.SPACE).perform()
time.sleep(2)
actions.send_keys(Keys.TAB).perform()
time.sleep(0.5)
actions.send_keys(Keys.TAB).perform()
time.sleep(0.5)
actions.send_keys(Keys.TAB).perform()
time.sleep(0.5)
actions.send_keys(Keys.TAB).perform()
time.sleep(0.5)
time.sleep(0.5)
time.sleep(2)
i = 100
while i > 0:
    body.send_keys(Keys.SPACE)
    actions.send_keys("mas").perform()
    time.sleep(1)
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.SPACE)
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.SPACE)
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.SPACE)
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.SPACE)
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.SPACE)
    body.send_keys(Keys.TAB)
    body.send_keys(Keys.SPACE)
    i =- 1

time.sleep(3)
driver.quit()
