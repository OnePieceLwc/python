
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号   #显示所有列，把行显示设置成最大
pd.set_option('display.max_columns', None)  # 显示所有行，把列显示设置成最大
pd.set_option('display.max_rows', None)
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import learning_curve
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn import svm
from sklearn.model_selection import validation_curve
from sklearn.metrics import plot_roc_curve
from sklearn.model_selection import GridSearchCV

data = pd.read_csv(r"D:\card_transdata.csv")
x = data.drop(columns=['fraud'], inplace=False)
y = data['fraud']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

svm_model = svm.SVC(kernel="rbf", gamma="auto", cache_size=5000, )
svm_model.fit(x_train, y_train)
y_pred = svm_model.predict(x_test)
acc = accuracy_score(y_pred, y_test)
print(acc)

y_pred = pd.DataFrame(y_pred)
print(y_pred.value_counts())

y_test.value_counts()
print(y_test.value_counts())

# 网格调参
param_grid = {'Kernel': ["linear", "rbf", "sigmoid"]}
grid = GridSearchCV(svm_model, param_grid)
grid.fit(x_train, y_train)
print(grid.best_params_)

# 搜寻到的最佳模型
svm_model=grid.best_estimator_
# 进行模型性能估计
y_pred1 = svm_model.predict(x_train)
y_pred2 = svm_model.predict(x_test)
print(y_pred1)
print(y_pred2)

# 交叉验证
score = cross_val_score(GaussianNB(), x, y, cv=5)
print("交叉验证分数为{}".format(score))
print("平均交叉验证分数:{}".format(score.mean()))

# 学习曲线
max_depth=["linear", "rbf", "sigmoid"]
train_score, val_score = validation_curve(svm_model, x, y,
                                          param_name='max_depth',
                                          param_range=max_depth, cv=5, scoring='accuracy')
plt.plot(max_depth, np.median(train_score, 1), color='blue', label='training score')
plt.plot(max_depth, np.median(val_score, 1), color='red', label='validation score')
plt.legend(loc='best')
plt.xlabel('max_depth')
plt.ylabel('score')


#学习曲线
train_sizes, train_loss, val_loss = learning_curve(svm_model, x, y,cv=5,train_sizes=[0.1, 0.25, 0.3, 0.5, 0.75, 1])
train_loss_mean = np.mean(train_loss, axis=1)
val_loss_mean = np.mean(val_loss, axis=1)
plt.plot(train_sizes, train_loss_mean, 'o-', color='r', label='Training')
plt.plot(train_sizes, val_loss_mean, 'o-', color='g', label='Cross-validation')
plt.xlabel('Training_examples')
plt.ylabel('Loss')
plt.legend(loc='best')
plt.show()

# 各种评价指标
y_pred1 = svm_model.predict(x_test)
acc = accuracy_score(y_test, y_pred1)
f1 = f1_score(y_test, y_pred1)
recall = recall_score = recall_score(y_test, y_pred1)
precision = precision_score(y_pred1, y_test)
print(acc)
print(f1)
print(recall)
print(precision)

# 可视化
plot_confusion_matrix(svm_model, x_test, y_test)
plt.show()

# Roc曲线
plot_roc_curve(svm_model, x_test, y_test)
plt.show()
