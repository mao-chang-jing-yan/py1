from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_digits


def kmeans():
    """
    手写数字聚类过程
    :return: None
    """
    ld = load_digits()
    print(ld.target[:20])

    # 进行聚类
    km = KMeans(n_clusters=8)
    km.fit_transform(ld.data)
    print(km.labels_[:20])
    print('轮廓系数为：', silhouette_score(ld.data, km.labels_))

    return None


if __name__ == "__main__":
    kmeans()
