import os

PATH = '/Users/gzw/Documents/workspace/python'

def mkdir(dir):
    try:
        path = os.path.join(PATH,dir)
        print(os.mkdir(path))
        return path
    except :
        return path

def mkfile(path,filename,content):
    filePath = os.path.join(path,filename)
    with open(filePath,'w') as f:
        f.write(content)
    return filePath

