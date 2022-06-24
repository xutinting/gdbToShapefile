# -*- coding: UTF-8 -*-
import os
from config import PATHS

input_path = PATHS['input_path']

JBNTdata_path = input_path + '/'   + 'JBNT'

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

# 判断city code
def getCitycode(cityname):
    city = {
        u'成都市':'510100',
        u'自贡市':'510300',
        u'攀枝花市':'510400',
        u'泸州市':'510500',
        u'德阳市':'510600',
        u'绵阳市':'510700',
        u'广元市':'510800',
        u'遂宁市':'510900',
        u'内江市':'511000',       
        u'乐山市':'511100',
        u'南充市':'511300',
        u'眉山市':'511400',
        u'宜宾市':'511500',
        u'广安市':'511600',
        u'达州市':'511700',
        u'雅安市':'511800',
        u'巴中市':'511900',
        u'资阳市':'512000',
        u'阿坝藏族羌族自治州':'513200',
        u'甘孜藏族自治州':'513300',
        u'凉山彝族自治州':'513400',
    }

    if cityname == u'成都市':
        return city['成都市']
    elif cityname == u'自贡市':
        return city['自贡市']
    elif cityname == u'攀枝花市':
        return city['攀枝花市']
    elif cityname == u'泸州市':
        return city['泸州市']
    elif cityname == u'德阳市':
        return city['德阳市']
    elif cityname == u'绵阳市':
        return city['绵阳市']
    elif cityname == u'广元市':
        return city['广元市']
    elif cityname == u'遂宁市':
        return city['遂宁市']
    elif cityname == u'内江市':
        return city['内江市']       
    elif cityname == u'乐山市':
        return city['乐山市']
    elif cityname == u'南充市':
        return city['南充市']
    elif cityname == u'眉山市':
        return city['眉山市']
    elif cityname == u'宜宾市':
        return city['宜宾市']
    elif cityname == u'广安市':
        return city['广安市']
    elif cityname == u'达州市':
        return city['达州市']
    elif cityname == u'雅安市':
        return city['雅安市']
    elif cityname == u'巴中市':
        return city['巴中市']
    elif cityname == u'资阳市':
        return city['资阳市']
    elif cityname == u'阿坝藏族羌族自治州':
        return city['阿坝藏族羌族自治州']
    elif cityname == u'甘孜藏族自治州':
        return city['甘孜藏族自治州']
    elif cityname == u'凉山彝族自治州':
        return city['凉山彝族自治州']
    else:
        return "Invalid citydoe"


# 修改原数据文件夹
citiesname = ['成都市','自贡市','攀枝花市','泸州市','德阳市',\
            '绵阳市','广元市','遂宁市','内江市','乐山市','南充市',\
            '眉山市','宜宾市','广安市','达州市','雅安市','巴中市',\
            '资阳市','阿坝藏族羌族自治州','甘孜藏族自治州','凉山彝族自治州']

# 得到每个city对应的countyname
def getcountyInfo(cityname):
    if(cityname == u'成都市'):
        counties = [
            {'county':u'锦江区','countycode':'510104'},
            {'county':u'青羊区','countycode':'510105'},
            {'county':u'金牛区','countycode':'510106'},
            {'county':u'武侯区','countycode':'510107'},
            {'county':u'成华区','countycode':'510108'},
            {'county':u'高新区','countycode':'510109'},
            {'county':u'天府新区成都直管区','countycode':'510110'},
            {'county':u'龙泉驿区','countycode':'510112'},
            {'county':u'青白江区','countycode':'510113'},
            {'county':u'新都区','countycode':'510114'},
            {'county':u'温江区','countycode':'510115'},
            {'county':u'双流区','countycode':'510116'},
            {'county':u'郫都区','countycode':'510117'},
            {'county':u'金堂县','countycode':'510121'},
            {'county':u'大邑县','countycode':'510129'},
            {'county':u'蒲江县','countycode':'510131'},
            {'county':u'新津县','countycode':'510118'},
            {'county':u'都江堰市','countycode':'510181'},
            {'county':u'彭州市','countycode':'510182'},
            {'county':u'邛崃市','countycode':'510183'},
            {'county':u'崇州市','countycode':'510184'},
            {'county':u'简阳市','countycode':'510185'}
        ]
        return counties
    elif(cityname == u'自贡市'):
        counties = [
            {'county':u'自流井区','countycode':'510302'},
            {'county':u'贡井区','countycode':'510303'},
            {'county':u'大安区','countycode':'510304'},
            {'county':u'沿滩区','countycode':'510311'},
            {'county':u'荣县','countycode':'510321'},
            {'county':u'富顺县','countycode':'510322'}
        ]
        return counties
    elif(cityname == u'攀枝花市'):
        counties = [
            {'county':u'东区','countycode':'510402'},
            {'county':u'西区','countycode':'510403'},
            {'county':u'仁和区','countycode':'510411'},
            {'county':u'米易县','countycode':'510421'},
            {'county':u'盐边县','countycode':'510422'},
        ]
        return counties
    elif(cityname == u'泸州市'):
        counties = [
            {'county':u'江阳区','countycode':'510502'},
            {'county':u'纳溪区','countycode':'510503'},
            {'county':u'龙马潭区','countycode':'510504'},
            {'county':u'泸县','countycode':'510521'},
            {'county':u'合江县','countycode':'510522'},
            {'county':u'叙永县','countycode':'510524'},
            {'county':u'古蔺县','countycode':'510525'}
        ]
        return counties
    elif(cityname == u'德阳市'):
        counties = [
            {'county':u'旌阳区','countycode':'510603'},
            {'county':u'罗江区','countycode':'510604'},
            {'county':u'中江县','countycode':'510623'},
            {'county':u'广汉市','countycode':'510681'},
            {'county':u'什邡市','countycode':'510682'},
            {'county':u'绵竹市','countycode':'510683'}
        ]
        return counties
    elif(cityname == u'绵阳市'):
        counties = [
            {'county':u'涪城区','countycode':'510703'},
            {'county':u'游仙区','countycode':'510704'},
            {'county':u'安州区','countycode':'510705'},
            {'county':u'三台县','countycode':'510722'},
            {'county':u'盐亭县','countycode':'510723'},
            {'county':u'梓潼县','countycode':'510725'},
            {'county':u'北川羌族自治县','countycode':'510726'},
            {'county':u'平武县','countycode':'510727'},
            {'county':u'江油市','countycode':'510781'}
        ]
        return counties
    elif(cityname == u'广元市'):
        counties = [
            {'county':u'利州区','countycode':'510802'},
            {'county':u'昭化区','countycode':'510811'},
            {'county':u'朝天区','countycode':'510812'},
            {'county':u'旺苍县','countycode':'510821'},
            {'county':u'青川县','countycode':'510822'},
            {'county':u'剑阁县','countycode':'510823'},
            {'county':u'苍溪县','countycode':'510824'}
        ]
        return counties
    elif(cityname == u'遂宁市'):
        counties = [
            {'county':u'船山区','countycode':'510903'},
            {'county':u'安居区','countycode':'510904'},
            {'county':u'蓬溪县','countycode':'510921'},
            {'county':u'射洪县','countycode':'510922'},
            {'county':u'大英县','countycode':'510923'},
            {'county':u'射洪市','countycode':'510981'}
        ]
        return counties
    elif(cityname == u'内江市'):
        counties = [
            {'county':u'市中区','countycode':'511002'},
            {'county':u'东兴区','countycode':'511011'},
            {'county':u'威远县','countycode':'511024'},
            {'county':u'资中县','countycode':'511025'},
            {'county':u'隆昌市','countycode':'511083'}
        ]
        return counties
    elif(cityname == u'乐山市'):
        counties = [
            {'county':u'市中区','countycode':'511102'},
            {'county':u'沙湾区','countycode':'511111'},
            {'county':u'五通桥区','countycode':'511112'},
            {'county':u'金口河区','countycode':'511113'},
            {'county':u'犍为县','countycode':'511123'},
            {'county':u'井研县','countycode':'511124'},
            {'county':u'夹江县','countycode':'511126'},
            {'county':u'沐川县','countycode':'511129'},
            {'county':u'峨边彝族自治县','countycode':'511132'},
            {'county':u'马边彝族自治县','countycode':'511133'},
            {'county':u'峨眉山市','countycode':'511181'}
        ]
        return counties
    elif(cityname == u'南充市'):
        counties = [
            {'county':u'顺庆区','countycode':'511302'},
            {'county':u'高坪区','countycode':'511303'},
            {'county':u'嘉陵区','countycode':'511304'},
            {'county':u'南部县','countycode':'511321'},
            {'county':u'营山县','countycode':'511322'},
            {'county':u'蓬安县','countycode':'511323'},
            {'county':u'仪陇县','countycode':'511324'},
            {'county':u'西充县','countycode':'511325'},
            {'county':u'阆中市','countycode':'511381'}
        ]
        return counties
    elif(cityname == u'眉山市'):
        counties = [
            {'county':u'东坡区','countycode':'511402'},
            {'county':u'仁寿县','countycode':'511421'},
            {'county':u'彭山区','countycode':'511403'},
            {'county':u'洪雅县','countycode':'511423'},
            {'county':u'丹棱县','countycode':'511424'},
            {'county':u'青神县','countycode':'511425'}
        ]
        return counties
    elif(cityname == u'宜宾市'):
        counties = [
            {'county':u'翠屏区','countycode':'511502'},
            {'county':u'叙州区','countycode':'511504'},
            {'county':u'南溪区','countycode':'511503'},
            {'county':u'江安县','countycode':'511523'},
            {'county':u'长宁县','countycode':'511524'},
            {'county':u'高县','countycode':'511525'},
            {'county':u'珙县','countycode':'511526'},
            {'county':u'筠连县','countycode':'511527'},
            {'county':u'兴文县','countycode':'511528'},
            {'county':u'屏山县','countycode':'511529'}
        ]
        return counties
    elif(cityname == u'广安市'):
        counties = [
            {'county':u'广安区','countycode':'511602'},
            {'county':u'前锋区','countycode':'511603'},
            {'county':u'岳池县','countycode':'511621'},
            {'county':u'武胜县','countycode':'511622'},
            {'county':u'邻水县','countycode':'511623'},
            {'county':u'华蓥市','countycode':'511681'},
        ]
        return counties
    elif(cityname == u'达州市'):
        counties = [
            {'county':u'通川区','countycode':'511702'},
            {'county':u'达川区','countycode':'511703'},
            {'county':u'宣汉县','countycode':'511722'},
            {'county':u'开江县','countycode':'511723'},
            {'county':u'大竹县','countycode':'511724'},
            {'county':u'渠县','countycode':'511725'},
            {'county':u'万源市','countycode':'511781'},
        ]
        return counties
    elif(cityname == u'雅安市'):
        counties = [
            {'county':u'雨城区','countycode':'511802'},
            {'county':u'名山区','countycode':'511803'},
            {'county':u'荥经县','countycode':'511822'},
            {'county':u'汉源县','countycode':'511823'},
            {'county':u'石棉县','countycode':'511824'},
            {'county':u'天全县','countycode':'511825'},
            {'county':u'芦山县','countycode':'511826'},
            {'county':u'宝兴县','countycode':'511827'},
        ]
        return counties
    elif(cityname == u'巴中市'):
        counties = [
            {'county':u'巴州区','countycode':'511902'},
            {'county':u'恩阳区','countycode':'511903'},
            {'county':u'通江县','countycode':'511921'},
            {'county':u'南江县','countycode':'511922'},
            {'county':u'平昌县','countycode':'511923'},
        ]
        return counties
    elif(cityname == u'资阳市'):
        counties = [
            {'county':u'雁江区','countycode':'512002'},
            {'county':u'安岳县','countycode':'512021'},
            {'county':u'乐至县','countycode':'512022'},
        ]
        return counties
    elif(cityname == u'阿坝藏族羌族自治州'):
        counties = [
            {'county':u'马尔康市','countycode':'513201'},
            {'county':u'汶川县','countycode':'513221'},
            {'county':u'理县','countycode':'513222'},
            {'county':u'茂县','countycode':'513223'},
            {'county':u'松潘县','countycode':'513224'},
            {'county':u'九寨沟县','countycode':'513225'},
            {'county':u'金川县','countycode':'513226'},
            {'county':u'小金县','countycode':'513227'},
            {'county':u'黑水县','countycode':'513228'},
            {'county':u'壤塘县','countycode':'513230'},
            {'county':u'阿坝县','countycode':'513231'},
            {'county':u'若尔盖县','countycode':'513232'},
            {'county':u'红原县','countycode':'513233'},
        ]
        return counties
    elif(cityname == u'甘孜藏族自治州'):
        counties = [
            {'county':u'康定市','countycode':'513301'},
            {'county':u'泸定县','countycode':'513322'},
            {'county':u'丹巴县','countycode':'513323'},
            {'county':u'九龙县','countycode':'513324'},
            {'county':u'雅江县','countycode':'513325'},
            {'county':u'道孚县','countycode':'513326'},
            {'county':u'炉霍县','countycode':'513327'},
            {'county':u'甘孜县','countycode':'513328'},
            {'county':u'新龙县','countycode':'513329'},
            {'county':u'德格县','countycode':'513330'},
            {'county':u'白玉县','countycode':'513331'},
            {'county':u'石渠县','countycode':'513332'},
            {'county':u'色达县','countycode':'513333'},
            {'county':u'理塘县','countycode':'513334'},
            {'county':u'巴塘县','countycode':'513335'},
            {'county':u'乡城县','countycode':'513336'},
            {'county':u'稻城县','countycode':'513337'},
            {'county':u'得荣县','countycode':'513338'},
        ]
        return counties
    elif(cityname == u'凉山彝族自治州'):
        counties = [
            {'county':u'西昌市','countycode':'513401'},
            {'county':u'木里藏族自治县','countycode':'513422'},
            {'county':u'盐源县','countycode':'513423'},
            {'county':u'德昌县','countycode':'513424'},
            {'county':u'会理县','countycode':'513425'},
            {'county':u'会东县','countycode':'513426'},
            {'county':u'宁南县','countycode':'513427'},
            {'county':u'普格县','countycode':'513428'},
            {'county':u'布拖县','countycode':'513429'},
            {'county':u'金阳县','countycode':'513430'},
            {'county':u'昭觉县','countycode':'513431'},
            {'county':u'喜德县','countycode':'513432'},
            {'county':u'冕宁县','countycode':'513433'},
            {'county':u'越西县','countycode':'513434'},
            {'county':u'甘洛县','countycode':'513435'},
            {'county':u'美姑县','countycode':'513436'},
            {'county':u'雷波县','countycode':'513437'},
        ]
        return counties
    else:
        return 'cityname not defined'

def correctDir (root_path):
    dir_cities = os.listdir(root_path)
    
    for dir_city in dir_cities:
        dir_cityname = dir_city[6 : ]
        dir_counties = os.listdir(root_path + '/' + dir_city) # county目录集合
        counties_list = getcountyInfo(dir_cityname)
        dir_countycode = ''
        dir_countyname = ''
        for dir_county in dir_counties:
            dir_countycode = dir_county[ : 6]
            dir_countyname = dir_county[6 : ]
            match = dir_county[6 : len(dir_county) -1 ]
            counties = []
            countycode = ''
            for c in counties_list:
                counties.append(c['county'])
                if(c['county'] == dir_countyname):
                    countycode = c['countycode']
            for county in counties:
                exist = county.find(match) + 1
                # countyname 和 countycode全对应
                if ( dir_countyname == county and dir_countycode == countycode):
                    # print(dir_cityname,dir_countyname,"存在")
                    pass
                # countyname对应，但是countycode不对应
                elif(dir_countyname == county and not dir_countycode == countycode):
                    print(dir_cityname,dir_countyname,"存在,但是countycode不对应")
                elif(exist and dir_countycode == countycode):
                    print(dir_cityname,dir_countyname,"存在,countycode对应,但是名字部分对应")
                elif(exist and not dir_countycode == countycode):
                    print(dir_cityname,dir_countyname,"存在,但是countycode不对应,名字部分对应")
    print("---------------------Done!")
                
correctDir(JBNTdata_path)
