from models.translator import Translator, TranslatorConfig
import pandas as pd
import json
from datasets import load_dataset, Image
from tqdm import tqdm

# 先简单测试翻译 -> 已测试成功
config = TranslatorConfig(model_id='./models/translator/opus-mt-zh-en')
# # 随便翻译一句
translator = Translator(config)

translator.to('cuda')
# output_text = translator('你好')

# print(output_text.translated_text)

# 翻译表格内容
# df = pd.read_excel('../../data/sucai/图片说明.xlsx', sheet_name='Sheet2')
# # 新增一列，用于存放翻译后的内容
# prompt = []
# for i in tqdm(range(len(df))):
#     text = ''
#     text += df['大类别'][i] + ','
#     text += df['小类别'][i] + ','
#     text += df['标签'][i]
#     output_text = translator(text)
#     prompt.append(output_text.translated_text[:-1])

# # 去掉句号
# df['英文提示词'] = prompt

# df.to_excel('../../data/sucai/图片提示词.xlsx', index=False)
