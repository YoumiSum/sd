"""这个函数修改jsonl格式到能够读取的格式，主要操作有：
1. 将'\'改为多系统通用的'/'；
2. 如果没有触发词，则额外添加触发词；
函数输出的仍然是jsonl格式文件
"""
import json


def modify_jsonl(jsonl_file, trigger_words=None, save_file=None):
    # 读取jsonl文件
    data = []
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            # 先做一次字符转换，防止json.loads报错，不支持'\'字符
            line = line.replace('\\', '/')
            data.append(json.loads(line))

    # 修改jsonl文件
    new_data = []
    for d in data:
        # 添加触发词
        if trigger_words is not None:
            if not trigger_words.endswith(', '):
                trigger_words += ', '
            d['text'] = trigger_words + d['text']

        new_data.append(json.dumps(d, ensure_ascii=False))

    # 保存文件
    if save_file is None:
        save_file = jsonl_file

    # 保存jsonl文件
    with open(save_file, 'w', encoding='utf-8') as f:
        for line in new_data:
            f.write(line + '\n')


if __name__ == '__main__':
    jsonl_file = '../data/AI海报/metadata.jsonl'
    trigger_words = 'cmit'
    save_file = '../data/AI海报/modified_metadata.jsonl'
    modify_jsonl(jsonl_file, trigger_words, save_file)
