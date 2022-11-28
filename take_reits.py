import requests
import pandas as pd

url = 'https://www.fundamentus.com.br/fii_resultado.php'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

df = pd.read_html((requests.get(url, headers=header).text).replace('.', '').replace(',','.'))[0]

df['Dividend Yield'] = df['Dividend Yield'].apply(lambda x: x.replace('%', '')).astype('float')
df['Vacância Média'] = df['Vacância Média'].apply(lambda x: x.replace('%', '')).astype('float')
df['Cap Rate'] = df['Cap Rate'].apply(lambda x: x.replace('%', '')).astype('float')



Preco_Teto = df['Cotação']/df['P/VP']
df.insert(2,"Preco_Teto",Preco_Teto)
df = df.loc[(df['P/VP'] >= 0.4) & (df['P/VP'] <= 1) & (df['Dividend Yield'] > 6) & (df['Vacância Média'] <= 15) & (df['Liquidez'] >= 2000000)] # & (df['Cap Rate'] >= 5) | (df['Cap Rate'] == 0)]
df = df.sort_values(['P/VP'], ascending = True)
#df = df.loc[(df['Papel'] == "BTCR11")]
print(f"""{df}""")






