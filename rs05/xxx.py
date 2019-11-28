import requests
from bs4 import BeautifulSoup
import time


movie_name_list = []


def download_page(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
	}
	data = requests.get(url,headers=headers).content
	return data

def main():
	for num in range(374,1174):
		time.sleep(3)
		xxx=download_page("http://www.rs05.com/movie/?p="+str(num))
		#print(xxx)
		
		soup = BeautifulSoup(xxx)
		for movie_li in soup.find_all('div', attrs={'class': 'brief'}):
			movie_name = movie_li.getText()
			#movie_name_list.append(movie_name)	
			#print(movie_name)
			a=open('test.txt', 'a',encoding='utf-8')
			a.write(movie_name+"\n")
			a.close()



if __name__ == '__main__':
	main()