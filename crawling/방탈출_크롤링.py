from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime as dt
import platform
from dateutil.relativedelta import relativedelta

def GetInfo():
    start = time.time()

    # 윈도우에서 테스트할 때와 EC2에서 실행할 때 Chrome 설정이 다름
    if 'Windows' in platform.platform():
        print("OOOOOOOO")
        driver = webdriver.Chrome()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome('./chromedriver', options=options)

    available_slot = []
    #try:
        # 0. 접속
    url = 'http://decoder.kr/book-rubato/'
    driver.get(url)
    
    a =  driver.find_elements(By.TAG_NAME, 'td') 
    
    for m in range(2):
        print("111111111111")

        time.sleep(3)

        driver.find_element(By.CLASS_NAME, 'picker__nav--next').click()
       
        
    
    driver.quit()

if __name__ == "__main__":
    GetInfo()