# Selenium 공식문서 getting_started 예제 - windows chrome 용
# https://selenium-python.readthedocs.io/getting-started.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from time import sleep

options = Options()
#==== 인증서 오류 (Error parsing cert retrieved from AIA) 해결 ====
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#=================================================================

driver = webdriver.Chrome(options=options)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close()