import requests as req
import json
from bs4 import BeautifulSoup
import pickle


def parse_article(url):
	r = req.get(url)
	soup = BeautifulSoup(r.text, "lxml")
	text = ''
	text_container = soup.find_all(class_="b-text")[0]
	for p in text_container.find_all("p"):
		text += p.text

	date = soup.find_all(class_="g-date")[0]

	return date, text



if __name__ == "__main__":
	dataset = []
	url = "https://lenta.ru/search/v2/process"
	params = {
		'from': 0,
		'size': 9999,
		'sort': 2,
		'title_only': 0,
		'domain': 1,
		'query': 'биткоин'
	}
	r = req.get(url, params=params)
	data = json.loads(r.text)
	for item in data['matches']:
		date, text = parse_article(item['url'])
		dataset.append({
			'url': item['url'],
			'date': date,
			'text': text
			})


	with open('lenta.pkl', 'wb') as f:
		pickle.dump(dataset, f)