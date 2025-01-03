from flask import Flask, render_template, request, redirect, flash, url_for
import subprocess

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flash messages

@app.route("/")
def index():
    return render_template("Youtube_Video_Downloader.html")

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    cookies_file = "/home/ec2-user/Demo_Youtube_Downloader/cookies.txt"

    try:
        # Run the yt-dlp command with cookies
        result = subprocess.run(
            ["yt-dlp", "--cookies", cookies_file, "--get-url", url],
            capture_output=True, text=True, check=True
        )
        video_url = result.stdout.strip()
        return redirect(video_url)
    except subprocess.CalledProcessError as e:
        flash(f"Error: {e.stderr}")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)


