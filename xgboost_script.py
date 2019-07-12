import pandas as pd
import numpy as np
import xgboost as xgb
from pandas import ExcelWriter,ExcelFile

def encode_and_bind(original_dataframe, feature_to_encode):
    res = pd.concat([original_dataframe, pd.get_dummies(original_dataframe[feature_to_encode],prefix=feature_to_encode,dummy_na=True)], axis=1)
    res.drop(columns=[feature_to_encode],axis=1,inplace=True)
    return(res)

df=pd.read_excel('Juliet_Test_Suite/combined_data_table.xlsx')
# msk= np.random.rand(len(df))<0.8
# train=df[msk]
# test=df[~msk]
# train['Clang Rule']=train['Clang Rule'].astype('category').cat.codes
# train['CodeSonar Rule']=train['CodeSonar Rule'].astype('category').cat.codes
# train['Severity']=train['Severity'].astype('category').cat.codes
# train['CWE']=train['CWE'].astype('category').cat.codes
# test['Clang Rule']=test['Clang Rule'].astype('category').cat.codes
# test['CodeSonar Rule']=test['CodeSonar Rule'].astype('category').cat.codes
# test['Severity']=test['Severity'].astype('category').cat.codes
# test['CWE']=test['CWE'].astype('category').cat.codes
# writer=ExcelWriter('trainset.xlsx')
# train.to_excel(writer,'sheet 1',index=False)
# # writer.save()
# X=train.iloc[:,:-1]
# # y=train.iloc[:,-1]
# d_train=xgb.DMatrix(data=X,label=y)
df=encode_and_bind(df,'Clang Rule')
df=encode_and_bind(df,'CodeSonar Rule')
df=encode_and_bind(df,'Severity')
df=encode_and_bind(df,'CWE')
df = df[np.isfinite(df['True Positive'])]
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
# writer=ExcelWriter('cat_rencode.xlsx')
# df.to_excel(writer,'sheet 1',index=False)
# writer.save()
d_data=xgb.DMatrix(data=X,label=y)
params = {"objective":"binary:logistic",'colsample_bytree': 0.3,'learning_rate': 0.1, 'alpha': 10}
cv_results = xgb.cv(dtrain=d_data, params=params, nfold=3, num_boost_round=50, early_stopping_rounds=10, metrics="error", as_pandas=True)
print(cv_results.head(10))
print(cv_results.tail(1))
