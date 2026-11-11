"""Local development server. Install: pip install flask youtube-transcript-api yt-dlp"""
from flask import Flask, request, jsonify, send_from_directory
from youtube_transcript_api import YouTubeTranscriptApi
from yt_dlp import YoutubeDL
import re

app = Flask(__name__, static_folder='.')

@app.get('/')
def home():
    return send_from_directory('.', 'index.html')

@app.get('/api/transcript')
def transcript():
    video_id = request.args.get('videoId', '')
    if not re.fullmatch(r'[\w-]{11}', video_id):
        return jsonify(error='유효하지 않은 영상 ID입니다.'), 400
    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=['ko', 'en'])
        entries = [{'start': x.start, 'text': x.text} for x in fetched]
        title = '추출된 대본'
        try:
            with YoutubeDL({'quiet': True, 'skip_download': True, 'no_warnings': True}) as ydl:
                info = ydl.extract_info('https://www.youtube.com/watch?v=' + video_id, download=False)
                title = info.get('title') or title
        except Exception:
            pass
        return jsonify(title=title, entries=entries)
    except Exception as e:
        return jsonify(error='자막 추출 실패: 공개 자막이 없거나 접근이 제한되어 있을 수 있습니다. (' + type(e).__name__ + ')'), 422

if __name__ == '__main__':
    app.run(debug=True, port=5000)
