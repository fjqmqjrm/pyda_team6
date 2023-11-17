from pyda_team6.data_analysis.serious_injury_accident import create_injury_count_by_violation_df
from pyda_team6.data_processing.data_load import data_load, extract_violation_for_serious_injury
from pyda_team6.data_visualization.serious_injury_accident_visualization import plot_horizontal_bar_chart

# 데이터 불러오기
full_data = data_load()

# 중상자가 발생한 사고의 경우, 법규 위반 형태 추출
violation_for_serious_injury = extract_violation_for_serious_injury(full_data)

# 법규위반 별 중상사고 건수 데이터프레임 생성
injury_count_df = create_injury_count_by_violation_df(full_data)

# 법규위반 형태별 빈도수 시각화
plot_horizontal_bar_chart(injury_count_df, '법규위반', '중상사고건수', '법규위반 별 중상사고 건수', '중상사고 건수', '법규위반')
