# docker run -it -p 5000:5000 quay.io/codait/max-text-summarizer

# importing the requests library
import requests

def resume_text(texte):
#fonction qui récupère une chaîne de caractère et qui affiche un résumé de cette fonction
    payload = {"text":[texte]}
    r = requests.post(url = 'http://0.0.0.0:5000/model/predict', json = payload)
    return r.json()


#payload = {"text":["MON TEXTE A RESUMER EST"]}
#test_fonct1= resume_text("MON TEXTE A RESUMER EST")
#print(test_fonct1)

#fonction qui prend le texte en param et qui renvoie le résumer