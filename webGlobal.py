#-----------------------------------------------------------------------------
# Name:        webGlobal.py
#
# Purpose:     This module is used as a local config file to set constants, 
#              global parameters which will be used in the other modules.
#              
# Author:      Yuancheng Liu
#
# Created:     2020/11/24
# Copyright:   YC @ Singtel Cyber Security Research & Development Laboratory
# License:     YC
#-----------------------------------------------------------------------------
import os

print("Current working directory is : %s" % os.getcwd())
dirpath = os.path.dirname(__file__)
print("Current source code location : %s" % dirpath)
APP_NAME = 'WebAttestation_v0.1'

URL_LIST = os.path.join(dirpath , "urllist.txt")
DATA_DIR = os.path.join(dirpath , "datasets")
BROWSER_DRIVER_W = os.path.join(dirpath ,'drivers' ,"chromedriver.exe")
BROWSER_DRIVER_L = os.path.join(dirpath ,'drivers' ,"chromedriver")