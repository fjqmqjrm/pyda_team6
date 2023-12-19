# 데이터 불러오기
from pyda_team6.data_analysis.accident_types_injury import injury_degree_count
from pyda_team6.data_processing.data_load import data_load
from pyda_team6.data_visualization.accident_types_injury_visualization import draw_stacked_bar_chart

full_data = data_load()

# 사고 유형별 상해정도별 상해자 수 데이터프레임 생성
car_to_car_df = injury_degree_count(full_data, '차대차')
car_to_person_df = injury_degree_count(full_data, '차대사람')

# 차대차 사고 상해정도별 상해자 수 시각화
draw_stacked_bar_chart(car_to_car_df, "상해정도", "Car to car accident injury count")
# 차대사람 사고 상해정도별 상해자 수 시각화
draw_stacked_bar_chart(car_to_car_df, "상해정도", "Car to person accident injury count")