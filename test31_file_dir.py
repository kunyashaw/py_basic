# os.path
# pathlib
import os
print(os.path.abspath('.'))
print(os.path.abspath('..'))
# 判断文件是否存在
print(os.path.exists('F:\projects'))
print(os.path.isfile('F:\projects'))
print(os.path.isdir('F:\projects'))
# 路径的拼接
print(os.path.join('F:\projects','python','docs'))#F:\projects\python\docs
print(os.path.join('F:\projects','\python','docs'))#F:\python\docs
print(os.path.join('F:\projects','D:\python','docs'))#D:\python\docs

# pathlib
from pathlib import Path
p = Path('.')#将.封装下
print(p.resolve())# 得到p对应的绝对路径
print(p.is_dir())
# pathlib可以用来新建一个目录
p = Path('./test')
Path.mkdir(p) #创建目录
p = Path('./test1/test2')
Path.mkdir(p,parents=True) #创建目录