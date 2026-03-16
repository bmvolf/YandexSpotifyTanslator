from yandex_music import Client, PlaylistId
import Data
import FileManager
import json
import re
#Очень лень делать нормальную проверку на дурака
def parseLink(link):
    srcMatch = re.search(r'src="([^"]+)"', link)
    if srcMatch:
        src = srcMatch.group(1)
    playlistNumber = src.split('/')
    Data.Playlist = playlistNumber[-1]
    Data.User = playlistNumber[-2]


def printTrack(playlist):
    title = playlist.title
    cnt = playlist.track_count
    songs = playlist.tracks
    names = []
    artists = []
    print(f'{title}. Количество треков: {cnt}')
    for song in songs:
        s = song.fetchTrack()
        names.append(s.title)
        artists.append(s.artistsName()[0])
    FileManager.write(json.dumps([names, artists, title], ensure_ascii=False))
    print("Done!")


print('Это приложение позволяет переносить плейлисты из яндекс музыки в спотифай\n' \
'Для начала работы вставьте html ссылку на ваш плейлист')
parseLink(input())
client = Client(Data.Token).init()
playlist = client.users_playlists(Data.Playlist, Data.User)
printTrack(playlist)

#Здесь должно быть продолжение, где треки по имени и автору переводятся в спотифае через его апи
#Но апи спотика работает только через VPN
#А библа, для сбора названий с яндекса выдает ошибку по времени при использовании Впн, хотя даже без него она медленная
#И как это чинить я не знаю