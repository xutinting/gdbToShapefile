# -*- coding: UTF-8 -*-
import arcpy
import os
from config import PATHS

input_path = PATHS['input_path']

def getGDBs():
    filesNames = os.listdir(input_path)

    GDBs = []
    for fileName in filesNames:
        extension = os.path.splitext(fileName)[1]

        if extension == '.gdb':
            file = os.path.join(input_path, fileName)
            GDBs.append(file)

    return GDBs

def listFeatureDatasets(gdb):
    arcpy.env.workspace = gdb

    gdbName = os.path.splitext(os.path.basename(gdb))[0]
    
    featureDatasetsNames = arcpy.ListDatasets('*', 'Feature')
    featuresDatasetsNames = []
    for featureDatasetName in featureDatasetsNames:
        dataset = os.path.join(gdb, featureDatasetName)

        datasetType = arcpy.Describe(dataset).datasetType

        if datasetType == 'FeatureDataset':
            featuresDatasetsNames.append(featureDatasetName)

    message = 'The datasets from file geodatabase {} were successfully listed\n'.format(gdbName)

    return [message, featuresDatasetsNames,gdbName]


admin_codes = [
{ 'City' : '成都市', 'County' : '锦江区', 'CountyCode' : '510104' },
{ 'City' : '成都市', 'County' : '青羊区', 'CountyCode' : '510105'},
{ 'City' : '成都市', 'County' : '金牛区', 'CountyCode' : '510106' },
{ 'City' : '成都市', 'County' : '武侯区', 'CountyCode' : '510107' },
{ 'City' : '成都市', 'County' : '成华区', 'CountyCode' : '510108' },
{ 'City' : '成都市', 'County' : '高新区', 'CountyCode' : '510109' },
{ 'City' : '成都市', 'County' : '天府新区成都直管区', 'CountyCode' : '510110'  },
{ 'City' : '成都市', 'County' : '龙泉驿区', 'CountyCode' : '510112'  },
{ 'City' : '成都市', 'County' : '青白江区', 'CountyCode' : '510113'  },
{ 'City' : '成都市', 'County' : '新都区', 'CountyCode' : '510114'  },
{ 'City' : '成都市', 'County' : '温江区', 'CountyCode' : '510115' },
{ 'City' : '成都市', 'County' : '双流区', 'CountyCode' : '510116' },
{ 'City' : '成都市', 'County' : '郫都区', 'CountyCode' : '510117'  },
{ 'City' : '成都市', 'County' : '金堂县', 'CountyCode' : '510121'  },
{ 'City' : '成都市', 'County' : '大邑县', 'CountyCode' : '510129' },
{ 'City' : '成都市', 'County' : '蒲江县', 'CountyCode' : '510131'  },
{ 'City' : '成都市', 'County' : '新津县', 'CountyCode' : '510118'  },
{ 'City' : '成都市', 'County' : '都江堰市', 'CountyCode' : '510181'  },
{ 'City' : '成都市', 'County' : '彭州市', 'CountyCode' : '510182'  },
{ 'City' : '成都市', 'County' : '邛崃市', 'CountyCode' : '510183' },
{ 'City' : '成都市', 'County' : '崇州市', 'CountyCode' : '510184'  },
{ 'City' : '成都市', 'County' : '简阳市', 'CountyCode' : '510185'  },

{ 'City' : '自贡市', 'County' : '自流井区', 'CountyCode' : '510302' },
{ 'City' : '自贡市', 'County' : '贡井区', 'CountyCode' : '510303'  },
{ 'City' : '自贡市', 'County' : '大安区', 'CountyCode' : '510304' },
{ 'City' : '自贡市', 'County' : '沿滩区', 'CountyCode' : '510311' },
{ 'City' : '自贡市', 'County' : '荣县', 'CountyCode' : '510321' },
{ 'City' : '自贡市', 'County' : '富顺县', 'CountyCode' : '510322' },

{ 'City' : '攀枝花市', 'County' : '东区', 'CountyCode' : '510402'},
{ 'City' : '攀枝花市', 'County' : '西区', 'CountyCode' : '510403'},
{ 'City' : '攀枝花市', 'County' : '仁和区', 'CountyCode' : '510411' },
{ 'City' : '攀枝花市', 'County' : '米易县', 'CountyCode' : '510421'},
{ 'City' : '攀枝花市', 'County' : '盐边县', 'CountyCode' : '510422' },

{ 'City' : '泸州市', 'County' : '江阳区', 'CountyCode' : '510502' },
{ 'City' : '泸州市', 'County' : '纳溪区', 'CountyCode' : '510503' },
{ 'City' : '泸州市', 'County' : '龙马潭区', 'CountyCode' : '510504'},
{ 'City' : '泸州市', 'County' : '泸县', 'CountyCode' : '510521' },
{ 'City' : '泸州市', 'County' : '合江县', 'CountyCode' : '510522'},
{ 'City' : '泸州市', 'County' : '叙永县', 'CountyCode' : '510524'},
{ 'City' : '泸州市', 'County' : '古蔺县', 'CountyCode' : '510525'},

{ 'City' : '德阳市', 'County' : '旌阳区', 'CountyCode' : '510603'},
{ 'City' : '德阳市', 'County' : '罗江区', 'CountyCode' : '510604'},
{ 'City' : '德阳市', 'County' : '中江县', 'CountyCode' : '510623'},
{ 'City' : '德阳市', 'County' : '广汉市', 'CountyCode' : '510681'},
{ 'City' : '德阳市', 'County' : '什邡市', 'CountyCode' : '510682'},
{ 'City' : '德阳市', 'County' : '绵竹市', 'CountyCode' : '510683' },

{ 'City' : '绵阳市', 'County' : '涪城区', 'CountyCode' : '510703'},
{ 'City' : '绵阳市', 'County' : '游仙区', 'CountyCode' : '510704'},
{ 'City' : '绵阳市', 'County' : '安州区', 'CountyCode' : '510705' },
{ 'City' : '绵阳市', 'County' : '三台县', 'CountyCode' : '510722'},
{ 'City' : '绵阳市', 'County' : '盐亭县', 'CountyCode' : '510723'},
{ 'City' : '绵阳市', 'County' : '梓潼县', 'CountyCode' : '510725'},
{ 'City' : '绵阳市', 'County' : '北川羌族自治县', 'CountyCode' : '510726' },
{ 'City' : '绵阳市', 'County' : '平武县', 'CountyCode' : '510727' },
{ 'City' : '绵阳市', 'County' : '江油市', 'CountyCode' : '510781'},

{ 'City' : '广元市', 'County' : '利州区', 'CountyCode' : '510802' },
{ 'City' : '广元市', 'County' : '昭化区', 'CountyCode' : '510811' },
{ 'City' : '广元市', 'County' : '朝天区', 'CountyCode' : '510812'},
{ 'City' : '广元市', 'County' : '旺苍县', 'CountyCode' : '510821'},
{ 'City' : '广元市', 'County' : '青川县', 'CountyCode' : '510822'},
{ 'City' : '广元市', 'County' : '剑阁县', 'CountyCode' : '510823'},
{ 'City' : '广元市', 'County' : '苍溪县', 'CountyCode' : '510824'},

{ 'City' : '遂宁市', 'County' : '船山区', 'CountyCode' : '510903' },
{ 'City' : '遂宁市', 'County' : '安居区', 'CountyCode' : '510904'},
{ 'City' : '遂宁市', 'County' : '蓬溪县', 'CountyCode' : '510921'},
{ 'City' : '遂宁市', 'County' : '射洪县', 'CountyCode' : '510922'},
{ 'City' : '遂宁市', 'County' : '大英县', 'CountyCode' : '510923'},

{ 'City' : '内江市', 'County' : '市中区', 'CountyCode' : '511002'},
{ 'City' : '内江市', 'County' : '东兴区', 'CountyCode' : '511011'},
{ 'City' : '内江市', 'County' : '威远县', 'CountyCode' : '511024' },
{ 'City' : '内江市', 'County' : '资中县', 'CountyCode' : '511025' },
{ 'City' : '内江市', 'County' : '隆昌市', 'CountyCode' : '511083' },

{ 'City' : '乐山市', 'County' : '市中区', 'CountyCode' : '511102'},
{ 'City' : '乐山市', 'County' : '沙湾区', 'CountyCode' : '511111'},
{ 'City' : '乐山市', 'County' : '五通桥区', 'CountyCode' : '511112'},
{ 'City' : '乐山市', 'County' : '金口河区', 'CountyCode' : '511113'},
{ 'City' : '乐山市', 'County' : '犍为县', 'CountyCode' : '511123' },
{ 'City' : '乐山市', 'County' : '井研县', 'CountyCode' : '511124'  },
{ 'City' : '乐山市', 'County' : '夹江县', 'CountyCode' : '511126'  },
{ 'City' : '乐山市', 'County' : '沐川县', 'CountyCode' : '511129' },
{ 'City' : '乐山市', 'County' : '峨边彝族自治县', 'CountyCode' : '511132' },
{ 'City' : '乐山市', 'County' : '马边彝族自治县', 'CountyCode' : '511133'  },
{ 'City' : '乐山市', 'County' : '峨眉山市', 'CountyCode' : '511181'},

{ 'City' : '南充市', 'County' : '顺庆区', 'CountyCode' : '511302'  },
{ 'City' : '南充市', 'County' : '高坪区', 'CountyCode' : '511303'  },
{ 'City' : '南充市', 'County' : '嘉陵区', 'CountyCode' : '511304'  },
{ 'City' : '南充市', 'County' : '南部县', 'CountyCode' : '511321' },
{ 'City' : '南充市', 'County' : '营山县', 'CountyCode' : '511322' },
{ 'City' : '南充市', 'County' : '蓬安县', 'CountyCode' : '511323'  },
{ 'City' : '南充市', 'County' : '仪陇县', 'CountyCode' : '511324'  },
{ 'City' : '南充市', 'County' : '西充县', 'CountyCode' : '511325'  },
{ 'City' : '南充市', 'County' : '阆中市', 'CountyCode' : '511381'  },

{ 'City' : '眉山市', 'County' : '东坡区', 'CountyCode' : '511402'  },
{ 'City' : '眉山市', 'County' : '仁寿县', 'CountyCode' : '511421'  },
{ 'City' : '眉山市', 'County' : '彭山区', 'CountyCode' : '511403'  },
{ 'City' : '眉山市', 'County' : '洪雅县', 'CountyCode' : '511423' },
{ 'City' : '眉山市', 'County' : '丹棱县', 'CountyCode' : '511424' },
{ 'City' : '眉山市', 'County' : '青神县', 'CountyCode' : '511425'  },

{ 'City' : '宜宾市', 'County' : '翠屏区', 'CountyCode' : '511502'  },
{ 'City' : '宜宾市', 'County' : '叙州区', 'CountyCode' : '511504'  },
{ 'City' : '宜宾市', 'County' : '南溪区', 'CountyCode' : '511503'  },
{ 'City' : '宜宾市', 'County' : '江安县', 'CountyCode' : '511523' },
{ 'City' : '宜宾市', 'County' : '长宁县', 'CountyCode' : '511524' },
{ 'City' : '宜宾市', 'County' : '高县', 'CountyCode' : '511525' },
{ 'City' : '宜宾市', 'County' : '珙县', 'CountyCode' : '511526' },
{ 'City' : '宜宾市', 'County' : '筠连县', 'CountyCode' : '511527' },
{ 'City' : '宜宾市', 'County' : '兴文县', 'CountyCode' : '511528' },
{ 'City' : '宜宾市', 'County' : '屏山县', 'CountyCode' : '511529'  },

{ 'City' : '广安市', 'County' : '广安区', 'CountyCode' : '511602' },
{ 'City' : '广安市', 'County' : '前锋区', 'CountyCode' : '511603'  },
{ 'City' : '广安市', 'County' : '岳池县', 'CountyCode' : '511621'  },
{ 'City' : '广安市', 'County' : '武胜县', 'CountyCode' : '511622'  },
{ 'City' : '广安市', 'County' : '邻水县', 'CountyCode' : '511623'  },
{ 'City' : '广安市', 'County' : '华蓥市', 'CountyCode' : '511681'  },

{ 'City' : '达州市', 'County' : '通川区', 'CountyCode' : '511702' },
{ 'City' : '达州市', 'County' : '达川区', 'CountyCode' : '511703' },
{ 'City' : '达州市', 'County' : '宣汉县', 'CountyCode' : '511722' },
{ 'City' : '达州市', 'County' : '开江县', 'CountyCode' : '511723'  },
{ 'City' : '达州市', 'County' : '大竹县', 'CountyCode' : '511724' },
{ 'City' : '达州市', 'County' : '渠县', 'CountyCode' : '511725' },
{ 'City' : '达州市', 'County' : '万源市', 'CountyCode' : '511781' },

{ 'City' : '雅安市', 'County' : '雨城区', 'CountyCode' : '511802'},
{ 'City' : '雅安市', 'County' : '名山区', 'CountyCode' : '511803' },
{ 'City' : '雅安市', 'County' : '荥经县', 'CountyCode' : '511822'},
{ 'City' : '雅安市', 'County' : '汉源县', 'CountyCode' : '511823' },
{ 'City' : '雅安市', 'County' : '石棉县', 'CountyCode' : '511824'},
{ 'City' : '雅安市', 'County' : '天全县', 'CountyCode' : '511825'},
{ 'City' : '雅安市', 'County' : '芦山县', 'CountyCode' : '511826' },
{ 'City' : '雅安市', 'County' : '宝兴县', 'CountyCode' : '511827' },

{ 'City' : '巴中市', 'County' : '巴州区', 'CountyCode' : '511902' },
{ 'City' : '巴中市', 'County' : '恩阳区', 'CountyCode' : '511903' },
{ 'City' : '巴中市', 'County' : '通江县', 'CountyCode' : '511921' },
{ 'City' : '巴中市', 'County' : '南江县', 'CountyCode' : '511922' },
{ 'City' : '巴中市', 'County' : '平昌县', 'CountyCode' : '511923' },

{ 'City' : '资阳市', 'County' : '雁江区', 'CountyCode' : '512002'  },
{ 'City' : '资阳市', 'County' : '安岳县', 'CountyCode' : '512021'  },
{ 'City' : '资阳市', 'County' : '乐至县', 'CountyCode' : '512022' },

{ 'City' : '阿坝藏族羌族自治州', 'County' : '马尔康市', 'CountyCode' : '513201'},
{ 'City' : '阿坝藏族羌族自治州', 'County' : '汶川县', 'CountyCode' : '513221' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '理县', 'CountyCode' : '513222' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '茂县', 'CountyCode' : '513223' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '松潘县', 'CountyCode' : '513224'  },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '九寨沟县', 'CountyCode' : '513225' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '金川县', 'CountyCode' : '513226' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '小金县', 'CountyCode' : '513227' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '黑水县', 'CountyCode' : '513228' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '壤塘县', 'CountyCode' : '513230' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '阿坝县', 'CountyCode' : '513231' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '若尔盖县', 'CountyCode' : '513232' },
{ 'City' : '阿坝藏族羌族自治州', 'County' : '红原县', 'CountyCode' : '513233' },

{ 'City' : '甘孜藏族自治州', 'County' : '康定市', 'CountyCode' : '513301' },
{ 'City' : '甘孜藏族自治州', 'County' : '泸定县', 'CountyCode' : '513322' },
{ 'City' : '甘孜藏族自治州', 'County' : '丹巴县', 'CountyCode' : '513323'},
{ 'City' : '甘孜藏族自治州', 'County' : '九龙县', 'CountyCode' : '513324' },
{ 'City' : '甘孜藏族自治州', 'County' : '雅江县', 'CountyCode' : '513325' },
{ 'City' : '甘孜藏族自治州', 'County' : '道孚县', 'CountyCode' : '513326' },
{ 'City' : '甘孜藏族自治州', 'County' : '炉霍县', 'CountyCode' : '513327'},
{ 'City' : '甘孜藏族自治州', 'County' : '甘孜县', 'CountyCode' : '513328' },
{ 'City' : '甘孜藏族自治州', 'County' : '新龙县', 'CountyCode' : '513329'  },
{ 'City' : '甘孜藏族自治州', 'County' : '德格县', 'CountyCode' : '513330' },
{ 'City' : '甘孜藏族自治州', 'County' : '白玉县', 'CountyCode' : '513331'  },
{ 'City' : '甘孜藏族自治州', 'County' : '石渠县', 'CountyCode' : '513332'  },
{ 'City' : '甘孜藏族自治州', 'County' : '色达县', 'CountyCode' : '513333'  },
{ 'City' : '甘孜藏族自治州', 'County' : '理塘县', 'CountyCode' : '513334'  },
{ 'City' : '甘孜藏族自治州', 'County' : '巴塘县', 'CountyCode' : '513335'  },
{ 'City' : '甘孜藏族自治州', 'County' : '乡城县', 'CountyCode' : '513336'  },
{ 'City' : '甘孜藏族自治州', 'County' : '稻城县', 'CountyCode' : '513337' },
{ 'City' : '甘孜藏族自治州', 'County' : '得荣县', 'CountyCode' : '513338' },

{ 'City' : '凉山彝族自治州', 'County' : '西昌市', 'CountyCode' : '513401' },
{ 'City' : '凉山彝族自治州', 'County' : '木里藏族自治县', 'CountyCode' : '513422' },
{ 'City' : '凉山彝族自治州', 'County' : '盐源县', 'CountyCode' : '513423' },
{ 'City' : '凉山彝族自治州', 'County' : '德昌县', 'CountyCode' : '513424' },
{ 'City' : '凉山彝族自治州', 'County' : '会理县', 'CountyCode' : '513425'},
{ 'City' : '凉山彝族自治州', 'County' : '会东县', 'CountyCode' : '513426'},
{ 'City' : '凉山彝族自治州', 'County' : '宁南县', 'CountyCode' : '513427' },
{ 'City' : '凉山彝族自治州', 'County' : '普格县', 'CountyCode' : '513428'},
{ 'City' : '凉山彝族自治州', 'County' : '布拖县', 'CountyCode' : '513429' },
{ 'City' : '凉山彝族自治州', 'County' : '金阳县', 'CountyCode' : '513430'},
{ 'City' : '凉山彝族自治州', 'County' : '昭觉县', 'CountyCode' : '513431' },
{ 'City' : '凉山彝族自治州', 'County' : '喜德县', 'CountyCode' : '513432' },
{ 'City' : '凉山彝族自治州', 'County' : '冕宁县', 'CountyCode' : '513433' },
{ 'City' : '凉山彝族自治州', 'County' : '越西县', 'CountyCode' : '513434' },
{ 'City' : '凉山彝族自治州', 'County' : '甘洛县', 'CountyCode' : '513435'},
{ 'City' : '凉山彝族自治州', 'County' : '美姑县', 'CountyCode' : '513436' },
{ 'City' : '凉山彝族自治州', 'County' : '雷波县', 'CountyCode' : '513437' }
]


