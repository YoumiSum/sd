import pandas as pd


def main():
    # 读取表格
    excel_path = '../../../data/background/图片提示词.xlsx'
    df = pd.read_excel(excel_path)

    # 读取英文提示词列的内容
    prompt = df['英文提示词'].values.tolist()

    # 保留第一个逗号以后得内容
    for i in range(len(prompt)):
        current_prompt = prompt[i]
        current_prompt = current_prompt.split(',')[1:]

        # 删除所有空格
        current_prompt = [x.strip() for x in current_prompt]

        modified_prompt = ', '.join(current_prompt)
        prompt[i] = modified_prompt

    # 将修改后的内容写入表格
    df['英文提示词'] = prompt
    df.to_excel('../../../data/background/图片提示词.xlsx', index=False)


if __name__ == '__main__':
    main()
