# -*- coding: utf-8 -*-

from queue import PriorityQueue as PQ

"""
优化单源最短路径问题：
Dijkstra 算法
"""

INF = float("inf")


# pq = PQ()
# pq.put((-2, 'c'))
# pq.put((-3, 'b'))
# pq.put((-4, 'a'))
# pq.put((-7, 'c'))
# print(pq.queue)
class Node:
    def __init__(self, u, step):
        self.u = u
        self.step = step

    def __lt__(self, other):
        return self.step < other.step


def Dijkstra(st):
    pq = PQ()
    pq.put(Node(st, 0))

    dist[st] = 0

    while not pq.empty():
        it = pq.get()
        t = it.u
        if flag[t]:
            continue
        flag[t] = 1

        for i in range(1, n + 1):  # 更新当前点t的邻接点到源点的最短距离
            if not flag[i] and Map[t][i] < INF:
                if dist[i] > dist[t] + Map[t][i]:
                    dist[i] = dist[t] + Map[t][i]
                    pq.put(Node(i, dist[i]))


if __name__ == '__main__':
    # n = int(input("请输入城市的个数：\n"))
    # m = int(input("请输入城市之间的路线个数：\n"))
    n = 5
    m = 11
    Map = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    dist = [INF for _ in range(n + 1)]  # 记录源点到某点的最短路径长度
    # flag[i] = True 说明顶点i已加入到S中，否则顶点i属于 V-S
    flag = [0 for _ in range(n + 1)]
    p = [-1 for _ in range(n + 1)]  # 记录源点到某点最短路径上的该点的前驱。

    # print("请输入城市之间的路线和距离：")

    # while m:
    #     u, v, w = (int(i) for i in input().split())
    #     Map[u][v] = w
    #
    #     m -= 1

    inputs = [(1, 2, 2), (1, 3, 3),
              (2, 3, 5), (2, 4, 6),
              (3, 4, 7), (3, 5, 1),
              (4, 5, 4)]

    for u, v, w in inputs:
        Map[u][v] = w

    # st = int(input("请输入小明所在位置："))
    st = 1
    Dijkstra(st)

    print("小明所在的位置：", st)

    for i in range(1, n + 1):
        print("小明：", str(st), " - 要去的位置:", i, end=' ')

        if dist[i] == INF:
            print("sorry, 无路可达。")
        else:
            print("最短距离为：", dist[i])

    # findPath(st)
