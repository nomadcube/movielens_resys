# coding=utf-8
import numpy as np

from scipy.sparse import csr_matrix


def cosine_similarity(rating_matrix, user_based=True):
    """
    由M*N评分矩阵计算得到物品相似度矩阵（N*N）或用户相似度矩阵（M*M）

    :param rating_matrix: csr_matrix, 评分矩阵
    :param user_based: bool, 为True时计算的是用户相似度矩阵，否则是物品相似度矩阵
    :return: csr_matrix, 相似度矩阵
    """
    rating_matrix = rating_matrix.transpose() if user_based is False else rating_matrix
    inner_product = rating_matrix * rating_matrix.transpose().todense()
    row_mode = row_mod(rating_matrix)
    mod_product = row_mode * row_mode.transpose().todense()
    inner_product /= mod_product
    return csr_matrix(inner_product)


def row_mod(mat):
    """
    计算矩阵各行向量的模

    :param mat: csr_matrix, M*N 大小
    :return: csr_matrix, M*1 大小
    """
    mat.data = np.power(mat.data, 2.0)
    return csr_matrix(np.power(mat.sum(axis=1), 0.5))


if __name__ == '__main__':
    from read import read_ratings
    rating_mat = read_ratings("/Users/wumengling/PycharmProjects/movielens_resys/data/small_train_ratings.dat")
    print cosine_similarity(rating_mat, False)
