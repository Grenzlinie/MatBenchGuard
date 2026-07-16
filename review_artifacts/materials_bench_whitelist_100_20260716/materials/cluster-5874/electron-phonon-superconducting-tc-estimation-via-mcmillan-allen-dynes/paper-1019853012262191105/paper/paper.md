
# First-principles design of ambient-pressure Mg_{x}B_{2}C_{2} and Na_{x}BC superconductors

Charly R. Tomassetti, \( ^{1} \)  Daviti Gochitashvili, \( ^{1} \), Christopher

Renskers, \( ^{1} \)  Elena R. Margine, \( ^{1,*} \)  and Aleksey N. Kolmogorov \( ^{1,\dagger} \) 

 \( ^{1} \) Department of Physics, Applied Physics, and Astronomy, Binghamton University-SUNY, Binghamton, New York 13902, USA
(Dated: July 15, 2024)

We employ ab initio modeling to investigate the possibility of attaining high-temperature conventional superconductivity in ambient-pressure materials based on the known  \( MgB_{2}C_{2} \)  and recently proposed thermodynamically stable  \( NaBC \)  ternary compounds. The constructed  \( (T, P_{\mathrm{M}}) \)  phase diagrams (M = Mg or Na) indicate that these layered metal borocarbides can be hole-doped via thermal deintercalation that has been successfully used in previous experiments to produce  \( Li_{1>x}\geq_{0.5}BC \)  samples. The relatively low temperature threshold required to trigger  \( NaBC \)  desodiation may help prevent the formation of defects shown recently to be detrimental to the electron-phonon coupling in the delithiated LiBC analog. According to our numerical solutions of the anisotropic full-bandwidth Migdal-Eliashberg equations, the proposed  \( Mg_{x}B_{2}C_{2} \)  and  \( Na_{x}BC \)  materials exhibit superconducting critical temperatures between 43 K and 84 K. At the same time, we demonstrate that buckling of defect-free honeycomb BC layers, favored in heavily-doped  \( Na_{x}BC \)  compounds, can substantially reduce or effectively suppress the materials' potential for  \( MgB_{2} \) -type superconductivity.

## I. Introduction

The naturally hole-doped stoichiometric  \( MgB_{2} \)  with honeycomb boron layers has served as a blueprint for designing ambient-pressure high- \( T_{c} \)  superconductors ever since the unexpected 2001 discovery of the material's conventional superconductivity at 39 K [1]. It was quickly established that no other known diborides of Al or transition metals display the quasi-2D electronic features responsible for the strong electron-phonon (e-ph) coupling, while the possibility of adding new members to the large  \( MB_{2} \)  family is prohibited by unfavorable thermodynamics at ambient conditions (M = Li, Cu, Ag, Au, etc.) [2, 3]. Expansion of the search space to other metal-boron compositions (e.g., MB) or ternary metal borides (e.g.,  \( Mg_{x}M_{1-x}B_{2} \)  and  \( Li_{x}M_{y}B \) ) further demonstrated the difficulty of obtaining stable materials with the desired hole-doped covalent bonds [3–11]. Meanwhile, graphite intercalation compounds (GICs) with fully filled  \( \sigma \)  states display a different e-ph coupling mechanism and generally lower  \( T_{c} \)  [12–14].

The electron-deficient honeycomb frameworks with alternating B and C atoms possess the signature quasi-2D electronic states and hard vibrational modes to be  \( MgB_{2} \) -type superconductors. Since the only two metal borocarbides with this morphology, LiBC [15] and  \( MgB_{2}C_{2} \)  [16], are semiconductors in the stoichiometric form, several studies have been dedicated to investigating their hole-doped derivatives.  \( Li_{1>x}B_{C} \)  had been predicted in early computational works to superconduct at temperatures as high as 100 K [17–19], but successful experimental efforts to delithiate  \( Li_{x}B_{C} \)  unfortunately resulted in no detectable  \( T_{c} \)  [20–26]. The lack of superconductivity has been attributed to the likely presence of defects in the BC layers that become thermodynamically favored at low Li concentrations [25, 27]. Reintercalation of  \( Li_{x}B_{C} \)  with other group I or II elements has been identified in our recent work as a possible route of obtaining elusive  \( MgB_{2} \)  analogs [27].

Computational studies examining hole-doped  \( MgB_{2}C_{2} \) , through removal and/or replacement of Mg with alkali metals [28–31], also noted the materials' potential for high- \( T_{c} \)  superconductivity. In particular, Spanò et al. [30] considered various  \( (\mathrm{Mg},\mathrm{Li})\mathrm{B}_{2}\mathrm{C}_{2} \)  and  \( (\mathrm{Mg},\mathrm{Na})\mathrm{B}_{2}\mathrm{C}_{2} \)  phases and concluded that a substitution of Mg by Li is energetically favorable in hole-doped  \( MgB_{2}C_{2} \) . The most extensive experimental investigation of the compound's derivatives was performed by Mori and Takayama-Muromachi in 2004 [32]. The appearance of Pauli magnetism in the synthesized  \( Mg_{0.5}Li_{0.8}B_{2}C_{2} \)  material indicated that the sample became metallic, but no superconductivity was observed down to 1.8 K. Attempts at high pressure synthesis of  \( (\mathrm{Mg},\mathrm{Li})\mathrm{B}_{2}\mathrm{C}_{2} \)  and boron doping of the B/C nets in  \( MgB_{2}C_{2} \)  were unsuccessful, resulting in large amounts of neighboring phases, LiBC and  \( MgB_{2} \)  [32]. To the best of our knowledge, there have been no reported attempts to deintercalate  \( MgB_{2}C_{2} \)  through high-temperature annealing as has been done with LiBC [22, 23, 25, 26].

The recently uncovered thermodynamic stability of NaBC at low temperatures [27], in a simple hexagonal structure [33], offers another pathway for designing high- \( T_{c} \)  metal borocarbides. Prior theoretical work simulated holes in NaBC through desodiation [34] or substitution of C by B [33], and predicted the hole-doped NaBC to have high critical temperatures in both cases (e.g., 35 K for  \( NaB_{1.1}C_{0.9} \)  using the Allen-Dynes modified McMillan formula and  \( \mu^{*}=0.1 \)  [33]). The discovery of a new  \( NaB_{5}C \)  compound, as recently as 2021 [35], brings up questions about what other materials may exist in this ternary system and what properties they may display.
 
![](./images/1019853012262191105_1.jpg)

FIG. 1. Crystal structures of select examined layered  \( Na_{x}B_{2}C \)  and  \( Mg_{x}B_{2}B_{2}C_{2} \)  phases denoted with Pearson symbols. The fully intercalated compounds are (a)  \( NaBC \)  with perfectly flat BC layers previously proposed to be a low-temperature ground state [27] and (f)  \( MgB_{2}C_{2} \)  with BC layers buckled around rhombus-shaped Mg patches first observed in 1994 [16].

In this work, we use density functional theory (DFT) to analyze thermodynamic stability and superconducting properties of the  \( Na_{1>x}BC \)  and  \( Mg_{1>x}B_{2}C_{2} \)  compositional subspaces. We identify the most favorable layered configurations, map out the  \( (T,P_{\mathrm{M}}) \)  synthesis conditions needed to thermally deintercalate the ternary compounds, and calculate the superconducting  \( T_{c} \)  of the hole-doped materials using the anisotropic Midgal-Eliashberg (aME) formalism. Our findings indicate that NaBC and  \( MgB_{2}C_{2} \) , shown in Fig. 1, are promising precursors for ambient-pressure synthesis of high- \( T_{c} \)  conventional superconductors.

## II. Methods

VASP [36] was used to conduct the stability analysis of Na-B-C and Mg-B-C phases using projector augmented wave potentials [37] and a 500 eV plane-wave cutoff. Due to the known importance of dispersive interactions in layered materials [7, 38–40], we used the optB86b-vdW functional [41], and checked the sensitivity of the results to the DFT approximations with the optB88-vdW [42] and r2SCAN+rVV10 [40, 43] functionals. All structures were evaluated with dense ( \( \Delta k \sim 2\pi \times 0.025 \, \AA^{-1} \) ) Monkhorst-Pack k-meshes [44].

Global structure searches were performed with an evolutionary algorithm implemented in the MAISE package [45]. In fixed-composition runs, randomly initialized 16-member populations with up to 22 atoms per unit cell were evolved for up to 250 generations using standard mutation and crossover operations [45]. The thermodynamic corrections due to vibrational entropy were calculated within the finite displacement methods implemented in PHONOPY [46]. We employed supercells between 56 and 168 atoms, applying 0.1 Å displacements within the harmonic approximation. Previous quasi-harmonic approximation results for related Li-B-C, Li-Na-B-C, and Na-Sn materials [27, 47, 48] show that volume expansion has a negligible effect on the formation free energies in the considered temperature range. A combinatorial screening method was used to sequentially remove intercalants and leave only non-equivalent configurations. Equivalence was evaluated with our structural fingerprint based on the radial distribution function [45, 49].

The QUANTUM ESPRESSO package [50] was used for calculating properties related to superconductivity. We employed the optB86b-vdW and optB88-vdW functionals [41, 42, 51–54] and norm-conserving pseudopotentials from the Pseudo Dojo library [55] generated with the relativistic PBE parametrization [56]. A plane-wave cutoff value of 100 Ry, a Methfessel-Paxton smearing [57] value of 0.02 Ry, and  \( \Gamma \) -centered Monkhorst-Pack [44] k-meshes were used to describe the electronic structure. The lattice parameters and atomic positions were relaxed until the total energy was converged within  \( 10^{-6} \)  Ry and the maximum force on each atom was less than  \( 10^{-4} \)  Ry/A. The dynamical matrices and the linear variation of the self-consistent potential were calculated within density-functional perturbation theory [58] on irreducible sets of regular q-meshes. The optimized lattice parameters for the investigated phases and the k- and q-meshes used are reported in Table S1 [59].

The e-ph interactions and superconducting properties were evaluated with the EPW code [60–63]. The Wannier interpolation [64–66] was performed on uniform  \( \Gamma \) -centered k-grids (see Table S1 [59]) with the Wannier90 code [64–66] in library mode. We considered 2p orbitals for every C or B atom as projections for the maximally localized Wannier functions to accurately describe the electronic structure of all the compounds under investigation. The anisotropic full-bandwidth [63, 67] equations were solved with a sparse intermediate representation of
 
![](./images/1019853012262191105_2.jpg)

![](./images/1019853012262191105_3.jpg)

![](./images/1019853012262191105_4.jpg)

![](./images/1019853012262191105_5.jpg)

FIG. 2. Relative energies of  \( Na_{x}BC \)  and  \( Mg_{x}B_{2}C_{2} \)  phases referenced to a hypothetical fully deintercalated BC phase and (a),(b) the elemental ground states or (c),(d) the fully intercalated ternary ground states. The solid green lines define the global convex hulls, the solid black lines mark the boundaries of the local convex hulls for deintercalated honeycomb derivatives, the dashed blue lines show the estimated configurational entropy contributions from metal disorder, and the dashed gray lines point to the chemical potentials of  \( Na_{x}^{gas} \)  ( \( Mg^{gas} \) ) needed to destabilize the starting  \( \mathrm{NaBC} \)  ( \( MgB_{2}C_{2} \) ) phase. The solid symbols denote metal borocarbides with honeycomb (black hexagons), bond rotation (BR, purple triangles), interlayer bridging (IB, orange circles), and fully connected (3D, red circles) morphologies of the BC covalent networks. The crossed gray circles in panel (d) correspond to deintercalated phases derived from the large experimental  \( MgB_{2}C_{2} \)  structure. The circle points highlight materials examined for their superconducting properties. The shaded areas correspond to compositions that should be accessible via deintercalation.

the Matsubara frequencies [68] on fine uniform k- and q-point grids (see Table S1 [59]), with an energy window of  \( \pm0.2 \)  eV around the Fermi level. The Coulomb  \( \mu^{*} \)  parameter was chosen to be 0.20, which ensures good agreement between measured and computed  \( \Delta \) ME  \( T_{e} \)  values for  \( MgB_{2} \)  [69]. Visualizations of crystal structures and Fermi surfaces were created with VESTA [70] and FermiSurfer [71], respectively. To resolve different phases at the same composition, we use Pearson symbols and space groups when needed. Full structural information for relevant DFT-optimized  \( Na_{x}BC \)  or  \( Mg_{x}B_{2}C_{2} \)  phases is provided as CIF files in the Supplementary Material.

## III. Results and discussion

## A. Stability

Complementary structure search strategies shown to be effective in the exploration of related metal borocarbides [27] were employed to examine the  \( Na_{x}BC \)  and  \( Mg_{x}B_{2}C_{2} \)  subspaces with the ultimate aim of determining the composition ranges where the materials should remain layered and relatively defect-free after hole-doping. First, we conducted a combinatorial screening by generating different  \( \mathrm{NaBC} \)  and  \( \mathrm{MgB_{2}C_{2}} \)  (super)cells and systematically removing metal ions, leaving only the non-equivalent configurations. The supercells included standard expansions of the fully-filled hP6 structure, known to be the ground state for LiBC and NaBC, such as  \( \sqrt{3} \times \sqrt{3} \)  × 1,  \( 2 \times 2 \times 1 \) , and orthorhombic supercells of increasing size up to 54 atoms with both AA and AA' stackings of the BC sheets. We also proceeded with systematic deintercalation of the oS80 ground state of  \( MgB_{2}C_{2} \)  down to x = 11/16. The full set of considered layered phases contained over 700 distinct metal decorations.

The formation energies of the best candidate hole-doped structures (Fig. 2(a)-(b)) fall above the global convex hull as defined by the respective combinations of NaBC ( \( MgB_{2}C_{2} \) ),  \( B_{4}C \) , and C materials. However, the successful deintercalation experiments on LiBC have established that the BC framework retains its layered
 

morphology at high temperatures (up to 1770 K) and low metal concentrations (down to at least x = 0.5) [25]. This indicates that the high kinetic barriers associated with rebonding of the covalent layers are sufficiently high to keep the materials from decomposing into other products under a wide range of experimental conditions. Hence, we examine the feasibility of the intercalated  \( M_{x}BC \)  phases within the kinetically restricted subspace and, for convenience, display their relative stability with respect to  \( \mathrm{NaBC} \)  ( \( MgB_{2}C_{2} \) ) and a fully deintercalated hypothetical layered BC, as was done in our previous study on  \( Li_{x}BC \)  [47]. Fig. 2(c) and (d) show that the best  \( Mg_{x}B_{2}C_{2} \)  phases, just as in the LiBC case, stay close to the  \( MgB_{2}C_{2} \leftrightarrow BC \)  tie-line, but the  \( Na_{x}BC \)  derivatives fall way below the corresponding reference line and are actually within 25 meV/atom, for x down to 3/4, of being globally stable relative to  \( NaBC \) ,  \( B_{4}C \) , and C. For reference, we show configurational entropy contributions estimated as  \( \Delta F_{conf} = kT [x \ln(x) + (1 - x) \ln(1 - x)] / (2 + x) \)  as functions of  \( y = (1 - x) / (1 + x / 2) \)  in Fig. 2(c) or  \( y = (1 - x) / (2 + x / 2) \)  in Fig. 2(d), at the expected deintercalation temperatures.

To analyze the preferred Mg arrangement after deintercalation, we first considered the conventional unit cell of the  \( OsO_{8}-MgB_{2}C_{2} \)  ground state, where the Mg atoms are grouped in rhombus-shaped patches with two non-equivalent sites at the acute- and obtuse-angled corners (Fig. 1(f)). The relative energies of Mg-depleted structures are contained in a well-defined wedge (Fig. 2(d)), with the more stable configurations featuring Mg atoms in the obtuse-angle sites. Structures derived from hP6- \( Mg_{2}B_{2}C_{2} \)  supercells with more even distributions of Mg atoms prove to be more favorable for compositions below  \( \sim 0.95 \) , and one can expect the material to quickly depart from the complex rhombus-patterned arrangement of Mg atoms upon deintercalation.

The amount and distribution of the intercalants can influence the compound’s superconducting properties by defining not only the doping level of the BC sheets but also the degree of their buckling. The maximum B or C out-of-plane displacements in the synthesized  \( MgB_{2}C_{2} \)  material [16] reaches  \( d_{max} = 0.20 \, \AA \) . To illustrate the dependence of the corrugation on the metal type, concentration, and distribution, we collected the DFT data for all constructed  \( Na_{x}BC \)  and  \( Mg_{x}B_{2}C_{2} \)  phases in Fig. 3. Focusing on the most stable structures in each ternary, we observe different trends for covalent framework buckling upon extraction of the larger alkali and smaller alkaline-earth metals. The BC layers start as perfectly flat in the fully loaded NaBC, become progressively more distorted with decreasing Na content reaching  \( d_{avg} = 0.14 \, \AA \)  at x = 5/8, and finally settle with an intermediate corrugation value of  \( 0.07 \, \AA \)  at x = 1/2. The  \( MgB_{2}C_{2} \)  material, being half-filled, possesses a significantly corrugated BC network with  \( d_{avg} = 0.10 \, \AA \) , exhibits numerous nearly degenerate configurations with gradually decreasing buckling down to  \( 0.06 \, \AA \)  at x = 11/16, and has perfectly flat layers in a high-symmetry crystal structure.

![](./images/1019853012262191105_6.jpg)

![](./images/1019853012262191105_7.jpg)

FIG. 3. Average distortion of BC layers ( \( d_{avg} \) ) at different compositions x in (a)  \( Na_{x}BC \)  and (b)  \( Mg_{x}B_{2}C_{2} \) . The color map shows the energy of the considered phases within a 20 meV/atom window relative to the most stable structure at each composition, which are connected with dashed black lines. The circled phases were examined for superconducting properties with aME calculations.

with a uniform distribution of Mg ions at x = 2/3. Some configurations in both Na and Mg sets led to the natural formation of interlayer C-C bonds upon local relaxation but none of these phases were found to be preferred in the composition range considered.

Additionally, we constructed layered structures with both AA and AA' stackings incorporating rotated B-C bonds. This defect type was theorized to occur in  \( Li_{x}BC \)  [25, 27] and could be responsible for the absence of superconductivity in the synthesized samples. The most stable stoichiometric ternary phases with rotated bonds, mP15-MgB₂C₂ and mP36-NaBC, are well above the corresponding ground states, by 151 meV/atom and 119 meV/atom, respectively. In  \( Mg_{x}B_{2}C_{2} \) , the relative energy of the defective structures with respect to  \( MgB_{2}C_{2} \)  and BC decreases almost linearly with metal content x but remains well above the energy of the best ordered honeycomb phases, e.g., by 61 meV/atom, at the lowest x = 2/3 end (see Fig. 2(d)). In  \( Na_{x}BC \) , a similar linear trend as a function of composition makes the structures with rotated bonds more competitive, with the best one at x = 1/2 actually becoming slightly more favored, by 7 meV/atom, over the ordered honeycomb counterparts.

Previous computational work on the  \( Li_{x}BC \)  system
 
![](./images/1019853012262191105_8.jpg)

![](./images/1019853012262191105_9.jpg)

![](./images/1019853012262191105_10.jpg)

![](./images/1019853012262191105_11.jpg)

![](./images/1019853012262191105_12.jpg)

(v) mS28 (C2/m)

![](./images/1019853012262191105_13.jpg)

(vi) mP14 (Pm)

FIG. 4. Crystal structures of competing  \( Mg_{2/3}B_{2}C_{2} \)  phases proposed in (i) previous work [29] and (ii),(vi) the present study.

also showed that non-layered structures with bridged or fully-connected 3D frameworks can become favored once the metal concentration falls below a certain level ( \( x \sim 2/3 \) ) [27, 47], but experiments indicate that  \( Li_{x}BC \)  remains layered down to approximately  \( x \sim 0.45 \) , at which point the material begins to decompose [25]. To probe the response of the  \( Na_{x}BC \)  and  \( Mg_{x}B_{2}C_{2} \)  compounds to alternative non-layered configurations, we performed unconstrained evolutionary searches. We found that non-layered morphologies become competitive around x = 1/2 for  \( Na_{x}BC \)  and x = 2/3 for  \( Mg_{x}B_{2}C_{2} \) , see Fig. 2(c)-(d).

The critical  \( Mg_{2/3}B_{2}C_{2} \)  stoichiometry examined by Pham et al. [29] deserves a closer look. This previous study identified an hP7 structure phase with AA stacking (Fig. 4(i)) as the 1:3:3 ground state with the optB88-vdW functional. Our optB88-vdV calculations show that an hP14 structure ( \( P6_{3}/mcm \) ) with the AA' stacking (Fig. 4(ii)) is degenerate in energy at 0 K but is slightly preferred by 0.5 meV/atom with the inclusion of the zero-point energy (ZPE) and becomes more stable by 0.9 meV/atom at 600 K with the inclusion of the vibrational entropy. The finding is not unexpected given that the parent  \( MgB_{2}C_{2} \)  material has the same stacking sequence and that LiBC, with a 5% shorter interlayer spacing, has a more pronounced preference for AA' over AA by 17 meV/atom at 0 K. To assess the reliability of the observations for these and other relevant polymorphs found with the evolutionary algorithm, we also calculated the free energies with the optB86-vdW and r2SCAN+rVV10 functionals. Fig. 5 summarizes the

![](./images/1019853012262191105_14.jpg)

![](./images/1019853012262191105_15.jpg)

FIG. 5. Relative free energies of select  \( Mg_{2/3}B_{2}C_{2} \)  polymorphs calculated at (a) T = 0 K and (b) T = 600 K with the optB86b-vdW [41], optB88-vdW [42], and r2SCAN+rVV10 [40, 43] functionals. The labeled points correspond to the crystal structures shown in Fig. 4. The blue hexagons denote phases with honeycomb BC layers, while the red spheres denote phases with complex re-ordered 3D networks. The latter set is more favored in both optB86b-vdW and r2SCAN+rVV10 approximations up to 600 K.

structure stability results relative to hP7 obtained with the three exchange-correlation functionals at 0 K and 600 K. The r2SCAN+rVV10 [40, 43] and optB86b [41] results indicate that several non-layered low-symmetry phases (Fig. 4(iv)-(vi)) are noticeably more stable than hP7 or hP14 ( \( P6_{3}/mcm \) ) at 0 K, with mP14 (Fig. 4(vi)) remaining preferred at 600 K. The optB88 functional [42], on the other hand, favors the layered polymorphs. Overall, the three approximations agree that the ordered honeycomb phases remain competitive at this composition, especially at high temperatures, and that the most stable decoration, by at least 15 meV/atom, has the  \( \sqrt{3} \times \sqrt{3} \)  in-plane expansion of the BC primitive unit cell. Therefore, one can indeed expect hP14- \( Mg_{2/3}B_{2}C_{2} \)  ( \( P6_{3}/mcm \) ) to be the product of  \( MgB_{2}C_{2} \)  deintercalation at high temperatures.

In the case of  \( Li_{x}BC \) , deintercalation is driven by the large gain in entropy attained when Li enters the diatomic gas state. As has been done previously [47], we can evaluate the entropy of Na and Mg within the ideal gas model by accounting for either the vibrational, rotational, and translational degrees of freedom for  \( Na_{g}^{gas} \) , or just the translational degrees of freedom for monatomic  \( Mg^{gas} \)  [72]. In Fig. 2(a)-(b), we illustrate how NaBC and  \( MgB_{2}C_{2} \)  should become destabilized when the chemical potentials for  \( Na_{g}^{gas} \)  and  \( Mg^{gas} \) , relative to their respective bulk ground states, fall below certain free energy values, approximated via extrapolations of the  \( NaBC \leftrightarrow Na_{3/4}BC \)  or  \( MgB_{2}C_{2} \leftrightarrow Mg_{4/5}B_{2}C_{2}\) lines. The necessary change in the chemical potential for  \( Na_{g}^{gas} \)  is
 
![](./images/1019853012262191105_16.jpg)

FIG. 6. Calculated map of phase stability  \( (T, P_{\mathrm{Na}}) \)  for deintercalated derivatives of  \( NaBC \) . The phase boundaries correspond to thermodynamic equilibria between neighboring layered  \( Na_{x}BC \)  materials and  \( Na_{2}^{gas} \) .

much smaller in magnitude than those for  \( Li_{2}^{gas} \)  and  \( Mg^{gas} \) , which indicates that NaBC deintercalation should be easier to achieve.

In Figs. 6 and 7, we propose  \( (T, P_{\mathrm{M}}) \)  diagrams demonstrating the required  \( Na_{2}^{gas} \)  or  \( Mg^{gas} \)  vapor pressures and temperatures needed to transition to metastable deintercalated products  \( Na_{x}BC \)  and  \( Mg_{x}B_{2}C_{2} \) . We find the positions of phase boundaries in  \( Na_{x}BC \)  by analyzing the identified ordered oP22, oS32, and oS80 structures at x = 3/4, 2/3, and 1/2, respectively. After incorporating the vibrational entropy for the bulk phases, we determined the equilibrium  \( (T, P_{\mathrm{M}}) \)  conditions within the temperature range of 200-2000 K by aligning the relative Gibbs free energies per Na atom for NaBC and the three combinations of  \( Na_{x}BC \)  with  \( Na_{2}^{gas} \) . A similar procedure was done for  \( Mg_{x}B_{2}C_{2} \)  using the oS48 and hP14  \( (P_{63}/mcm) \)  structures at x = 4/5 and 2/3, respectively. The resulting phase diagrams show that deintercalation of the known  \( MgB_{2}C_{2} \)  should well be achievable with similar experimental setups used for  \( Li_{x}BC \)  [22, 25, 47]. NaBC may be desodiated under considerably lower temperatures. The large separation of stability regions suggests that attaining a certain x composition in  \( Na_{x}BC \)  could be possible by choosing the targeted  \( (T, P_{\mathrm{M}}) \)  conditions and establishing the thermodynamic equilibrium, as opposed to relying upon the kinetics-determined non-equilibrium reaction [47].

## B. Superconductivity

The following analysis aims to establish whether the proposed layered  \( Na_{x}BC \)  and  \( Mg_{x}B_{2}C_{2} \)  materials attainable at ambient pressure have the necessary electronic and vibrational properties to be high- \( T_{c} \)  superconduct-

![](./images/1019853012262191105_17.jpg)

FIG. 7. Calculated map of phase stability  \( (T, P_{\mathrm{Mg}}) \)  for deintercalated layered derivatives of  \( MgB_{2}C_{2} \) . The phase boundaries correspond to thermodynamic equilibria between neighboring layered  \( Mg_{x}B_{2}C_{2} \)  materials and  \( Mg^{gas} \) .

tors. Previous work [18, 19, 27–29, 33, 34] has demonstrated similarities between hole-doped borocarbides and  \( MgB_{2} \) , attributing the strong e-ph coupling to the pairing of hole-doped  \( \sigma \)  states at the Fermi level with bond-stretching BC or B phonon modes. The superconducting properties of the relevant  \( Mg_{x}B_{2}C_{2} \) ,  \( Na_{x}BC \) , and  \( NaB_{1+x}C_{1-x} \)  compounds have been investigated in several studies [28, 29, 33, 34] but the  \( T_{c} \)  estimates have not included the e-ph anisotropy important in  \( MgB_{2} \) -type materials. The recent implementation of the anisotropic Migdal-Eliashberg formalism and the present identification of representative  \( Na_{x}BC \)  and  \( Mg_{x}B_{2}C_{2} \)  materials allow us to make more accurate  \( T_{c} \)  predictions and examine the  \( T_{c}s \)  sensitivity to different morphological traits.

First, we evaluated the potential for superconductivity in select phases depicted in Figs. 1 and 4, and listed in Table I to check for optimal doping levels in the Mg- and Na-based borocarbides. In addition to the honeycomb phases defining the local convex hull  \( (oS48-\mathrm{Mg}_{4/5}\mathrm{B}_{2}\mathrm{C}_{2}, \mathrm{hP}14-\mathrm{Mg}_{2/3}\mathrm{B}_{2}\mathrm{C}_{2} \left(P6_{3}/mcm\right), \mathrm{oP}22-\mathrm{Na}_{3/4}\mathrm{BC} \)  and  \( oS32-\mathrm{Na}_{2/3}\mathrm{BC} \) ), the set included other low-energy metastable phases  \( (mP19-\mathrm{Mg}_{3/4}\mathrm{B}_{2}\mathrm{C}_{2}, \mathrm{hP}7-\mathrm{Mg}_{2/3}\mathrm{B}_{2}\mathrm{C}_{2}, \mathrm{mP}23-\mathrm{Na}_{7/8}\mathrm{BC}, \mathrm{oP}22-\mathrm{Na}_{3/4}\mathrm{BC}, \mathrm{and} \mathrm{mP}21-\mathrm{Na}_{5/8}\mathrm{BC}) \)  to provide a better sampling of the composition range. All of the Mg borocarbides and the Na borocarbides with x > 2/3 display the hallmark  \( MgB_{2} \)  electronic properties, including the hole-doped B- and C- \( \sigma \)  states lifted at  \( \Gamma \)  by about 0.5 eV above the Fermi level (Figs. 8(a), S1 and S2 [59]), the corresponding sets of inner and outer Fermi surface cylinders (Figs. S10 and S11 [59]), and a considerable total DOS of 0.23-0.27 (0.17-0.21) states/ \( (eV \)  atom) in the Mg (Na) phases (Figs. 8(b), S1 and S2 [59]).

To determine the importance of the stacking order of the BC sheets, we performed superconductivity calcul-
 

TABLE I. Properties of select  \( Na_{x}BC \)  and  \( Mg_{x}B_{2}C_{2} \)  phases: the thermodynamic stability ( \( \Delta E_{hull} \) ) with respect to the local kinetically-restrained convex hull, average buckling of BC layers ( \( d_{avg} \) ), density of states (DOS( \( E_{F} \) )), superconducting  \( \lambda \) , and superconducting critical temperature calculated with the Allen-Dynes modified McMillian equation ( \( T_{c}^{AD} \) ) and with the aME formalism ( \( T_{c}^{aME} \) ).

<table><tr><td>Phase composition</td><td>Space group</td><td>Pearson symbol</td><td>\( \Delta E_{\text{hull}} \)  (meV/atom)</td><td>\( d_{\text{avg}} \)  ( \( \textup{\AA} \) )</td><td>DOS( \( E_{F} \) ) (states/(eV atom))</td><td>\( \lambda \)</td><td>\( T_{c}^{\textup{AD}} \)  (K)</td><td>\( T_{c}^{\textup{aME}} \)  (K)</td></tr><tr><td>Na \( _{7/8} \) BC</td><td>P2/m</td><td>mP23</td><td>6.7</td><td>0.04</td><td>0.17</td><td>0.97</td><td>24.9</td><td>88</td></tr><tr><td>Na \( _{3/4} \) BC</td><td>Pbam</td><td>oP22</td><td>0.0</td><td>0.11</td><td>0.21</td><td>0.95</td><td>21.9</td><td>84</td></tr><tr><td>Na \( _{2/3} \) BC</td><td>Cm \( c \) 21</td><td>oS32</td><td>0.0</td><td>0.12</td><td>0.32</td><td>1.32</td><td>15.6</td><td>43</td></tr><tr><td>Na \( _{5/8} \) BC</td><td>P2/m</td><td>mP21</td><td>10.9</td><td>0.14</td><td>0.19</td><td>0.51</td><td>1.0</td><td>-</td></tr><tr><td>Mg \( _{4/5} \) B \( _{2} \) C \( _{2} \)</td><td>C2221</td><td>oS48</td><td>0.0</td><td>0.06</td><td>0.23</td><td>0.99</td><td>20.8</td><td>57</td></tr><tr><td>Mg \( _{3/4} \) B \( _{2} \) C \( _{2} \)</td><td>P2</td><td>mP19</td><td>22.0</td><td>0.05</td><td>0.26</td><td>0.97</td><td>18.8</td><td>59</td></tr><tr><td>Mg \( _{2/3} \) B \( _{2} \) C \( _{2} \)</td><td>P62m</td><td>hP7</td><td>0.0</td><td>0.00</td><td>0.27</td><td>1.12</td><td>28.7</td><td>73</td></tr></table>

lations for the hP7 (AA) and hP14 (AA',  \( P6_{3}/mcm \) )  \( Mg_{2/3}B_{2}C_{2} \)  variants, shown in Fig. 4(i)-(ii). The primary difference between them is a more pronounced dispersion of the  \( C-p_{z} \)  states along the  \( \Gamma-A \)  direction in the AA-stacked structure due to a larger interlayer overlap of the  \( p_{z} \)  orbitals centered on the vertically aligned C atoms (Fig. S3 [59]). While the stacking shift causes a significant rearrangement of the conduction states near 1.5 eV, it has a negligible effect on the total DOS( \( E_{F} \) ), the isotropic e-ph coupling (Fig. S6 [59]), or the anisotropic  \( T_{c} \)  (Fig. S9 [59]). We checked the sensitivity of the results to the choice of the functional by examining hP7 in both optB86b and optB88 approximations. The latter produces a slightly larger 0.3% interlayer spacing, a close in-plane lattice constant within 0.1%, a 5 meV softening of the bond-stretching BC modes lying near 80 meV, an 8% boost in the isotropic  \( \lambda \) , and a 10 K increase in  \( T_{c} \)  (Figs. S4, S6, S7 and S9 [59]).

The total e-ph coupling strengths in the majority of the examined layered borocarbides are near 1.0, but the Eliashberg spectral functions plotted in Figs. S4 and S5 [59] help appreciate the different make-ups of the integral values. In the Mg-intercalated phases, only about half of the e-ph coupling comes from the BC bond-stretching phonon modes with frequencies above 75 meV, with the other half determined primarily by mixed soft modes below 50 meV. The soft modes were found to play a similarly important role in our study of the  \( Li_{x}BC \)  and  \( Li_{x}{M}_{y}BC \)  materials [27]. In the Na borocarbides with x = 7/8 and x = 3/4, the bond-stretching modes soften significantly, down to 60 meV, and make a dominant contribution, between 70% and 80%, to the total coupling. In this respect, the two phases bear stronger resemblance to the  \( MgB_{2} \)  superconductor [27, 69]. Fittingly, calculations of the superconducting  \( T_{c} \)  with the anisotropic full-bandwidth Migdal-Eliashberg equations result in gap functions with a  \( MgB_{2} \) -like two-gap structure, vanishing at 57 K, 59 K, 73 K, 88 K, and 84 K for the  \( 0S48-Mg_{4}/5B_{2}C_{2} \) , mP19- \( Mg_{3/4}B_{2}C_{2} \) , and hP7- \( Mg_{2/3}B_{2}C_{2} \) , mP23- \( Na_{7/8}BC \) , and oP22- \( Na_{3/4}BC \)  phases, respectively (Figs. S7 and S8 [59]).
The consistently high ab initio  \( T_{c} \)  values obtained for this set, as well as for a number of layered Li-Mg-B [69] and  \( Li_{x}M_{y}BC \)  compounds [27], make it seem that any material with ordered hole-doped honeycomb frameworks should have robust phonon-mediated superconductivity, a notion not borne out by experiments on  \( Li_{x}BC \)  [20–26] or  \( Mg_{0.5}Li_{0.8}B_{2}C_{2} \)  [32]. In addition to showing a  \( T_{c} \)  reduction caused by BC layer buckling and an effective superconductivity suppression caused by BC layer bridging or disorder, we use  \( 0S32-Na_{2/3}BC \)  and mP21- \( Na_{5/8}BC \)  as examples to further illustrate the detrimental effect relatively moderate deviations from the perfect planar morphology can have on the e-ph coupling.

At first glance, oS32- \( Na_{2/3}BC \)  with a high 0.12- \( \AA \)  average buckling appears to be an even better candidate for high- \( T_{c} \)  superconductivity because of the highest DOS( \( E_{F} \) )=0.32 states/(eV atom) and  \( \lambda = 1.32 \)  among the considered Na borocarbides (Figs. 8(e) and S5 [59]). However, the distribution of the electronic states and the breakdown of  \( \lambda \)  contributions set it apart from the examined phases with higher Na content. Just as the curvature of C layers in nanotubes makes the valence states acquire a mixed  \( sp^{2}/sp^{3} \)  hybrid character [73], the distortion of the BC layers in this partially deintercalated metal borocarbide causes a consequential realignment of the C-p states (we will refer to the in-plane and out-of-plane directions as z and  \( (x,y) \)  regardless of the orientation of the unit cell). Namely, a 0.5 eV gap opens up between the  \( p_{z} \)  and  \( p_{x,y} \)  states around -0.5 eV along the R-A and X-S directions, and the separation between the  \( p_{x,y} \)  states along  \( \Gamma-Z \)  increases to about 1 eV, which reshapes the outer Fermi surface cylinders from the upper  \( p_{x,y} \)  states at 1 eV and collapses the inner ones from the lower sets that are now essentially at the Fermi level (Fig. 8(f)). As a result, the largest contribution to the e-ph coupling comes not from the bond-stretching BC phonon modes, but rather from low-frequency manifold with predominantly Na character (Fig. S5 [59]). The superconducting gap function does not have the two typical distinct gaps (Fig. S8 [59]) and the  \( T_{c} \)  can be expected to be around 43 K, but an unusually slow convergence in the
 
![](./images/1019853012262191105_18.jpg)

![](./images/1019853012262191105_19.jpg)

![](./images/1019853012262191105_20.jpg)

![](./images/1019853012262191105_21.jpg)

![](./images/1019853012262191105_22.jpg)

FIG. 8. Electronic properties of (a),(b),(c) mP23-Na \( _{7/8} \) BC, (d),(e),(f) oS32-Na \( _{2/3} \) BC, and (g),(h),(i) mP21-Na \( _{5/8} \) BC. The left (middle) panels show band structures with orbital character (total and projected DOS). The right panels show Fermi surfaces where colors are used to show (c),(f) the value of the superconducting gap at 10 K or (i) the band index. mP23-Na \( _{7/8} \) BC possesses the signature MgB \( _{2} \) -like Fermi surface cylinders, while the other two phases with large BC layer buckling do not.

iterative solution of the aME equations, presumably due to the presence of a sharp DOS peak at  \( E_{F} \) , introduces a higher degree of uncertainty in this estimate.

The mP21-Na_{5/8}BC phase with the largest  \( d_{avg} = 0.14 \)  Å has a total DOS(E_{F}) value of 0.19 states/(eV atom) comparable to those in Na_{x>2/3}BC (Figs. 8 and S2 [59]). The Eliashberg spectral function also has a well-defined maximum corresponding to the BC bond-stretching vibrations, but the peak is localized around 90 meV instead of spreading over a broad range and attaining its highest value at  \( \sim65 \)  meV. This indicates the lack of the characteristic phonon softening and leads to a net e-ph coupling value of only 0.51 (Fig. S5 [59]). The band structure plot in Fig. 8(g) reveals that, just as in oS32-Na_{2/3}BC, the corrugation of the BC layer pushes the C-p_{x,y} states further apart to 1 eV along  \( \Gamma - Z \) . Despite the lower pair of the p_{x,y} bands remaining hole-doped and generating the inner Fermi cylinders, the outer ones are no longer discernible (Fig. 8(i)). Given the low value of  \( \lambda \)  and the 1 K estimate of the Allen-Dynes T_{c}, we did not attempt aME calculations for this phase.

Table I summarizes the aME results for Na and Mg borocarbides at all examined compositions. The  \( T_{c} \)  values in the Mg phases trend upward from 57 K to 73 K with decreasing x, closely following the aME estimates obtained for  \( Li_{x}BC \)  at the matching levels of the electron count [27]. The highest  \( T_{c} \)  of 88 K for the Na phases, on the other hand, is found in the least hole-doped mP23-Na \( _{7/8} \) BC that lies above the local convex hull. The factor of two  \( T_{c} \)  reduction in oS32-Na \( _{2/3} \) BC with higher doped but significantly more puckered BC layers is in qualitative agreement with the trend found for  \( Li_{1/2}BC \)  [27].
 

However, our findings for mP21-Na_{5/8}BC raise a question whether buckling alone could suppress superconductivity at other possible compositions or decorations not sampled in this study.

A systematic screening of superconducting properties at the highest level of theory would be difficult to carry out because of the prohibitively high computational cost of aME calculations. Several simple descriptors have been proposed in previous studies to detect specific signs of the  \( MgB_{2} \) -type superconductivity. For example, the difference between  \( \Gamma \) - and M-point bond-stretching phonon frequencies was found to be a suitable proxy for phonon softening in metal borides with hexagonal unit cells [6], while a zone-center descriptor involving the comparison of screened phonon frequencies ( \( \omega \) ) obtained via standard calculations versus unscreened phonon frequencies ( \( \tilde{\omega} \) ) obtained by fixing the occupation number in the finite displacement method was shown to provide estimates of the e-ph coupling [74]. Unfortunately, the application of the descriptors to the metal borocarbides proved to be not straightforward because of the large size and low symmetry of the considered structures and we opted for a manual inspection of the relevant electronic structure features. In order to distinguish between the electron count and BC layer corrugation factors, we focused on two representative compositions,  \( Na_{5/8}BC \)  and  \( Mg_{3/4}B_{2}C_{2} \) , and considered an additional 8 Na and 7 Mg phases within 100 meV/atom from the respective most stable configuration. Upon examination of their band structures and Fermi surfaces, we confirm that all 3 Na and 4 Mg structures with the average buckling above 0.12 Å have absent, distorted, or reduced Fermi surface cylinders (Figs. S12 and S13 [59]). The results provide evidence that buckling is indeed a major factor capable of suppressing phonon-mediated superconductivity at various metal borocarbide stoichiometries.

[1] J. Nagamatsu, N. Nakagawa, T. Muranaka, Y. Zenitani, and J. Akimitsu, Superconductivity at 39 K in magnesium diboride, Nature 410, 63 (2001).

[2] J. Pelleg, M. Rotman, and M. Sinder, Borides of Ag and Au prepared by magnetron sputtering, Physica C: Superconductivity 466, 61 (2007).

[3] A. N. Kolmogorov and S. Curtarolo, Theoretical study of metal borides stability, Physical Review B 74, 224507 (2006).

[4] A. N. Kolmogorov and S. Curtarolo, Prediction of different crystal structure phases in metal borides: A lithium monoboride analog to  \( MgB_{2} \) , Physical Review B 73, 180501 (2006).

[5] M. Calandra, A. N. Kolmogorov, and S. Curtarolo, Search for high  \( T_{c} \)  in layered structures: The case of LiB, Physical Review B 75, 144506 (2007).

[6] A. N. Kolmogorov, M. Calandra, and S. Curtarolo, Thermodynamic stabilities of ternary metal borides: An ab

## IV. Conclusions

Our ab initio investigation into the stability of Na and Mg borocarbides uncovers layered oP22-Na_{3/4}BC, oS32-Na_{2/3}BC, oS80-Na_{1/2}BC, oS48-Mg_{4/5}B_{2}C_{2}, and hP14-Mg_{2/3}B_{2}C_{2} (P6_{3}/mcm) phases as the most likely products of high-temperature deintercalation of the respective fully-loaded NaBC and MgB_{2}C_{2} materials. The proposed (T, P_{M}) diagrams establish temperature and Na_{2} (Mg) gas partial pressure conditions defining phase boundaries between the metal borocarbides as long as they retain the layered BC morphology. The deintercalation of NaBC requires much lower temperatures and may produce Na_{x}BC derivatives with fewer defects in the BC honeycomb layers. Examination of layered Na and Mg borocarbides at various compositions with aME reveals that buckling of the covalent honeycomb BC networks, that tends to occur in heavily deintercalated Na_{2/3>x}BC, can effectively suppress MgB_{2}-type superconductivity. Fortunately, our aME calculations indicate that all accessible hole-doped phases identified in this study should have high T_{c} between 43 K and 84 K. We hope that the combination of the extensive experimental knowledge of the related Li and Mg borocarbides and the present ab initio findings can guide the synthesis of new ambient-pressure high-T_{c} superconductors.

## Acknowledgments

The authors acknowledge support from the National Science Foundation (NSF) (Award No. DMR-2320073). This work used the Frontera supercomputer at the Texas Advanced Computing Center via the Leadership Resource Allocation (LRAC) award DMR22004 and the Expanse system at the San Diego Supercomputer Center through the NSF-supported ACCESS program (allocation TG-DMR180071).

initio guide for synthesizing layered superconductors, Physical Review B 78, 094520 (2008).

[7] A. N. Kolmogorov, S. Hajinazar, C. Angyal, V. L. Kuznetsov, and A. P. Jephcoat, Synthesis of a predicted layered LiB via cold compression, Phys. Rev. B 92, 144110 (2015).

[8] R. J. Cava, H. W. Zandbergen, and K. Inumaru, The substitutional chemistry of  \( MgB_{2} \) , Physica C: Supercond. 385, 8 (2003).

[9] A. Bianconi, Y. Busby, M. Fratini, V. Palmisano, L. Simonelli, M. Filippi, S. Sanna, F. Congiu, A. Saccone, M. Giovannini, and S. De Negri, Controlling the Critical Temperature in  \( Mg_{1-x}Al_{x}B_{2} \) , J. Supercond. Nov. Magn. 20, 495 (2007).

[10] J. Karpinski, N. D. Zhigadlo, S. Katrych, K. Rogacki, B. Batlogg, M. Tortello, and R. Puzniak,  \( MgB_{2} \)  single crystals substituted with Li and with Li-C: Structural and superconducting properties, Phys. Rev. B 77, 214507
 

(2008).

[11] P. Parisiades, E. Liarokapis, N. D. Zhigadlo, S. Katrych, and J. Karpinski, Raman Investigations of C-, Li- and Mn-Doped  \( MgB_{2} \) , J. Supercond. Nov. Magn. 22, 169 (2009).

[12] M. Calandra and F. Mauri, Theoretical Explanation of Superconductivity in  \( C_{6}C_{a} \) , Physical Review Letters 95, 237002 (2005).

[13] I. Mazin, Intercalant-Driven Superconductivity in  \( YbC_{6} \)  and  \( CaC_{6} \) , Physical Review Letters 20375, 10.1103/PhysRevLett.95.227001 (2005).

[14] E. R. Margine, H. Lambert, and F. Giustino, Electron-phonon interaction and pairing mechanism in superconducting Ca-intercalated bilayer graphene, Scientific Reports 6, 10.1038/srep21414 (2016).

[15] M. Wörle, R. Nesper, G. Mair, M. Schwarz, and H. G. Von Schnering, LiBC—ein vollständig interkalierter heterography, Z. fur Anorg. Allg. Chem. 621, 1153 (1995).

[16] M. Wörle and R. Nesper,  \( MgB_{2}C_{2} \) , a new graphite-related refractory compound, J. Alloys Compd. 216, 75 (1994).

[17] P. Ravindran, P. Vajeeston, R. Vidya, A. Kjekshus, and H. Fjellvåg, Detailed electronic structure studies on superconducting  \( MgB_{2} \)  and related compounds, Phys. Rev. B 64, 224509 (2001).

[18] H. Rosner, A. Kitaigorodsky, and W. E. Pickett, Prediction of high  \( T_{c} \)  superconductivity in hole-doped LiBC, Phys. Rev. Lett. 88, 127001 (2002).

[19] J. K. Dewhurst, S. Sharma, C. Ambrosch-Draxl, and B. Johansson, First-principles calculation of superconductivity in hole-doped LiBC:  \( T_{c} \)  65 K, Phys. Rev. B 68, 020504 (2003).

[20] A. Bharathi, S. J. Balaselvi, M. Premila, T. Sairam, G. Reddy, C. Sundar, and Y. Hariharan, Synthesis and search for superconductivity in LiBC, Solid State Commun. 124, 423 (2002).

[21] Y. Nakamori and S. ichi Orimo, Synthesis and characterization of single phase  \( Li_{x}BC \)  (x=0.5 and 1.0) using Li hydride as a starting material, J. Alloys Compd. 370, L7 (2003).

[22] L. Zhao, P. Klavins, and K. Liu, Synthesis and properties of hole-doped  \( Li_{1-x}BC \) , J. Appl. Phys. 93, 8653 (2003).

[23] A. M. Fogg, J. B. Claridge, G. R. Darling, and M. J. Rosseinsky, Synthesis and characterisation of  \( Li_{x}BC \) —hole doping does not induce superconductivity, Chem. Commun. 3, 1348 (2003).

[24] A. M. Fogg, P. R. Chalker, J. B. Claridge, G. R. Darling, and M. J. Rosseinsky, LiBC electronic, vibrational, structural, and low-temperature chemical behavior of a layered material isoelectronic with  \( MgB_{2} \) , Phys. Rev. B 67, 245106 (2003).

[25] A. M. Fogg, J. Meldrum, G. R. Darling, J. B. Claridge, and M. J. Rosseinsky, Chemical control of electronic structure and superconductivity in layered borides and borocarbides: understanding the absence of superconductivity in  \( Li_{x}BC \) , J. Am. Chem. Soc. 128, 10043 (2006).

[26] B. Kalkan and E. Ozdas, Staging phenomena in lithium-intercalated boron–carbon, ACS Appl. Mater. Interfaces 11, 4111 (2019).

[27] C. R. Tomassetti, G. P. Kafle, E. T. Marcial, E. R. Margine, and A. N. Kolmogorov, Prospect of high-temperature superconductivity in layered metal borocarbides, Journal of Materials Chemistry C 12, 4870 (2024).

[28] A. K. Verma, P. Modak, D. M. Gaitonde, R. S. Rao, B. K. Godwal, and L. C. Gupta, Possible high-temperature superconductivity in hole-doped  \( MgB_{2}C_{2} \) , Europhysics Letters (EPL) 63, 743 (2003).

[29] T.-T. Pham and D.-L. Nguyen, First-principles prediction of superconductivity in  \( MgB_{3}C_{3} \) , Physical Review B 107, 134502 (2023).

[30] E. Spanò, M. Bernasconi, and E. Kopnin, Electron-phonon interaction in hole-doped  \( MgB_{2}C_{2} \) , Physical Review B 72, 014530 (2005).

[31] T. Mori, Investigation of Superconductivity in Isoelectronic and Related Compounds of  \( MgB_{2} \) , Journal of the Physical Society of Japan 71, 323 (2002).

[32] T. Mori and E. Takayama-Muromachi, Hole doping of  \( MgB_{2}C_{2} \) , a  \( MgB_{z} \)  related  \( [B/C] \)  layered compound, Current Applied Physics 4, 276 (2004).

[33] R. Miao, G. Huang, and J. Yang, First-principles prediction of  \( MgB_{2} \) -like NaBC: A more promising high-temperature superconducting material than LiBC, Solid State Communications 233, 30 (2016).

[34] P. P. Singh, Hole-doped, high-temperature superconductors  \( Li_{x}BC \) ,  \( Na_{x}BC \)  and  \( C_{x} \) : a coherent-potential-based prediction, Solid State Communications 124, 25 (2002).

[35] S. Delacroix, F. Igoa, Y. Song, Y. L. Godec, C. Coelho-Diogo, C. Gervais, G. Rousse, and D. Portehault, Electron Precise Sodium Carborbide Nanocrystals from Molten Salts: Single Sources to Boron Carbides, Inorg. Chem. 60, 4252 (2021).

[36] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).

[37] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50, 17953 (1994).

[38] A. N. Kolmogorov and V. H. Crespi, Registry-dependent interlayer potential for graphitic systems, Phys. Rev. B 71, 235415 (2005).

[39] S. Lebègue, J. Harl, T. Gould, J. G. Ángyán, G. Kresse, and J. F. Dobson, Cohesive properties and asymptotics of the dispersion interaction in graphite by the random phase approximation, Phys. Rev. Lett. 105, 196401 (2010).

[40] J. Ning, M. Kothakonda, J. W. Furness, A. D. Kaplan, S. Ehlert, J. G. Brandenburg, J. P. Perdew, and J. Sun, Workhorse minimally empirical dispersion-corrected density functional with tests for weakly bound systems: r2SCAN+rVV10, Phys. Rev. B 106, 075422 (2022).

[41] J. Klimeš, D. R. Bowler, and A. Michaelides, Van der Waals density functionals applied to solids, Phys. Rev. B 83, 195131 (2011).

[42] J. Klimeš, D. R. Bowler, and A. Michaelides, Chemical accuracy for the van der Waals density functional, J. Phys. Condens. Matter 22, 022201 (2010).

[43] J. W. Furness, A. D. Kaplan, J. Ning, J. P. Perdew, and J. Sun, Accurate and Numerically Efficient  \( r^{2} \) SCAN Meta-Generalized Gradient Approximation, J. Phys. Chem. Lett. 11, 8208 (2020).

[44] H. J. Monkhorst and J. D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13, 5188 (1976).

[45] S. Hajinazar, A. Thorn, E. D. Sandoval, S. Kharabadze, and A. N. Kolmogorov, MAISE: Construction of neural network interatomic models and evolutionary structure optimization, Comput. Phys. Commun. 259, 107679
 

(2021).

[46] A. Togo and I. Tanaka, First principles phonon calculations in materials science, Scr. Mater. 108, 1 (2015).

[47] S. Kharabadze, M. Meyers, C. R. Tomassetti, E. R. Margine, I. I. Mazin, and A. N. Kolmogorov, Thermodynamic stability of Li–B–C compounds from first principles, Phys. Chem. Chem. Phys. 25, 7344 (2023).

[48] A. Thorn, D. Gochitashvili, S. Kharabadze, and A. N. Kolmogorov, Machine learning search for stable binary Sn alloys with Na, Ca, Cu, Pd, and Ag, Phys. Chem. Chem. Phys. 25, 22415 (2023).

[49] A. N. Kolmogorov, S. Shah, E. R. Margine, A. F. Bialon, T. Hammerschmidt, and R. Drautz, New Superconducting and Semiconducting Fe-B Compounds Predicted with an Ab Initio Evolutionary Search, Phys. Rev. Lett. 105, 217003 (2010).

[50] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, and M. Cococcioni et al., Advanced capabilities for materials modelling with Quantum ESPRESSO, J. Phys: Condens. Matter 29, 465901 (2017).

[51] T. Thonhauser, V. R. Cooper, S. Li, A. Puzder, P. Hyldgaard, and D. C. Langreth, Van der Waals density functional: Self-consistent potential and the nature of the van der Waals bond, Phys. Rev. B 76, 125112 (2007).

[52] T. Thonhauser, S. Zuluaga, C. A. Arter, K. Berland, E. Schröder, and P. Hyldgaard, Spin signature of nonlocal correlation binding in metal-organic frameworks, Phys. Rev. Lett. 115, 136402 (2015).

[53] K. Berland, V. R. Cooper, K. Lee, E. Schröder, T. Thonhauser, P. Hyldgaard, and B. I. Lundqvist, Van der Waals forces in density functional theory: a review of the vdW-DF method, Rep. Prog. Phys. 78, 066501 (2015).

[54] D. C. Langreth, B. I. Lundqvist, S. D. Chakarova-Käck, V. R. Cooper, M. Dion, P. Hyldgaard, A. Kelkkanen, J. Kleis, L. Kong, and S. Li et al., A density functional for sparse matter, J. Phys: Condens. Matter 21, 084203 (2009).

[55] M. J. van Setten, M. Giantomassi, E. Bousquet, M. J. Verstraete, D. R. Hamann, X. Gonze, and G.-M. Rignanese, The PseudoDojo: Training and grading a 85 element optimized norm-conserving pseudopotential table, Comput. Phys. Commun. 226, 39 (2018).

[56] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77, 3865 (1996).

[57] M. Methfessel and A. T. Paxton, High-precision sampling for Brillouin-zone integration in metals, Phys. Rev. B 40, 3616 (1989).

[58] S. Baroni, S. De Gironcoli, A. Dal Corso, and P. Giannozzi, Phonons and related crystal properties from density-functional perturbation theory, Rev. Mod. Phys. 73, 515 (2001).

[59] See Supplemental Material for Figs. S1-S13 and Table S1.

[60] F. Giustino, M. L. Cohen, and S. G. Louie, Electron-phonon interaction using Wannier functions, Phys. Rev. B 76, 165108 (2007).

[61] S. Poncé, E. R. Margine, C. Verdi, and F. Giustino, EPW: Electron-phonon coupling, transport and superconducting properties using maximally localized Wannier functions, Comput. Phys. Commun. 209, 116 (2016).

[62] E. R. Margine and F. Giustino, Anisotropic Migdal-Eliashberg theory using Wannier functions, Phys. Rev. B 87, 024505 (2013).

[63] H. Lee, S. Poncé, K. Bushick, S. Hajinazar, J. Lafuente-Bartolome, J. Leveille, C. Lian, J.-M. Lihm, F. Macheda, H. Mori, H. Paudyal, W. H. Sio, S. Tiwar, M. Zacharias, X. Zhang, N. Bonini, E. Kioupakis, E. R. Margine, and F. Giustino, Electron-phonon physics from first principles using the EPW code, npj Comput. Mater. 9, 156 (2023).

[64] N. Marzari, A. A. Mostofi, J. R. Yates, I. Souza, and D. Vanderbilt, Maximally localized Wannier functions: Theory and applications, Rev. Mod. Phys. 84, 1419 (2012).

[65] G. Pizzi, V. Vitale, R. Arita, S. Blügel, F. Freimuth, G. Géranton, M. Gibertini, D. Gresch, C. Johnson, and T. Koretsune et al., Wannier90 as a community code: new features and applications, J. Phys: Condens. Matter 32, 165902 (2020).

[66] A. Marrazzo, S. Beck, E. R. Margine, N. Marzari, A. A. Mostofi, J. Qiao, I. Souza, S. S. Tsirkin, J. R. Yates, and G. Pizzi, The Wannier-Functions Software Ecosystem for Materials Simulations (2023), arXiv:2312.10769 [cond-mat.mtrl-sci].

[67] R. Lucrezi, P. P. Ferreira, S. Hajinazar, H. Mori, H. Paudyal, E. R. Margine, and C. Heil, Full-bandwidth anisotropic Migdal-Eliashberg theory and its application to superhydrides, Communications Physics 7, 33 (2024).

[68] H. Mori, T. Nomoto, R. Arita, and E. R. Margine, Efficient anisotropic Migdal-Eliashberg calculations with the Intermediate Representation basis and Wannier interpolation (2024), arXiv:2404.11528 [cond-mat.supr-con].

[69] G. P. Kafle, C. R. Tomassetti, I. I. Mazin, A. N. Kolmogorov, and E. R. Margine, Ab initio study of Li-Mg-B superconductors, Phys. Rev. Mater. 6, 084801 (2022).

[70] K. Momma and F. Izumi, VESTA3 for three-dimensional visualization of crystal, volumetric and morphology data, Journal of Applied Crystallography 44, 1272 (2011).

[71] M. Kawamura, FermiSurfer: Fermi-surface viewer providing multiple representation schemes, Computer Physics Communications 239, 197 (2019).

[72] P. C. Ellgen, Thermodynamics and chemical equilibrium (2014).

[73] T. Dumitrica, C. M. Landis, and B. I. Yakobson, Curvature-induced polarization in carbon nanoshells, Chemical Physics Letters 360, 182 (2002).

[74] Y. Sun, F. Zhang, C.-Z. Wang, K.-M. Ho, I. I. Mazin, and V. Antropov, Electron-phonon coupling strength from ab initio frozen-phonon approach, Phys. Rev. Mater. 6, 074801 (2022).
 
