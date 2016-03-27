# coding=utf-8
from scipy.sparse import coo_matrix
from array import array


def read(rating_file_name, item_cnt=3409):
    """
    将评分数据读入成csr稀疏矩阵

    :param rating_file_name: str, 评分数据文件
    :return: csr_matrix
    """
    row_index = array('I')
    col_index = array('I')
    data = array('f')
    with open(rating_file_name, 'r') as f:
        for line in f.readlines():
            row, col, element, timestmp = line.strip().split("::")
            row_index.append(int(row))
            col_index.append(int(col))
            data.append(float(element))
    return coo_matrix((data, (row_index, col_index)), dtype="float", shape=(max(row_index) + 1, item_cnt)).tocsr()


if __name__ == '__main__':
    rating_mat = read("/Users/wumengling/PycharmProjects/movielens_resys/data/small_train_ratings.dat")
    print rating_mat.shape
    print rating_mat
