# Heart Disease Prediction

- **초기 프로젝트**
    - 데이터: 2021 BRFSS Data (SAS Transport Format), https://www.cdc.gov/brfss/annual_data/annual_2021.html
    - 기술 스택: Python, jupyter notebook
    - 협업: Slack, Github
    - 일정: 2023.10.23 - 2023.11.22 (1개월)
    - 인원: 3명
>
- **1차 보완**
    - 일정: 2024.03.23 - 2024.4.23 (1개월)
    - 인원: 1명
    - 목적: 논문 작성 및 모델 성능 지표 향상
>
- **2차 보완**
    - 일정: 2024.07.12 - 2024.7.17 (1주일)
    - 인원: 1명
    - 목적: 모델 성능 지표 향상
>
---

## 1. 프로젝트 배경
1. 전화 설문 빅데이터를 기반으로 개인의 심장질환 발병 위험을 예측할 수 있는 모델의 부재
2. 전통적인 심장질환 진단 방법의 한계

## 2. EDA
- 전체 데이터셋(438,693)과 독립변수 선정 및 결측치 제거 후의 데이터셋(236,378개) 모두에서 심장질환 양성 사례가 8%, 심장질환 음성 사례가 92%를 차지하는 매우 불균형한 데이터
## 3. Feature Engineering
1. `독립변수 선정`: 선행 연구를 기반으로, 304개의 컬럼 중 심장질환과 연관성 있는 21개의 독립변수 선택
2. `결측치 제거`: ‘응답 없음', ‘모름' 제거
3. 성능의 개선이 없어, scaler 적용 및 outlier 제거는 진행하지 않음. 
4. `Resampling`: 클래스 불균형에 따른 모델 성능 저하 방지를 위해, 8가지의 서로 다른 Resampling 기법 사용

## 4. 모델 설계
### 4-1. Baseline Model
- 질병 진단 모델이므로 recall이 가장 높은 모델을 선택하고자 했으나, 해당 모델의 다른 수치들이 전체 모델 평균에 비해 매우 떨어지는 문제 발생(그림: Recall이 0.95 이상인 모델의 평가지표)
![그림1](https://github.com/user-attachments/assets/c85d8701-fa22-45a4-af94-210f28ed656e)
- 따라서 최소 기준을 선정하여, Recall 이 0.8 이상이면서 Precision 이 0.2 이상인 모델 선별 후,
- Recall 이 높은 Logistic Regression 모델, 나머지 수치가 모두 높은 LightGBM 모델을 두 최종 모델로 선정
![그림2](https://github.com/user-attachments/assets/05fa0f82-7c7d-4b49-bc09-b01e0d4ba289)
#### Baseline Model 평가 및 분석

| ![Alt text 1](https://github.com/user-attachments/assets/0f3541e5-c65c-40eb-8608-400c38e94104) | ![Alt text 2](https://github.com/user-attachments/assets/7574b01a-f157-4e14-b17b-8dd4312d4f49) | ![Alt text 3](https://github.com/user-attachments/assets/2d626108-a525-459f-b65d-260b1548b722) |
|---------------------|---------------------|---------------------|
| SHAP summary plot       | 오분류 분석 (정답, 오답)              | 오분류 분석 (FP, FN)         |



