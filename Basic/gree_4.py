# -*- coding: utf-8 -*-
"""

单源最短路径：Dijkstra

"""


INF = float("inf")


def Dijkstra(u):
    for i in range(1, n + 1):
        dist[i] = Map[u][i]

        if dist[i] == INF:
            p[i] = -1
        else:
            p[i] = u

    dist[u] = 0
    flag[u] = True  # 初始时，集合S中只有一个源点u

    for i in range(1, n + 1):
        tmp, t = INF, u

        for j in range(1, n + 1):  # 在集合V-S中找离源点u最近的顶点t
            if not flag[j] and dist[j] < tmp:
                tmp = dist[j]
                t = i

        if t == u:  # 找不到t,跳出循环
            return

        # 更新 V和S
        flag[t] = True  # 顶点t加入S中

        for j in range(1, n + 1):  # 更新集合V-S中t的邻接点到源点u的距离
            if not flag[j] and Map[t][j] < INF:
                if dist[j] > tmp + Map[t][j]:
                    dist[j] = tmp + Map[t][j]
                    p[j] = t


def findPath(u):
    stack = []
    print("源点为: ", u)
    for i in range(1, n + 1):
        x = p[i]
        while x != -1:  # 将前驱依次压入栈中
            stack.append(x)
            x = p[x]

        print("源点到其他各顶点的最短路径为：", end='')
        while stack:  # 栈不为空时，依次出栈
            print(stack[-1], "-- ", end='')
            stack.pop()

        print(i, "；最短距离为：", dist[i])


if __name__ == '__main__':
    # n = int(input("请输入城市的个数：\n"))
    # m = int(input("请输入城市之间的路线个数：\n"))
    n = 5
    m = 11
    Map = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    dist = [INF for _ in range(n + 1)]  # 记录源点到某点的最短路径长度
    # flag[i] = True 说明顶点i已加入到S中，否则顶点i属于 V-S
    flag = [False for _ in range(n + 1)]
    p = [-1 for _ in range(n + 1)]  # 记录源点到某点最短路径上的该点的前驱。

    # print("请输入城市之间的路线和距离：")

    # while m:
    #     u, v, w = (int(i) for i in input().split())
    #     Map[u][v] = w
    #
    #     m -= 1

    inputs = [(1, 5, 12), (5, 1, 8),
              (1, 2, 16), (2, 1, 29),
              (5, 2, 32), (2, 4, 13),
              (4, 2, 27), (1, 3, 15),
              (3, 1, 21), (3, 4, 7),
              (4, 3, 19)]

    for u, v, w in inputs:
        Map[u][v] = w

    # st = int(input("请输入小明所在位置："))
    st = 5
    Dijkstra(st)

    # print("小明所在的位置：", st)
    #
    # for i in range(1, n + 1):
    #     print("小明：", str(st), " - 要去的位置:", i, end=' ')
    #
    #     if dist[i] == INF:
    #         print("sorry, 无路可达。")
    #     else:
    #         print("最短距离为：", dist[i])

    findPath(st)

