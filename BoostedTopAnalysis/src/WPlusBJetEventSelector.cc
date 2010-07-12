#include "Analysis/BoostedTopAnalysis/interface/WPlusBJetEventSelector.h"
#include "DataFormats/Math/interface/deltaR.h"

WPlusBJetEventSelector::WPlusBJetEventSelector ( edm::ParameterSet const & params ) :
  jetTag_	(params.getParameter<edm::InputTag>("jetSrc")  ),
  wJetSelector_ (params.getParameter<edm::ParameterSet>("BoostedTopWJetParameters") ),
  jetPtMin_	(params.getParameter<double>("jetPtMin") ),
  jetEtaMax_	(params.getParameter<double>("jetEtaMax") ),
  dR_		(params.getParameter<double>("coneSize")  ),
  bTagAlgo_	(params.getParameter<string>("bTagAlgorithm") ),
  bTagOP_	(params.getParameter<double>("bTagOP")  )
{
  //make the bitset
  push_back("Inclusive");
  push_back(">= 1 WJet");
  push_back(">= 1 bJet");

  //turn on
  set("Inclusive");
  set(">= 1 WJet");
  set(">= 1 bJet");
}

bool WPlusBJetEventSelector::operator() (edm::EventBase const & t, reco::Candidate::LorentzVector const & v, pat::strbitset & ret, bool towards)
{
  ret.set(false);
  wJets_.clear();
  bJets_.clear();

  passCut( ret, "Inclusive" );

  edm::Handle<vector<pat::Jet>  >   jetHandle;
  t.getByLabel( jetTag_, jetHandle );

  //Get the towards Lorentz vector
  reco::Candidate::LorentzVector vtowards = (towards) ? v : (-1)*v ;

  //Search for top jets
  for( vector<pat::Jet>::const_iterator jetBegin=jetHandle->begin(), jetEnd=jetHandle->end(), ijet=jetBegin ;
    ijet!=jetEnd; ijet++ )
  {
    //Only consider jets in the towards hemisphere
    double deltaR_ = reco::deltaR<double>( vtowards.eta(), vtowards.phi(), ijet->eta(), ijet->phi()  );
    if( deltaR_ < dR_ ) {
      if( ijet->pt() > jetPtMin_ && fabs( ijet->eta() ) < jetEtaMax_ ) {
        pat::strbitset iret = wJetSelector_.getBitTemplate();
	if( wJetSelector_( *ijet, iret )  ) {
	  wJets_.push_back( reco::ShallowClonePtrCandidate( edm::Ptr<pat::Jet>( jetHandle, ijet-jetBegin )  )  );
	} // end if wjet selector
	// not W jet, check b tag
	else {
	  if( ijet->bDiscriminator( bTagAlgo_ ) > bTagOP_ )
	    bJets_.push_back( reco::ShallowClonePtrCandidate( edm::Ptr<pat::Jet>( jetHandle, ijet-jetBegin )  )  );
	}  // end else
      }  // end if pt, eta
    } // end if deltaR

  }  // end for pat jets

  if( ignoreCut(">= 1 WJet") || hasWJets() )  {
    passCut( ret, ">= 1 WJet" );

    if( ignoreCut(">= 1 bJet") || hasBJets() ) {
      passCut( ret, ">= 1 bJet" );
    }  // end >= 1 bjet
  }  // end >= 1 wjet

  return (bool)ret;
}

