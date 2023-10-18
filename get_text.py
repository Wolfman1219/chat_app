from bs4 import bs4
import urllib

url = "https://openai.com/blog/chatgpt-can-now-see-hear-and-speak"
a_website = urllib.request.urlopen(url)

a_soup = bs4.BeautifulSoup(a_website)

website_text = a_soup.findAll(text = True)


print(website_text)