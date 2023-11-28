from pyda_team6.data_analysis.kmeans_clustering_distance import kmeans_clustering
from pyda_team6.data_processing.data_load import data_load_distance
from pyda_team6.data_visualization.pair_plot_distance import plot_pair_plot
import warnings

# 경고 메시지 무시
warnings.filterwarnings("ignore", category=FutureWarning)

# 데이터 불러오기
df = data_load_distance()
# KMeans 클러스터링
df = kmeans_clustering(df)

# Pair plot 그리기
plot_pair_plot(df)

