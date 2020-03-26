import os
import cv2
import math
import sys
import xml.etree.ElementTree as ET


def view_bar(message, num, total):
    """
    Display the schedule
    :param message:
    :param num:
    :param total:
    :return:
    """
    rate = num / total
    rate_num = int(rate * 40)
    rate_nums = math.ceil(rate * 100)
    r = '\r%s:[%s%s]%d%%\t%d/%d' % (message, ">" * rate_num, " " * (40 - rate_num), rate_nums, num, total,)
    sys.stdout.write(r)
    sys.stdout.flush()
    print('\r')


def create_save_folder(save_dir):
    """
    Create the VOC format dataset save dir
    :param save_dir:
    :return:
    """
    voc_train_ann = os.path.join(save_dir, 'train', 'Annotations')
    voc_train_jpg = os.path.join(save_dir, 'train', 'JPEGImages')
    voc_test_ann = os.path.join(save_dir, 'test', 'Annotations')
    voc_test_jpg = os.path.join(save_dir, 'test', 'JPEGImages')
    if not os.path.exists(voc_train_ann):
        os.makedirs(voc_train_ann)
    if not os.path.exists(voc_train_jpg):
        os.makedirs(voc_train_jpg)
    if not os.path.exists(voc_test_ann):
        os.makedirs(voc_test_ann)
    if not os.path.exists(voc_test_jpg):
        os.makedirs(voc_test_jpg)
    return voc_train_ann, voc_train_jpg, voc_test_ann, voc_test_jpg


def get_bbox(img_name):
    """
    Get the bbox from oval
    :param img_name: Label img name in DAGM2007
    :return: xmin, xmax, ymin, ymax
    """
    xmax, xmin, ymax, ymin = 0, 1000, 0, 1000
    src = cv2.imread(img_name)
    for x in range(src.shape[0]):
        for y in range(src.shape[1]):
            if all(src[x, y] == [255, 255, 255]):
                if x > xmax:
                    xmax = x
                if x < xmin:
                    xmin = x
                if y > ymax:
                    ymax = y
                if y < ymin:
                    ymin = y
    ymax, xmax = xmax, ymax
    ymin, xmin = xmin, ymin
    return xmin, xmax, ymin, ymax


def create_xml_file(label_file_path, save_folder, n_id, class_name):
    """
    Write .xml to VOC format dataset
    :param label_file_path: Label img name in DAGM2007
    :param save_folder: Annotation
    :param n_id:
    :param class_name:
    :return:
    """
    img_new_name = '{:06d}'.format(n_id) + '.jpg'
    xmin, xmax, ymin, ymax = get_bbox(label_file_path)
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    for name in root.iter('filename'):
        name.text = '{:06d}'.format(n_id) + '.jpg'
    for name in root.iter('path'):
        name.text = os.path.join(save_folder, img_new_name)
    for obj in root.iter('object'):
        for va in obj.iter('name'):
            va.text = class_name
        for va in obj.iter('xmin'):
            va.text = str(xmin)
        for va in obj.iter('xmax'):
            va.text = str(xmax)
        for va in obj.iter('ymin'):
            va.text = str(ymin)
        for va in obj.iter('ymax'):
            va.text = str(ymax)
    new_xml = '{:06d}'.format(n_id) + '.xml'
    tree.write(os.path.join(save_folder, new_xml))


def write_img(original_folder, name, save_folder, n_id):
    """
    Write image to VOC format dataset
    :param original_folder:
    :param name:
    :param save_folder:
    :param n_id:
    :return:
    """
    img_name = name + '.PNG'
    img_new_name = '{:06d}'.format(n_id) + '.jpg'
    src = cv2.imread(os.path.join(original_folder, img_name))
    cv2.imwrite(os.path.join(save_folder, img_new_name), src)
