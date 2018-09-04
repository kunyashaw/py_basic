# 模块是在代码量变得相当大之后，为了将需要重复使用的有组织的代码段放在一起，这部分代码可以附加到先用的程序中，附加的过程叫做导入
# 直接引入一个模块
import os
print(os.environ)
# 从模块中引入一个东西，比如方法
from time import sleep
sleep(1)
# 引入自定义模块
import test21_mymodule 
test21_mymodule.printMe()
import test21_mymodule  as t
t.printMe()
