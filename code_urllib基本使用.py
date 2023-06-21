url="http://www.baidu.com"
url1='https://www.baidu.com'
import urllib.request
# response=urllib.request.urlopen(url)
# headers=response.getheaders()
# raw=response.read()
page=urllib.request.urlretrieve(url,'baidu.html')
print(page)
