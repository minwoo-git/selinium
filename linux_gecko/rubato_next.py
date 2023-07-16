from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://decoder.kr/book-rubato/")
sleep(6)

for i in range(10):
  elem = driver.find_element(By.CSS_SELECTOR, ".picker__nav--next")
  print(elem)
  elem.click()
  sleep(3)

driver.close()