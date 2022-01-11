import io
import os
import sys

import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from test import *

global i, num  # 全局变量i用来存储当前显示的图片编号,num是图片总数
global alpha    #val_por是鼠标在进度条的位置，alpha是对比度的范围
i = 0
num = 0
alpha = 2
item = 'PythonTab'
array = [item] * 10  # 创建一个有10个元素的列表，存储图片路径信息
file_dir = "E:\\images\\"
for root, dirs, files in os.walk(file_dir):
    for name in files:
        filename = os.path.join(root, name)
        array[num] = filename
        num += 1  # 此时array列表前(num-1)个元素是我们图片的路径(从0开始)


class Myclass(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Myclass, self).__init__(parent)
        self.setupUi(self)
        jpg = QtGui.QPixmap(array[i]).scaled(self.label.width(), self.label.height())  # 默认显示文件夹中第一张图片
        self.label.setPixmap(jpg)
        self.pre_btn.clicked.connect(self.pre_image)
        self.pushButton_2.clicked.connect(self.next_image)

    def pre_image(self):
        global i
        i -= 1
        if i < 0:
            i = num - 1
        jpg = QtGui.QPixmap(array[i]).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        # jpg.setScaledContents(True)   #自适应QLabel大小

    def next_image(self):
        global i
        i += 1
        if i >= num:
            i = 0
        jpg = QtGui.QPixmap(array[i]).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        # jpg.setScaledContents(True)   #自适应QLabel大小

    def mouseMoveEvent(self, event):
       # global val_por
        global alpha
        val_por = (event.pos().x() - self.progressBar.x()) / 450  # 获取鼠标在进度条的相对位置
        self.progressBar.setProperty("value", int(val_por * self.progressBar.maximum()))  # 改变进度条的值
        alpha = alpha * val_por
        img = cv2.imread(array[i])
        jpg = np.clip((alpha * img), 0, 255)  # 将对比变化后的图片赋给jpg
        cv2.imwrite("E:/images_contrast/out2.jpg", jpg)
        QImg = QtGui.QPixmap('E:/images_contrast/out2.jpg').scaled(self.label.width(), self.label.height())
        self.label.setPixmap(QImg)
        #self.update()
        alpha = 2
