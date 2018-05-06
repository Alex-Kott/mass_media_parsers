import requests as req
from bs4 import BeautifulSoup


def parse_articles(page):
	news = []
	soup = BeautifulSoup(page, "lxml")
	for listing_column in soup.find_all(class_="listing__column"):
		link = listing_column.find_all(class_="link")[0]
		url = "https://russian.rt.com{}".format(link['href'])
		r = req.get(url)

		news_page = BeautifulSoup(r.text, "lxml")
		try:
			article_text = news_page.find_all(class_="article__text")[0]
			article_date = news_page.find_all(class_="article__date")[0]
			news.append({
				'url': url,
				'date': article_date.text.strip(),
				'text': article_text.text.strip()
				})
		except:
			pass

	return news



if __name__ == "__main__":
	dataset = []
	url = "https://russian.rt.com/search"
	params = {
		'q': 'биткоин',
		'type': '',
		'df': '2000-01-01',
		'dt': '2018-12-12',
		'page': 1
	}
	for i in range(30):
		params['page'] = i
		r = req.get(url, params=params)
		dataset.extend(parse_articles(r.text))


	with open('rt.pkl', 'wb') as f:
		pickle.dump(dataset, f)