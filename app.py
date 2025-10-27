# app.py
import streamlit as st
from analyzer import analyze_sentiment
import pandas as pd

st.set_page_config(page_title="Emotion Analyzer", page_icon="💬", layout="centered")

st.title("情感分析器（中英双语）")
st.write("输入一句话（支持中文/英文），模型会返回情感倾向与分数。")

# 单句分析
st.subheader("单句分析")
text = st.text_area("输入文本（单句或多句）：", height=120)
if st.button("分析"):
    sentiment, score = analyze_sentiment(text)
    st.markdown(f"情感判断： {sentiment}  \n分数： {score}")

st.markdown("---")

# 批量文件分析（可选）
st.subheader("批量分析（上传 txt 文件，每行一条）")
uploaded_file = st.file_uploader("上传 .txt 文件", type=["txt"])
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8", errors="ignore").splitlines()
    results = []
    for line in content:
        s, sc = analyze_sentiment(line)
        results.append({"text": line, "sentiment": s, "score": sc})
    df = pd.DataFrame(results)
    st.dataframe(df)
    # 汇总比例
    summary = df['sentiment'].value_counts().to_dict()
    st.write("情感统计：", summary)

st.markdown("---")
st.caption("项目：基于 SnowNLP (中文) 和 TextBlob (英文) 的情感分析演示。上传到 GitHub 后可部署到 Streamlit Cloud。")