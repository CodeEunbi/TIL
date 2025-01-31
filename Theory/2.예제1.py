import requests

#서울의 위도
lat = 37.56
#서울의 경도
lon = 126.97
API_key = ''
#API 요청 URL
URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
data = requests.get(URL).json()
#key값 출력
print(data.keys())

#데이터 추출 - 원하는 값만 추출
