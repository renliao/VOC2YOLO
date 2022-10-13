'''
该代码用于按照split_labels.py的划分结果，生成images and labels DIR
'''
import os
import shutil
from tqdm import tqdm

SPLIT_PATH = 'D:\\Projects\\insect_yolo\\transformed\\split_txt\\'
IMGS_PATH = 'D:\\Projects\\insect_yolo\\before_transform\\JPEGImages\\'
TXTS_PATH = 'D:\\Projects\\insect_yolo\\transformed\\labels_txt\\'
 
TO_IMGS_PATH = 'D:\\Projects\\insect_yolo\\transformed\\images'
TO_TXTS_PATH = 'D:\\Projects\\insect_yolo\\transformed\\labels'
 
data_split = ['train.txt','val.txt','test.txt']
to_split = ['train','val','test']

for index, split in enumerate(data_split):
    split_path = os.path.join(SPLIT_PATH, split)
    # print(split_path)
    to_imgs_path = os.path.join(TO_IMGS_PATH, to_split[index])
    if not os.path.exists(to_imgs_path):
        os.makedirs(to_imgs_path)
    # print(to_imgs_path)
    to_txts_path = os.path.join(TO_TXTS_PATH, to_split[index])
    if not os.path.exists(to_txts_path):
        os.makedirs(to_txts_path)
    # print(to_txts_path)
    f = open(split_path, 'r')
    count = 1
    lineres=[]
    for line in tqdm(f.readlines(), desc="{} is copying".format(to_split[index])):
        # 复制图片
        src_img_path = os.path.join(IMGS_PATH, line.strip() + '.jpeg')
        dst_img_path = os.path.join(to_imgs_path, line.strip() + '.jpeg')
        # print(src_img_path,dst_img_path)
        if os.path.exists(src_img_path):
            shutil.copyfile(src_img_path, dst_img_path)
        else:
            print("error file: {}".format(src_img_path))
 
        # 复制txt标注文件
        src_txt_path = os.path.join(TXTS_PATH, line.strip() + '.txt')
        dst_txt_path = os.path.join(to_txts_path, line.strip() + '.txt')
        if os.path.exists(src_txt_path):
            shutil.copyfile(src_txt_path, dst_txt_path)
        else:
            print("error file: {}".format(src_txt_path))