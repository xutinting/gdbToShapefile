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

    inWorkspace = input_path + '/' + 'JBNT' + '/' + str(city_code) + city + '/' + county_code + county +'/'+  '1.矢量数据'
    
    if (os.path.exists(inWorkspace)):
        if(county_code == '511702'):
            BHTB_shp = inWorkspace + '/' + county_code + '2015JBNTBHTB.shp'
        else:
            BHTB_shp = inWorkspace + '/' + county_code + '2014JBNTBHTB.shp'

        outWorkspace = output_path  + '/' + str(city_code) + city + '/' + county_code + county
        outBHTB_shp = outWorkspace + '/' + county_code + '2022JBNTBHTB.shp'

        if not os.path.exists(outWorkspace):
            os.makedirs(outWorkspace)
        arcpy.env.workspace = inWorkspace
        # 检查自定义坐标系，并纠正
            # 获取原始数据shp文件空间参考
        spatialRef = arcpy.Describe(BHTB_shp).spatialReference
        spatialRefWkid = spatialRef.factoryCode
            # 判断wkid是否对应并纠正
        if(os.path.exists(outBHTB_shp)):
            print("already processed!")
        else:
            if not (spatialRefWkid == wkid):
                n = n + 1
                print(n)
                print(city)
                print(county)
                newSrRef = arcpy.SpatialReference(wkid)
                arcpy.Project_management(BHTB_shp,outBHTB_shp,newSrRef)
                print(arcpy.Describe(outBHTB_shp).spatialReference.factoryCode)
                print("--------------------------------------")
            else:
                arcpy.Copy_management(BHTB_shp,outBHTB_shp,"")

    # # 合并图层
    #     # 筛选补划图斑
    # bh_shp = input_path + '/' + u'四川占用补划20220530' + '/' + u'补划图斑.shp'
    # arcpy.MakeFeatureLayer_management(bh_shp,"bh_shp")
    # selectBh = arcpy.SelectLayerByLocation_management("bh_shp","INTERSECT",outBHTB_shp)
    #     # 合并
    # uniteDir = output_path + '/'+ str(city_code) + city + '/' + county_code + county + '/'
    # arcpy.Merge_management([selectBh,outBHTB_shp],)
    # outBh = output_path + '/' + 'bh' 
    # arcpy.CopyFeatures_management(selectBh, outBh + '/' + 'test.shp')

print("-------------------------Done!")

# 测试
# unite_cd = input_path + '/' + u'成都市边界' +'/'+ u'成都市_510100_子_边界.shp'
# unite_cq = input_path + '/' + u'重庆市边界'+ '/' + u'重庆市_500000_子_边界.shp'
# unite_result = output_path + '/' + 'result.shp'
# arcpy.Merge_management([unite_cd, unite_cq], unite_result)

# 擦除图层

# 结果按行政区划目录输出

    # 创建文件夹 
    # county_path = (output_path + '/' + str(city_code) + city + '/' + county_code + county)
    # if not os.path.exists(county_path):
    #     os.makedirs(county_path)