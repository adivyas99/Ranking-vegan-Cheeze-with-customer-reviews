## Importing libraries
# Starting Code from here-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame

#import nltk
#nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

#------------------------
#Getting scores of sentiments
#------------------------
# Scores of YouTube data-
data = pd.read_csv('youtube_data2_for_.csv')

compund = []
pos = []
neg =[]
neu = []


for i in data.reviews_youtube:
    i = i.replace("\'",'')
    i = i.strip()
    #print(get_textBlob_score(i))
    ss = sid.polarity_scores(i)
    compund.append(ss['compound'])
    pos.append(ss['pos'])
    neg.append(ss['neg'])
    neu.append(ss['neu'])
    #print(ss)

data['compund'] = compund
data['pos'] = pos
data['neg'] = neg
data['neu'] = neu
#get_vader_score('bad')
maxValuesObj = data[['pos','neg']].idxmax(axis=1)
data['sentiments'] = maxValuesObj
data.to_csv('/Users/anilvyas/Desktop/Audace Labs/Rated_data/youtube_data.csv')

#------------------------
# Scores of Amazon data-
data2 = pd.read_csv('amazon_data.csv')

compund = []
pos = []
neg =[]
neu = []

        
for i in data2.reviews_amzn:
    i = i.replace("\'",'')
    i = i.strip()
    #print(get_textBlob_score(i))
    ss = sid.polarity_scores(i)
    compund.append(ss['compound'])
    pos.append(ss['pos'])
    neg.append(ss['neg'])
    neu.append(ss['neu'])
    #print(ss)

data2['compund'] = compund
data2['pos'] = pos
data2['neg'] = neg
data2['neu'] = neu

maxValuesObj = data2[['pos','neg']].idxmax(axis=1)
data2['sentiments'] = maxValuesObj

data2.to_csv('/Users/anilvyas/Desktop/Audace Labs/Rated_data/amazon_data.csv')

#------------------------
# Scores of BlogPosts data-
data3 = pd.read_csv('/Users/anilvyas/Desktop/Audace Labs/Rated_data/cheese dataset.csv')

compund = []
pos = []
neg =[]
neu = []


for i in data3.reviewer_text:
    i = i.replace("\'",'')
    i = i.strip()
    #print(get_textBlob_score(i))
    ss = sid.polarity_scores(i)
    compund.append(ss['compound'])
    pos.append(ss['pos'])
    neg.append(ss['neg'])
    neu.append(ss['neu'])
    #print(ss)

data3['compund'] = compund
data3['pos'] = pos
data3['neg'] = neg
data3['neu'] = neu

maxValuesObj = data3[['pos','neg']].idxmax(axis=1)
data3['sentiments'] = maxValuesObj

data3.to_csv('/Users/anilvyas/Desktop/Audace Labs/Rated_data/cheese dataset.csv')





#--------------------------
# Getting Count plots and line plots of sentiments
#--------------------------
#  Youtube data-
data.compund.plot(kind = 'line', figsize=(6,6))
data.sentiments.value_counts().plot(kind= 'bar')
data.pos.plot(kind = 'line')
data.neg.plot(kind = 'line')
data.neu.plot(kind = 'line')
fig = data.sentiments.value_counts().plot(kind= 'bar', figsize=(13,8)).get_figure()
fig.savefig("/Users/anilvyas/Desktop/Audace Labs/Rated_data/youtube_count_pyplot.pdf")

#  Amazon data-
data2.compund.plot(kind = 'line')
data.pos.plot(kind = 'line')
data.neg.plot(kind = 'line')
data.neu.plot(kind = 'line')
fig = data2.sentiments.value_counts().plot(kind= 'bar', figsize=(13,8)).get_figure()
fig.savefig("/Users/anilvyas/Desktop/Audace Labs/Rated_data/amazon_count_pyplot.pdf")

#  BlogPosts data-
data3.compund.plot(kind = 'line')
data.pos.plot(kind = 'line')
data.neg.plot(kind = 'line')
data.neu.plot(kind = 'line')
fig = data3.compund.plot(kind = 'line', figsize=(13,8)).get_figure()

fig = data3.sentiments.value_counts().plot(kind= 'bar', figsize=(13,8)).get_figure()
fig.savefig("/Users/anilvyas/Desktop/Audace Labs/Rated_data/sentiment_count_pyplot.pdf")


#--------------------------
## Analysis
#--------------------------

## Analysis Youtube data-

av = data.groupby('links_youtube')

unique_youtube = data['links_youtube'].unique().tolist()
unique_youtube2 = ['1. cashews, \n2. flour + plant-based milk, \n3. potatoes+carrot, \n4. soy milk+sweet potato',
                  '1. cashew, \n2. pistachio, \n3. sunflower seed, \n4. cashew',
                  '1. cashew nuts+plant based milk, \n2. butternut squash+plantbased milk, \n3. tofu + soy milk, \n4. rice flour',
                  '1. cashews, \n2. cauliflower, \n3. potato+sweet potato+plantbased milk+tapioca , \n4. cashew+tapioca, \n5. cashew',
                  '1. almonds, \n2. cashew+cornstarch, \n3. cashews+plantmilk ',
                  '1. cashew, \n2. vegan yogurt+oil, \n3. aquafaba',
                  '1. cashew+tapioca, \n2. cashew+sweet potato+tapioca, \n3. cashew',
                  '1. cashew+nondairy yogurt, \n2. cashew',
                  '1. tofu+carrot, \n2. tofu, \n3. tofu+soymilk ']

## manually entered the classification of ingredients

percents = []
names = []
for i in unique_youtube:
    #print(av.get_group(i))
    name = unique_youtube2[unique_youtube.index(i)]
    #name = av.get_group(i).iloc[0]['links_youtube']
    leng = av.get_group(i).shape[0]
    pos = av.get_group(i).sentiments.value_counts()['pos']
    percent = (pos/leng)*100
    #print(percent)
    percents.append(percent)
    names.append(name)
    

datadf = pd.DataFrame({'names':names,'percents':percents})
datadf.sort_values('percents',ascending = False,inplace=True)

df = datadf.groupby('names')['percents'].mean()#.plot(kind = 'bar',ascending= True)
#df.sort_values('percents',inplace=True)
df1 = pd.DataFrame({'names':df.index, 'percents':df})
#df = DataFrame({'names' : datadf.groupby( "names")['percents'].mean()}).reset_index()
#df1 = df1.drop(['names'])
df1['percents'] = df1.percents.astype(np.float16)
df1.sort_values('percents',ascending = False,inplace=True)
df1.plot(kind = 'bar', legend = False)
fig = df1.plot(kind = 'bar', legend = False).get_figure()
fig.savefig("youtube_plot.pdf")

index = np.arange(len(unique_youtube2))
plt.bar(datadf.names, datadf.percents)
plt.xlabel('Links', fontsize=9)
plt.ylabel('Positivity', fontsize=8)
plt.xticks(names, names, fontsize=8, rotation=90)
plt.title('Percent Positivity for each video link')
plt.savefig('youtube_.png', figsize=(800,1000), dpi = 500)
plt.show()
#----------------------
## Analysis Amazon data-
av = data2.groupby('links_amzn')
unique_amazon = data2['links_amzn'].unique().tolist()
unique_amazon2 = ['zucchini',
                  'Soy Base',
                  'Cashew',
                  'Cashew',
                  'walnut',
                  'Cashew']
percents = []
names = []
for i in unique_amazon:
    #print(av.get_group(i))
    #name = av.get_group(i).iloc[0]['links_amzn']
    name = unique_amazon2[unique_amazon.index(i)]
    leng = av.get_group(i).shape[0]
    pos = av.get_group(i).sentiments.value_counts()['pos']
    percent = (pos/leng)*100
    #print(percent)
    percents.append(percent)
    names.append(name)

datadf = pd.DataFrame({'names':names,'percents':percents})
datadf.sort_values('percents',ascending = False,inplace=True)

df = datadf.groupby('names')['percents'].mean()#.plot(kind = 'bar',ascending= True)
df1 = pd.DataFrame({'names':df.index, 'percents':df})
#df = DataFrame({'names' : datadf.groupby( "names")['percents'].mean()}).reset_index()
#df1 = df1.drop(['names'])
df1['percents'] = df1.percents.astype(np.float16)
df1.sort_values('percents',ascending = False,inplace=True)
df1.plot(kind = 'bar', legend = False)
fig = df1.plot(kind = 'bar', legend = False).get_figure()
fig.savefig("amazon_plot.pdf")


index = np.arange(len(names))
plt.bar(datadf.names, datadf.percents)
plt.xlabel('Links', fontsize=5)
plt.ylabel('Positivity', fontsize=7)
plt.xticks(names, names, fontsize=1, rotation=30)
plt.title('Percent Positivity for each video link')
plt.savefig('amazon_.pdf', figsize=(20,10))
plt.show()

#----------------------
## Analysis Blogposts data-
data3.name = data3.name.replace('VEGAN CHEDDAR CHEESE', 'https://lovingitvegan.com/vegan-cheddar-cheese/')
data3.name = data3.name.replace('Hickory Smoked Vegan Cheese', 'https://fullofplants.com/hickory-smoked-aged-vegan-cheese/')
data3.name = data3.name.replace('GO-TO CASHEW CHEESE RECIPE', 'https://www.thefullhelping.com/go-to-cashew-cheese-recipe/')
av = data3.groupby('name')
unique_sentiments = data3['name'].unique().tolist()
'''unique_sentiments2=['Cashew',
                    'Cashew+TapiocaStarch',
                    'Cashew+Yeast',
                    'Cashew+Yeast',
                    'Cashew+Yeast',
                    'Cashew',
                    'Cashew',
                    'Potato+Carrot',
                    'Potato+Carrot',
                    'Cashew+Yeast',
                    'CoconutMilk',
                    'Almonds',
                    'YukonGold+Zuchini',
                    'Cashew+CoconutOil']'''

unique_sentiments2=['soy sauce, tomato paste, ACV, red pepper, garlic, onion, nutritional yeast, salt, paprika, mustard',
                    'nutritional yeast, lemon juice, salt',
                    'white miso, nutritional yeast, salt',
                    'lemon juice, garlic powder, salt, pepper',
                    'nutritional yeast, apple cider vinegar, agave, salt',
                    'nutritional yeast, onion powder, garlic powder, miso, salt',
                    'lemon juice, nutritional yeast, onion powder, garlic powder, paprika, salt, mustard',
                    'nutritional yeast, apple cider vinegar,lemon juice, salt',
                    'nutritional yeast, soy sauce, lemon juice, garlic powder',
                    'maple syrup, nutritional yeast, cayenne, lemon',
                    'lemon juice, garlic powder, salt',
                    'lemon juice, salt',
                    'nutritional yeast, onion powder, garlic powder, paprika, salt, liquid aminos, lemon juice',
                    'lemon juice, nutritional yeast, salt']
percents = []
names = []
for i in unique_sentiments:
    #print(av.get_group(i))
    #name = av.get_group(i).iloc[0]['name']
    name = unique_sentiments2[unique_sentiments.index(i)]
    leng = av.get_group(i).shape[0]
    pos = av.get_group(i).sentiments.value_counts()['pos']
    percent = (pos/leng)*100
    #print(percent)
    percents.append(percent)
    names.append(name)

datadf = pd.DataFrame({'names':names,'percents':percents})
datadf.sort_values('percents',ascending = False,inplace=True)

df = datadf.groupby('names')['percents'].mean()#.plot(kind = 'bar',ascending= True)
df1 = pd.DataFrame({'names':df.index, 'percents':df})
#df = DataFrame({'names' : datadf.groupby( "names")['percents'].mean()}).reset_index()
#df1 = df1.drop(['names'])
df1['percents'] = df1.percents.astype(np.float16)
df1.sort_values('percents',ascending = False,inplace=True)
df1.plot(kind = 'bar', legend = False)
fig = df1.plot(kind = 'bar', legend = False).get_figure()
fig.savefig("amazon_plot.pdf")


index = np.arange(len(names))
plt.bar(datadf.names, datadf.percents)
plt.xlabel('Links', fontsize=5)
plt.ylabel('Positivity', fontsize=6)
plt.xticks(names, names, fontsize=7, rotation=90)
plt.title('Percent Positivity vs Flavoring ingredient for each BlogPost')
plt.savefig('sentiments_.png', figsize=(60,50))
plt.show()


##-----------------
#End



#### Extra Code -  - Trash
'''from textblob import TextBlob
# Get the polarity score using below function
def get_textBlob_score(sent):
    # This polarity score is between -1 to 1
    polarity = TextBlob(sent).sentiment.polarity
    return polarity


get_textBlob_score('aditya is a cool man and he is a not bad boy')'''
'''def get_vader_score(sent):
    # Polarity score returns dictionary
    ss = sid.polarity_scores(sent)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')'''



