import os
import shutil
import time


USB = r'H:\ '.strip()  # u盘的路径
SAVE = r'F:\udisk\ '.strip()  # 存储到的路径
old = []


def copy_file(file, path):
    """
    
    :param file: the file will be copied.
    :param path: the path file will be copied to.
    :return: None
    """
    try:
        if not os.path.exists(path):
            print('创建存储目录', path)
            os.makedirs(path)
        shutil.copy(file, path)
    except Exception:
        print('exception')


def usb_walker():
    """
    traverse the USB.   
    :return: 
    """
    if not os.path.exists(SAVE):
        print('创建存储目录')
        os.mkdir(SAVE)
    print('开始抓取U盘')
    # 创建一个txt文件，用于存取要复制文件的绝对路径。
    f = open(SAVE+time.strftime("%m%d%H%M")+'.txt', 'a')
    # root代表目录路径，dirs代表root下的目录，files代表root下的文件。
    for root, dirs, files in os.walk(USB):
        print(root)
        for file in files:
            # export代表要从U盘复制出来的文件的绝对路径。
            export = os.path.join(root, file)
            f.writelines(export+'\n')
            copy_file(export, root.replace('H:', r'F:\udisk'))
    f.close()


def update():
    """
    judge whether the USB'file is updated
    :return: 
    """
    global old
    new = os.listdir(USB)
    if new == old:
        print('usb没有更新')
        return 0
    else:
        old = new
        return 1


while True:
    if os.path.exists(USB):
        if update():
            usb_walker()
        else:
            print('进入休眠')
            time.sleep(20)
            print('结束休眠')
    else:
        print('usb不存在')


