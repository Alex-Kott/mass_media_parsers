import requests as req
import json
from bs4 import BeautifulSoup
import pickle




if __name__ == "__main__":
	dataset = []
	r = req.get("https://www.rbc.ru/search/ajax/?project=rbcnews&offset=0&limit=10000&query=биткоин")
	data = json.loads(r.text)
	for item in data['items']:
		page_source = req.get(item['fronturl']).text
		news_page = BeautifulSoup(page_source, "lxml")
		try:
			article_text_container = news_page.find_all(class_="article__text")[0]
		except:
			continue

		text = ''
		for p in article_text_container.find_all('p'):
			text += p.text
		
		dataset.append({
			'url': item['fronturl'],
			'date': item['publish_date'],
			'text': text
			})

	with open('rbc.pkl', 'wb') as f:
		pickle.dump(dataset, f)