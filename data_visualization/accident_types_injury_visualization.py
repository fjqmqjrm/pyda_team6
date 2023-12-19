import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 사용자 환경에 맞게 폰트 경로 설정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def draw_stacked_bar_chart(df, category_col, title):

    # 누적형 막대그래프 그리기
    ax = df.plot(x=category_col, kind='bar', stacked=True, title=title)

    # 그래프의 레이아웃 및 X 축 라벨 조정
    plt.xticks(range(len(df[category_col])), df[category_col])
    ax.set_xticklabels(df[category_col], rotation=0, ha='right')
    ax.set_xlabel(category_col)
    ax.set_ylabel('injuries')

    ax.legend().set_visible(True)

    # 그래프의 레이아웃 조정
    plt.tight_layout()

    # 그래프 표시
    plt.show()