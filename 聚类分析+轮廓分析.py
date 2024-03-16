import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

file_path = "C:\\Users\\lx\\Desktop\\副本随机数据.xlsx"
data = pd.read_excel(file_path)
print(1)
selected_columns = ['残疾类型', '个人的生活自理能力', '居住形式', '受教育程度', '经济情况', '工作情况']
data = data[selected_columns]

data = data.dropna()

label_encoders = {}
for column in data.columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

silhouette_scores = []
K = range(2, 600)  # 选择聚类数量的范围
for num_clusters in K:
    kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=42)  # 显式设置n_init参数和random_state参数
    cluster_labels = kmeans.fit_predict(data_scaled)
    silhouette_avg = silhouette_score(data_scaled, cluster_labels)
    silhouette_scores.append(silhouette_avg)

plt.plot(K, silhouette_scores, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Analysis For Optimal k')
plt.show()

best_num_clusters = K[silhouette_scores.index(max(silhouette_scores))]
print(f"基于轮廓分析，最佳的聚类数量为: {best_num_clusters}")

kmeans = KMeans(n_clusters=best_num_clusters, n_init=10, random_state=42)  # 显式设置n_init参数和random_state参数
data['cluster'] = kmeans.fit_predict(data_scaled)

print("每个数据点所属的聚类类别:")
for index, row in data.iterrows():
    print(f"数据点 {index+1} 属于聚类 {row['cluster']+1}")
