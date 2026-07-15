# Non-relativistic spin splitting above and below the Fermi level in a g-wave altermagnet

Nicholas Dale \( ^{*1,2,\dagger} \) , Omar A. Ashour \( ^{*1,2,3} \) , Marc Vila \( ^{1,2} \) , Resham B. Regmi \( ^{5,6} \) , Justin Fox \( ^{1,2,4} \) , Cameron W. Johnson \( ^{2} \) , Alexei Fedorov \( ^{7} \) , Alexander Stibor \( ^{2} \) , Nirmal J. Ghimire \( ^{5,6} \) , and Sinéad M. Griffin \( ^{1,2,\S} \) 

 \( ^{1} \) Materials Sciences Division, Lawrence Berkeley National Lab, 1 Cyclotron Road, Berkeley, CA 94720, USA  
 \( ^{2} \) Molecular Foundry, Lawrence Berkeley National Lab, 1 Cyclotron Road, Berkeley, CA 94720, USA  
 \( ^{3} \) Department of Physics, University of California, Berkeley, CA 94720, USA  
 \( ^{4} \) Department of Physics, Carnegie Mellon University, Pittsburgh, PA 15213, USA  
 \( ^{5} \) Department of Physics and Astronomy, University of Notre Dame, Notre Dame, IN 46556, USA  
 \( ^{6} \) Stravopoulos Center for Complex Quantum Matter, University of Notre Dame, Notre Dame, IN 46556, USA  
 \( ^{7} \) Advanced Light Source, Lawrence Berkeley National Lab, 1 Cyclotron Road, Berkeley, CA 94720, USA  
 \( ^{*} \) Authors contributed equally to this work.

 \( ^{*} \) e-mail: ndale@lbl.gov  
 \( ^{\S} \) email: sgriffin@lbl.gov

## ABSTRACT

Alternagnets are distinguished by their unique spin group symmetries, where spin and spatial symmetries are fully decoupled, resulting in nonrelativistic spin splitting (NRSS) of electronic bands. This phenomenon, unlike conventional spin splitting driven by relativistic spin-orbit coupling, has transformative potential in fields such as spintronics, superconductivity, and energy-efficient electronics. However, direct observation of NRSS is challenging due to presence of competing phases, low Néel temperatures, and the limitations of existing experimental probes to unambiguously capture the associated properties. Here, we integrate theoretical and experimental approaches to uncover NRSS in the intercalated transition metal dichalcogenide  \( CoNb_{4}Se_{8} \) . Symmetry analysis, density functional theory (DFT), a novel Symmetry-Constrained Adaptive Basis (SCAB), and tight-binding modeling predict the presence of symmetry-enforced spin splitting, which we directly confirm using spin-resolved photoemission spectroscopy (spin-ARPES) for the occupied band structure and a newly developed technique, spin- and angle-resolved electron reflection spectroscopy (spin-ARRES), for the unoccupied states. Together, these complementary tools reveal alternating spin textures consistent with our predicted g-wave altermagnetic order and demonstrate the persistence of NRSS across a broad energy range. Crucially, temperature-dependent measurements show the suppression of NRSS at the Néel temperature, providing the first direct evidence of an altermagnetic phase transition. Residual spin splitting above the ordering temperature suggests the coexistence of altermagnetic fluctuations and spin-orbit coupling effects, underscoring a complex interplay of mechanisms. By establishing  \( CoNb_{4}Se_{8} \)  as a prototypical g-wave altermagnet, this work offers a robust framework for understanding NRSS, and characterizing NRSS, and lays the foundation for designing energy-efficient spin-based technologies.

## Introduction

The resurgence of interest in spin-split antiferromagnets (AFMs) \( ^{1-6} \) , first suggested in the 1960s \( ^{7} \) , have driven a renewed effort to understand their unique magnetic and electronic and magnetic order. Recent advances have provided a clearer framework for these materials, including order parameter descriptions \( ^{5,8,9} \)  and group-theoretical classifications \( ^{10} \) . Unlike conventional AFMs, which exhibit doubly-degenerate electronic bands across the entire Brillouin zone (BZ), these so-called 'altermagnets' \( ^{11} \)  feature momentum-dependent spin splitting arising from intrinsic symmetries rather than relativistic effects. This non-relativistic spin splitting (NRSS) arises from the rich symmetries of spin groups \( ^{11-16} \) , which completely decouple spin and real space in the absence of spin-orbit coupling. In NRSS materials, the charge densities of the two oppositely-polarized spin sublattices map onto each other through space group operations that are neither a translation nor an inversion, such as glide and screw operations. Within the BZ, the band structure is only spin degenerate at a set of nodal surfaces, and spin-split elsewhere. The number of the nodal surfaces leads to specific magnetic states such as the experimentally realized d-wave (2 nodal surfaces) \( ^{17-19} \)  and g-wave (4 nodal surfaces) \( ^{20-25} \)  phases. The understanding and observation of NRSS unlocks functional properties of both fundamental and technological interest ranging from unconventional superconductivity \( ^{26-28} \)  and novel topological effects \( ^{29,30} \)  to energy-efficient microelectronics \( ^{31-37} \) .

However, experimentally observing NRSS in materials remains a formidable challenge due to its subtle and often indirect
 
n nature. While theory predicts a rich variety of spin-split states stemming from symmetry-enforced mechanisms, translating these predictions into direct experimental observations is non-trivial and faces several key obstacles.
First and foremost, the fabrication of high-quality samples poses a significant barrier. Many candidate materials suffer from domain formation \( ^{38,39} \) , competing ground states \( ^{40} \), mosaicity in thin films 41 \), or during transport between growth and measurement chambers 23 \. These issues obscure intrinsic electronic of NRSS making difficult disentangle material's properties from extrinsic For instance Spin- and Angle-Resolved Photoemission Spectroscopy (spin-ARPES), ostensibly the most direct tool for observing provides access spin-split constant energy surfaces across However requires homogeneity over beam spot sizes 50 \mu m high-quality stoichiometric samples 20,23 . Moreover while spin-ARPES can confirm splitting distinguishing NRSS conventional spin-orbit coupling effects often corroboration theoretical models example spin-split band features measured in MnTe^{20-22} RuO_{2}^{17,18} were validated symmetry analysis tight-binding and/or density functional theory (DFT) calculations to competing mechanisms like spin-orbit coupling or ferromagnetism 38 .In addition challenges with sample quality inherent limitations of many experimental techniques yield only indirect complicating efforts unambiguously attribute observed true origins Transport optical such anomalous Hall effect (AHE) 42,43 circular dichroism sensitive but require coexisting ferromagnetism applied magnetic fields detection AHE example typically arises nonzero magnetization 44 conflicting strictly nature NRSS Similarly probes off-diagonal conductivity tensor components that result other time-reversal symmetric mechanisms 45 making their interpretation definitive Furthermore transport signatures depend splitting Fermi level many metals exhibit strongest signatures higher energies 6 limiting utility Low temperatures several candidate present obstacle 11 since state-of-the-art combining spin-sensitivity spectromicroscopy can be challenging temperatures 46,47 restricts conditions which verified complicates efforts link phenomena theoretical predictions.In this work we address challenges by employing a multifaceted approach directly predict observe understand candidate intercalated transition dichalcogenide (TMD). Through analysis density functional theory an intuitive tight-binding model demonstrate how coupling crystal field Zeeman splits give conditions observing system throughout structure use predictions characterization where spin-ARPES new technique and angle-resolved reflection spectroscopy (spin-ARRES) 48,49 probe across broad range occupied (ARPES) unoccupied (ARRES) electronic first time Importantly connect our observed symmetry-enforced model measuring temperature we additionally present direct altermagnetic phase transition material.

## Results

## Crystal Structure and Magnetic Order

 \( CoNb_{4}Se_{8} \)  crystallizes in the hexagonal space group  \( P6_{3}/mmc \)  (No. 194), with two formula units per unit cell, as shown in Fig. 1A, 1B. In this 1/4-intercalated TMD, Co ions are positioned between two 2H-NbSe \( _{2} \)  monolayers in octahedral sites, resulting in a centrosymmetric system with collinear AFM order. Unlike the non-centrosymmetric 1/3-intercalated TMD  \( CoNb_{3}Se_{6} \) , which exhibits significant Dzyaloshinskii-Moriya interaction with spins canting away from the c-axis \( ^{50,51} \) ,  \( CoNb_{4}Se_{8} \)  maintains robust collinear AFM order \( ^{52} \) . While several factors influence the intercalant ordering for such intercalated TMDs \( ^{53} \) , well-ordered crystals for the 1/4-intercalated  \( CoNb_{4}Se_{8} \)  compound have recently been synthesized \( ^{52} \) , which we study here.

DFT calculations confirm that the AFM ground state of  \( CoNb_{4}Se_{8} \)  is energetically favored, lying 60 meV per formula unit lower than the FM state, in agreement with Ref. \( ^{[52]} \) . The calculated spin-polarized charge density (Fig. 1) reveals that the alternating crystal field in this intercalated TMD breaks the charge density symmetry at each Co site differently. This staggered field arises from a  \( 60^{\circ} \)  rotation (or mirror symmetry) in the orientation of chalcogen atoms surrounding Co ions at c=0 (sublattice I) and c=1/2 (sublattice II), resulting in a  \( 60^{\circ} \)  rotation (or mirror) between the magnetization densities in the spin-up and spin-down sublattices.

## Symmetry and Electronic Structure

The two magnetic sublattices in  \( CoNb_{4}Se_{8} \)  are connected by 12 symmetry operations—here we highlight those that are most intuitive for understanding the origins of the NRSS in this system, namely a  \( 6_{3} \)  screw along the crystallographic c-axis and a glide mirror through the ab-plane. With the z-axis parallel to the crystal's c-axis, the sublattices are thus related by a 6-fold rotation  \( C_{6z} \)  combined with a  \( \frac{1}{2}c \)  translation, or alternatively, by the mirror  \( M_{z} \)  across the c=1/4 plane (see Fig. 1A, 1B). The
 

![](./images/1070588194879176733_1.jpg)

Figure 1. Real-space magnetic structure of  \( CoNb_{4}Se_{8} \) . (A) Magnetic structure of  \( CoNb_{4}Se_{8} \)  along the b-axis, and (B) along the c-axis at c=0 (sublattice I) and c=1/2 (sublattice II). The DFT-calculated pink and blue defined as spin up and down, respectively, indicating  \( C_{6z} \)  rotation relating the two only the bottom Se atoms for (C) Schematics of the DFT-calculated spin-dependent crystal field splitting in  \( CoNb_{4}Se_{8} \)  in the trigonal basis, where filling of the arrows denotes orbital occupation, and color indicates the orbital phase  \( \varphi \) . For clarity, only one of the  \( \left|e_{g}^{\prime\pm}\right\rangle \)  and  \( \left|e_{g}^{\pm}\right\rangle \)  orbitals are shown,  \( \left|e_{g}^{\prime-}\right\pm}\right\rangle \)  and  \( \left|e_{g}^{\pm}\right\rangle \)  being their complex conjugates, and the  \( \left|a_{1g}\right\rangle \) ( \( d_{z^{2}} \)  ) orbital omitted.

DFT-calculated spin-polarized electronic band structure (Fig. 2B, 2C) finds spin splitting in  \( CoNb_{4}Se_{8} \) , which we explain below symmetry analysis and a tight-binding model below.

The calculated local magnetic moment of  \( 1.49\mu_{B} \)  per Co ion is consistent with a nominal  \( Co-d^{8} \)  configuration (S=1,  \( m=2\mu_{B} \) ) for an itinerant system, confirming a recent report \( ^{2} ) . In  CoNb_{4}Se_{8} , the Co-Se octahedral complex undergoes a trigonal distortion, likely resulting from the onset of a charge density wave (CDW) in the host system, reducing the octahedral symmetry  O_{h}  to trigonal  D_{3d} . This distortion breaks all  C_{4}  axes of the octahedral site, leaving a single  C_{3}  axis aligned with the crystal's c-axis. In the  D_{3d}  crystal field, the Co d-orbitals split into three manifolds: two doubly-degenerate levels with  E_{g}  symmetry and a non-degenerate  A_{1g}  level (the  d_{z}^{2}  orbital). Our DFT-projected density of states (PDOS) confirms this arrangement for each sublattice (see Supplementary Material (SM)).

Conventional crystal-field analysis, which relies on atomic d orbitals or their real-coefficient linear combinations, has limitations in fully describing this system. It typically uses a different local basis for each sublattice, preventing it from capturing the full global symmetry relationships critical to understanding the NRSS. More specifically, while atomic d orbitals are eigenstates of  C_{2} , they lack the required  C_{3}  or  C_{6}  symmetry to describe both sublattices simultaneously. To address these limitations, we developed a Symmetry-Constrained Adaptive Basis (SCAB), which combines  C_{3z}  eigenstates with complex coefficients selected to account for both local and global symmetries in  CoNb_{4}Se_{8} .

## Symmetry-Constrained Adaptive Basis (SCAB) and Tight-Binding Model

The SCAB provides a unified framework for symmetry-driven analysis by systematically capturing the symmetry relationships linking the different sublattices. Here, this basis combines  C_{6z} eigenstates with carefully chosen complex coefficients tailored to maintain the crystal's  C_{C} symmetries. The resulting SCAB orbitals, shown in Fig. 1C, exhibit three lobes with phase values of  0  and  \pm2\pi/3 , preserving the  C_{3z}  symmetry axis of each sublattice. In sublattice I, the SCAB-derived  \left|e_{g}^{\pm}\right\rangle . In sublattice I are lower energy than the  left|e_{g}^{\prime\pm}\right\rangle  orbitals, a trend that is reversed in sublattice II due to the  C_{6}  symmetry operation, and is consistent with our DFT-calculated magnetization density. Mulliken population analysis indicates that in sublattice I, the lower-energy  \left|e_{g}^{\pm}\right\rangle  orbitals are nearly fully occupied, while hybridization among the remaining orbitals ( \left|e_{g}^{\prime\pm}\right\rangle  and  \lefta_{1g}\right\rangle ) prevents a distinct separation of crystal field splitting.

Our goal with the SCAB is to clarify the specific chemical and structural factors in real space that govern spin splitting in reciprocal space. Building on recent insights into orbital symmetry and chemical bonding 54 , our approach shows that the bonding strengths between the magnetic ion and surrounding ligands must alternate to reverse orbital energy order under
 

A

![](./images/1070588194879176733_2.jpg)

B

![](./images/1070588194879176733_3.jpg)

C

![](./images/1070588194879176733_4.jpg)

D

![](./images/1070588194879176733_5.jpg)

E

![](./images/1070588194879176733_6.jpg)

F

![](./images/1070588194879176733_7.jpg)

Figure 2. Predicted momentum-space electronic structure of  \( CoNb_{4}Se_{8} \) . (A) Hopping schematic between  \( \left|e_{g}^{\pm}\right\rangle \)  and Se atoms in sublattice I and II. (B) Corresponding reciprocal space constant energy surface 180 meV above the Fermi level, calculated with DFT. This energy cut is chosen for clarity – the Fermi surface at  \( E_{F}=0 \)  eV is shown in Fig. S2. (C) Spin-resolved DFT band structure along  \( M^{\prime\prime}-\Gamma^{\prime}-M^{\prime} . The  \Gamma^{\prime\prime} ( M^{\prime} ) point lies between  \Gamma  and A (M and L), and  C_{6z}^{3}M^{\prime}=M^{\prime\prime} . (D-F) Band structure of the tight-binding model for g-wave alternagnets, comparing orbital (D), sublattice (E), and spin (F) polarization, where pink and blue denote spin-up and spin-down bands, respectively.

sublattice transposing operations (e.g.,  C_{6z}  or  M_{z} ). More concretely,  \left|e_{g}^{\pm}\right\rangle  and  \left|e_{g}^{\prime\pm}\right\rangle  orbitals should exhibit different bonding strengths along a specified direction, with these strengths switching upon applying a sublattice transposing operation an odd number of times. This highlights the critical role of ligand orbitals in the NRSS in  CoNb_{4}Se_{8} .

In sublattice I (Fig. 2A), the three top lobes of  \left|e_{g}^{\prime\pm}\right\rangle  orbital align Se above Co (see  t_{1}  hopping in Fig. 2A), and similarly for its bottom lobes (rotated  60^{\circ}  relative to the top lobes), strong repulsion and forming an antibonding molecular orbital. In contrast, in sublattice II the bonding between  \left|e_{g}^{\prime\pm}\right\rangle  and the top Se orbitals is now  C_{6z} -rotated with respect to sublattice I (see  t_{2}  hopping in Fig. 2A). This results in the top Se ligand orbitals lying between the lobes of  \left|e_{g}^{\prime\pm}\right\rangle , resulting in less repulsion and forming a lower-energy bonding orbital (hence,  t_{1} \neq t_{2} ). The energetic ordering is reversed for the  \left|e_{g}^{\pm}\right\rangle  orbitals, as  \left|e_{g}^{\pm}\right\rangle = C_{6z}^{-1}\left|e_{g}^{\prime\pm}\right\rangle :  \left| \pm}\right\rangle  interacts through the  t_{2}  hopping in sublattice I while  t_{1}  mediates the interaction in sublattice II. This bonding picture is consistent with the energy-level ordering derived from our DFT-calculated PDOS (SM) and crystal field analysis from Fig. 1C.

We now employ the SCAB within a tight-binding model to disentangle the roles of orbital polarization, crystal field, and spin in generating the NRSS in  CoNb_{4}Se_{8}  (see SM for the full Hamiltonian):

 \[ \mathcal{H}=\mathcal{H}_{0}+\mathcal{H}_{C F}+\mathcal{H}_{A F M}, \] 

where  H_{0}  represents magnetic ion-ligand hoppings,  H_{CF}  captures crystal-field effects, and  H_{AFM}  introduces an effective AFM exchange. We examine the band structure along the  M^{\prime\prime}-\Gamma^{\prime}-M^{\prime}  path (Fig. 2D-F), which aligns with the real space Co-Se bond along the x-axis in Fig. 2A and therefore the hoppings along this direction can be understood through  t_{1}  and  t}_{2} . First, analyzing  H_{C}  with  H_{AFM}=0 , we observe orbital polarization in the bands which indicates that the orbitals bond with different strengths ( t_{1}  and  t_{2} ). This polarization switches when crossing the  \Gamma^{\prime}  point, confirming opposite orbital characters along the  \pm x  Co-Se bond directions. Because the crystal field couples the energy ordering of the  \left|e_{g}^{\pm}\right\rangle  and  \left|e_{g}^{\prime\pm}\right\rangle  orbitals with the sublattice degree of freedom, the bands also display sublattice polarization which follows the same trend as the orbital polarization. The sign reversal of the sublattice character at  \Gamma^{\prime}  is essential to the NRSS: including  H_{AFM} generates opposite spin splittings on the sublattices, thus producing spin-split bands as shown in Fig. 2F.
 

A

![](./images/1070588194879176733_8.jpg)

B

![](./images/1070588194879176733_9.jpg)

C

![](./images/1070588194879176733_10.jpg)

D

![])(./images/1070588194879176733_11.jpg)

![](./images/1070588194879176733_12.jpg)

F

![](./images/1070588194879176733_13.jpg)

Figure 3. ARPES measurement of spin-split occupied electronic structure in  \( CoNb_{4}Se_{8} \) . (A, B) 13 K ARPES spectra along electron pockets surrounding  \( M^{\prime\prime} \equiv C_{6e}^{3}M^{\prime} \)  (A) and  \( M^{\prime} \)  (°B). Pink (blue) parabolas are guides to eye for spin up (down) electronic states. (C) Calculated band structure along  \( M^{\prime\prime} - \Gamma^{\prime} - M^{\prime} \) , overlaid onto ARPES spectra along the same cut. DFT data has been stretched in energy by 50% and shifted by 0.02 eV. (D, E) Spin-resolved EDCs spectra along momenta indicated by black (white) vertical lines in A (B). Red (blue) ticks indicate peak locations for bands polarized spin up (down), extracted as a parabolic fit within the vicinity of spectral maximum. (F) Representative momentum-dependent spin splitting, extracted from the difference in spin up and spin down band locations in (C) and (D).

Our model and symmetry analysis, guided and supported by DFT results, establish a comprehensive theoretical framework for understanding NRSS in  CoNb_{4}Se_{8} . Using our DFT and theoretical results predicting those regions of the BZ with NRSS we now present clear evidence of NRSS in spin-resolved electronic structure above and below the Fermi level ( E_{F} ), which diminishes upon crossing the Néel ordering temperature.

## The Occupied Electronic Structure of CoNb_{4}Se_{8} via ARPES

The experimental ARPES spectra of  CoNb_{4}Se_{8}  presented in (Fig. 3) along the momentum direction  M^{\prime\prime}-\Gamma^{\prime}-M^{\prime}  capture many of the salient features of the tight-binding model. Notably, the raw data (Fig. 3A, B) reveal two electron pockets at the BZ edge with a depth of  \approx0.35  eV and a momentum splitting of  \approx 0.09\ \AA^{-1}  at  E_{F} . This spectral signature is distinct from that of pure 2H-NbSe _{2} , which has no electron pockets at the BZ edges and instead exhibits pockets around the zone corners 55 . Here, we have selected a nonzero  k_{z}  to highlight the spin splitting observed away from time-reversal invariant momenta 20 .

In real space, NRSS is described by a spin flip and a space group operation that connects the opposite-spin sublattices, namely a proper or improper rotation (including mirrors) combined with a translation. However, in momentum space, only p the rotation operations are relevant. The pair of electron pockets around the  M^{\prime}  points map onto each other by inverting parallel momentum – equivalent to three applications of the  C_{6}  rotation operator – and inverting spin through  C_{2} . This phenomenon is reflected in the DFT results (Fig. 3C), which also shows two spin-split electron pockets at the zone edge, with opposite spin splitting at  M^{\prime\prime}  and  M^{\prime}  (see Methods). The alternating splitting is further examined in Fig. 3D and Fig. 3E, presenting a spin-resolved view of the bands around the  M^{\prime}  points.

Energy distribution curves (EDCs) at momentum  k_{1}  (Fig. 3D) display significant spin polarization. States polarized along the +c direction are shifted closer to the Fermi level by  70 \pm 20  meV than those along -c. By contrast, at momentum
 

![](images/1070588194879176733_14.jpg)

Figure 4. ARRES measurement of spin-split unoccupied electronic structure in  \( CoNb_{4}Se_{8} \)  (A, B) Schematic of sp-ARRES experiment: Spin-polarized electrons incident on the sample are preferentially absorbed if there is an unoccupied electronic state with corresponding spin  \( \vec{s} \) , energy E and momentum  \( \vec{k} \) . (C, D) DFT calculations of unoccupied electronic structure (C) and NRSS along c-axis (D) at constant energy surface 10.965 eV above  \( E_{F} \) . (E, F) Spin-integrated (E) and spin-polarized (F) ARRES spectra at constant energy surface 11 eV above  \( E_{F} \)  at T = 30 K. Band locations, indicated by maximal band curvature, overlaid in black. (G, H) Spin contrast in DFT (G) and the ARRES experiment (H) along  \( k_{\parallel} = 0.3 \frac{\pi}{a} \) .

 \( k_{2}=C_{2}(k_{1})=C_{6}^{3}(k_{1}) \)  (Fig. 3E), the spin splitting is inverted: states polarized along +c are now  30\pm20  meV further from  E_{F} . Fig. 3F summarizes this alternating spin splitting, providing strong evidence for  CoNb_{4}Se_{8}  being a bulk-type g-wave consistent with similar patterns in compounds  MnTe}^{20} CrSb^{23} , which share same point group The observed asymmetry magnitude sample-detector misalignment.

NRSS in  CoNb_{4}Se_{8}  is not restricted to the quasiparticle states near  E_{F}  but extends over a large energy range. DFT (Fig. 4C, D) show that even at 11 eV above  E_{F} , constant energy surfaces exhibit spin splitting that alternates with each  C_{6z}  rotation about the zone center, reflecting persistent symmetry-breaking effects in reciprocal space (see Methods).

## The Unoccupied Electronic Structure of CoNb_{4}Se_{8} via ARRES

We introduce a new technique called spin- and angle-resolved electron reflection spectroscopy (spin-ARRES) (Fig. 4A), which improves on a well-established method for probing the unoccupied electronic structure 48,49  by adding the spin resolution available in SPLEEM 56 . Spin-ARRES measures the reflectivity of the sample surface for an incident electron with energy E, momentum  \vec{k} , and spin  \vec{s}  (Fig. 4C). The reflectivity sharply drops when an unoccupied electronic state is present at  (E,\vec{k},\vec{s})  in its electronic structure (Fig. 4B). Analogous to spin- and angle-resolved inverse photoemission spectroscopy (SP-ARIPES) 57,58 , spin-ARRES offers a significantly greater interaction cross-section (by a factor of  10^{5} ) due to its use of electrons rather than photons, enabling higher-throughput spectroscopy 59 .

The spin-integrated ARRES constant energy surface for  CoNb_{4}Se_{8} , shown in Fig. 4E, reveals a clear band-like structure in the unoccupied electronic states well above  E_{F electronic absorption curvature 60 , outlined in black, peaks at momentum regions predicted by first-principles calculations to correspond to unoccupied states, consistent with previous experiments on similar materials 48,49 . Just as electron reflectance contrast  \frac{I_{t}-I_{f}}{P(I_{t}-I_{t})}  indicates energy splitting of unoccupied electronic states at  \vec{k}_{\parallel} \neq 0  in SPLEEM 56 , here in spin-ARRES the contrast indicates energy splitting of electronic states at  \vec{k}_{\parallel} \neq 0 .

The spin-ARRES spectra with  \vec{s}\parallel c  in Fig. 4F present a spin texture that alternates along a circular orbit around the  \Gamma^{\prime}  point, in qualitative agreement with the first-principles calculations. When considering the angular path at a radius of  0.3\pi/a  (Fig. 4G, Fig. 4H), it is clear that at every  \pi/3  the spin contrast changes sign. Interestingly, both the DFT (Fig. 4E) and spin-ARRES spectra (Fig. 4F) show zero splitting at the  \Gamma^{prime}  point, with finite spin splitting appearing only at  \vec{k}\neq0 . Taken together, these
 
oste,>reinforce the theoretical prediction of a bulk-type g-wave altermagnetic symmetry, where spin splitting at  kz \neq 0  alternates with each  C_{6z}  rotation about  \Gamma'^{10}  rather than following the conventional s-wave splitting seen in ferromagnets 61 .

## Temperature-Dependent Evidence of Altermagnetic Phase Transition

The presence of alternating  C_{6z}  spin splitting alone does not fully confirm altermagnetic order, as similar effects might result from conventional spin-orbit coupling mechanisms. To clearly establish NRSS as the origin, we present temperature-dependent evidence in Fig. 5 that confirms an altermagnetic phase transition in  CoNb}_{4}Se}_{8} , indicated by temperature-dependent changes in spin splitting within the electronic structure.

In the low-energy ARPES spectra, two distinct spin-split electron pockets emerge below the Néel temperature (Fig. 5A). Above this temperature (Fig.  5B ), the spectral weight near the Fermi level decreases uniformly across the BZ. From Luttinger's theorem, such a change in Fermion number (Fig.  5C ) suggests a phase transition, typically accompanied by symmetry breaking. Similar spectral changes are commonly observed in ARPES for AFM 62 , CDW 63 , and superconducting 64  transitions.

In our tight-binding model, the strength of NRSS is reflected in the degree of spin splitting at the  M^{\prime}  pockets. At 13K, the momentum distribution curves (MDCs) at the Fermi level, shown panels D and E, exhibit two peaks with nearly equal intensity. The stronger peak aligns spins along the +c direction, while the weaker peak aligns spins along -c, suggesting magnetization of Co atoms on the c=0 plane along +c. Above the Néel transition, both peaks decrease sharply in intensity (Fig. 5D), with the -c polarized peak further decreasing by an additional 50% relative to the +c polarized peak (Fig. 5E).

The overall reduction in Fermi surface spectral weight across the Néel transition, as shown in Fig. 5F, reflects spontaneous symmetry breaking typical of AFM phase transitions 62 . However, the selective reduction in spectral weight for only one of the spin-split bands across  T_{N}  (Fig. 5G) can only be attributed to the onset of NRSS in  CoNb_{4}Se_{8} , thereby confirming theoretical predictions for this class of intercalated compounds 2,52 . Additionally, the observed increase in split peak weight between 13 K and 50 K may signal another phase transition. This behavior is tentatively linked to the CDW origins known to appear around 30 K in the parent compound  NbSe_{2}^{65 } , which may explain observed changes in susceptibility and transport properties in the 1/4-intercalated compound 52 .

## Discussion

## Discussion

This study represents a pivotal step in establishing  CoNb_{4}Se}_{8}  as a prototypical g-wave altermagnet, offering a robust framework for understanding and characterizing NRSS. By combining theory and calculations with complementary experimental probes – spin-ARPES and spin-ARRES – we directly observe symmetry-enforced NRSS and an altermagnetic phase transition. These findings address longstanding challenges in observing NRSS and uncover new physics tied to symmetry-protected spin-split states in quantum materials.

The complementary use of spin-ARPES and spin-ARRES to measure the electronic structure of  CoNb}_{4}Se}_{8}  offers unprecedented insight into the nature of NRSS in  CoNb_{4}Se}_{8} , addresses key limitations of existing probes. Spin-ARPES directly confirms the predicted spin-split bands in the occupied electronic structure, providing momentum-resolved evidence of g-wave symmetry, and validating the predictions of our theoretical framework. Meanwhile, spin-ARRES extends this capability to unoccupied states, revealing NRSS across a broad energy range and overcoming the energy limitations of spin-ARPES. The combination of these techniques overcomes the limitations of single-method approaches, where spin-ARPES alone may struggle with resolution and spatial inhomogeneity, and indirect probes such as anomalous Hall effect measurements are constrained by coexisting ferromagnetism or the need for applied magnetic fields.
Our introduction of spin-ARRES as a novel probe of the (unoccupied spin-polarized band structure offers complementary information to spin-ARPES. Despite having a broader energy resolution ( \sim ) 225 meV; see Supplementary Information) that limits its ability to distinguish NRSS at fine energy scales, its superior spatial resolution ( \sim  1  \mu m) over ARPES opens exciting possibilities. For example, the technique enables high-resolution magnetostructural measurements of altermagnetic domains on the meso- and nanoscale, which is crucial for applications requiring localized control over spin states in spintronic devices 39,48 . Additionally, our experimental demonstration of NRSS of unoccupied bands opens the door to a wealth of optical signatures of NRSS in altermagnets where the splitting of both occupied and unoccupied bands is required 54,66,67 .
Crucially, we observe a clear altermagnetic phase transition in  CoNb}_{4}Se}_{8} , with the suppression of NRSS near the Néel temperature confirming that the spin splitting is directly linked to altermagnetic order. This temperature-dependent evolution distinguishes the observed spin splitting from conventional mechanisms such as spin-orbit coupling. However, the persistence of residual ion spin splitting above  T_{N}  indicates secondary contributions. In Nb-based compounds, SOC is significant, and at the surface where ARPES is sensitive, local inversion symmetry breaking in the metallic state of the parent compound  NbSe}_{2}  can produce a similar spin texture to what we observe 68 . This explanation is consistent with our experimental setup, as the photon energy of 55 eV results in a short electron mean free path 69 , enhancing surface sensitivity. On the other hand, the observed decrease in spectral weight across the Néel transition is not present in  NbSe}_{2} , suggesting a coexistence of SOC and intrinsic altermagnetic splitting in  CoNb}_{4}Se}_{8} . Alternatively, the residual spin splitting above  T_{N}  may be explained by dynamic
 

A

![](./images/1070588194879176733_15.jpg)

D

![](./images/1070588194879176733_16.jpg)

F

![](./images/1070588194879176733_17.jpg)

B

![](./images/1070588194879176733_18.jpg)

E

G

C

![](./images/1070588194879176733_19.jpg)

![](./images/1070588194879176733_20.jpg)

![](./images/1070588194879176733_21.jpg)

Figure 5. Observation of an altermagnetic phase transition. (A to C) Low-energy ARPES spectra of  \( CoNb_{4}Se_{8} \)  along  \( M^{\prime\prime}-\Gamma^{\prime}-M^{\prime} \)  path in momentum space at T=50 K (A), 200 K (B), and their difference (C). (D, E) MDCs spectra as a function of temperature along region in yellow rectangles in A,B and normalized by total intensity (D) and maximum peak height (E). (F) Fermi surface spectral weight along  \( M^{\prime\prime}-\Gamma^{\prime}-M^{\prime} \)  as a function of temperature. (G) Relative peak height of NRSS bands as a function of temperature, extracted from Lorentzian-like fits to MDCs spectra in (D). Grey lines in (F,G) correspond to the Néel ordering temperature.
 
altermagnetic fluctuations, analogous to those seen in low-dimensional quantum materials near a quantum critical point 70 . These results highlight a complex interplay of mechanisms contributing to the observed NRSS and its persistence above the ordering temperature.
Finally, our proposal of a Symmetry-Constrained Adaptive Basis (SCAB), provides a novel and transferrable approach to link local bonding asymmetries to global momentum-dependent spin textures. This represents a significant advance over traditional crystal field analysis, which cannot capture the interplay of sublattice symmetries critical to NRSS and the corresponding g-wave altermagnetic order. This approach allows us to understand, both using a tight-binding model and DFT calculations, how crystal-field and Zeeman splittings cooperate to drive NRSS and predict the alternating spin splitting characteristic of g-wave symmetry.
The introduction of NRSS to the phases available in intercalated transition metal dichalcogenides 52,71  offers an inviting materials family in which to explore the interplay of competing order in phase transitions. For example, the parent compound 2H-NbSe _{2}  hosts competing CDW 65 , anisotropic superconducting 55,72 , and pair density wave order 73 . CoNb _{4} Se _{8}  presented in this work exhibits no superconducting order and evidence for the 3x3 CDW phase present in the parent compound 52 . Lifting of time-reversal symmetry in altermagnets therefore applies additional constraints on the pairing symmetry and angular momentum of Cooper pairs 74 . The vast playground of possibilities in intercalated TMDs offer a range of possibilities for exploring coexisting and competing phases in altermagnetic TMDs. For instance, altermagnetic TMD with stronger spin orbit coupling have been synthesized 71 , and the van-der-Waals nature of the material leaves tantalizing possibilities for interface- and heterostructure-enabled quantum phases 74-76 .

## Acknowledgements

We acknowledge assistance in sample holder fabrication, Andreas Schmid assistance on the QSPLEEM experimental setup, and Edward Barnard for assistance in implementing ARRES data acquisition software. We appreciate helpful discussions about the DFT calculations and crystal field analysis with Ella Banyas, Isaac Craig, Jack Broad, Kevin Moseni, and Veronika Sunko. We thank Igor Mazin for useful discussions, and Aeron Hammack, Shelly Conroy, John Vinson and Adam Schwartzberg for feedback on drafts of this manuscript.

## Funding

This work was primarily supported Laboratory Directed Research and Development Program of LBNL under the U.S. Department of Energy (DoE) Contract No. DE-AC02-05CH11231. The theoretical work was funded by the U.S. Department of Energy, Office of Science, Office of Basic Energy Sciences, Materials Sciences and Engineering Division under Contract No. DE-AC02-05-CH11231 within the Theory of Materials program. Work was performed at the Molecular Foundry and at the Advanced Light Source supported by the Office of Science, Office of Basic Energy Sciences, of the U.S. Department of Energy under contract no. DE-AC02-05CH11231. This research used resources of the National Energy Research Scientific Computing Center, a DOE Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231 using NERSC award BES-ERCAP0020966. N.J.G. and R.B.R. were supported by Army Research Office under Cooperative Agreement Number W911NF-22-2-0173.

## Author Contributions

S.M.G., N.D., A.S., and C.W.J. conceived the study. O.A.A., J.F., and N.D. conducted DFT calculations. O.A.A., M.V., N.D. and S.M.G. developed the SCAB. M.V. developed the tight-binding model with input from O.A.A., N.D., J.F., and S.M.G. R.B.R. and N.J.G. grew the crystals. N.D. and A.F. conducted spin-ARPES measurements. C.W.J. developed the ARRES technique at the Foundry and N.D. and A.S. conducted the spin-ARRES measurements. N.D., O.A.A., M.V., and S.M.G. wrote the paper with input from all coauthors. S.M.G. supervised the project.

## Data and Availability

All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials.

## Competing Interests

The authors declare that they have no competing interests.

## References

1. Noda, Y., Ohno, K. & Nakamura, S. Momentum-dependent band spin splitting in semiconducting  \( MnO_{2} : a density functional calculation. Phys. Chem. Chem. Phys. 18, 13294‖).
 
2. Šmejkal, L. et al. Crystal time-reversal symmetry breaking and spontaneous Hall effect in collinear antiferromagnets. Sci. Adv. 6, DOI: https://doi.org/10.1126/sciadv.aaz8809 (2020).

3. Naka, M. et al. Spin current generation in organic antiferromagnets. Nat. Commun. 10, 4305, DOI: https://doi.org/10.1038/s41467-019-12229-y (2019).

4. Ahn, K.-H., Hariki, A., Lee, K.-W. & Kuneš, J. Antiferromagnetism in  \( RuO_{2} \)  as d-wave pomeranchuk instability. Phys. Rev. B 99, 184432, DOI: https://doi.org/10.1103/PhysRevB.99.184432 (2019).

5. Hayami, S., Yanagi, Y. & Kusunose, H. Momentum-dependent spin splitting by collinear antiferromagnetic ordering. J. Phys. Soc. Jpn. 88, 123702, 2019).

6. Yuan, L.-D., Wang Z., Luo, J.-W., Rashba, E. I. & Zunger, A. Giant momentum-dependent spin222, DOI: https://doi.org/10.1103/PhysRevB.102.014422 (2020).

7. Pekar, S. I. & Rashba, E. Combined Resonance in Crystals in Inhomogeneous Magnetic Fields. Zh. Eksp. Teor. Fiz. 47, 1927–1932 (1964).

8. Hayami, S., Yatsushiro, M., Yanagi, Y. & Kusunose, H. Classification of atomic-scale multipoles under crystallographic point groups and application to linear response tensors. Phys. Rev. B 98, 165110, DOI: https://doi.org/10.1103/PhysRevB.98.165110 (2018).

9. Hayami, S., Yanagi, Y. & Kusunose, H. Bottom-up design of spin-split and reshaped electronic band structures in antiferromagnets without spin-orbit coupling: Procedure on the basis of augmented multipoles. Phys. Rev. B 102, 144441, DOI: https://doi.org/10.1103/PhysRevB.102.144441 (2020).

10. Šmejkal, L., Sinova, J. &angwirth, T. Beyond Conventional Ferromagnetism and Antiferromagnetism: Phase with Nonrelativistic Spin and Crystal Rotation Symmetry. Phys. Rev. X 12, 1–16, DOI: https://doi.org/10.1103/PhysRevX.12.031042 (2022).

11. Šmejkal, L., Sinova, J. &ungwirth, T. Emerging Landscape of Altermagnetism. Phys. Rev. X 12, 1–27, DOI: https://doi.org/10.1103/PhysRevX.12.040501 (2022). ArXiv: 2204.10844.

12. Brinkman, W. & Elliott, R. J. Space Theory Spin Waves. J. Appl. Phys. 1457–1459, DOI: https://doi.org/10.1063/1.1708514 (1966).

13. Brinkman, W. F. & Elliott R. J. Theory of spin-space groups. Proc. Royal Soc. London. Ser. A. Math. Phys. Sci. 294, 343–358, DOI: https://doi.org/10.1098/rspa.1966.0211 (1996).

14. Litvin, D. B. & Opechowski, W. Spin groups. Physica 76, 538–554, DOI: https://doi.org/10.1016/0031-8914(1974).

15. Litvin, D. B. Spin point groups. Acta Crystallogr. Sect. A: Cryst. Physics, Diffraction, Theor. Gen. Crystallogr. 33, 279–287, DOI: https:/.1107/S0567739477000709 (1977).

16. Liu, P., Li, J., Han, J., Wan, X. & Liu, Q. Spin-Group Symmetry in Materials Negligible Spin-Orbit Coupling. Phys. Rev. X 12, 021016, DOI: https://doi.org/10.1103/PhysRevX.12.021016 (2022).

17. Fedchenko, O. et al. Observation RuO_{2} . Sci. Adv. 10, eadj4883, DOI: https://doi.org/10.1126/sciadv.adj4883 (2024).

18. Lin, Z. et al. Observation of giant spin splitting and d-wave spin texture in room temperature altermagnet  \( RuO_{2} \) , DOI: https://doi.org/10.48550/arXiv.2402.04995 (2024). arXiv:2402.04995.

19. Reichlova, H. et al. Observation Hall Response in Mn}_{5}Si}_{3}  d-wave altermagnet candidate. Nat.Commun. 156961, DOI: https://doi.org/10.1038/s41467-024-48493-w (2024).

20. Krempasky, J. et al. Altermagnetic lifting of Kramers spin degeneracy. Nature 626, 517–522, DOI: https://doi.org/10.1038/s41586-023-06907-7 (2024).

21. Lee, S. et al. Broken Kramers degeneracy in altermagnetic MnTe. Phys. Rev. Lett. 132, 036702, DOI: https://doi.org/10.1103/PhysRevLett.132.036702 (2024).

22. Osumi, T. et al. Observation of a giant band splitting in altermagnetic MnTe. Phys. Rev. B 109, 115102, DOI: https://doi.org/10.1103/PhysRevB.109.115102 (2024).

23. Reimers, S. et al. Direct observation of altermagnetic band splitting in CrSb thin films. Nat. Commun. 152116, DOI: https://doi.org/10.1038/s41467-024-46476-5 (2024).
 
24. Yang, G. et al. Three-dimensional mapping electronic origin large altermagnetic splitting near Fermi level in DOI: https://doi.org/10.48550/arXiv.2405.12575 (2024). arXiv:2405.12575.

25. Zeng, M. et al. Observation of spin splitting in room-temperature metallic antiferromagnet CrSb. Adv. Sci. 2406529, DOI: https://doi.org/10.1002/advs.202406529 (2024).

26. Mazin, I. I. Notes on altermagnetism and superconductivity, DOI: https://doi.org/10.48550/arXiv.2203.05000 (2022). arXiv:2203.05000.

27. de Carvalho, V. S. & Freire, H. Unconventional superconductivity in altermagnets with spin-orbit coupling DOI: https://doi.org/10.48550/arXiv.2409.10712 (2024). arXiv:2409.10712.

28. Chakraborty, D. & Black-Schaffer, A. M. Zero-field finite-momentum and field-induced superconductivity in altermagnets. Phys. Rev. B 110, L060508, DOI: https://doi.org/10.1103/PhysRevB.110.L060508 (2024).

29. Das, S. K. & Roy, B. From local spin nematicity to altermagnets: Footprints of band topology, DOI: https://doi.org/10.48550/arXiv.2403.14620 (2024). arXiv:2403.14620.

30. Li, C. et al. Topological Weyl altermagnetism in CrSb, DOI: https://doi.org/10.48550/arXiv.2405.14777 (2024). arXiv:2405.14777.

31. Chappert, C., Fert, A. & Van Dau, F. N. The emergence of spin electronics in data storage. Nat. Mater. 6, 813–823, DOI: https://doi.org/10.1038/nmat2024 (2007).

32. Ralph, D. & Stiles, M. Spin transfer torques. J. Magn. Magn. Mater. 320, 1216, DOI: https://doi.org/10.1016/j.jmmm.2007.12.019 (2008).

33. Brataas, A., Kent, A. D. & Ohno, H. Current-induced torques in magnetic materials. Nat. Mater. 11, 372–381, DOI: https://doi.org/10.1038/nmat3311 (2012).

34. González-Hernández, R. et al. Efficient electrical spin splitter based on nonrelativistic collinear antiferromagnetism. Phys. Rev. Lett. 126, 127701, DOI: https://doi.org/10.1103/PhysRevLett.126.127701 (2021).

35. Bai, H. et al. Observation of spin splitting torque in a collinear antiferromagnet  \( ruo_{2} \) . Phys. Rev. Lett. 128, 197202, DOI: https://doi.org/10.1103/PhysRevLett.128.197202 (2022).

36. Karube, S. et al. Observation of spin-splitter torque in collinear antiferromagnetic  \( ruo_{2} \) . Phys. Rev. Lett. 129, 137201, DOI: https://doi.org/10.1103/PhysRevLett.129.137201 (2022).

37. Marrows, C. H., Barker, J., Moore, T. A. & Moorsom, T. Neuromorphic computing with spintronics. npj Spintron. 2, 12, DOI: https://doi.org/10.1038/s44306-024-00019-2 (2024).

38. Hariki, A. et al. X-ray magnetic circular dichroism in altermagnetic  \( \alpha \) -MnTe. Phys. Rev. Lett. 132, 176701, DOI: https://doi.org/10.1103/PhysRevLett.132.176701 (2024).

39. Amin, O. J. et al. Altermagnetism imaged and controlled down to the nanoscale, DOI: https://doi.org/10.48550/arXiv.2405.02409 (2024). arXiv:2405.02409.

40. Smolyanyuk, A., Mazin, I. I., Garcia-Gassull, L. & Valenti, R. Fragility of magnetic order in the prototypical al  \( RuO_{2} \) . Phys. Rev. B 109, 134424, DOI: https://doi.org/10.1103/PhysRevB.109.134424 (2024).

41. Fields, S. S., Callahan, P. G., Combs, N. G., Cress, C. D. & Bennett, S. P. Orientation control and mosaicity in heteroepitaxial  \( RuO_{2} \)  thin films grown through reactive direct current sputtering. Cryst. Growth & Des. 24, 4604–4612, DOI: https://doi.org/10.1021/acs.cgd.4c00271 (2024). https://doi.org/10.1021/acs.cgd.4c00271.

42. Feng, Z. et al. An anomalous Hall effect in altermagnetic ruthenium dioxide. Nat. Electron. 5, 735–743, DOI: https://doi.org/10.1038/s41928-022-00866-z (2022).

43. Gonzalez Betancourt, R. D. et al. Spontaneous anomalous Hall effect arising from an unconventional compensated magnetic phase in a semiconductor. Phys. Rev. Lett. 130, 036702, DOI: https://doi.org/10.1103/PhysRevLett.130.036702 (2023).

44. Hariki, Takahashi, Y. & Kuneš, J. X-ray magnetic circular dichroism in  \( RuO_{2} \) . Phys. Rev. B 094413, DOI: https://doi.org/10.1103/PhysRevB.109.094413 (2024).

45. Sunko, V. et al. Linear magneto-conductivity as a DC probe of time-reversal symmetry breaking, DOI: https://doi.org/10.48550/arXiv.2310.15631 (2023). arXiv:2310.15631.

46. Vasilyev, D. & Kirschner, J. Design and performance of a spin-polarized electron energy loss spectrometer with high momentum resolution. Rev. Sci. Instruments 87, 083902, DOI: https://doi.org/10.1063/1.4961471 (2016). https://pubs.aip.org/aip/rsi/article-pdf/doi/10.1063/1.4961471/16095681/083902_1_online.pdf.
 
47. Castellanos-Reyes, J. A. et al. Unveiling the impact of temperature on magnon diffuse scattering detection in the transmission electron microscope. Phys. Rev. B 108, 134435, DOI: https://doi.org/10.1103/PhysRevB.108.134435 (2023).

48. Jobst, J., Kautz, J., Geelen, D., Tromp, R. M. & Van Der Molen, S. J. Nanoscale measurements of unoccupied band dispersion in few-layer graphene. Nat. Commun. 6, 1–6, DOI: https://doi.org/10.1038/ncomms9926 (2015).

49. Jobst, J. et al. Quantifying electronic band interactions in van der Waals materials using angle-resolved reflected-electron spectroscopy. Nat. Commun. 7, 1–6, DOI: https://doi.org/10.1038/ncomms13621 (2016). Publisher: Nature Publishing Group.

50. Xie, L. S., Čhernyshov, S., Gonzalez, O., Craig, I. M. & Bedia, D. K. Structure and magnetism of iron- and chromium-intercalated niobium and tantalum disulfides. J. Am. Chem. Soc. 144, 9525–9542, DOI: https://doi.org/10.1021/jacs.1c12975 (2022). PMID: 35584537, https://doi.org/10.1021/jacs.1c12975.

51. Cheong, S.-W. & Huang, F.-T. Altermagnetism with non-collinear spins. npj Quantum Mater. 9, 13, DOI: https://doi.org/10.1038/s41535-024-00626-6 (2024).

52. Regmi, R. B. et al. Altermagnetism in the layered intercalated transition metal dichalcogenide  \( CoNb_{4}Se_{8} \) , DOI: https://doi.org/10.48550/arXiv.2408.08835 (2024). arXiv:2408.08835.

53. Craig, I. M., Kim, B. J., Limmer, D. T., Bedia, D. K. & Griffin, S. M. Modeling the superlattice phase diagram of transition metal intercalation in bilayer  \( 2H-TaS_{2} \) , DOI: https://doi.org10.48550/arXiv.2410.19664 (2024). arXiv:2410.19664.

54. Vila, M., Sunko, V. & Moore, J. E. Orbital-spin locking and its optical signatures in altermagnets, DOI: https://doi.org/10.48550/arXiv.2410.23513 (2024). arXiv:2410.23513.

55. Rahn, D. J. et al. Gaps and kinks in the electronic structure of the superconductor  \( 2H-NbSe_{2} \)  from angle-resolved photoemission at 1 K. Phys. Rev. B 85, 224532, DOI: https://doi.org/10.1103/PhysRevB.85.224532 (2012).

56. Rougemaille, N. & Schmid, A. K. Magnetic imaging with spin-polarized low-energy electron microscopy. Eur. Phys. J. Appl. Phys. 50, 20101, DOI: https://doi.org/10.1051/epjap/2010048 (2010).

57. Donath, M. Spin-resolved inverse photoemission of ferromagnetic surfaces. Appl. Phys. A 49, 351–364, DOI: https://doi.org/10.1007/BF00615018 (1989).

58. Campos, A. F., Duret, P., Cabaret, S., Duden, T. & Tejeda, A. Spin- and angle-resolved inverse photoemission setup with spin orientation independent from electron incidence angle. Rev. Sci. Instruments 93, DOI: https://doi.org/10.1063/5.0076088 (2022). ArXiv: 2110.12883 Publisher: AIP Publishing, LLC.

59. Woodruff, D. P. Modern techniques of surface science (Cambridge University Press, 2016).

60. Zhang, P. et al. A precise method for visualizing dispersive features in image plots. Rev. Sci. Instruments 82, 043712, DOI: https://doi.org/10.1063/1.3585113 (2011). https://pubs.aip.org/aip/rsi/article-pdf/doi/10.1063/1.3585113/13461328/043712_1_online.pdf.

61. Graf, J. et al. Universal high energy anomaly in the angle-resolved photoemission spectra of high temperature superconductors: Possible evidence of spinon and holon branches. Phys. Rev. Lett. 98, 1–4, DOI: https://doi.org/10.1103/PhysRevLett.98.067004 (2007).

62. Harter, J. W. et al. Nodeless superconducting phase arising from a strong  \( (\pi, \pi) \)  antiferromagnetic phase in the infinite-layer electron-doped  \( sr_{1-x}la_{x}cuo_{2} \)  compound. Phys. Rev. Lett. 109, 267001, DOI: https://doi.org/10.1103/PhysRevLett.109.267001 (2012).

63. Zong, A. et al. Evidence for topological defects in a photoinduced phase transition. Nat. Phys 15, 27–31, DOI: https://doi.org/10.1038/s41567-018-0311-9 (2019).

64. Smallwood, C. L. et al. Tracking Cooper pairs in a cuprate superconductor by ultrafast angle-resolved photoemission. Science 336, 1137–1139, DOI: https://doi.org/10.1126/science.1217423 (2012). ArXiv: 1206.2300.

65. Rossnagel, K. On the origin of charge-density waves in select layered transition-metal dichalcogenides. J. Physics: Condens. Matter 23, 213001, DOI: https://doi.org/10.1088/0953-8984/23/21/213001 (2011).

66. Adamantopoulos, T. et al. Spin and orbital magnetism by light in rutile altermagnets. npj Spintron. 2, 46, DOI: https://doi.org/10.1038/s44306-024-00053-0 (2024).

67. Weber, M. et al. All optical excitation of spin polarization in d-wave altermagnets, DOI: https://doi.org/10.48550/arXiv.2408.05187 (2024). arXiv:2408.05187.
 
68. Bawden, L. et al. Spintronics–valley locking in the normal state of a transition-metal dichalcogenide superconductor. Nat Commun 7, 11711, DOI: https://doi.org/10.1038/ncomms11711 (2016).

69. Hüfner, S. Photoelectron spectroscopy: principles and applications (Springer Science & Business Media, 2013).

70. Norman, M. R., Randeria, M., Ding, H. & Campuzano, J. C. Phenomenology of the low-energy spectral function in high- \( T_{c} \)  superconductors. Phys. Rev. B 57, R11093–R11096, DOI: https://doi.org/10.1103/PhysRevB.57.R11093 (1998).

71. Mandujano, H. et al. Itinerant A-type antiferromagnetic order in  \( Co_{0.25}TaSe_{2} \) , DOI: https://doi.org/10.48550/arXiv.2408.10421 (2024). arXiv:2408.10421.

72. Fletcher, J. D. et al. Penetration depth study of superconducting gap structure of  \( 2H-NbSe_{2} \) . Phys. Rev. Lett. 98, 057003, DOI: https://doi.org/10.1103/PhysRevLett.98.057003 (2007).

73. Liu, X., Chong, Y. X., Sharma, R. & Davis, J. C. S. Discovery of a cooper-pair density wave state in a transition-metal dichalcogenide. Science 372, 1447–1452, DOI: https://doi.org/10.1126/science. abd4607 (2021). https://www.science.org/doi/pdf/10.1126/science.abd4607.

74. Jungwirth, T., Fernandes, R. M., Sinova, J. &al, L. Alternagnets and beyond: Nodal magnetically-ordered phases (2024). arXiv:2409.10034.

75. Cao, Y. et al. Correlated insulator behaviour at half-filling in magic-angle graphene superlattices. Nature 556, 80–84, DOI: https://doi.org/10.1038/nature26154 (2018). Publisher: Nature Publishing Group.

76. Heinsdorf, N. Altermagnetic Instabilities from Quantum Geometry, DOI: https://doi.org/10.48550/arXiv.2410.12789 (2024). arXiv:2410.12789.

77. Stansbury, C. & Lanzara, A. PyARPES: An analysis framework for multimodal angle-resolved photoemission spectroscopies. SoftwareX 11, 100472, DOI: https://doi.org/10.1016/softx.2020.100472 (2020). Publisher: Elsevier B.V.

78. dela Figuera, J. & McCarty, K. F. Low-Energy Electron Microscopy, 531–561 (Springer Berlin Heidelberg, Berlin, Heidelberg, 2013).

79. Rougemaille, N. & Schmid, A. K. Self-organization and magnetic domain microstructure of Fe nanowire arrays. J. Appl. Phys. 99, 08S502, DOI: https://doi.org/10.1063/1.2165610 (2006).

80. Blöchl, P. E. Projector augmented-wave method. Phys. Rev. B 50, 17953–17979, DOI: https://doi.org/10.1103/physrevb.50.17953 (1994).

81. Kresse, G. & Furthmüller, J. Efficiency using a plane-wave basis set. Comput. Mater. Sci. 6, 6, 15–50, DOI: https://doi.org/10.1016/0927-0256(96)00008-0 (1996).

82. Kresse, G. & Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 54, 11169–11186, DOI: https://doi.org/10.1103/PhysRevB.54.11169 (1996).

83. Kresse, G. & Hafner, J. Ab initio molecular dynamics for liquid metals. Phys. Rev. B 47, 558–561, DOI: https://doi.org/10.1103/PhysRevB.47.558 (1993).

84. Kresse, G. & Hafner, J. Ab initio molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transition in germanium. Phys. Rev. B 49, 14251–14269, DOI: https://doi.org/10.1103/PhysRevB.49.14251 (1994).

85. Kresse, G. & Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B 59, 1758–1775, DOI: https://doi.org/10.1103/PhysRevB.59.1758 (1999).

86. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 77, 3865–3868, DOI: https://doi.org/10.1103/PhysRevLett.77.3865 (1996).

87. Methfessel, M. & Paxton, A. T. High-precision sampling for Brillouin-zone integration in metals. Phys. Rev. B 40, 3616–3621, DOI: https://doi.org/10.1103/PhysRevB.40.3616 (1989).

88. Ganose, A. M., Jackson, A. J. & Scanlon, D. O. Sumo: Command-line tools for plotting and analysis of periodic *ab initio* calculations. J. Open Source Softw. 3, 717, DOI: https://doi.org/10.21105/joss.00717 (2018).

89. Ganose, A. M., Searle, A., Jain, A. & Griffin, S. M. IFermi: A python library for Fermi surface generation and analysis. J. Open Source Softw. 6, 3089, DOI: https://doi.org/10.21105/joss.03089 (2021).

90. Maintz, S., Deringer, V. L., Tchougréeff, A. L. & Dronskowski, R. LOBSTER: A tool to extract chemical bonding from plane-wave based DFT. J. Comput. Chem. 37, 1030–1035, DOI: https://doi.org/10.1002/jcc.24300 (2016).

91. Nelson, R. et al. et al. Lobster: Local orbital projections, atomic charges, and chemical-bonding analysis from projector-augmented-wave-based density-functional theory. J. Comput. Chem. 41, 1931–1940, DOI: https://doi.org/10.1002/jcc.26353 (2020). https:onlinelibrary./doi/pdf/10.1002/jcc.26353.
 
92. Blöchl, P. E., Jepsen, O. & Andersen, O. K. Improved tetrahedron method for Brillouin-zone integrations. Phys. Rev. B 49, 16223–16233, DOI: https://doi.org/10.1103/PhysRevB.49.16223 (1994).

93. Dudarev, S. L., Botton, G. A., Savrasov, S. Y., Humphreys, C. J. & Sutton, A. P. Electron-energy-loss spectra and the structural stability of nickel oxide: An LSDA+U study. Phys. Rev. B 57, 1505–1509, DOI: https://doi.org/10.1103/PhysRevB.57.1505 (1998).

94. Grimme, S., Antony, J., Ehrlich, S. & Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. The J. Chem. Phys. 132, 154104, DOI: https://doi.org/10.1063/1.3382344 (2010).

95. Grimme, S., Ehrlich, S. & Goerigk, L. Effect of the damping function in dispersion corrected density functional theory. J. Comput. Chem. 32, 1456–1465, DOI: https://doi.org/10.1002/jcc.21759 (2011).

96. Perdew, J. P. et al. Restoring the Density-Gradient Expansion for Exchange in Solids and Surfaces. Phys. Rev. Lett. 100, 136406, DOI: https://doi.org/10.1103/PhysRevLett.100.136406 (2008).

97. Furness, J. W., Kaplan, A. D., Ning, J., Perdew, J. P. & Sun, J. Accurate and Numerically Efficient r2SCAN Meta-Generalized Gradient Approximation. J. Phys. Chem. Lett. 11, 8208–8215, DOI: https://doi.org/10.1021/acs.jpclett.0c02405 (2020).

98. Šmejkal, L., Sinova, J. & Jungwirth, T. Beyond Conventional Ferromagnetism and Antiferromagnetism: A Phase with Nonrelativistic Spin and Crystal Rotation Symmetry. Phys. Rev. X 12, 031042, DOI: https://doi.org/10.1103/PhysRevX.12.031042 (2022).

99. Slater, J. C. & Koster, G. F. Simplified lcao method for the periodic potential problem. Phys. Rev. 94, 1498–1524, DOI: https://doi.org/10.1103/PhysRev.94.1498 (.

100. Gotlieb, K. et al. Revealing hidden spin-momentum locking in a high-temperature cuprate superconductor. Science 1275, 1271–1275, DOI: https://doi.org/10.1126/science.aaof980 (2018).

101. Blundell, S. Magnetism in Condensed Matter (Oxford University Press, 2001).

## Supplementary Material

## Materials and Experimental Methods

## Crystal Growth

Single crystals of  \( CoNb_{4}Se_{8} \)  were grown \( ^{52} \)  by chemical vapor transport using iodine as the transport agent. First, a polycrystalline sample was prepared by heating stoichiometric amounts of cobalt powder (Alfa Aesar 99.998%), niobium powder (Alfa Aesar 99.8%), and selenium pieces (Alfa Aesear 99.9995%) in an evacuated silica ampule at  \( 950\ ^{\circ}C \)  for 5 days. Subsequently, 2 g of the powder was loaded together with 0.4 g of iodine in a fused silica tube of 14 mm inner diameter. The tube was evacuated and sealed under vacuum. The ampule of 10 cm length was loaded in a horizontal tube furnace in which the temperature of the hot zone was kept at  \( 950\ ^{\circ}C \)  and that of the cold zone was  \( \approx850\ ^{\circ}C \)  for 7 days. Several  \( CoNb_{4}Se_{8} \)  crystals formed with a distinct, well-faceted flat plate-like morphology.

## spin-ARPES measurements

ARPES was measured at the Advanced Light Source beamline 10.0.1 using a Scienta R4000 spectrometer equipped with DA30 deflector plates for spin-integrated ARPES mapping and for steering electrons into dual very low energy electron diffraction (VLEED) spin-detectors. Figures in the main text were acquired using a photon 55 eV, a temperature of 13 K, and a pressure better than 5e-11 Torr, producing an overall energy and momentum resolution of 10 meV 0.01 Å \( ^{-1} \) , respectively.

The two exchange-scattering type spin-detectors use in-plane magnetization of FeO thin film targets to provide  \( (k_{z}, k_{x}) \)  and  \( (k_{x},k_{y}) \)  components of the spin-asymmetry, e.g. with redundancy in the  \( k_{z} \)  component. For each spin-detector, the sequentially measured spectra  \( I_{+}(\omega) \)  and  \( I_{-}(\omega) \)  are used to compute the raw spin-scattering asymmetry,  \( A_{\pm}(\omega) = (I_{+} - I_{-}) / (I_{+} + I_{-}) \) , which is corrected by the instrumental spin-scattering efficiency factor, i.e. the Sherman function  \( S_{eff} \) , to determine the photoelectron spin-polarization  \( P(\omega) = A_{\pm}(\omega) / S_{eff} \) . The corrected spin-dependent spectra are then calculated as  \( I_{\uparrow}(\omega) = I_{av}(\omega) (1 \pm P(\omega)) \) , where  \( I_{av} = (I_{+} + I_{-}) / 2 \) . The Sherman function for this exchange spin-detector is calibrated to be  \( S_{eff} \approx 0.2 \) . All ARPES data in this paper were analyzed using pyARPES, an open-source python-based analysis framework \( ^{77} \) .

## spin-ARPES measurements

Angle Resolved Reflection Electron Spectroscopy measurements were conducted using the QSPLEEM the Molecular Foundry at a temperature of 25 K.

Details of this technique are presented in Fig. S1, and build upon Refs. \( ^{48,49} \) . The QSPLEEM is equipped with illumination and imaging equalizers which effectively change the parallel momentum  \( \vec{k}_{\parallel}} \)  of the electrons impinging upon and reflecting
 

A

![](./images/1070588194879176733_22.jpg)

Figure S1. Angle Resolved Electron Reflection Spectroscopy Technique. (A to C) Schematic (above) and corresponding LEED pattern (below) for the ARRES measurement for (A)  \( \vec{k}_{\parallel}=0} \) , (B)  \( \vec{K}_{\parallel}\neq0 \) , and (C)  \( \vec{K}_{\parallel}\neq0 \)  with a realignment of the Ewald sphere onto the center of the camera. Green circle and orange hexagon indicate edge of Ewald sphere and BZ of  \( CoNb_{4}Se_{8} \) .
 

A

![](./images/1070588194879176733_23.jpg)

B

![](./images/1070588194879176733_24.jpg)

C

./images/1070588194879176733_25.jpg)

D

![](./images/1070588194879176733_26.jpg)

Figure S2. Energy and Momentum Resolution in SPLEEM (A) LEEM image of  \( CoNb_{4}Se_{8} \)  at 25 K for start voltage of 5V. Scale bar:  \( 10 \mu m \) . (B) LEEM reflectivity versus incident electron start voltage associated with region of sample in A. Dashed black curve indicates Fermi-Dirac fit described in the text. (C) LEED pattern for electron start voltage of 48V. Scale bar:  \( \pi/2a \) . (D) Lineout along  \( (0,0) \)  spot in C. Dashed black curve indicates Gaussian peak fit to the data

off of the sample, respectively. As mentioned in the main text, the incident  \( \vec{k}_{||} \)  of electrons that are absorbed into the sample correspond to unoccupied electronic states at that same momentum. For an incident electron with energy E, the parallel momentum is defined by  \( \vec{k}_{||} = E \sin \theta_{inc} \)  where  \( \theta_{inc} = \frac{\pi}{2} \) . As the angle of incidence on the sample controllable by the illumination equalizer. At normal incidence (Fig. S1A), for electron optics set to LEED mode the detector displays a low energy diffraction pattern corresponding to the order on the sample surface. Upon tuning  \( \theta_{inc} \) , nonzero incident momentum  \( \vec{k}_{||} \neq 0 \)  (Fig. S1B) causes the sampled diffraction pattern within the Ewald sphere (green circle) to shift to a new center about the reflected angle angle  \( \theta_{ref} \) . The imaging equalizer independently tunes  \( \theta_{re} \rightarrow \pi/2 \)  such that the specular spot centered at returns to the center of the detector (Fig. S1C), whereby a measurement of the intensity at detector center corresponds to the sample electron reflectivity at incident momentum  \( \vec{k}_{||} \neq 0 \) . This procedure can be repeated for every energy momentum, and spin value in the user's choice coordinate array.

As mentioned in the main text, spin-polarized ARRES measurements are conducted by measuring the reflectance contrast to an electron beam with spin polarization P (in our case,  \( P \approx 0.3 \) ). The spin polarization of the unoccupied electronic states are found by  \( A = \frac{1}{P} \frac{I_{+} - I_{-}}{I_{+} + I_{-}} \) , where  \( I_{+} \)  ( \( I_{-} \) ) is the reflected intensities for spins polarized parallel (antiparallel) to a spin vector ( \( \hat{s} \) ) \( . In all measurements for the main text, we set  \hat{s}  to be along the c axis of the sample, parallel to the sample Néel vector. Prior to measurement, the spin vector  \hat{s}  is calibrated following the procedure in Ref. 79 .

The overall experimental resolution ( \delta E = 225  meV ,  \delta k = 0.01 \pi / a ) is described following Fig. S2. Samples become
 
electron transparent for incident electron energy  (E) above the work function  (\Phi)^{78} . Given a certain region of interest on your sample  (\mathbf{r}) , depicted via LEEM mode in Fig. S2A, the energy resolution can be determined from the width of an error function fit to the intensity  I(\mathbf{r}, E)  of that region as a function of incident electron start voltage  (E) :

 \[ f(E)=\frac{1}{2}\left[1-\mathrm{erf}\left(\frac{E-\Phi(\mathbf{r})}{\sqrt{2(\sigma^{2}+(k_{B}T)^{2})}}\right)\right] \quad (S1) \] 

Here  \sigma  denotes the standard deviation of a gaussian which is convolved with the Fermi-Dirac distribution of electrons at temperature T. For low temperature ( k_{B}T << \sigma ), the energy resolution is the FWHM of that gaussian, i.e.  \delta E = 2\sigma\sqrt{2\ln2} = 225  meV.

Similarly, the momentum resolution can be determined from LEED data, shown in Fig. S2C for the sample measured in the main text. Momentum resolution  \delta\vec{k}/|\vec{G}|  is found as the ratio between the width of the diffraction spots to the BZ size. Here, the width of the LEED spots are the FWHM extracted from Gaussian fit to the  (0,0)  peak in LEED data (Fig. S2D), whereas the distance between the spots corresponds to the reciprocal lattice vector with norm given  |\vec{G}| . Combining these we find an overall momentum resolution of  0.01\pi/a .

## Computational Methods

Our density functional theory (DFT) calculations use the projector augmented wave (PAW) method  {}^{80}  as implemented in the Vienna Ab Initio Simulation Package (VASP) {}^{81-85}  version 6.4.3 and the potpaw.64 PAW dataset. All calculations in the main text use functional {}^{86} , without any dispersion or Hubbard corrections. We set the wavefunction energy cutoff at 900 eV BZ integrations were performed on a  \Gamma -centered  11 \times 11 \times 7  k-grid with 100 meV of second-order smearing {}^{87} . All calculations used an energy convergence criterion of  10^{-7}  eV, and a force convergence criterion of  10^{-3}  eV/ \AA . Band structures and 3D constant energy surfaces (Figs. 2 and S8) were plotted using modified versions of sumo {}^{88}  and IFermi {}^{89} , respectively.

The projected density of states, PAW wavefunction overlaps with d-orbitals, and Mulliken gross populations were calculated using LOBSTER {}^{90,91} . The overlap coefficients were then rotated to the SCAB and integrated over the BZ using the tetrahedron method {}^{92}  to obtain the PDOS shown in Fig. S4, and again integrated over energy to obtain the populations in Fig. 1C. The constant energy contours in Figs. 4C and 4D were calculated on a  48 \times 48  k-grid, and then interpolated to a  960 \times 960  k-grid. For the colormaps in those figures, the bands on the  48 \times 48 48  grid was convolved with a Gaussian ( \sigma = 100  meV) centered at 10.965 eV. In Fig. 4C, all bands were equally weighed, and in 4D, spin up and down bands were oppositely weighed, giving a qualitative measure of the spin splitting, similar to a k-resolved spin-weighted density of states.

To select the optimal DFT functional, benchmarked the performance of several exchange-correlation functionals, van-der-Waals corrections, and Hubbard U corrections, as shown Table S1. These calculations used a  9 \times 9 \times 5  k-grid and an 800 eV cutoff. As seen from the table, the PBE functional without corrections performs nearly as well as PBE corrected a Hubbard U of 0.75 eV and a D3 van-der-Waals correction with Becke-Johnson damping. For simplicity, we choose the uncorrected PBE for our calculations.

Table S1. Comparison of exchange-correlation functionals for structural (lattice constants a and c) and magnetic (magnetic moment m per Co) parameters in  CoNb_{4}Se_{8} . Hubbard U values are in eV and we used Dudarev's approach 93 . The magnetic moment values are computed directly from DFT, and are slightly smaller than the more accurate values obtained via Mulliken population analysis used in the main text.

<table><tr><td></td><td>a Error (%)</td><td>c Error (%)</td><td>M error (%)</td><td>a ( \textup{\AA} )</td><td>c ( \textup{\AA} )</td><td>m ( \mu_B )</td></tr><tr><td>Experiment (5K) ^{52} </td><td>-</td><td>-</td><td>—</td><td>6.904</td><td>12.321</td><td>1.375</td></tr><tr><td>PBE ^{86} </td><td>+0d</td><td>+1.251</td><td>+6.256</td><td>6.964</td><td>12.475</td><td>1.461</td></tr><tr><td>PBE ^{86} -D3(BJ) ^{94,95} </td><td>-0.818</td><td>-2.066</td><td>-50.327</td><td>6.848</td><td>12.066</td><td>0.683</td></tr><tr><td>PBE ^{86} -D3(BJ) ^{94,95} , U=0.5</td><td>-0.606</td><td>-1.659</td><td>-11.417</td><td>6.862</td><td>12.117</td><td>1.218</td></tr><td>PBE ^{86} -D3(BJ) ^{94,95} , U=0.75</td><td>-0.548</td><td>-1.341</td><td>+2.256</td><td>6.866</td><td>12.156</td><td>1.406</td></tr><td>PBE ^{86} -D3(BJ) ^{94,95} , U=1</td><td>-0.492</td><td>-1.192</td><td>+11.856</td><td>6.870</td><td>12.174</td><td>1.538</td></tr><td>PBE ^{86} -D3(BJ) ^{94,95} , U=3</td><td>-0.224</td><td>+0.368</td><td>4.893</td><td>6.889</td><td>12.366</td><td>2.116</td></tr><tr><td>PBE ^{} ^{96} </td><td>-0.926</td><td>-2.045</td><td>-63.490</td><td>6.840</td><td>12.069</td><td>0.502</td></tr><tr><td>PBE ^{96} -D3(BJ) ^{94,95} </td><td>-2.326</td><td>-3.910</td><td>—</td><td>6.744</td><td>11.840</td><td>0.000</td></tr><tr><td>R ^2 SCAN </td><td>+1.038</td><td>+2.256</td><td>+49.166</td><td>6.976</td><td>12.599</td><td>2.051</td></tr></table>
 

![](./images/1070588194879176733_27.jpg)

Figure S3. The DFT-calculated spin-polarized band structure of  \( CoNb_{4}Se_{8} \)  along high symmetry lines in the BZ without SOC. Spin-up (solid pink) and spin-down (dashed blue) are degenerate along every high symmetry line. The Fermi level is set to 0 eV and is marked by the dashed line.

![](./images/1070588194879176733_28.jpg)

![](./images/1070588194879176733_29.jpg)

Figure S4. The DFT-calculated spin-polarized density of states projected on the symmetry-constrained adaptive basis (SCAB) without SOC. States above (below) the center horizontal line correspond to spin up (down). The gray shading is the total DOS from all d-orbitals from both Co sublattices. The Fermi level is set to 0 eV and is marked by the solid line.
 

A

B

![]images/1070588194879176733_30.jpg)

Figure S5. (A) Top view of the  \( \left|e_{g}^{\pm}\right\rangle \)  orbital (with  \( \left|e_{g}^{\pm}\right\rangle \)  being its complex conjugate), with the black lines indicating the directions where the orbital is expected to bond differently (solid vs dashed) along two directions related by a  \( C_{6z} \)  rotation. (B) Top view of the real-space lattice at c=0 (top, sublattice I) and at c=1/2 (bottom, sublattice II). The same black lines from panel A are superimposed on the Co sites, showing that the anisotropic bonding directions correspond to the Co-Se bonds and therefore an  \( \left|e_{g}^{\pm}\right\rangle \)  orbital will bond with different strength depending on the sublattice. (C) Mapping of the  \( CoNb_{4}Se_{8} \)  lattice into a simpler lattice by removing the Nb atoms and some of the Se atoms.
 Se atoms.

## Supplementary Text

## Tight-binding model and Symmetry-Constrained Adaptive Basis (SCAB)

We derive a symmetry-constrained adaptive basis for NRSS in a g-wave altermagnet by finding a basis of the  \( \ell=2 \)  Hilbert space where the crystal field Hamiltonian is diagonal in both sublattices. The basis is derived by ensuring that the action of  \( C_{6z} \)  (or other representatives of the opposite-spin sublattice symmetry coset) simply exchange diagonal elements of the crystal field Hamiltonian. This property of the SCAB can be seen in the crystal field Hamiltonians of sublattices I and II in Eqs. (S8) and (S9), as discussed later in this section. The systematic derivation properties of SCABs for general altermagnets will be the topic of upcoming work.

We then use the SCAB to construct a tight-binding model (TBM) to better understand NRSS in  CoNb}_{4}Se}_{8} . An intuitive formulation for a TBM should include d orbitals from the magnetic ions and capture the crystal field effects. In addition, as recently recognized for d-wave altermagnets 54 , it is important that the hopping energies of the orbitals involved in the crystal field splitting \left(\left|e_{g}^{\pm}\right\rangleight.  and  \left.\left|e_{g}^{\prime\pm}\right\rangle\right)  to be anisotropic and also respect the sublattice transpose symmetries \left(C_{6z}\right.  and  M_{z} ). More concretely, the hopping between the  \left|e_{g}^{\pm}\right\rangle  and  \left|e_{g}^{\prime\pm}\right\rangle  orbitals with a neighboring site should differ, and the hopping from one of these orbitals along a particular direction should be the same as the hopping of the other orbital along that direction rotated by  60^{\circ}  or mirrored across the xy plane. By looking at the shape of these orbitals (Fig. S5A), it is clear that for the hoppings to show such anisotropy, their directions should be along the lobes of the  \left|e_{g}^{\pm}\right\rangle  and  \left|e_{g}^{\prime\pm}\right\rangle  orbitals. By looking at the real space lattice of  CoNb}_{4}Se}_{8}  (Fig. S5B), one notices that these directions correspond to the bonds between Co and Se atoms. Therefore, our TBM should also include orbitals from the Se sites.

Since the above ingredients should be enough to describe NRSS with g-wave symmetry, we can formulate our TBM in a simpler lattice than  CoNb}_{4}Se}_{8}  as long as all symmetries are preserved. Fig. S5C depicts the lattice of  CoNb}_{4}Se}_{8}  and a lattice where the Nb and some Se atoms have been removed. One can easily see that the main features needed for our model are preserved, that is, the alternating octahedral coordination between sublattices and the bonding directions between magnetic and nonmagnetic atoms. It is worth noting that this simpler lattice corresponds to the actual lattice structure of other altermagnetic materials in the same spin point group as  CoNb}_{4}Se}_{8} , such as MnTe or CrSb 98 . In this manner, our TBM is defined in the unit cell shown in Fig. S6, and includes two magnetic (M) sites and two ligand (L) sites. The fractional coordinates  \mathbf{r} = (x, y, z)  read

 \[ \begin{aligned}M_{\mathrm{I}}&=(0,0,0)\\M_{\mathrm{II}}&=(0,{0},{1}/{2})\\L_{\mathrm{I}}&=(1/4,1/4,1/{4})\\L_{\mathrm{II}}&=(3/4,3/4,3/{4}).\end{aligned} \]
 

Figure S6. Unit cell of the tight-binding model, with the sublattices, vectors and coordinate axes identified. Numbers  i = 1 - 6  indicate the neighbors of each ligand site j = I, II used to define the hoppings, denoted by  t_{ij}^{ML} .

While we use the SCAB basis in our TBM, it also possible to employ a basis of d orbitals (the real-valued or cubic spherical harmonics with  \ell=2 ). As shown below this is in fact useful to define the interactions (hoppings) between M and L sites. The relationship between these basis is:

 \[ \begin{pmatrix}e_{g}^{l+}\\ e_{g}^{s}\\ a_{1g}\\ e_{g}^{+}\\ e_{g}^{-}\end{pmatrix}=P_{SCAB\gets d}\begin{pmatrix}d_{xy}\\ d_{x^{2}-y^{2}\\ d_{xz}\\ d_{yz}\\ d_{z^{2}}\end{pmatrix}, \quad (S2) \] 

with

 \[ P_{SCAB\gets d}=\frac{1}{\sqrt{6}}\mathrm{diag}\left(e^{i\pi/3},e^{-i\pi/3},1,1,1\right)\begin{pmatrix} \] \begin{pmatrix}i\sqrt{2}&-\sqrt{2}&1&i&0\\i\sqrt{2}&-\sqrt{2}&1&-i&0\\0&0&0&0&\sqrt{6}\\-i\sqrt{2}&\sqrt{2}&1&i&0\i\sqrt{2}&\quad \sqrt{2}&1&-i&0\end{pmatrix}. \quad (S3) \] 

We define the Hamiltonian as

 \[ \mathcal{H}=\mathcal{H}_{0}+\mathcal{H}_{CF}+\mathcal{H}_{AFM}, \quad (S4) \] 

where the first term is the nearest-neighbor hopping between M and L sites, the second term is the crystal field and the last term is an effective antiferromagnetic e. Explicitly, they take the form:

 \[mathcal{H}_{0}=\sum_{i,\tau}c_{i\}&\epsilon_{i\tau}^{M}c_{i\tau}+\sum_{i,\tau}b_{i\epsilon_{i\tau}^{L}b_{i\tau}+\sum_{\langle i,j\rangle,\tau,\tau^{\prime}}c_{i\tau}^{\dagger}[t_{ij}^{ML}]_{\tau\tau^{\prime}}b_{j\tau^{\prime}}+H.C \quad (S5) \] 

 \[ \mathcal{H}_{CF}=\sum_{i,\tau,\tau^{\prime}}c_{i\tau}^{\dagger}[\Delta_{i}]_{\tau\tau^{\prime}}c_{i\tau^{\prime}} \quad (S6) \] 

 \[ \mathcal{H}_{AFM}=m_{AFM}\sum_{i,s,s^{\prime}}c_{is}^{\dagger}[\mathbf{m}_{i}\cdot\mathbf{s}]_{ss^{\prime}}c_{is^{\prime}}. \quad (S7) \]
 

Here,  c^{\dagger}\left(b^{\dagger}\right)  and  c\left(b\right)  are creation and annihilation operators acting on the M (L) site, respectively. Sites are labeled by the i and j indices,  \langle\rangle  denotes nearest-neighbor interaction and  \tau  and s are orbital and spin indices, respectively.

Next, let us define in more detail each term of the Hamiltonian. Starting from the antiferromagnetic interaction, which denotes the coupling of conduction electrons with local magnetic moments  m_{i}  with strength  m_{AFM} , we take  \mathbf{m} = + (0, 0, \hat{\mathbf{z}})  for sublattice I and  \mathbf{m} = -(0, 0, \hat{\mathbf{z}})  for sublattice II, as this corresponds to the magnetic order in  CoNb_{4}Se_{8} . The crystal field term captures the orbital splitting shown in Fig. 1C in the main text and the PDOS from Fig. S4. Employing the SCAB, the crystal field is just a diagonal matrix with different onsite energies at the different orbitals:

 \[ \Delta_{\mathrm{I}}=\mathrm{diag}\left(\frac{3\delta_{\mathrm{I}}}{5},\frac{3\delta_{\mathbf{I}}}{5},-2\delta_{\mathbf{I}}}{3},-\frac{2\delta_{\mathbf{2}}}{5},-\frac{2\delta_{\mathbf{3}}+\frac{\delta_{\mathbf{2}}}{5},-\frac{2\delta_{\mathbf{I}}}{3}+\frac{\delta}{5}\right). \quad (S8) \] 

Here,  \delta_{I} > 0  is the crystal field corresponding to the octahedral coordination and  \delta_{2}  models trigonal distortionwith  \delta_{2} < 0  for a trigonal elongation along the c axis, as in  CoNb_{4}Se_{8} . Importantly, the crystal field of sublattice II is simply

 \[ \Delta_{\mathrm{II}}=\mathrm{C}_{6z}^{+}\Delta_{\mathrm{I}}\mathrm{C}_{6z}=M_{z}^{\dagger}\Delta_{\mathrm{I}}M_{z}=} After \left(-\frac{2\delta_{\mathrm{I}}}{5}+\frac{\delta_{\mathrm{2}}}{3},-\frac{2\delta_{\mathrm{I}}}{5}+\frac{\delta_{\mathrm{2}}}{3},-\frac{2\delta_{\mathrm{I}}}{5}-\frac{\delta_{\mathrm{2}}}{5},-\frac{3\delta_{\mathrm{I}}}{5},\frac{3\delta_{\mathrm{I}}}{5}\right). \quad (S9) \] 

These expressions show that, with the choice of an appropriate basis (SCAB), the crystal field potential swaps the orbital energies at the two opposite sublattices and therefore correctly reproduces the orbital splitting shown in the main text (Fig. 1C).

Finally, the onsite energies of the M and L sites and by the hoppings between said sites. To define the hopping terms, we resort to the tabulated Slater-Koster overlap integrals between two pair of orbitals at neighboring sites i and  j^{99} . In this way, given an L site and its six M neighbors (Fig. S6), one can define six different hoppings. The simplest and most efficient way is to use the SlaterKoster to define only one of those hoppings, and then obtain the rest by applying symmetry operations. For example, we define the hopping  t_{ij}^{ML} = t_{ij}^{ML'}  as the hopping from the L site in sublattice I to the M site labeled as 1 in Fig. S6. Since the SlaterKoster integrals are better defined in cubic harmonics, we first represent the hoppings in such basis and then convert them using Eq. (S2) into the SCAB. Also, besides the five d orbitals for the M sites, we choose a single  p_{z}  orbital for the L sites for concreteness and simplicity. Hence,

 \[ \left|\Psi\right\rangle=\left(p_{z}^{I}\quad p_{z}^{II}\quad d_{xy}^{I}\quad d_{x_{2}-y^{2}}^{I}\quad d_{xz}^{I}\quad\ d_{yz}^{I}\quad d_{z^{2}}^{I}\quad d_{xy}^{II}\quad d}_{x_{2}-y^{2}}^{II}\quad d_{xz}^{II}\qquad d_{y_{z}}^{III}\quad d_{z2}^{III}\right)^{T}\otimes\left(\uparrow\right), \quad (S10) \] 

and

 \[ \begin{align*}t_{II}^{ML}&=\left(\langle d_{xy}^{\mathrm{II}}|\mathcal{H}|p_{z}^{\mathrm{I}}\rangle\quad\langle d_{x_{2}-\mathrm{y}^{2}}^{\mathrm{II}}|\mathcal{H}|p_{z}^{\mathrm{I}}\rangle\quad\langle d_{xz}^{\mathrm{II}}|\mathcal{H}\rangle\quad\langle d}_{\mathrm{z}}^{\mathrm{II}}|\mathcal{H}|p_{z}^{\mathrm{I}}\rangle\quad\langle d_{xz}^{\mathrm{II}}|\mathcal{H}|p_{z}^{\mathrm{I}}\rangle\right)^{T}\\&=\left(0\quad\frac{\sqrt{3}}{2}l^{2}nV_{\sigma}-l^{2}nV\pi\quad\sqrt3}ln^{2}V_{\sigma}+l(1-2n^{2})V_{\pi}\quad0\quad n(n-\frac{l^{2}}{2})V_{\sigma}+\sqrt{3}l^{2}nV_{\pi}\right)^{T}\otimes\left(\uparrow\right),\end{align*} \quad (S11) \] 

where  V_{\pi}  and  V_{\sigma}  are the parametrizations of the  \pi  and  \sigma  chemical bonds, and l, m and n are the direction cosines for the x, y and z Cartesian directions, respectively, of the  t_{II}^{ML} hopping (e.g. l is related to the angle between  t{T}  and the x)}. Having defined this hopping term, the rest are straightforwardly obtained as

 \[ \begin{align*}t_{2I}^{ML}&=t_{II}^{ML}C_{3z},\ t_{3I}=t_{2L}^{ML}C_{3z},\ t_{4I}^{ML}=t_{1I}^{ML}M_{z},\ t={}C_{3z},\ t_{6I}=t_{3I}^{ML}M_{z},\\t_{{II}}^{ML}=t_{6I}^{ML}C_{6z},\ t_{2II}^{ML}=t_{5I}^{ML}C_{6z},\ t_{3II}^{ML}=t_{4I}^{ML}C_{6z},\ t_{4II}^{ML}=t_{3I}^{ML}C_{6z5II}^{ML}=t_{2I}^{ML}C{t_{1I}^{ML}},\end{align*} \quad (S12) \] 

where  C_{3z}  is a three-fold rotation about the z axes. Regarding the onsite energies,  \varepsilon_{i\tau}^{MI}  encodes the energies of each d orbital, while  \varepsilon_{i\tau}^{E}  describes the energy of the  p_{z}  orbitals.

To confirm our earlier intuition that hoppings along two directions related by a  C_{6z}  or  M_{z}  operation should interchange the hybridization of their  \left|e_{g}^{\pm}\right\rangle  and  \left|e_{g}^{\prime\pm}\right\rangle  orbitals, we now compare the absolute value of each term for the hoppings  \left|t_{1I}^{ML}\right|  and  \left|t_{4I}^{ML}\right|  (see Fig. S6), which are related by  M_{z} . In the SCAB, one obtains

 \[ \begin{align*}t_{1I}^{ML}&=\left(\left\langle e_{g}^{\prime+}\right|.\mathcal{H}\left|p_{z}^{\mathrm{I}}\right\rangle\quad\left\langle e_{g}^{\prime-}\right|.\mathcal{H}\left|p_{z}^{\mathrm{I}}\right\rangle\quad\left\langle a_{1\mathrm{g}}\right|.\mathcal{H}\left|p_{z}^{\mathrm{I}}\right\rangle\quad\left\langle e_{g}^{\mathrm{+}}\right|.\mathcal{H}\left|p_{z}^{\mathrm{I}}\right\rangle\right)^{T}\\&=\left(\boldsymbol{\alpha}\quad\boldsymbol{\alpha}\quad\boldsymbol{ \beta}\quad\boldsymbol{\gamma}\quad\boldsymbol{\gamma}^{\mathrm{T}}\right.\\&t_{4I}^{ML}=\left(\left\langle e_{g}^{\prime+}\right|.\mathcal{H}\left|p_{z}^{\mathrm{I}}\n\right\rangle\quad\left\langle e_{g}^{\prime-}\right|.\mathcal{H}\left|p_{z}^{\mathrm{I}}\right\rangle\quad\left\langle a_{1\mathrm{g}}\right|.\mathcal{H}\left|p_{z}^{\mathrm{I}}\right\rangle\quad\left e_{g}^{\mathrm{+}}\right|.\mathcal{H}\left|p_{z}^{\mathrm{I}}\right\rangle\right)^{T}\\&=\left(\boldsymbol{\gamma}\quad\boldsymbol{\gamma}\quad\boldsymbol{ \beta}\quad\boldsymbol{\alpha}\quad\boldsymbol{\alpha}^{\mathrm{T}}\right.\\ \end{align*} (S13) (S14)\]
 

![](./images/1070588194879176733_32.jpg)

Figure S7. Band structure of Eq. (S4) using the parameters described in the text calculated from the TBM. Solid pink (dashed blue) bands correspond to spin up (spin down).

with

 \[ \begin{aligned}&\alpha=\frac{1}{2\sqrt}}\left|l\left(2lnV_{\pi}+\left(1-2n^{2}\right)\sqrt{2}V_{\pi}+n\left(\sqrt{2}n-l\right)V_{\sigma}\sqrt{3}\right)\right|,\\&\beta=\left|V_{\sigma}n^{3}+\left(\sqrt{3}V_{\pi}-\frac{V_{\sigma}}{2}\right)l^{2}n\right|,\\&\gamma=\frac{1}{2\sqrt{3}}\left|l\left(\left(\sqrt{2}-2n\left(l+n\sqrt{2}\right)\right)V_{\pi}+\sqrt{3}n\left(l+n\sqrt{2}\right)V_{\sigma}\right)\right|,\\ \end{aligned} \quad (S15) \] 


therefore demonstrating that the  e_{g}^{\pm}  and  e_{g}^{\prime\pm}  orbitals swap their hopping magnitude upon a sublattice transposing symmetry. We note that the explicit terms  \alpha}  and  \gamma  derived here corresponds to the  t}_{1}  and  t}_{2}  hoppings used in the main text.

With each Hamiltonian term understood, one can Fourier transform Eq. (S4) to plot the band structure as shown in the main text. We plot in Fig. S7 the band structure of Eq. (S4) for up and down spins. We use the following parameters, which are the same used for Fig. 2D-F in the main text, but here we show all bands at all energies rather than a narrower energy window. We take  V_{\sigma} = -1  as a reference value and use  |V_{\sigma}|  as a unit. Then we take  V_{\pi} = -0.7 ,  \delta_{1} = 1.2 ,  \delta_{2} = -0}.2  and  m_{AFM} = 0.2 , where  \delta}_{1}  is positive so  |e_{g}^{\prime\pm}\rangle  have higher energy at sublattice I,  \delta_{2}  to denote an elongation distortion of the octahedron, and  m_{AFM}  is positive so sublattice I has magnetization parallel to  +2 . The value of the exchange interaction are chosen smaller than the crystal field so it is clear the parent bands (i.e. not spin-split) of each pair of spin-split bands (see Fig. 2E-F in the main text). Since for  CoNb}_{4}Se}_{8} , the angle between  t_{1}^{ML}  and the x axis is approximately  37^{\circ} , we take  l = \cos\left(37\frac{\pi}{180}\right) ,  n = \cos\left(53\frac{\pi}{180}\right) . Finally, we set the onsite energies of all d orbitals to zero,  e_{i\tau}^{M} = 0 \forall i, \tau , and the onsite energy for the ligand  p_{z}  orbitals to  e_{i\tau}^{L} = -2 \forall i, \tau .

## Supplementary Figures

## 3D electronic structure of CoNb_{4}Se_{8}

Here in Fig. S8 we demonstrate that altermagnetic spin-splitting occurs away from time-reversal invariant momenta (TRIMs). Along high symmetry directions, i.e.  \Gamma-K  and  \Gamma-M , the spin-splitting in the Fermi surface (Fig. S8A) changes sign, implying a zero crossing at these TRIMs. More explicitly, the DFT band structure along  k_{z}=0  (Fig. S8B) has spin degeneracy, whereas at  k_{z}=c^{*}/4  (Fig. S8C), there is significant spin-splitting, confirming previous predictions ^{10} .
 

A

![](./images/1070588194879176733_33.jpg)

D

![](./images/1070588194879176733_34.jpg)

B

![](./images/1070588194879176733_35.jpg)

E

![](./images/1070588194879176733_36.jpg)

C

![](./images/1070588194879176733_37.jpg)

F

./images/1070588194879176733_38.jpg)

Figure S8. 3D Electronic Structure of CoNb4Se8 (A) Fermi surface CoNb4Se8 , calculated using spin-polarized DFT (B, C). Calculated spin-polarized band structure along  \Gamma-M-A-L  plane for  k_{z}=0  (B) and  k_{z}={c^{*}}/{4}=\pi/(2c)  (C). Spin-up (-down) bands are shown in solid pink (dashed blue) and the Fermi level is set to 0 eV and marked with a dashed link. (D) ARPES Fermi surface cuts along  \Gamma-M-A-L  plane, (E) corresponding  E_{F}  MDCs along the M-L direction. peak locations extracted from Lorentzian peak fit indicated by by red and blue ticks. (F) splitting along the M-L direction, extracted from peak locations in E. Blue dashed curve corresponds to a sinusoidal fit to the splitting as a function of out of plane momentum  k_{z} . Red arrows indicate  k_{z}^{\prime}  value for data presented in the main text.
 
In fact, this behavior is reflected in the experimental 3D electronic structure of  CoNb_{4}Nb}_{4}Se}_{8}  as measured in ARPES at 13K. Along the BZ edge the ARPES spectra (Fig. S8D) present a pair of electron pockets whose size varies with out of plane momentum  k_{z} . This is clear from momentum distribution curves (MDCs) presented in Fig. S8E near the zone edge, display a pair of peaks whose splitting oscillates in two full periods while traversing along  k_{z} . This oscillatory splitting behavior, summarized in Fig. S8F, reasonably fits to the function  s_{0} + s_{1} \sin^{2}(2\pi k_{z}c^{*}) , where  s_{0} = 0.12 \, \AA^{-1}  is the residual momentum splitting from, e.g. spin orbit coupling, and  s_{1} = 0.03 \, \AA^{-1}  is the altermagnetic splitting which oscillates with momentum. Here we find  c^{*} \approx 0.8 \, \AA^{-1}  corresponding to a c axis length of  7.8 \, \AA , which is within 50% of the experimentally determined  c = 12.4 \, \AA . Higher resolution data along the  k_{z}  direction would certainly address this discrepancy.

Combined with the findings in the following section, it is clear that a combination of factors contributes to the overall spin texture of  }  at low temperature, which is discussed further in the main manuscript.

## Persistence of Spin Polarization above  T_{N} 

Similar to NRSS, relativistic spin splitting can occur at the surface with nonzero spin-orbit coupling 100 , manifesting as a spin texture that alternates upon inverting parallel momentum. Here, we present 200K ARPES spectra of  CoNb}_{4}Se}_{8}  in (Fig. S9) along the momentum direction  M^{\prime\prime}-I^{\prime}-M^{\prime} . Similar to the low temperature data presented in the main text, the 200 K spectra (Fig. S9A, B) also exhibit two electron pockets at the BZ edge with a similar depth and momentum splitting near  E_{F} .

Above  T_{N} , energy distribution curves (EDCs) at momentum  k}_{1}  (Fig. S9C) still display spin polarization. States polarized along the +c direction are shifted closer to the Fermi level by  60 \pm 30  meV than those along -c. By contrast, at momentum  k}_{2} = C_{2}(k_{1}) = C_{6}^{3}(k_{1}) , the spin splitting is inverted: states polarized along +c are now  100 \pm 30  meV further from  E_{F} . Fig. S9D summarizes this alternating spin splitting in  CoNb}_{4}Se}_{8} , which is within error bars of the magnitude seen in the altermagnetic phase. As discussed in the main text, altermagnetic ordering drives an increase in the presence of spin-split electronic states at the Fermi level. We attribute this spin splitting to that which exists in the parent compound  NbSe}_{2}  upon local inversion symmetry breaking 68 .

## Collinear Antiferromagnetic Order in CoNb_{4}Se_{8}

Fig. S10 presents the temperature-dependent magnetic susceptibility of  CoNb_{4}Se_{8}  as a function of applied magnetic field  \vec{B} , on the same sample as reported in ref 52 . When  \vec{B}|| , the susceptibility  (\chi_{c})  exhibits a sharp decrease below 168 K, whereas when  \vec{B}  is along the ab-plane, the susceptibility  \chi_{ab}  manifests a kink at 168 K followed by a gradual and modest increase at lower temperatures. This behavior is characteristic of textbook antiferromagnetic ordering with moments aligned parallel to the c-axis, with a Néel ordering temperature of 168 K 101 .
 

A

![](images/1070588194879176733_39.jpg)

B

![](./images/1070588194879176733_40.jpg)

C

![]images/1070588194879176733_41.jpg)

D

![](./images/1070588194879176733_42.jpg)

Figure S9. ARPES Measures Spin-Split Occupied Electronic Structure in  \ (CoNb_{4}Se_{8} \)  above  \( T_{N} \) . ( (A,B) 200K ARPES spectra along electron pockets surrounding  \( M^{\prime\prime} \equiv C_{6}^{3}(M^{\prime}) \)  (A) and  \( M^{\prime} \)  (B). (C) spin-resolved EDCs spectra along momenta indicated by black (white) vertical lines in A (B). Red (blue) ticks indicate peak locations for bands polarized spin up (down). (D) Altermagnetic splitting, extracted from the difference in spin up and spin down band locations in c,d.
 

![](./images/1070588194879176733_43.jpg)

Figure S10. Collinear Antiferromagnetic Order in  \( CoNb_{4}Se_{8} \) . (A) Magnetic susceptibility measured in a magnetic field of 0.1 T applied along c-axis ( \( \chi_{c} \) ) and within the ab-plane ( \( \chi_{ab} \) ), for the same sample as reported in Ref \( ^{52} \) .
 
