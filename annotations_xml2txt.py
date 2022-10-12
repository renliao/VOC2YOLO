'''
该代码用来从 dir/*.xml 生成 output/*.txt;
从xml文件中提取对应图片的注释信息，并将其按yolo训练所需的格式存储在*.txt文件中，
一个xml文件生成一个对应的txt文件
'''
import os.path
import xml.etree.ElementTree as ET
class_names = ['Boerner', 'linnaeus', 'armandi' ,'coleoptera' ,'Linnaeus', 'Leconte' ,'acuminatus' ]
 
xmlpath = 'D:\\Projects\\insect\\Annotations\\train_val'  # 原xml路径
txtpath = 'D:\\Projects\\insect\\yolo_txt'  # 转换后txt文件存放路径
files = []
if not os.path.exists(txtpath):
    os.makedirs(txtpath)
 
for root, dirs, files in os.walk(xmlpath):
    pass
print("current dir is {}\nhis subdirs are {}\nnumber of files in current dir is {}\n".format(root,dirs,len(files)))
number = len(files)
print(type(files[0]),files[0],files[0][0],files[0][1],files[0][2],files[0][3],files[0][4])#files[i] <--> *.xml

i = 0
while i < number:
    name = files[i][0:-4]
    print(name)
    xml_name = name + ".xml"
    txt_name = name + ".txt"
    xml_file_name = xmlpath + '\\'+ xml_name
    txt_file_name = txtpath + '\\'+txt_name
    print(xml_name,txt_name,xml_file_name,txt_file_name)
    xml_file = open(xml_file_name,encoding='utf-8')
    print(xml_file)
    tree = ET.parse(xml_file)
    print(tree)
    root = tree.getroot()
    print(root)
    image_name = root.find('filename').text
    print(image_name)
    w = int(root.find('size').find('width').text)
    h = int(root.find('size').find('height').text)
    c = int(root.find('size').find('depth').text)
    print("img_width={},img_height={},img_channels={}".format(w,h,c))
    #write info from xml to txt
    obj=[i for i in root.iter('object') ]
    print(obj)

    f_txt = open(txt_file_name, 'w+')
    content = ""

    first = True

    for obj in root.iter('object'):

        name = obj.find('name').text
        class_num = class_names.index(name)
        # class_num = 0

        xmlbox = obj.find('bndbox')

        x1 = int(xmlbox.find('xmin').text)
        x2 = int(xmlbox.find('xmax').text)
        y1 = int(xmlbox.find('ymin').text)
        y2 = int(xmlbox.find('ymax').text)

        if first:
            content += str(class_num) + " " + \
                        str((x1 + x2) / 2 / w) + " " + str((y1 + y2) / 2 / h) + " " + \
                        str((x2 - x1) / w) + " " + str((y2 - y1) / h)
            first = False
        else:
            content += "\n" + \
                        str(class_num) + " " + \
                        str((x1 + x2) / 2 / w) + " " + str((y1 + y2) / 2 / h) + " " + \
                        str((x2 - x1) / w) + " " + str((y2 - y1) / h)

    print(str(i / (number - 1) * 100) + "%\n")
    # print(content)
    f_txt.write(content)
    f_txt.close()
    xml_file.close()
    i += 1