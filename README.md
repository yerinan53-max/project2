# 법률 문서 임베딩 기반 유사 판례 검색

Sentence-BERT 임베딩과 코사인 유사도를 활용해 사용자가 입력한 사건 내용과 의미적으로 유사한 판례를 검색하는 딥러닝 프로젝트입니다.

## 주요 기능

- 법률 문서 텍스트 전처리
- Sentence-BERT 기반 문서 임베딩 생성
- 코사인 유사도 기반 Top-K 유사 판례 검색
- 검색 결과의 공통 쟁점 키워드와 분야 분포 시각화
- Jupyter Notebook 기반 학습 및 성능 비교 실험

## 데이터 안내

실험 및 모델 학습에는 AI Hub 법률 데이터가 사용되었습니다. 다만 AI Hub 데이터 이용 조건을 준수하기 위해 아래 파일은 저장소에 포함하지 않습니다.

- AI Hub 원본 데이터
- 전처리된 CSV 데이터
- 학습된 모델 파일
- 임베딩 인덱스 파일

공개 저장소에는 기능 확인을 위한 합성 샘플 데이터만 포함합니다.

## 실행 방법

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## 프로젝트 구조

```text
.
├─ app.py
├─ data/
│  └─ sample_cases.csv
├─ notebooks/
│  └─ train_embedding_model.ipynb
├─ src/
│  ├─ analysis.py
│  ├─ config.py
│  ├─ data.py
│  ├─ embedding.py
│  └─ search.py
├─ tests/
└─ requirements.txt
```

## 예시 질의

```text
지나가는 행인을 폭행함
중고차를 무사고 차량이라고 해서 구매했는데 사고 이력이 발견되었다
전세 보증금을 집주인이 돌려주지 않는다
```
