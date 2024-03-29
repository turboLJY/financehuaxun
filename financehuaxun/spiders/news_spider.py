#encoding:utf-8
import scrapy
import re
from scrapy.selector import Selector
from financehuaxun.items import FinancehuaxunItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule

class ExampleSpider(CrawlSpider):
    name = "huaxunnews"
    allowed_domains = ["finance.591hx.com"]
    start_urls = ['http://finance.591hx.com/']
    rules=(
        Rule(LinkExtractor(allow=r"/([a-zA-Z]+)+/2016\-12\-12+/*"),
        callback="parse_news",follow=True),
    )
    def printcn(suni):
        for i in uni:
            print uni.encode('utf-8')
    def parse_news(self,response):
        item = FinancehuaxunItem()
        item['news_thread']=response.url.strip().split('/')[-1][:-6]
        # self.get_thread(response,item)
        self.get_title(response,item)
        self.get_time_from(response,item)
        self.get_url(response,item)
        self.get_text(response,item)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!remenber to Retrun Item after parse
        return item 
    def get_title(self,response,item):
        title=response.xpath("/html/head/title/text()").extract()
        if title:
            # print 'title:'+title[0][:-5].encode('utf-8')
            item['news_title']=title[0][:-10]

    def get_time_from(self,response,item):
        time_from=response.xpath("//div[@id='main']/div[1]/div[1]/text()").extract()
        if time_from:
            # print 'time'+time[0][:-5].encode('utf-8')
            item['news_time_from']=time_from[0]

    def get_text(self,response,item):
        news_body=response.xpath("//div[@id='newsCon']/p/text()").extract()
        if news_body:
            # for  entry in news_body:
            #   print entry.encode('utf-8')
            item['news_body']=news_body 
    def get_url(self,response,item):
        news_url=response.url
        if news_url:
            #print news_url 
            item['news_url']=news_url
