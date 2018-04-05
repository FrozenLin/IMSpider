# -*- coding: utf-8 -*-


from scrapy.cmdline import execute

import sys
import os

# 设置主目录到项目下,参数__file__指的是当前python文件
# os.path.dirname()获取父目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute函数传入参数，数组
# 启动伯乐在线爬虫
# execute(["scrapy", "crawl", "jobbole"])
# execute(["scrapy", "crawl", "zhihu"])
# 启动知乎爬虫
# execute(["scrapy", "crawl", "zhihu_sel"])
# 启动拉勾网爬虫
execute(["scrapy", "crawl", "lagou"])
