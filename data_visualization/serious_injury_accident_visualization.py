import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 사용자 환경에 맞게 폰트 경로 설정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


def plot_horizontal_bar_chart(dataframe, x_column, y_column, title, xlabel, ylabel, color='skyblue', figsize=(10, 6)):
    """
    수평 막대 그래프를 생성하는 함수

    Parameters:
    - dataframe: pandas DataFrame
        시각화할 데이터프레임
    - x_column: str
        x 축으로 사용할 열 이름
    - y_column: str
        y 축으로 사용할 열 이름
    - title: str
        그래프 제목
    - xlabel: str
        x 축 라벨
    - ylabel: str
        y 축 라벨
    - color: str, optional (default='skyblue')
        막대 색상
    - figsize: tuple, optional (default=(10, 6))
        그래프 크기
    """
    # 그래프 크기 설정
    plt.figure(figsize=figsize)

    # 수평 막대 그래프 생성
    plt.barh(dataframe[x_column], dataframe[y_column], color=color)

    # 그래프 제목 및 라벨 설정
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # 그리드 표시
    plt.grid(axis='x')

    # 그래프 출력
    plt.show()