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
    for i in range(10): # 접속 확인
        time.sleep(1)
        picker = driver.find_elements(By.CLASS_NAME, 'picker__box')
        if len(picker) != 0: break

    if len(picker) == 0: return # 10초동안 접속되지 않으면 종료

    #for x in range(2) :
    driver.find_element(By.CLASS_NAME, 'picker__nav--next').click()
    time.sleep(10)
    print("3333333333333")

    driver.quit()

if __name__ == "__main__":
    GetInfo()