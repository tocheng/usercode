import FWCore.ParameterSet.Config as cms

from PhysicsTools.SelectorUtils.pfElectronSelector_cfi import pfElectronSelector
from PhysicsTools.SelectorUtils.pfMuonSelector_cfi import pfMuonSelector

shyftPFSelection = cms.PSet(
    electronIdPFTight = pfElectronSelector.clone(
        cutsToIgnore=cms.vstring()
        ),
    muonIdPFTight = pfMuonSelector.clone(
        cutsToIgnore=cms.vstring()
        ),
    electronIdPFLoose = pfElectronSelector.clone(
        cutsToIgnore = cms.vstring('Fiducial','MaxMissingHits','D0','ConversionRejection','MVA')
        ),
    muonIdPFLoose = pfMuonSelector.clone(
        cutsToIgnore=cms.vstring('Chi2','minTrackerLayers','minValidMuHits','maxIp','minPixelHits','minMatchedStations')
        ),
    # input parameter sets
    muonSrc = cms.InputTag('selectedPatMuonsPFlow'),
    electronSrc = cms.InputTag('selectedPatElectronsPFlow'),
    jetSrc = cms.InputTag('goodPatJetsPFlow'),
    metSrc = cms.InputTag('patMETsPFlow'),
    trigSrc = cms.InputTag('patTriggerEvent'),
    rhoSrc = cms.InputTag('kt6PFJets', 'rho'),
    trig = cms.string(''),
    pvSrc   = cms.InputTag('goodOfflinePrimaryVertices'),    
    # kinematic cuts
    minJets        = cms.int32( 1 ),
    muPtMin        = cms.double( 20.0 ),
    muEtaMax       = cms.double( 2.1 ),
    eleEtMin       = cms.double( 20.0 ),
    eleEtaMax      = cms.double( 2.5 ),
    muPtMinLoose   = cms.double( 10.0 ),
    muEtaMaxLoose  = cms.double( 2.5 ),
    eleEtMinLoose  = cms.double( 20.0 ),
    eleEtaMaxLoose = cms.double( 2.5 ),
    jetPtMin       = cms.double( 30.0 ),
    jetEtaMax      = cms.double( 2.5 ),
    jetScale       = cms.double( 0.0 ),
    jetUncertainty = cms.double( 0.0 ),
    jetSmear       = cms.double( 0.0 ),
    metMin         = cms.double( 0.0 ),
    metMax         = cms.double( 100000.0),
    unclMetScale   = cms.double( 0.0 ),
    useData        = cms.bool(False),
    removeLooseLep = cms.bool(False),
    doElectrons    = cms.bool(False), # 0 = mu, 1 = ele
    looseLepRemovalDR=cms.double(0.5),
    tightMuMinIso  = cms.double(0.20), ## the cut values here are the ones used for top projections at PF2PAT level
    tightEleMinIso = cms.double(0.15),
    useL1Corr      = cms.bool(True),
    jecPayloads    = cms.vstring([
        'START53_V27_AK5PFchs_L1FastJet.txt',
        'START53_V27_AK5PFchs_L2Relative.txt',
        'START53_V27_AK5PFchs_L3Absolute.txt',
        'START53_V27_Uncertainty_AK5PF.txt']),
    cutsToIgnore   = cms.vstring( ['Trigger'] )
)
