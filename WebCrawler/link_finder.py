from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):  # Inherited HTMLParser class
    print(" LinkFinder(HTMLParser):")
    def __init__(self, base_url, page_url):
        print("__init__(self, base_url, page_url):")
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        print(" def error(self, message):")
        pass

    def handle_starttag(self, tag, attrs):
        print("handle_starttag(self, tag, attrs):")
        if tag=='a': # href are inside anchor tag so just check for a tag
            for(attribute,value) in attrs: # attribute is type of tag, value is actual content
                if attribute=='href': # check for href in content
                    url=parse.urljoin(self.base_url,value) #make full url by adding value to base url
                    self.links.add(url) # add to our set

    def page_links(self):
        print("page_links(self):")
        return self.links
