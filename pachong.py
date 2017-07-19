#encoding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import re
import sys
reload(sys)   
sys.setdefaultencoding('utf8')

def url_open(url):
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            }
    html = requests.get(url, headers=headers)

    return html

def find_list(url):
    title_list = []
    url_list = []
    html = url_open(url).content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml') 
    all_a = soup.find('div',class_='all').find_all('a')
    for a in all_a:
        title_list.append(a.get_text())
        url_list.append(a['href'])

    return title_list, url_list

def get_pages(url):
    html = url_open(url).content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagenavi').select('a > span')[-2].get_text()
    #print(pages)

    return pages 

def find_img(url):
    count = 0
    all_list = find_list(url)
    url_list = all_list[1]
    title_list = all_list[0]
    print('------------------------start-----------------------')
    for num in range(len(url_list)):
        try:
            os.mkdir(title_list[num])
            os.chdir(title_list[num])
            pages = int(get_pages(url_list[num]))
            page_num = pages
            print('now:{0} has:{1} all:{2}'.format(title_list[num], pages, count))
            for i in range(pages):
                try:
                    page_num -= i
                    page_url = url_list[num] + '/' + str(page_num)
                    html = url_open(page_url).text
                    soup = BeautifulSoup(html, 'lxml')
                    img_url = soup.find('div', class_='main-image').find_all('img')[0]['src']
                    save_img(img_url)
                    count += 1
                    page_num = pages 
                except:
                    print('------------------------save-error------------------------')
            os.chdir('..')
            print('------------------------done------------------------')
        except:
            print('-----------------------enter-error-----------------------')
            
def save_img(url):
    filename = url.split('/')[-1]
    with open(filename,'wb') as f:
        img = url_open(url).content
        f.write(img)

def main():
    url = 'http://www.mzitu.com/all/'
    find_img(url)

if __name__ == '__main__':
    main()

    """---------------------
最近学习python，写了个简单的爬虫，分享一下
程序交流板块没权限发帖，就发到这里了www.t00ls.net, r" j/ m0 |( V! K+ i" R

使用的环境：www.t00ls.net! y' s7 K. G, h( @7 n9 Q
1.python2.7+linux----------------
"""
