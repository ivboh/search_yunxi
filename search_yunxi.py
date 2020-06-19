from urllib.request import Request, urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
#from selenium import webdriver
#import selenium
import time
import numpy as np
import io
import datetime

def read_link(URL):
  url = urlopen(URL)
  return [line.decode('utf-8') for line in url]

def scrape(logger_path , search_list):
  '''
  open webpage with given URL list.
  '''
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
  search_list = read_link("https://yunxi.s3.us-east-2.amazonaws.com/search/search_link.txt")
  for i in search_list:
    print(i)
  logger_path = "my_log.txt"
  i=0
  while(i>=0):
    scrape(logger_path, search_list)
    print(str(i)+'\n')
    i+=1  
if __name__ == "__main__":
  main()
