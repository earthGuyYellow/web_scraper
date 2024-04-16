import requests
from bs4 import BeautifulSoup
import pprint

'''Loop through multiple pages adding the page index to url as string,
then use beautiful soup module to convert link to text and pass through to HTML parser,
shortly after the soup.select attribute is assigned to select the hyperlinked urls. 
The subtext class is assigned to select the votes. 

'''
for page in range(1,6):
	res = requests.get('https://news.ycombinator.com/news?p=' + str(page))
	soup = BeautifulSoup(res.text, 'html.parser')
	links = soup.select('.titleline > a')
	subtext_class = soup.select('.subtext')

def create_custom_hackernews(links, subtext_class):
	hackn = []
	
	for index,item in enumerate(links):
		headline_title = links[index].getText()
		href = links[index].get('href',None)
		vote = subtext_class[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hackn.append({'Headline Title':headline_title, 'link':href, 'votes': points})

	return sorted(hackn, key= lambda x:x['votes'], reverse=True)
	

pprint.pprint(create_custom_hackernews(links,subtext_class))