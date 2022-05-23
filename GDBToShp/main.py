# -*- coding: UTF-8 -*-
import arcpy
import os
from config import PATHS
from util import getGDBs,listFeatureDatasets,admin_codes


# 输入文件夹路径
input_path = PATHS['input_path']
# 输出文件夹路径
output_path = PATHS['output_path']

# read gdb file path
gdblist = getGDBs()
gdb = gdblist[0]



for admin_code in admin_codes:
    # 创建目录
    city = admin_code['City']
    county = admin_code['County']
    county_code = admin_code['CountyCode']
    county_path = (output_path + '\\' + city + '\\' + county_code + county)
    if not os.path.exists(county_path):
        os.makedirs( county_path )
    # 选择图斑
    [message, featuresDatasetsNames,gdbName] = listFeatureDatasets(gdb)
    in_features = gdb
    out_feature_class = county_path + "\\" + "STBHHX_2019.shp"
    where_clause = "行政区划代码 = " + county_code
    arcpy.Select_analysis(in_features,out_feature_class,where_clause)