# coding=utf-8
import numpy as np


def predict_ratings(rating_matrix, similarity_matrix):
    """
    已知待推荐用户的评分列表，通过物品相似度矩阵计算推荐结果

    :param rating_matrix: M*N csr_matrix, 评分矩阵
    :param similarity_matrix: N*N csr_matrix, 物品相似度矩阵
    :return: csr_matrix, M*N 预测评分矩阵
    """
    return rating_matrix * similarity_matrix


def recommend(predict_mat):
    """
    根据预测评分矩阵计算各个用户的k个推荐结果

    :param predict_mat: csr_matrix, 预测评分矩阵
    :return: array， 各个用户的推荐结果
    """
    result = dict()
    for user_id, each_prediction in enumerate(predict_mat):
        if each_prediction.nnz > 0:
            result[user_id] = np.argmax(each_prediction)
    return result


if __name__ == '__main__':
    from read import read
    from similarity_matrix import cosine_similarity
    rating_mat = read("/Users/wumengling/PycharmProjects/movielens_resys/data/small_train_ratings.dat")
    item_simi = cosine_similarity(rating_mat, False)
    test_rating = read("/Users/wumengling/PycharmProjects/movielens_resys/data/small_test_ratings.dat")
    pred_mat = predict_ratings(test_rating, item_simi)
    print recommend(pred_mat)
