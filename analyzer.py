from textblob import TextBlob
from snownlp import SnowNLP
import re

def contains_chinese(text):
    """判断字符是否包含中文"""
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def analyze_sentiment(text):
    """
    分析输入文本的情感倾向
    中文：snownlp模型
    英文：textblob模型
    返回：情感类别、极性分数
    """
    text = text.strip()
    if not text:
        return "中性 ", 0.0
    
    #中文文本
    if contains_chinese(text):
        s = SnowNLP(text)
        score = s.sentiments
        if score > 0.6:
            return "积极 ", round(score, 3)
        elif score < 0.4:
            return "消极 ", round(score, 3)
        else:
            return "中性 ", round(score, 3)
    
    #英文文本
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 ~ 1，负面~正面
    if polarity > 0.1:
        sentiment = "积极 "
    elif polarity < -0.1:
        sentiment = "消极 "
    else:
        sentiment = "中性 "
    return sentiment, round(polarity, 3)