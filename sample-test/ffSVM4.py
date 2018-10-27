## In this model, PCA is performed on the 4 feature data set to extract 2 equivalent feature. </br>
## Upon these 2 features SVM is applied to predict if a forest fire will happen or not

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('FFSAMPLESVM.csv')
# df = df.drop(['Id'],axis=1)
target = df['FForNOT']

from sklearn.preprocessing import StandardScaler

features = ['ISI', 'TEMP', 'RH', 'WIND']
# Separating out the features
x = df.loc[:, features].values
# Separating out the target
y = df.loc[:,['FForNOT']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, df[['FForNOT']]], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)

targets = ['noff', 'ff']
colors = ['r', 'g']
for target, color in zip(targets,colors):
    indicesToKeep = (finalDf['FForNOT'] == target)
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

from sklearn.cross_validation import train_test_split
import numpy as np

Y = []

for val in target:
    if(val == 'noff'):
        Y.append(-1)
    else:
        Y.append(1)
        
df = df.drop(['FForNOT'],axis=1)
#X = 
X = principalDf
## Shuffle and split the data into training and test set
#X, Y = shuffle(X,Y)
x_train = []
y_train = []
x_test = []
y_test = []

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

y_train = y_train.reshape(112,1)
y_test = y_test.reshape(38,1)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='linear')
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_test,y_pred))
