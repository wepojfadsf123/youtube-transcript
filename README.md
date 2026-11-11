# Scriptly — 유튜브 대본 추출기

## 실행 방법

Python 3.9 이상에서:

```bash
pip install flask youtube-transcript-api yt-dlp
python server.py
```

브라우저에서 http://localhost:5000 을 엽니다.

## 기능
- 유튜브 일반 영상, Shorts, 라이브 다시보기 URL 입력
- 공개 자막 추출 (한국어 우선, 영어 대체)
- 타임코드 켜기/끄기
- 연속 중복 자막 정리
- 대본 복사 및 TXT 저장

## 제한
- 유튜브의 접근 제한이나 자막 부재에 따라 실패할 수 있습니다.
- 서버를 외부에 공개하려면 요청 제한, 캐싱, 오류 처리, 보안 설정 등을 추가하세요.
- 타인의 콘텐츠는 권리와 이용 조건을 준수하여 사용하세요.
