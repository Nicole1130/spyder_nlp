#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:11:59 2019

@author: nicolezhu
"""

import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]))

import my_spider_main
# 爬取指定网页内容
root_url = "https://baike.baidu.com/item/%E5%A7%9A%E6%98%8E/28?fr=aladdin" # 姚明
#root_url = "https://baike.baidu.com/item/%E5%A7%9A%E6%B2%81%E8%95%BE/531809" # 姚女儿
obj_spider = my_spider_main.Spider()
data = obj_spider.craw(root_url)


# 文本预处理处理
import re
Paragraph = data.split('\n') # 分段
for i in range(len(Paragraph)-1,-1,-1):
    if len(Paragraph[i])<10:
        del(Paragraph[i])
sentences = re.split('(。|！|\!|\.|？|\?)',Paragraph[0])         # 保留分割符

# 三元组提取
import knowledge_tuple
kl_tuple = knowledge_tuple.knowledge_tuple()
Tuples = []
for p in Paragraph:
    Tuple = kl_tuple.get_tuple(p)
    if len(Tuple) != 0:
        Tuples.extend(Tuple)
## 用姚明测试
#Tuple = kl_tuple.get_tuple()



# 导入neo4j
import py2neo_main
my_neo4j = py2neo_main.my_neo4j()
my_neo4j.clear_graph()
my_neo4j.add_tuple(Tuples)