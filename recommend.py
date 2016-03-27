# coding=utf-8
from scipy.sparse import csr_matrix


def item_based_recommend(rating_matrix, similarity_matrix):
    """
    已知待推荐用户的评分列表，通过物品相似度矩阵计算推荐结果

    :param rating_matrix: M*N csr_matrix, 评分矩阵
    :param similarity_matrix: N*N csr_matrix, 物品相似度矩阵
    :return: csr_matrix, M*N 预测评分矩阵
    """
    return rating_matrix * similarity_matrix


if __name__ == '__main__':
    from read import read
    from similarity_matrix import cosine_similarity
    rating_mat = read("/Users/wumengling/PycharmProjects/movielens_resys/data/small_train_ratings.dat")
    item_simi = cosine_similarity(rating_mat, False)
    test_rating = read("/Users/wumengling/PycharmProjects/movielens_resys/data/small_test_ratings.dat")
    print item_based_recommend(test_rating, item_simi).shape
