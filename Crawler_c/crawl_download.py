from bs4 import BeautifulSoup
import requests
import gzip
import pymysql
import datetime

URL = 'https://lenta.ru/robots.txt'

'''
urls = [
    'https://lenta.ru/robots.txt',
    'https://gazeta.ru/robots.txt',
    'https://bfm.ru/robots.txt',
    'https://vz.ru/robots.txt',
    'https://lenta.ru/sitemap.xml',
    'https://lenta.ru/news/sitemap2.xml.gz',
    'https://gazeta.ru/sitemap.xml',
    'https://bfm.ru/sitemap.xml',
    'https://lenta.ru/news/2012/05/16/devour/',
    'https://vz.ru/sitemap.xml',
]
'''
# Списки соответсвующие таблицам
keywordsList = [] # Список ключевых слов
sitesList = [
	{'ID': 1, 'Name': 'lenta.ru'},
	{'ID': 2, 'Name': 'gazeta.ru'},
]  # Список сайтов
pagesList = [] # Список страниц
personalpagerankList = []  # Список рейтингов

'''
# Состав данных
keywordDict = {'ID': None, 'Name': None, 'PersonID': None}  #Структура ID -> int, Name -> str, PersonID -> int
sitesDict = {'ID': 1, 'Name': 'lenta.ru'}
sitesDict = {'ID': None, 'Name': None}  # Cтруктура ID -> int, Name -> str
pagesDict = {'ID': None, 'Url': None, 'SiteID': None, 'FoundDateTime': None,
             'LastScanDate': None}  # Структура ID -> int, Url -> str, Siteid -> int, FoundDateTime -> datetime, LastScanDate-> datetime
personalpagerankDict = {'ID': None, 'PageID': None,
                        'Rank': None}  # Структура PersonID -> int, PageID -> int, Rank -> int
'''


def get_html(url):
    '''
    Скачивает страницу по заданному адресу (url)
    '''
    resp = requests.get(url)
    head = resp.headers
    if resp.status_code == requests.codes.ok:
        if head['Content-Type'] == 'application/octet-stream':
            return gzip.decompress(resp.content)
        else:
            return resp.text
    else:
        return resp.status_code


def get_url(sites):
    '''
	Читает данные по сайтам (sites) и записыает строку pages
	'''


def write_robots(sitesLst, pagesLst):
    lst = []
    for i in sitesLst:
        print('ID: ', i['ID'])

        if len(pagesLst) == 0:
            print(i['Name'])
            url = '/'.join(['https:/', i['Name'], '/robots.txt'])
            lst.append({'ID': len(pagesLst), 'Url': url, 'SiteID': i['ID'], 'FoundDateTime': datetime.datetime.now(), 'LastScanDate': None})     	
        else:    
            for item in pagesLst:
                print('SiteID: ', item['SiteID'])
                if item['SiteID'] == i:
                    continue
                else:
                    print(i['Name'])
                    url = '/'.join(['https:/', i['Name'], '/robots.txt'])
                    lst.append({'ID': len(pagesLst), 'Url': url, 'SiteID': i['ID'], 'FoundDateTime': datetime.datetime.now(), 'LastScanDate': None})
                    print(len(pagesLst))
    return lst


def read_robots(name):
    pass


def read_html(url):
    pass


def sitemap(html):
    soup = BeautifulSoup(html, 'lxml')
    for url in soup.find_all('loc'):
        yield url

        # st = [url.text for url in soup.find_all('loc')]
        # return st


def db_write_sitemap():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='ratepersons',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()


def main():
    lst = write_robots(sitesList, pagesList)
    pagesList.extend(lst)
    print(pagesList)
    # print(get_html(URL))
    # for url in urls[:8]:
    #    print('headers for {}'.format(url), get_headers(url)['Content-Type'].split(';')[0])
    # print(sitemap(get_html(URL)))
    # print(get_html(urls[3]))
    # print(len(sitemap(get_html(URL))))
    # print(len(sitemap(get_html('https://lenta.ru/article/sitemap.xml'))))
    # print([(i, site) for i, site in enumerate(sitemap(get_html(URL)))])
    # print(sitemap(get_content(URL)))


if __name__ == '__main__':
    main()