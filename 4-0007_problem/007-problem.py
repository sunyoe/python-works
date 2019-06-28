import sys,os,re
'''
 该脚本功能：根据目录中自己写过的程序，统计出写过多少行代码。包括空行和注释，并分别列出来。
    未成功
 sys库：包含一些函数方法和变量——用来处理python运行时配置和资源，从而可以与当前程序之外的系统环境进行交互
    读入、读出数据，获取参数，退出当前进程等
 os库：负责程序和操作系统的交互，提供了访问操作系统底层的接口
    比如路径、环境变量等方面
 re库：用于字符串匹配，正则表达式
'''

def cal(path):
    # os.listdir('filename') 返回指定目录下的所有文件和目录名
    filelist = os.listdir(path)

    # print filelist
    # xxx.endswith('') 判断文本是否以某个或者某几个字符结束
    filelist = (item for item in filelist if item.endswith('.py'))
    ret = [0,0,0]
    for item in filelist:
        res = calfile(path, item)
        for i in (0,1,2):
            ret[i] += res[i]
    return tuple(ret)
    # tuple 元组


def calfile(path, filename):
    totline = 0
    blankline = 0 # 空白行
    commentline = 0 # 解释行
    fileobj = open(path +filename, 'r')
    linelist = fileobj.readlines()
    totline = len(linelist)
    for line in linelist:
        # re.compile() 返回的是一个匹配对象
        pattern = re.compile(r'(\s*)#')
        pattern1 = re.compile(r'(\s*)$')
        if pattern.match(line):
            commentline += 1
        if pattern1.match(line):
            blankline += 1
    fileobj.close()
    return totline,blankline,commentline


'''
下面的部分应该都是在处理输入路径的问题，但是处理的不好
sys.argv[] 实现从程序外部向程序传递参数；从外部获得的是一个列表，应该说这是一个分片操作
sys.argv[0] 表示代码本身文件路径
sys.argv[1] 表示获取用户输入的参数（从第二位开始的输入参数）
'''
#path = '../nine-segmentation/'
path = sys.argv[1]
data = cal(path)
dic = dict(zip(['total line', 'blank line', 'comment line'], list(data)))
print(dic)