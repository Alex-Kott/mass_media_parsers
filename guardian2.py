import requests as req
from bs4 import BeautifulSoup
import pickle



if __name__ == "__main__":
	url = "https://www.theguardian.com/technology/bitcoin"
	n = 25
	dataset = []
	for i in range(2, n):
		page = req.get(url, params={'page': i})
		soup = BeautifulSoup(page.text, "lxml")
		lis = soup.find_all("li", class_="u-faux-block-link")
		for li in lis:
			news_url = li.a['href']
			news_page = req.get(news_url)
			news_soup = BeautifulSoup(news_page.text, "lxml")

			try:
				text = ''
				content = news_soup.find(class_="content__article-body")
				for p in content.find_all("p"):
					text += p.text
			except:
				continue

			datetime = news_soup.find("time")['datetime']
			
			dataset.append({
				'url': news_url,
				'date': datetime,
				'text': text
				})

	with open('guardian.pkl', 'wb') as f:
		pickle.dump(dataset, f)