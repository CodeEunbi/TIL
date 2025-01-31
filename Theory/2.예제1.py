import requests

#서울위 위도
lat = 37.56
#서울의 경도
lon = 126.97
API_key = '776c53f8b46f57dd9223b306b4cbaa9d'
#API 요청 URL
URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
data = requests.get(URL).json()
print(data)