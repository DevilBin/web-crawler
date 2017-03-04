#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from time import sleep
import requests

class spider():

    def __init__(self):
        self.siteURL = "http://www.qiushibaike.com"
        self.result = ""

    def getPage(self, pageIndex):
        url = self.siteURL + "/text/page/" + str(pageIndex) + "?s=4952763"
        sleep(3)
        page = requests.get(url)
        return page

    def getContents(self, pageIndex):
        print("[I]: Page index", pageIndex)
        page = self.getPage(pageIndex)
        if page.status_code == 200:
            pattern = re.compile('<div class="content">(.*?)</div>', re.S)
            items = re.findall(pattern, page.text)
            for item in items:
                pattern = re.compile('<span>(.*?)<.span>', re.S)
                its = re.findall(pattern, item)
                for it in its:
                    self.result += it.replace("<br/>", "\n")
                    self.result += "\n\n\n"
        else:
            print("[E]: Page", pageIndex, "not found.")

    def retContents(self):
        return self.result
