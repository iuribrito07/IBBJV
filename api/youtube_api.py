import requests

#Definindo a chave da API do YouTube
API_KEY = "SUA_CHAVE_AQUI"

#Definindo o canal do YouTube para coletar os vídeos
CHANNEL_ID = "SEU_CANAL_ID"

#Solicitação GET para a API do YouTube para obter os vídeos do canal
response = requests.get (f"https://www.googleapis.com/youtube/v3/videos?part=id,snippet&channelId={CHANNEL_ID}&maxResults=3&key={API_KEY}")")

#Verificação se a solicitação foi bem-sucedida
if response.status_code = 200:
    #Obter os vídeos da resposta
    videos = response.json()["items"]

    #Criando uma lista para armazenar os ID's dos vídeos
    video_ids = []

    #Usanod os ID's para criar elementos iframe em seu codigo HTML
    html_code = ""
    for video in videos:
        html_code += f'<iframe width="320" height="180" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'
    print(html_code)
else:
    print("Erro ao obter vídeos do canal")