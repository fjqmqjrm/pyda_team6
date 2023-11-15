# 중상사고 분석
from pyda_team6.data_processing.data_load import data_load, extract_violation_for_serious_injury

"""중상자가 발생한 사고의 법규 위반 별 중상사고 건수를 나타내는 데이터프레임을 생성하는 함수
    파라미터 - df: pandas DataFrame (전체 데이터가 담긴 데이터프레임)
    리턴 - injury_count_by_violation: pandas DataFrame(법규위반 별 중상사고 건수를 나타내는 데이터프레임) -> 컬럼: '법규위반', '중상사고건수'"""
def create_injury_count_by_violation_df(df):
    # 중상자가 발생한 사고의 경우, 법규 위반 형태를 추출
    violation_series = extract_violation_for_serious_injury(df)

    # 법규위반 별 중상사고 건수를 계산하고 데이터프레임으로 변환
    injury_count_by_violation = violation_series.value_counts().reset_index()

    # 컬럼명을 '법규위반', '중상사고건수'로 변경
    injury_count_by_violation.columns = ['법규위반', '중상사고건수']

    return injury_count_by_violation


