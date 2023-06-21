from bs4 import BeautifulSoup
import urllib3
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def google(query):
    global soup
    query = query.replace(" ","+")
    try:
        url = f'https://www.youdao.com/result?word={query}&lang=en'
        http=urllib3.PoolManager()
        res= http.request('GET',url,headers=headers)
        soup = BeautifulSoup(res.data,'html.parser')
    except:
        print("Make sure you have a internet connection")
    try:
        try:
            ans = soup.select('.RqBzHd')[0].getText().strip()
        except:
            try:
                title=soup.select('.AZCkJd')[0].getText().strip()
                try:
                    ans=soup.select('.e24Kjd')[0].getText().strip()
                except:
                    ans=""
                ans=f'{title}\n{ans}'
            except:
                try:
                    ans=soup.select('.hgKElc')[0].getText().strip()
                except:
                    ans=soup.select('.kno-rdesc span')[0].getText().strip()
    except:
        ans = "can't find on google"
    return ans
result = google(str(input("Query\n")))
print(result)