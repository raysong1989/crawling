from bs4 import BeautifulSoup
import requests
from hotdeal.models import Deal
from datetime import datetime, timedelta
# pip install python-telegram-bot
# 텔레그램 사용 
import telegram
# 텔레그래프 방 생성 후 token 값 입력 
#bot_token = ""
#bot = telegram.Bot(token = bot_token)

# 뽐뿌 페이지 
response = requests.get("http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu")

# 페이지 소스 코드 출력
#print(response.text)

# 페이지 가공
soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

def run():
    # delete deals older than 3days
    # row, _ = Deal.objects.filter(created_at__lte=datetime.now() - timedelta(days=3)).delete()
    # 하나의 상품 전체 정보 가져오기
    for item in soup.find_all("tr", {"class" : ["list0", "list1"]}):
        try:
            image = item.find("img", class_="thumb_border").get("src")[2:]
            image = "http://" + image
            #print(image)
            title = item.find("font", class_="list_title").text
            title = title.strip()
            link = item.find("font", class_="list_title").parent.get("href")
            link = "http://www.ppomppu.co.kr/zboard/" + link
            reply_count = item.find("span", class_="list_comment2").text
            reply_count = int(reploy_count)
            up_count = item.find_all("td")[-2].text
            up_count = up_count.split("-")[0]
            up_count = int(up_count)

            if up_count >= 5:
                # 대소문자 무시 
                if (Deal.objects.filter(link__iexact=link).count() == 0):
                    Deal(image_url=image, title=title, link=link, reply_count=reply_count, up_count=up_count).save()
                    # chat_id 입력 
                    #bot.sendMessage(chat_id, "{} {}".format(title, link))

        except Exception as e:
            continue

