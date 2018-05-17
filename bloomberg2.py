import requests as req
from bs4 import BeautifulSoup
import pickle


if __name__ == "__main__":
	url = "https://www.bloomberg.com/search"
	n = 430
	dataset = []
	for i in range(1, n):
		params = {
			'query': 'bitcoin',
			'page': i
		}
		page = req.get(url, params=params)
		soup = BeautifulSoup(page.text, "lxml")

		for item in soup.find_all(class_="search-result"):
			h1 = item.find("h1")
			url = h1.a['href']

			news_page = req.get(url)
			news_soup = BeautifulSoup(news_page.text, "lxml")
			article_timestamp = news_soup.find("time", class_="article-timestamp")
			datetime = article_timestamp['datetime']

			text = ''
			fence_body = news_soup.find("div", class_="fence-body")
			for p in fence_body.find_all("p"):
				text += p.text

		dataset.append({
			'url': url,
			'date': datetime,
			'text': text
			})

	with open('bloomberg.pkl', 'wb') as f:
		pickle.dump(dataset, f)