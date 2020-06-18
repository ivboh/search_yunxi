from urllib.request import Request, urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
#from selenium import webdriver
#import selenium
import time
import numpy as np
import io
import datetime

def scrape(logger_path):
  '''
  open webpage with given URL list.
  '''
  search_list = ["https://v.qq.com/x/search/?q=%E6%9C%88%E4%B8%8A%E9%87%8D%E7%81%AB", \
                 "https://s.weibo.com/weibo/%25E6%259C%2588%25E4%25B8%258A%25E9%2587%258D%25E7%2581%25AB?topnav=1&wvr=6&b=1",\
                 "https://s.weibo.com/weibo/%E7%BD%97%E4%BA%91%E7%86%99Leo?topnav=1&wvr=6&topsug=1",\
                 "https://so.youku.com/search_video/q_%E6%9C%88%E4%B8%8A%E9%87%8D%E7%81%AB",
                 "https://so.iqiyi.com/so/q_%E6%9C%88%E4%B8%8A%E9%87%8D%E7%81%AB?source=suggest&sr=577017943149s_sr%3D1&s_token=suggest_4#f4fe07ba4179b5a9614a5e0bfd04d325#0#yue"]
  logger = open(logger_path, 'a+')
  logger.write(str(datetime.datetime.now()))
  for URL in search_list:
    time.sleep(np.random.randint(15,20))
    req = Request(URL)
    try:	
      webpage = urlopen(req)
    except URLError as e:
      if hasattr(e, 'reason'):
        logger.write('Failed to reach a server.')
        logger.write('Reason: '+e.reason)
      elif hasattr(e , 'errno'):
        logger.write('Server coundnot fulfill the request.')
        logger.write('Error code'+e.errno)
    else:
      #soup = BeautifulSoup(webpage.read(), 'html.parser')
      logger.write('Success.')
  logger.close()        

def main():
  i=0
  logger_path = "my_log.txt"	    
  while(i>=0):
    scrape(logger_path)
    print(str(i)+'\n')
    i+=1

if __name__ == "__main__":
  main()
