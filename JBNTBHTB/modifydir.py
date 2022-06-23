import os
from util import coordinate_list, getCitycode
from config import PATHS


input_path = PATHS['input_path']

JBNTdata_path = input_path + '/'   + 'JBNT'
citiesdir = os.listdir(JBNTdata_path)

for citydir in citiesdir:
    city_path = JBNTdata_path + '/' + citydir
    cityname = citydir[6:]
    countysdir = os.listdir(city_path)
    for countydir in countysdir:

n = 0
for city_path in citiesdir:
    citypath = os.path.join(JBNTdata_path,city_path)
    if os.path.isdir(citypath):        
        countys_path = os.listdir(citypath)
        for county_path in countys_path:
            countypath=os.path.join(citypath,county_path)
            if os.path.isdir(countypath):
                # 此处获得县级目录，分割county_path，得到countyCode and countyName    
                countyname= county_path[5:]
                # 通过countyName在coordinate_list模糊查询，然后取得正确的cityName,countyCode,countyName,wkid
                # 下面就接到你的逻辑，这里我们直接遍历数据目录，反过来到coordinate_list去查找正确元素，而不是直接遍历coordinate_list，去找数据
