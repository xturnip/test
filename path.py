import os
import os.path
import xml.dom.minidom

path = 'E:\\train\\66'
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        print(xmlFile)

        # TODO
        # xml文件读取操作

        # 将获取的xml文件名送入到dom解析
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 最核心的部分,路径拼接,输入的是具体路径
        root = dom.documentElement
        # 获取标签对name/pose之间的值
        pose = root.getElementsByTagName('path')
        name = root.getElementsByTagName('filename')
        # 原始信息
        print('原始信息')
        n0 = name[0]
        print(n0.firstChild.data)
        p0 = pose[0]
        print(p0.firstChild.data)

        # 修改
        p0.firstChild.data = 'E:\\train\\66\\' + n0.firstChild.data
        # 打印输出
        print('修改后的 pose')
        print(p0.firstChild.data)
        print('~~~~~')
        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('写入name/pose OK!')
