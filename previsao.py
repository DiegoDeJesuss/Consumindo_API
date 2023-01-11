import requests

API_key = "c529fb87e1b4f72553cac6f2658816ea"
cidade = "rio de janeiro"

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_key}&lang=pt_br"


requisicao = requests.get(link)

print(requisicao)

requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15

print(descricao, f'{temperatura} C')