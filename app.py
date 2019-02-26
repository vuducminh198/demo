from flask import Flask, json
import urllib.request
import requests
import os

# api_url: str = input('Nhập API: ').strip()
api_url = 'https://mp3.zing.vn/xhr/media/get-source?type=album&key=LGxHyLZZHHdFRzatHtDmZmyZWQHXJQLNi'
json_data = requests.get(api_url).json()
try:
    os.mkdir('download')
except Exception as error:
    pass

for song in json_data['data']['items']:
    print(str(song['title']))
    urllib.request.urlretrieve(
        str(song['source']['128']).replace('//mp3-s1-zmp3.zadn.vn/', 'http://vnno-zn-5-tf-mp3-s1-zmp3.zadn.vn/'),
        './download/{}.mp3'.format(str(song['name']).replace(' ', '').replace('?', '')))
    print('[OK] Đã tải {}'.format(song['name']))

#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
