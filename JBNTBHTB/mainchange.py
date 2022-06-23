# -*- coding: UTF-8 -*-
import os
import arcpy
from util import coordinate_list, getCitycode
from config import PATHS


input_path = PATHS['input_path']
output_path = PATHS['output_path']
result_path = PATHS['result_path']

# 补划图斑
BH_shp = input_path + '/' + u'四川占用补划20220530' + '/' + u'补划图斑.shp'
arcpy.MakeFeatureLayer_management(BH_shp,'BH_shp')

JBNTdata_path = input_path + '/'   + 'JBNT'
cities_path = os.listdir(JBNTdata_path)
for city_path in cities_path:
    citypath=os.path.join(JBNTdata_path,city_path)
    if os.path.isdir(citypath):        
        countys_path = os.listdir(citypath)
        for county_path in countys_path:
            countypath=os.path.join(citypath,county_path)
            if os.path.isdir(countypath):
                # 此处获得县级目录，分割county_path，得到countyCode and countyName    
                countyname = county_path[6:len(county_path)-2] 
                for coordinate in coordinate_list:
                    county = coordinate['county']                                      
                    if county.find(countyname):  
                        print(county+" find!")                      
                        city = coordinate['city']
                        city_code = getCitycode(city)
                        county_code = coordinate['county_code']
                        wkid = coordinate['wkid']
                        inWorkspace = input_path + '/' + 'JBNT' + '/' + str(city_code) + city + '/' + county_code + county +'/'+  u'1.矢量数据'
                        resultJBNT = result_path + '/' + city + '/' + county_code + county
                        if (os.path.exists(resultJBNT)):
                            print(city + county + "already processed!")
                            print("----------------------------------")
                        elif (os.path.exists(inWorkspace)):
                            JBNT_shp = inWorkspace + '/' + county_code + '2014JBNTBHTB.shp'
                            if (os.path.exists(JBNT_shp)):
                                outWorkspace = output_path  + '/' + str(city_code) + city + '/' + county_code + county
                                if not os.path.exists(outWorkspace):
                                    os.makedirs(outWorkspace)
                                # 转换坐标系的基本农田图层
                                transWkidJBNT_shp = outWorkspace + '/' + county_code + 'JBNT.shp'
                                arcpy.env.workspace = inWorkspace
                                # 是否处理 
                                if(os.path.exists(transWkidJBNT_shp)):
                                    pass
                                else:
                                    # 检查自定义坐标系，并纠正
                                    # 获取原始数据shp文件空间参考
                                    spatialRef = arcpy.Describe(JBNT_shp).spatialReference
                                    spatialRefWkid = spatialRef.factoryCode
                                    # 判断wkid是否对应并纠正
                                    if not (spatialRefWkid == wkid):
                                        n = n + 1
                                        print(n)
                                        print(city + county + 'need to correct wkid.')
                                        print("loading--------------------------------------")
                                        newSrRef = arcpy.SpatialReference(wkid)
                                        arcpy.Project_management(JBNT_shp,transWkidJBNT_shp,newSrRef)
                                        print(arcpy.Describe(transWkidJBNT_shp).spatialReference.factoryCode)
                                        print(city + county + 'wkid have corrected.')
                                    else:
                                        arcpy.Copy_management(JBNT_shp,transWkidJBNT_shp,"")
                                # 合并图层
                                    # 筛选补划图斑
                                BH_shp = input_path + '/' + u'四川占用补划20220530' + '/' + u'补划图斑.shp'
                                BHQ_shp = inWorkspace + '/' + county_code + '2014JBNTBHQ.shp'
                                intersectBH = arcpy.SelectLayerByLocation_management('BH_shp',"INTERSECT",BHQ_shp)
                                # 输出每个区的补划图斑
                                countyBH = outWorkspace + '/' + county_code + 'BHTB.shp'
                                    # 擦除图层
                                erase_shp = input_path + '/' + u'四川占用补划20220530' + '/' + u'占地项目.shp'
                                    # 结果图层
                                if not os.path.exists(resultJBNT):
                                    os.makedirs(resultJBNT)
                                outBHTB = resultJBNT + '/' + county_code + '2022JBNTBHTB.shp'
                                if (intersectBH):
                                    arcpy.CopyFeatures_management(intersectBH,countyBH)
                                    # 定义合并字段      
                                    fieldMappings = arcpy.FieldMappings()
                                    fieldMappings.addTable(transWkidJBNT_shp)
                                    merge_shp = outWorkspace + '/' + county_code + 'JBNTBHTB.shp'
                                    arcpy.Merge_management([transWkidJBNT_shp,intersectBH],merge_shp,fieldMappings)
                                    # 删除补划图斑多余的字段
                                    arcpy.DeleteField_management(merge_shp,['OBJECTID','XMMC','SDM','JJBH','ID_PROVINC','ORECID'])
                                    # 擦除
                                    arcpy.Erase_analysis(merge_shp,erase_shp,outBHTB)  
                                else:
                                    print(city)
                                    print(county)
                                    print("this county don't have BHTB")
                                    print("---------------------------")
                                    arcpy.Erase_analysis(transWkidJBNT_shp,erase_shp,outBHTB)
                            else:
                                print(city + county + "county dir exist, but '2014JBNTBHTB.shp' don't exist, it may have mdb data or other name.")
                                print("---------------------------")
                        else:
                            print(city + county + "county dir don't exist, and dont' konw whether '2014JBNTBHTB.shp' exist.")
                    else:
                        print(countyname + " not find!")


print("-------------------------Done!")                                                                      
