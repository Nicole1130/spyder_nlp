#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:38:57 2019

@author: nicolezhu
"""

from py2neo import Graph, Node, Relationship
from py2neo import  NodeSelector
import json

class my_neo4j(object):
    def __init__(self):
        self.graph = Graph("http://localhost:7474", username="neo4j", password='123')
        #graph.delete_all() # 清空数据库
        
    def clear_graph(self):
        self.graph.delete_all() # 清空数据库
        
    def update_node(self,label,name1):
        try :
            node = self.graph.find_one(label=label, property_key='name', property_value=name1)
            if(node == None):
                return Node(label, name=name1)
            else:
                return node
        except Exception as e:
            print(e)
    
    def add_tuple(self,tuples):
        try:
            for t in tuples:
                entity1 = self.update_node('人物',t[0])
                entity2 = self.update_node('人物',t[2])
                link = Relationship(entity1,t[1], entity2)
                self.graph.create(link)
            print("导入成功！")
        except Exception as e:
            print(e)
            
        
#    def findHasNode(label,name):
#        data2 = graph.find_one(label=label, property_key='name', property_value=name)
#        if(data2 == None):
#            return 0
#        else:
#            return data2
#    
#    def createRelationship(t1,t1_name,t2,t2_name,r):
#        tempDate = findHasNode(t1,t1_name)
#        tempDate2 = findHasNode(t2,t2_name)
#        if(tempDate == 0): #如果没有tempDate这个节点就创建这个节点，并进行返回这个节点
#            graph.create(Node(t1,name = t1_name))
#            tempDate = findHasNode(t1, t1_name)
#        if(tempDate2 == 0): #如果没有tempDate2这个节点就创建这个节点，并进行返回这个节点
#            graph.create(Node(t2,name = t2_name))
#            tempDate2 = findHasNode(t2,t2_name)
#        graph.create(Relationship(tempDate, r, tempDate2))

if __name__ == '__main__':
    ori_data = json.load(open("all.json"))
    entity_name = '中文名'
    entity = Node('school', name=ori_data[entity_name ])
    ori_data.pop(entity_name)
    m_n = my_neo4j()
    for r,data in zip(ori_data.keys(),ori_data.values()):
        if len(data)<10:
            entity2 = Node('school', name=data)
            link = Relationship(entity, r, entity2)
            m_n.graph.create(link)
        else:
            entity[r] = data

#a = Node('school', name='天津工业')
#c = Node('school', name='天津工业')
#b = Node('school', name='太原理工')
#d = Node('school', name='太原理工')
#r = Relationship(a, 'KNOWNS', b)
#rr = Relationship(a, 'pp', d)
#s = a | b | r
#ss = a | d | rr
#graph.create(s)
#graph.create(ss)

