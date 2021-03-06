# -*- coding: UTF-8 -*-
import os
import arcpy
from util import coordinate_list,getCitycode
from config import PATHS

input_path = PATHS['input_path']
output_path = PATHS['output_path']
result_path = PATHS['result_path']

# 补划图斑
BH_shp = input_path + '/' + u'四川占用补划20220530' + '/' + u'补划图斑.shp'
arcpy.MakeFeatureLayer_management(BH_shp,'BH_shp')

for coordinate in coordinate_list:
    city = coordinate['city']
    city_code = getCitycode(city)
    county_code = coordinate['county_code']
    county = coordinate['county']
    coordinate_name = coordinate['name']
    wkid = coordinate['wkid']

    inWorkspace = input_path + '/' + 'JBNT' + '/' + str(city_code) + city + '/' + county_code + county +'/'+  u'1.矢量数据'
    JBNT_shp = inWorkspace + '/' + county_code + '2014JBNTBHTB.shp'

    resultJBNT = result_path + '/' + str(city_code) + city + '/' + county_code + county
    outWorkspace = output_path  + '/' + str(city_code) + city + '/' + county_code + county
    # 转换坐标系的基本农田图层
    transWkidJBNT = outWorkspace + '/' + county_code + 'JBNT.shp'

    # print(city)
    # print(county)
    # print("loading--------------------")
    if (os.path.exists(resultJBNT)):
        pass
    elif (os.path.exists(inWorkspace)):
        if not (os.path.exists(JBNT_shp)):
            print(city)
            print(county)
            print("2014JBNTBHTB.shp don't exist")
            print("-------------")
        else:
            if not os.path.exists(outWorkspace):
                os.makedirs(outWorkspace)
            arcpy.env.workspace = inWorkspace
            # 检查自定义坐标系，并纠正
                # 获取原始数据shp文件空间参考
            spatialRef = arcpy.Describe(JBNT_shp).spatialReference
            spatialRefWkid = spatialRef.factoryCode
                # 判断wkid是否对应并纠正
            if(os.path.exists(transWkidJBNT)):
                print("already processed!")
            else:
                if not (spatialRefWkid == wkid):
                    n = n + 1
                    print(n)
                    print(city)
                    print(county)
                    print('this county need to correct wkid')
                    newSrRef = arcpy.SpatialReference(wkid)
                    arcpy.Project_management(JBNT_shp,transWkidJBNT,newSrRef)
                    print(arcpy.Describe(transWkidJBNT).spatialReference.factoryCode)
                    print("wkid have corrected--------------------------------")
                else:
                    arcpy.Copy_management(JBNT_shp,transWkidJBNT,"")
            # 合并图层
                # 筛选补划图斑
            BHQ_shp = inWorkspace + '/' + county_code + '2014JBNTBHQ.shp'
            intersectBH = arcpy.SelectLayerByLocation_management('BH_shp',"INTERSECT",BHQ_shp)
            # 输出每个区的补划图斑
            countyBH = outWorkspace + '/' + county_code + 'BHTB.shp'
                # 擦除图层
            erase_shp = input_path + '/' + u'四川占用补划20220530' + '/' + u'占地项目.shp'
                # 结果图层
            if not os.path.exists(resultJBNT):
                os.makedirs(resultJBNT)
            outBHTB = resultJBNT +'/' + county_code + '2022JBNTBHTB.shp'
            if (intersectBH):
                arcpy.CopyFeatures_management(intersectBH,countyBH)
                # 合并BHTB和JBNT
                # 定义合并字段      
                fieldMappings = arcpy.FieldMappings()
                fieldMappings.addTable(transWkidJBNT)
                merge_shp = outWorkspace + '/' + county_code + 'JBNTBHTB.shp'
                arcpy.Merge_management([transWkidJBNT,intersectBH],merge_shp,fieldMappings)
                # 删除补划图斑多余的字段
                arcpy.DeleteField_management(merge_shp,['OBJECTID','XMMC','SDM','JJBH','ID_PROVINC','ORECID'])
                # 擦除
                arcpy.Erase_analysis(merge_shp,erase_shp,outBHTB)  
            else:
                print(city)
                print(county)
                print("this county don't have BHTB, only erase it")

    else:
        n = n + 1
        print(n)
        print(city)
        print(county)
        print("don't exist county dir")
        print("--------------------------")

print("-------------------------Done!")
