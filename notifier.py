# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103,C0111
"""Swtich在庫監視君 通知処理"""

import os
import urllib
import urllib2

import env

env.initProduction()

class LineNotifier(object):
    END_POINT = 'https://notify-api.line.me/api/notify'
    HEADER = {"Authorization" : "Bearer " + os.environ['LINE_NOTIFY_TOKEN']}

    def postMessage(self, messageLines):
        params = {'message' : '%0D%0A'.join(messageLines)}
        request = urllib2.Request(
            self.END_POINT,
            urllib.urlencode(params),
            self.HEADER)
        urllib2.urlopen(request)

class SlackNotifier(object):

    END_POINT = 'https://slack.com/api/chat.postMessage'
    BOT_INFO = {
        'username' : "Switchアラート",
        'link_names' : True,
        'icon_url' : 'https://goo.gl/LNxWpR',
        'token' : os.environ['SLACK_TOKEN'],
        'channel' : os.environ['SLACK_CHANNEL_ID'],
    }

    def postMessage(self, message):

        params = self.BOT_INFO.copy()
        params.update(text=message)

        request = urllib2.Request(self.END_POINT, urllib.urlencode(params))
        urllib2.urlopen(request)
