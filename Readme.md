# Web Downloader



#### Introduction 

This module will provide API to download the webpage components :  html file, image file, css fil,  javascript file, href link file based on the input url (the url must start with 'http' or 'https' ). 

To prosses multiple URLs at the same time, The user can list all the url he wants to download  in the file "urllist.txt" as shown below: 

```
# Add the URL you want to download line by line(The url must start with 'http' or 'https' ):
# example: https://www.google.com
https://www.google.com
https://www.carousell.sg/
https://www.google.com/search?q=github&sxsrf=AOaemvJh3t5_h8H85AE8Ajbb1IMnBrRISA%3A1636698503535&source=hp&ei=hwmOYY6mHdGkqtsPq8S9sAY&iflsig=ALs-wAMAAAAAYY4Xl7GLWS16_xc2Q9XrG0p3q277DpkL&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzINCC4QxwEQowIQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1AAWABgjgdoAXAAeACAAQCIAQCSAQCYAQCwAQo&sclient=gws-wiz
https://stackoverflow.com/questions/66022042/how-to-let-kubernetes-pod-run-a-local-script/66025424
```



------

#### Program Setup

###### Development Environment : python 3.7.4

###### Additional Lib/Software Need

1. **beautifulsoup4 4.10.0**

   install:

   ```
   pip install beautifulsoup4
   ```

   Lib link: https://pypi.org/project/beautifulsoup4/

2. 

###### Hardware Needed : None



------

#### Program Usage

###### Module API Usage

1. Downloader init: 

```
soup = urlDownloader(imgFlg=True, linkFlg=True, scriptFlg=True)
```

- imgFlg: Set to "True" to download all the "<img>" tag files. 
- linkFlg: Set to "True" to download all the html section, image, icon, css file imported by  "<href>"
- scriptFlg: set to "True" to download  all the js file. 

2. Call API method savePage to scape url and save the data in a folder 

   ```
   soup.savePage('<url>', '<folder_name>')
   
   # Exampe:
   soup.savePage('https://www.google.com', 'www_google_com')
   ```

3.  



###### Program Execution 

1. Copy the url you want to check in the url record file "**urllist.txt**"

2. Cd to the program folder and run program execution cmd: 

   ```
   python webDownload.py
   ```

3. Check the result: 

   For example, if you copy the url "https://www.carousell.sg/" as the first url you want to check into the file "urllist.txt" file, all the html files, image file and js files will be under folder "1_www.carousell.sg_files"

   - The main web page will be saved as:  "1_www.carousell.sg_files/1_www.carousell.sg.html"
   - The image used in the page will be saved in folder: "1_www.carousell.sg_files/img"
   - The html/imge/css import by href will be saved in folder: "1_www.carousell.sg_files/link"
   - The js file used by the page will be saved in fodler: "1_www.carousell.sg_files/script"



------

> Last edit by LiuYuancheng(liu_yuan_cheng@hotmail.com) at 13/11/2021

