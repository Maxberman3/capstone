import pandas as pd
import numpy as np
from alipy.experiment import AlExperiment
from sklearn.linear_model import LogisticRegression

df=pd.read_excel('Juliet_Test_Suite/combined_data_table.xlsx')
# print(len(df)*0.005)
df['Clang Rule']=df['Clang Rule'].astype('category').cat.codes
df['CodeSonar Rule']=df['CodeSonar Rule'].astype('category').cat.codes
df['Severity']=df['Severity'].astype('category').cat.codes
df['CWE']=df['CWE'].astype('category').cat.codes
df = df[np.isfinite(df['True Positive'])]
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
al=AlExperiment(X,y,model=LogisticRegression(penalty='l1',solver='liblinear'),performance_metric='accuracy_score',stopping_criteria='num_of_queries', stopping_value=300)
al.split_AL(test_ratio=0.2,initial_label_rate=0.005,split_count=5,all_class=False)
al.set_query_strategy(strategy='QueryInstanceUncertainty')
al.set_performance_metric(performance_metric='accuracy_score')
al.start_query(multi_thread=True)
al.get_experiment_result()
al.plot_learning_curve()
