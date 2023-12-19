# pyda_team6 
    파이썬을 이용한 데이터사이언스 캡스톤디자인 연계실습 6조의 레포지토리입니다.
## 깃 이슈 
    깃 이슈를 통해 각자 맡은 파트의 진행상황과 커밋메세지 이슈번호 부여로 코드 관리를 하였습니다.
## 디렉터리
    resource : 사용하고자 하는 데이터
    data_processing : 데이터 처리 및 로드
    data_analysis : 분석 목적에 따른 데이터 분석
    data_visualization : 분석 결과 시각화
    run : 위의 디렉터리의 관련 함수를 불러와 실제 실행되는 코드 
## 데이터사이언스캡스톤디자인1 결과물

    목표 : 공공안전문제 해결방안 마련
    주제 : 개인형이동장치(PM) 교통사고량 증가 원인 분석
    
    1. 데이터수집 (TAAS(교통사고분석시스템) - PM 교통사고 데이터)
    2. 데이터탐색 (통계 분석 및 시각화) - 상황적 변수 / 지역적 변수를 나누어서 진행
       상황적 변수 : 운전자 연령/성별, 사고시간대, 발생월, 요일, 발생동, 기상상태, 도로형태, 사망/중상/경상/부상자수, 법규위반형태
       지역적 변수 : 발생지점에서 0~2km, 2~3km 거리 내에 있는 지하철역
## 발전정도 
    캡스톤 디자인 당시 데이터 확보와 전처리까지 진행하였으며 당시 정리했던 데이터를 기반으로 파이데 수업시간에 배운 pandas,matplotlib,apyori,scikit-learn,seaborn 라이브러리들을 활용하여 아래 분석들을 진행하였습니다. 
### 1. 중상사고 분석
        목적 :  데이터 상에서 가장 큰 상해정도인 ‘중상’ 사고자가 발생한 사건을 분석하여 PM사고의 상해를 줄이기 위한 지표를 확보하고 시각화한다.
        사용한 라이브러리 : pandas,matplotlib
### 중상사고 분석 - 관련 파일 
```css
📂 pyda_team6 
    │
    ├─ 📂 data_visualization 
    │  └─ serious_injury_accident_visualization.py
    │
    ├─ 📂 data_analysis
    │  └─ erious_injury_accident.py 
    │
    ├─ 📂 data_processing 
    │  └─ data_load.py
    │
    ├─ 📂 resource 
    │  └─ Integrated_damage_data.xlsx    
    │
    └─ 📂 run
       └─ injury_analyze.py
```
### 2. 사고유형별 분석
        목적 :  차대차, 차대사람, 차량단독 이 세가지로 나누어서 나이대별 사고 빈도를 분석하여 사고유형별로 어떤 나이대에서 사고 빈도수가 높은지를 파악하고 시각화한다.
        사용한 라이브러리 : pandas,matplotlib
### 사고유형별 분석 - 관련 파일 
```css
📂 pyda_team6 
    │
    ├─ 📂 data_visualization
    │  └─ accident_type.py
    │  
    ├─ 📂 data_analysis
    │  └─ accident_type.py 
    │
    ├─ 📂 data_processing 
    │  └─ data_load.py
    │
    ├─ 📂 resource 
    │  └─ Integrated_damage_data.xlsx    
    │
    └─ 📂 run
       └─ accident_type_age_analyze.py
```
### 3. 가해 운전자 차종이 PM인 데이터에서 법규위반 상위 3가지 분석
        목적 :  시민들의 안전한 개인형이동장치 이용을 위해 법규 위반 단속 및 규정 강화를 실시하고자 한다. 이를 위해 교통사고 발생률을 높이는 PM이용자의 법규 위반 사안들에 대해 조사한다.
        사용한 라이브러리 : pandas, apyori, matplotlib
### 가해 운전자 차종이 PM인 데이터에서 법규위반 상위 3가지 분석 - 관련 파일 
```css
📂 pyda_team6 
    │
    ├─ 📂 data_visualization
    │  └─ trafficlaw_violation__visualization.py
    │
    ├─ 📂 data_analysis
    │  └─ trafficlaw_violation_analysis.py 
    │
    ├─ 📂 data_processing 
    │  └─ data_load.py
    │
    ├─ 📂 resource 
    │  └─ Integrated_damage_data.xlsx    
    │
    └─ 📂 run
       └─ trafficlaw_violation_run.py
```
### 3-(2). 교통사고 발생 월별, 행정구역별 빈도 분석
        목적 :  법규 위반 단속에 투입되는 인력을 효율적으로 배치하기 위해 일년 중 가장 많이 발생하는 시기와 그 시기의 행정구역에 대해 조사하고자 한다.
        사용한 라이브러리 : pandas, apyori, matplotlib
### 교통사고 발생 월별, 행정구역별 빈도 분석 - 관련 파일 
```css
📂 pyda_team6 
    │
    ├─ 📂 data_visualization
    │  └─ trafficlaw_violation__visualization.py
    │
    ├─ 📂 data_analysis
    │  └─ trafficlaw_violation_analysis.py 
    │
    ├─ 📂 data_processing 
    │  └─ data_load.py
    │
    ├─ 📂 resource 
    │  └─ Integrated_damage_data.xlsx    
    │
    └─ 📂 run
       └─ trafficlaw_violation_run.py
```
### 4. 강남구 지하철 역 근처 PM 교통사고 건수에 따른 분석 보고
     목적 
     : 서울 지하철 역 주변의 교통사고 건수와 역과의 거리 간의 관계를 조사하고, 교통사고와 지역 특성의 상관 관계를 확인하는 것이다. 이를 통해 캡스톤디자인2에서 교통 안전성과 지하철 역 주변 환경의 특성을 연관 짓고자 힌디.
     사용한 라이브러리 : pandas,scikit-learn,matplotlib,seaborn

### 강남구 지하철 역 근처 PM 교통사고 건수에 따른 분석 보고 - 관련 파일 
```css
📂 pyda_team6 
    │
    ├─ 📂 data_visualization
    │  └─ pair_plot_distance.py
    │
    ├─ 📂 data_analysis
    │  └─ kmeans_clustering_distance.py 
    │
    ├─ 📂 data_processing 
    │  └─ data_load.py
    │
    ├─ 📂 resource 
    │  └─ number_distance.xlsx    
    │
    └─ 📂 run
       └─ distance_clustering_run.py
```
### 커밋 컨벤션
커밋 상황에 대한 빠른 식별을 위해 커밋 컨벤션을 통일하였습니다.
- feat : 새로운 기능 추가
- fix : 버그 수정
- docs : 문서 수정
- style : 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
- refactor : 코드 리펙토링
- test : 테스트 코드, 리펙토링 테스트 코드 추가
- chore : 빌드 업무 수정, 패키지 매니저 수정

