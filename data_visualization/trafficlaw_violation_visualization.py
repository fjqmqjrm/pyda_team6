import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 사용자 환경에 맞게 폰트 경로 설정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# <3-1> 가장 많이 발생한 상위 3위 법규 위반 형태 시각화
def top3_violations_byPM(df):
    top3 = df.head(3)
    plt.figure(figsize=(10, 6))
    plt.bar(top3.index, top3.values, color='pink')
    plt.xlabel('법규위반 형태')
    plt.ylabel('빈도수')
    plt.title('교통사고 발생률을 높이는 PM 운전자의 교통법규위반 Top3')
    plt.show()

# 발생월별 빈도 분석 시각화
def monthly_count_visualization(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df.index, df.values, color='skyblue')
    plt.xlabel('발생월')
    plt.ylabel('교통사고 발생 건수')
    plt.title('발생월별 빈도 분석')
    plt.show()

# <3-2> 4월, 7월의 교통사고량 상위 3위 행정구역 시각화
def district_count_visualization(df):
    top3 = df.head(3)
    plt.figure(figsize=(10, 6))
    plt.bar(top3.index, top3.values, color='gray')
    plt.xlabel('발생동')
    plt.ylabel('교통사고 발생 건수')
    plt.title('4월, 7월의 행정구역 빈도 분석')
    plt.show()