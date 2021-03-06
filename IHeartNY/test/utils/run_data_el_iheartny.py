#!/usr/bin/env python

from run_iheartny_mod import run_threads, Sample

import shlex


samples = [
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012A_22Jan/res/*root',
           title='SingleEl_iheartNY_V1_el_Run2012A', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012B_22Jan/res/*root',
           title='SingleEl_iheartNY_V1_el_Run2012B', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_1*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_1', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_2*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_2', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_3*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_3', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_4*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_4', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_5*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_5', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_6*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_6', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_7*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_7', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_8*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_8', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012C_22Jan/res/shyft_ultraslim_9*.root',
           title='SingleEl_iheartNY_V1_el_Run2012C_9', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_1*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_1', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_2*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_2', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_3*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_3', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_4*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_4', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_5*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_5', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_6*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_6', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_7*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_7', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_8*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_8', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele'),
    Sample(directory='/uscms_data/d3/skinnari/TopXS_Feb15/CMSSW_5_3_22_patch1/src/Analysis/IHeartNY/test/ElectronHad_Run2012D_22Jan/res/shyft_ultraslim_9*.root',
           title='SingleEl_iheartNY_V1_el_Run2012D_9', jersys=None, jecsys=False, pdfsys=False, qcd=True, pu=None, noms=True, flags='--isData --lepType=ele')
]

run_threads( samples )
# Now the threads are done, exit gracefully
print 'So long, and thanks for all the fish!'
