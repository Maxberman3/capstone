import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
from alipy import ToolBox
from sklearn.metrics import roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def encode_and_bind(original_dataframe, feature_to_encode):
    res = pd.concat([original_dataframe, pd.get_dummies(original_dataframe[feature_to_encode],prefix=feature_to_encode)], axis=1)
    res.drop(columns=[feature_to_encode],axis=1,inplace=True)
    return(res)
df=pd.read_excel('Juliet_Test_Suite/combined_data_table.xlsx')
df=encode_and_bind(df,'Clang Rule')
df=encode_and_bind(df,'CodeSonar Rule')
df=encode_and_bind(df,'Severity')
df=encode_and_bind(df,'CWE')
df.dropna(subset=['True Positive'],inplace=True)
df=df.reindex()
X=df.drop('True Positive',axis=1)
y=df.loc[:,'True Positive']

#change these parameters to alter experiment
init_labels=0.005#initial label rate
trn_tst_split=0.2# train test split portion
stop=300#number of queries to execute

alibox = ToolBox(X=X, y=y, query_type='AllLabels', saving_path='.')
alibox.split_AL(test_ratio=0.2,initial_label_rate=0.005,split_count=3)
# model=LogisticRegression(penalty='l1',solver='liblinear')
model=RandomForestClassifier(n_estimators=100)
stopping_criterion = alibox.get_stopping_criterion('num_of_queries', 300)
uncertainStrategy = alibox.get_query_strategy(strategy_name='QueryInstanceUncertainty')
unc_result = []
train_idx, test_idx, label_ind, unlab_ind = alibox.get_split(0)
saver = alibox.get_stateio(0)
# print(y.loc[label_ind.index])
model.fit(X=X.values[label_ind.index,:], y=y.values[label_ind.index])
while not stopping_criterion.is_stop():
    select_ind = uncertainStrategy.select(label_ind, unlab_ind, model=model, batch_size=1)
    label_ind.update(select_ind)
    unlab_ind.difference_update(select_ind)
    model.fit(X=X.values[label_ind.index,:], y=y.values[label_ind.index])
    pred = model.predict(X.values[test_idx,:])
    accuracy = alibox.calc_performance_metric(y_true=y[test_idx],y_pred=pred,performance_metric='accuracy_score')
    st = alibox.State(select_index=select_ind, performance=accuracy)
    saver.add_state(st)
    saver.save()
    stopping_criterion.update_information(saver)
fpr = dict()
tpr = dict()
fpr[0],tpr[0], _ = roc_curve(y.values[test_idx],pred)
stopping_criterion.reset()
unc_result.append(copy.deepcopy(saver))
QBCStrategy=alibox.get_query_strategy(strategy_name='QueryInstanceQBC')
qbc_result = []
train_idx, test_idx, label_ind, unlab_ind = alibox.get_split(1)
saver = alibox.get_stateio(1)
model.fit(X=X.values[label_ind.index,:], y=y.values[label_ind.index])
while not stopping_criterion.is_stop():
    select_ind = QBCStrategy.select(label_ind, unlab_ind, model=model, batch_size=1)
    label_ind.update(select_ind)
    unlab_ind.difference_update(select_ind)
    model.fit(X=X.values[label_ind.index,:], y=y.values[label_ind.index])
    pred = model.predict(X.values[test_idx,:])
    accuracy = alibox.calc_performance_metric(y_true=y[test_idx],y_pred=pred,performance_metric='accuracy_score')
    st = alibox.State(select_index=select_ind, performance=accuracy)
    saver.add_state(st)
    saver.save()
    stopping_criterion.update_information(saver)
fpr[1],tpr[1], _ = roc_curve(y.values[test_idx],pred)
stopping_criterion.reset()
qbc_result.append(copy.deepcopy(saver))
randStrategy=alibox.get_query_strategy(strategy_name='QueryRandom')
rand_result = []
train_idx, test_idx, label_ind, unlab_ind = alibox.get_split(2)
saver = alibox.get_stateio(2)
model.fit(X=X.values[label_ind.index,:], y=y.values[label_ind.index])
while not stopping_criterion.is_stop():
    select_ind = randStrategy.select(label_ind, unlab_ind, model=model, batch_size=1)
    label_ind.update(select_ind)
    unlab_ind.difference_update(select_ind)
    model.fit(X=X.values[label_ind.index,:], y=y.values[label_ind.index])
    pred = model.predict(X.values[test_idx,:])
    accuracy = alibox.calc_performance_metric(y_true=y[test_idx],y_pred=pred,performance_metric='accuracy_score')
    st = alibox.State(select_index=select_ind, performance=accuracy)
    saver.add_state(st)
    saver.save()
    stopping_criterion.update_information(saver)
fpr[2],tpr[2], _ = roc_curve(y.values[test_idx],pred)
stopping_criterion.reset()
qbc_result.append(copy.deepcopy(saver))
plt.figure()
lw=2
plt.plot(fpr[0],tpr[0],color='darkorange',lw=lw,label='Uncertainy')
plt.plot(fpr[1],tpr[1],color='g',lw=lw,label='QBC')
plt.plot(fpr[2],tpr[2],color='y',lw=lw,label='Random')
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC at {} Queries'.format(str(stop)))
plt.legend(loc="lower right")
plt.show()
