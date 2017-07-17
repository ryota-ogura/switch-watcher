# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103,C0111
"""Swtich在庫監視君"""

import crawlers
import notifier

# 動かすクローラー
execCrawlers = [
    crawlers.Yodobashi(),
    crawlers.MyNintendo()
]

# 通知先
slack = notifier.SlackNotifier()

for crawler in execCrawlers:
    for url in crawler.urls:
        if crawler.hasStock(crawlers.getContent(url)):
            slack.postMessage("@r-ogura\n" + crawler.name + " 在庫あり！ : " + url)
