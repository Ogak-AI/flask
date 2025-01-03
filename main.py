from flask import Flask, render_template, request, redirect
import yt_dlp as youtube_dl

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Youtube_Video_Downloader.html")

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    ydl_opts = {'format': 'best'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict['url']
    return video_url

if __name__ == '__main__':
    app.run()

