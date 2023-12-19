import pandas as pd

def injury_degree_count(df, accident_type):

    df_select = df[["사고유형", "가해운전자 차종", "가해운전자 상해정도", "피해운전자 차종", "피해운전자 상해정도"]]

    # 특정 열의 값에서 띄어쓰기 앞까지의 문자열 추출
    first_word_values = df_select["사고유형"].str.split().str[0]

    # 띄어쓰기 앞까지의 문자열이 target_word와 일치하는 행만 추출
    filtered_dataframe = df_select[first_word_values == accident_type]

    #PM사고자 추출
    df_pm1 = filtered_dataframe[filtered_dataframe["가해운전자 차종"] == "개인형이동수단(PM)"]
    df_pm2 = filtered_dataframe[filtered_dataframe["피해운전자 차종"] == "개인형이동수단(PM)"]

    df_pm1 = df_pm1[["가해운전자 차종", "가해운전자 상해정도"]]
    df_pm2 = df_pm2[["피해운전자 차종", "피해운전자 상해정도"]]

    df_pm1.columns = ['차종', '상해정도']
    df_pm2.columns = ['차종', '상해정도']

    final_df = pd.concat([df_pm1, df_pm2], ignore_index=True)

    count_result_1 = final_df["상해정도"].value_counts().reset_index()
    count_result_1.columns = ["상해정도", 'Count']

    # PM이 아닌 사고자 추출
    df_pm1 = filtered_dataframe[filtered_dataframe["가해운전자 차종"] != "개인형이동수단(PM)"]
    df_pm2 = filtered_dataframe[filtered_dataframe["피해운전자 차종"] != "개인형이동수단(PM)"]

    df_pm1 = df_pm1[["가해운전자 차종", "가해운전자 상해정도"]]
    df_pm2 = df_pm2[["피해운전자 차종", "피해운전자 상해정도"]]

    df_pm1.columns = ['차종', '상해정도']
    df_pm2.columns = ['차종', '상해정도']

    final_df = pd.concat([df_pm1, df_pm2], ignore_index=True)

    count_result_2 = final_df["상해정도"].value_counts().reset_index()
    count_result_2.columns = ["상해정도", 'Count']

    merged_df = pd.merge(count_result_1, count_result_2, on="상해정도", how='left', suffixes=('_df1', '_df2'))
    merged_df.columns = ["상해정도", "PM", "not PM"]

    return merged_df