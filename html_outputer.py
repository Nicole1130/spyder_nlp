import json
from os.path import join as pjoin

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
     
    def log(self,file,data,t=0): # t=0覆盖，1追加
        if t == 0 :# 覆盖方式
            with open(file,"w",encoding='utf-8') as f:
                json.dump(data,f,ensure_ascii=False,indent=4);
        elif t == 1 :# 追加方式        
            fr = open(file, 'a') 
            model=json.dumps(data,ensure_ascii=False,indent=4)
            fr.write(model)  
            fr.close()
        else:
            print("log写入方式错误")
            return
        
    def output_json(self,data):
        with open("all.json","w",encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=4);
            
    def output_html(self):
        fout = open('output.html', 'w', encoding="utf-8")

        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close
        
