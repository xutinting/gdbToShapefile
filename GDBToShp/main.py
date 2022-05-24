# -*- coding: UTF-8 -*-
from sqlite3 import Cursor
import arcpy
import os
from config import PATHS
from util import getGDBs,admin_codes


input_path = PATHS['input_path']
output_path = PATHS['output_path']

# read gdb file path
gdblist = getGDBs()
gdb = gdblist[0]

# repair gdb file
# geodatabase = gdb
# output_location = input_path
# recovered_name = "recoveredWhistler.gdb"
# arcpy.RecoverFileGDB_management(geodatabase, output_location, recovered_name)

# 测试
arcpy.env.workspace = gdb

print('Processing................. ')

for admin_code in admin_codes:
    # create directory
    city = admin_code['City']
    county = admin_code['County']
    county_code = admin_code['CountyCode']
    county_path = (output_path + '/' + city + '/' + county_code + county)
    if not os.path.exists(county_path):
        os.makedirs( county_path )
    # 获取gdb要素
    feature_datasets = arcpy.ListDatasets('','') + ['']
    feature_classes = arcpy.ListFeatureClasses('','',feature_datasets)
    for fcp in feature_classes:
        # choose & convert gdb
        in_features = gdb + "/" + fcp
        out_feature_class = county_path + "/" + "STBHHX_2019.shp"
        where_clause = "行政区划代码 = " + county_code
        arcpy.Select_analysis(in_features,out_feature_class,where_clause)

print("-----------------Done!")