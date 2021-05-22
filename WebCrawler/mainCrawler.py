from urllib.request import urlopen
from link_finder import LinkFinder
from Crawler import *
from domain import *

class MainCrawler:
    print("class MainCrawler:")
    project_name=''
    base_url=''
    domain_name=''
    toCrawl_file=''
    crawled_file=''
    toCrawl=set()
    crawled=set()

    def __init__(self,project_name,base_url,domain_name):
        print("__init__(self,project_name,base_url,domain_name):")
        MainCrawler.project_name=project_name
        MainCrawler.base_url=base_url
        MainCrawler.domain_name=domain_name
        MainCrawler.toCrawl_file=MainCrawler.project_name+'/toCrawl.txt'
        MainCrawler.crawled_file=MainCrawler.project_name+'/crawled.txt'
        self.boot()
        self.crawl_page('First Crawler',MainCrawler.base_url)

    @staticmethod
    def boot(): # Create the directory/data files/ starts the basic setup
        print("boot():")
        create_directory(MainCrawler.project_name)
        create_files(MainCrawler.project_name,MainCrawler.base_url)
        MainCrawler.toCrawl= file_to_set(MainCrawler.toCrawl_file)
        MainCrawler.crawled=file_to_set(MainCrawler.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        print("crawl_page(thread_name, page_url):")
        if page_url not in MainCrawler.crawled:
            print(thread_name+'Now crawling '+page_url)
            print('Left to Crawl :'+str(len(MainCrawler.toCrawl))+' | Crawled :'+str(len(MainCrawler.crawled)))
            MainCrawler.add_links_to_queue(MainCrawler.gather_links(page_url))
            MainCrawler.toCrawl.remove(page_url)
            MainCrawler.crawled.add(page_url)
            MainCrawler.update_files()

    @staticmethod
    def gather_links(page_url):
        print("gather_links(page_url):")
        html_data=''
        try:
            res=urlopen(page_url)
            if 'text/html' in res.getheader('Content-Type'):
                html_bytes=res.read()
                html_data=html_bytes.decode('utf-8')
            finder=LinkFinder(MainCrawler.base_url,page_url)
            finder.feed(html_data)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        print("add_links_to_queue(links):")
        for url in links:
            if url in MainCrawler.toCrawl or url in MainCrawler.crawled :
                continue
            if MainCrawler.domain_name!=get_domain_name(url):
                continue
            MainCrawler.toCrawl.add(url)

    @staticmethod
    def update_files():
        print(" update_files():")
        set_to_file(MainCrawler.toCrawl,MainCrawler.toCrawl_file)
        set_to_file(MainCrawler.crawled,MainCrawler.crawled_file)
