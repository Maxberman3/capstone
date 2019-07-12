import pandas as pd
import numpy as np
from alipy.experiment import AlExperiment
from alipy.experiment import ExperimentAnalyser
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
X=df.drop('True Positive',axis=1)
y=df.loc[:,'True Positive']
al_unc=AlExperiment(X,y,model=LogisticRegression(penalty='l1',solver='liblinear'),performance_metric='accuracy_score',stopping_criteria='num_of_queries', stopping_value=300)
al_unc.split_AL(test_ratio=0.2,initial_label_rate=0.005,split_count=5,all_class=True)
al_unc.set_query_strategy(strategy='QueryInstanceUncertainty')
al_unc.set_performance_metric(performance_metric='accuracy_score')
al_unc.start_query(multi_thread=False)
# print(al.get_experiment_result())
# al.plot_learning_curve()
analyser=ExperimentAnalyser(x_axis='num_of_queries')
analyser.add_method('uncertainty',al_unc.get_experiment_result())
al_qbc=AlExperiment(X,y,model=LogisticRegression(penalty='l1',solver='liblinear'),performance_metric='accuracy_score',stopping_criteria='num_of_queries', stopping_value=300)
al_qbc.split_AL(test_ratio=0.2,initial_label_rate=0.005,split_count=5,all_class=True)
al_qbc.set_query_strategy(strategy='QueryInstanceQBC')
al_qbc.set_performance_metric(performance_metric='accuracy_score')
al_qbc.start_query(multi_thread=False)
analyser.add_method('by committee',al_qbc.get_experiment_result())
al_rndm=AlExperiment(X,y,model=LogisticRegression(penalty='l1',solver='liblinear'),performance_metric='accuracy_score',stopping_criteria='num_of_queries', stopping_value=300)
al_rndm.split_AL(test_ratio=0.2,initial_label_rate=0.005,split_count=5,all_class=True)
al_rndm.set_query_strategy(strategy='QueryRandom')
al_rndm.set_performance_metric(performance_metric='accuracy_score')
al_rndm.start_query(multi_thread=False)
analyser.add_method('random',al_rndm.get_experiment_result())
# al_err=AlExperiment(X,y,model=LogisticRegression(penalty='l1',solver='liblinear'),performance_metric='accuracy_score',stopping_criteria='num_of_queries', stopping_value=300)
# al_err.split_AL(test_ratio=0.2,initial_label_rate=0.005,split_count=5,all_class=True)
# al_err.set_query_strategy(strategy='QueryExpectedErrorReduction')
# al_err.set_performance_metric(performance_metric='accuracy_score')
# al_err.start_query(multi_thread=False)
# analyser.add_method('error reduction',al_err.get_experiment_result())
analyser.plot_learning_curves()
