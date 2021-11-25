#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        webAttestation.py
#
# Purpose:     This module is used to do the url/web attestation by using the 
#              Phishperida API. The user can list all the url he wants to check 
#              in the file "urllist.txt" .
#              For each url, the program will do below steps:
#               1. use webDownloader module to download all the web components.
#               2. use webScreenShoter module to get a screenshot of the webpage.
#               3. pass the web components and the screen shot to Phishperida API
#               to do the phishing web/url check. 
#
# Author:      Yuancheng Liu
#
# Created:     2021/11/25
# Version:     v_0.1
# Copyright:   n.a
# License:     n.a
#-----------------------------------------------------------------------------
import os
from urllib.parse import urljoin, urlparse
import webGlobal as gv
import webDownload as webDL
import webScreenShoter as webSS
#import phishpediaPKG as webPH

GV_FLG = True  # Flag to identify whether use gloval value

if GV_FLG:
    import webGlobal as gv
URL_RCD = gv.URL_LIST if GV_FLG else 'urllist.txt'  # file to save url list
RST_DIR = gv.DATA_DIR if GV_FLG else 'datasets'

dlImg = True # download image
dlHref = True # download the components linked by href.
dlScript = True # download java scripts

def main():
    downloader = webDL.urlDownloader(imgFlg=dlImg, linkFlg=dlHref, scriptFlg=dlScript)
    capturer = webSS.webScreenShoter()
    #checker = webPH.phishperidaPKG()
    count = failCount= 0
    if not os.path.exists(RST_DIR): os.mkdir(RST_DIR)
    print("> load url record file %s" %URL_RCD)
    with open(URL_RCD) as fp:
        urllines = fp.readlines()
        for line in urllines:
            if line[0] in ['#', '', '\n', '\r']: continue # jump comments/empty lines.
            count += 1
            print("Process URL {}: {}".format(count, line.strip()))
            if ('http' in line):
                line = line.strip()
                domain = str(urlparse(line).netloc)
                folderName = "_".join((str(count), domain))
                result_d = downloader.savePage(line, folderName)
                result_c = capturer.getScreenShot(line, folderName)
                #result_p = checker.phishperidaCheck(RST_DIR)
                # soup.savePage('https://www.google.com', 'www_google_com')
                if result_d and result_c: 
                    print('Finished.')
                else:
                    failCount +=1
    print("\n>Download result: download %s url, %s fail" %(str(count), str(failCount)))

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
