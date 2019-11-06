# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:27:41 2019

@author: Administrator
"""
import url_manager
import html_downloader
import html_parser
import html_outputer
import json

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url) #添加初始url
        while self.urls.has_new_url():
            try:
                result_data = []
                new_url = self.urls.get_new_url()
                print("craw %d : %s" %(count, new_url))
                html_cont = self.downloader.download(new_url)
                names, values = self.parser.my_basicInfo_paser(new_url, html_cont)
                for (name, value) in zip(names,values):
                    result_data.append({name:value})
                
#                fw = open('all.json', 'w')
#                fw.write(json.dumps(result_data))
#                fw.close()
#                print("任务完成")
                
                with open('all.json', 'w',encoding='utf-8') as f:
                    json.dump(result_data, f)
                
                if count == 10:
                    break
                count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html()
        return result_data


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/%E5%A4%A9%E6%B4%A5%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6/275160?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
