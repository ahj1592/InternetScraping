import requests
from bs4 import BeautifulSoup
import datetime

URL = 'https://gall.dcinside.com/mgallery/board/lists/?id=kospi&page=' # 코스피마이너갤러리
#URL = 'https://gall.dcinside.com/mgallery/board/lists/?id=stockus&page=' # 미국주식마이너갤러리

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

print('Program start at:', datetime.datetime.now())

for page_num in range(1, 5):
    print(f'========== 현재 페이지 번호: {page_num} ==========')
    url = URL + str(page_num)
    resp = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    contents = soup.find('tbody').find_all('tr')

    for content in contents:
        # 말머리가 '일반'인 것만 추출
        subject_tag = content.find('td', class_='gall_subject')
        subject = subject_tag.text
    
        if subject != "일반":
            continue

        # 제목 추출
        title_tag = content.find('a')
        title = title_tag.text
        print('제목:', title)

        # 댓글수 추출
        reply_tag = content.find('span', class_='reply_num')
        if reply_tag == None:
            reply_num = 0
        else:
            reply_num = int(reply_tag.text[1:-1]) # remove '[', ']'
        print('댓글수:', reply_num)

        # 글쓴이 추출
        writer_tag = content.find('td', class_='gall_writer ub-writer').find('span', class_='nickname')
        writer = writer_tag.text
        print('글쓴이:', writer)

        # 작성일
        date_tag = content.find('td', class_='gall_date')
        date_dict = date_tag.attrs
        print('작성일:', date_dict['title'])


        # 조회 추출
        views_tag = content.find('td', class_='gall_count')
        views = views_tag.text
        print("조회:", views)
    
        # 추천 추출
        recommend_tag = content.find('td', class_='gall_recommend')
        recommend = recommend_tag.text
        print("추천:", recommend)

        print('=' * 50)
    
print('Program End at:', datetime.datetime.now())