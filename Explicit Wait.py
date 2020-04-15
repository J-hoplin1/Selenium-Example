from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings("ignore")

#

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
url = ''
driver.get(url)

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'')))          #WebDriverWait((driver),(timeout))
finally:
    print(driver.find_element_by_id('').text)
    driver.close()

'''
WebDriverWait 와 expected_conditions를 결합하여 사용하면 셀레니움에서 묵시적 대기 기능을 사용할 수 있다.

묵시적 대기는 DOM이 어떤 상태로 바뀔 때까지 기다린다는 점에서 명시적 대기와는 다르다.
'''