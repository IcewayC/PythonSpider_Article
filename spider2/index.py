# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

articleUrl = 'http://www.qiushibaike.com/textnew/page/%d' #文章地址
commentUrl = 'http://www.qiushibaike.com/article/%s' #评论地址
page = 0


#打开网页 获取源码
def getContentOrComment(Url):
    #加头部信息headers，模拟浏览器
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    headers = {'User-Agent':user_agent}
    req = urllib2.Request(url=Url, headers=headers) #用地址创建一个请求
    response = urllib2.urlopen(req) #打开网址
    content = response.read()
    return content


while True:
    raw = raw_input("输入enter查看或输入exit退出，请输入你们的选择：")
    if raw == 'exit':
        break
    page += 1
    articlePage = getContentOrComment(articleUrl % page)
    soupArticle = BeautifulSoup(articlePage, 'html.parser')#解析方式
    articleFloor = 1
    for string in soupArticle.find_all(attrs="article block untagged mb15"):
        commentID = str(string.get('id')).strip().split('_')[-1]
        # print commentID
        print '\n'
        print articleFloor, '.', string.find(attrs='content').get_text().strip()#获取文本
        articleFloor += 1

        commentPage = getContentOrComment(commentUrl % commentID)
        soupComment = BeautifulSoup(commentPage, 'html.parser')
        commentFloor = 1
        for comment in soupComment.find_all(attrs='body'):
            print "     ", commentFloor, "楼回复", comment.get_text().strip()


