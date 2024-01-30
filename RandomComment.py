import urllib.parse
import urllib.request
import json
import random

# API 키와 엔드포인트
api_key = 'AIzaSyDo-_c_8gqRfhBu3gDzkz0qCJ2hLyuVpmU'
api_end = 'https://www.googleapis.com/youtube/v3/commentThreads'

# 이용할 정보
video_id = 'RhAGVwpnA_s'
owner_name = '@hyundaisteelofficial'
num_winners = 5

# api 파라미터
api_param = {'key': api_key, 'part': 'snippet', 'videoId': video_id, 'maxResult': '20'}

# api 파라미터 인코딩
encoded_api_param = urllib.parse.urlencode(api_param)
raw_response = urllib.request.urlopen(f'{api_end}?{encoded_api_param}')
raw_comment = json.load(raw_response)
raw_response.close()

# 각 댓글을 하나씩 가져오기
user_lists = []
user_names = []

for item in raw_comment['items']:
    user_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
    user_names.append(user_name)
user_lists.append(user_names)
isNextPage = raw_comment.get('nextPageToken')

# 만약 댓글이 다음 페이지에서도 발견된다면
# 댓글을 다시 읽어온다.
count = 0
while isNextPage:
    if count > 100:
        break
    for item in raw_comment['items']:
        user_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        user_names.append(user_name)
    user_lists.append(user_names)
    isNextPage = raw_comment.get('nextPageToken')
    count += 1

# 리스트의 리스트에서 리스트를 꺼내, 그 안에 있는 원소를 직접 빈 리스트에 넣어준다.
res_list = []
for user_list in user_lists:
    for user_name in user_list:
        res_list.append(user_name)

# 중복 이름 제거
unique_list = list(set(res_list))

# 동영상 게시자의 이름을 제거
if owner_name in unique_list:
    unique_list.remove(owner_name)

# 리스트 원소 위치를 랜덤하게 정렬
random.shuffle(unique_list)

winners = unique_list[:num_winners]
print("설 한우 당첨 시청자")
print("=========================")
for i, winner in enumerate(winners):
    print(i+1, "번 : ", winner)
print("=========================")
print("축하드립니다!")