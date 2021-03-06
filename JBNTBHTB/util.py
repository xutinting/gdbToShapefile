# -*- coding: UTF-8 -*-
import os
import fnmatch
from wsgiref.util import shift_path_info
from config import PATHS

input_path = PATHS['input_path']

coordinate_list = [
    { 'city' : u"成都市", 'county' : u"锦江区", 'county_code' : "510104", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"青羊区", 'county_code' : "510105", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"金牛区", 'county_code' : "510106", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"武侯区", 'county_code' : "510107", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"成华区", 'county_code' : "510108", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"高新区", 'county_code' : "510109", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"天府新区成都直管区", 'county_code' : "510110", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"龙泉驿区", 'county_code' : "510112", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"青白江区", 'county_code' : "510113", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"新都区", 'county_code' : "510114", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"温江区", 'county_code' : "510115", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"双流区", 'county_code' : "510116", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"郫都区", 'county_code' : "510117", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"金堂县", 'county_code' : "510121", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"大邑县", 'county_code' : "510129", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"成都市", 'county' : u"蒲江县", 'county_code' : "510131", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"新津县", 'county_code' : "510118", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"都江堰市", 'county_code' : "510181", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"彭州市", 'county_code' : "510182", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"邛崃市", 'county_code' : "510183", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"成都市", 'county' : u"崇州市", 'county_code' : "510184", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"成都市", 'county' : u"简阳市", 'county_code' : "510185", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"自贡市", 'county' : u"自流井区", 'county_code' : "510302", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"自贡市", 'county' : u"贡井区", 'county_code' : "510303", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"自贡市", 'county' : u"大安区", 'county_code' : "510304", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"自贡市", 'county' : u"沿滩区", 'county_code' : "510311", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"自贡市", 'county' : u"荣县", 'county_code' : "510321", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"自贡市", 'county' : u"富顺县", 'county_code' : "510322", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"攀枝花市", 'county' : u"东区", 'county_code' : "510402", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"攀枝花市", 'county' : u"西区", 'county_code' : "510403", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"攀枝花市", 'county' : u"仁和区", 'county_code' : "510411", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"攀枝花市", 'county' : u"米易县", 'county_code' : "510421", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"攀枝花市", 'county' : u"盐边县", 'county_code' : "510422", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },

    { 'city' : u"泸州市", 'county' : u"江阳区", 'county_code' : "510502", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"泸州市", 'county' : u"纳溪区", 'county_code' : "510503", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"泸州市", 'county' : u"龙马潭区", 'county_code' : "510504", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"泸州市", 'county' : u"泸县", 'county_code' : "510521", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"泸州市", 'county' : u"合江县", 'county_code' : "510522", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"泸州市", 'county' : u"叙永县", 'county_code' : "510524", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"泸州市", 'county' : u"古蔺县", 'county_code' : "510525", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"德阳市", 'county' : u"旌阳区", 'county_code' : "510603", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"德阳市", 'county' : u"罗江区", 'county_code' : "510604", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"德阳市", 'county' : u"中江县", 'county_code' : "510623", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"德阳市", 'county' : u"广汉市", 'county_code' : "510681", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"德阳市", 'county' : u"什邡市", 'county_code' : "510682", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"德阳市", 'county' : u"绵竹市", 'county_code' : "510683", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"绵阳市", 'county' : u"涪城区", 'county_code' : "510703", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"绵阳市", 'county' : u"游仙区", 'county_code' : "510704", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"绵阳市", 'county' : u"安州区", 'county_code' : "510705", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"绵阳市", 'county' : u"三台县", 'county_code' : "510722", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"绵阳市", 'county' : u"盐亭县", 'county_code' : "510723", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"绵阳市", 'county' : u"梓潼县", 'county_code' : "510725", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"绵阳市", 'county' : u"北川羌族自治县", 'county_code' : "510726", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"绵阳市", 'county' : u"平武县", 'county_code' : "510727", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"绵阳市", 'county' : u"江油市", 'county_code' : "510781", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"广元市", 'county' : u"利州区", 'county_code' : "510802", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"广元市", 'county' : u"昭化区", 'county_code' : "510811", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"广元市", 'county' : u"朝天区", 'county_code' : "510812", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"广元市", 'county' : u"旺苍县", 'county_code' : "510821", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"广元市", 'county' : u"青川县", 'county_code' : "510822", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"广元市", 'county' : u"剑阁县", 'county_code' : "510823", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"广元市", 'county' : u"苍溪县", 'county_code' : "510824", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"遂宁市", 'county' : u"船山区", 'county_code' : "510903", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"遂宁市", 'county' : u"安居区", 'county_code' : "510904", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"遂宁市", 'county' : u"蓬溪县", 'county_code' : "510921", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"遂宁市", 'county' : u"射洪县", 'county_code' : "510922", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"遂宁市", 'county' : u"大英县", 'county_code' : "510923", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"遂宁市", 'county' : u"射洪市", 'county_code' : "510981", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"内江市", 'county' : u"市中区", 'county_code' : "511002", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"内江市", 'county' : u"东兴区", 'county_code' : "511011", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"内江市", 'county' : u"威远县", 'county_code' : "511024", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"内江市", 'county' : u"资中县", 'county_code' : "511025", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"内江市", 'county' : u"隆昌市", 'county_code' : "511083", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"乐山市", 'county' : u"市中区", 'county_code' : "511102", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"乐山市", 'county' : u"沙湾区", 'county_code' : "511111", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"乐山市", 'county' : u"五通桥区", 'county_code' : "511112", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"乐山市", 'county' : u"金口河区", 'county_code' : "511113", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"乐山市", 'county' : u"犍为县", 'county_code' : "511123", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"乐山市", 'county' : u"井研县", 'county_code' : "511124", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"乐山市", 'county' : u"夹江县", 'county_code' : "511126", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"乐山市", 'county' : u"沐川县", 'county_code' : "511129", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"乐山市", 'county' : u"峨边彝族自治县", 'county_code' : "511132", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"乐山市", 'county' : u"马边彝族自治县", 'county_code' : "511133", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"乐山市", 'county' : u"峨眉山市", 'county_code' : "511181", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },

    { 'city' : u"南充市", 'county' : u"顺庆区", 'county_code' : "511302", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"南充市", 'county' : u"高坪区", 'county_code' : "511303", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"南充市", 'county' : u"嘉陵区", 'county_code' : "511304", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"南充市", 'county' : u"南部县", 'county_code' : "511321", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"南充市", 'county' : u"营山县", 'county_code' : "511322", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"南充市", 'county' : u"蓬安县", 'county_code' : "511323", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"南充市", 'county' : u"仪陇县", 'county_code' : "511324", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"南充市", 'county' : u"西充县", 'county_code' : "511325", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"南充市", 'county' : u"阆中市", 'county_code' : "511381", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"眉山市", 'county' : u"东坡区", 'county_code' : "511402", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"眉山市", 'county' : u"仁寿县", 'county_code' : "511421", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"眉山市", 'county' : u"彭山区", 'county_code' : "511403", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"眉山市", 'county' : u"洪雅县", 'county_code' : "511423", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"眉山市", 'county' : u"丹棱县", 'county_code' : "511424", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"眉山市", 'county' : u"青神县", 'county_code' : "511425", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"宜宾市", 'county' : u"翠屏区", 'county_code' : "511502", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"叙州区", 'county_code' : "511504", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"南溪区", 'county_code' : "511503", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"江安县", 'county_code' : "511523", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"长宁县", 'county_code' : "511524", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"高县", 'county_code' : "511525", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"珙县", 'county_code' : "511526", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"筠连县", 'county_code' : "511527", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"兴文县", 'county_code' : "511528", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"宜宾市", 'county' : u"屏山县", 'county_code' : "511529", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"广安市", 'county' : u"广安区", 'county_code' : "511602", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"广安市", 'county' : u"前锋区", 'county_code' : "511603", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"广安市", 'county' : u"岳池县", 'county_code' : "511621", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"广安市", 'county' : u"武胜县", 'county_code' : "511622", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"广安市", 'county' : u"邻水县", 'county_code' : "511623", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"广安市", 'county' : u"华蓥市", 'county_code' : "511681", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },

    { 'city' : u"达州市", 'county' : u"通川区", 'county_code' : "511702", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"达州市", 'county' : u"达川区", 'county_code' : "511703", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"达州市", 'county' : u"宣汉县", 'county_code' : "511722", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"达州市", 'county' : u"开江县", 'county_code' : "511723", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"达州市", 'county' : u"大竹县", 'county_code' : "511724", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"达州市", 'county' : u"渠县", 'county_code' : "511725", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"达州市", 'county' : u"万源市", 'county_code' : "511781", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },

    { 'city' : u"雅安市", 'county' : u"雨城区", 'county_code' : "511802", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"雅安市", 'county' : u"名山区", 'county_code' : "511803", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"雅安市", 'county' : u"荥经县", 'county_code' : "511822", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"雅安市", 'county' : u"汉源县", 'county_code' : "511823", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"雅安市", 'county' : u"石棉县", 'county_code' : "511824", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"雅安市", 'county' : u"天全县", 'county_code' : "511825", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"雅安市", 'county' : u"芦山县", 'county_code' : "511826", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"雅安市", 'county' : u"宝兴县", 'county_code' : "511827", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },

    { 'city' : u"巴中市", 'county' : u"巴州区", 'county_code' : "511902", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"巴中市", 'county' : u"恩阳区", 'county_code' : "511903", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"巴中市", 'county' : u"通江县", 'county_code' : "511921", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"巴中市", 'county' : u"南江县", 'county_code' : "511922", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },
    { 'city' : u"巴中市", 'county' : u"平昌县", 'county_code' : "511923", 'name' : "CGCS2000_3_Degree_GK_Zone_36", 'wkid' : 4524 },

    { 'city' : u"资阳市", 'county' : u"雁江区", 'county_code' : "512002", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"资阳市", 'county' : u"安岳县", 'county_code' : "512021", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"资阳市", 'county' : u"乐至县", 'county_code' : "512022", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },

    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"马尔康市", 'county_code' : "513201", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"汶川县", 'county_code' : "513221", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"理县", 'county_code' : "513222", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"茂县", 'county_code' : "513223", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"松潘县", 'county_code' : "513224", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"九寨沟县", 'county_code' : "513225", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"金川县", 'county_code' : "513226", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"小金县", 'county_code' : "513227", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"黑水县", 'county_code' : "513228", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"壤塘县", 'county_code' : "513230", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"阿坝县", 'county_code' : "513231", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"若尔盖县", 'county_code' : "513232", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"阿坝藏族羌族自治州", 'county' : u"红原县", 'county_code' : "513233", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },

    { 'city' : u"甘孜藏族自治州", 'county' : u"康定市", 'county_code' : "513301", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"泸定县", 'county_code' : "513322", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"丹巴县", 'county_code' : "513323", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"九龙县", 'county_code' : "513324", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"雅江县", 'county_code' : "513325", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"道孚县", 'county_code' : "513326", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"炉霍县", 'county_code' : "513327", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"甘孜县", 'county_code' : "513328", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"新龙县", 'county_code' : "513329", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"德格县", 'county_code' : "513330", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"白玉县", 'county_code' : "513331", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"石渠县", 'county_code' : "513332", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"色达县", 'county_code' : "513333", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"理塘县", 'county_code' : "513334", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"巴塘县", 'county_code' : "513335", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"乡城县", 'county_code' : "513336", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"稻城县", 'county_code' : "513337", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },
    { 'city' : u"甘孜藏族自治州", 'county' : u"得荣县", 'county_code' : "513338", 'name' : "CGCS2000_3_Degree_GK_Zone_33", 'wkid' : 4521 },

    { 'city' : u"凉山彝族自治州", 'county' : u"西昌市", 'county_code' : "513401", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"木里藏族自治县", 'county_code' : "513422", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"盐源县", 'county_code' : "513423", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"德昌县", 'county_code' : "513424", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"会理县", 'county_code' : "513425", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"会东县", 'county_code' : "513426", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"宁南县", 'county_code' : "513427", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"普格县", 'county_code' : "513428", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"布拖县", 'county_code' : "513429", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"金阳县", 'county_code' : "513430", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"昭觉县", 'county_code' : "513431", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"喜德县", 'county_code' : "513432", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"冕宁县", 'county_code' : "513433", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"越西县", 'county_code' : "513434", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"甘洛县", 'county_code' : "513435", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"美姑县", 'county_code' : "513436", 'name' : "CGCS2000_3_Degree_GK_Zone_34", 'wkid' : 4522 },
    { 'city' : u"凉山彝族自治州", 'county' : u"雷波县", 'county_code' : "513437", 'name' : "CGCS2000_3_Degree_GK_Zone_35", 'wkid' : 4523 }    
]

cities = {
    u'成都市': '510100',
    u'自贡市': '510300',
    u'攀枝花市': '510400',
    u'泸州市': '510500',
    u'德阳市': '510600',
    u'绵阳市': '510700',
    u'广元市': '510800',
    u'遂宁市': '510900',
    u'内江市': '511000',
    u'乐山市': '511100',
    u'南充市': '511300',
    u'眉山市': '511400',
    u'宜宾市': '511500',
    u'广安市': '511600',
    u'达州市': '511700',
    u'雅安市': '511800',
    u'巴中市': '511900',
    u'资阳市': '512000',
    u'阿坝藏族羌族自治州': '513200',
    u'甘孜藏族自治州': '513300',
    u'凉山彝族自治州': '513400',
}

# 判断city code
def getCitycode(cityname):
    return cities.get(cityname) or 'invalid city name'

citiesname = [u'成都市', u'自贡市', u'攀枝花市', u'泸州市', u'德阳市',
            u'绵阳市', u'广元市', u'遂宁市', u'内江市', u'乐山市', u'南充市',
            u'眉山市', u'宜宾市', u'广安市', u'达州市', u'雅安市', u'巴中市',
            u'资阳市', u'阿坝藏族羌族自治州', u'甘孜藏族自治州', u'凉山彝族自治州']

# 得到每个city对应的countyname、countycode
def listdirInMac(path):
    return [dir for dir in os.listdir(path) if not dir.startswith('.')]

def getcountyInfo(cityname):
    return [county for county in coordinate_list if county['city'] == cityname]

def checkcountyDir(root_path):
    for city in cities.keys():
        # 对每个城市进行循环
        # cities 是一个字典，.keys()取得所有键名
        if not os.path.exists(root_path + '/' + cities[city] + city):
            continue
        dirs = listdirInMac(root_path + '/' + cities[city] + city)
        for county in getcountyInfo(city):
            # 对某个城市的每一个区进行循环
            county_code = county['county_code']
            county_name = county['county']
            matched = ''
            for dir in dirs:
                # find dir that matched with county
                if (dir.find(county_name[:-1]) > -1):
                    matched = dir

            # 如果condition为True，a = 1，否则 a = 2
            # a = 1 if condition else 2
            code_matched = "yes" if matched[:6] == county_code else "no"
            name_matched = "yes" if matched[6:] == county_name else "no"

            # county目录不存在
            if matched == '':
                print('{0} , {1}target dir does not exists.'.format(
                    city, county['county']))
                continue

            if (code_matched == "yes"):# code对应
                if (name_matched == "yes"): # name对应
                    pass
                else:# name部分对应
                    print('{0} {1} countycode matched, but countyname partmatched.'.format(city, county['county']))            
            else:# code不对应
                if (name_matched == "yes"):# name对应
                    print('{0} {1} countycode not matched, countyname matched.'.format(city, county['county']))
                else:# name部分对应
                    print('{0} {1} countycode not matched, countyname partmatched.'.format(city, county['county']))

    print("Dir checking---------------------Done!")

JBNTpath = input_path + '/' + 'JBNT'
# checkcountyDir(JBNTpath)

def modifyname (path):
    citydirs = os.listdir(path)
    for citydir in citydirs:
        countydirs = (os.listdir(path + '/' + citydir))
        for countydir in countydirs:
            # if (countydir == '510104锦江区'):
            countycode = countydir[:6]
            filepath = path + '/' + citydir + '/' + countydir + '/' + u'1.矢量数据'
            if not os.path.exists(filepath):
                continue
            else:
                files = os.listdir(filepath)
                for file in files:
                    if fnmatch.fnmatchcase(file,"*JBNTBHTB.shp"):
                        matchfile = countycode + '2014JBNTBHTB.shp'
                        if fnmatch.fnmatchcase(file,matchfile):
                            pass
                        else:
                            print(citydir,countydir,"有JBNTBHTB.shp文件,但是不是2014JBNTBHTB.shp")
                    elif fnmatch.fnmatchcase(file,"*.mdb"):
                        print(citydir,countydir,"没有JBNT shapefile文件, 有mdb文件")
