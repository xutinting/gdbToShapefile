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
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510104' },
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510105'},
{ 'City' : '�ɶ���', 'County' : '��ţ��', 'CountyCode' : '510106' },
{ 'City' : '�ɶ���', 'County' : '�����', 'CountyCode' : '510107' },
{ 'City' : '�ɶ���', 'County' : '�ɻ���', 'CountyCode' : '510108' },
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510109' },
{ 'City' : '�ɶ���', 'County' : '�츮�����ɶ�ֱ����', 'CountyCode' : '510110'  },
{ 'City' : '�ɶ���', 'County' : '��Ȫ����', 'CountyCode' : '510112'  },
{ 'City' : '�ɶ���', 'County' : '��׽���', 'CountyCode' : '510113'  },
{ 'City' : '�ɶ���', 'County' : '�¶���', 'CountyCode' : '510114'  },
{ 'City' : '�ɶ���', 'County' : '�½���', 'CountyCode' : '510115' },
{ 'City' : '�ɶ���', 'County' : '˫����', 'CountyCode' : '510116' },
{ 'City' : '�ɶ���', 'County' : 'ۯ����', 'CountyCode' : '510117'  },
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510121'  },
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510129' },
{ 'City' : '�ɶ���', 'County' : '�ѽ���', 'CountyCode' : '510131'  },
{ 'City' : '�ɶ���', 'County' : '�½���', 'CountyCode' : '510118'  },
{ 'City' : '�ɶ���', 'County' : '��������', 'CountyCode' : '510181'  },
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510182'  },
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510183' },
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510184'  },
{ 'City' : '�ɶ���', 'County' : '������', 'CountyCode' : '510185'  },

{ 'City' : '�Թ���', 'County' : '��������', 'CountyCode' : '510302' },
{ 'City' : '�Թ���', 'County' : '������', 'CountyCode' : '510303'  },
{ 'City' : '�Թ���', 'County' : '����', 'CountyCode' : '510304' },
{ 'City' : '�Թ���', 'County' : '��̲��', 'CountyCode' : '510311' },
{ 'City' : '�Թ���', 'County' : '����', 'CountyCode' : '510321' },
{ 'City' : '�Թ���', 'County' : '��˳��', 'CountyCode' : '510322' },

{ 'City' : '��֦����', 'County' : '����', 'CountyCode' : '510402'},
{ 'City' : '��֦����', 'County' : '����', 'CountyCode' : '510403'},
{ 'City' : '��֦����', 'County' : '�ʺ���', 'CountyCode' : '510411' },
{ 'City' : '��֦����', 'County' : '������', 'CountyCode' : '510421'},
{ 'City' : '��֦����', 'County' : '�α���', 'CountyCode' : '510422' },

{ 'City' : '������', 'County' : '������', 'CountyCode' : '510502' },
{ 'City' : '������', 'County' : '��Ϫ��', 'CountyCode' : '510503' },
{ 'City' : '������', 'County' : '����̶��', 'CountyCode' : '510504'},
{ 'City' : '������', 'County' : '����', 'CountyCode' : '510521' },
{ 'City' : '������', 'County' : '�Ͻ���', 'CountyCode' : '510522'},
{ 'City' : '������', 'County' : '������', 'CountyCode' : '510524'},
{ 'City' : '������', 'County' : '������', 'CountyCode' : '510525'},

{ 'City' : '������', 'County' : '�����', 'CountyCode' : '510603'},
{ 'City' : '������', 'County' : '�޽���', 'CountyCode' : '510604'},
{ 'City' : '������', 'County' : '�н���', 'CountyCode' : '510623'},
{ 'City' : '������', 'County' : '�㺺��', 'CountyCode' : '510681'},
{ 'City' : '������', 'County' : 'ʲ����', 'CountyCode' : '510682'},
{ 'City' : '������', 'County' : '������', 'CountyCode' : '510683' },

{ 'City' : '������', 'County' : '������', 'CountyCode' : '510703'},
{ 'City' : '������', 'County' : '������', 'CountyCode' : '510704'},
{ 'City' : '������', 'County' : '������', 'CountyCode' : '510705' },
{ 'City' : '������', 'County' : '��̨��', 'CountyCode' : '510722'},
{ 'City' : '������', 'County' : '��ͤ��', 'CountyCode' : '510723'},
{ 'City' : '������', 'County' : '������', 'CountyCode' : '510725'},
{ 'City' : '������', 'County' : '����Ǽ��������', 'CountyCode' : '510726' },
{ 'City' : '������', 'County' : 'ƽ����', 'CountyCode' : '510727' },
{ 'City' : '������', 'County' : '������', 'CountyCode' : '510781'},

{ 'City' : '��Ԫ��', 'County' : '������', 'CountyCode' : '510802' },
{ 'City' : '��Ԫ��', 'County' : '�ѻ���', 'CountyCode' : '510811' },
{ 'City' : '��Ԫ��', 'County' : '������', 'CountyCode' : '510812'},
{ 'City' : '��Ԫ��', 'County' : '������', 'CountyCode' : '510821'},
{ 'City' : '��Ԫ��', 'County' : '�ന��', 'CountyCode' : '510822'},
{ 'City' : '��Ԫ��', 'County' : '������', 'CountyCode' : '510823'},
{ 'City' : '��Ԫ��', 'County' : '��Ϫ��', 'CountyCode' : '510824'},

{ 'City' : '������', 'County' : '��ɽ��', 'CountyCode' : '510903' },
{ 'City' : '������', 'County' : '������', 'CountyCode' : '510904'},
{ 'City' : '������', 'County' : '��Ϫ��', 'CountyCode' : '510921'},
{ 'City' : '������', 'County' : '�����', 'CountyCode' : '510922'},
{ 'City' : '������', 'County' : '��Ӣ��', 'CountyCode' : '510923'},

{ 'City' : '�ڽ���', 'County' : '������', 'CountyCode' : '511002'},
{ 'City' : '�ڽ���', 'County' : '������', 'CountyCode' : '511011'},
{ 'City' : '�ڽ���', 'County' : '��Զ��', 'CountyCode' : '511024' },
{ 'City' : '�ڽ���', 'County' : '������', 'CountyCode' : '511025' },
{ 'City' : '�ڽ���', 'County' : '¡����', 'CountyCode' : '511083' },

{ 'City' : '��ɽ��', 'County' : '������', 'CountyCode' : '511102'},
{ 'City' : '��ɽ��', 'County' : 'ɳ����', 'CountyCode' : '511111'},
{ 'City' : '��ɽ��', 'County' : '��ͨ����', 'CountyCode' : '511112'},
{ 'City' : '��ɽ��', 'County' : '��ں���', 'CountyCode' : '511113'},
{ 'City' : '��ɽ��', 'County' : '��Ϊ��', 'CountyCode' : '511123' },
{ 'City' : '��ɽ��', 'County' : '������', 'CountyCode' : '511124'  },
{ 'City' : '��ɽ��', 'County' : '�н���', 'CountyCode' : '511126'  },
{ 'City' : '��ɽ��', 'County' : '�崨��', 'CountyCode' : '511129' },
{ 'City' : '��ɽ��', 'County' : '�������������', 'CountyCode' : '511132' },
{ 'City' : '��ɽ��', 'County' : '�������������', 'CountyCode' : '511133'  },
{ 'City' : '��ɽ��', 'County' : '��üɽ��', 'CountyCode' : '511181'},

{ 'City' : '�ϳ���', 'County' : '˳����', 'CountyCode' : '511302'  },
{ 'City' : '�ϳ���', 'County' : '��ƺ��', 'CountyCode' : '511303'  },
{ 'City' : '�ϳ���', 'County' : '������', 'CountyCode' : '511304'  },
{ 'City' : '�ϳ���', 'County' : '�ϲ���', 'CountyCode' : '511321' },
{ 'City' : '�ϳ���', 'County' : 'Ӫɽ��', 'CountyCode' : '511322' },
{ 'City' : '�ϳ���', 'County' : '���', 'CountyCode' : '511323'  },
{ 'City' : '�ϳ���', 'County' : '��¤��', 'CountyCode' : '511324'  },
{ 'City' : '�ϳ���', 'County' : '������', 'CountyCode' : '511325'  },
{ 'City' : '�ϳ���', 'County' : '������', 'CountyCode' : '511381'  },

{ 'City' : 'üɽ��', 'County' : '������', 'CountyCode' : '511402'  },
{ 'City' : 'üɽ��', 'County' : '������', 'CountyCode' : '511421'  },
{ 'City' : 'üɽ��', 'County' : '��ɽ��', 'CountyCode' : '511403'  },
{ 'City' : 'üɽ��', 'County' : '������', 'CountyCode' : '511423' },
{ 'City' : 'üɽ��', 'County' : '������', 'CountyCode' : '511424' },
{ 'City' : 'üɽ��', 'County' : '������', 'CountyCode' : '511425'  },

{ 'City' : '�˱���', 'County' : '������', 'CountyCode' : '511502'  },
{ 'City' : '�˱���', 'County' : '������', 'CountyCode' : '511504'  },
{ 'City' : '�˱���', 'County' : '��Ϫ��', 'CountyCode' : '511503'  },
{ 'City' : '�˱���', 'County' : '������', 'CountyCode' : '511523' },
{ 'City' : '�˱���', 'County' : '������', 'CountyCode' : '511524' },
{ 'City' : '�˱���', 'County' : '����', 'CountyCode' : '511525' },
{ 'City' : '�˱���', 'County' : '����', 'CountyCode' : '511526' },
{ 'City' : '�˱���', 'County' : '������', 'CountyCode' : '511527' },
{ 'City' : '�˱���', 'County' : '������', 'CountyCode' : '511528' },
{ 'City' : '�˱���', 'County' : '��ɽ��', 'CountyCode' : '511529'  },

{ 'City' : '�㰲��', 'County' : '�㰲��', 'CountyCode' : '511602' },
{ 'City' : '�㰲��', 'County' : 'ǰ����', 'CountyCode' : '511603'  },
{ 'City' : '�㰲��', 'County' : '������', 'CountyCode' : '511621'  },
{ 'City' : '�㰲��', 'County' : '��ʤ��', 'CountyCode' : '511622'  },
{ 'City' : '�㰲��', 'County' : '��ˮ��', 'CountyCode' : '511623'  },
{ 'City' : '�㰲��', 'County' : '������', 'CountyCode' : '511681'  },

{ 'City' : '������', 'County' : 'ͨ����', 'CountyCode' : '511702' },
{ 'City' : '������', 'County' : '�ﴨ��', 'CountyCode' : '511703' },
{ 'City' : '������', 'County' : '������', 'CountyCode' : '511722' },
{ 'City' : '������', 'County' : '������', 'CountyCode' : '511723'  },
{ 'City' : '������', 'County' : '������', 'CountyCode' : '511724' },
{ 'City' : '������', 'County' : '����', 'CountyCode' : '511725' },
{ 'City' : '������', 'County' : '��Դ��', 'CountyCode' : '511781' },

{ 'City' : '�Ű���', 'County' : '�����', 'CountyCode' : '511802'},
{ 'City' : '�Ű���', 'County' : '��ɽ��', 'CountyCode' : '511803' },
{ 'City' : '�Ű���', 'County' : '������', 'CountyCode' : '511822'},
{ 'City' : '�Ű���', 'County' : '��Դ��', 'CountyCode' : '511823' },
{ 'City' : '�Ű���', 'County' : 'ʯ����', 'CountyCode' : '511824'},
{ 'City' : '�Ű���', 'County' : '��ȫ��', 'CountyCode' : '511825'},
{ 'City' : '�Ű���', 'County' : '«ɽ��', 'CountyCode' : '511826' },
{ 'City' : '�Ű���', 'County' : '������', 'CountyCode' : '511827' },

{ 'City' : '������', 'County' : '������', 'CountyCode' : '511902' },
{ 'City' : '������', 'County' : '������', 'CountyCode' : '511903' },
{ 'City' : '������', 'County' : 'ͨ����', 'CountyCode' : '511921' },
{ 'City' : '������', 'County' : '�Ͻ���', 'CountyCode' : '511922' },
{ 'City' : '������', 'County' : 'ƽ����', 'CountyCode' : '511923' },

{ 'City' : '������', 'County' : '�㽭��', 'CountyCode' : '512002'  },
{ 'City' : '������', 'County' : '������', 'CountyCode' : '512021'  },
{ 'City' : '������', 'County' : '������', 'CountyCode' : '512022' },

{ 'City' : '���Ӳ���Ǽ��������', 'County' : '�������', 'CountyCode' : '513201'},
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '�봨��', 'CountyCode' : '513221' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '����', 'CountyCode' : '513222' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : 'ï��', 'CountyCode' : '513223' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '������', 'CountyCode' : '513224'  },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '��կ����', 'CountyCode' : '513225' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '����', 'CountyCode' : '513226' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : 'С����', 'CountyCode' : '513227' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '��ˮ��', 'CountyCode' : '513228' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '������', 'CountyCode' : '513230' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '������', 'CountyCode' : '513231' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '��������', 'CountyCode' : '513232' },
{ 'City' : '���Ӳ���Ǽ��������', 'County' : '��ԭ��', 'CountyCode' : '513233' },

{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513301' },
{ 'City' : '���β���������', 'County' : '����', 'CountyCode' : '513322' },
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513323'},
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513324' },
{ 'City' : '���β���������', 'County' : '�Ž���', 'CountyCode' : '513325' },
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513326' },
{ 'City' : '���β���������', 'County' : '¯����', 'CountyCode' : '513327'},
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513328' },
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513329'  },
{ 'City' : '���β���������', 'County' : '�¸���', 'CountyCode' : '513330' },
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513331'  },
{ 'City' : '���β���������', 'County' : 'ʯ����', 'CountyCode' : '513332'  },
{ 'City' : '���β���������', 'County' : 'ɫ����', 'CountyCode' : '513333'  },
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513334'  },
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513335'  },
{ 'City' : '���β���������', 'County' : '�����', 'CountyCode' : '513336'  },
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513337' },
{ 'City' : '���β���������', 'County' : '������', 'CountyCode' : '513338' },

{ 'City' : '��ɽ����������', 'County' : '������', 'CountyCode' : '513401' },
{ 'City' : '��ɽ����������', 'County' : 'ľ�����������', 'CountyCode' : '513422' },
{ 'City' : '��ɽ����������', 'County' : '��Դ��', 'CountyCode' : '513423' },
{ 'City' : '��ɽ����������', 'County' : '�²���', 'CountyCode' : '513424' },
{ 'City' : '��ɽ����������', 'County' : '������', 'CountyCode' : '513425'},
{ 'City' : '��ɽ����������', 'County' : '�ᶫ��', 'CountyCode' : '513426'},
{ 'City' : '��ɽ����������', 'County' : '������', 'CountyCode' : '513427' },
{ 'City' : '��ɽ����������', 'County' : '�ո���', 'CountyCode' : '513428'},
{ 'City' : '��ɽ����������', 'County' : '������', 'CountyCode' : '513429' },
{ 'City' : '��ɽ����������', 'County' : '������', 'CountyCode' : '513430'},
{ 'City' : '��ɽ����������', 'County' : '�Ѿ���', 'CountyCode' : '513431' },
{ 'City' : '��ɽ����������', 'County' : 'ϲ����', 'CountyCode' : '513432' },
{ 'City' : '��ɽ����������', 'County' : '������', 'CountyCode' : '513433' },
{ 'City' : '��ɽ����������', 'County' : 'Խ����', 'CountyCode' : '513434' },
{ 'City' : '��ɽ����������', 'County' : '������', 'CountyCode' : '513435'},
{ 'City' : '��ɽ����������', 'County' : '������', 'CountyCode' : '513436' },
{ 'City' : '��ɽ����������', 'County' : '�ײ���', 'CountyCode' : '513437' }
]


