import pandas as pd
import lightgbm as lgb
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

#import dataset, change manually on your station
dataset = pd.read_csv('G:\\VS code projects\\crypto-market-observer\\datasets\\btc_1h_data_2018_to_2025.csv')

print(dataset.head())
dataset['Open time'] = pd.to_datetime(dataset['Open time'])
dataset = dataset.dropna(subset=['Open time'])
dataset['day_of_week'] = dataset['Open time'].dt.dayofweek.astype('int8')

dataset['hour'] = dataset['Open time'].dt.hour.astype('int8')
dataset = dataset.drop(columns=['Open time', 'Close time', 'Ignore'])
dataset['vol_spread'] = dataset['High'] - dataset['Low']

target = dataset['Close']
dataset = dataset.drop(columns=['Close', 'High', 'Low', 'Taker buy base asset volume', 'Taker buy quote asset volume'])


X_train, X_test, y_train, y_test = train_test_split(dataset, target, test_size =.2)

model = lgb.LGBMRegressor(n_estimators = 2, max_depth = 2, learning_rate = 1, objective = 'binary:logistic')

labEnc = LabelEncoder()

y_train = labEnc.fit_transform(y_train)

model.fit(X_train, y_train)

preds = model.predict(X_test)

print(classification_report(y_test, preds))
print(confusion_matrix(y_test, preds))

