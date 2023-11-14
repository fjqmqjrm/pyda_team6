# 데이터 불러오기
import pandas as pd
# 사용할 메인 데이터(Integrated_damage_data.xlsx를 불러오는 함수)
def data_load():
    # Integrated_damage_data.xlsx 파일을 dataframe으로 변경
    df = pd.read_excel("../resource/Integrated_damage_data.xlsx", engine="openpyxl")
    return df

