import os
import os.path
import xml.dom.minidom
def sops():
  path='c:\\Users\\user\\Desktop\\MODIFY\\83\\'   #要修改的文件路径
  files=os.listdir(path)#返回文件夹中的文件名列表
  #print(files)
  s=[]
  count=0
  for xmlFile in files:
    if not os.path.isdir(xmlFile):#os.path.isdir()用于判断对象是否为一个目录
        #如果不是目录，则直接打开
        name1='up'
        print(name1)
        dom=xml.dom.minidom.parse(path+'\\'+xmlFile)
        #print(dom)
        root=dom.documentElement
        newfolder=root.getElementsByTagName('folder')
        #print(newfolder)
        newpath = root.getElementsByTagName('path')
        newname = root.getElementsByTagName('name')
        newname[0].firstChild.data = name1
        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            #print('写入name/pose OK!')
        count=count+1
if __name__ == '__main__':
    sops()
