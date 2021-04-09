 ## 개발자 도구 보다는 변수마다 print 출력하여 구하는게 더 효율적

# python crawling
# pip install beautifulsoup4

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#https 경로를 적었을 경우 SSL Error 발생
#[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
import ssl

context = ssl._create_unverified_context()

baseUrl = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
# 한글, 영어 ascii encoding
#import urllib.parse
plusUrl = input("입력")
url = baseUrl + urllib.parse.quote_plus(plusUrl)

#html 가져오기
html = urllib.request.urlopen(url, context=context).read()
#html 분석
soup = BeautifulSoup(html, "html.parser")

#html 전부 가져온 뒤 class 전체 찾기
#개발자도구에서 class 값 수동으로 입력
#find & find_all (find 하나 찾기, find_all 모두 찾기)
#for 반복문을 통해 제목 추출
title = soup.find_all(class_="api_txt_lines")
print(title)

