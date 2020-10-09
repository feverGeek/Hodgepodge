import multipost
import request 
import re

URL = "http://stool.chinaz.com"

def get_sites(target):
    url = URL + "/same?s=" + target
    res = request.get(url)
    pattern = re.compile("<a.*?href=\"(.*?)\".*?rel=\"nofollow\">\d+</a>")
    pages = pattern.findall(res.text)
    for p in pages:
        pass  


if __name__ == '__main__':
    target = "bbs.wghostk.com"
    get_sites(target)
