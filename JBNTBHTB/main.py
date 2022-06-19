# -*- coding: UTF-8 -*-
import os
import arcpy
from util import coordinate_list
from config import PATHS,workPath

arcpy.env.workspace = workPath
input_path = PATHS['input_path']
output_path = PATHS['output_path']


# 检查自定义坐标系，并纠正

# 合并图层(将新增基本农田图层合并到基本农田图层)
unite_cd = input_path + '/' + u'成都市边界' +'/'+ u'成都市_510100_子_边界.shp'
unite_cq = input_path + '/' + u'重庆市边界'+ '/' + u'重庆市_500000_子_边界.shp'
unite_result = output_path + '/' + 'result.shp'

arcpy.Merge_management([unite_cd, unite_cq], unite_result)
print("-------------------------Done!")
# 擦除图层（将项目区占用图层从基本农田图层擦除）

# 将结果按行政区划目录输出（按四川行政区划目录存储成果）

# region
# for coordinate in coordinate_list:
#     city = coordinate['city']
#     county_code = coordinate['county_code']
#     county = coordinate['county']
#     # 创建文件夹
#     county_path = (output_path + '/' + city + '/' + county_code + county)
#     if not os.path.exists(county_path):
#         os.makedirs(county_path)

#     name = coordinate['name']
#     wkid = coordinate['wkid']

# 图层名：
# output_name = county_code + '2022JBNTBHTB'
#     # 

# endregion