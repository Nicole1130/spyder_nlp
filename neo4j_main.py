#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:31:20 2019

@author: nicolezhu
"""
import json
#from py2neo import Node, Relationship, Graph
#graph = Graph('http://localhost:7474', username='neo4j', password='123') 


from neo4j.v1 import GraphDatabase
driver = GraphDatabase.driver("bolt://127.0.0.1:7687", auth=("neo4j", "123"))

class node(object):
    def __init__(self,label,n_type):
        self.label = label
        self.n_type = n_type
        
    def add_node(self,tx,label,node_type,node_name):    
        tx.run("match(%s:%s{name:$node_name}) return (%s)" %(label,node_type,label),node_name=node_name)
        
def add_node(tx,label,node_type,node_name):
#    tx.run("match(%s:%s{name:$node_name}) return (%s)" %(label,node_type,label),node_name=node_name)           
    tx.run("create(%s:%s{name:$node_name})" %(label,node_type),node_name=node_name)

def check_node(tx,label,node_type):
    order = label+'.id'
    print(tx.run("match(%s:%s) return (%s)" %(label,node_type,order)))      
#def add_node(tx, name1, relation,name2):
#
#    tx.run("MERGE (a:Node {name: $name1}) "
#        "MERGE (b:Node {name: $name2}) "
#           "MERGE (a)-[:"+relation+"]-> (b)",
#           name1=name1,name2=name2)
    
            
def add_property(tx,label,n_type,p_type,p_name):
#    tx.run("match(TYLG:school) set TYLG.year='1900' return TYLG")    # 可行
    order1 = label+'.'+p_type
    tx.run("match(%s:%s) set %s=%s return %s" %(label,n_type,order1,p_name,label)) 


if __name__ == '__main__':
    with driver.session() as session:
        try:
            a=node('TYLG','school')
#            session.write_transaction(a.add_node,'TYLG','school','太原理工')
            session.write_transaction(add_node, 'TYLG','school','太原理工')
            session.write_transaction(check_node, 'TYLG','school')
            session.write_transaction(check_node, 'TYLG1','school')
#            session.write_transaction(add_property,'TYLG','school','year','1994')
#            session.write_transaction(get_node,'TYLG','school')
        except Exception as e:
            print(str(e))
        
        
        
#        ori_data = json.load(open("all.json"))
#        entity_name = '中文名'
#        entity = ori_data[entity_name ]
#        ori_data.pop(entity_name)
#        for r,data in zip(ori_data.keys(),ori_data.values()):
#            try:
#                session.write_transaction(add_node, entity_name, r,data)
#            except Exception as e:
#                print(entity,r,data,str(e))
            