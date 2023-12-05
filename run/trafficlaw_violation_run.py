# 코드 불러오기
from pyda_team6.data_processing.data_load import data_load
from pyda_team6.data_analysis.trafficlaw_violation_analysis import perpetrator_PM, freq_violation, monthly_count, district_count
from pyda_team6.data_visualization.trafficlaw_violation_visualization import top3_violations_byPM, monthly_count_visualization, district_count_visualization

# 데이터 불러오기
df = data_load()

# 가해운전자 차종이 PM인 경우의 데이터를 추출
df = perpetrator_PM(df)

# 각각 법규 위반 형태의 빈도 분석
df1 = freq_violation(df)

# 가장 많이 발생한 상위 3위 법규 위반 형태 시각화
top3_violations_byPM(df1)

# 발생월별 빈도 분석 및 시각화
df2 = monthly_count(df)
monthly_count_visualization(df2)

# 교통사고량이 급격히 증가하는 4월, 7월의 행정구역 빈도 분석
df3 = district_count(df)
# 4월, 7월의 교통사고량 상위 3위 행정구역 시각화
district_count_visualization(df3)