#!/usr/bin/env python

from run_iheartny_unfold import run_threads, Sample

import shlex

from optparse import OptionParser
parser = OptionParser()
parser.add_option('--postfit', metavar='F', type='string', action='store',
                  default=None,
                  dest='postfit',
                  help='Use posterior top-tagging SF? Options are \'comb\' (combined fit) or \'emu\' (separate e/mu fit result). Default is None (that means to use prior value).')
(options, args) = parser.parse_args()
argv = []


samples = [
    
    #------------------------------    
    # Nominal samples, NNPDF
    #------------------------------
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_inclusive_mu',
           title='TT_max700_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_nom',
           flags='--mttGenMax=700. --makeResponse --semilep=1.0 --pdfSys=0.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
           ),
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_700to1000_mu',
           title='TT_Mtt-700to1000_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_nom',
           flags='--makeResponse  --semilep=1.0 --pdfSys=0.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
    ),
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_1000toInf_mu',
           title='TT_Mtt-1000toInf_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_nom',
           flags='--makeResponse  --semilep=1.0 --pdfSys=0.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
    ),
    
    #------------------------------    
    # PDF Up samples, NNPDF
    #------------------------------
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_inclusive_mu',
           title='TT_max700_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_pdfup',
           flags='--mttGenMax=700. --makeResponse --semilep=1.0 --pdfSys=1.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
           ),
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_700to1000_mu',
           title='TT_Mtt-700to1000_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_pdfup',
           flags='--makeResponse  --semilep=1.0 --pdfSys=1.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
    ),
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_1000toInf_mu',
           title='TT_Mtt-1000toInf_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_pdfup',
           flags='--makeResponse  --semilep=1.0 --pdfSys=1.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
    ),
    
    #------------------------------    
    # PDF Down samples, NNPDF
    #------------------------------
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_inclusive_mu',
           title='TT_max700_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_pdfdown',
           flags='--mttGenMax=700. --makeResponse --semilep=1.0 --pdfSys=-1.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
           ),
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_700to1000_mu',
           title='TT_Mtt-700to1000_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_pdfdown',
           flags='--makeResponse  --semilep=1.0 --pdfSys=-1.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
    ),
    Sample(directory='/store/user/skinnari/Unfold_24feb2015/TT_1000toInf_mu',
           title='TT_Mtt-1000toInf_CT10_TuneZ2star_8TeV-powheg-tauola_iheartNY_V1_mu_NNPDF_pdfdown',
           flags='--makeResponse  --semilep=1.0 --pdfSys=-1.0 --pdfSet=2.0',
           pdfsys=False, noms=True, jersys=True, jecsys=True, btagsys=True, toptagsys=True, qcd=True, postfit=options.postfit
    ),

]


run_threads( samples )
# Now the threads are done, exit gracefully
#print 'So long, and thanks for all the fish!'
