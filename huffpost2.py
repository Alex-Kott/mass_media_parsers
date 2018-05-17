from bs4 import BeautifulSoup
import requests as req
import pickle



def is_next_page_exists(html):
	soup = BeautifulSoup(html, "lxml")
	a = soup.find('a', class_="yr-next")

	if 'disabled' in a['class']:
		return False
	return True




if __name__ == '__main__':
	url = "https://www.huffingtonpost.com/topic/bitcoin"

	dataset = []
	for i in range(1, 1000):
		headers={
			'Accept-Encoding': 'gzip, deflate, br',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
			}
		response = req.get(url,
							params= {'page': i},
							headers=headers
							)
		
		soup = BeautifulSoup(response.text, "lxml")
		cards = soup.find_all(class_="card")
		for card in cards:
			try:
				card_link = card.find_all(class_="card__link")[0]
				news_url = "https://www.huffingtonpost.com{}".format(card_link['href'])

				news_page = req.get(news_url, headers=headers)
				page_soup = BeautifulSoup(news_page.text, "lxml")
				content_components = page_soup.find_all(class_="content-list-component")

				date = page_soup.find_all(class_="timestamp")[0].span.text

				text = ''
				for component in content_components:
					text += component.text
					
				try:
					entry_text = page_soup.find_all(class_="entry__text")[0]
					ps = entry_text.find_all("p")
					for p in ps:
						text += p.text
				except:
					pass

				if text.strip() == '':
					continue

				dataset.append({
					'url': news_url,
					'date': date,
					'text': text.strip()
					})
			except:
				pass

		if not is_next_page_exists(response.text):
			break

	with open('huffpost.pkl', 'wb') as f:
		pickle.dump(dataset, f)