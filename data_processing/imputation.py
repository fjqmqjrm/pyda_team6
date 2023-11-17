# 결측치 채우기

# 결측치 대체(최빈값) 함수
def fill_missing_with_mode(df):
    """
    DataFrame의 결측치를 최빈값으로 대체하는 함수

    Parameters:
    - df: pandas DataFrame
        결측치를 대체할 DataFrame

    Returns:
    - filled_df: pandas DataFrame
        결측치가 최빈값으로 대체된 DataFrame
    """
    filled_df = df.copy()
    for col in filled_df.columns:
        mode_value = filled_df[col].mode().iloc[0]  # 최빈값 계산
        filled_df[col].fillna(mode_value, inplace=True)  # 결측치를 최빈값으로 대체

    return filled_df


