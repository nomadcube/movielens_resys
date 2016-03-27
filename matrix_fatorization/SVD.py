# coding=utf-8
from scipy.sparse import linalg
from collabrate_filtering.recommend import recommend


def singular_value_decomposition(mat, k):
    """
    对稀疏矩阵进行奇异值分解

    :param mat: csr_matrix
    :param k: int, 特征值个数
    :return: [csr_matrix, csr_matrix, csr_matrix], 即svd分解出来的3个低秩矩阵
    """
    return linalg.svds(mat, k=k)


def svd_recommend(mat, k):
    """
    SVD推荐算法
    用SVD将评分矩阵分解并取前k个特征值，分解后的3个低秩矩阵相乘得到估计评分矩阵，再计算推荐结果

    :param mat: csr_matrix, 评分矩阵
    :param k: int, 特征值个数
    :return: dict, 用户为key, 对应的推荐结果为value
    """
    u, s, v = singular_value_decomposition(mat, k)
    predict_ratings = u * s * v
    return recommend(predict_ratings)


if __name__ == '__main__':
    from read import read_ratings

    rating_mat = read_ratings("/Users/wumengling/PycharmProjects/movielens_resys/data/small_train_ratings.dat")
    print singular_value_decomposition(rating_mat, 2)

    print svd_recommend(rating_mat, 2)