# KREAM 가격 예측 프로젝트 설정 파일
# 이 파일을 config.py로 복사하고 실제 값으로 변경하세요

# Naver API 키 (블로그 검색용 - blog.ipynb에서 사용)
NAVER_CLIENT_ID = "your_naver_client_id"
NAVER_CLIENT_SECRET = "your_naver_client_secret"

# Naver 검색 API 키 (social_media_mentions.ipynb에서 사용)
NAVER_SEARCH_CLIENT_ID = "your_naver_search_client_id"
NAVER_SEARCH_CLIENT_SECRET = "your_naver_search_client_secret"

# Naver Cloud Platform API 키 (감정 분석용 - social_media_mentions.ipynb에서 사용)
NCP_CLIENT_ID = "your_ncp_client_id"
NCP_CLIENT_SECRET = "your_ncp_client_secret"

# KREAM 로그인 정보 (선택사항 - 크롤링 시 필요)
KREAM_EMAIL = "your_email@example.com"
KREAM_PASSWORD = "your_password"

# 데이터 경로
DATA_PATH = "./dataset/data/"
MODEL_PATH = "./models/"

# 기타 설정
CHROME_DRIVER_PATH = None  # None이면 webdriver-manager가 자동으로 설치

