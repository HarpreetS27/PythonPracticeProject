from urllib.parse import urlparse

url=r"https://www.stackoverflow.com/questions/53992694/what-does-netloc-mean"
def get_domain_name(url):
    try:
        result=get_sub_domain_name(url).split('.')
        #print(len(result))
        if len(result)>3:
            print("Domain Name:"+result[1]+'.'+result[2]+'.'+result[3])
            return result[1]+'.'+result[2]+'.'+result[3]
        else:
            print("Domain Name:"+result[-2]+'.'+result[-1])
            return result[-2]+'.'+result[-1]
    except:
        return ''


def get_sub_domain_name(url):
    try:
        print("Sub Domain Name: "+urlparse(url).netloc)
        return urlparse(url).netloc
    except:
        return ''

get_sub_domain_name(url)
get_domain_name(url)