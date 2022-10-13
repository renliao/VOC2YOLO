'''
经过上一步的annotations_cocoxml2yolotxt.py，您已经生成了yolo格式的labels(*.txt);
接下来就需要将labels划分为train val test三个部分；
本项目所用的数据集划分策略：train=0.8 val=0.1 test=0.1,该比例可由您自行配置
''' 
import os
import random 
random.seed(0)
 
#划分比例
train_p=0.8
val_p=0.1
test_p=0.1
#(*txt)labels的加载路径
labels_path='D:\\Projects\\insect_yolo\\transformed\\labels_txt'
#划分结果的保存路径
saverst_Path='D:\\Projects\\insect_yolo\\transformed\\split_txt'
temp_txt = os.listdir(labels_path)
# print(len(temp_txt),temp_txt[0])
#从labels_path中刷选一遍*.txt格式的文件，防止其他文件干扰
total_txt = []
for txt in temp_txt:
    if txt.endswith(".txt"):
        total_txt.append(txt)
num=len(total_txt)
print("total number of labels(*.txt) is {:.0f}, a example is {}".format(num,total_txt[0]))
#按比例划分
train_num=int(train_p*num)
val_num=int(val_p*num)
test_num=int(test_p*num)
print("train num is {:.0f}, val num is {:.0f}, test num is {:.0f}".format(train_num,val_num,test_num))
#create train.txt
train_txt=random.sample(total_txt,train_num)
# print(len(train_txt),train_txt[0])
ftrain = open(os.path.join(saverst_Path,'train.txt'), 'w')
for i in train_txt:
    name=i[0:-4]+'\n'
    ftrain.write(name)
ftrain.close()
#create val.txt
res_txt=[]#total_txt-train_txt
for i in total_txt:
    if not (i in train_txt):
        res_txt.append(i)
# print(len(res_txt))
val_txt=random.sample(res_txt,val_num)
# print(len(val_txt),val_txt[0])
fval = open(os.path.join(saverst_Path,'val.txt'), 'w')
for i in val_txt:
    name=i[0:-4]+'\n'
    fval.write(name)
fval.close()
#create test.txt
test_txt=[]#res_txt-val_txt
for i in res_txt:
    if not (i in val_txt):
        test_txt.append(i)
# print(len(test_txt))
ftest = open(os.path.join(saverst_Path,'test.txt'), 'w')
for i in test_txt:
    name=i[0:-4]+'\n'
    ftest.write(name)
ftest.close()
print("the output is in {}".format(saverst_Path))