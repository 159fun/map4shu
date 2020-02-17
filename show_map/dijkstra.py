import heapq  # 堆优化库，目前没写出来，只能导入库
import time


# 用邻接表和堆排序优化的算法
def dijkstra(G, start, end):
    INF = float('inf')

    dis = dict((key, INF) for key in G)  # start到每个点的距离
    dis[start] = 0
    vis = dict((key, False) for key in G)  # 是否访问过，1位访问过，0为未访问
    #  堆优化
    pq = []  # 存放排序后的值
    heapq.heappush(pq, [dis[start], start])

    t3 = time.time()
    path = dict((key, [start]) for key in G)  # 记录到每个点的路径
    while len(pq) > 0:
        v_dis, v = heapq.heappop(pq)  # 未访问点中距离最小的点和对应的距离
        if vis[v]:
            continue
        vis[v] = True
        p = path[v].copy()  # 到v的最短路径
        for node in G[v]:  # 与v直接相连的点
            new_dis = dis[v] + float(G[v][node])
            if new_dis < dis[node] and (not vis[node]):  # 如果与v直接相连的node通过v到src的距离小于dis中对应的node的值,则用小的值替换
                dis[node] = new_dis  # 更新点的距离
                #  dis_un[node][0] = new_dis    #更新未访问的点到start的距离
                heapq.heappush(pq, [dis[node], node])
                temp = p.copy()
                temp.append(node)  # 更新node的路径
                path[node] = temp  # 将新路径赋值给temp

    t4 = time.time()
    print('Dijkstra算法所用时间:', t4 - t3)
    return dis[end], path[end]


'''原生算法'''
'''def dijkstra(matrix, src, end):  # 输入矩阵，起点，终点
    if matrix is None:
        return None
    # 定点集合
    nodes = [i for i in range(len(matrix))]  # 获取顶点列表，用邻接矩阵存储图
    # 顶点是否被访问
    visited = [src]  # 从源点出发
    # 初始化dis
    dis = {src: 0}  # 源点到自身的距离为0
    for i in nodes:
        dis[i] = matrix[src][i]
    path = {src: {src: []}}  # 记录源节点到每个节点的路径
    k = pre = src

    while nodes:
        temp_k = k
        mid_distance = float('inf')  # 设置中间距离无穷大
        for v in visited:
            for d in nodes:
                if (matrix[src][v] != float('inf')) and (matrix[v][d] != float('inf')):  # 有边
                    new_distance = matrix[src][v] + matrix[v][d]
                    if new_distance <= mid_distance:
                        mid_distance = new_distance
                        matrix[src][d] = new_distance  # 进行距离更新
                        k = d
                        pre = v
        if k != src and temp_k == k:
            break
        dis[k] = mid_distance  # 最短路径
        path[src][k] = [i for i in path[src][pre]]
        path[src][k].append(k)

        visited.append(k)
        nodes.remove(k)
        print(nodes)
    if dis[end] == float('inf'):
        return dis[end], path[src][src]  # 如果没有路径返回源点
    else:
        return dis[end], path[src][end]  # 有路径的话返回路径'''
