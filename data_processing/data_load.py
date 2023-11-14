# 데이터 불러오기
import pandas as pd
# 사용할 메인 데이터(Integrated_damage_data.xlsx를 불러오는 함수)
def data_load():
    # Integrated_damage_data.xlsx 파일을 dataframe으로 변경
    df = pd.read_excel("../resource/Integrated_damage_data.xlsx", engine="openpyxl")
    return df

# 우리 데이터 상에서는 pm 사고로 인해 발생한 상해 정도 중 최고치가 '중상'
# 중상자가 발생한 사고의 경우 , 법규 위반 형태(중상자 0이 아닌 경우를 추출)


# 사고 유형에 따라 데이터 프레임 나누기(분류 기준 : 차대사람 , 차대차, 차량단독)

