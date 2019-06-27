import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df=pd.read_excel('Juliet_Test_Suite/combined_data_table.xlsx')
df['Clang Rule']=df['Clang Rule'].astype('category').cat.codes
df['CodeSonar Rule']=df['CodeSonar Rule'].astype('category').cat.codes
df['Severity']=df['Severity'].astype('category').cat.codes
df['CWE']=df['CWE'].astype('category').cat.codes
df = df[np.isfinite(df['True Positive'])]
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
clf=RandomForestClassifier(n_estimators=100)
print(np.mean(cross_val_score(clf, X, y, cv=5)))
