'''
Selenium : 셀레니움 라이브러리는 Webdriver위에서 호출되는 API이다. Webdriver는 웹사이트를 불러올 수 있다는 점에서 브라우저와 비슷한 점도 조금 있지만
bs4의 BeautifulSoup객체와 마찬가지로 페이지 요소를 찾는데 쓸 수 있고 텍스트를 보내거나 클릭하는 등 페이지요소를 조작할 수 있고 스크레이퍼 작동할떄 필요한
행동을 할 수 있다.

크롬에서도 헤드리스 옵션을 본격적으로 지원하여 크롬 드라이버를 이용할 것이다. 다운로드는  https://chromedriver.chromium.org/downloads 여기서 할 수 있다. 크롬 드라이버는 자신의 컴퓨터와 맞는것을 찾아서
다운로드하는것을 권장한다.
'''

from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(executable_path='(웹드라이버 경로)',chrome_options=option)

url = ''

driver.get(url)
time.sleep(1)
print(driver.find_element_by_id('(id)').text)
driver.close()