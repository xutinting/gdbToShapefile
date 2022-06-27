from config import PATHS
from util import checkcountyDir

input_path = PATHS['input_path']

# 测试county文件名是否对应
JBNTpath = input_path + '/' + 'JBNT'
checkcountyDir(JBNTpath)