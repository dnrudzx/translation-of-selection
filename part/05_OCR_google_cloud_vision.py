import io
import os

#구글클라우드플랫폼 - API및 서비스 - 사용자인증정보 - 서비스계정키
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./[Service_Account_Key].json"

from google.cloud import vision

client = vision.ImageAnnotatorClient()

file = os.path.abspath('capture.png')

with io.open(file, 'rb') as img:
    content = img.read()

img = vision.Image(content=content)

response = client.text_detection(image=img)

texts = response.text_annotations
for text in texts:
    print(format(text.description))