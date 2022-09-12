# docker run -it -p 5000:5000 quay.io/codait/max-text-summarizer

# importing the requests library
import requests


payload = {"text":["MON TEXTE A RESUMER EST"]}
r = requests.post(url = 'http://0.0.0.0:5000/model/predict', json = payload)
print(r.url)
print(r.json())
