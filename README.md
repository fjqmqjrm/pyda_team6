# pyda_team6 
    파이썬을 이용한 데이터사이언스 캡스톤디자인 연계실습 6조의 레포지토리입니다.
## 발전정도 
### 1. 중상사고 분석
        목적 :  데이터 상에서 가장 큰 상해정도인 ‘중상’ 사고자가 발생한 사건을 분석하여 PM사고의 상해를 줄이기 위한 지표를 확보하고 시각화한다.
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
### 4. 교통사고 발생 월별, 행정구역별 빈도 분석
        목적 :  법규 위반 단속에 투입되는 인력을 효율적으로 배치하기 위해 일년 중 가장 많이 발생하는 시기와 그 시기의 행정구역에 대해 조사하고자 한다.
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
### 커밋 컨벤션

- feat : 새로운 기능 추가
- fix : 버그 수정
- docs : 문서 수정
- style : 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
- refactor : 코드 리펙토링
- test : 테스트 코드, 리펙토링 테스트 코드 추가
- chore : 빌드 업무 수정, 패키지 매니저 수정


