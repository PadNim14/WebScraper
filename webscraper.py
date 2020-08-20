import requests
from bs4 import BeautifulSoup
import json

url = 'http://ethans_fake_twitter_site.surge.sh/'
respsone = requests.get(url, timeout=5)
content = BeautifulSoup(respsone.content, "html.parser")
# print(content)
# tweet = content.findAll('p', attrs={"class": "content"})

tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text.encode('utf-8'),
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text.encode('utf-8'),
        "tweet": tweet.find('p', attrs={"class": "content"}).text.encode('utf-8'),
        "likes": tweet.find('p', attrs={"class": "likes"}).text.encode('utf-8'),
        "shares": tweet.find('p', attrs={"class": "shares"}).text.encode('utf-8')
    }
    print(tweetObject)
    # tweetArr.append(tweetObject)
    # with open('twitterData.json', 'w') as outfile:
    #     json.dump(tweetArr, outfile)