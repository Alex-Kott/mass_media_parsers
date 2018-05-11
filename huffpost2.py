from bs4 import BeautifulSoup
import requests as req



def is_next_page_exists(html):
	soup = BeautifulSoup(html, "lxml")
	a = soup.find('a', class_="disabled")
	print(a)

	return True




if __name__ == '__main__':
    url = "https://www.huffingtonpost.com/topic/bitcoin"

    for i in range(1, 1000):
    	headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'deflate'}
    	result = req.get(url, headers=headers)
    	# print(result.url)
    	# html = result.text

    	# if not is_next_page_exists(html):
    		# break
