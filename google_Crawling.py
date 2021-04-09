## selenium  사용 하지 않고 bs4 사용 시  header 값 필요
## selenium 사용하지 않을 시 class 값 구할 수 없음
## selenium 사용 시 개발자 도구 보다는 변수마다 print 출력하여 구하는게 더 효율적

# pip install selenium
# selenium 은  웹앱을 테스트하는데 이용하는 프레임워크
# webdriver라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 제어
# 웹 제어
from selenium import webdriver
# 한글, 영어 ascii encoding
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = "https://www.google.com/search?source=hp&ei=rqnAX9fHApb6-Qb3hY24Bg&q="
plusUrl = input("검색 : ")
url = baseUrl + quote_plus(plusUrl)

#selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
#절대경로 설정
driver = webdriver.Chrome("/Users/ray/Downloads/devScripts/devPython/chromedriver")
driver.get(url)

# 열린 페이지 소스 받기
html = driver.page_source
soup = BeautifulSoup(html)

divClass = soup.select(".d5oMvf")
#print(type(divClass))
# list 가져오기 위해 select_one 사용
for i in divClass:
    print(i.select_one(".d5oMvf").text)
    print(i.select_one(".Krnil").text)
    # a 태그에서 href 가져오기
    print(i.a.attrs["href"])
    print()

# driver 닫기
driver.close()


