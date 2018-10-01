#coding=utf-8
#这是用来获取微博主页评论信息的脚本

import requests  #http常用
import json  #把json的代码转换为Python
from lxml import html  #解析html ，下面用来去除html标签等
import re  #解析不规则文本

class Tool:
    removeImg=re.compile('<img.*?>| {1,7}|&nbsp;')
    removeAddr=re.compile('<a.*?>|</a>')
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')

    removeTag=re.compile('<.*?>')
    @classmethod
    def replace(cls,x):
        #正则表达式 sub:替换
        x=re.sub(cls.removeImg,'',x)
        x=re.sub(cls.removeAddr,'',x)
        x=re.sub(cls.replaceLine,'',x)
        x=re.sub(cls.removeTag,'',x)
        return x.strip()


class weibo(object):
    def get_weibo(self,id,page):#个人主页的id
        '''
        获取博主的微博
        :return:list_cards
        '''
        #微博主页的url，107603是统一的，不同主页后面不一样
        url="https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}&containerid=107603{}&page={}".format(id,id,id,page);
        response=requests.get(url)
        #因为返回的信息和字典差不多，json.loads()可以把返回的信息转化为python的字典
        ob_json=json.loads(response.text)
        list_cards=ob_json.get('cards')
        return list_cards
    def get_comments(self,id):  #点击评论进入的id
        url="https://m.weibo.cn/api/comments/show?id={}&page=1".format(id)
        response=requests.get(url)
        ob_json=json.loads(response.text)
        list_comments=ob_json.get('hot_data')
        return list_comments
    def main(self,uid,page):
        list_cards=self.get_weibo(uid,page)
        # print list_cards
        for card in list_cards:
            if card.get('card_type')==9:
                id=card.get('mblog').get('id') #这是评论去的id
                text=card.get('mblog').get('text')
                #因为得到的评论会含有html的标签，这是去除标签的
                text=Tool.replace(text)
                print '***'
                print u"@@@微博："+text+'\n'
                list_comments=weibo.get_comments(id)
                count_hotcomments=1
                for comment in list_comments:
                    created_at=comment.get('created_at')#获取时间
                    like_counts=comment.get('like_counts') #点赞数
                    text=comment.get('text')
                    #除了用re去除标签外，下面的方法更好
                    #fromstring()解析html
                    tree=html.fromstring(text)
                    text=tree.xpath('string(.)')
                    name_user=comment.get('user').get('screen_name')
                    source=comment.get('source')
                    if source=='':
                        source=u'未知'
                    print str(count_hotcomments),': **',name_user,'**',u'**发表于:**'+created_at,u'**点赞数:**'+str(like_counts)+u'**来自**'+source
                    print text+'\n'
                    count_hotcomments+=1
                    print'==================='
if __name__=='__main__':
    weibo=weibo()
    weibo.main('1241148864',1)








