import requests as req
from bs4 import BeautifulSoup



if __name__ == "__main__":
	url = "https://www.bloomberg.com/search"
	n = 430
	for i in range(1, n):
		params = {
			'query': 'bitcoin',
			'page': n
		}
		page = req.get(url, params=params)
		soup = BeautifulSoup(page.text, "lxml")

		for item in soup.find_all(class_="search-result"):
			try:
				url = item.find_all("a")
				print(url)
			except:
				# print(item)
				pass