import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import math
import random
from textblob import TextBlob
import csv

def constantTimer(min, max):
	return math.floor(random.randint(min,max)) + min

def processTweet(tweet):  
    text = tweet.find_element_by_class_name('tweet-text').text.encode('ascii', 'ignore')
    date = tweet.find_element_by_class_name('tweet-timestamp').get_attribute('title')
    blob = TextBlob(text)
    sentiment = blob.sentiment

    res = {'tweet': text, 'date': date, 'sentiment': sentiment.polarity}

    return res

#change directory accordingly. Also make sure the right driver is being used
browser = webdriver.PhantomJS(r'C:\Users\Class2018\Desktop\J&J\twitterApp\Remicade-Twitter-Project\phantomjs-2.1.1-windows\bin\phantomjs.exe')
query = u'remicade'
base_url = u'https://twitter.com/search?f=tweets&vertical=default&q=' + query + '%20lang%3Aen&src=typd'

browser.get(base_url)

body = browser.find_element_by_css_selector('body')

lastHeight = browser.execute_script("return document.body.scrollHeight")

startTime = time.time()
lastHeight = browser.execute_script("return document.body.scrollHeight")
footer = browser.find_element_by_class_name("timeline-end")
print(lastHeight)
while True:
    browser.execute_script("arguments[0].scrollIntoView()", footer)
    timer = constantTimer(1,3)
#    print(timer)
    time.sleep(2)
    newHeight = browser.execute_script("return document.body.scrollHeight")
    print(newHeight)
    if newHeight == lastHeight or time.time() - startTime > (15 * 60):
        browser.execute_script("arguments[0].scrollIntoView()", footer)
        print('rescrolling 1')
        time.sleep(10)
        browser.execute_script("arguments[0].scrollIntoView()", footer)
        print('rescrolling 2')
        time.sleep(10)
        browser.execute_script("arguments[0].scrollIntoView()", footer)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        print(newHeight)
        if newHeight == lastHeight:
            break
    lastHeight = newHeight

tweets = browser.find_elements_by_class_name('js-stream-tweet')

results = []

for tweet in tweets:
    results.append(processTweet(tweet))
    
print(results[len(results) - 1])
print(time.time() - startTime)
    
with open('out.csv', 'wb') as f:
    w = csv.DictWriter(f, results[0].keys())
    w.writeheader()
    for res in results:
        w.writerow(res)
        
        
    
browser.quit()
