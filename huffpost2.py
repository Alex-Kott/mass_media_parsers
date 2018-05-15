from bs4 import BeautifulSoup
import requests as req



def is_next_page_exists(html):
	soup = BeautifulSoup(html, "lxml")
	a = soup.find('a', class_="yr-next")

	if 'disablesd' in a['class']:
		return False
	return True




if __name__ == '__main__':
    url = "https://www.huffingtonpost.com/topic/bitcoin"

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
    	# print(result.text)
    	soup = BeautifulSoup(response.text, "lxml")
    	cards = soup.find_all(class_="card")
    	for i in cards:
    		print(i)

    	if not is_next_page_exists(response.text):
    		break
