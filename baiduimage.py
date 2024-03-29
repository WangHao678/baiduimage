import os
import requests
from urllib import parse
import time
import random
import re

class BaiduImage(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        self.headers = {'User-Agent':'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

    def get_image(self,url,word):
        html = requests.get(url=url,headers=self.headers).text
        p = re.compile('"thumbURL":"(.*?)"',re.S)
        link_list = p.findall(html)
        # link_list:['xxx.jpg','xxx.jpg']
        self.save_image(link_list,word)

    #保存图片到指定路径
    def save_image(self,link_list,word):
        directory = '/home/tarena/images/{}/'.format(word)
        if not os.path.exists(directory):
            os.makedirs(directory)
        for link in link_list:
            html = requests.get(url=link,headers=self.headers).content
            filename = directory + link[-30:]
            with open(filename,'wb') as f:
                f.write(html)

    def run(self):
        word = input('你想要谁的照片?请输入:')
        params = parse.quote(word)
        url = self.url.format(params)
        self.get_image(url,word)

if __name__ == '__main__':
    spider = BaiduImage()
    spider.run()
