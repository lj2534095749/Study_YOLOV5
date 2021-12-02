import shutil
import os

base_path = r'D:\MachineLearning\Code\Study_YOLOV5\datasets\DongYing-Product'
labels_path = base_path + r'\labels'
annotations_path = base_path + r'\Annotations'
segmentation_path = base_path + r'\Segmentation'

file_List = ["train", "val", "test"]
for file in file_List:
    if not os.path.exists(base_path + '/images/%s' % file):
        os.makedirs(base_path + '/images/%s' % file)
    if not os.path.exists(base_path + '/labels/%s' % file):
        os.makedirs(base_path + '/labels/%s' % file)

    f = open(base_path + '/%s.txt' % file, 'r')
    lines = f.readlines()
    for line in lines:
        line = "/".join(line.split('/')[-5:]).strip()
        shutil.copy(line, base_path + "/images/%s" % file)
        line = line.replace('JPEGImages', 'labels')
        line = line.replace('jpg', 'txt')
        shutil.copy(line, base_path + "/labels/%s" % file)
