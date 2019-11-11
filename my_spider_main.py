# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:27:41 2019

@author: Administrator
"""
import sys
import os
sys.path.append(os.path.dirname(sys.argv[0]))

import url_manager
import html_downloader
import html_parser
import html_outputer
import time


class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        while root_url != None:
            try:               
                html_cont = self.downloader.download(root_url)
                # 爬取百科词条名称
                title = self.parser.my_paser(root_url, html_cont,'title')  
            
#                # 爬取百科词条基本信息表格
#                result_data_dict = dict()
#                names, values = self.parser.my_paser(root_url, html_cont,'basic_info')
#                for (name, value) in zip(names,values):
#                      result_data_dict[name] = value
#                return result_data_dict
            
                # 爬取百科词条简介
                summ = self.parser.my_paser(root_url, html_cont,'intro')  
                log_info = [title]
                self.outputer.log('fail.json',log_info,1) # 追加方式
                self.outputer.log('succ.json',log_info,0) # 覆盖方式                
                return summ
                
            except:
                print('craw failed')
                log_info = [root_url,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))]
                self.outputer.log('fail.json',log_info,1) # 追加方式
                return

if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/%E5%A4%A9%E6%B4%A5%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6/275160?fr=aladdin"
    obj_spider = Spider()
    data = obj_spider.craw(root_url)
    html_outputer.HtmlOutputer().output_json(data)  



