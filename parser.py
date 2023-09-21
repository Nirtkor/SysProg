import requests

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params={'what': 'chart'})
chart = response.json()['chartPositions']
for track in chart:
    position = track['track']['chart']['position']
    title = track['track']['title']
    author = []
    artists = track['track']['artists']
    for i in range(min(len(artists), 10)):
        author.append(artists[i]['name'])
    with open('data.txt', 'a') as f:
        print(f"{position}: {author}: {title}", file=f)