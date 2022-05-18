# -*- coding: UTF-8 -*-
import arcpy
import os.path
from arcpy import env
from config import PATHS as paths
from util import getGDBs

[message,GDBs] = getGDBs()

print(message,GDBs)
# 修改了
# env.workspace = "C:/Users/pc/Desktop/Practice/GDBToShp/input"
# in_features = "四川省生态保护红线.gdb"
# out_feature_class = "C:/Users/pc/Desktop/Practice/GDBToShp/output/STBHHX_200.shp"
# # 阿坝藏族羌族自治州-马尔康市
# countyCode = 201
# where_clause = '"FID" = ' + str(countyCode)
# arcpy.Select_analysis(in_features,out_feature_class,where_clause)
