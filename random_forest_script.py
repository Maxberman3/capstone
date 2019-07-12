import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

def encode_and_bind(original_dataframe, feature_to_encode):
    res = pd.concat([original_dataframe, pd.get_dummies(original_dataframe[feature_to_encode],prefix=feature_to_encode,dummy_na=True)], axis=1)
    res.drop(columns=[feature_to_encode],axis=1,inplace=True)
    return(res)
df=pd.read_excel('Juliet_Test_Suite/combined_data_table.xlsx')
df=encode_and_bind(df,'Clang Rule')
df=encode_and_bind(df,'CodeSonar Rule')
df=encode_and_bind(df,'Severity')
df=encode_and_bind(df,'CWE')
df = df[np.isfinite(df['True Positive'])]
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
clf=RandomForestClassifier(n_estimators=100)
print(np.mean(cross_val_score(clf, X, y, cv=5)))
