import random


def select_random_lines(inputFile, outputFile, num_lines):
    """从文件中随机选取 num_lines 行，且不重复"""
    with open(inputFile, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 确保文件行数足够
    if len(lines) < num_lines:
        raise ValueError("文件行数少于请求的行数")

    # 随机选取 num_lines 个不重复的行
    selected_lines = random.sample(lines, num_lines)

    # 将选取的行写入新文件
    with open(outputFile, 'w', encoding='utf-8') as file:
        file.writelines(selected_lines)


# 使用示例
count = 10000

inputFile = 'data/processed_data/ip_space_data.txt'  # 请替换为你的文件名
outputFile = 'sample/ipTest_' + str(count) + '.txt'

# inputFile = 'data/processed_data/word_data.txt'  # 请替换为你的文件名
# outputFile = 'sample/word_data_' + str(count) + '.txt'

# inputFile = 'sample/ipWord-train.txt'
# outputFile = 'sample/ipWord-test.txt'
select_random_lines(inputFile, outputFile, count)
