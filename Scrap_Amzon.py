from selenium import webdriver 
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

names_amzn=[] #List to store name of the product
links_amzn=[] #List to store price of the product
reviews_amzn = []

driver = webdriver.Chrome('/Users/anilvyas/Desktop/Audace Labs/chromedriver-2')
web_links = ['https://www.amazon.com/Daiya-Zesty-Cheddar-Style-Cheeze/dp/B07DSK4R7F?ref_=fsclp_pl_dp_1',
             'https://www.amazon.com/Go-Veggie-Dairy-Free-Topping-Parmesan/dp/B018660S4W?ref_=fsclp_pl_dp_2',
             'https://www.amazon.com/Organic-Dairy-Free-Cashew-Parmesan-Gluten-Free/dp/B076XR11WH?ref_=fsclp_pl_dp_4',
             'https://www.amazon.com/Beyond-Better-Queso-Spicy-Ounce/dp/B00FQVVUVG?ref_=fsclp_pl_dp_7',
             'https://www.amazon.com/Parma-Vegan-Parmesan-Gluten-Free-Plant-Based/dp/B00BWVXFDU?ref_=fsclp_pl_dp_8',
             'https://www.amazon.com/Beyond-Better-Cashew-Cheese-Alternative/dp/B01A680A82?ref_=fsclp_pl_dp_13']
for k in web_links:
    driver.get(k)
    sleep(0.1)
    content = driver.page_source
    soup = BeautifulSoup(content)
    
    for i in soup.findAll('span', attrs = {'class':'cr-widget-FocalReviews'}):
        articledata = i.find('a', attrs = {'class':'a-link-emphasis a-text-bold'})
        articlecode = articledata['href']
        link = 'https://www.amazon.com/'+articlecode
    
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    while True:
        try:
            for j in soup.findAll('div', attrs={'class':'a-section review aok-relative'}):
                name = j.find('span', attrs={'class':'a-profile-name'}).text
                names_amzn.append(name)
                art = j.find('span', attrs={'class':'a-size-base review-text review-text-content'}).text
                reviews_amzn.append(art)
                links_amzn.append(k)
                print(name)
            for j in soup.findAll('div', attrs={'class':'a-text-center celwidget a-text-base'}):
                nl = j.find('li', attrs={'class':'a-last'})
                knl = nl.find('a')
                nlink = knl['href']
                nlink = 'https://www.amazon.com/'+nlink
                print(nlink)
            driver.get(nlink)
            content = driver.page_source
            soup = BeautifulSoup(content)
        except TypeError:
            break

amazon_reviews = pd.DataFrame(
    {'links_amzn': links_amzn,
     'names_amzn': names_amzn,
     'reviews_amzn': reviews_amzn,
    })
amazon_reviews.to_csv('/Users/anilvyas/Desktop/Audace Labs/amazon_data.csv')
driver.close()
