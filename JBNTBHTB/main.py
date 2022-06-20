# -*- coding: UTF-8 -*-
import os
import io
import arcpy
from util import coordinate_list,getCitycode
from config import PATHS,workPath

arcpy.env.workspace = workPath
input_path = PATHS['input_path']
output_path = PATHS['output_path']
# JBNT图层路径
JBNT_path = input_path + '/' + 'JBNT'

n = 0
for coordinate in coordinate_list:
    city = coordinate['city']
    city_code = getCitycode(city)
    county_code = coordinate['county_code']
    county = coordinate['county']
    coordinate_name = coordinate['name']
    wkid = coordinate['wkid']

    arcpy.env.workspace = JBNT_path
    # if(county == u"大邑县"):
    #     n = n + 1
    #     print(city)
    #     print(city_code)
    #     print(county_code)
    #     print(county)
    #     print(coordinate_name)
    #     print(wkid)
    #     print(n)
    #     print("-----------------------")
    
    # 检查自定义坐标系，并纠正
    workSpace = input_path + '/' + 'JBNT' + '/' + str(city_code) + city + '/' + county_code + county +'/'+  '1.矢量数据'
    shapefileJBNT = workSpace + '/' + county_code + '2014JBNTBHTB.shp'
    if(os.path.exists(shapefileJBNT)):
        # 获取shp空间参考
        spatialRef = arcpy.Describe(shapefileJBNT).spatialReference
        spatialName = spatialRef.name
        spatialRefWkid = spatialRef.factoryCode
        # 判断wkid是否对应并纠正
        if not (spatialRefWkid == wkid):
            new_spatialRef = arcpy.SpatialReference(wkid)
            arcpy.DefineProjection_management(shapefileJBNT,new_spatialRef)
    # 创建文件夹 
    # county_path = (output_path + '/' + str(city_code) + city + '/' + county_code + county)
    # if not os.path.exists(county_path):
    #     os.makedirs(county_path)


print("-------------------------Done!")



# 合并图层(将新增基本农田图层合并到基本农田图层)
# unite_cd = input_path + '/' + u'成都市边界' +'/'+ u'成都市_510100_子_边界.shp'
# unite_cq = input_path + '/' + u'重庆市边界'+ '/' + u'重庆市_500000_子_边界.shp'
# unite_result = output_path + '/' + 'result.shp'
# arcpy.Merge_management([unite_cd, unite_cq], unite_result)

# 擦除图层（将项目区占用图层从基本农田图层擦除）


# 将结果按行政区划目录输出（按四川行政区划目录存储成果）