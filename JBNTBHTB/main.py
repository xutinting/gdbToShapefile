# -*- coding: UTF-8 -*-
import os
import arcpy
from util import coordinate_list,getCitycode
from config import PATHS

input_path = PATHS['input_path']
output_path = PATHS['output_path']

n = 0
for coordinate in coordinate_list:
    city = coordinate['city']
    city_code = getCitycode(city)
    county_code = coordinate['county_code']
    county = coordinate['county']
    coordinate_name = coordinate['name']
    wkid = coordinate['wkid']

    inWorkspace = input_path + '/' + 'JBNT' + '/' + str(city_code) + city + '/' + county_code + county +'/'+  u'1.矢量数据'
    
    if (os.path.exists(inWorkspace)):
        if(county_code == '511702'):
            BHTB_shp = inWorkspace + '/' + county_code + '2015JBNTBHTB.shp'
        else:
            BHTB_shp = inWorkspace + '/' + county_code + '2014JBNTBHTB.shp'

        outWorkspace = output_path  + '/' + str(city_code) + city + '/' + county_code + county
        transWkidBHTB = outWorkspace + '/' + county_code + 'JBNTBHTB.shp'

        if not os.path.exists(outWorkspace):
            os.makedirs(outWorkspace)
        arcpy.env.workspace = inWorkspace
        # 检查自定义坐标系，并纠正
            # 获取原始数据shp文件空间参考
        spatialRef = arcpy.Describe(BHTB_shp).spatialReference
        spatialRefWkid = spatialRef.factoryCode
            # 判断wkid是否对应并纠正
        if(os.path.exists(transWkidBHTB)):
            print("already processed!")
        else:
            if not (spatialRefWkid == wkid):
                n = n + 1
                print(n)
                print(city)
                print(county)
                newSrRef = arcpy.SpatialReference(wkid)
                arcpy.Project_management(BHTB_shp,transWkidBHTB,newSrRef)
                print(arcpy.Describe(transWkidBHTB).spatialReference.factoryCode)
                print("--------------------------------------")
            else:
                arcpy.Copy_management(BHTB_shp,transWkidBHTB,"")
        # 合并图层
            # 筛选补划图斑
        BH_shp = input_path + '/' + u'四川占用补划20220530' + '/' + u'补划图斑.shp'
        BHQ_shp = input_path + '/' + inWorkspace + '/' + county_code + '2014JBNTBHQ.shp'
        arcpy.MakeFeatureLayer_management(BH_shp,'BH_lyr')
        intersectBH = arcpy.SelectLayerByLocation_management('BH_lyr',"INTERSECT",transWkidBHTB)
        
        outBHTB = outWorkspace + '/' + county_code + '2022JBNTBHTB.shp'
        erase_shp = input_path + '/' + u'四川占用补划20220530' + '/' + u'占地项目.shp'
        if (intersectBH):
            # 定义合并字段      
            fieldMappings = arcpy.FieldMappings()
            fieldMappings.addTable()
            unite_shp = outWorkspace + '/' + county_code + 'JBNT_unite.shp'
            arcpy.Merge_management([intersectBH,transWkidBHTB],unite_shp,fieldMappings)
        else:  
            arcpy.Erase_analysis(transWkidBHTB,erase_shp,outBHTB)


print("-------------------------Done!")

# 擦除图层

# 结果按行政区划目录输出
