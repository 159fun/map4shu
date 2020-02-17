# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models


# 定义模型存放点信息
class address_info(models.Model):
    index = models.IntegerField(db_index=True)  # 节点的序号作为查询的主键
    longitude = models.FloatField()  # 节点的经度
    latitude = models.FloatField()  # 节点的纬度
    data = models.CharField(max_length=20)  # 节点的名称信息


# 定义模型存放边长信息
class weights(models.Model):
    index1 = models.IntegerField(db_index=True)  # 边的第一个端点
    index2 = models.IntegerField(db_index=True)  # 边的另一个端点
    weight = models.IntegerField(db_index=True)  # 边的权值
    state = models.IntegerField(default=1, db_index=True)  # 边的路况信息，可以骑行为1
