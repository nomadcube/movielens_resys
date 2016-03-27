# coding=utf-8
import numpy as np

from sklearn.linear_model import LinearRegression


def estimated_weights(x, y):
    """
    用线性回归估计推荐结果加权混合的权重值
    相当于求使得加权后的预测评分和真实评分的mae最小的权重解

    :param x: M*N matrix, 各个推荐算法得出的预测评分值，M为(user-item)对的数目，N为推荐算法个数
    :param y: M*1 array, (user-item)对的真实评分值
    :return: (N+1)*1 array, 各个推荐算法的估计权重值及intercept.
    """
    lm = LinearRegression()
    lm.fit(x, y)
    return lm.coef_

