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

    def find_node(self,label,name1)  :
        node = self.graph.find_one(label=label, property_key='name', property_value=name1)
        return node
    
    def update_node(self,label,name1): # 更新节点
        try :
            node = self.find_node(label,name1)
            if(node == None):
                return Node(label, name=name1)
            else:
                return node
        except Exception as e:
            print(e)
            
    def change_property(self,label,name1,p_name,p_value):# 添加节点属性
        try :
            node = self.find_node(label,name1)        
            if(node == None):
                print("Node does not exist!")
                return None
            else:
                node[p_name] = p_value
                self.graph.push(node)
        except Exception as e:
            print(e)
            
    def add_tuple(self,tuples,test_r='school'): # 添加三元组
    # tuples结构应为[label1，name1，r，label2，name2]
    # 目前简化起见省略两个label   
        try:
            for t in tuples:
                entity1 = self.update_node(test_r,t[0])
                entity2 = self.update_node(test_r,t[2])
                link = Relationship(entity1,t[1], entity2)
                self.graph.create(link)
            print("导入成功！")
        except Exception as e:
            print(e)
            
    def query_node(self,label,name1): # 查询节点
    # 返回节点的属性、关系列表
        try :
            node = self.find_node(label,name1)
            if(node == None):
                print("Node does not exist!")
                return None
            else:
                n_property = dict(node)
                n_relation =list()
                for rel in self.graph.match(start_node=node):                  
                    n_relation.append(rel.end_node()["name"])
                return [n_property,n_relation]
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
    # 测试从json文件中添加三元组关系
    ## 导入百科关系结构表文件
    ori_data = json.load(open("all.json"))
    entity_index = '中文名'    
    entity_name = ori_data[entity_index]
    ori_data.pop(entity_index)
    m_n = my_neo4j()
    tuples=[]
    for r,data in zip(ori_data.keys(),ori_data.values()):
        # all.json中选择短的作为关系
        if len(data)<10:
            tuples.append([entity_name,r,data])
    m_n.add_tuple(tuples)
            
    
    # 测试节点属性添加功能
    m_n = my_neo4j()
    m_n.change_property('school','天津工业大学','测试','01')
    
    # 测试节点查询功能，返回与目标节点的属性和连接关系
    m_n = my_neo4j()
    node_info = m_n.query_node('school','天津工业大学')
    


