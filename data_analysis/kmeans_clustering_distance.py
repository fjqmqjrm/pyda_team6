import seaborn as sns
from sklearn.cluster import KMeans


def kmeans_clustering(df):
    # KMeans 클러스터링을 수행하는 함수
    # '0~2(km)', '2~3(km)' 열을 사용하여 클러스터링을 진행

    # KMeans 모델 생성 및 학습 k=3
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df[['0~2(km)', '2~3(km)']])

    # 클러스터링 결과 출력
    print("클러스터링 결과:")
    print(df[['역', 'Cluster']])

    return df