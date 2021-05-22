import threading
from queue import Queue
from mainCrawler import MainCrawler
from domain import *
from Crawler import *

PROJECT_NAME = 'WebsiteCrawler'
HOMEPAGE = 'https://www.uspcldh.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
TOCRAWL_FILE = PROJECT_NAME + '/toCrawl.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NO_OF_THREADS = 8
toCrawl = Queue()
MainCrawler(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def crawl():
    print("crawl():")
    queued_links = file_to_set(TOCRAWL_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' Links are still there to Crawl')
        create_jobs()


def create_jobs():
    print("create_jobs():")
    for link in file_to_set(TOCRAWL_FILE):
        toCrawl.put(link)
        toCrawl.join()
        crawl()


def create_workers():
    print("create_workers():")
    for _ in range(NO_OF_THREADS):  # _ means you don't need any variable
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    print("work():")
    while True:
        url = toCrawl.get()
        MainCrawler.crawl_page(threading.current_thread().name, url)
        toCrawl.task_done()


create_workers()
crawl()