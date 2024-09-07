from PIL import Image
from torchvision import transforms
from typing import Tuple, Any, Union, Optional
import json

json_file = 'D:/data/background/metadata.jsonl'
data_dir = 'D:/data/background/'


def main():
    img_resize = transforms.Resize((768))

    def center_crop(img: Image, size: Tuple[int, int] = (768, 1152)):
        # 这个函数输入PIL格式图像，输出按一定大小中心裁剪的图像，如果某个边比较短，每个通道补像素255
        # img: PIL格式图像
        # size: 输出图像的大小
        # return: PIL格式图像

        # 中心裁剪，如果某个边比较短，每个通道补像素255
        w, h = img.size

        # 如果长和宽均大于等于size，直接裁剪
        if w >= size[1] and h >= size[0]:
            return img.crop(((w - size[1]) // 2, (h - size[0]) // 2,
                             (w + size[1]) // 2, (h + size[0]) // 2))
        else:
            if w / h > size[1] / size[0]:
                # 高度不够，补255
                new_img = Image.new('RGB', (size[1], size[0]), (255, 255, 255))
                new_img.paste(img, (0, (size[0] - h) // 2))
            else:
                # 宽度不够，补255
                new_img = Image.new('RGB', (size[1], size[0]), (255, 255, 255))
                new_img.paste(img, ((size[1] - w) // 2, 0))

        return new_img

    def preprocess_img(img_path: str, save_path: str = None):
        img = Image.open(img_path)
        img = img_resize(img)
        img = center_crop(img)

        if save_path is not None:
            img.save(save_path)
        else:
            img.save(img_path)

    # 遍历文件夹下的所有的图像，先读取jsonl文件，然后读取图像，进行预处理
    # 读取jsonl文件
    with open(json_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        img_path = json.loads(line)['file_name']
        img_path = img_path.split('/')[1:]
        img_path = data_dir + '/'.join(img_path)
        preprocess_img(img_path)


if __name__ == "__main__":
    main()
