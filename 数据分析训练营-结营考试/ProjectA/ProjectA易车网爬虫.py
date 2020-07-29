import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# 输入易车网内任意品牌网址，输出包含名称，最低价格，最高价格，产品图片链接的csv文件
def car_pricing(url,csvfile):
	
	wd=requests.get(url).content
	soup= BeautifulSoup(wd,'html.parser')
	# 分别获取包含image，names，price的元素列表
	image_urls=soup.select('#data_table_MasterSerialList_0 > div > div > a > img')
	names=soup.select('#data_table_MasterSerialList_0 > div > ul > li.name')
	prices=soup.select('#data_table_MasterSerialList_0 > div > ul > li.price')

	# 构建包含名称，价格，图片链接的list [['Model','min_price','max_price','image_url'],..]
	car_pricing=[]
	for name, price, image_url in zip(names,prices,image_urls):
	    name= name.text
	    price_range= price.text.strip().replace('万','').split('-')
	#     print(price_range)
	    min_price= price_range[0]  
	#     此处避免用1做索引，因为有部分车型只有一个价格 而非取件 取1会报错
	    max_price= price_range[-1]
	    image_url= image_url.attrs['src']
	    car_pricing.append([name,min_price,max_price,image_url])
	# 添加字段名
	titles=['Model','min_price','max_price','image_url']
	df= pd.DataFrame(car_pricing,columns=titles)
	df.to_csv(csvfile,index=None,encoding='gbk')

if __name__ == '__main__':	
	# 大众车型网址
	url='http://car.bitauto.com/volkswagen/'
	csvfile='car_pricing.csv'
	car_pricing(url,csvfile)


