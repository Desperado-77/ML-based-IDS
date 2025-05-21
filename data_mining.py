import os
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

ImagePath = pathlib.Path('.img')
ImagePath.mkdir(parents=True, exist_ok=True)

def display_image(image_path):
   # img = plt.imread(image_path)
   # plt.imshow(img)
   # plt.axis('off')
   # plt.show()
   return 1


# （button 1）
def button1():
    image_path = '.img/button1.png'
    display_image(image_path)
    return image_path
# （button 2）
def button2():
    image_path = '.img/button2.png'
    display_image(image_path)
    return image_path
# （button 3）
def button3():
    image_path = '.img/button3.png'
    display_image(image_path)
    return image_path
# （button 4）
def button4():
    image_path = '.img/button4.png'
    display_image(image_path)
    return image_path
# （button 5）
def button5():
    image_path = '.img/button5.png'
    display_image(image_path)
    return image_path
# （button 6）
def button6():
    image_path = '.img/button6.png'
    display_image(image_path)
    return image_path

# （第一个GO）
def m1():  # 第一个模型
    image_path = '.img/model1.png'
    display_image(image_path)
    return image_path
def m2():  # 第二个模型
    image_path = '.img/model2.png'
    display_image(image_path)
    return image_path
def m3():  # 第三个模型
    image_path = '.img/model3.png'
    display_image(image_path)
    return image_path

# 绘制混淆矩阵（第二个GO）
def matrix1():  # 下拉框选项1 决策树
    image_path = '.img/matrix1.png'
    display_image(image_path)
    return image_path
def matrix2():  # 下拉框选项2 逻辑回归
    image_path = '.img/matrix2.png'
    display_image(image_path)
    return image_path
def matrix3():  # 下拉框选项3 人工神经网络
    image_path = '.img/matrix3.png'
    display_image(image_path)
    return image_path

# 绘制各个模型的准确率比较图（第三个GO）
def comparison1():
    image_path = '.img/comparison1.png'
    display_image(image_path)
    return image_path
# 绘制误报率和漏报率比较图（第四个GO）
def comparison2():
    image_path = '.img/comparison2.png'
    display_image(image_path)
    return image_path