class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls: #若输入url不在新、旧列表中
            self.new_urls.add(url) # 添加到新列表中

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):    
        return len(self.new_urls) != 0

    def get_new_url(self): # 获取新的url进行后续处理
        new_url = self.new_urls.pop() # new_urls集合出列一个元素
        self.old_urls.add(new_url) # 添加旧url集合中
        return new_url
