# 베이스 이미지 (Python 3.12 사용)
FROM python:3.12

# 작업 디렉터리 설정
WORKDIR /app

# 현재 디렉터리의 모든 파일을 컨테이너로 복사
COPY . /app

# 필요한 패키지 설치
RUN pip install uv
RUN uv venv .venv
RUN uv pip install flask


# Flask 환경 변수 설정
ENV FLASK_APP=app.py
ENV PATH="/app/.venv/bin:$PATH"

# 포트 개방

# Flask 서버 실행
CMD ["uv","run","python","app.py"]

