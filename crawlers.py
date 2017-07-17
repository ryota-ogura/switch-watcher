# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103,C0111
"""Swtich在庫監視君 クローラー定義"""

import urllib2
import re

class Yodobashi(object):
    """yodobashi.comクローラー"""
    name = 'Yodobashi.com'
    urls = [
        'http://www.yodobashi.com/product/100000001003431566/',
        'http://www.yodobashi.com/product/100000001003431565/'
    ]
    def hasStock(self, content):
        # buyBtn があれば在庫あり
        return re.search(r'buyBtn', content) is not None

    def heartBeat(self):
        return self.hasStock(getContent('https://goo.gl/sdSke8'))

class MyNintendo(object):
    """MyNintendoクローラー"""
    name = 'マイニンテンドー'
    urls = [
        'https://store.nintendo.co.jp/category/NINTENDOSWITCH/'
    ]
    def hasStock(self, content):
        # soldout が無ければ在庫あり
        return re.search(r'soldout', content) is None

    def heartBeat(self):
        return self.hasStock(getContent(self.urls[0])) is False

def getContent(url):
    """UAを指定して指定のURLコンテンツをフェッチする"""
    headers = {
        "User-Agent" : (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/59.0.3071.115 Safari/537.36')
    }
    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    return response.read()
