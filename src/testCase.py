#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        testCase.py
#
# Purpose:     This module is a test case module used as an example and test 
#              the function of the module <webDownloader.py>
#              
# Author:      Yuancheng Liu
#
# Created:     2024/05/03
# Version:     v_0.1.2
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
#-----------------------------------------------------------------------------

import os
import webDownloader
from urllib.parse import urlparse

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


def testCase(inputfile, outputFolder):
    print("Current working directory is : %s" % os.getcwd())
    dirpath = os.path.dirname(os.path.abspath(__file__))
    print("Current source code location : %s" % dirpath)
    downloader = webDownloader.webDownloader(
        imgFlg=True, linkFlg=True, scriptFlg=True, caFlg=True)
    urlCount = failCount = 0
    print("> load url record file %s" % inputfile)
    with open(os.path.join(dirpath, inputfile)) as fp:
        urllines = fp.readlines()
        for line in urllines:
            if line[0] in ['#', '', '\n', '\r', '\t']:continue  # jump comments/empty lines.
            urlCount += 1
            print("> Process URL {}: {}".format(urlCount, line.strip()))
            if ('http' in line):
                urlStr = line.strip()
                domain = str(urlparse(urlStr).netloc)
                downloadFolderPath = os.path.join(dirpath, outputFolder,
                                                  '_'.join((str(urlCount), domain)))
                result = downloader.downloadWebContents(
                    urlStr, downloadFolderPath)
                if result:
                    print('Finished.')
                else:
                    failCount += 1
    print("\n> Download result: download %s url, %s fail" %
          (str(urlCount), str(failCount)))

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    inputfile = "urlList.txt"
    outputFolder = "outputFolder"
    testCase(inputfile, outputFolder)
