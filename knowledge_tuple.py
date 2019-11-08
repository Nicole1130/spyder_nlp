#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:57:09 2019

@author: nicolezhu
"""

import jiagu

class knowledge_tuple(object):
    def __init__(self):
        self.text = '姚沁蕾（Yao Xinlei）,2000年9月12日出生于上海市徐汇区,祖籍江苏省苏州市吴江区震泽镇，是姚明和叶莉的女儿。'
#        self.text = '姚明（Yao Ming），1980年9月12日出生于上海市徐汇区，祖籍江苏省苏州市吴江区震泽镇，前中国职业篮球运动员，司职中锋，现任中职联公司董事长兼总经理。'
    
    def get_tuple(self,text = None):  
        if text != None:
            self.text = text
        knowledge = jiagu.knowledge(self.text)
        return knowledge

if __name__ == '__main__':
    kl_tuple = knowledge_tuple()
#    Tuple = kl_tuple.get_tuple('姚沁蕾（Yao Xinlei），Amy，美籍华人，女，是姚明和叶莉的女儿。')
    text = '姚沁蕾（Yao Xinlei）,2000年9月12日出生于上海市徐汇区,祖籍江苏省苏州市吴江区震泽镇，是姚明和叶莉的女儿。'
    Tuple = kl_tuple.get_tuple(text)
    print(Tuple)