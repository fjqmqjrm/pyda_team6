import pandas as pd

# 가해운전자 차종이 PM인 경우의 데이터를 추출
def perpetrator_PM(df):
    perpetrator_PM_df = df[df['가해운전자 차종'] == '개인형이동수단(PM)']
    return perpetrator_PM_df

# 각각 법규 위반 형태의 빈도 분석
def freq_violation(df):
    freq_violation_df = df['법규위반'].value_counts()
    return freq_violation_df

# 발생월별 빈도 분석
def monthly_count(df):
    # "사고일시" 컬럼을 datetime 형식으로 변환
    df['사고일시'] = pd.to_datetime(df['사고일시'], format='%Y년 %m월 %d일 %H시')
    # 월별 빈도 분석
    monthly_count_df = df['사고일시'].dt.month.value_counts().sort_index()
    return monthly_count_df

# 교통사고량이 급격히 증가하는 4월, 7월의 행정구역 빈도 분석
def district_count(df):
    # "사고일시" 컬럼을 datetime 형식으로 변환
    df['사고일시'] = pd.to_datetime(df['사고일시'], format='%Y년 %m월 %d일 %H시')
    # 4월, 7월만 추출한 후, 행정구역 빈도 분석
    district_count_df = df[(df['사고일시'].dt.month == 4) | (df['사고일시'].dt.month == 7)]
    df['동'] = df['시군구'].str[-4:]
    district_count_df = df['동'].value_counts()
    return district_count_df