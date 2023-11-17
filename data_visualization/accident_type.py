import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 사용자 환경에 맞게 폰트 경로 설정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


def plot_age_frequency(age_frequency_df, accident_type):
    """
    연령대별 빈도수를 시각화하는 함수

    Parameters:
    - age_frequency_df: pandas DataFrame
        연령대별 빈도수를 담은 데이터프레임
    - accident_type: str
        사고 유형 이름 (차대차, 차대사람, 차량단독 등)
    """
    plt.figure(figsize=(10, 6))
    plt.bar(age_frequency_df['연령대'], age_frequency_df['빈도수'], color='skyblue')
    plt.title(f'{accident_type} 사고 연령대별 빈도수')
    plt.xlabel('연령대')
    plt.ylabel('빈도수')
    plt.show()