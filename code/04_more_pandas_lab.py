import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Part 1: UFO

'''

ufo = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_17/master/data/ufo.csv')   # can also read csvs directly from the web!



# 1. change the column names so that each name has no spaces
#           and all lower case

ufo.columns = [x.replace(" ", "").lower() for x in ufo.columns]
ufo.head()
ufo.count(axis = 1) 
# 2. Show a bar chart of all shapes reported

ufo['shapereported'].value_counts().plot(kind = 'bar')

# 3. Show a dataframe that only displays the reportings from Utah

ufo[ufo['state'] == 'UT']

# 4. Show a dataframe that only displays the reportings from Texas

ufo[ufo['state'] == 'TX']

# 5. Show a dataframe that only displays the reportings from Utah OR Texas

ufo[(ufo['state'] == 'TX') | (ufo['state'] == 'UT')]

# 6. Which shape is reported most often?

ufo['shapereported'].value_counts().idxmax()

# 7. Plot number of sightings per day in 2014 (days should be in order!)

ufo['Day'] = ufo['time'].apply(lambda x:int(x.split('/')[1]))
ufo['Month'] = ufo['time'].apply(lambda x:int(x.split('/')[0]))
ufo['Year'] = ufo['time'].apply(lambda x:int(x.split('/')[2][:4]))

ufo['MonthDay'] = ufo['Month'].map(str) + '/' + ufo['Day'].map(str)

ufo['MonthDay'][ufo['Year'] == 2014].value_counts().hist(bins=365)

'''
Part 2: IRIS

'''


iris = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_17/master/data/iris.csv')   # can also read csvs directly from the web!
iris.head()

# 1. Show the mean petal length by flower species

iris['petal_length'].groupby(iris['species']).mean()

# 2. Show the mean sepal width by flower species

iris['sepal_width'].groupby(iris['species']).mean()

# 3. Use the groupby to show both #1 and #2 in one dataframe

iris[['petal_length','sepal_width']].groupby(iris['species']).mean()

# 4. Create a scatter plot plotting petal length against petal width
#    Use the color_flowers function to 
# apply this function to the species column to give us 
# designated colors!


def color_flower(flower_name):
    if flower_name == 'Iris-setosa':
        return 'b'
    elif flower_name == 'Iris-virginica':
        return 'r'
    else:
        return 'g'


colors = iris.species.apply(color_flower)

colors

iris.plot(x='petal_length', y='petal_width', kind='scatter', c=colors)

# 5. Show flowers with sepal length over 5 and petal length under 1.5
iris[(iris['sepal_length'] > 5) & (iris['petal_length'] < 1.5)]

# 6. Show setosa flowers with petal width of exactly 0.2

iris[(iris['species'] == 'Iris-setosa') & (iris['petal_width'] == 0.2)]

# 7. Write a function to predict the species for each observation

def classify_iris(data):
    if data[3] < .75:
        return 'Iris-setosa'
    elif data[2] < 5:
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'

# example use: 
# classify_iris([0,3,2.1,3.2]) == 'Iris-virginica'
# assume the order is the same as the dataframe, so:
# [sepal_length', 'sepal_width', 'petal_length', 'petal_width']


# make predictions and store as preds
preds = iris.drop('species', axis=1).apply(classify_iris, axis = 1)


preds


# test your function: compute accuracy of your prediction
(preds == iris['species']).sum() / float(iris.shape[0])


'''
Part 3: FIFA GOALS

'''

goals = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_17/master/data/fifa_goals.csv')
# removing '+' from minute and turning them into ints
goals.minute = goals.minute.apply(lambda x: int(x.replace('+','')))


goals.head()


# 1. Show goals scored in the first 5 minutes of a game
goals[goals.minute <= 5]


# 2. Show goals scored after the regulation 90 minutes is over
goals[goals.minute > 90]


# 3. Show the top scoring players
goals.player.value_counts(sort=True)

# 4. Show a histogram of minutes with 20 bins
goals.minute.hist(bins=20)

# 5. Show a histogram of the number of goals scored by players
goals.player.value_counts(sort=True).hist()

