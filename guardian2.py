import requests as req
from bs4 import BeautifulSoup



if __name__ == "__main__":
	url = "https://www.theguardian.com/technology/bitcoin"
	n = 25
	dataset = []
	for i in range(1, n):
		page = req.get(url, params={'page': i})
		soup = BeautifulSoup(page.text, "lxml")
		lis = soup.find_all("li", class_="u-faux-block-link")
		for li in lis:
			print(li)







		# dataset.append({
		# 	'url': url,
		# 	'date': datetime,
		# 	'text': text
		# 	})

	# with open('bloomberg.pkl', 'wb') as f:
		# pickle.dump(dataset, f)