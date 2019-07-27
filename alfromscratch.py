import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def encode_and_bind(original_dataframe, feature_to_encode):
    res = pd.concat([original_dataframe, pd.get_dummies(original_dataframe[feature_to_encode],prefix=feature_to_encode)], axis=1)
    res.drop(columns=[feature_to_encode],axis=1,inplace=True)
    return(res)

df=pd.read_excel('Juliet_Test_Suite/combined_data_table.xlsx')
df=encode_and_bind(df,'Clang Rule')
df=encode_and_bind(df,'CodeSonar Rule')
df=encode_and_bind(df,'Severity')
df=encode_and_bind(df,'CWE')
df = df[np.isfinite(df['True Positive'])]
# print(df.head())
init_label_indx=random.sample(range(0,len(df)),200)
init_labels=df[df.index.isin(init_label_indx)]
remainder=df[~df.index.isin(init_label_indx)]
assert len(init_labels)+len(remainder)==len(df),'the split did not work correctly'
X=init_labels.drop('True Positive',axis=1)
# print(X.columns)
y=init_labels.loc[:,'True Positive']
# model.fit(X=X[label_ind.index, :], y=y[label_ind.index])print(y)
X_test=remainder.drop('True Positive',axis=1)
y_test=remainder.loc[:,'True Positive']
lr=LogisticRegression(penalty='l1',solver='liblinear').fit(X,y)
cdf = pd.DataFrame(lr.coef_.transpose(), X.columns, columns=['Coefficients'])
print(cdf)
predictions=lr.predict(X_test)
counter=0
for i in predictions:
    if i==1:
        counter+=1
print(counter)
# print(lr.predict(X_test))
# print(lr.predict_proba(X_test))
print(lr.score(X_test,y_test))
