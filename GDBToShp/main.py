# -*- coding: utf-8 -*-
import arcpy
import os.path
from arcpy import env
from config import PATHS as paths
from util import getGDBs

# read gdb file
[message,GDBs] = getGDBs()
print(message,GDBs)

City = "City"
County = "County"
CountyCode = "CountyCode"

CodeObjects = {
    1:{City : "成都市", County : "锦江区",CountyCode : "510104"},
    2:{City : "成都市", County : "青羊区",CountyCode : "510105"},
}

print(CodeObjects[1][City])

# env.workspace = "C:/Users/pc/Desktop/Practice/GDBToShp/input"
# in_features = "四川省生态保护红线.gdb"
# out_feature_class = "C:/Users/pc/Desktop/Practice/GDBToShp/output/STBHHX_200.shp"
# # 阿坝藏族羌族自治州-马尔康市
# countyCode = 201
# where_clause = '"FID" = ' + str(countyCode)
# arcpy.Select_analysis(in_features,out_feature_class,where_clause)
