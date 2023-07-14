from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) #안에다 경로를 넣으면 인식을 못한다. 그냥 같은 directory로.
url = 'http://decoder.kr/book-rubato/'
driver.get(url)

time.sleep(3)

#list = driver.find_elements_by_class_name('picker__day') #동작안함 #셀레니움4.10에선 find_elements(By.~, ~)이런식으로 기술해야한다
#day_list = driver.find_elements(By.CLASS_NAME, 'picker__day.picker__day--infocus')
#day_list = driver.find_elements(By.CLASS_NAME, 'picker__day')
day_list = driver.find_elements(By.TAG_NAME, 'td')




time.sleep(1)

available_slot = []

# td > div

for day in day_list: #td
    if(day.find_element(By.TAG_NAME, 'div').get_attribute('class') == "picker__day picker__day--infocus" ) :
        day_string = day.find_element(By.TAG_NAME, 'div').get_attribute('aria-label')
        day_class = day.find_element(By.TAG_NAME, 'div').get_attribute('class')
        print(day_string)
        print(day_class)

        day.click()
        time.sleep(5)

        #print("clicked")

        #time_tables = driver.find_element_by_class_name('ab-time-screen').find_elements(By.TAG_NAME,'button')
        # time_tables = driver.find_element(By.CLASS_NAME, 'ab-time-screen').find_elements(By.TAG_NAME,'button')
        # time_tables = time_tables[1:]  # 처음 날짜 표시는 제외
        # for time_table in time_tables:
        #     if not time_table.get_attribute('disabled'):
        #         print(time_table.get_attribute('value'))
                #available_slot.append(time_table.get_attribute('value'))

driver.close()
#while(True):
#    	pass