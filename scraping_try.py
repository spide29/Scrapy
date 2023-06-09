# from bs4 import BeautifulSoup
# import requests
# r=requests.get("https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers")
# soup=BeautifulSoup(r.content,"html.parser")
# div_text=soup.find("div",{"class":"_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-small__nleKL"}).get_text()
# print(div_text)


# import requests
# from bs4 import BeautifulSoup

# handle_httpstatus_list = [400]

# headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
# handle_httpstatus_list = [403, 404]
# allowed_domains = ['bet365.it']
# url = "https://www.bet365.it"
# html = requests.get(url).text

# soup = BeautifulSoup(html, 'lxml')

# elements = soup.select('rcl-ParticipantFixtureDetailsTeam_TeamName ')



# for element in elements:
#     print(element.text)

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.cnil.fr/en/actualite"
html = requests.get(url).text

soup = BeautifulSoup(html, 'lxml')

elements = soup.select('._p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf._p13n-zg-nav-tree-all_style_zg-browse-height-small__nleKL')

data = []
for element in elements:
    data.append(element.text)

df = pd.DataFrame({'text': data})
df.to_excel('output.xlsx', index=False)




