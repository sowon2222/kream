# KREAM 스니커즈 가격 예측 프로젝트

## 프로젝트 개요

본 프로젝트는 KREAM 플랫폼의 스니커즈 거래 데이터와 **소셜 미디어 트렌드(블로그 언급량 및 감정 분석)**를 결합하여
향후 리셀(Resell) 가격을 예측하는 머신러닝 기반 데이터 분석 시스템입니다.

데이터 수집부터 전처리, 모델 학습, 시각화까지의 전체 파이프라인을 직접 구현하였으며,
리셀 시장의 가격 변동성을 정량적으로 분석하여 데이터 기반 의사결정 지원 시스템을 구축하는 것을 목표로 했습니다.

## 주요 기능

- **웹 크롤링**: KREAM 플랫폼의 스니커즈 거래 데이터 자동 수집
- **데이터 수집**: 블로그 검색 결과, 구매/판매 내역, 거래 로그 등 다차원 데이터 확보
- **감정 분석**: 네이버 블로그 게시물의 감정(긍정/부정/중립) 분류
- **머신러닝**: 회귀 모델(Ridge, Lasso, RandomForest, GB) 비교 및 최적 모델 선정
- **가격 예측**: 특정 스니커즈 모델의 향후 예상 거래 가격 예측

## 기술 스택

### 데이터 수집
- **Selenium** – KREAM 플랫폼 자동 크롤링
- **Naver API** – 블로그 검색 및 감정 분석
- **BeautifulSoup** – HTML 파싱 및 데이터 추출

### 데이터 분석 및 머신러닝
- **Python 3.x**
- **Pandas / NumPy** – 데이터 처리 및 수치 연산
- **Scikit-learn** – 머신러닝 모델 구현
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - Ridge Regression
  - Lasso Regression

### 시각화
- **Matplotlib** – 모델 결과 및 피처 중요도 시각화

## 프로젝트 구조

```
kream_project/
│
├── notebooks/                      # 분석 노트북
│   ├── crawling.ipynb              # KREAM 데이터 크롤링
│   ├── blog.ipynb                  # 블로그 검색 데이터 수집
│   ├── social_media_mentions.ipynb # 소셜 미디어 감정 분석
│   ├── extract_data.ipynb          # 데이터 통합
│   ├── model_train.ipynb           # 모델 학습 및 평가
│   └── kream_stock_predict.ipynb   # 가격 예측
│
├── dataset/                        # 데이터셋
│   └── data/
│       ├── BLOG.csv                # 블로그 검색 결과
│       ├── BUY_LIST.csv            # 구매 목록
│       ├── SELL_LIST.csv           # 판매 목록
│       ├── DEAL_LIST.csv           # 거래 내역
│       └── RELEASE_PRICE.csv       # 발매가 정보
│
├── models/                         # 학습된 모델
│   ├── random_forest_model.pkl
│   └── scaler.pkl
│
├── README.md                       # 프로젝트 문서
├── requirements.txt                # 패키지 목록
├── config.example.py               # 설정 파일 예시
└── .gitignore                      # Git 제외 파일 목록
```

## 시작하기

### 환경 요구사항
- Python 3.7 이상
- Chrome 브라우저 (Selenium 기반)
- Naver API Key (블로그 검색 및 감정 분석용)

### 설치 방법

#### 1. 저장소 클론
```bash
git clone <repository-url>
cd kream_project
```

#### 2️. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 3️. 패키지 설치
```bash
pip install -r requirements.txt
```

#### 4️. 설정 파일 생성 및 API 키 등록
```bash
cp config.example.py config.py
# config.py 내부에 API 키 및 로그인 정보 입력
```


### 사용 방법

#### 1. 데이터 수집
```python
# notebooks/crawling.ipynb  → KREAM 거래 데이터 수집
# notebooks/blog.ipynb      → 블로그 검색 데이터 수집
# notebooks/social_media_mentions.ipynb → 감정 분석 수행
```

#### 2. 모델 학습
```python
# notebooks/model_train.ipynb 실행
# 최적 모델이 자동 선택되어 models/ 디렉터리에 저장됩니다.
```

#### 3. 가격 예측
```python
# notebooks/kream_stock_predict.ipynb 실행
# 모델명을 입력하면 향후 예상 리셀 가격을 출력합니다.
```

## 데이터 특성

### 주요 피처 (Features)
- `total`: 블로그 검색 결과 개수
- `b_price`: 평균 구매가
- `s_price`: 평균 판매가
- `release_price`: 발매가
- `price_ratio`: 판매가 / 구매가 비율
- `year`, `month`, `day`, `dayofweek`: 날짜 특성

### 타깃 변수 (Target)
- `log_price`: 거래 가격의 로그 변환값 (`np.log1p(price)`)

## 모델 성능

| 모델 | MAE | MSE | 특징 |
|------|-----|-----|------|
| Random Forest | **0.047** | **0.008** | 가장 높은 예측 정확도 |
| Gradient Boosting | 0.094 | 0.017 | 두 번째로 우수한 성능 |
| Ridge | 0.287 | 0.132 | 단순 회귀 모델 |
| Lasso | 0.567 | 0.539 | 과적합 발생 |

RandomForest Regressor는 평균 절대 오차(MAE)가 0.047로, 실제 거래가 대비 약 4.7% 이내 오차 수준의 정확도를 보였습니다.
이는 리셀가 예측 모델로서 충분한 실효성을 갖춘 결과입니다.

## 주요 작업 내용

### 데이터 수집 파이프라인
- Selenium과 BeautifulSoup을 활용한 KREAM 웹 크롤링 자동화
- Naver API 기반 블로그 데이터 및 감정 점수 수집

### 데이터 전처리 및 피처 엔지니어링
- 결측치 처리 (30% 이상 결측 컬럼 제거, 평균값으로 대체)
- 로그 변환으로 데이터 정규화 (log_price)
- 파생 피처(price_ratio, dayofweek) 생성

### 모델 학습 및 검증
- Ridge, Lasso, Gradient Boosting, RandomForest 비교 실험
- 테스트 데이터 기반 성능평가 (MAE, MSE) 후 최적 모델 선정
- joblib을 통한 모델 저장 및 재사용

### 예측 시스템
- 학습된 모델을 활용한 스니커즈 가격 예측 모듈 구현
- 특정 모델명 입력 시 향후 예상 거래가 출력

## API 키 및 보안

API 키는 `config.py`를 통해 별도 관리합니다.

필요한 주요 키:
- **Naver Developers**: 블로그 검색 API
- **Naver Cloud Platform**: 감정 분석 API
- **KREAM 로그인 정보**(선택): 크롤링 시 사용

## 향후 개선 방향

- [ ] 실시간 데이터 업데이트 파이프라인 구축
- [ ] 딥러닝 모델(LSTM, Transformer) 적용
- [ ] Flask + Chart.js 기반 웹 대시보드 구현
- [ ] 추가 특성(브랜드, 카테고리, 협업 등) 도입
- [ ] 하이퍼파라미터 튜닝을 통한 모델 고도화

## 주의사항

- **API 키**: 네이버 API 키는 환경 변수나 설정 파일로 관리하세요
- **크롤링**: 웹 크롤링 시 KREAM의 이용약관을 준수하세요
- **데이터**: 실제 거래 데이터 사용 시 개인정보 보호에 주의하세요

## 라이선스

본 프로젝트는 교육 및 연구 목적으로 제작되었습니다.

## 작성자

프로젝트 개발자 (Data Collection, Modeling, Report 작성)

## 감사의 말

- KREAM 플랫폼
- Naver API
- 오픈소스 커뮤니티
