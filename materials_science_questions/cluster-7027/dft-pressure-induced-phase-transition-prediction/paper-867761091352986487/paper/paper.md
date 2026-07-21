
# Double-layer ice from first principles

Ji Chen, \( ^{1,*} \)  Georg Schusteritsch, \( ^{2} \)  Chris J. Pickard, \( ^{2,3} \) 

Christoph G. Salzmann, \( ^{4} \)  and Angelos Michaelides \( ^{1,\dagger} \) 

 \( ^{1} \) Department of Physics and Astronomy,

London Centre for Nanotechnology,

Thomas Young Centre, University College London,

Gower Street, London WC1E 6BT, U.K.

 \( ^{2} \) Department of Materials Science and Metallurgy, University of Cambridge,

27 Charles Babbage Road, Cambridge CB3 0FS, U.K.

 \( ^{3} \) Advanced Institute for Materials Research,

Tohoku University 2-1-1 Katahira, Aoba, Sendai, 980-8577, Japan

 \( ^{4} \) Department of Chemistry, University College London,

20 Gordon Street, London, WC1H 0AJ, U.K.

## Abstract

The formation of monolayer and multilayer ice with a square lattice structure has recently been reported on the basis of transmission electron microscopy experiments, renewing interest in confined two dimensional ice. Here we report a systematic density functional theory study of double-layer ice in nano-confinement. A phase diagram as a function of confinement width and lateral pressure is presented. Included in the phase diagram are honeycomb hexagonal, square-tube, hexagonal-close-packed and buckled-rhombic structures. However, contrary to experimental observations, square structures do not feature: our most stable double-layer square structure is predicted to be metastable. This study provides general insight into the phase transitions of double-layer confined ice and a fresh theoretical perspective on the stability of square ice in graphene nanocapillary experiments.
 

## I. INTRODUCTION

Recently, experimental evidence for the formation of two dimensional (2D) ice with a novel lattice structure in graphene nanocapillaries was reported. \( ^{1} \)  Specifically, transmission electron microscopy (TEM) measurements showed that 2D ice appears as a layered structure with a square arrangement of oxygen atoms. Individual layers are located directly on top of each other in an AA stacking manner, and the thickest structures observed consisted of three layers. However, the interpretation of the observations has been questioned and it has even been suggested that the square lattice structure observed is not that of ice but rather sodium chloride, a common contaminant. \( ^{2-4} \)  These observations and discussions have inspired great interest in further investigating confined 2D ice using advanced experimental and computational techniques.

Ab initio methods such as density functional theory (DFT) and quantum Monte Carlo (QMC) have recently been used to examine the stability of 2D ice structures. These studies have significantly improved our understanding of 2D ice, particularly monolayer 2D ice. \( ^{5-9} \)  For example, in previous studies we have predicted a pentagonal monolayer 2D ice structure and found that monolayer square ice is stable at high pressure, lending support to the measurements of Algara-Siller et al. \( ^{1} \)  In addition, the benchmark-quality QMC data has shed light on the accuracy of force field (FF) models and DFT functionals. \( ^{9} \)  For instance, SPC/E \( ^{10} \)  and TIP4P \( ^{11} \)  type models were found to overbind high density 2D ice phases. Meanwhile, several exchange-correlation (XC) functionals, in particular the rPW86-vdW2, \( ^{12} \)  were identified that predict relatively correct binding energies for both 2D and 3D ice. This suggests that DFT can be used in further investigations of confined ice beyond the monolayer.

Apart from monolayer 2D ice, double-layer ice is of great importance to the questions surrounding square ice as it was also observed in the experiments of Algara-Siller et al.. However, due to the possibility of forming interlayer hydrogen bonds a simple extension of monolayer ice phase diagram to the double-layer would be inappropriate. Indeed, double-layer ice has been discussed in many FF studies, yet observations were quite sensitive to the FF model and computational setup used. \( ^{1,7,13-25} \)  While double-layer ice with the AA stacking observed in experiments has been formed in some simulations, \( ^{1,24} \)  many other studies have reported different structures. Bearing in mind that these FFs encounter problems for monolayer ice, \( ^{9} \)  question marks have to be raised regarding their performance for double-
 

layer ice. Therefore, a systematic DFT study of double-layer ice using reliable DFT XC functionals is needed. In particular the stacking order and the interlayer interaction in 2D ice are yet to be investigated. With this in mind, herein we report a DFT study aimed at exploring double-layer ice phases under confinement. The aims are to establish the stability of various double-layer ice structures as a function of lateral pressure and width of confinement, and to shed light on the experimental observation of AA stacking square ice.

The remainder of this paper is organised as follows. Section II describes the details of various DFT calculations. Section III reports and discusses the main results, wherein: (i) we propose a phase diagram for double-layer ice at 0 K as a function of confinement width and pressure up to 5 GPa; and (ii) we discuss the stability of double-layer square ice. In section IV we provide a brief summary of our results.

## II. SIMULATION DETAILS

We have carried out ab initio random structure searches (AIRSS) \( ^{26} \)  using two different schemes: (i) A fully random structure search with 8, 12, and 24 water molecules per unit cell; and (ii) A limited random structure search starting with hexagonal, pentagonal, square and HCP lattices containing randomly orientated water molecules. For the latter approach 12 water molecules were considered for the hexagonal unit cell, 24 for the pentagonal cell, 8 and 18 for the square and HCP lattices, respectively. Periodic boundary conditions were used with two layers of ice and a vacuum region outside the ice layers. K-point sampling was used with Monkhorst-Pack grids with a lateral separation between points larger than  \( 0.03 \, \AA^{-1} \) . The lateral cell dimensions were relaxed until the lateral stress tensor converged to the target lateral pressures (0 - 5 GPa). The cell dimension perpendicular to the slab was fixed during structure optimization. DFT calculations were performed using the Vienna Ab initio Simulation Package (VASP) where the core electrons were described with projector augmented wave (PAW) potentials. \( ^{27,28} \)  An energy cut-off of 550 eV was used in the structure search and phase diagram calculations. The absolute binding energy values referred to in the text and reported in the tables are calculated using hard PAW potentials in conjunction with a 1000 eV cut-off. The bulk of the results are based on a non-local van der Waals inclusive XC functional rPW86-vdW2 (often known as vdW-DF2). \( ^{12} \)  This functional, as implemented in VASP by Klimeš et al., \( ^{29} \)  has proved to be suitable for pre-
 

dicting the binding of monolayer and bulk ice phases. \( ^{9,30} \)  Nevertheless, the optPBE-vdW and optB88-vdW functionals, \( ^{29,31} \)  the Perdew-Burke-Ernzerhof (PBE) functional \( ^{32} \)  and the Heyd-Scuseria-Ernzerhof (HSE) hybrid functional \( ^{33,34} \)  with the van der Waals correction of Tkatchenko and Scheffler \( ^{35} \)  (PBE+vdW(TS), HSE+vdW(TS)) have also been tested for some specific structures.

The confinement was not modelled by explicit graphene sheets but rather with a uniform 2D confining potential. Specifically a Morse potential was fitted to QMC results for the interaction of a water monomer with graphene. \( ^{36} \)  The potential  \( V(z) = D((1 - e^{-a(z - z_0)})^2 - 1) \) , where z is the distance between the oxygen atom and the wall,  \( D = 57.8 \, meV \) ,  \( a = 0.92 \, \AA^{-1} \) ,  \( z_0 = 3.85 \, \AA \) . More details on this confining potential can be found in Ref. 5 and the supplemental material. \( ^{37} \)  Calculations of 2D ice confined within actual sheets of graphene have also been performed to estimate the optimal separation of graphene layers as discussed below.

The binding energy is defined as,

 \[ E_{\mathrm{b}}=E_{\mathrm{H}_{2}\mathrm{O}}^{\mathrm{t o t}}-E_{\mathrm{i c e}}^{\mathrm{t o t}}/n_{\mathrm{H}_{2}\mathrm{O}}, \quad (1) \] 

where  \( E_{H_{2}O}^{tot} \)  is the total energy of a water molecule in vacuum,  \( E_{ice}^{tot} \)  and  \( n_{H_{2}O} \)  are the total energy and number of water molecules in the 2D ice structures. The enthalpy is defined as,

 \[ H=E_{\mathrm{i c e}}^{\mathrm{t o t}}+E_{\mathrm{c o n f i n e m e n t}}+P\times A\times h, \quad (2) \] 

where  \( E_{confinement} \)  is the energy in the confinement potential, A is the lateral area, h is the layer height which equals the width of the confinement w, and P is the lateral pressure. \( ^{38} \) 

Some short ab initio molecular dynamics (AIMD) simulations were also carried out with a view to understand the possible role of anharmonic effects. These simulations were performed within the canonical ensemble at a target temperature of 300 K using a Nosé-Hoover thermostat. \( ^{39} \)  Each simulation was performed with a time-step of 0.5 fs for a total of 10 ps. Of these 10 ps, the first 3 ps were used for equilibration and analysis was performed on the remaining 7 ps. The phonon densities of states were also calculated through Fourier transformation of the velocity auto-correlation function from these molecular dynamics trajectories.
 

## III. RESULTS AND DISCUSSIONS

## A. Structures and binding energies of double-layer ice at ambient pressure

We start our discussion by looking at the most relevant double-layer ice structures and their binding energies at ambient pressure (Fig. 1, Table I). They have initially been obtained with a confinement of 9.5 Å and re-optimized after the confinement is removed. The most stable is a hexagonal structure, which consists of two layers of 2D honeycomb lattice that locate directly on top of an another with AA stacking (Fig. 1a). The hexagonal structure has been observed quite often in force field studies, \( ^{[13,17-20,40]} \)  and has also been suggested experimentally on a metal supported graphene surface. \( ^{[41]} \)  Second most stable is a double-layer pentagonal structure (Fig. 1b), reminiscent of a Cairo tiling pattern. This structure was first observed by Johnston et al. through quenching of liquid water using both the mW and TIP4P/ice water models. \( ^{[18]} \)  Similarly, a monolayer pentagonal structure was predicted in our previous DFT study. \( ^{[5]} \)  The monolayer pentagonal ice has a vanishing energy difference to the monolayer hexagonal phase. \( ^{[9]} \)  Surprisingly, we find that the double-layer pentagonal structure is 25 meV/H \( _{2} \) O less stable than the hexagonal double-layer. Following these two we have the square-tube phase (Fig. 1c), the hexagonal-close-packed (HCP) phase (Fig. 1d), and the double-layer square structure (Fig. 1e). The double-layer square structure is a new structure identified in the current AIRSS study. As with the hexagonal, pentagonal, square-tube, and HCP structures the double-layer square structure is held together with interlayer hydrogen bonds in an AA stacking arrangement. This double-layer AA stacked square ice structure is a candidate for the AA stacked structure observed in experiments. \( ^{[1]} \)  It is the most stable double-layer square ice structure identified in our structure searches using both the 8 and 18 water molecule unit cells. It has a binding energy of 511 meV/H \( _{2} \) O, being less stable than the most stable hexagonal structure by 37 meV/H \( _{2} \) O. Apart from the above structures, Fig. 1f also shows a double-layer buckled-rhombic structure. The interlayer interaction in this structure is mediated by van der Waals forces and it is free of interlayer hydrogen bonds. The buckled-rhombic phase is only stable under confinement. We will have more to say about this structure later. We note that all the structures identified here are non-polar, and in this study the potential impact of an external electric field is not considered. \( ^{[42,43]} \)
 
![](./images/867761091352986487_1.jpg)

FIG. 1. Double-layer ice structures. Side and top views of the (a) hexagonal (honeycomb), (b) pentagonal, (c) square-tube, (d) hexagonal-close-packed (HCP), (e) square and (f) buckled-rhombic double-layer structures. Red and white spheres represent oxygen and hydrogen atoms, respectively. The blue boxes in the top views show the unit cells used in the periodic DFT calculations. All the structure files are provided in the supplemental material. \( ^{37} \) 

## B. Phase transitions of double-layer ice

Examining the phase transitions at different confinement widths is desirable as the phase stability of confined ice is sensitive to the width of confinement. \( ^{5,15,16,19,44} \)  However, since a confinement that mimics graphene nanocapillaries is particularly interesting we first established what the appropriate confinement width for graphene is by examining the total energy of a double-layer ice film within two layers of graphene (Fig. 2). These calculations show that the optimal width of confinement is around 9.5 Å. This is the main reason our structure searches were performed at 9.5 Å confinement. However we also examined the stability of the relevant ice structures at a broader range of confinement. Fig. 3 shows the relative enthalpy with respect to the square-tube structure for confinements between 8.5 and 11.0 Å. At confinement widths of 8.5 and \(9.0\ \AA\), just a single transition is observed from the hexagonal to the HCP structure at about 0.5 GPa. At \(9.5\ \AA\) the hexagonal structure is still the most stable structure below ca. 0.5 GPa. However, the square-tube structure becomes more stable than the HCP structure, leading to a new phase transition from the hexagonal to
 

<table><tr><td>Structure</td><td>\( E_{b} \)  (meV/H \( _{2} \) O)</td><td>A ( \( \textup{\AA}^{2} \) /H \( _{2} \) O)</td><td>d ( \( \textup{\AA} \) )</td></tr><tr><td>Hexagonal</td><td>548/575</td><td>10.10/9.76</td><td>2.85/2.80</td></tr><tr><td>Pentagonal</td><td>523/553</td><td>8.88/8.65</td><td>2.86/2.81</td></tr><tr><td>Square-tube</td><td>523/549</td><td>8.27/8.14</td><td>2.85/2.80</td></tr><tr><td>HCP</td><td>520/550</td><td>8.07/8.10</td><td>2.75/2.68</td></tr><tr><td>Square</td><td>511/538</td><td>8.49/8.40</td><td>2.86/2.80</td></tr></table>

TABLE I. Binding energies (Eq. 1) and structural information of double-layer ice structures at ambient pressure without confinement. Larger values for  \( E_{b} \)  suggest stronger binding. A is the lateral area per water molecule within a single layer. d is the average interlayer distance. Hexagonal represents the hexagonal honeycomb structure (Fig. 1a) and HCP represents the hexagonal-close-packed structure (Fig. 1d). Results using both the rPW86-vdW2 and optPBE-vdW functionals are reported (separated by a slash with rPW86-vdW2 in front).

![](./images/867761091352986487_2.jpg)

FIG. 2. Total energy profile of water confined within two perfectly flat sheets of graphene fixed at the separations shown. The dashed lines show the confinement width regime examined in this study. The inset shows the structural model used for this specific set of calculations, which involves 16 water molecules in a hexagonal double-layer ice structure confined between two 32 carbon atom graphene sheets. On the energy scale the energy minimum is set to zero.

the square-tube structure. The HCP structure is slightly more stable than the square-tube at pressures above ca. 1.5 GPa and transforms to the buckled-rhombic structure at ca. 5 GPa. The transition between these two high density double-layer ice phases has also been identified in Ref. 7. As the width of confinement increases: (i) the stability of the hexagonal structure is not altered; (ii) the HCP and square-tube structures have very similar stability
 

in a wide range of pressures, within which the square-tube structure is slightly preferred at wider confinements; and (iii) the transition pressure to the buckled-rhombic structure decreases, squeezing the stable region of the square-tube and HCP structures. Generally, the width dependency is strong for the HCP and buckled-rhombic structure whereas the relative stability of the hexagonal, pentagonal, square and square-tube phases barely changes at different confinement widths. This is not so surprising as the hexagonal, pentagonal, square and square-tube structures have the same number of interlayer hydrogen bonds and similar interlayer separations. The HCP structure is thinner and would be favored at narrow confinement whilst the buckled-rhombic structure is thicker and tends to appear in wider confinements.

The sequence of phase transitions at different confinement widths allows us to sketch a putative phase diagram for double-layer ice at 0 K as a function of pressure and confinement width (Fig. 4). In brief, double-layer ice appears as a hexagonal structure at low pressures ( \( \sim \)  0.5 GPa). This then transforms to the HCP structure at higher pressures for narrow confinement widths and to the square-tube structure for larger confinement widths. At higher pressures and larger confinement widths double-layer ice favors a buckled-rhombic structure.

## C. Stability of double-layer square ice

Contrary to the monolayer, our predicted phase diagram for double-layer ice does not have a regime in which square ice is stable, whereas it is the only stable ice structure identified so far that matches the TEM images in graphene nanocapillaries. \( ^{[45]} \)  Our calculations reveal that irrespective of the confinement width the square structure is always at least ca. 20 meV/H \( _{2} \) O less stable than the most stable structure (Fig. 3). This is consistent with another DFT study in which slightly different computational settings were used and double-layer square ice was also not identified as a stable phase. \( ^{[7]} \)  Intuitively the fact that the double-layer square phase is metastable is not so surprising by just comparing the square phase with the square-tube phase. Two steps can turn a double-layer square structure to a square-tube structure: changing the hydrogen ordering of the square phase and shifting the tubes by half a lattice unit. The re-ordering of hydrogen bonds is unlikely to cause a significant energy increase whereas the tube formation allows a further optimization step.
 
![](./images/867761091352986487_3.jpg)

![](./images/867761091352986487_4.jpg)

![](./images/867761091352986487_5.jpg)

![](./images/867761091352986487_6.jpg)

![](./images/867761091352986487_7.jpg)

![](./images/867761091352986487_8.jpg)

FIG. 3. Enthalpies (relative to square-tube) of the double-layer ice structures as a function of lateral pressure for different confinement widths. These are from (a) to (f): 8.5, 9.0, 9.5, 10.0, 10.5 and 11.0 Å. The enthalpies of the hexagonal and square phases and the pentagonal phase are only shown up to 1 GPa and 0.5 GPa, respectively, because they are structurally unstable above this. The unstable structures and additional data showing the instability of these phases is included in the supplemental material.

towards a more stable structure, the square-tube structure. However, due to the small energy differences between the different phases further calculations are needed to test this conclusion. Naturally it is reasonable to first consider the limitations of the simulations and to this end we specifically consider the following issues: (i) The accuracy of the underlying DFT calculations; (ii) The role of zero point energies; (iii) Finite temperature effects including harmonic and anharmonic phonon contributions; and (iv) Hydrogen ordering and the influence of configurational entropy. Each of these issues is addressed at a confinement width of 9.5 Å.
 
![](./images/867761091352986487_9.jpg)

FIG. 4. Schematic phase diagram of double-layer ice with respect to lateral pressure and confinement width. The phase diagram can be divided into four regions: (i) The hexagonal phase at low pressures; (ii) The HCP phase at high pressures and small confinement widths; (iii) The square-tube phase at pressures in the GPa regime and large confinement widths; (iv) The buckled-rhombic phase at high pressures and large confinement widths. The specific data points calculated are shown with the same set of symbols as in Fig. 3. Note that a logarithmic scale is used for pressure from 1 bar to 0.5 GPa and then a linear scale from 0.5 G Pa to 5 GPa. We note that the enthalpy difference between the HCP and square-tube structures is so small that the boundary between these two phases is not well defined from our calculations, from which we see a region (0.5 - 1 GPa, 9.5 - 10 Å) that the hexagonal, HCP and square-tube structures are intermixed. However, due to the fact that the HCP has smaller interlayer distance and higher lateral density than the square-tube, the transition boundary between them is more likely to have a positive slope as shown in the figure.

Sensitivity to exchange correlation functional: The first issue is the accuracy of DFT calculations specifically the XC functional used. The results reported so far have been obtained with the rPW86-vdW2 functional, which has proved to be accurate in predicting the binding energies of monolayer and bulk ice polymorphs. \( ^{9,30} \)  Nevertheless, it is also worth examining the results with other functionals. In Table I and Fig. 5a we report the binding energy, lattice parameter and enthalpy calculated using the optPBE-vdW functional. As shown in Fig. 5a, although the two functionals differ in their prediction of absolute binding energies and lattice parameters, the relative enthalpies between different phases mostly
 

agree. Importantly, the difference between the square structure and the stable structures are consistent for these two functionals. Specifically at 1 GPa, the pressure regime at which square ice is estimated to form, \( ^{1} \)  the square-tube structure has a lower enthalpy by ca. 19 meV/H \( _{2} \) O than the square structure.

There are, of course, many other XC functionals we could consider. \( ^{46} \)  Focusing on 1 GPa we have explored how several other functionals perform, including those with a different treatment of van der Waals and a hybrid exact exchange functional. The key results are given in Table II. Overall we find that the difference between the square-tube and square structure is not very sensitive to the choice of XC functional and for all functionals square-tube is ca. 20 meV/H \( _{2} \) O more stable than the square structure at 1 GPa. The apparent insensitivity to the XC functional can be further shown by the decomposition of enthalpy in Table II.

<table><tr><td>Methods</td><td>\( \Delta H \)</td><td>\( \Delta E_{\text{tice}}^{\text{tot}} \)</td><td>\( \Delta E_{\text{confinement}} \)</td><td>\( (\Delta P \times A \times h) \)</td></tr><tr><td>rPW86-vdW2</td><td>19</td><td>14</td><td>0</td><td>5</td></tr><tr><td>optPBE-vdW</td><td>20</td><td>15</td><td>0</td><td>5</td></tr><tr><td>optB88-vdW</td><td>24</td><td>18</td><td>0</td><td>6</td></tr><tr><td>PBE+vdW(TS)</td><td>23</td><td>16</td><td>0</td><td>7</td></tr><tr><td>HSE+vdW(TS)</td><td>25</td><td>19</td><td>0</td><td>6</td></tr></table>

TABLE II. Stability of the square-tube and double-layer square structures at 1 GPa calculated using different XC functionals at a confinement width of 9.5 Å.  \( \Delta H \) ,  \( \Delta E_{tice}^{tot} \) ,  \( \varDelta E_{confinement} \)  and  \( \varDelta(P \times A \times h) \)  are differences between the square and the square-tube structure for energy terms as defined in Eqs. 1 and 2. All values are reported in units of meV/H \( _{2} \) O.

Role of zero point energies: Since we consider small energy differences between the various phases it is possible that differences in zero point energy (ZPE) could tip the balance in stability between them. Therefore we computed the ZPE of relevant phases within the harmonic approximation. As shown in Fig. 5b no significant changes in phase transitions have been identified when ZPEs are accounted for. Specifically, comparing the enthalpy of the square structure and the square-tube structure at 1 GPa, the relative stability of the square structure is slightly increased by ca. 4 meV/H \( _{2} \) O.

Finite temperatures: Considering that the experiments from which square ice has been suggested have been carried out at room temperature, \( ^{1} \)  it is also important to evaluate the influence of finite temperature. Therefore, the free energy instead of the enthalpy should be
 
![](./images/867761091352986487_10.jpg)

![](./images/867761091352986487_11.jpg)

FIG. 5. (a) Comparison of the relative enthalpies obtained with the optPBE-vdW (solid line) and rPW86-vdW2 (dashed lines) functionals. (b) Comparison of the relative enthalpies obtained from rPW86-vdW2 with (solid line) and without (dashed lines) zero point energy (ZPE). ZPEs have been calculated as,  \( E_{ZPE} = \sum_{i=1}^{i=N} \frac{1}{2} \hbar \omega_{\Gamma,i} \)  where  \( \omega_{\Gamma,i } \)  is the ith gamma point vibrational frequency calculated using the finite displacement method, and  \( \hbar \)  is the reduced Planck constant, and N is the number of vibrational modes.

calculated. As a first step the phonon free energy has been calculated at the harmonic level as,  \( E_{\mathrm{vib}} = \int \hbar \omega \left[ \frac{1}{2} + \frac{1}{\exp(\hbar \omega / k_{B} T) - 1} \right] g(\omega) d\omega \) , where  \( g(\omega) \)  is the phonon density of states (Fig. 6),  \( k_{B} \)  the Boltzmann constant and T the temperature. At 300 K the phonon free energy of the square structure is 6 meV/ \( H_{2}O \)  less than that of the square-tube structure. Thus finite temperature effects increase the stability of the square structure, and even though the energy difference between the square and square-tube structures is very small, the square-tube structure remains marginally more stable.

Role of anharmonic effects: It is also possible that anharmonic phonon effects at finite temperature alter the stability of ice structures. Recently Engel et al. found that
 

it can result in a difference of  \( 6.5 \pm 3.1 \)  meV/ \( H_{2}O \)  for bulk ice  \( I_{h} \)  and  \( I_{c} \) , which is large enough to explain the difference between harmonic theories and experiments. \( ^{47} \)  They also showed that the anharmonic contribution mainly comes from the vibrational modes at high frequencies that are related to the motion of hydrogen atoms. Therefore, we carried out ab initio molecular dynamics simulations at 300 K for both the square-tube and square structures. Instead of accurately computing the challenging anharmonic free energy, here we try to estimate the influence of anharmonic effects qualitatively from these molecular dynamics simulations. Fig. 6a shows the distribution of OH bond lengths, which reflects the different types of hydrogen bonds in the two structures. The phonon density of states of these high frequency modes calculated from these trajectories are shown in Fig. 6b, where no significant difference is observed. We can also do the integration using the harmonic phonon free energy equation with these phonon density of states, which further shows that they are very similar as the integration gives a vanishing difference. Therefore, these simulations indicate that the anharmonic contribution is unlikely to alter the relative stability of the square and the square-tube structures.

Role of hydrogen ordering: In the discussion above the lowest enthalpy square and square-tube structures are compared. It is also important to consider how our conclusions at finite temperatures would be affected by the configurational entropy of hydrogen ordering (different distributions of hydrogen atoms within the same lattice of oxygen atoms), which is important in ice. \( ^{49,50} \)  A transition from the square-tube structure to the HCP structure driven by configurational entropy has been predicted in Ref. 7. Here the possible configurations of different hydrogen distributions of the square and the square-tube structure are counted and the configurational entropy is estimated as  \( S = k_{B}ln\Omega \) , where  \( \Omega \)  is the number of possible states. Following the Bernal-Fowler and Pauling ice rules, \( ^{51,52} \)  we impose three rules to the square phase: (i) hydrogen atoms locate in or between the two layers; (ii) half of the water molecules only bond to neighbors within the same layer, the other half form one hydrogen bond within the layer and one hydrogen bond with the other layer; and (iii) between each oxygen atom pair there should be no more than one hydrogen atom. This leads to  \( \Omega_{square} = [C_{4}^{2} \times (C_{4}^{1})^{8}]^{1/8} \times (3/4)^{2} \) . For the square-tube phase the rules are: (i) no hydrogen atoms are allowed outside of the tube; (ii) cells must be connected along the tube by more than  \( (1/2) \)  hydrogen bonds per water molecule; and (iii) between each oxygen atom pair there should be no more than one hydrogen atom. This leads to  \( \Omega_{square-tube} = (C_{8}^{4})^{3/8} \times (3/4)^{2} \) .
 
![](./images/867761091352986487_12.jpg)

![](./images/867761091352986487_13.jpg)

FIG. 6. (a) Distribution of OH bond length for the square and square-tube structures as obtained from ab initio molecular dynamics simulations at 300 K. (b) Phonon density of states for the square and square-tube structures. Dashed lines: harmonic phonon density of states using the finite displacement method. The calculation was performed with a  \( 2 \times 2 \times 1 \)  supercell and a  \( 8 \times 8 \times 1 \)  grid in the phonon zone using the Phonopy package. \( ^{48} \)  Solid lines: phonon density of states calculated from ab initio molecular dynamics at 300 K.

The contribution to the free energy difference between these two phases is  \( \Delta F \approx 0.02k_{B}T \)  (< 1 meV/H \( _{2} \) O), which is negligible compared to the difference between the square and square-tube structures. Although this estimate is crude and is based on the assumption that all possible hydrogen ordered states are degenerate, it suggests that configurational entropy effects are unlikely to alter the relative stability of the two structures significantly.

In this section we have addressed issues including the sensitivity of the results to the XC functional, ZPE, harmonic and anharmonic phonon free energies, and configurational entropy. There are other issues not addressed which might also be important. For instance, the presence of real graphene instead of a confining potential, the finite size of the ice structures
 

observed in the experiments and the role of edges. We believe these effects will not affect our conclusions significantly because: (i) The graphene is incommensurate with the ice and the interaction between graphene and water molecules is not very sensitive to the orientation and lateral position of water molecules, which we have shown in our previous study. \( ^{5} \)  (ii) More hydrogen bonds break at the edge of the square structure than the square-tube structure. Thus, on the basis of our calculations, we conclude that double-layer square ice is a metastable phase across a wide range of confinement widths and pressures. Interestingly, our previous work found that monolayer square ice is a stable phase, \( ^{5,9} \)  which lends support to the experimental observations of square ice. \( ^{1} \)  Therefore, although we find double-layer square ice is metastable, it is possible that it forms as the growth of a metastable double-layer phase assisted by the presence of a stable monolayer. The influence of crystal growth kinetics and nucleation of square ice under confinement would therefore be an interesting issue to explore in future work. Experimentally, some well controlled annealing experiments could also be informative and help to establish if square ice is metastable. Zhou et al. questioned the observations of square ice from a different perspective suggesting that the confined material is layers of NaCl instead of ice. \( ^{2-4} \)  Such a concern also calls for further experimental and theoretical investigations of both confined water and confined NaCl.

## IV. SUMMARY

In summary, on the basis of DFT calculations a phase diagram of double-layer ice as a function of pressure and confinement width at 0 K is predicted. Complementary to our previous studies on monolayer ice, \( ^{5,9} \)  this study shows an interesting change of the phase diagram from monolayer to double-layer ice in confinement due to the presence of interlayer hydrogen bonds. For monolayer ice, a pentagonal and a square structure appear in the GPa regime, whereas for double-layer ice the pentagonal and square structures are metastable and in the GPa regime double-layer ice favours HCP and square-tube structures. Beyond the general insights on the phase diagram of confined ice, we have performed extensive calculations focusing on the double-layer square ice, which has been a matter of debate recently between experiment and theory. Our results suggest that the double-layer square ice is a metastable phase.
 

## ACKNOWLEDGEMENTS

J.C. and A.M. are supported by the European Research Council under the European Union’s Seventh Framework Programme (FP/2007-2013) / ERC Grant Agreement number 616121 (HeteroIce project). A.M. and C.J.P. are supported by the Royal Society through a Royal Society Wolfson Research Merit Award. C.J.P. and G.S. are also supported by EPSRC Grants No. EP/G007489/2 and No. EP/J010863/2. C.G.S is supported by the Royal Society (UF100144). We are also grateful for computational resources to the London Centre for Nanotechnology, UCL Research Computing, and to the UKCP consortium (EP/F036884/1) for access to Archer.

 \( ^{*} \)  ji.chen@ucl.ac.uk

 \( ^{\dagger} \)  angelos.michaelides@ucl.ac.uk

 \( ^{1} \)  G. Algara-Siller, O. Lehtinen, F. C. Wang, R. R. Nair, U. Kaiser, H. A. Wu, A. K. Geim, and I. V. Grigorieva, Nature 519, 443 (2015).

 \( ^{2} \)  W. Zhou, K. Yin, C. Wang, Y. Zhang, T. Xu, A. Borisevich, L. Sun, J. C. Idrobo, M. F. Chisholm, S. T. Pantelides, R. F. Klie, and A. R. Lupini, Nature 528, E1 (2015).

 \( ^{3} \)  G. Algara-Siller, O. Lehtinen, and U. Kaiser, Nature 528, E3 (2015).

 \( ^{4} \)  F. C. Wang, H. A. Wu, and A. K. Geim, Nature 528, E3 (2015).

 \( ^{5} \)  J. Chen, G. Schusteritsch, C. J. Pickard, C. G. Salzmann, and A. Michaelides, Physical Review Letters 116, 025501 (2016).

 \( ^{6} \)  F. Corsetti, P. Matthews, and E. Artacho, Scientific Reports 6, 18651 (2016).

 \( ^{7} \)  F. Corsetti, J. Zubeltzu, and E. Artacho, Physical Review Letters 116, 085901 (2016).

 \( ^{8} \)  T. Roman and A. Groß, The Journal of Physical Chemistry C 120, 13649 (2016).

 \( ^{9} \)  J. Chen, A. Zen, J. G. Brandenburg, D. Alfe, and A. Michaelides, Physical Review B 94, 220102 (2016).

 \( ^{10} \)  H. J. C. Berendsen, J. R. Grigera, and T. P. Straatsma, The Journal of Physical Chemistry 91, 6269 (1987).

 \( ^{11} \)  W. L. Jorgensen, J. Chandrasekhar, J. D. Madura, R. W. Impey, and M. L. Klein, The Journal of Chemical Physics 79, 926 (1983).
 

 \( ^{12} \)  K. Lee, E. D. Murray, L. Kong, B. I. Lundqvist, and D. C. Langreth, Physical Review B 82, 081101 (2010).

 \( ^{13} \)  K. Koga, X. C. Zeng, and H. Tanaka, Physical Review Letters 79, 5262 (1997).

 \( ^{14} \)  K. Koga, H. Tanaka, and X. C. Zeng, Nature 408, 564 (2000).

 \( ^{15} \)  R. Zangi and A. E. Mark, The Journal of Chemical Physics 119, 1694 (2003).

 \( ^{16} \)  N. Giovambattista, P. J. Rossky, and P. G. Debenedetti, Physical Review Letters 102, 050603 (2009).

 \( ^{17} \)  S. Han, M. Y. Choi, P. Kumar, and H. E. Stanley, Nature Physics 6, 685 (2010).

 \( ^{18} \)  J. C. Johnston, N. Kastelowitz, and V. Molinero, The Journal of Chemical Physics 133, 154516 (2010).

 \( ^{19} \)  N. Kastelowitz, J. C. Johnston, and V. Molinero, The Journal of Chemical Physics 132, 124511 (2010).

 \( ^{20} \)  J. Bai and X. C. Zeng, Proceedings of the National Academy of Sciences 109, 21240 (2012).

 \( ^{21} \)  N. Giovambattista, P. Rossky, and P. Debenedetti, Annual Review of Physical Chemistry 63, 179 (2012).

 \( ^{22} \)  W.-H. Zhao, L. Wang, J. Bai, L.-F. Yuan, J. Yang, and X. C. Zeng, Accounts of Chemical Research 47, 2505 (2014).

 \( ^{23} \)  Q. Lu, J. Kim, J. D. Farrell, D. J. Wales, and J. E. Straub, The Journal of Chemical Physics 141, 18C525 (2014).

 \( ^{24} \)  M. Sobrino Fernandez Mario, M. Neek-Amal, and F. M. Peeters, Physical Review B 92, 245428 (2015).

 \( ^{25} \)  J. Zubeltzu, F. Corsetti, M. V. Fernández-Serra, and E. Artacho, Physical Review E 93, 062137 (2016).

 \( ^{26} \)  C. J. Pickard and R. J. Needs, Journal of Physics: Condensed Matter 23, 053201 (2011).

 \( ^{27} \)  G. Kresse and J. Furthmüller, Physical Review B 54, 11169 (1996).

 \( ^{28} \)  G. Kresse and D. Joubert, Physical Review B 59, 1758 (1999).

 \( ^{29} \)  J. Klimeš, D. R. Bowler, and A. Michaelides, Physical Review B 83, 195131 (2011).

 \( ^{30} \)  B. Santra, J. Klimeš, A. Tkatchenko, D. Alfe, B. Slater, A. Michaelides, R. Car, and M. Scheffler, The Journal of Chemical Physics 139, 154702 (2013).

 \( ^{31} \)  J. Klimeš, D. R. Bowler, and A. Michaelides, Journal of Physics: Condensed Matter 22, 022201 (2010).

 \( ^{32} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Physical Review Letters 77, 3865 (1996).

 \( ^{33} \)  J. Heyd, G. E. Scuseria, and M. Ernzerhof, The Journal of Chemical Physics 118, 8207 (2003).

 \( ^{34} \)  J. Heyd, G. E. Scuseria, and M. Ernzerhof, The Journal of Chemical Physics 124, 219906 (2006).

 \( ^{35} \)  A. Tkatchenko and M. Scheffler, Physical Review Letters 102, 073005 (2009).
 

 \( ^{36} \)  J. Ma, A. Michaelides, D. Alfe, L. Schimka, G. Kresse, and E. Wang, Physical Review B 84, 033402 (2011).

 \( ^{37} \)  See Supplemental Material for additional data and structure files.

 \( ^{38} \)   \( P = \frac{1}{2} (\sigma_{xx} + \sigma_{yy}) \) ,  \( \sigma = \sigma' \times L_{z}/h \) ,  \( \sigma_{xx}' \)  and  \( \sigma_{yy}' \)  are the calculated lateral (x and y direction) diagonal stress tensor elements for the slab/vacuum model,  \( L_{z} \)  is the length of the cell in the out-of-plane direction. In the calculation  \( \sigma_{xx}' \times L_{z} \)  and  \( \sigma_{yy}' \times L_{z} \)  are conserved quantities, the calculation of the enthalpy is independent of the definition of h. Therefore, the shape of the phase diagram is not affected by the definition. However, the definition of h does affect the values of the transition pressures predicted. Our definition indicates an upper limit of layer height (width of confinement), corresponding to a lower limit of transition pressures. Assuming the lower limit of width is w - 3.0 (w = 9.5) the upper limit of the transition pressures are about 1.5 times larger.

 \( ^{39} \)  S. Nosé, The Journal of Chemical Physics 81, 511 (1984).

 \( ^{40} \)  H. Witek and V. Buch, The Journal of Chemical Physics 110, 3168 (1999).

 \( ^{41} \)  G. A. Kimmel, J. Matthiesen, M. Baer, C. J. Mundy, N. G. Petrik, R. S. Smith, Z. Dohnlek, and B. D. Kay, Journal of the American Chemical Society 131, 12838 (2009).

 \( ^{42} \)  W.-H. Zhao, J. Bai, L.-F. Yuan, J. Yang, and X. C. Zeng, Chemical Science 5, 1757 (2014).

 \( ^{43} \)  M. Sobrino Fernández, F. M. Peeters, and M. Neek-Amal, Physical Review B 94, 045436 (2016).

 \( ^{44} \)  R. Zangi and A. E. Mark, Physical Review Letters 91, 025502 (2003).

 \( ^{45} \)  The lateral lattice constant and pressure of the square ice calculated are in agreement with the TEM measurements of lattice constant and pressure estimate. The lattice constant calculated using the rPW86-vdW2 functional at 1 GPa is 2.82 Å, and likewise a 2.83 Å lattice constant predicts a pressure of 0.91 GPa. There are a few aspects that need to be noted: (i) Thermal expansion is not considered; (ii) The estimated pressure in the experiments is based on a simple model whose accuracy is not clear; (iii) The relation between the lattice constant and pressure depends on the functional used, for instance the optPBE-vdW functional gives a lateral pressure of 0.65 GPa with a lattice constant of 2.83 Å; (iv) The relation between the lattice constant and pressure depends to some extent on the definition of lateral pressure, or in other words, the definition of the layer height. For double-layer ice our definition might underestimate the pressure, whereas the upper limit of pressure is about 50% larger as noted above.
 

46 M. J. Gillan, D. Alfe, and A. Michaelides, The Journal of Chemical Physics 144, 130901 (2016).

47 E. A. Engel, B. Monserrat, and R. J. Needs, Physical Review X 5, 021033 (2015).

 \( ^{48} \)  A. Togo and I. Tanaka, Scr. Mater. 108, 1 (2015).

 \( ^{49} \)  C. G. Salzmann, P. G. Radaelli, A. Hallbrucker, E. Mayer, and J. L. Finney, Science 311, 1758 (2006).

 \( ^{50} \)  C. G. Salzmann, B. Slater, P. G. Radaelli, J. L. Finney, J. J. Shephard, M. Rosillo-Lopez, and J. Hindley, The Journal of Chemical Physics 145, 204501 (2016).

 \( ^{51} \)  J. D. Bernal and R. H. Fowler, The Journal of Chemical Physics 1, 515 (1933).

 \( ^{52} \)  L. Pauling, Journal of the American Chemical Society 57, 2680 (1935).
 

## SUPPLEMENTAL MATERIAL

This supplemental material contains: the confining potential at different widths (Fig. S1); additional enthalpy data and structures in Fig. SS2 and Fig. S3; and structure files for phases reported in the main text.

![](./images/867761091352986487_14.jpg)

FIG. S1. Confining potential at different widths.
 
![](./images/867761091352986487_15.jpg)

FIG. S2. Enthalpies (relative to ST) of the double-layer ice structures as a function of lateral pressure at a confinement width of 9.5 Å. Solid lines with filled symbols are the same as Fig. 3(c). Dashed lines show the enthalpy of the structures obtained via structure optimisation starting with the hexagonal, pentagonal, and square phases at high pressure. The corresponding structures are shown in Fig. S2. The data points of the dashed lines are at 1, 2, 3, 4, and 5 GPa. We note that the small regime where the red dashed line has the lowest enthalpy does not indicate that we should have a new phase there. The red dashed line is the ST structure, with a larger unit cell and thus a slightly different hydrogen ordering.
 
![](./images/867761091352986487_16.jpg)

FIG. S3. The structures correspond to the dashed lines in Fig. S1. (a) A square structure, with a different unit cell and hydrogen ordering, that comes from optimising the hexagonal phase at 2 GPa. (b) A ST structure, with a different unit cell and hydrogen ordering, that comes from optimising the pentagonal phase at 1 GPa. (c) A tilted square structure that comes from optimising the square phase at 2 GPa. Same structures were seen at higher pressures up to 5 GPa.
 
