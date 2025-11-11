# -*- coding: utf-8 -*-
# 在此文件处编辑代码
def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    
    参数:
    text - 输入的字符串
    
    返回:
    list - 按字符频率降序排列的字符列表
    """
    # 只保留字母和汉字，并将字母转换为小写
    filtered_text = []
    for char in text:
        if char.isalpha() or '\u4e00' <= char <= '\u9fff':  # 只保留字母和汉字
            if char.isalpha():
                filtered_text.append(char.lower())
            else:
                filtered_text.append(char)
    
    # 统计字符频率
    char_count = {}
    for char in filtered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 按频率降序排序，如果频率相同，按字符本身升序排列
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    # 返回字符列表
    return [char for char, count in sorted_chars]

# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("==================")
    print("请输入一段文本（输入空行结束）：")
    
    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    # 合并输入文本
    text = "\n".join(lines)
    
    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)
        
        # 打印结果
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))
        
        # 提示用户比较不同语言
        print("\n提示：尝试输入中英文文章片段，观察字符频率差异")
