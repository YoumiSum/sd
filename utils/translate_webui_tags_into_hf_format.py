"""包含所有将SD-WebUI打的txt标签转换为Hugging Face数据集格式的函数。
"""
import os
import json


def translate_webui_tags_into_hf_format(root_dir: str,
                                        img_format: str = 'jpg', img_dir="tags"):
    """将SD-WebUI打的txt标签转换为Hugging Face数据集格式。

    Args:
        root_dir (str): SD-WebUI打的txt标签文件夹路径
        img_format (str, optional): 图像格式. Defaults to 'jpg'.

    Returns:
        None
    """
    data = []
    source_dir = os.path.join(root_dir, img_dir)
    # 遍历文件夹下的所有txt文件
    for txt_file in os.listdir(source_dir):
        if txt_file.endswith('.txt'):
            with open(os.path.join(source_dir, txt_file), 'r',
                      encoding='utf-8') as f:
                lines = f.readlines()

            # 读取txt文件，一般只有一行，如果多行就相加
            prompt = ''
            for line in lines:
                line = line.strip()
                if line == '':
                    continue
                prompt += line

            # 通过txt文件名形成图像文件名
            img_file = txt_file.split('.')[0] + '.' + img_format

            data.append({'file_name': f'./{img_dir}/' + img_file, 'text': prompt})

    with open(os.path.join(root_dir, 'metadata.jsonl'), 'w',
              encoding='utf-8') as f:
        for d in data:
            json.dump(d, f, ensure_ascii=False)
            f.write('\n')


if __name__ == '__main__':
    translate_webui_tags_into_hf_format(r'C:\Users\Youmi\Desktop\youmi\diffusion\genshin_keli\train_img', 'png', img_dir="tags")
