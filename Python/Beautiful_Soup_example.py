#BeautifulSoup example

from bs4 import BeautifulSoup
import urllib2

redditFile = urllib2.urlopen("http://www.reddit.com")
redditHtml = redditFile.read()
redditFile.close()

#Creating a BeautifulSoup object
#To create a soup object of the content of the url we passed in.
soup = BeautifulSoup(redditHtml)
#Finds all descendants that match your filters.
redditAll = soup.find_all("a")
#Within the <a> tag, the href attribute specifies the URL of the page the
#link goes to.
for links in soup.find_all('a'):
    print (links.get('href'))
