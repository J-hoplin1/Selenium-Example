'''
클라이언트 쪽 리다이렉트는 페이지 콘텐츠를 보내기 전에 서버에서 실행하는 리다이렉트와는 달리 브라우저에서 자바스크립트를 통해 실행되는 리다이렉트이다.

서버쪽 리다이렉트의 경우 셀레니움을 전혀 쓰지 않고 urllib, bs4만 이용해서 쉽게 처리할 수 있다. 반면에 클라이언트쪽 리다이렉트는 자바스크립트를 실제실행하지 않으면
전혀 처리할 수 없다.

셀레니움은 자바스크립트 리다이렉트를 다른 자바스크립트와 같은 방법으로 처리합니다. 리다이렉트에서 중요한것은 페이지가 리다이렉트를 끝낸 시점이 언제인지 아는것이다.

리다이렉트 감지를 하기위해서는 DOM 요소하나를 주시하고 있어야한다. NoSuchElementException예외를 일으킬 떄(=페이지의 DOM에 더는 존재하지 않을 때)가 바로 리다이렉트가 일어난 시점이다.
'''

from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
    element = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 3:
            print("Redirection finished!")
            return
        time.sleep(1)
        try:
            element == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

print("Redirecting Client.... ")
opt = webdriver.ChromeOptions()
#Add option : Headless
opt.add_argument('headless')
driver = webdriver.Chrome(chrome_options=opt)
url = ''
driver.get(url)
waitForLoad(driver)
print(driver.page_source)