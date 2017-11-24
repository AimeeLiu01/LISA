#coding=utf-8
import urllib
import json
import types
import re
import time
from sqlalchemy import *
from sqlalchemy.orm import *
num=1
idlist=[]
error=0  
def getinfo(nid,connection):
        global num
        global error
        global idlist
        #获取全局变量
        url="http://www.creditjx.gov.cn/datareporting/doublePublicity/punishDetail/"+nid
        #拼接详情页的地址
        f = urllib.urlopen(url)
        #访问
        html=f.read().decode('utf-8')
        m=re.findall(r'<td.*">(.*?)</td>',html)
        #匹配html中数据
        sql='INSERT INTO t_jiangxi (case_no ,case_name,punish_reason,law_item,punish_type1,punish_type2,entity_name,credit_no,org_code,reg_no,tax_no,identity_card,legal_man,punish_result,punish_date,punish_agent,current_status,area_code,offical_updtime) VALUES ('
        for i in m:
            a='"'+i+'",'
            sql=sql+a
        #利用循环拼接需要执行的sql语句
        sql=sql+")"
        sql=sql.replace(",)",")")
        #去掉多余的,确保sql语句正常
        try:
            result = connection.execute(sql)
            #执行sql语句
            if result:
                print "第"+str(num)+"条数据保存成功"
            else:
                print "第"+str(num)+"条数据保存失败"
            num=num+1
        except:
            print "第"+str(num)+"保存失败,正在重新保存"
            error=error+1
            if error<3:
                print idlist[num-1]
                getinfo(idlist[num-1])
            else:
                print "放弃第"+str(num)+"数据"
                error=0
                num=num+1
                pass
def request(url,pages):
    global idlist
    print "正在获取第"+str(pages)+"页数据..."
    data={
        'tableType':1,
        'inpParam':'',
        'orgIdOrRegionId:':'',
        'page':pages,
        'pageSize':15
        }
    data = urllib.urlencode(data).encode('utf-8')
    f = urllib.urlopen(url,data=data)
    result=f.read()
    m=re.findall(r'"id":"(.*?)"',result)
    idlist=m
    a=1
    mysql_engine = create_engine('mysql://root:112233@127.0.0.1/base?charset=utf8')
    #address 数据库://用户名:密码（没有密码则为空）@主机名：端口/数据库名
    connection = mysql_engine.connect()
    for i in m:
        try:
            a=a+1
            getinfo(i,connection)
        except:
            continue
    connection.close()
    #关闭连接
def main():
    url='http://www.creditjx.gov.cn/datareporting/doublePublicity/queryDoublePublicityList.json'
    pages=input('请输入需要爬取的页数,一页15条\n')
    pages=pages+1
    for i in range(1,pages):
        time.sleep(1)
        #暂停一秒
        request(url,i)
if __name__=='__main__':
    main()
