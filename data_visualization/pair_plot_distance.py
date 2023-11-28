import seaborn as sns
import matplotlib.pyplot as plt
def plot_pair_plot(df):
    # Pair plot 그리기
    sns.set(style="ticks")
    sns.pairplot(df, hue="Cluster", markers=["o", "s", "D"])

    # 그래프 출력
    plt.show()