#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        webScreenShoter.py
#
# Purpose:     This module will use different brower driver API to capture the
#              webpage's screen shot based on the given url. The user can list
#              all the  url he wants to downlad in the file "urllist.txt" .
#
# Author:      Yuancheng Liu
#
# Created:     2021/11/23
# Version:     v_0.1
# Copyright:   n.a
# License:     n.a
#-----------------------------------------------------------------------------
import os
import sys
from time import sleep
from PIL import Image
from urllib.parse import urljoin, urlparse
from selenium import webdriver

GV_FLG = True  # Flag to identify whether use gloval value

if GV_FLG:
    import webGlobal as gv
URL_RCD = gv.URL_LIST if GV_FLG else 'urllist.txt'  # file to save url list
RST_DIR = gv.DATA_DIR if GV_FLG else 'datasets'

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


class webScreenShoter(object):

    def __init__(self, driverType="C"):
        #browser exposes an executable file
        #Through Selenium test we will invoke the executable file which will then
        #invoke actual browser
        self.driverPath = None

        if sys.platform.startswith('win'):
            self.driverPath = gv.BROWSER_DRIVER_W if GV_FLG else "chromedriver.exe"
        else:
            self.driverPath = gv.BROWSER_DRIVER_L if GV_FLG else "chromedriver"

    def getScreenShot(self, url, folderName):
        driver = webdriver.Chrome(executable_path=self.driverPath)
        driver.get(url)
        # wait one second to let the browser to show the whole webpage
        sleep(1)
        filepath = os.path.join(RST_DIR, folderName, "shot.png")
        #print("path:"+filepath)
        driver.get_screenshot_as_file(filepath)
        driver.quit()
        driver = None
        print("Finished...")
        return True

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


def main():
    soup = webScreenShoter()
    if not os.path.exists(RST_DIR):
        os.mkdir(RST_DIR)
    count = failCount = 0
    print("> load url record file %s" % URL_RCD)
    with open(URL_RCD) as fp:
        urllines = fp.readlines()
        for line in urllines:
            if line[0] in ['#', '', '\n', '\r']:
                continue  # jump comments/empty lines.
            count += 1
            print("Process URL {}: {}".format(count, line.strip()))
            if ('http' in line):
                line = line.strip()
                domain = str(urlparse(line).netloc)
                folderName = "_".join((str(count), domain))
                filepath = os.path.join(RST_DIR, folderName)
                if not os.path.exists(filepath):
                    os.mkdir(filepath)
                result = soup.getScreenShot(line, folderName)
                #soup.savePage('https://www.google.com', 'www_google_com')
                if result:
                    print('Finished.')
                else:
                    failCount += 1
    print("\n>Download result: download %s url, %s fail" %
          (str(count), str(failCount)))


#-----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
