# coding=utf-8
from scipy.sparse import coo_matrix
from array import array


def read_ratings(rating_file_name, item_cnt=3409):
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


def read_movies(movies_file_name, genres_mapping_rel):
    """
    将电影类别数据读入成稀疏矩阵

    :param movies_file_name: str, 电影类别数据
    :param genres_mapping_rel: dict, 将电影类别名称映射为整型
    :return: csr_matrix, M*N 矩阵，M为电影数目，N为总类别数目，当电影属于当前类别时对应元素值为1，否则为0
    """
    rows = array('I')
    cols = array('I')
    elements = array('f')
    with open(movies_file_name, 'r') as f:
        for line in f.readlines():
            movie_id, name, genres = line.strip().split("::")
            for each_genre in genres.split("|"):
                rows.append(int(movie_id))
                cols.append(genres_mapping_rel[each_genre])
                elements.append(1.0)
    return coo_matrix((elements, (rows, cols)), dtype="float").tocsr()


if __name__ == '__main__':
    rating_mat = read_ratings("/Users/wumengling/PycharmProjects/movielens_resys/data/small_train_ratings.dat")
    # print rating_mat.shape
    # print rating_mat
    genres_rel = {genre: genre_no for genre_no, genre in enumerate(
        ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
         "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"])}
    movies = read_movies("/Users/wumengling/PycharmProjects/movielens_resys/data/small_movies.dat", genres_rel)
