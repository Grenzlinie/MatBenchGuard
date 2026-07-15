
# A substitutional quantum defect in  \( WS_{2} \)  discovered by high-throughput computational screening and fabricated by site-selective STM manipulation

John C. Thomas \( ^{1,2,3*} \) , Wei Chen \( ^{4†} \) , Yihuang Xiong \( ^{3†} \) , Bradford A. Barker \( ^{5} \) , Junze Zhou \( ^{1} \) , Weiru Chen \( ^{3} \) , Antonio Rossi \( ^{1,2,6} \) , Nolan Kelly \( ^{5} \) , Zhuohang Yu \( ^{7,8} \) , Da Zhou \( ^{9} \) , Shalini Kumari \( ^{7,8} \) , Edward S. Barnard \( ^{1} \) , Joshua A. Robinson \( ^{7,8,9,10} \) , Mauricio Terrones \( ^{7,8,9,10} \) , Adam Schwartzberg \( ^{1} \) , D. Frank Ogletree \( ^{1} \) ，Eli Rotenberg \( ^{6} \) ，Marcus M. Noack \( ^{11} \) ，Sinéad Griffin \( ^{1,2} \) ，Archana Raja \( ^{1,2,} \) ，David A. Strubbe \( ^{5} \) ，Gian-Marco Rignanese \( ^{4} \) ，Alexander Weber-Bargioni \( ^{1,2*} \) ，and Geoffroy Hautier \( ^{3*} \) 

 \( ^{1} \) Molecular Foundry, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, United States of America

 \( ^{2} \) Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, CA, United States of America

 \( ^{3} \) Thayer School of Engineering, Dartmouth College, Hanover, NH 03755, USA

 \( ^{4} \) Institute of Condensed Matter and Nanoscience, Université catholique de Louvain, Louvain-la-Neuve 1348, Belgium

 \( ^{5} \) Department of Physics, University of California, Merced, Merced, CA 95343, USA  
 \( ^{6} \) Advanced Light Source, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, United States of America

 \( ^{7} \) Department of Materials Science and Engineering, The Pennsylvania State University, University Park, PA 16082 United States of America

 \( ^{8} \) Center for Two-Dimensional and Layered Materials, The Pennsylvania State University, University Park, PA, 16802 United States of America

 \( ^{9} \) Department of Physics, The Pennsylvania State University, University Park, PA, 16802 United States of America

 \( ^{10} \) Department of Chemistry, The Pennsylvania State University, University Park, PA, 16802 United States of America
 

#  \( ^{11} \) Applied Mathematics and Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, United States of America
 \( ^{*} \) jthomas@lbl.gov, afweber-bargioni@lbl.gov, geoffroy.hautier@dartmouth.edu
 \( ^{\dagger} \) These authors contributed equally.

## ABSTRACT

Point defects in two-dimensional materials are of key interest for quantum information science. However, the space of possible defects is immense, making the identification of high-performance quantum defects extremely challenging. Here, we perform high-throughput (HT) first-principles computational screening to search for promising quantum defects within  \( WS_{2} \) , which present localized levels in the band gap that can lead to bright optical transitions in the visible or telecom regime. Our computed database spans more than 700 charged defects formed through substitution on the tungsten or sulfur site. We found that sulfur substitutions enable the most promising quantum defects. We computationally identify the neutral cobalt substitution to sulfur ( \( Co_{S}^{0} \) ) as very promising and fabricate it with scanning tunneling microscopy (STM). The  \( Co_{S}^{0} \)  electronic structure measured by STM agrees with first principles and showcases an attractive new quantum defect. Our work shows how HT computational screening and novel defect synthesis routes can be combined to design new quantum defects.

## INTRODUCTION

Point defects in semiconductors are considered as building blocks for quantum information science (QIS) applications. Optically-active quantum defects (OQDs) can be used in quantum sensing, memory, and networks \( ^{1-4} \) . The performance of an OQD depends on its fundamental properties and limitations that can vary across defects \( ^{5,6} \) . Certain defects, such as the silicon-divacancy center in diamond, show robust optical coherence but low spin coherence, while the  \( NV^{-} \) center in diamond shows high spin coherence but lower optical coherence \( ^{7,8} \) . The identification of new OQDs in a specific host with optimal spin, optical, and electronic properties is essential to the development of QIS applications.

Two-dimensional (2D) materials, particularly transition metal dichalcogenides (TMDs), provide an enormous phase space of functionality with tunable and exceptional spin, optical and electronic properties \( ^{9-17} \) . Additionally, as materials are reduced from bulk to lower dimensionality, the spin-coherence lifetime of an OQD is expected to increase \( ^{18} \) . A decisive factor for an OQD is the appearance of in-gap localized states making it important to understand and measure the electronic levels induced by a defect in a given 2D host. While a number of techniques can routinely resolve the atomic lattice, the electronic levels introduced by the defect in the host are not easily accessible by most experimental
 

techniques. However, scanning tunneling microscopy (STM) and scanning tunneling spectroscopy (STS) can probe atomic-scale defects at the required length scale  \( {}^{19,20} \) . This has been used to characterize many defects in 2D materials, e.g., carbon radical dopants, chalcogen vacancies, oxygen substitutions, and a variety of metal substitutions  \( {}^{15,16,19,21-23} \) . Next to these experimental developments, first-principles approaches have been successfully used to compute and understand the properties of quantum defects in bulk semiconductors and 2D hosts  \( {}^{24-27} \) . First principles techniques have even been used to suggest OQDs in 2D materials, but these studies have remained targeted on a few defects and have not browsed the large elemental space of possible defects  \( {}^{28-32} \) .

Here, we use first principles high-throughput (HT) computing to build a database of point defects in  \( WS_{2} \)  considering all possible substitutional defects from 57 elements. We use this database to identify a handful of promising defects and show that the substitution of cobalt on sulfur ( \( Co_{S} \) ) in  \( WS_{2} \)  is especially appealing. First principles computations indicate that the neutral  \( Co_{S} \)  shows several localized levels in the band gap, spin multiplicity, and a potential for bright telecom emission. This defect is then synthesized in situ, examined with STM/STS, and the measured energy levels confirm and benchmark the theoretical predictions, which highlights a unique two-level quantum system.

## HIGH-THROUGHPUT SEARCH

A greatly sought-after electronic structure for an OQD involves two localized defect levels (one occupied, the other unoccupied) well within the band gap \( ^{33} \) . This requires a precise matching of defect and band edge levels. Additionally, the optical transition between these defect levels should be bright and exhibit large transition dipole moments (TDMs). While having localized defect levels within the band gap is not in itself necessary for developing OQDs, this electronic structure has advantages in terms of brightness and robustness versus temperature \( ^{34} \) . With the 2.4 eV electronic band gap for  \( WS_{2} \) , finding defect levels that are at the same time isolated within the band gap and with transitions in the telecom or visible range (from 750 meV up to 2 eV) should be achievable. However, identifying defects that could act as an OQD within  \( WS_{2} \)  is challenging.

To search for such a defect, we have built a database with the computed electronic structure of 757 charged point defects in  \( WS_{2} \)  considering either the tungsten ( \( M_{W} \) ) or sulfur ( \( M_{S} \) ) substitution site (see Fig. 1a). All the elements from the periodic table are used with the exception of rare-earths and transuranides. We start our screening by computing the relaxed structure and formation energies of the defect in multiple charge states within Density Functional Theory (DFT) in the generalized gradient approximation (GGA). Single-particle energies and band gaps are notoriously underestimated within DFT and one of the gold standards in defect computation is to use hybrid functionals such as PBE0 which adds a fraction of Fock exchange to the GGA functional \( ^{35,36} \) .
 

Recently, we have shown that for 2D materials, using a unique fraction of Fock exchange for the defect and the host is not adequate and we use here an approach combining a different amount of Fock exchange for defect levels and band edges (see Methods) \( ^{36} \) . The use of hybrid functionals leads to a significantly higher computational cost and can preclude broad screening. Here, we accelerate the hybrid computation by fixing the wave function from DFT and applying the hybrid functional Hamiltonian from PBE0 \( ^{37} \) . This single-shot PBE0 approach (or PBE0 \( _{0} \) ) is similar to the single-shot GW ( \( G_{0}W_{0} \) ) approach and enables single-particle energy predictions that are much improved compared to DFT at a minimal computational overhead, which we have used for defects in silicon \( ^{37} \) .

Our computational database includes formation energies, spin state, and single-particle electronic energy levels for all the possible charged defects. It also contains the TDMs between these single-particle levels indicating optical transition brightness. We use this database to search for attractive OQD candidates. We only consider defects with a charge state that is stable within a certain Fermi level ( \( E_{F} \) ) and with transitions between defect levels localized within the band gap. For these defects, we evaluate their single-particle excitation energies and TDMs. Fig. 1b shows the TDM versus excitation energy for all defects. We differentiate between  \( M_{S} \)  and  \( M_{W} \)  defects as well as singlets and multiplets. Few defects show high brightness (with a TDM of at least 2.5 D) and an excitation energy within the telecom or visible range (single-particle excitation energy > 750 meV) (see Supplementary Table 1 and Supplementary Figs. 1 and 2 for a full list with their single-particle levels). We identify a series of potential singlet OQDs that could act as single-photon emitters and are formed through the substitution of W with a main group element:  \( Sb_{W}^{-1} \) ,  \( P_{W}^{-1} \),  \( Pb_{W}^{-2} \) ,  \( N_{W}^{-1} \) , and  \( C_{W}^{-2} \) . Only two transition metal defects appear as promising singlets:  \( Os_{W} \)  and  \( Ti_{S} \) . Spin multiplets that are of greater technological interest only appear through sulfur substitution:  \( Co_{S}^{0} \) ,  \( Fe_{S}^{0} \),  \( Zn_{S}^{0} \) ,  \( Si_{S}^{-1} \) , and  \( W_{S}^{+1} \)  except for  \( Ru_{W}^{0} \) . The  \( W_{S} \)  defect has been suggested as an OQD by Tsai et al. as well, but in the zero charge state \( ^{28} \) . Notably, common substitutional defects to tungsten in  \( WS_{2} \) : Re, V, Nb, Mo, and Cr, do not show an adequate electronic structure (see Supplementary Fig. 3) \( ^{19,38-41} \) . They all have at most one level in the band gap of the substitutional d orbital character that is slightly above the valence band edge (V) or below the conduction band (Cr and Re). They are only excitable optically through a transition between a localized defect state and a delocalized band level forming a bound exciton \( ^{34} \) . Our findings agree with experimental results from photoluminescence or STS on  \( M_{W} \)  defects \( ^{19,38,40,41} \) .
 
![](./images/917724983780704774_1.jpg)

Fig. 1: Two-Level Quantum Defect Screening in WS \( _{2} \) . a Two defect configurations that are considered in this work: substitution on W site (M \( _{W} \) ) and on S site (M \( _{S} \) ). b Transition dipole moment vs. single-particle excitation energy at the single-shot PBE0. The marker and color scheme stand for the defect structure and whether the ground state is singlet or not. Each point stands for a charge defect that is thermodynamically stable within a certain E \( _{F} \)  range in the band gap, and with electronic structures that possess two localized defect levels within the band gap, as shown in the inset.

While substitutional transition metals on W sites are easy to synthesize, our screening results show that this is not the most promising approach for OQD discovery. All our candidate transition metal OQDs except  \( Ru_{W}^{0} \)  and  \( Os_{W}^{0} \(  show up instead as  \) M_{S} \( . Fig. 2a shows the different electronic structure for  \) M_{W} \(  and  \) M_{S} \(  in a molecular orbital diagram picture when M is a transition metal \) ^{42} $ . For both substitutions, the d orbitals of the defect mix with either sulfur ( \( M_{W} \) ) or tungsten ( \( M_{S} \) ) forming bonding and anti-bonding
 

states separated by  \( \Delta_{AB} \) . Additionally the different d orbitals are split in three groups:  \( (d_{xz}, d_{yz}) \) ,  \( (d_{xy}, d_{y^{2}-x^{2}}) \)  and  \( d_{z^{2}} \)  with an energy  \( \Delta d \)  according to crystal field splitting theory. For the sake of simplicity, we assume here a  \( C_{3v} \)  and  \( D_{3h} \)  point group respectively for the  \( M_{S} \)  and  \( M_{W} \)  defects, where lower symmetry through Jahn-Teller distortions are also possible. We performed bonding analysis, and determined density of states, for all 3d transition metal defects (Supplementary Fig. 4) and we observed a smaller splitting between bonding and anti-bonding states for  \( M_{S} \)  versus  \( M_{W} \)  ( \( \Delta_{AB} \) ). This can be rationalized by the different atomic positions for sulfur and tungsten orbitals. Additionally, the splitting between d orbitals ( \( \Delta d \) ) is higher for  \( M_{S} \)  versus  \( M_{W} \) . Fig. 2b shows the positions of bonding and anti-bonding molecular orbitals across the 3d series ( \( M_{W} \)  (blue) and  \( M_{S} \)  (yellow) in the neutral charge state), where 3d atomic orbitals shift to lower energy from Ti to Cu.  \( M_{S} \)  substitutions show clear advantage in terms of a smaller  \( \Delta_{AB} \)  and larger  \( \Delta_{d} \) , which leads to d-d transitions in the telecom or visible range and enables more potential for OQDs with two levels localized in the band gap.

![](./images/917724983780704774_2.jpg)

Fig. 2: Molecular orbital trend within the 3d transition metal series for  \( M_{S} \)  and  \( M_{W} \)  defects. a The molecular orbital diagram shows the splitting between anti-bonding and bonding state ( \( \Delta AB \) ) as well as the splitting with d orbitals ( \( \Delta d \) ) for a typical  \( M_{V} \)  and  \( M_{S} \)  defect. b A schematic of the bonding and anti-bonding state for different 3d transition metals in  \( M_{W} \)  (blue) and  \( M_{S} \)  (yellow) positions.

## CANDIDATES

While our analysis shows that within gap d-d transitions are more likely in  \( M_{S} \)  and rationalizes why there are still differences between  \( M_{S} \)  defects. Fig. 1 shows that  \( Co_{S}^{0} \)  is by far the most attractive OQD considering its non-singlet spin multiplicity, its large excitation energy, and transition dipole moment. We compute the electronic structure and formation energy for this  \( Co_{S}^{0} \)  defect within full-fledged PBE0 computations including structural relaxation and self-consistency. We plot the defect formation energy for different charge states of  \( Co_{S} \)  versus  \( E_{F} \)  in Fig. 3a. The defect is stable in its zero charge state spanning a
 

large  \( E_{F} \)  range. The two thermodynamic charge transition levels correspond to  \( (+1/0) \)  at 0.4 eV above the valence band maximum (VBM) and  \( (0/1-) \)  at 0.4 eV below the conduction band minimum (CBM).

![](./images/917724983780704774_3.jpg)

![](./images/917724983780704774_4.jpg)

Fig. 3: Thermodynamic charge transition levels and electronic structure of  \( Co_{S} \) . a Formation energy of  \( Co_{s} \)  as a function of Fermi level. The charge transition levels are referenced to the band-edge positions of pristine  \( WS_{2} \)  as obtained with PBE0 incorporating 22% of Fock exchange PBE0(0.22). b Orbital diagram of the localized defect states for neutral  \( Co_{S} \) . Resonant states within the valence band and conduction band manifolds are not depicted. The occupied (unoccupied) states are shown by the filled (empty) rectangles, the height of which indicates the degree of dispersion. The band-edge positions refer to those of the pristine  \( WS_{2} \)  obtained with PBE0(0.22). Energies are referenced to the vacuum level. SOC is not taken into account for the localized defect states. c Top view of the charge density (in blue) for the three  \( Co_{S}^{0} \)  defect states as indicated in b. The isovalue is  \( 0.001 e/Å^{3} \) .

The electronic structure of the neutral  \( Co_{S}^{0} \)  is shown in Fig. 3b. A full description of the electronic structure for all three charge states is given in Supplementary Fig. 5. The neutral defect undergoes a Jahn-Teller distortion towards the  \( C_{s} \)  symmetry. While there is significant mixing with the host, the projection on the Co-3d orbitals is provided in Fig. 3b with the wavefunctions illustrated in Fig. 3c. The defect shows occupied  \( d_{xy} \)  and  \( d_{z^{2}} \)  states well within the band gap that can be excited to the unoccupied  \( d_{x^{2}-y^{2}} \) ,  \( d_{xz} \)  or  \( d_{yz} \)  levels that are also below the conduction band. The lowest energy transition is between the  \( d_{z^{2}} \)  and  \( d_{x^{2}-y^{2}} \)  states and sits at a 1.5 eV difference in single-particle energies and shows a TDM of 1.2 D. All these values are obtained from full PBE0 but confirm the prediction from our screening at the single-shot level. The zero-phonon lines (ZPL) associated with this transition can be computed in constrained DFT by imposing the occupation of the unoccupied  \( d_{x^{2}-y^{2}} \)  state and relaxing the structure. We compute a ZPL of 0.96 eV, well within the telecom region. Transition from the  \( d_{z^{2}} \)  to the next orbital ( \( d_{xy} \) ) is significantly higher with a ZPL of 1.18 eV (and a TDM of 3.0 D). All these results confirm the interest of the neutral Co substitutional defect as it combines emission in the telecom and spin multiplicity.
 

In order to benchmark this novel screening approach, we create and characterize the  \( Co_{S} \)  defect. Comparisons between the specific energy levels and effective orbital symmetries enable a direct comparison with the HT screening approach and first-principles computations in general. In order to fabricate the  \( Co_{S} \)  defect in  \( WS_{2} \) , we make use of a unique experimental workflow inside a low temperature and ultrahigh vacuum (UHV) scanning probe microscope (SPM) that is shown in Fig. 4a-c. Sulfur vacancies ( \( V_{S} \) ) within otherwise as-grown  \( WS_{2} \)  are created by resistively heating the sample and, in tandem, exposing it to a low incidence angle  \( Ar^{+} \) sputtering beam (Fig. 4a) \( ^{43} \) . This technique produces a high density of  \( V_{S} \)  available for functionalization and subsequent reactivity. As adsorbed cobalt has been shown to be unstable on pristine TMD systems, such as  \( MoS_{2} \)  and  \( WS_{2} \) , we are able to make use of adsorbed instability near the VBM of  \( WS_{2} \)  (below -1.3 V) to systemically induce diffusion and/or evaporation events with the SPM tip \( ^{44,45} \) . A Co physical vapor deposition apparatus (Fig. 4b) in UHV deposits randomly adsorbed Co to a defective  \( WS_{2}/MLG/SiC(0001) \)  sample, which is held at liquid helium temperatures, at submonolayer coverage. The bias over an adsorbed Co atom can then be ramped towards the tip-induced diffusion energy range to effectively excite the Co adatom into a  \( V_{S} \)  for  \( Co_{S} \)  defect creation. Fig. 4d-g shows resulting data at each fabrication workflow step with scanning tunneling micrographs. Linear defects are identified as one dimensional inversion domains, which are a result of the  \( V_{S} \)  creation process and has been described in detail elsewhere \( ^{43} \) . We then focus on the realization of  \( Co_{S} \) . STM images, taken in constant-current mode, over a single Co defect are acquired before a Co diffusion event and after  \( Co_{S} \)  formation, where the apparent height is reduced by 0.14 nm (Fig. 4h).
 
![](./images/917724983780704774_5.jpg)

![](./images/917724983780704774_6.jpg)

![](./images/917724983780704774_7.jpg)

![](./images/917724983780704774_8.jpg)

![](./images/917724983780704774_9.jpg)

![](./images/917724983780704774_10.jpg)

Fig. 4:  \( Co_{S} \)  Defect Formation and Characterization. a The process of forming a high density of  \( V_{S} \) , b low-temperature deposition of Co atoms in situ, and c subsequent placement into a  \( V_{S} \)  with the assistance of the STM probe that is used to selectively manipulate atoms at voltage ranges below -1.3 V is shown schematically. Corresponding scanning tunneling micrographs that capture  \( WS_{2}/Gr/SiC(0001) \)  d after defect introduction via  \( Ar^{+} \) bombardment and e post Co deposition are plotted ( \( I_{tunnel} = 30 \)  pA,  \( V_{sample} = 1.2 \)  V). Scale bars, 2 nm. STM images f before a voltage excitation and g after Co substitution within an identified  \( V_{S} \)  are also shown ( \( I_{tunnel} = 30 \)  pA,  \( V_{sample} = 1.2 \)  V,  \( V_{excitation} = -2.1 \)  V). Scale bars, 2 nm. h The apparent height difference of  \( Co_{S} \)  compared to adsorption atop as-grown  \( WS_{2} \)  is measured to be 0.15 nm, taken from linescans across both f and g red highlighted regions.

In order to investigate the evolved electronic structure with SPM, we make use of STS and differential conductance mapping, which are representative of the local density of states (LDOS) over a given defect. Point STS over  \( Co_{S} \)  is shown in Fig. 5a-b, where in-gap states near 0.36 eV and 0.47 eV are measured. We attribute peak broadening to electronic-phonon coupling, where effective electron-phonon coupling strength is estimated with a single-mode Franck-Condon model \( ^{16} \) . We include multiple phonon modes and additional quanta of each mode (available for co-excitation) in the description detailed in Supplementary Fig. 6 to explain dI/dV signal strength and broadening observed beyond the model approximation. Additionally, a resonance peak is identified at negative voltages ( \( -0.84 \pm 0.06 \)  eV) that is attributed to electronic charging from the underlying substrate to  \( Co_{S} \) , which shifts the defect to an anion state, where an electron is, on average, donated to available  \( Co_{S} \)  defect levels. Spatially resolved DOS below the charging onset is comparable to that of the occupied orbitals in the anionic state and to the charge neutral state above this onset. Fig. 5c-e shows high-resolution differential conductance image
 

maps that detail electronic orbital densities measured at -0.9 eV, 0.36 eV, and 0.47 eV. The LDOS at these energies are further benchmarked against calculations at the PBE0 level of theory and shown in Fig. 5f-h for each energy range experimentally measured, where  \( Co_{S} \)  unoccupied orbitals are hybridized with bonded W atoms and are  \( \sim \) 1.5 nm in diameter (see Supplementary Fig. 7 for simulated STS for charge states presented). We find strong agreement between experiment and theoretically obtained energy levels and orbital symmetries, where we can then assign the dI/dV peak at 0.36 eV to predominantly  \( d_{x^{2}-y^{2}} \)  orbital density, and the peak measured at 0.47 eV to a mixing of  \( d_{yz} \)  and  \( d_{xz} \)  orbitals at the  \( Co_{S} \)  charge neutral state. The peak at -0.84 eV is attributed to the  \( Co_{S} \)  charging (to  \( Co_{S}^{-1} \) ), and is discussed in further detail below. Quantitatively, the  \( d_{x^{2}-y^{2}} \)  state is experimentally 0.64 eV below the CBM while theory predicts a level 0.5 eV below the CBM, indicating a good agreement.
 
![](./images/917724983780704774_11.jpg)

Fig. 5: Experimental and Simulated  \( Co_{S} \)  Scanning Tunneling Spectroscopy. a STS spectra recorded on a  \( Co_{S} \)  defect and the as-grown  \( WS_{2} \)  monolayer on graphene ( \( V_{modulation} = 5  mV \) ). b In-gap states identified are located at peak maxima of 0.36 eV and 0.47 eV, each with a full-width half maximum near 0.045 eV. Differential conductance (dI/dV) imaging maps over the defect are depicted at c = 0.9 eV, d = 0.373 eV, and e = 0.486 eV ( \( V_{modulation} = 5  mV \) ), showing  \( Co_{S} \)  orbital geometries. Scale bars, 0.25 nm. f-h Simulated STS maps using PBE0 over  \( Co_{S} \)  orbitals identifying energy range densities near experimentally measured values. Scale bars, 0.25 nm. A charging peak is identified in a, where the i lowest unoccupied  \( Co_{S}^{0} \)  state becomes j resonant with the  \( E_{F} \)  of the substrate and an electron is donated to produce the  \( Co_{S}^{-1} \)  defect. Both c and f are representative of the  \( Co_{S}^{-1} \)  orbital densities collected at the specified energy (the charging ring onset in c is removed for clarity).

We attribute the sharp peak at -0.84 eV to a charging process of the neutral cobalt to the anionic  \( Co_{S}^{-1} \)  state. This charging is due to the localized tip-induced band bending process has been described in the literature on similar systems \( ^{16,46} \) . The  \( Co_{S} \)  lowest unoccupied state is occupied at adequate negative voltages and alters the  \( Co_{S} \)  charge state making it anionic, detailed in Fig. 5i-j. The neutral/anionic charge transition level is computed to be around 2.1 eV above the VBM (see Fig. 3) which is close to the charge transition level for  \( V_{S} \)  (see Supplementary Fig. 13) for which a charging peak at a similar
 

position is observed for the same type of sample \( ^{16} \) . The charging peak near -0.84 eV varies spatially as the bias is ramped to more negative values: the radius of the ring around the defect center increases. In order to increase STS statistics, we perform an autonomous hyperspectral experiment over  \( Co_{S} \)  (see Supplementary Notes 1 and 2 in addition to Supplementary Figs. 8-11) \( ^{20} \) . The charging peak is found to energetically shift between a minimum of -0.924 eV and a maximum of -0.627 eV during point STS measurements, which amounts to a 0.3 eV tip-induced bending range of available states. This is near the onset of the lowest unoccupied state at  \( \sim \) 0.3 eV above the  \( E_{F} \) , enabling  \( Co_{S} \)  to behave as an electron acceptor. Spatially-resolved charging ring formation as a function of applied bias is shown in Supplementary Fig. 12, where linescans taken across differential conductance maps from the defect center to outside the charging region highlight a shift to larger distances at more negative voltages. Outside the defect charging region, the substrate remains in a neutral state, which is verified with STS around pristine  \( WS_{2} \)  regions. While the charging process makes the identification of states closer to the VBM less straightforward, we note that, inside the charging ring, a state around the cobalt is observed. This state has the form of a  \( d_{z^{2}} \)  orbital as expected from the computed LDOS of the neutral cobalt defect in that energy range (Fig. 5c and Supplementary Fig. 7b). The better comparison is with the LDOS of the  \( Co_{S}^{-1} \)  as the defect should be charged within the ring. Theory predicts a reorganization of orbitals, an upward shift of the  \( d_{z^{2}} \)  and a change of symmetry going from  \( C_{s} \)  to  \( C_{3v} \)  when  \( Co_{S} \)  becomes negatively charged (see Supplementary Fig. 5). From this picture, we expect the  \( d_{z^{2}} \)  state for  \( Co_{S}^{-1} \)  to be 1 eV lower than the  \( d_{x^{2}-y^{2}} \)  state from  \( Co_{S}^{0} \) . We found experimentally a value of 1.3 eV. If there is an upward shift of  \( d_{z^{2}} \)  when charged, it is smaller in experiment than in theory. This discrepancy could come from the influence of the dielectric environment of the graphene/SiC contacts that is not modeled in our  \( WS_{2} \)  system in vacuum. In any case, next to the  \( d_{x^{2}-y^{2}} \) ,  \( d_{yz} \)  and  \( d_{xz} \)  Co state within the band gap, an additional Co  \( d_{z^{2}} \)  state is observed within the band gap (and 1.3 eV lower than the  \( d_{x^{2}-y^{2}} \)  state) confirming the theoretical results that Co in  \( WS_{2} \)  can lead to a two-level system of great interest as a OQD.

## CONCLUSION

We use HT computational screening to search for promising quantum defects in  \( WS_{2} \) . Based on a database gathering computed properties for 757 charged defects in  \( WS_{2} \) , we identify a handful of promising quantum defects with high brightness and in-gap defect states compatible with optical emission in the telecom or visible range. We fabricate the  \( Co_{S}^{0} \)  defect, which shows brightness, a spin-doublet ground state, and a computed ZPL in the telecom at 0.966 eV, through metal deposition and subsequent sulfur vacancy substitution by cobalt with an STM tip. STM and STS analysis indicates cobalt-related defect states within the band gap confirming the computational prediction and the interest of  \( Co_{S} \)  as an OQD.
 

Our HT data indicates that fundamental electronic structure reasons make transition metal substitution on sulfur sites more likely to lead to a OQD with in-gap defect states that could emit in the telecom or visible than for the tungsten substitution. This motivates more efforts in the community along that direction. The fabrication process and HT computational screening used to identify  \( Co_{S} \)  highlight the capability of combining HT screening and advanced synthesis techniques to identify and realize new OQDs. This can be performed across a wide range of atomic species within 2D materials and other hosts with many yet to be experimentally realized, which can be executed for a number of different desired material properties, e.g., from catalysis to QIS.

## MATERIALS AND METHODS

## Scanning probe microscopy (SPM) measurements

All measurements were performed with a Createc GmbH scanning probe microscope operating under ultrahigh vacuum (pressure  \( <2\times10^{-10} \)  mbar) at liquid helium temperatures (T < 6 K). Either etched tungsten or platinum iridium tips were used during acquisition. Tip apexes were further shaped by indentations onto a gold substrate for subsequent measurements taken over a defective substrate. STM images are taken in constant-current mode with a bias applied to the sample. STS measurements were recorded using a lock-in amplifier with a resonance frequency of 683 Hz and a modulation amplitude of 5 mV.

## Sample preparation

Monolayer islands of  \( WS_{2} \)  were grown on graphene/SiC substrates with an ambient pressure CVD approach. A graphene/SiC substrate with 10 mg of  \( WO_{3} \)  powder on top was placed at the center of a quartz tube, and 400 mg of sulfur powder was placed upstream. The furnace was heated to  \( 900\;^{\circ}C \)  and the sulfur powder was heated to  \( 250\;^{\circ}C \)  using a heating belt during synthesis. A carrier gas for process throughput was used (Ar gas at 100 sccm) and the growth time was 60 min. The CVD grown  \( WS_{2}/MLG/SiC \)  was further annealed in vacuo at  \( 400\;^{\circ}C \)  for 2 hours. Cobalt was deposited at a pressure of  \( 1\times10^{-9}\;mbar \)  for 60 seconds with the sample held at 5 K.

## Neural network and Gaussian process implementation

The acquisition software used for autonomous experimentation was gpSTS, which is a library for autonomous experimentation for scanning probe microscopy \( ^{20,47} \) . An Intel Xeon E5-2623 v3 CPU with 8 cores and 64 GB of memory combined with a Tesla K80 with 4992 CUDA cores was used for training.
 

the neural network. Training data for  \( WS_{2} \)  and  \( V_{S} \)  was combined with  \( Co_{S} \)  spectra obtained from an extended autonomous run.

## First-principles calculations

We considered 57 elements that could substitute for W and S in the construction of a  \( WS_{2} \)  quantum defect database, as highlighted in the periodic table in Supplementary Fig. 1. This collection covers the majority of the elements except the rare-earth elements and noble gases. All defect computations were performed at DFT level using automatic defect workflows that are implemented in ATOMATE software package  \( {}^{48-50} \) . The defect structure generations and the formation energy computations are performed using PyCDT. The DFT calculations were performed using Vienna Ab-initio Simulation Package (VASP) \( {}^{51,52} \)  and the projector-augmented wave (PAW) method \( {}^{53} \)  with the Perdew-Burke-Ernzerhof (PBE) functional \( {}^{54} \) . Each charged defect is simulated in a 144-atom orthorhombic supercell and with a vacuum of approximately 14 Å. A plane-wave basis energy cutoff of 520 eV was used and the Brillouin zone is sampled using  \( \Gamma \)  point only. The defect structures were optimized at a fixed volume until the forces on the ions are smaller than 0.01 eV/ \( \AA \) . The charge states of each defect are determined by considering all the oxidation states of the elements documented in the ICSD database \( {}^{49} \)  and taking into account the formal charges in  \( WS_{2} \)  ( \( W^{4+} \)  and  \( S^{2-} \) ). The total energy of the charged defects were further corrected to overcome the finite-size effect using the method of Komsa et al. \( {}^{55,56} \)  as implemented in SLABCC \( {}^{57} \) .

The above procedures generated overall 757 substitutional charged defects in monolayer  \( WS_{2} \) . Based on the defect formation energy, we first identified 260 charged defects that are thermodynamically stable, meaning their charge states are accessible in a certain  \( E_{F} \)  range. Among these stable defects, we further search for the ones that possess two in-gap, localized levels that would enable the optical intra-defect transition. The localization is defined using inverse participation ratio (IPR) as detailed below. We considered levels with IPR larger than 0.05 as localized states (bulk-like states in general have IPR smaller than 0.01 in  \( WS_{2} \) ). This trimmed down the list to 143 candidates, among which 112 have non-singlet ground states. The classification of singlets and multiplets is based on the electronic structure of the defect. In this case, the singlets and multiplets refer to the total magnetic quantum number of the unpaired electrons. Thus, defects with all electrons paired are classified as singlet, while those with one or two paired electrons are classified as doublet, triplet, etc. We note that due to limitations of Kohn-Sham (KS) DFT and possibility of spin contamination for spin-polarized systems, more powerful methods such as spin-flip Bethe-Salpeter are required in general to rigorously determine the total spin  \( S^{58} \) . Finally, we screened out the ones that would emit at telecom wavelength with reasonable brightness. The emission wavelength is approximated using the single-particle KS energy difference using the single-shot PBE0 incorporating 7% of Fock exchange. We refrained from applying potential corrections at this stage as the
 

KS energy difference is largely unaffected by the electrostatic finite-size effect. The brightness of the optical transition is approximated by the transition dipole moment (TDM) as detailed below. To search for the most relevant transitions, we consider the transitions that give the smallest energy difference, while also allowing an energy window of up to 100 meV to take into account the errors and band degeneracy. We then identified the transition with the largest TDM as the most relevant transition. The above procedures recommend 17 non-singlet candidates that emit at least 750 meV with a TDM of 3 D, as shown in Supplementary Table 1.

The localization of an orbital is described using the IPR. For a given KS State, the IPR is evaluated based on the probabilities of finding an electron with an energy  \( E_{i} \)  close to an atomic site  \( \alpha^{59-61} \) :

 \[ \chi\left(E_{i}\right)=\frac{\sum_{\alpha}\rho_{\alpha}^{2}\left(E_{i}\right)}{\left[\sum_{\alpha}\rho_{\alpha}\left(E_{i}\right)\right]^{2}}, \quad (1) \] 

where the summation runs over all atomic sites  \( \alpha \) . The participation ratio  \( \chi^{-1} \)  stands for the number of atomic sites that confine the wave function. Thus, a larger (smaller) IPR indicates a localized (delocalized) state. IPR is unitless ranging between 0 to 1. We computed IPR using VASP PROCAR. The optical transition dipole moment was evaluated by the PYVASPWFC code based on the single-particle wavefunction calculated at the PBE level \( ^{62} \) . The transition dipole moment is written as:

 \[ \mu_{k}=\frac{\mathrm{i}\hbar}{\left(\varepsilon_{\mathrm{f},k}-\varepsilon_{\mathrm{i},k}\right)m}\left\langle\psi_{\mathrm{f},k}|\mathbf{p}|\psi_{\mathrm{i},k}\right\rangle, \quad (2) \] 

where  \( \hbar \)  is the Planck constant,  \( \varepsilon_{i,k} \)  and  \( \varepsilon_{f,k} \)  are the eigenvalues of the initial and final states, m is the electron mass,  \( \psi_{i} \)  and  \( \psi_{f} \)  are the initial and final wavefunctions, and p is the momentum operator.

For selected substitutional defects, we carried out the fully self-consistent hybrid functional (PBE0) calculations including structural relaxations. In line with the single-shot PBE0 calculations and following previous work \( ^{36} \) , we described the defect levels using the mixing parameter  \( \alpha = 0.07 \)  for the Fock exchange, which generally satisfies the Koopmans' condition for localized defects in monolayer WS \( _{2} \) . On the other hand, we used  \( \alpha = 0.22 \)  for the pristine WS \( _{2} \)  to determine the band-edge position. The alignment of defect levels with respect to the band edges was then achieved through the vacuum level which serves a common reference level. Spin-orbit coupling (SOC) is taken into account unless otherwise specified. We used a planewave cutoff energy of 400 eV and a  \( 2 \times 2 \times 1 \)  k-point mesh for ground-state calculations. The zero-phonon line was assessed using a single  \( \Gamma \)  point by imposing occupation constraints (constrained DFT \( ^{27} \) ). For charged defects, the total energies are subject to finite-size effects and were corrected by the method of Komsa et al. \( ^{55,56} \)  as implemented in SLABBCC \( ^{57} \) , whereas the single-particle KS levels were corrected by the potential correction scheme (SCPC) of Chagas da Silva et al. \( ^{63} \) . The simulated STM images were plotted at a constant height of 3.5 Å above the surface using the STM-2DScan package \( ^{64} \)  based on the Tersoff-Hamann theory \( ^{65} \) .
 

## Data availability

The data that support the findings of this study are available from the corresponding authors on reasonable request.

## Code availability

The code used for the findings of this study are available from the corresponding authors on reasonable request.

## Acknowledgements

This work was supported by the U.S. Department of Energy, Office of Science, Basic Energy Sciences in Quantum Information Science under Award Number DE-SC0022289. This work was supported as part of the Center for Novel Pathways to Quantum Coherence in Materials, an Energy Frontier Research Center funded by the U.S. Department of Energy, Office of Science, Basic Energy Sciences. Work was performed at the Molecular Foundry and at the Advanced Light Source supported by the Office of Science, Office of Basic Energy Sciences, of the U.S. Department of Energy under contract no. DE-AC02-05CH11231. S.K and J.A.R. acknowledge support from the National Science Foundation Division of Materials Research (NSF-DMR) under awards 2002651 and 2011839. N.K. and D.A.S acknowledge support from the National Science Foundation award DMR-2144317, and the Merced nAnomaterials Center for Energy and Sensing (MACES), a NASA-funded research and education center, under award NNH18ZHA008CMIROG6R. B.A.B. was supported by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, CTC and CPIMS Programs, under Award DE-SC0019053. This research used resources of the National Energy Research Scientific Computing Center, a DOE Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231 using NERSC award BES-ERCAP0020966. Additional computational resources were provided by the Multi-Environment Computer for Exploration and Discovery (MERCED) cluster at UC Merced, funded by National Science Foundation Grant No. ACI-1429783.

## Author Contributions

G.H., A.W.-B, J.C.T., S.G., A. R. conceived the overall project. W.C., Y.X., B.A.B., W. C., S.G., D.A.S., G.-M.R., and G.H. performed the theoretical simulations along with compiling the database for quantum defect search. J.C.T, J.Z., and A.R. performed STM/STS experiments and subsequent analysis with support from E.S.B., A.S., D.F.O., E.R., A.R., and A.W.-B. J.C.T. and M.M.N. implemented autonomous experimentation. Z.Y., D.Z., S.K., J.A.R., and M.T. carried out sample growth. All authors discussed the results and contributed towards the manuscript.
 

## Competing interests

The authors declare that they have no competing interests.

## REFERENCES

[1] Maletinsky, P. et al. A robust scanning diamond sensor for nanoscale imaging with single nitrogen-vacancy centres. Nat. Nanotechnol. 7, 320 (2012).

[2] Bradley, C. E. et al. A Ten-Qubit Solid-State spin register with quantum memory up to one minute. Phys. Rev. X 9, 031045 (2019).

[3] Pompili, M. et al. Realization of a multinode quantum network of remote solid-state qubits. Science 372, 259 (2021).

[4] Wolfowicz, G. et al. Quantum guidelines for solid-state spin defects. Nat. Rev. Mater. 6, 906 (2021).

[5] Bassett, L. C., Alkauskas, A., Exarhos, A. L., & Fu, K.-M. C. Quantum defects by design. Nanophotonics 8, 1867 (2019).

[6] Atatüre, M., Englund, D., Vamivakas, N., Lee, S.-Y., & Wrachtrup, J. Material platforms for spin-based photonic quantum technologies. Nat. Rev. Mater. 3, 38 (2018).

[7] Sukachev, D. D. et al. Silicon-Vacancy spin qubit in diamond: A quantum memory exceeding 10 ms with Single-Shot state readout. Phys. Rev. Lett. 119, 223602 (2017).

[8] Bourgeois, E., Gulka, M., & Nesladek, M. Photoelectric detection and quantum readout of nitrogen-vacancy center spin states in diamond. Adv. Opt. Mater. 8, 1902132 (2020).

[9] Stern, H. L. et al. Room-temperature optically detected magnetic resonance of single defects in hexagonal boron nitride. Nat. Commun. 13, 618 (2022).

[10] Kianinia, M., Xu, Z.-Q., Toth, M., & Aharonovich, I. Quantum emitters in 2D materials: emitter engineering, photophysics, and integration in photonic nanostructures. Appl. Phys. Rev. 9, 011306 (2022).

[11] Lin, Z. et al. Defect engineering of two-dimensional transition metal dichalcogenides. 2D Mater. 3, 022002 (2016).

[12] Manzeli, S., Ovchinnikov, D., Pasquier, D., Yazyev, O. V., & Kis, A. 2D transition metal dichalcogenides. Nat. Rev. Mater. 2, 1 (2017).
 

[13] Li, C. et al. Engineering graphene and TMDs based van der waals heterostructures for photovoltaic and photoelectrochemical solar energy conversion. Chem. Soc. Rev. 47, 4981 (2018).

[14] Ugeda, M. M. et al. Observation of topologically protected states at crystalline phase boundaries in single-layer  \( WSe_{2} \) . Nature Communications, vol. 9, p. 3401, Aug 2018.

[15] Schuler, B. et al. Electrically driven photon emission from individual atomic defects in monolayer  \( WS_{2} \) . Sci. Adv. 6, eabb5988 (2020).

[16] Schuler, B. et al. Large spin-orbit splitting of deep in-gap defect states of engineered sulfur vacancies in monolayer  \( WS_{2} \) . Phys. Rev. Lett. 123, 076801 (2019).

[17] Montblanch, A. R. P., Barbone, M., Aharonovich, I., Atatür, M., & Ferrari, A. C. Layered materials as a platform for quantum technologies. Nat. Nanotechnol. 18, 555 (2023).

[18] Ye, M., Seo, H., & Galli, G. Spin coherence in two-dimensional materials. npj Comput. Mater. 5, 44 (2019).

[19] Schuler, B. et al. How substitutional point defects in two-dimensional  \( WS_{2} \)  induce charge localization, spin-orbit splitting, and strain. ACS Nano 13, 10520 (2019).

[20] Thomas, J. C. et al. Autonomous scanning probe microscopy investigations over WS2 and Au{111}. npj Comput. Mater. 8, 99 (2022).

[21] Barja, S. et al. Identifying substitutional oxygen as a prolific point defect in monolayer transition metal dichalcogenides. Nat. Commun. 10, 3382 (2019).

[22] Cochrane, K. A. et al. Spin-dependent vibronic response of a carbon radical ion in two-dimensional  \( WS_{2} \) . Nat. Commun. 12, 7287 (2021).

[23] Stolz, S. et al. Layer-dependent schottky contact at van der waals interfaces: V-doped  \( WSe_{2} \)  on graphene," npj 2D Mater. Appl. 6, 66 (2022).

[24] Gali, A. Ab initio theory of the nitrogen-vacancy center in diamond. Nanophotonics 8, 1907 (2019).

[25] Freysoldt, C. et al. First-principles calculations for point defects in solids. Rev. Mod. Phys. 86, 253 (2014).

[26] Dreyer, C. E., Alkauskas, A., Lyons, J. L., Janotti, A., & Van de Walle, C. G. First-principles calculations of point defects for quantum technologies. Annu. Rev. Mater. Res. 48, 1 (2018).

[27] Ivády, V., Abrikosov, I. A., & Gali, A. First principles calculation of spin-related quantities for point defect qubit research. npj Comput. Mater.4, 76 (2018).
 

[28] Tsai, J.-Y., Pan, J., Lin, H., Bansil, A., & Yan, Q. Antisite defect qubits in monolayer transition metal dichalcogenides. Nat. Commun. 13, 492 (2022).

[29] Frey, N. C., Akinwande, D., Jariwala, D., & Shenoy, V. B. Machine learning-enabled design of point defects in 2D materials for quantum and neuromorphic information processing. ACS Nano 14, 13406 (2020).

[30] Ping, Y. & Smart, T. J. Computational design of quantum defects in two-dimensional materials. Nat. Comput. Sci. 1, 646 (2021).

[31] Narang, P., Ciccarino, C. J., Flick, J., & Englund, D. Quantum materials with atomic precision: artificial atoms in solids: ab initio design, control, and integration of single photon emitters in artificial quantum materials. Adv. Func. Mater. 29 1904557 (2019).

[32] Li, S., Thiering, G., Udvarhelyi, P., Ivády, V., & Gali, A. Carbon defect qubit in two-dimensional  \( WS_{2} \) . Nat. Commun. 13, 1 (2022).

[33] Gupta, S., Yang, J.-H., & Yakobson, B. I. Two-level quantum systems in two-dimensional materials for single photon emission. Nano Lett. 19, 408 (2019).

[34] Xiong, Y., Mathew, M., Griffin, S. M., Sipahigil, A., & Hautier, G. Midgap state requirements for optically active quantum defects. Preprint available at https://arxiv.org/abs/2302.10767 (2023).

[35] Freysoldt, C. et al. First-principles calculations for point defects in solids. Rev. Mod. Phys. 86, 253 (2014).

[36] Chen, W., Griffin, S. M., Rignanese, G.-M., & Hautier, G. Nonunique fraction of Fock exchange for defects in two-dimensional materials. Phys. Rev. B106, L161107 (2022).

[37] Xiong, Y. et al. High-throughput identification of spin-photon interfaces in silicon. Preprint available at https://arxiv.org/abs/2303.01594 (2023).

[38] Loh, L. et al. Impurity-induced emission in Re-doped  \( WS_{2} \)  monolayers. Nano Lett. 21, 5293 (2021).

[39] Qin, Z. et al. Growth of nb-doped monolayer  \( WS_{2} \)  by liquid-phase precursor mixing. ACS Nano 13, 10768 (2019).

[40] Zhang, F. et al. Monolayer vanadium-doped tungsten disulfide: A room-temperature dilute magnetic semiconductor. Adv. Sci. 7, 2001174 (2020).

[41] Han, A. et al. One-step synthesis of single-site vanadium substitution in 1T-WS \( _{2} \)  monolayers for enhanced hydrogen evolution catalysis. Nat. Commun. 12, 709 (2021).
 

[42] Pike, N. A. et al. Origin of the counterintuitive dynamic charge in the transition metal dichalcogenides. Phys. Rev. B 95, 201106 (2017).

[43] Rossi, A. et al.  \( WS_{2} \)  Band Gap Renormalization Induced by Tomonaga Luttinger Liquid Formation in Mirror Twin Boundaries. Preprint available at https://arxiv.org/abs/2301.02721 (2023).

[44] Kandel S. A. & Weiss, P. S. Binding and mobility of atomically resolved cobalt clusters on molybdenum disulfide. J. Phys. Chem. B 105, 8102 (2001).

[45] Tang, W. et al. Identically sized Co quantum dots on monolayer  \( WS_{2} \)  Featuring Ohmic Contact. Phys. Rev. Applied 13, 024003 (2020).

[46] Teichmann, K. et al. Controlled charge switching on a single donor with a scanning tunneling microscope. Phys. Rev. Lett. 101, 076103 (2008).

[47] Noack, M. M. et al. gpCAM. https://github.com/lbl-camera/gpCAM (2022).

[48] Mathew, K. et al. Atomate: A high-level interface to generate, execute, and analyze computational materials science workflows. Comput. Mater. Sci. 139, 140 (2017).

[49] Ong, S. P. et al. Python materials genomics (pymatgen): A robust, open-source python library for materials analysis," Comput. Mater. Sci. 68, 314 (2013).

[50] Jain, A. et al. Commentary: The Materials Project: A materials genome approach to accelerating materials innovation. APL Mater. 1, 11002 (2013).

[51] Kresse, G. & Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. Comput. Mater. Sci. 6, 15 (1996).

[52] Kresse G. & Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 54, 11169 (1996).

[53] Blöchl, P. E. Projector augmented-wave method. Phys. Rev. B 50, 17953 (1994).

[54] Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 77, 3865 (1996).

[55] Komsa, H.-P. & Pasquarello, A. Finite-size supercell correction for charged defects at surfaces and interfaces. Phys. Rev. Lett. 110, 095505 (2013).

[56] Komsa, H.-P., Berseneva, N., Krasheninnikov, A. V., & Nieminen, R. M. Charged point defects in the flatland: Accurate formation energy calculations in two-dimensional materials. Phys. Rev. X 4, 031044 (2014).
 

[57] Farzalipour Tabriz, M., Aradi, B., Frauenheim, T., & Deák, P. SLABCC: Total energy correction code for charged periodic slab models. Comput. Phys. Commun. 240, 101 (2019).

[58] Barker, B. A. & Strubbe, D. A. Spin-flip Bethe-Salpeter equation approach for ground and excited states of open-shell molecules and defects in solids. Preprint available at http://arxiv.org/abs/2207.04549. (2022).

[59] Wegner, F. Inverse participation ratio in  \( 2+\varepsilon \)  dimensions. Zeitschrift für Phys. B Condens. Matter 36, 209 (1980).

[60] Pashartis C. & Rubel, O. Localization of electronic states in III-V semiconductor alloys: A comparative study. Phys. Rev. Applied 7, 064011 (2017).

[61] Konstantinou, K., Mocanu, F. C., Lee, T.-H., & Elliott, S. R. Revealing the intrinsic nature of the mid-gap defects in amorphous  \( Ge_{2}Sb_{2}Te_{5} \) . Nat. Commun. 10, 3065 (2019).

[62] Zheng, Q. Vasp band unfolding. https://github.com/QijingZheng/VaspBandUnfolding (2018).

[63] Chagas da Silva, M. et al. Self-consistent potential correction for charged periodic systems. Phys. Rev. Lett. 126, 076401 (2021).

[64] Leung, S. Stm 2d scan. https://https://github.com/ShuangLeung/STM_2DScan (2020).

[65] Tersoff, J. & Hamann, D. R. Theory of the scanning tunneling microscope. Phys. Rev. B 31, 805 (1985).
 

# Supplemental Material for
A substitutional quantum defect in WS \( _{2} \)  discovered by high-throughput computational screening and fabricated by site-selective STM manipulation

John C. Thomas \( ^{1,2,3*} \) , Wei Chen \( ^{4†} \) , Yihuang Xiong \( ^{3†} \) , Bradford A. Barker \( ^{5} \) , Junze Zhou \( ^{1} \) , Weiru Chen \( ^{3} \) , Antonio Rossi \( ^{1,2,6} \) , Nolan Kelly \( ^{5} \) , Zhuohang Yu \( ^{7,8} \) , Da Zhou \( ^{9} \) , Shalini Kumari \( ^{7,8} \) , Edward S. Barnard \( ^{1} \) , Joshua A. Robinson \( ^{7,8,9,10} \) , Mauricio Terrones \( ^{7,8,9,10} \) , Adam Schwartzberg \( ^{1} \) , D. Frank Ogletree \( ^{1} \)  , Eli Rotenberg \( ^{6} \) , Marcus M. Noack \( ^{11} \) , Sinéad Griffin \( ^{1,2} \) , Archana Raja \( ^{1,2,} \)  David A. Strubbe \( ^{5} \) , Gian-Marco Rignanese \( ^{4} \) , Alexander Weber-Bargioni \( ^{1,2*} \) , and Geoffroy Hautier \( ^{3*} \) 

 \( ^{1} \) Molecular Foundry, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, United States of America

 \( ^{2} \) Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, CA, United States of America

 \( ^{3} \) Thayer School of Engineering, Dartmouth College, Hanover, NH 03755, USA

 \( ^{4} \) Institute of Condensed Matter and Nanoscience, Université catholique de Louvain, Louvain-la-Neuve 1348, Belgium

 \( ^{5} \) Department of Physics, University of California, Merced, Merced, CA 95343, USA  
 \( ^{6} \) Advanced Light Source, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, United States of America

 \( ^{7} \) Department of Materials Science and Engineering, The Pennsylvania State University, University Park, PA 16082 United States of America

 \( ^{8} \) Center for Two-Dimensional and Layered Materials, The Pennsylvania State University, University Park, PA, 16802 United States of America

 \( ^{9} \) Department of Physics, The Pennsylvania State University, University Park, PA, 16802 United States of America

 \( ^{10} \) Department of Chemistry, The Pennsylvania State University, University Park, PA, 16802 United States of America

 \( ^{11} \) Applied Mathematics and Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, United States of America
 \( ^{*} \) jthomas@lbl.gov, afweber-bargioni@lbl.gov, geoffroy.hautier@dartmouth.edu
 \( ^{\dagger} \) These authors contributed equally.

## SUPPLEMENTARY NOTES

## 1 Autonomous Experimentation

A Gaussian process (GP) model can be defined for a given dataset,  \( D = \{x_{i}, y_{i}\} \) , which takes into account  \( y(x) = f(x) + \varepsilon(x) \) , where x are the positions in some input or parameter space, y is the associated noisy function evaluation, and  \( \varepsilon(x) \)  represents the noise term. The variance-covariance matrix  \( \Sigma \)  of the prior Gaussian probability distribution is defined by Matérn kernel functions  \( k(x_{i}, x_{j}; \phi) \) , where  \( \phi \)  is the
 

set of hyperparameters found by maximizing the marginal log-likelihood of the data \( ^{1} \) . A predictive mean and variance can then be defined given a Gaussian probability distribution with a set of optimized hyperparameters, which can be further used to find the next optimal point measurements in the GP-driven data acquisition loop. For the results presented, an acquisition function that collects points to reduce uncertainty and improve the statistical model (exploration mode) was used. Drift was corrected during the autonomous experiment, where x-y offsets were calculated after each spectral loop and applied to the dataset.

## 2|1D Convolutional Neural Network

Spectra for  \( WS_{2} \)  and  \( V_{S} \)  were taken from Thomas et al. and used during training \( ^{1} \) . The one-dimensional convolutional neural network (CNN) chosen makes use of two convolution layers, one dropout layer, and one fully connected linear layer. We use an 80/20 train/validation split ratio on 394 individually and separately acquired scanning tunneling spectra, consisting of 45  \( Co_{S} \) , 158  \( V_{S} \) , and 191  \( WS_{2} \)  spectra. Validation data is further split (60/40 ratio) for a portion to be used during training, which yields an estimate of the model's skill, and a test set used on unbiased data after training. The softmax of the trained model is then used after training to obtain point STS class probabilities. All convolutional layers make use of a  \( 1 \times 3 \)  kernel to compute the sliding dot product and produce spectral feature maps at each layer (stride 1, padding 1). This is followed by batch normalization, a rectified linear unit activation, and a maxpooling layer. The Adam algorithm \( ^{2} \)  with a learning rate of  \( 10^{-4} \)  and computed cross-entropy loss for optimization are used during training to automatically identify spectral features. Spectra for  \( WS_{2} \) ,  \( V_{S} \) , and  \( Co_{S} \)  that are unseen by the trained model are used for test data. The CNN architecture chosen uses shared weights to reduce the number of trainable parameters and extract spectral features on the pixel level.
 

Defect Database:

<table><tr><td>Defect</td><td>Total spin</td><td>\( \Delta \) KS (eV)</td><td>TDM (Debye)</td></tr><tr><td>\( Br_{W}^{0} \)</td><td>1/2</td><td>0.854</td><td>5.79</td></tr><tr><td>\( Sc_{S}^{0} \)</td><td>1/2</td><td>0.8</td><td>3.01</td></tr><tr><td>\( Sb_{W} \)</td><td>0</td><td>1.037</td><td>6.33</td></tr><tr><td>\( Rb_{W} \)</td><td>1</td><td>0.825</td><td>10.01</td></tr><tr><td>\( Te_{W} \)</td><td>1/2</td><td>0.778</td><td>8.03</td></tr><tr><td>\( S_{W}^{0} \)</td><td>0</td><td>0.939</td><td>10.77</td></tr><tr><td>\( P_{W}^{-} \)</td><td>0</td><td>1.134</td><td>6.13</td></tr><tr><td>\( Ir_{W}^{+} \)</td><td>0</td><td>0.84</td><td>5.17</td></tr><tr><td>\( As_{W}^{-} \)</td><td>0</td><td>0.941</td><td>7.74</td></tr><tr><td>\( Pb_{W}^{-2} \)</td><td>0</td><td>1.035</td><td>6.95</td></tr><tr><td>\( C_{W}^{-2} \)</td><td>0</td><td>1.093</td><td>8.29</td></tr><tr><td>\( K_{W}^{-} \)</td><td>1</td><td>0.877</td><td>9.67</td></tr><tr><td>\( Ca_{W}^{0} \)</td><td>1</td><td>0.755</td><td>10.42</td></tr><tr><td>\( Ca_{W}^{-2} \)</td><td>0</td><td>0.794</td><td>9.89</td></tr><tr><td>\( Mg_{S}^{+} \)</td><td>1/2</td><td>0.786</td><td>4.23</td></tr><tr><td>\( N_{W}^{-} \)</td><td>0</td><td>1.08</td><td>9.56</td></tr><tr><td>\( Ru_{W}^{0} \)</td><td>0</td><td>0.937</td><td>3.97</td></tr><tr><td>\( Ru_{W}^{+} \)</td><td>1/2</td><td>0.824</td><td>3.06</td></tr><tr><td>\( Co_{S}^{0} \)</td><td>1/2</td><td>1.29</td><td>6.41</td></tr><tr><td>\( Bi_{W}^{-} \)</td><td>0</td><td>0.838</td><td>8.8</td></tr><tr><td>\( W_{S}^{+} \)</td><td>1/2</td><td>0.968</td><td>3.9</td></tr><tr><td>\( Vac_{W}^{-2} \)</td><td>1</td><td>0.76</td><td>7.97</td></tr><tr><td>\( Rh_{W}^{-} \)</td><td>0</td><td>0.788</td><td>7.45</td></tr><tr><td>\( Os_{W}^{0} \)</td><td>0</td><td>1.04</td><td>3.42</td></tr><tr><td>\( Fe_{S}^{0} \)</td><td>1</td><td>1.184</td><td>4.93</td></tr><tr><td>\( Sr_{W}^{0} \)</td><td>1</td><td>0.754</td><td>11.04</td></tr><tr><td>\( Sr_{W}^{-2} \)</td><td>0</td><td>0.78</td><td>10.68</td></tr><tr><td>\( Na_{W}^{-} \)</td><td>1</td><td>0.802</td><td>9.02</td></tr><tr><td>\( Zn_{S}^{0} \)</td><td>1</td><td>1.11</td><td>3.6</td></tr><tr><td>\( Ge_{S}^{-} \)</td><td>1/2</td><td>0.838</td><td>7.02</td></tr><tr><td>\( Ti_{S}^{0} \)</td><td>0</td><td>1.843</td><td>4.33</td></tr><tr><td>\( Li_{S}^{0} \)</td><td>1/2</td><td>0.764</td><td>3.8</td></tr></table>

Supplementary Table 1: All the thermodynamically stable two-level defect candidates that show transition dipole moment (TDM) larger than 2.5 D and Kohn-Sham energy difference ( \( \Delta \) KS) larger than 750 meV are summarized in the table below. The  \( \Delta \) KS is computed at single-shot PBE0 level using an  \( \alpha \)  of 0.07, as detailed in the main text.

Effect of spin-orbit coupling (SOC) on  \( Co_{S} \)  defect levels:

<table><tr><td></td><td>occupation</td><td>no SOC</td><td>SOC</td></tr><tr><td>\( d_{x^{2}-y^{2}} \)</td><td>0</td><td>-4.06</td><td>-4.08</td></tr><tr><td>\( d_{z^{2}} \)</td><td>1</td><td>-5.42</td><td>-5.40</td></tr><tr><td>\( d_{xy} + d_{xz} \)</td><td>1</td><td>-5.56</td><td>-5.53</td></tr></table>

Supplementary Table 2: Eigenvalues (in eV) of defect levels associated with the Co-3d states for the neutral  \( Co_{S}^{0} \)  defect calculated within collinear (no SOC) and noncollinear spin-polarizations (with SOC). All energies are referred to the vacuum level.
 
![](./images/917724983780704774_12.jpg)

Supplementary Fig. 1: In this work, we considered 57 elements for constructing a quantum defect database in  \( WS_{2} \) . Our selection covers the majority of the elements, excluding the rare-earth elements and noble gases. The elements that were not considered are colored in grey.
 
![](./images/917724983780704774_13.jpg)

 
![](./images/917724983780704774_14.jpg)

Supplementary Fig. 2: The single-shot PBE0 single-particle defect level diagrams of the screened candidates that have  \( \Delta KS > 750 \)  meV and TDM larger than 2.5 D. The two levels that are involved in the transition are highlighted using the arrows, and the localization IPR represented by the color bar. These candidates are grouped into: a  \( M_{W} \)  defects with singlet ground states, b  \( M_{W} \)  defects with nonsinglet ground states, c  \( M_{S} \)  defects with singlet ground states, and d  \( M_{S} \)  defects with nonsinglet ground states.
 
![](./images/917724983780704774_15.jpg)

Supplementary Fig. 3: Single-shot PBE0 defect level diagrams of a  \( V_{W}^{-} \) , b  \( Cr_{W}^{0} \) , c  \( Mo_{W}^{0} \( , and d  \) Re_{W}^{+} \(  in monolayer WS}_{2} $ .
 
![](./images/917724983780704774_16.jpg)

Supplementary Fig. 4: Partial density of states and crystal orbital Hamilton population (COHP) analysis of 3d transition metal defects in WS \( _{2} \) . Projected density of states of the transition metals for a substitution on S and b substitution on W. The shown density of states are computed at single-shot PBE0 level. The COHP of 3d defects substitution on a S and b W are evaluated using PBE wave functions. The Fermi level is shown with a dashed horizontal line and band edges are shown with solid horizontal lines.
 
![](./images/917724983780704774_17.jpg)

Supplementary Fig. 5:  \( Co_{S} \)  defect energy levels. Localized defect states are shown in the +1, 0, and -1 charge states. Resonant states within the valence band and conduction band manifolds are not depicted. The associated single-particle levels are indicated by the horizontal bars (closed for occupied and open for unoccupied states). The dashed lines connect the active orbitals responsible for charging/discharging between two charge states. The band-edge positions indicated in the plot refer to the ones for the pristine  \( WS_{2} \) , which are obtained from PBE0 calculations by admixing 22% of Fock exchange. SOC is only applied to the band edges.
 
![](./images/917724983780704774_18.jpg)

Supplementary Fig. 6: Phonon Excitation Comparison. The first and second peaks  \( (\hbar\omega_{eg}) \)  within acquired dI/dV are fitted according to the single-mode Franck-Condon model at both 0.36 eV and 0.47 eV. This can be fit as  \( \frac{dI}{dV}(V)=A\sum_{n=0}^{\infty}e^{-S}\frac{1}{n!}S^{n}\delta(e^{V}-\hbar\omega_{eg}-n\hbar\omega_{0}) \) , where A is an arbitrary scaling factor, S is the Huang-Rhys factor,  \( \hbar\omega_{eg} \)  is the electronic excitation energy or zero-phonon line, and  \( \hbar\omega_{0} \)  is the excited phonon mode. We use a Gaussian function with a full width at half maximum ( \( \Gamma \) ) to replace the  \( \delta \)  function and account for broadening. Phonon modes were taken from literature values \( ^{3,4} \) . A Huang-Rhys factor of S=1.3, a first excitation of  \( \hbar\omega_{eg}=0.341 \)  eV, a phonon mode of  \( \hbar\omega_{0}=0.018 \)  eV, and a broadening of  \( \Gamma=0.021 \)  eV is estimated for the lower energy defect state, and S=1.2, a first excitation of  \( \hbar\omega_{eg}=0.447 \)  eV,  \( \hbar\omega_0=0.018 \)  eV, and  \( \Gamma=0.021 \)  eV is estimated for the next available unoccupied state with higher energy.
 
![](./images/917724983780704774_19.jpg)



![](./images/917724983780704774_20.jpg)



![](./images/917724983780704774_21.jpg)



![](./images/917724983780704774_22.jpg)

 
![](./images/917724983780704774_23.jpg)

![](./images/917724983780704774_24.jpg)

Supplementary Fig. 7: Element-resolved density of states (DOS) of  \( Co_{S} \)  in  \( WS_{2} \) . We considered a +1, b neutral, and c -1 charge states. The Scanning Tunneling Spectroscopy results are simulated using PBE0 charge density and energy levels. Wavefunctions of atomic orbitals of Co that contribute most to each Co-related in-gap state are shown below the DOS.
 
![](./images/917724983780704774_25.jpg)

![](./images/917724983780704774_26.jpg)

Supplementary Fig. 8: Hyperspectral Data Collection. a  \( \cos \)  is identifiable by point bias spectroscopy followed by classification using a trained 1D-CNN, where image tracking can be performed on the defect of interest during an autonomous STS experiment. Outside spectra (either pristine  \( WS_{2} \)  or  \( V_{S} \) ) are bucketed under a different classification (shown in blue). Acquired point STS locations are overlaid on acquired topography ( \( I_{tunnel} = 30 \)  pA,  \( V_{sample} = 1.2 \)  V). Scale bar, 0.5 nm. b Accumulated spectra over  \( \cos \)  are shown with the mean spectrum that is colored by classification, where a charging peak is measured at  \( -0.84 \pm 0.06 \)  eV.

![](./images/917724983780704774_27.jpg)

![](./images/917724983780704774_28.jpg)

Supplementary Fig. 9: Drift Correction. Computed offsets during a  \( Co_{S} \)  autonomous experiment is shown in two dimensions and b the magnitude of the 2D vector as a function of time. Drift is multidirectional, but primarily near  \( 70^{\circ} \) . In order to correct for drift at each point, a drift rate was calculated between acquired images ( \( \mathring{A}/s \) ) at every interval, and subsequently applied to each timestamped spectra.
 
![](./images/917724983780704774_29.jpg)

Supplementary Fig. 10: Autonomous Experimentation. A live experimental run within a range of 0.25 V to 0.65 V, which is chosen to highlight in-gap states for  \( Co_{S} \)  below the conduction band and above  \( E_{F} \) . Both the mean model function and variance function are shown at a given interval (N) as the experiment progresses in exploration mode.

![](./images/917724983780704774_30.jpg)

Supplementary Fig. 11: 1D Convolutional Neural Network Performance. a) Accuracy and loss after 20 training epochs is shown on both training and validation datasets. b) Confusion matrices taken after classification on test data using the argmax value across class probabilities (yielded by the softmax). Training can be concluded after 2 epochs, where test data shows zero off-diagonal elements, loss is minimized, and accuracy is optimized.
 
![](./images/917724983780704774_31.jpg)

![](./images/917724983780704774_32.jpg)

![](./images/917724983780704774_33.jpg)

Supplementary Fig. 12:  \( Co_{S} \)  Charging Region. a High resolution scanning tunneling differential conductance maps at -0.90 eV, -0.95 eV, -1.00 eV, -1.05 eV, and -1.10 eV ( \( V_{modulation} = 5 \)  meV). Solving for the local maxima at the center of  \( Co_{S} \)  and taking a same-size line scan from the center position to outside the charging region highlights the energetic shift as the bias is ramped to more negative values (shown spatially). Outside the ring,  \( WS_{2} \)  remains neutral and, inside the ring,  \( Co_{S} \)  is negatively charged at a given bias. b This is shown further as a compilation of linescans and a c compiled image as a function of distance and centered along the charging ring.
 
![](./images/917724983780704774_34.jpg)

![](./images/917724983780704774_35.jpg)

Supplementary Fig. 13: Thermodynamic charge transition levels of S vacancy in WS \( _{2} \) . The defect formation energies are evaluated under W-rich conditions ( \( \mu_{S} = -6.25 \)  eV,  \( \mu_{W} = -13.83 \)  eV) and W-poor conditions ( \( \mu_{S} = -4.94 \)  eV,  \( \mu_{W} = 16.45 \)  eV). The 0/-1 charge transition level is at 2.14 eV with respect to VBM. The vertical dotted lines indicate the band edges.
 
![](./images/917724983780704774_36.jpg)

Supplementary Fig. 14: Differential Conductance Mapping. dI/dV images ( \( V_{modulation} = 5 \, meV \) ) over the point STS ( \( V_{modulation} = 5 \, meV \) ) region shown for a  \( Co_{S} \)  defect using a jet color scale, where the energy is ramped from near the VBM of  \( WS_{2} \)  to -0.7 eV, from unoccupied peaks of interest, and then to below the CBM of  \( WS_{2} \) . Orbitals of the as-formed  \( Co_{S} \)  and surrounding  \( V_{S} \)  are visualized as a function of bias voltage. Charging effects are only present in negative sample bias regimes.

## REFERENCES

[1] Thomas, J. C. et al. Autonomous scanning probe microscopy investigations over WS \( _{2} \)  and Au{111}. npj Comput. Mater. 8, 99 (2022).

[2] Kingma, D. P. & Ba, J. Adam: A method for stochastic optimization. Preprint available at https://arxiv.org/abs/1412.6980 (2014).

[3] Molina-Sánchez, A. & Wirtz, L. Phonons in single-layer and few-layer  \( MoS_{2} \)  and  \( WS_{2} \) . Phys. Rev. B 84, 155413 (2011).

[4] Molas, M. R., Nogajewski, K., Potemski, M., & Babinski, A. Raman scattering excitation spectroscopy of monolayer  \( WS_{2} \) . Sci. Rep. 7, 5036 (2017).
 
