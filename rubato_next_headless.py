from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from time import sleep

firefox_options = Options()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(options=firefox_options)
driver.get("http://decoder.kr/book-rubato/")
sleep(6)


for i in range(10):
  divMonth = driver.find_element(By.CSS_SELECTOR, ".picker__month")
  print(divMonth.text, end=' ')

  btnNext = driver.find_element(By.CSS_SELECTOR, ".picker__nav--next")
  btnNext.click()
  sleep(3)

  divMonth = driver.find_element(By.CSS_SELECTOR, ".picker__month")
  print('=>', divMonth.text)
  sleep(1)


driver.close()