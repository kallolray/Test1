import requests
import yt_dlp
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test1')
def test1():
    r = requests.get('https://api.github.com/users/kallolray')
    return r.content
 
@app.route('/test2/<ytID>')
def test2(ytID):
    link = 'https://youtube.com/watch?v='+ytID
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format':'all[acodec!=none]', 'xff':'IN'}) as video:
        info_dict = video.extract_info(link, download = False)
        video_title = info_dict['url']
        return video_title

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)