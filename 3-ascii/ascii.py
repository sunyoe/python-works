from PIL import Image
# 管理命令行参数输入的库
import argparse
'''
不足之处：对应比较复杂的图片，这样处理之后的效果可能会不太明显
'''

# 构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file') # 输入文件
parser.add_argument('-o','--output') # 输出文件
parser.add_argument('--width',type = int, default = 80) # 输出字符画宽
parser.add_argument('--height',type = int, default = 80)    # 输出字符画高

# 解析并获取参数
args = parser.parse_args()

# 输入的图片的文件路径
IMG = args.file

# 输出字符画的宽度、高度和路径
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 字符画所使用的字符集，一共70个字符
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# RGB值转字符的函数，alpha值为0时表示图片中该位置为空白
def get_char(r,g,b,alpha = 256):
    # 判断 alpha 值
    if alpha == 0:
        return ' '

    # 获取字符集的长度，这里为70
    length = len(ascii_char)

    # 将 RGB 值转为灰度值 gary，灰度值范围为0-255
    gary = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 灰度值范围为 0-255，而字符集只有70，需要将灰度值映射到指定的字符上
    unit = (256.0 + 1)/ length

    # 返回灰度值对应的字符
    return ascii_char[int(gary/unit)]
'''
图片处理步骤：
1. 首先使用 PIL 的 Image.open 打开图片文件，获得对象image
2. 使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度
    注意：该函数的第二个参数使用 Image.NEAREST，表示输出低质量的图片
3. 遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符
4. 将所有的像素对应的字符拼接在一起成为一个字符串txt
5. 打印输出字符串 txt
6. 如果执行时配置了输出文件，将打开文件将txt输出到文件，如果没有，则默认输出到output.txt文件

注意，通过 PIL 库的 getpixel 获取调用 getchar 时候的参数
char = get_char(*im.getpixel((j,i)))
'''
if __name__ == "__main__":
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 初始化输出的字符串
    txt = ''

    # 遍历图片中的每一行、每一列
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # 将（j,i）坐标的 RGB 像素转为字符后添加到 txt 字符串
            txt += get_char(*im.getpixel((j,i)))
        # 遍历完一行后需要增加换行符
        txt += '\n'
    # 输出到屏幕
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)