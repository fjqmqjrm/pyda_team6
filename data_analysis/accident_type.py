import pandas as pd
import warnings
from pandas.core.common import SettingWithCopyWarning

from pyda_team6.data_processing.data_load import data_load


def create_accident_type_df(df, accident_type_keyword):
    """
    특정 키워드를 포함하는 사고 유형에 해당하는 데이터프레임을 생성하는 함수

    Parameters:
    - df: pandas DataFrame
        전체 데이터가 담긴 데이터프레임
    - accident_type_keyword: str
        분석하고자 하는 사고 유형의 키워드

    Returns:
    - accident_type_df: pandas DataFrame
        특정 키워드를 포함하는 사고 유형에 해당하는 데이터프레임
    """
    # 주어진 사고 유형 키워드를 포함하는 행만 추출
    accident_type_df = df[df['사고유형'].str.contains(accident_type_keyword, case=False, na=False)].copy()
    return accident_type_df

def calculate_age_frequency(df):
    """
    주어진 데이터프레임에서 연령대별 빈도수를 계산하는 함수

    Parameters:
    - df: pandas DataFrame
        주어진 데이터프레임

    Returns:
    - age_frequency_df: pandas DataFrame
        연령대별 빈도수를 담은 데이터프레임
    """
    # '가해운전자 연령' 열에 값이 있는지 확인
    if df['가해운전자 연령'].notnull().any():
        # '미분류' 값을 제외하고 연령대 묶기
        df = df[df['가해운전자 연령'] != '미분류']
        df.loc[:, '연령대'] = df['가해운전자 연령'].astype(str).str[:1] + "0대"

        # null 값이 있는 행 제거
        df = df.dropna(subset=['연령대'])

        # 연령대별 빈도수 계산
        age_frequency = df['연령대'].value_counts().reset_index()
        age_frequency.columns = ['연령대', '빈도수']
        return age_frequency
    else:
        return None

warnings.filterwarnings("ignore", category=SettingWithCopyWarning)

