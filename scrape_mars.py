# import dependencies

import requests
import pymongo
import pandas as pd

from splinter import Browser
from bs4 import BeautifulSoup
import time


# open chrome driver browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

# ## NASA Mars News 

def scrape():
    browser = init_browser()
    
    mars_news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'"
    browser.visit(mars_news_url)

    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')

    titles = mars_news_soup.body.find("div", class_="content_title").text

    paras = mars_news_soup.body.find("div", class_="article_teaser_body").text


    # ## Mars Space Images

    time.sleep(3)

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(image_url)

    html = browser.html
    
    soup = BeautifulSoup(html, 'html.parser')
    
    image = soup.find('article', class_='carousel_item')

    image_url  = soup.find('article')['style']

    image_url= image_url.replace("background-image: url('", '') 
    
    image_url= image_url.replace("');", "") 
    
    full_image_url = "https://www.jpl.nasa.gov" + image_url

    full_image_url 

    #browser.click_link_by_id('full_image')

    #browser.click_link_by_partial_text('more info')

    #image_html = browser.html
    #mars_image_soup = BeautifulSoup(image_html, 'html.parser')
    
    #image = mars_image_soup.body.find("figure", class_="lede")

    #link = image.find('a')
    #href = link['href']

    #base_url='https://www.jpl.nasa.gov'

    #featured_image_url = base_url + href

    #featured_image_url

    # ## Mars Weather

    
    #time.sleep(3)

    #weather_url = "https://twitter.com/marswxreport?lang=en"
    #browser.visit(weather_url)

    #html = browser.html
    #mars_weather_soup = BeautifulSoup(html, 'html.parser')

    #weather_tweet = soup.find_all('div', class_='css-1dbjc4n')
    
    #weather_tweet[2].find('span')
    
    #weather_tweet[0].find('section', class_='css-1dbjc4n')
    
    #tweet_braket=weather_tweet[0].find('div',class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
    
    # tweet_braket1=tweet_braket.find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    
    # tweet=tweet_braket1.getText()

    # find the tweet text

    #tweet_container = mars_weather_soup.body.find('div','js-tweet-text-container')

    #mars_weather = tweet_container.find('p').text

    #mars_weather


    # ## Mars Facts
    time.sleep(3)
    facts_url = "https://space-facts.com/mars/"

    tables = pd.read_html(facts_url)

    df = tables[0]
    df.columns = ["Item", "Description"]

    facts_html=df.to_html()

    facts_html

    # ## Mars Hemispheres
    
    #cerberus
    time.sleep(3)
   
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find('div', class_='downloads')
    link = url.find('a')
    ce_href = link['href']
    
    #Schiaparelli 
    time.sleep(3)
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/Schiaparelli_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find('div', class_='downloads')
    link = url.find('a')
    sc_href = link['href']

    
    #Syrtis Major   
    time.sleep(3)
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/Syrtis Major_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find('div', class_='downloads')
    link = url.find('a')
    sy_href = link['href']
    
    
    #valles_marineris
    time.sleep(3)
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find('div', class_='downloads')
    link = url.find('a')
    va_href = link['href']

   
    hemispheres_image_urls = [
        {"title": "cerberus Hemisphere", "img_url": ce_href},
        {"title": "Schiaparelli Hemisphere", "img_url": sc_href},
        {"title": "Syrtis Major Hemisphere", "img_url": sy_href},
        {"title": "valles_marineris Hemisphere", "img_url": va_href}
    ]

    mars_dict = {
        'latestheadline': titles,
        'latestparagraph':  paras,
        'featuredimage': full_image_url,
        'factstable': facts_html,
        'weather': "tweet",
        "ce_title": "cerberus Hemisphere", "ce_img_url": ce_href,
        "sc_title": "Schiaparelli Hemisphere", "sc_img_url": sc_href,
        "sy_title": "Syrtis Major Hemisphere", "sy_img_url": sy_href,
        "va_title": "valles_marineris Hemisphere", "va_img_url": va_href 
        }

    browser.quit()
    return mars_dict
    


