import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


print("Loading data from pickle file...")
data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])
print(f"Loaded {len(data)} samples for training")

print("\nSplitting data into training and testing sets...")
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
print(f"Training samples: {len(x_train)}")
print(f"Testing samples: {len(x_test)}")

print("\nInitializing Random Forest Classifier...")
model = RandomForestClassifier()

print("Training model...")
model.fit(x_train, y_train)

print("\nMaking predictions on test set...")
y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)
print('\nResults:')
print(f'{score * 100:.2f}% of samples were classified correctly!')

print("\nSaving model to 'model.p'...")
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
print("Model saved successfully!")
