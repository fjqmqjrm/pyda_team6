# 데이터 불러오기
from pyda_team6.data_analysis.accident_type import create_accident_type_df, calculate_age_frequency
from pyda_team6.data_processing.data_load import data_load
from pyda_team6.data_visualization.accident_type import plot_age_frequency

full_data = data_load()

# 각 사고 유형에 해당하는 데이터프레임 생성
car_to_car_df = create_accident_type_df(full_data, '차대차')
car_to_person_df = create_accident_type_df(full_data, '차대사람')
vehicle_alone_df = create_accident_type_df(full_data, '차량단독')

# 각 데이터프레임에서 연령대별 빈도수 계산
car_to_car_age_frequency = calculate_age_frequency(car_to_car_df)
car_to_person_age_frequency = calculate_age_frequency(car_to_person_df)
vehicle_alone_age_frequency = calculate_age_frequency(vehicle_alone_df)

# 결과 출력
print("차대차 사고 연령대별 빈도수:")
print(car_to_car_age_frequency)

# 차대차 사고 연령대별 빈도수 시각화
plot_age_frequency(car_to_car_age_frequency, '차대차')

# 차대사람 사고 연령대별 빈도수 시각화
plot_age_frequency(car_to_person_age_frequency, '차대사람')

# 차량단독 사고 연령대별 빈도수 시각화
plot_age_frequency(vehicle_alone_age_frequency, '차량단독')