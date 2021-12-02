import os
import random
import argparse

base_path = r'D:\MachineLearning\Code\Study_YOLOV5\datasets\DongYing-Product'
labels_path = base_path + r'\labels'
annotations_path = base_path + r'\Annotations'
segmentation_path = base_path + r'\Segmentation'

parser = argparse.ArgumentParser()
parser.add_argument('--xml_path', default=annotations_path, type=str, help='input xml label path')
parser.add_argument('--txt_path', default=segmentation_path, type=str, help='output txt label path')
opt = parser.parse_args()

trainval_percent = 1.0
train_percent = 0.9

xmlfilepath = opt.xml_path
txtsavepath = opt.txt_path

total_xml = os.listdir(xmlfilepath)
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

num = len(total_xml)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list_index, tv)
train = random.sample(trainval, tr)

file_trainval = open(txtsavepath + '/trainval.txt', 'w')
file_test = open(txtsavepath + '/test.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')

for i in list_index:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)

file_trainval.close()
file_train.close()
file_val.close()
file_test.close()
