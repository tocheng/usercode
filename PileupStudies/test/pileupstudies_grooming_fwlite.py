#! /usr/bin/env python
import os
import glob
import math

from optparse import OptionParser

parser = OptionParser()


############################################
#            Job steering                  #
############################################

# Input files to use. This is in "glob" format, so you can use wildcards.
# If you get a "cannot find file" type of error, be sure to use "\*" instead
# of "*" to make sure you don't confuse the shell. 
parser.add_option('--files', metavar='F', type='string', action='store',
                  dest='files',
                  help='Input files')

# Output name to use. 
parser.add_option('--outname', metavar='F', type='string', action='store',
                  default='pileupstudies_fwlite',
                  dest='outname',
                  help='output name')


# RECO collection
parser.add_option('--recoColl', metavar='F', type='string', action='store',
                  default='ak5Lite',
                  dest='recoColl',
                  help='reco collection')

# GEN collection
parser.add_option('--genColl', metavar='F', type='string', action='store',
                  default='ak5Gen',
                  dest='genColl',
                  help='gen collection')

# "Undo" JEC?
parser.add_option('--uncorrInput', action='store_true',
                  default=False,
                  dest='uncorrInput',
                  help='Set to true if input jets are uncorrected')

# Output name to use. 
parser.add_option('--max', metavar='M', type='int', action='store',
                  default=-1,
                  dest='max',
                  help='Maximum number of events to process, default = all')

# Verbosity
parser.add_option('--verbose', action='store_true',
                  default=False,
                  dest='verbose',
                  help='Verbose switch')



# job splitting
parser.add_option('--nsplit', type='int', action='store',
                  default=None,
                  dest='nsplit',
                  help='Number of split jobs')
parser.add_option('--isplit', type='int', action='store',
                  default=None,
                  dest='isplit',
                  help='Index of job (0...nsplit)')

(options, args) = parser.parse_args()

argv = []

# Import everything from ROOT
import ROOT
ROOT.gROOT.Macro("rootlogon.C")

# Import stuff from FWLite
import sys
from DataFormats.FWLite import Events, Handle

ROOT.gSystem.Load('libCondFormatsJetMETObjects')

#from CondFormats.JetMETObjects import *


def findGenJet( recoJet0, genJets ) :
    minDR = 0.5
    retVal = None
    if options.verbose :
        print ' recojet eta,phi = {0:6.2f}, {1:6.2f}'.format( recoJet0.Eta(), recoJet0.Phi())
    for genJet in genJets :
        dR = recoJet0.DeltaR( genJet )
        if options.verbose :
            print ' -genjet eta,phi = {0:6.2f}, {1:6.2f}'.format( genJet.Eta(), genJet.Phi())
        if dR < minDR :
            if options.verbose :
                print 'new minimum, dR = ' + str(dR)
            minDR = dR
            retVal = genJet
    return retVal


print 'Getting files from this dir: ' + options.files

files = []
# Get the file list.
if options.files.find('.txt') >= 0 :
    infile = open( options.files, 'r')
    tmpfiles = infile.readlines()
    for ifile in tmpfiles :
        s = ifile.rstrip()
        print s
        files.append( s )

elif options.nsplit is None :
    files = glob.glob( options.files )
    for ifile in files:
        print ifile
elif options.nsplit is not None :


    tmpfiles = glob.glob( options.files )
    print 'All files : '  + str(len(tmpfiles))
    for ifile in tmpfiles :
        print ifile

    tot = len(tmpfiles)
    nsplit = options.nsplit
    isplit = options.isplit
    msplit = tot / nsplit
    print 'Splitting into ' + str(nsplit) + ' jobs with ' + str(msplit) + ' elements each, this job is index ' + str(isplit)
    end = min( tot, (isplit + 1) * msplit )
    for i in range( isplit * msplit, end ) :
        files.append( tmpfiles[i] )
    print 'Selected files : '
    for ifile in files :
        print ifile

if len(files) == 0 :
    print 'No files, exiting'
    exit(0)


# Create the output file. 
f = ROOT.TFile(options.outname + ".root", "recreate")
f.cd()


# Make histograms
print "Creating histograms"

nJets = ROOT.TH1F("nJets",         "Number of Jets, p_{T} > 30 GeV;N_{Jets};Number",               20, -0.5, 19.5 )


############################################
#     Jet energy scale and uncertainties   #
############################################



jecStr = [
    'Jec11_V3_L1FastJet_AK5PFchs.txt',
    'Jec11_V3_L2Relative_AK5PFchs.txt',
    'Jec11_V3_L3Absolute_AK5PFchs.txt',
    ]

jecPars = ROOT.std.vector(ROOT.JetCorrectorParameters)()

for ijecStr in jecStr :
    ijec = ROOT.JetCorrectorParameters( ijecStr )
    jecPars.push_back( ijec )
    

jec = ROOT.FactorizedJetCorrector(jecPars)

jecUncStr = ROOT.std.string('Jec11_V3_Uncertainty_AK5PFchs.txt')
jecUnc = ROOT.JetCorrectionUncertainty( jecUncStr )



############################################
# Physics level parameters for systematics #
############################################

# Kinematic cuts:
jetPtMin = 30.0


print 'Creating events...',
events = Events (files)
print 'Done'

jetPxHandle          = Handle( "std::vector<float>" )
jetPxLabel           = ( options.recoColl,   "px" )
jetPyHandle          = Handle( "std::vector<float>" )
jetPyLabel           = ( options.recoColl,   "py" )
jetPzHandle          = Handle( "std::vector<float>" )
jetPzLabel           = ( options.recoColl,   "pz" )
jetEnergyHandle      = Handle( "std::vector<float>" )
jetEnergyLabel       = ( options.recoColl,   "energy" )
jetJecFactorHandle   = Handle( "std::vector<float>" )
jetJecFactorLabel    = ( options.recoColl,   "jecFactor" )
jetAreaHandle        = Handle( "std::vector<float>" )
jetAreaLabel         = ( options.recoColl,   "jetArea" )


genJetPxHandle       = Handle( "std::vector<float>" )
genJetPxLabel        = ( options.genColl,   "px" )
genJetPyHandle       = Handle( "std::vector<float>" )
genJetPyLabel        = ( options.genColl,   "py" )
genJetPzHandle       = Handle( "std::vector<float>" )
genJetPzLabel        = ( options.genColl,   "pz" )
genJetEnergyHandle   = Handle( "std::vector<float>" )
genJetEnergyLabel    = ( options.genColl,   "energy" )




puHandle = Handle("std::vector<PileupSummaryInfo>")
puLabel = ( "addPileupInfo", "")

rhoHandle         = Handle( "double" )
rhoLabel = ( "kt6PFJets",   "rho" )

etaRatioHist = ROOT.TH3F('etaRatio', 'etaRecoRatio', 50, -5.0, 5.0, 200, 0., 2.0, 25, 0, 25)
ptRatioHist = ROOT.TH3F('ptRatio', 'ptRecoRatio', 50, 0., 500., 200, 0., 2.0, 25, 0, 25)



    
# loop over events
count = 0
ntotal = events.size()
if options.max > 0 :
    ntotal = options.max
percentDone = 0.0
ipercentDone = 0
ipercentDoneLast = -1
print "Start looping"
for event in events:
    ipercentDone = int(percentDone)
    if options.verbose:
        print 'Processing {0:10.0f}/{1:10.0f} : {2:5.0f}%'.format(
        count, ntotal, ipercentDone )
    elif ipercentDone != ipercentDoneLast :
        ipercentDoneLast = ipercentDone
        print 'Processing {0:10.0f}/{1:10.0f} : {2:5.0f}%'.format(
            count, ntotal, ipercentDone )
    count = count + 1
    percentDone = float(count) / float(ntotal) * 100.0


    if options.max > 0 and count > options.max :
        break

    event.getByLabel( genJetPxLabel, genJetPxHandle )
    genJetPxs = genJetPxHandle.product()
    event.getByLabel( genJetPyLabel, genJetPyHandle )
    genJetPys = genJetPyHandle.product()
    event.getByLabel( genJetPzLabel, genJetPzHandle )
    genJetPzs = genJetPzHandle.product()
    event.getByLabel( genJetEnergyLabel, genJetEnergyHandle )
    genJetEnergys = genJetEnergyHandle.product()

    ngenjet = 0
    genJets = []
    for ijet in range(0,len(genJetPxs)) :
        v = ROOT.TLorentzVector(genJetPxs[ijet],
                                genJetPys[ijet],
                                genJetPzs[ijet],
                                genJetEnergys[ijet])
        genJets.append(v)
        ngenjet += 1
        if options.verbose :
            print ' gen jet {0:4.0f}, pt = {1:6.2f}, eta = {2:6.2f}, phi = {3:6.2f}'.format(
                ijet, v.Perp(), v.Eta(), v.Phi()
                )
    if ngenjet < 2 :
        if options.verbose :
             print 'ngenjets < 2, exiting' 
        continue


    event.getByLabel( jetPxLabel, jetPxHandle )
    jetPxs = jetPxHandle.product()
    event.getByLabel( jetPyLabel, jetPyHandle )
    jetPys = jetPyHandle.product()
    event.getByLabel( jetPzLabel, jetPzHandle )
    jetPzs = jetPzHandle.product()
    event.getByLabel( jetEnergyLabel, jetEnergyHandle )
    jetEnergys = jetEnergyHandle.product()
    event.getByLabel( jetAreaLabel, jetAreaHandle )
    jetAreas = jetAreaHandle.product()
    if not options.uncorrInput :
        event.getByLabel( jetJecFactorLabel, jetJecFactorHandle )
        jetJecFactors = jetJecFactorHandle.product()
        
    event.getByLabel( rhoLabel, rhoHandle )
    rho = rhoHandle.product()[0]


    njet = 0
    recoJets = []
    matchedGenJets = []
    for ijet in range(0,len(jetPxs)) :
        if not options.uncorrInput :
            vRaw = ROOT.TLorentzVector(jetPxs[ijet] * jetJecFactors[ijet],
                                       jetPys[ijet] * jetJecFactors[ijet],
                                       jetPzs[ijet] * jetJecFactors[ijet],
                                       jetEnergys[ijet] * jetJecFactors[ijet])
        else :
            vRaw = ROOT.TLorentzVector(jetPxs[ijet],
                                       jetPys[ijet],
                                       jetPzs[ijet],
                                       jetEnergys[ijet])
        

        jec.setJetEta(vRaw.Eta())
        jec.setJetPt(vRaw.Perp())
        jec.setJetA(jetAreas[ijet])
        jec.setRho(rho)
        factor = jec.getCorrection()

        v = vRaw * factor

        if v.Perp() > 30.0 :
            recoJets.append(v)
            genJet = findGenJet( v, genJets )
            if genJet is not None :
                matchedGenJets.append( genJet )
            else :
                break
            njet += 1
    if len(recoJets) < 2 or len(matchedGenJets) < len(recoJets) :
        if options.verbose :
            print 'njets < 2, exiting'
        continue

    if options.verbose :
        for ijet in range(0,len(recoJets)) :
            v = recoJets[ijet]
            genJet = matchedGenJets[ijet]
            print 'ijet = {0:4.0f}, raw pt = {1:6.2f}, corr pt = {2:6.2f}, eta = {3:6.2f}, phi = {4:6.2f}, gen pt = {5:6.2f}, gen eta = {6:6.2f}, gen phi = {7:6.2f}'.format(
                ijet, vRaw.Perp(), v.Perp(), v.Eta(), v.Phi(), genJet.Perp(), genJet.Eta(), genJet.Phi()
                )



    event.getByLabel( puLabel, puHandle )
    puInfos = puHandle.product()

    npu = puInfos[0].getPU_NumInteractions()



    for ijet in range(0,2):
        if options.verbose :
             print 'filling histograms for ijet = ' + str(ijet)
        recoJet = recoJets[ijet]
        genJet = matchedGenJets[ijet]
        ptRatioHist .Fill( genJet.Pt(),  recoJet.Pt() /genJet.Pt(),  npu )
        etaRatioHist.Fill( genJet.Eta(), recoJet.Pt() /genJet.Pt(),  npu )


f.cd()
f.Write()
f.Close()
