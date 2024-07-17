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
- 질병 진단 모델이므로 recall이 가장 높은 모델을 선택하고자 했으나, 해당 모델의 다른 수치들이 전체 모델 평균에 비해 매우 떨어지는 문제 발생 (그림: Recall이 0.95 이상인 모델의 평가지표)
![그림1](https://github.com/user-attachments/assets/c85d8701-fa22-45a4-af94-210f28ed656e)
- 따라서 최소 기준을 선정하여, Recall 이 0.8 이상이면서 Precision 이 0.2 이상인 모델 선별 후,
- Recall 이 높은 Logistic Regression 모델, 나머지 수치가 모두 높은 LightGBM 모델을 두 최종 모델로 선정
![그림2](https://github.com/user-attachments/assets/05fa0f82-7c7d-4b49-bc09-b01e0d4ba289)
#### Baseline Model 평가 및 분석

| ![Alt text 1](https://github.com/user-attachments/assets/0f3541e5-c65c-40eb-8608-400c38e94104) | ![Alt text 2](https://github.com/user-attachments/assets/7574b01a-f157-4e14-b17b-8dd4312d4f49) | ![Alt text 3](https://github.com/user-attachments/assets/2d626108-a525-459f-b65d-260b1548b722) |
|---------------------|---------------------|---------------------|
| SHAP summary plot       | 오분류 분석 (정답, 오답)              | 오분류 분석 (FP, FN)         |

- 결과 분석

    - 연령 변수가 모델의 예측에 매우 큰 영향을 미친다.
    - 데이터의 연령이 높을수록 모델의 정확도가 감소한며, 이는 주로 가짜 양성(False Positive)이 원인이다. 
    - 따라서, 모델의 성능 지표를 향상시키기 위해 연령 편향 완화를 시도해 볼 가치가 있다.

### 4-2. Advanced Model
- AIF360 reweighing 알고리즘을 적용하여, 연령 편향을 완화하는 공정성 모델(Fair Model) 구축
- Fair model 에서 고연령대의 정확도가 미세하게 향상
- 이는 모델의 연령 편향 문제에 대한 초기 접근이 일부 효과를 보였음을 시사
      <img src="https://github.com/user-attachments/assets/a852fd2b-325d-49dc-ab8d-98a3c44a246a" alt="설명" width="500"/>
### 4-3. More Advanced Model
- StratifiedShuffleSplit 기법을 적용하여, 모델이 특정 연령대에 과적합되거나 편향되는 것을 방지한다.
- Hyper Parameter 최적화를 통해 성능을 향상시킨다.

| ![최종성능](https://github.com/user-attachments/assets/3b9bfbdb-7cd5-4df9-81e3-88c09598f900) | ![다운로드 (4)](https://github.com/user-attachments/assets/f2c07888-4aaf-43f4-aade-0be124d07d34) | ![x](https://github.com/user-attachments/assets/68b9ad95-2bd1-4644-ae48-dd811c9c59a2)|
|---------------------|---------------------|---------------------|
| 최종 성능       |     ROC Curve          |     고연령대 정확도 상승    |
