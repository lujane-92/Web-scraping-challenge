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

# ## NASA Mars News - Collect Latest News Title and Paragraph Text

def scrape():
    browser = init_browser()
    
    mars_news_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_news_url)

    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')

    news_title = mars_news_soup.body.find("div", class_="content_title").text

    news_paragraph = mars_news_soup.body.find("div", class_="article_teaser_body").text


    # ## JPL Mars Space Images

    time.sleep(3)

    mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(mars_image_url)

    browser.click_link_by_id('full_image')

    browser.click_link_by_partial_text('more info')

    image_html = browser.html
    mars_image_soup = BeautifulSoup(image_html, 'html.parser')
    
    image = mars_image_soup.body.find("figure", class_="lede")

    link = image.find('a')
    href = link['href']

    base_url='https://www.jpl.nasa.gov'

    featured_image_url = base_url + href

    featured_image_url

    # ## Mars Weather

    time.sleep(3)

    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)

    html = browser.html
    mars_weather_soup = BeautifulSoup(html, 'html.parser')

    # find the tweet text

    #tweet_container = mars_weather_soup.body.find('div','js-tweet-text-container')

    #mars_weather = tweet_container.find('p').text

    #mars_weather


    # ## Mars Facts
    time.sleep(3)
    mars_facts_url = "https://space-facts.com/mars/"

    tables = pd.read_html(mars_facts_url)

    df1 = tables[0]
    df1.columns = ["Description", "Value"]

    mars_facts_html=df1.to_html()

    mars_facts_html

    # ## Mars Hemispheres

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    browser.click_link_by_partial_text('Cerberus')

    browser.click_link_by_partial_text('Open')

    hemispheres_html = browser.html
    cerberus_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    cerberus = cerberus_soup.body.find('img', class_ = 'wide-image')
    cerberus_img = cerberus['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    cerberus_url = hem_base_url + cerberus_img
    
    # Schiaperelli hemisphere

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    browser.click_link_by_partial_text('Schiaparelli')

    browser.click_link_by_partial_text('Open')
    schiap_html = browser.html
    schiap_soup = BeautifulSoup(schiap_html, 'html.parser')

    schiap = schiap_soup.body.find('img', class_ = 'wide-image')
    schiap_img = schiap['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    schiap_url = hem_base_url + schiap_img
    
    # #### Syrtis hemisphere

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    browser.click_link_by_partial_text('Syrtis')

    browser.click_link_by_partial_text('Open')

    syrtis_html = browser.html
    syrtis_soup = BeautifulSoup(syrtis_html, 'html.parser')

    syrtis = syrtis_soup.body.find('img', class_ = 'wide-image')
    syrtis_img = syrtis['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    syrtis_url = hem_base_url + syrtis_img
    
    # #### Valles hemisphere

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    browser.click_link_by_partial_text('Valles')

    browser.click_link_by_partial_text('Open')

    valles_html = browser.html
    valles_soup = BeautifulSoup(valles_html, 'html.parser')

    valles = valles_soup.body.find('img', class_ = 'wide-image')
    valles_img = valles['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    valles_url = hem_base_url + valles_img

    
    hemispheres_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
        {"title": "Schiaparelli Marineris Hemisphere", "img_url": schiap_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url}
    ]

    mars_dict = {
        'latestheadline': news_title,
        'latestparagraph':  news_paragraph,
        'featuredimage': featured_image_url,
        'factstable': mars_facts_html,
        "va_title": "Valles Marineris Hemisphere", "va_img_url": valles_url,
        "ce_title": "Cerberus Hemisphere", "ce_img_url": cerberus_url,
        "sc_title": "Schiaparelli Marineris Hemisphere", "sc_img_url": schiap_url,
        "sy_title": "Syrtis Major Hemisphere", "sy_img_url": syrtis_url 
        }

    browser.quit()
    return mars_dict
    


