import pandas as pd
import json
from datasets import load_dataset, Image

TRIGGER_WORD = 'cmitbg'


def main():
    # 先测试嵌套文件夹是否可行 -> 已测试成功
    # 读取表格，构建数据集
    df = pd.read_excel('../../../data/background/图片提示词.xlsx')

    # 先生成数据字典，再生成jsonl文件
    data = []
    for i in range(len(df)):
        img_path = df['图片路径'][i]
        img_path = img_path.split('/')[2:]

        img_path = './' + '/'.join(img_path)

        text = df['英文提示词'][i]

        text = TRIGGER_WORD + ', ' + text

        # 必须有file_name字段
        data.append({'file_name': img_path, 'text': text})

    # 生成jsonl文件
    with open('../../../data/background/metadata.jsonl', 'w',
              encoding='utf-8') as f:
        for d in data:
            json.dump(d, f, ensure_ascii=False)
            f.write('\n')

    # 测试是否可行
    dataset = load_dataset('imagefolder', data_dir='../../../data/background/')

    # 这种方式地址不对，需要使用绝对路径
    # dataset = load_dataset(
    #     'json', data_files='../../data/background/metadata.jsonl').cast_column(
    #         'file_name', Image())

    print(dataset['train'][0])


if __name__ == '__main__':
    main()
