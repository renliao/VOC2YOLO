 
import os
import random 
random.seed(0)
 
xmlfilepath='D:\\Projects\\insect\\Annotations\\train_val'
saveBasePath='D:\\Projects\\insect\\ImageSets\\main'
val_percent = 0.2#从训练集中选取20%作为验证集
temp_xml = os.listdir(xmlfilepath)
print(len(temp_xml),temp_xml[0])
total_xml = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)
print(len(total_xml),total_xml[0])
num=len(total_xml)  
train_list=range(num)  
val_num=int(num*val_percent)  
val_list= random.sample(train_list,val_num)  
 
print("train size",num)
print("val size",val_num)
print(len(train_list),len(val_list))
ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w')  
fval = open(os.path.join(saveBasePath,'val.txt'), 'w')  
for i in train_list:  
    name=total_xml[i][:-4]+'\n'
    ftrain.write(name)
    if i in val_list:  
        fval.write(name)    
ftrain.close()  
fval.close()  
