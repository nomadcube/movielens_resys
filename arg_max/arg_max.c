#include "pthread.h"
#include "stdlib.h"
#include "stdio.h"

//公共变量
const int M = 4;
const int N = 3;
float mat[M][N] = {{0.0, 1.0, 2.0}, {3.0, 4.0, 5.0}, {6.0, 8.0, 3.0}, {2.0, 0.0, 10.0}};
int a[M];
long thread_count;


//各个线程调用的函数
void *max_column(void* rank)
{
    long row_no = (long) rank;
    float max_value = mat[row_no][0];
    int max_index = 0;
    int i;

    for(i = 1; i < N; i++)
    {
        if(mat[row_no][i] > max_value)
        {
            max_value = mat[row_no][i];
            max_index = i;
        }
    }

    a[row_no] = max_index;

    return NULL;
}

//入口函数
int main(int argc, char* argv[])
{
    long thread_id;
    pthread_t* threads_handler;
    thread_count = 4;

//   分配内存块用于存储thread_count个线程变量
    threads_handler = malloc(thread_count * sizeof(pthread_t));

//    创建线程并给各线程分配数据和任务
    for(thread_id = 0; thread_id < thread_count; thread_id++)
        pthread_create(&threads_handler[thread_id], NULL, max_column, (void*) thread_id);

//    在子线程终结前让主线程阻塞
    for(thread_id = 0; thread_id < thread_count; thread_id++)
        pthread_join(threads_handler[thread_id], NULL);

//    打印结果
    printf ("column id with max value is %i, %i, %i, %i" , a[0], a[1], a[2], a[3]);

    free(threads_handler);
    return 0;
}