# -*- coding: utf-8 -*-
def analyze_text(text):
    """
    分析文本中字符频率（区分大小写，过滤空格），并按“频率降序 + 字符升序”排列
    参数:
    text - 输入的字符串
    返回:
    list - 按规则排序的字符列表
    """
    # 过滤空格
    text = text.replace(" ", "")
    # 统计字符频率
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    # 按“频率降序 + 字符升序”严格排序
    sorted_items = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))
    return [char for char, freq in sorted_items]

if __name__ == "__main__":
    print("文本字符频率分析器")
    print("================")
    print("请输入一段文本（输入空行结束）：")
    
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    text = "\n".join(lines)
    if not text.strip():
        print("未输入有效文本！")
    else:
        sorted_chars = analyze_text(text)
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))
        print("\n提示：尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
