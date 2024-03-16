import os
import re
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 加载图像数据和标签
data = []
labels = []
is_path = r'D:\低频震荡的参数识别\是1' # 存储正例图像的文件夹路径
no_path = r'D:\低频震荡的参数识别\否1' # 存储负例图像的文件夹路径

for filename in os.listdir(is_path):
    if filename.endswith('.jpg'):
        img = plt.imread(os.path.join(is_path, filename))
        data.append(img)
        labels.append(1)

for filename in os.listdir(no_path):
    if filename.endswith('.jpg'):
        img = plt.imread(os.path.join(no_path, filename))
        data.append(img)
        labels.append(0)

# 将数据和标签转换为numpy数组
data = np.array(data)
labels = np.array(labels)

# 规范化和标准化数据
data = data.astype('float32') / 255.0
mean = np.mean(data)
std = np.std(data)
data = (data - mean) / std

# 将数据拆分为训练集和验证集
x_train, x_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)

# 实例化一个Sequential模型CNN
model = Sequential()
# 添加一个卷积层（卷积核的数量，卷积核的大小,步幅，激活函数，样本的长度）
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=data.shape[1:]))
# 添加一个池化层，卷积核为 2x2  （卷积核的大小，池化核的步长）
model.add(MaxPooling2D((2, 2)))
# 添加一个卷积层（卷积核的数量，卷积核的大小,步幅，激活函数，样本的长度）
model.add(Conv2D(64, (3, 3), activation='relu'))
# 添加一个池化层，卷积核为 2x2  （卷积核的大小，池化核的步长）
model.add(MaxPooling2D((2, 2)))
# 将多维张量展平为单维张量
model.add(Flatten())
# 添加一个全连接层
model.add(Dense(128, activation='relu'))
# 调整最后一层的神经元数量
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 训练模型
history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val))

# 在验证集上评估模型
val_loss, val_acc = model.evaluate(x_val, y_val)
print("验证丢失:", val_loss)
print("验证准确性:", val_acc)

# 负载测试数据
test_path = r'D:\低频震荡的参数识别\测试前50'
test_data = []
test_labels = []

for filename in os.listdir(test_path):
    if filename.endswith('.jpg'):
        img = plt.imread(os.path.join(test_path, filename))
        test_data.append(img)
        label = re.search(r'\d+', filename).group()  # Extract numeric part from filename using regex
        test_labels.append(int(label))

# 将测试数据和标签转换为numpy数组
test_data = np.array(test_data)
test_labels = np.array(test_labels)

# 预处理测试数据
test_data = test_data.astype('float32') / 255.0
test_data = (test_data - mean) / std

# 预测测试数据的标签
test_predictions = model.predict(test_data)
test_predictions = np.round(test_predictions).flatten()

# 将预测和真实标签转换为字符串
test_predictions = np.array(test_predictions, dtype=str)
test_labels = np.array(test_labels, dtype=str)

# 输出测试数据的真实和预测标签
print("真实标签:", test_labels)
print("预测标签:", test_predictions)

# 计算模型的精度并将其输出
test_accuracy = accuracy_score(test_labels, test_predictions)
print("测量精度:", test_accuracy)

# 可视化训练过程
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
