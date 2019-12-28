from selenium import webdriver 
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import time
names_youtube=[] #List to store name of the product
links_youtube=[] #List to store price of the product
reviews_youtube = []
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")

links = [#'https://www.youtube.com/watch?v=xFcp41bcfxU',
         #'https://www.youtube.com/watch?v=uh4XdgWL02E',
         'https://www.youtube.com/watch?v=DG7OkKk2ymg',#no
         'https://www.youtube.com/watch?v=s1vi7jzFOws',#no
         #'https://www.youtube.com/watch?v=x7hV-ed1Qm8',
         #'https://www.youtube.com/watch?v=fo2K1nSef2Y',
         #'https://www.youtube.com/watch?v=uPZhDz2Wk_s',
         'https://www.youtube.com/watch?v=NC9sdLD-cDo',#no
         #'https://www.youtube.com/watch?v=SqjYl90EUys',
         'https://www.youtube.com/watch?v=IfC9oOSRZq0',#no
         'https://www.youtube.com/watch?v=ccy2WVwnKM8',#no
         'https://www.youtube.com/watch?v=m0whdDgv_js',
         #'https://www.youtube.com/watch?v=oZCCDRuDy54',
         'https://www.youtube.com/watch?v=HcO-4lKOlC0',
         #'https://www.youtube.com/watch?v=keMlVX8n2GY',
         'https://www.youtube.com/watch?v=09gdf1dcvTA',
         'https://www.youtube.com/watch?v=egHDXRuNn2U']

#links = ['https://www.youtube.com/watch?v=NC9sdLD-cDo']
driver = webdriver.Chrome('/Users/anilvyas/Desktop/Audace Labs/chromedriver-2', chrome_options=chrome_options)

for link in links:
    driver.get(link)
    sleep(3)
    for i in range(500,40000, 500):
        sleep(0.8)
        driver.execute_script("window.scrollTo(0,"+ str(i)+')') 
    
    content = driver.page_source
    soup = BeautifulSoup(content)
    
    for j in soup.findAll('ytd-item-section-renderer', attrs={'id':'sections','class':'style-scope ytd-comments'}):
        #print(j)
        for a in j.findAll('ytd-comment-thread-renderer', attrs={'class':'style-scope ytd-item-section-renderer'}):
            try:
                #print("name- ", a)
                for k in a.findAll('a', attrs={'id':'author-text'}):
                    name=k.find('span', attrs={'class':'style-scope ytd-comment-renderer'}).text
                    print(name.strip())
                    names_youtube.append(name.strip())
                review=a.find('yt-formatted-string', attrs={'id':'content-text'}).text
                print(review)
                reviews_youtube.append(review)
                links_youtube.append(link)
            except:
                pass
                
        
youtube_data = pd.DataFrame(
    {'links_youtube': links_youtube,
     'names_youtube': names_youtube,
     'reviews_youtube': reviews_youtube,
    })
    
youtube_data.to_csv('/Users/anilvyas/Desktop/Audace Labs/youtube_data2_for_.csv')

driver.close()






