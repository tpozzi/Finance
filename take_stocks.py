import requests
import pandas as pd

url = 'https://www.fundamentus.com.br/resultado.php'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

df = pd.read_html((requests.get(url, headers=header).text).replace('.', '').replace(',','.'))[0]

df['DivYield'] = df['DivYield'].apply(lambda x: x.replace('%', '')).astype('float')
df['ROE'] = df['ROE'].apply(lambda x: x.replace('%', '')).astype('float')


Preco_Teto = df['Cotação']/df['P/VP']
df.insert(2,"Preco_Teto",Preco_Teto)
df = df.loc[(df['P/VP'] >= 0.4) & (df['P/VP'] <= 1.2) & (df['DivYield'] > 6) & (df['ROE'] >= 15) & (df['Liq2meses'] >= 2000000)]
df = df.sort_values(['P/VP'], ascending = True)

print(f"""{df}""")






