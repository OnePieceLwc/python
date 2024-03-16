import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# 分词
text = "Natural language processing is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language."
tokens = word_tokenize(text)
print(tokens)

# 去除停用词
stop_words = set(stopwords.words('english'))
tokens_filtered = [word for word in tokens if word.lower() not in stop_words]
print(tokens_filtered)

# 词频统计
freq_dist = nltk.FreqDist(tokens_filtered)
print(freq_dist.most_common(5))

# 情感分析
sia = SentimentIntensityAnalyzer()
sentiment_score = sia.polarity_scores(text)
print(sentiment_score)

# 文本分类
pos_tweets = [('I love this car', 'positive'), ('This view is amazing', 'positive'), ('I feel great this morning', 'positive'), ('I am so happy today', 'positive'), ('He is my best friend', 'positive')]
neg_tweets = [('I do not like this car', 'negative'), ('This view is horrible', 'negative'), ('I feel tired this morning', 'negative'), ('I am so sad today', 'negative'), ('He is my worst enemy', 'negative')]

# 特征提取函数
def word_feats(words):
    return dict([(word, True) for word in words])

# 构建数据集
pos_features = [(word_feats(word_tokenize(tweet)), sentiment) for (tweet, sentiment) in pos_tweets]
neg_features = [(word_feats(word_tokenize(tweet)), sentiment) for (tweet, sentiment) in neg_tweets]
train_set = pos_features + neg_features

# 训练分类器
classifier = NaiveBayesClassifier.train(train_set)

# 测试分类器
test_tweet = 'I love this view'
test_feature = word_feats(word_tokenize(test_tweet))
print(classifier.classify(test_feature))

# 测试分类器准确率
test_set = pos_features[:2] + neg_features[:2]
print('Accuracy:', accuracy(classifier, test_set))
