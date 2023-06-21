import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'
url1 = 'https://www.baidu.com/s?wd='+urllib.parse.quote('周杰伦')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
request = urllib.request.Request(url=url1, headers=headers)
response = urllib.request.urlopen(request)
