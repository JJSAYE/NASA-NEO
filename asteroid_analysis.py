import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC

df = pd.read_csv('/Users/jsaye/projects/datascience/NASA/asteroids.csv')
print(df.hazardous.value_counts() / df.shape[0])

def scatter(X, Y):
	x_title = X.upper()
	y_title = Y.upper().replace('_', ' ')
	X = df[X]
	Y = df[Y]

	plt.axes(facecolor='k')
	plt.scatter(
				x=X, 
				y=Y, 
				s=200, 
				c=df.hazardous, 
				alpha=0.7, 
				cmap='Paired', 
				edgecolors='k', 
				linewidth=2
				)	

	plt.xlabel(x_title)
	plt.ylabel(y_title)
	plt.title(x_title + '\n' + 'Against' + '\n' + y_title)
	plt.show()

scaler = StandardScaler()
label_encoder = LabelEncoder()

features = df[['magnitude', 'velocity', 'miles']]
features = scaler.fit_transform(features)

target = label_encoder.fit_transform(df['hazardous'])

X1, X2, y1, y2 = train_test_split(features, target, train_size=.8, random_state=0)

# knn = KNeighborsClassifier(n_neighbors=3, algorithm='ball_tree', metric='manhattan')
# model = knn.fit(X1,y1)
# labels = knn.predict(X2)

# model = LogisticRegression(fit_intercept=True, solver='liblinear', class_weight={1:2})
# model.fit(X1, y1)
# labels = model.predict(X2)

# model = RandomForestClassifier(n_estimators=200)
# model.fit(X1,y1)
# labels = model.predict(X2)

model = SVC(gamma='scale', decision_function_shape='ovo')
model.fit(X1, y1)
labels = model.predict(X2)

# scatter('magnitude', 'velocity')

mat = confusion_matrix(y2, labels)
sns.heatmap(
			mat.T, 
			square=True,
			annot=True, 
			fmt='d',
			cbar=True, 
			xticklabels=['Not Hazardous','Hazardous'],
			yticklabels=['Not Hazardous','Hazardous']
			,cbar_kws={'label': 'Number of observations'}
			)
plt.title(
		'Predicting Hazardous Asteroids' +
		 '\n' + 
		 'Accuracy Score: ' + 
		 str(round(accuracy_score(y2, labels)*100,1)) + 
		 "%"
		 )
plt.xlabel('True behavior')
plt.ylabel('Predicted behavior')
plt.show()

fig, ax = plt.subplots(1,2, sharex='col', sharey='row', facecolor='salmon')
axes =[0,1]
for x in axes:
	ax[x].set_facecolor('k')

#ACTUAL SUBPLOT
ax[0].scatter(
				X2[:,0:1].reshape(1892,1), 
				X2[:, 1:2].reshape(1892,1), 
				c=y2.reshape(1892,1), 
				alpha=0.8, 
				edgecolors='k', 
				s=200, 
				cmap='Paired'
				)
ax[0].set_title('Actual')
ax[0].set_xlim(-5,5)
ax[0].set_ylim(-2.5,6)
#PREDICTED SUBLOT
ax[1].scatter(
				X2[:,0:1].reshape(1892,1), 
				X2[:, 1:2].reshape(1892,1), 
				c=labels.reshape(1892,1), 
				alpha=0.8, 
				edgecolors='k', 
				s=200, 
				cmap='Paired'
				)

ax[1].set_title('Predicted')
ax[1].set_xlim(-5,5)
ax[1].set_ylim(-2.5,6)
plt.show()