from analyzer import analyze_sentiment

print("=== 智能文本情感分析器 ===")
while True:
    text = input("\n请输入一句话（输入 q 退出）：")
    if text.lower() == 'q':
        break
    sentiment, score = analyze_sentiment(text)
    print(f"情感判断：{sentiment}（分数：{score}）")