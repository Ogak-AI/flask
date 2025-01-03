from flask import Flask, render_template, request, redirect
import yt_dlp as youtube_dl

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Youtube_Video_Downloader.html")

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    
    cookies_file = "/home/ec2-user/Demo_Youtube_Downloader/cookies.txt"

    ydl_opts = {
        'format': 'best',
        'cookies': cookies_file,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [info_dict])
            video_url = next(f['url'] for f in formats if f['format_id'] == 'best')
        return redirect(video_url)
    except youtube_dl.utils.DownloadError as e:
        return str(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)


