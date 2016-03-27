# coding=utf-8
def weighted_recommend(n_predicts_ratings, weights):
    """
    对于n个推荐算法得出的预测评分，用权重进行加权混合

    :param n_predicts_ratings:list, 元素为matrix, 对应各个推荐算法的预测评分矩阵
    :param weights: array, 各个推荐算法的权重估计值和截距值
    :return: matrix, 加权混合后的推荐结果
    """
    mixed_predict = n_predicts_ratings[0]
    for predict_no, predict_mat in enumerate(n_predicts_ratings[1:]):
        mixed_predict += weights[predict_no] * predict_mat
    return mixed_predict
