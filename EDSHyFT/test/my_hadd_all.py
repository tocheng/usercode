#!/bin/python

import subprocess


dirs = [

'TTbarJets-madgraph_shyftana_38xOn35x_v1',
'WJets-madgraph_shyftana_38xOn35x_v1',
'ZJets-madgraph_shyftana_38xOn35x_v1',
'SingleTop_tWChannel-madgraph_shyftana_38xOn35x_v1',
'SingleTop_tChannel-madgraph_shyftana_38xOn35x_v1',
'SingleTop_sChannel-madgraph_shyftana_38xOn35x_v1',
'InclusiveMu15_shyftana_38xOn35x_v1',
'Vqq-madgraph_shyftana_38xOn35x_v1'


]

for idir in dirs :
    s = "hadd " + idir + '.root ' + idir + "/res/*.root"
    print s
    subprocess.call( [s, ""], shell=True )
