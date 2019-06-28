from PIL import Image
import os

'''
利用python进行图片的九宫格处理：
python图像处理库PIL——pillow，通过pillow可以实现图像压缩和图像处理等各种操作
思路：
    1. 读取到原图片，获取图片尺寸后，将宽高对比，生成以白色为背景的大正方形图
    2. 将大正方形图按照3*3比例进行切割，生成9个小正方形图
    3. 分别生成9张小正方形图片
'''

def fill_images(image):
    # 填充正方形白色背景图片

    # 获取图片的宽高
    width, height = image.size

    # 对比宽和高哪个大
    side = max(width, height)

    #新生成的图片式正方形的，边长取大的，背景设置为白色
    new_image = Image.new(image.mode, (side, side), color='white')

    # 根据尺寸不同，将原图片放入新建的空白图片中部
    if width > height:
        new_image.paste(image, (0, int((side - height) / 2)))
    else:
        new_image.paste(image, (int((side - width) / 2), 0))
    return new_image

def cut_images(image):
    # 切割大正方形

    width, height = image.size

    # 三分之一正方形线像素
    one_third_width = int(width / 3)

    # 保存每一个小切图的区域
    box_list = []

    '''
    切图区域是矩形，位置由对角线的两个点（左上、右下）确定，
    而 crop() 实际要传入四个参数（left， upper， right， lower）
    '''
    for x in range(3):
        for y in range(3):
            left = x * one_third_width # left pixel
            upper = y * one_third_width # up pixel

            right = (x + 1) * one_third_width # right pixel
            lower = (y + 1) * one_third_width # down pixel

            box = (left, upper, right, lower)
            box_list.append(box)

    # 调用crop函数进行图像复制
    image_list = [image.crop(box) for box in box_list]
    return image_list

def save_images(image_list):
    '''
    保存九张图片
    os.path.abspath 获得文件当前的绝对路径
    ospath.dirname 获得文件的父目录
    '''
    output_path = os.path.abspath(os.path.dirname(__file__))   
    for index, image in enumerate(image_list):
        image.save(f"{output_path}/{index + 1}.png", "PNG")

def run():
    input_path = input('请输入图片的路径：\n')
    image= Image.open(input_path)
    image = fill_images(image)
    image_list =cut_images(image)
    save_images(image_list)

if __name__ == '__main__':
    run()

