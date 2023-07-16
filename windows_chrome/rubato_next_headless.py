from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from time import sleep

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("http://decoder.kr/book-rubato/")
sleep(6)

driver.execute_script("var menu = document.querySelector('#menu-decoder'); menu.parentNode.removeChild(menu);")

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