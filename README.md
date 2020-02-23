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
```python
pip3 install django
```
  运行项目；
```
python manage.py runserver
```
- 用pyhton字典形式的链表存储节点信息，用**最小堆排序**优化了原生的Dijkstra算法；
- 网页部分较简陋，通过链接跳转*最短路径查询*、*后台数据管理*、*所有地点概览* 3个主要功能；
- django admin用户名gui，密码map4func，[百度地图api key](https://lbsyun.baidu.com/)需替换成自己申请的。
---
## 截图
![主界面](https://github.com/159fun/map4shu/blob/master/image/%E4%B8%BB%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.png?raw=true)
