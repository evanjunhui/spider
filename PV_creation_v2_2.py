#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import getIPa_from_rds
import random
import time

proxies_list = getIPa_from_rds.get_Ip(20000)  # 从数据库内导入IP地址 可选择数量
print('导出的代理IP的数量：',len(proxies_list))

print('打印前20的代理IP',proxies_list[1:20])
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Opera/8.0 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
]  # headers 的清单>

refer_list = ['https://www.baidu.com/',
          'https://www.so.com/',
          'http://blog.csdn.net/',
          'https://www.zhihu.com/search?type=content&q=csdn']
#浏览路径网址

url_list_or = ['https://blog.csdn.net/weixin_42555401/article/details/89381819',
            'https://blog.csdn.net/weixin_42555401/article/details/89181455',
            'https://blog.csdn.net/weixin_42555401/article/details/89429745',
            'https://blog.csdn.net/weixin_42555401/article/details/89457499'
            ]
#需要刷的原创网址

url_list_se = ['https://blog.csdn.net/weixin_42555401/article/details/89236214',
               'https://blog.csdn.net/weixin_42555401/article/details/89023098']
#需要刷的转发网址

PV = 0
FPV = 0
for proxy_ip in proxies_list:
    proxies = {'https': proxy_ip,
               'http': proxy_ip}
    random_user_agent = random.choice(USER_AGENTS)
    headers = {
        'user-agent': random_user_agent}

    try:
        response = requests.get(url=random.choice(refer_list), headers=headers, proxies=proxies, timeout=1)
        #测试是否IP有效
        for i in range(len(url_list_or)-1):
                 response = requests.get(url=random.choice(url_list_or), headers=headers, proxies=proxies, timeout=10)
                 time.sleep(30)
                 PV = PV + 1
        print('代理IP：' + proxy_ip + '有效')
        print('目前PV数量：', PV)

    except:
        # print('代理IP：' + proxy_ip + '无效')
        FPV = FPV + 1
        if FPV% 100 == 0:
           print('目前FPV数量:', FPV)

print('最终的PV是：', PV)
print('最终的FPV是：', FPV)