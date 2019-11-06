from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    # 获取当前百科名称
    def _get_title(self, page_url, soup): 
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        title = title_node.get_text()
        return title
    
    # 获取当前百科简介
    def _get_intro(self, page_url, soup): 
        summary_node = soup.find('div', class_="lemma-summary")
        summary = summary_node.get_text()
        return summary
    
    # 获取当前百科基本信息
    def _get_basic_info(self, page_url, soup):
        name_node = soup.find_all('dt', class_="basicInfo-item name")
        name_data = []
        value_data = []
        name_node = soup.find_all('dt', class_="basicInfo-item name")
        for i in range(len(name_node)):
            name_data.append("".join(name_node[i].get_text().split()))
#            name_data.append(re.sub(' ','',name_node[i].get_text()))
#            name_data.append(name_node[i].get_text().replace(' ', ''))
        value_node = soup.find_all('dd', class_="basicInfo-item value")
        for i in range(len(value_node)):
            value_data.append(value_node[i].get_text().replace('\n', ''))
        return name_data,value_data
        
    
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # lemma-summary
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def paser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
    def my_basicInfo_paser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        name,value = self._get_basic_info(page_url, soup)
        return name,value
        
        