# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from .models import address_info, weights
from .dijkstra import dijkstra
import json
import time


def search(request, distance=0, start='', end=''):
    address_point = address_info.objects.all()  # 把model中所有对象对应到一个包含所有对象的数组,
    begin = time.clock()
    address_longitude = []  # 创建空数组存储地点信息对应键值
    address_latitude = []
    address_data = []

    arcs = weights.objects.all()  # 创建数组对应存储边长信息的weights模型
    nopes = weights.objects.filter(state=1)

    graph = [[float('inf') for i in range(256)] for i in range(256)]  # 创建默认图无联通,权值无穷大
    for i in range(256):
        graph[i][i] = 0  # 无向图为对称矩阵，保证对称线处为0
    for arc in arcs:
        graph[arc.index1][arc.index2] = arc.weight
        graph[arc.index2][arc.index1] = arc.weight  # 对图中的边长赋值，无向图对称赋值两次

    graph1 = [[float('inf') for j in range(256)] for j in range(256)]  # 创建默认图无联通,权值无穷大
    for j in range(256):
        graph1[j][j] = 0  # 无向图为对称矩阵，保证对称线处为0
    for nope in nopes:
        graph1[nope.index1][nope.index2] = nope.weight
        graph1[nope.index2][nope.index1] = nope.weight

    walk = {}
    for i in range(len(graph)):
        a = {}
        for j in range(len(graph)):
            if graph[i][j] != float('inf'):
                a[j] = graph[i][j]
                walk[i] = a

    ride = {}
    for i in range(len(graph1)):
        a = {}
        for j in range(len(graph1)):
            if graph1[i][j] != float('inf'):
                a[j] = graph1[i][j]
                ride[i] = a

    if 'f' and 'g' in request.GET:  # 判断输入框是否有值
        f = request.GET['f']  # get获得前端输入值
        g = request.GET['g']
        sel = request.GET['sel']
        start = address_point.get(index=f).data
        end = address_point.get(index=g).data  # 根据输入值过虑点对象，用data中的字符索引

        if int(sel) == 1:  # 出行方式为步行的话使用原矩阵来进行最短路径计算
            (dis, path) = dijkstra(walk, int(f), int(g))
        else:  # 出行方式为骑行的话，去掉原矩阵中不能骑车的路段对应的边
            (dis, path) = dijkstra(ride, int(f), int(g))

        for node in path:  # 对最短路径中的点遍历信息构建数组
            a = address_point.get(index=node)  # 获得序号为node的点对象
            address_longitude.append(a.longitude)
            address_latitude.append(a.latitude)
            address_data.append(a.data)  # 得到最短路径中每个点的经纬度，信息
        distance = dis  # 获取最短路径距离
        print(path)
        final = time.clock()
        print("刷新地图时间" + str(final - begin))  # 打印处理时间

    return render(request, 'search.html',  # 指定返回回网页名称
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude),
                   'address_data': json.dumps(address_data),
                   'distance': json.dumps(distance),  # int型最短距离
                   'start': json.dumps(start),
                   'end': json.dumps(end),
                   })  # 返回前端json数据用来画图


def show(request):
    address_longitude = []
    address_latitude = []
    address_data = []
    pairs1 = []
    pairs2 = []
    pairs3 = []
    pairs4 = []
    address_point = address_info.objects.all()

    for node in address_point:  # 画出所有的点
        address_longitude.append(node.longitude)
        address_latitude.append(node.latitude)
        address_data.append(str(node.index) + node.data)

    if 'sel' in request.GET:  # 判断输入框是否有值
        sel = request.GET['sel']  # get获得前端输入值
        if int(sel) == 0:
            roads = weights.objects.filter(state=0)
        else:
            roads = weights.objects.all()  # 创建数组对应存储边长信息的weights模型
        for arc in roads:
            a = address_info.objects.get(index=arc.index1)  # 根据输入值过虑点对象，用data中的字符索引
            b = address_info.objects.get(index=arc.index2)
            pairs1.append(a.longitude)
            pairs2.append(a.latitude)
            pairs3.append(b.longitude)
            pairs4.append(b.latitude)

    return render(request, 'show.html',
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude),
                   'address_data': json.dumps(address_data),
                   'pairs1': json.dumps(pairs1),
                   'pairs2': json.dumps(pairs2),
                   'pairs3': json.dumps(pairs3),
                   'pairs4': json.dumps(pairs4)
                   })  # 返回前端json数据用来画图'''
