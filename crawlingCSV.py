# 내장되어 있는 lib
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
# 한글, 영어 ascii encoding
from urllib.parse import quote_plus

import ssl
context = ssl._create_unverified_context()

#api_txt_lines total_tit

search = input("검색 : ")
# format 하기 위해 f 사용
url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={quote_plus(search)}"

html = urlopen(url, context=context).read()
soup = BeautifulSoup(html, "html.parser")

# 빈 칸 있을 경우 . 사용, 클래스가 2개라고 명시
total = soup.select(".api_txt_lines.total_tit")

# CSV File Save
searchList = []

for i in total:
    temp = []
    # 제목
    temp.append(i.text)
    # 주소(속성)
    temp.append(i.attrs["href"])
    # 리스트 안에 리스트 적용
    # ex) [1,2,3,[4,5,6]]
    searchList.append(temp)

#text 사용하기 위해 w 적용
f = open(f"{search}.csv", "w", encoding="utf-8")
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)

f.close()

print("CSV File 완료")

