 ## 개발자 도구 보다는 변수마다 print 출력하여 구하는게 더 효율적

from urllib.request import urlopen
# 한글, 영어 ascii encoding
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()

baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
plusUrl = input("입력 : ")
url = baseUrl + quote_plus(plusUrl)

#print(url)

html = urlopen(url, context=context).read()
soup = BeautifulSoup(html, "html.parser")
img = soup.find_all(class_="_image_source")

n = 1
for i in img:
    imgUrl = i["data-source"]
    # 따로 닫는걸 지정하지 않아도 됨
    with urlopen(imgUrl) as f:
        # image name
        # 텍스트가 아니기 때문에 바이너리 형식으로 지정
        with open(plusUrl + str(n) + "jpg", "wb") as h:
            img = f.read()
            h.write(img)

        n += 1

print("다운로드 완료")


