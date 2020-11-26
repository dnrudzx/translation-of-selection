import requests #파파고를 위한 임포트

#개인키
client_id = "[NAVER Client id]"
client_secret = "[NAVER Client Secret]"

#파파고 오픈api URL
url = "https://openapi.naver.com/v1/papago/n2mt"
headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

#Sample text : 그냥 Pypi 메인페이지에 적힌거 긁어온 것
data = 'Find, install and publish Python packages with the Python Package Index'

#번역 속성 지정 : source(번역전 언어), target(번역후 언어), text(원문)
params = {"source": "en", "target": "ko", "text": data}

try:
    #연결
    response = requests.post(url, headers=headers, data=params)
    result = response.json()

    print(result['message']['result']['translatedText'])

except Exception as e:
    print(e)