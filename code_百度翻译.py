import urllib.request
import urllib.parse
headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'Accept-Encoding':'gzip,deflate,br',
'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'BIDUPSID=70DEE038AA493F6D2BF582BD657546C1;PSTM=1653758857;BD_UPN=12314753;BDUSS=ZSZzR3MmNPTDFFLVZUcGVNanQ2dGljUk44TXRhRkFNZ0t4bkpXeEh0QlZ-UUJqSVFBQUFBJCQAAAAAAAAAAAEAAACVg~8AZ2FzdGF0aW9uAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFVw2WJVcNliT3;BDUSS_BFESS=ZSZzR3MmNPTDFFLVZUcGVNanQ2dGljUk44TXRhRkFNZ0t4bkpXeEh0QlZ-UUJqSVFBQUFBJCQAAAAAAAAAAAEAAACVg~8AZ2FzdGF0aW9uAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFVw2WJVcNliT3;BAIDUID=52E7159B72EB6C732DDFE1B562A74EEC:FG=1;MCITY=-179%3A;ispeed_lsm=2;SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04180142933RXWkpfSn2dWQw2Ra03X%2F17GCeMn4FKyM3jQwVccM6NwjQIGfQ3YXSFlJ3LRixt1A1EoUeSo1cvP50dHNupHjVCbTQ%2Bux3ilRTBwAZWho5vM2%2FPfHajDoy6VvnpWHCOPBf2bTGjpFlONj3mfkYLYoUNROwY893EV7Z4mfB9wr8aYuZHdJEp4kW7fGI0lZBjxWgVcHd%2Bv54Y3%2BQJu%2BWB%2FyQHGstxJ9jN1nibMPm7HfkfbpJ0JJ1Tbf2cHvY3joEtb%2B5UgrAHtAHyETyy8QpZKAeQ%3D%3D64521690524201950899061353450551;BA_HECTOR=802h210g240g0k0l048h24sl1hmorrq1e;ZFY=oRSrJRLoT1Jehb5GjI4NfwHSL82F46slkhFlKKCrkCY:C;BAIDUID_BFESS=52E7159B72EB6C732DDFE1B562A74EEC:FG=1;Hm_lvt_aec699bb6442ba076c8981c6dc490771=1668050820;___wk_scode_token=JgEOBq6Dppf0w7fJYZKG8fzvz1g41nQF%2FLNb7iHoEeE%3D;delPer=0;BD_CK_SAM=1;PSINO=3;COOKIE_SESSION=104_0_8_8_8_14_1_0_8_7_5160_1_112_0_28_0_1668050941_0_1668050913%7C9%230_0_1668050913%7C1;BDRCVFR[HgW6KFoRztb]=mk3SLVN4HKm;Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1668051329;B64_BOT=1;BDRCVFR[r3VqGGrxDQ3]=mk3SLVN4HKm;BD_HOME=1;BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0;H_PS_PSSID=36561_37521_37626_37534_37497_37742_26350_37478;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;baikeVisitId=9b674a62-c9b1-4c13-8798-dbb3b6e01996;BDSVRTM=24',
'Host':'www.baidu.com',
'sec-ch-ua':'"NotA;Brand";v="99","Chromium";v="102","GoogleChrome";v="102"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'Sec-Fetch-Dest':'document',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/102.0.0.0Safari/537.36',
}
# url_byte="https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&rsv_spt=1&rsv_iqid=0x994a94b400056737&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=1549&rsv_sug4=1549"
url_base="https://www.baidu.com/s?"
data={'wd':'周杰伦','gender':'male','location':'中国台湾'}
data_new=urllib.parse.urlencode(data)
url=url_base+data_new
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
raw=response.read().decode('utf-8')