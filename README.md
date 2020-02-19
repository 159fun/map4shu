# map4shu
---
- 运行环境Pycharm，在项目终端下创建虚拟环境；
```
python3 -m venv 11_env（11_env为名称自取）
```
并激活虚拟环境；
```
source 11_env/bin/activate
```
安装django；
```
'pip3 install django'
```
运行项目；
```
python manage.py runserver
```
- 用pyhton字典形式的链表存储节点信息，用最小堆排序优化了原生的Dijkstra算法；
- 网页部分较简陋，通过链接跳转 查询、后台数据管理、所有地点概览 3个主要功能；
- django admin用户名gui，密码map4func；百度地图api key需替换成自己申请的。
