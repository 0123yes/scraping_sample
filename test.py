import bs4
import requests

res = requests.get('https://cookpad.com/')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# <title>の情報を取得
title_tag = soup.title
print(title_tag.text)  # レシピ検索No.1／料理レシピ載せるなら クックパッド  # .textでテキストだけ抽出

# divタグをすべて取得
# div_tags = soup.find_all("div")  # HPであったdiv
# div_tag_texts = [div_tag.text for div_tag in div_tags]
# print(div_tag_texts)

# left_containerを検索
# tags = soup.find_all("div", class_="left_container")  # 
# tag_texts = [tag.text for tag in tags]
# print(tag_texts)

tags = soup.find("div", class_="left_container")  # HPであったdiv
a_tag = tags.find("a")
url = f"https://cookpad.com{a_tag.attrs['href']}"
print(url)
