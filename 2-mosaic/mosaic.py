import numpy as np
from PIL import Image

def tp_pixelBlock(pixel, Start_coordinate, End_coordinate):
    '''
    pixel:单位像素块的元素大小
    Start_coordinate:处理的起始坐标（元组形式）
    End_coordinate:处理的终止坐标（元组形式）
    处理思想：取所选范围块的中间值的RGB值，对所选范围块的RGB进行重新赋值
    '''
    # 导入图片
    data = Image.open("./photo/test.jpg")

    # 将图像转换化为Numpy数组进行下一步的处理
    im1 = np.array(data)
    
    # 指定一个处理范围，并对该范围内的每一个坐标（像素）点进行像素化的处理
    for y in range(Start_coordinate[1], End_coordinate[1], pixel):
        for x in range(Start_coordinate[0], End_coordinate[0], pixel):
            # x 横向像素点坐标，y 纵向像素点坐标；pixel 要以多大的像素块来处理这张图像（pixel值越小，像素图越精确）
            im1[y:y + pixel, x:x + pixel] = im1[y + (pixel // 2)][x + (pixel // 2)]

    # 处理完成后，再把Numpy数组转换回图像，并且展示出来
    im2 = Image.fromarray(im1.astype(np.uint8))
    im2.show()

if __name__ == '__main__':
    # 设置好要处理的像素范围，并以多大的像素块来生成最终效果图
    tp_pixelBlock(100, (1000, 1000), (2000, 2000))