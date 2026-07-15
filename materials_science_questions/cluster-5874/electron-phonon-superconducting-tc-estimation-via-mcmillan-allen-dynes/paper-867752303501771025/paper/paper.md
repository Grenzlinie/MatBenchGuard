
# Dense superconducting phases of copper-bismuth at high pressure

Maximilian Amsler \( ^{1} \)  and Chris Wolverton \( ^{1,*} \) 

 \( ^{1} \) Department of Materials Science and Engineering,

Northwestern University, Evanston, Illinois 60208, USA

(Dated: February 28, 2022)

Although copper and bismuth do not form any compounds at ambient conditions, two intermetallics, CuBi and  \( Cu_{11}Bi_{7} \) , were recently synthesized at high pressures. Here we report on the discovery of additional copper-bismuth phases at elevated pressures with high-densities from ab initio calculations. In particular, a  \( Cu_{2}Bi \)  compound is found to be thermodynamically stable at pressures above 59 GPa, crystallizing in the cubic Laves structure. In strong contrast to  \( Cu_{11}Bi_{7} \)  and CuBi, cubic  \( Cu_{2}Bi \)  does not exhibit any voids or channels. Since the bismuth lone pairs in cubic  \( Cu_{2}Bi \)  are stereochemically inactive, the constituent elements can be closely packed and a high density of  \( 10.52 \, g/cm^{3} \)  at 0 GPa is achieved. The moderate electron-phonon coupling of  \( \lambda = 0.68 \)  leads to a superconducting temperature of 2 K, which exceeds the values observed both in  \( Cu_{11}Bi_{7} \)  and CuBi, as well as in elemental Cu and Bi.

Intermetallic compounds have been the subject of intense research not only as strengthening precipitates in a wide variety of structural alloys \( ^{1,2} \) , but also for other industrially relevant applications due to their compelling physical properties, ranging from strong permanent magnetism \( ^{3} \)  (e.g.  \( Nd_{2}Fe_{14}B^{4,5} \)  and  \( SmCo_{5}^{6} \) ) and superconductivity (e.g.  \( FeBi_{7}^{2,8} \) ,  \( Ca_{11}Bi_{10-x}^{9,10} \) ,  \( NiBi^{11} \) ,  \( NBi_{3}^{12,13} \) , and  \( CoBi_{3}^{14-16} \) ) to their promising conversion efficiencies in thermoelectric materials \( ^{17} \)  (e.g.  \( FeAs_{2}^{18} \) ,  \( FeSb_{2}^{19} \)  and  \( Bi_{2}Te_{3}^{20} \) ). Recently, binary intermetallics have attracted increasing attention in systems that exhibit severe immiscibility at ambient conditions, but form compounds once exposed to sufficiently high pressures. Although many such high-pressure compounds in immiscible systems had been synthesized in the early 1960s by Matthias et al. \( ^{14} \) , merely a few of them have been so far fully characterized with respect to their crystal structure, composition and properties. Only through the recent advances in experimental high-pressure techniques together with computational methods with high predictive accuracy \( ^{21,22} \)  has it become possible to explore and study such high pressure phases with increasing detail and at a much larger scale.

One such ambient-immiscible system that has proven to be especially rich in high-pressure compounds is Cu–Bi, where two novel phases were discovered since 2016 \( ^{23-25} \) .  \( Cu_{11}Bi_{7} \)  was synthesized at 6 GPa, and crystallizes in a new hexagonal structure related to the NiAs type \( ^{23} \) . It can be recovered to ambient pressure and is a superconductor with a transition temperature of  \( T_{c} = 1.36 \)  K. On the other hand, CuBi was synthesized at 5 GPa and 720 °C \( ^{24,25} \)  in an orthorhombic structure, and has a slightly lower value of  \( T_{c} = 1.3 \)  K. A peculiar structural feature that both phases have in common is the formation of porous voids in their crystal structure.  \( Cu_{11}Bi_{7} \)  exhibits empty channels running along the c-axis of the hexagonal cell, while CuBi contains 2-dimensional empty layers. In fact, we recently demonstrated that CuBi is composed of superconducting 2D sheets, so-called cubine, that are held together through weak van der Waals forces \( ^{26} \) .
Although at first glance the channels and voids in  \( Cu_{11}Bi_{7} \)  and CuBi appear to be empty, they serve a specific purpose in these materials, namely to provide room for hosting the stereochemically active bismuth lone pairs \( ^{23,25} \) . The formation of such porous structures at high pressures is somewhat surprising, since the thermodynamic stability of a solid state compound is governed by the Gibbs free energy,  \( G = E + pV - TS \) , which tends to favor dense structures as the pV term becomes increasingly dominant at higher pressures. Many examples are known where pressure leads to a collapse of low-dimensional structures towards a polymorph with higher packing density, and the transition from graphite to cubic diamond is only one example \( ^{27} \) . Hence, we suspect that also in the Cu–Bi system a high-density phase awaits

(a)

(b)

![](./images/867752303501771025_1.jpg)

FIG. 1. The crystal structure of cubicCu₂Bi from three different perspectives is shown in the panels (a), (b) and (c). Purple (large) and blue (small) spheres denote the Bi and Cu atoms, respectively. The isosurfaces of the ELF are shown at values of 0.9 (red), 0.8 (yellow), 0.7 (green), and 0.6 (blue).
 
![](./images/867752303501771025_2.jpg)

FIG. 2. The electronic band structure in the irreducible Brillouin zone is shown, color coded according to the projection on the Cu and Bi atoms in red and blue, respectively. In the right panel, the total density of states is shown as the shaded area, and the contributions of the Cu d-states, Bi p-states and Bi s-states are indicated by the red, blue and orange lines.

discovery that becomes accessible once a sufficiently high pressure is applied.

To identify these potential high-density phases, we carried out a search by employing the Minima Hopping structure prediction method (MHM) at 10 and 150 GPa with the Minhoaço package \( ^{28,29} \) , which implements a highly reliable algorithm to explore the low enthalpy phases of a compound at a specific pressure solely given the chemical composition \( ^{30-34} \) . Within this method, the low lying part of the enthalpy landscape is efficiently sampled by performing consecutive, short molecular dynamics (MD) escape steps to overcome enthalpy barriers, followed by local geometry optimizations. The Bell-Evans-Polanyi principle is exploited by aligning the initial MD velocities along soft mode directions in order to accelerate the search \( ^{35,36} \) . In the current study, the enthalpy landscape was modeled at the density functional theory (DFT) level, using the projector augmented wave (PAW) formalism \( ^{37} \)  as implemented in the VASP \( ^{38-40} \)  package together with the Perdew-Burke-Ernzerhof (PBE) approximation \( ^{41} \)  to the exchange correlation potential. The most promising candidate structures were refined by performing relaxations in intervals of 10 GPa with a plane-wave cutoff energy of 400 eV and a sufficiently dense k-point mesh to ensure a convergence of the total energy to within 2 meV/atom.

We performed structural searches at variable composition for systems with up to 20 atoms/cell. As intuitively expected, we found novel phases with higher packing densities that become thermodynamically stable at pressures readily accessible with current high-pressure techniques using diamond anvil cells (DAC), i.e. below 100 GPa. A tetragonal  \( Cu_{2}Bi \)  compound with  \( I4/mmm \)  symmetry of  \( La_{2}Sb \)  type, isostructural to  \( Ti_{2}Bi^{42} \) , touches the convex hull of stability at 51 GPa. Its pressure range of stability is however very small and reaches merely up to 59 GPa, above which another  \( Cu_{2}Bi \)  phase in the cubic Laves structure (Strukturbericht designation: C15) with  \( Fd-3m \)  symmetry becomes stable. Since an ordered representation is used to model the disordered  \( Cu_{11}Bi_{7} \)  phase \( ^{23} \) , we believe that our calculations overestimate its formation enthalpy, such that the true stability range of the tetragonal  \( Cu_{2}Bi \)  is even smaller and therefore this phase might not be synthesizeable at all in practice. On the other hand, the cubic  \( Cu_{2}Bi \)  phase has an extended range of stability up to several hundred GPa, rendering it the most promising candidate structure for  \( Cu_{2}Bi \) . We also investigated the two other Laves phases, the hexagonal C14 and C36 structures, which were both found to have higher enthalpies than C15. The structure of the cubic  \( Cu_{2}Bi \)  is shown in Fig. 1 from three different perspectives. A single Cu atom occupies the 16c Wyckoff site at  \( (0,0,0) \) , while a Bi atom occupies the 8b site at  \( (0.375,0.375,0) \) . The lattice constant is 6.77 Å at 60 GPa, and 7.52 Å at ambient pressure, respectively. This crystal structure, which was also observed in the isoelectronic  \( Au_{2}Bi \)  compound \( ^{43} \) , can be interpreted as two interpenetrating sub-lattices of Cu and Bi, where the Bi atoms are arranged in a face centered cubic diamond structure, whereas closely packed Cu tetrahedra occupy the tetrahedral ( \( T_{d} \) ) interstitial sites of the Bi sublattice. The centers of these tetrahedra themselves compose the second diamond sublattice, which are shown as blue polyhedra in Fig. 1.

This picture of interpenetrating diamond lattices is merely an interpretation of the structure, since there are no covalent bonds between the Bi atoms as one would expect from  \( sp^{3} \)  materials like carbon diamond, and the Bi–Bi distance is as large as 3.254 Å at 0 GPa which is significantly higher than the covalent bond length of a single Bi–Bi bond of 3.02 Å. The electronic band structure in Fig. 2 shows that the cubic  \( Cu_{2}Bi \)  is metallic, and like in the two experimentally observed Cu–Bi compounds  \( Cu_{11}Bi_{7} \)  and CuBi, the bands at the Fermi level of cubic  \( Cu_{2}Bi \)  are dominated by the Cu d and Bi p-states, as illustrated by the partial density of states (PDOS) in the right panel. The Bi 6s lone pairs are located deep below the Fermi level, as indicated by the orange lines at the bottom of the PDOS.

Laves phases are known for their high packing efficiencies, and according to our calculations cubic  \( Cu_{2}Bi \)  has a density of  \( \rho = 10.52 \, g/cm^{3} \)  if recovered to ambient pressures. This value is considerably higher than the computed densities of CuBi ( \( \rho = 10.03 \, g/cm^{3} \) ) and  \( Cu_{11}Bi_{7} \)  ( \( \rho = 10.28 \, g/cm^{3} \) ), but also than the decomposition product  \( 2Cu+Bi \)  ( \( \rho = 9.19 \, g/cm^{3} \) ). The dense packing in cubic  \( Cu_{2}Bi \)  suggests that its bonding properties differ strongly from the two previously reported Cu–Bi compounds  \( Cu_{11}Bi_{7} \)  and CuBi. Indeed, the isosurfaces of the electron localization function (ELF) of cubic  \( Cu_{2}Bi \)  in Fig. 1 reveal that the Bi  \( 6s^{2} \)  electrons are localized with spherical symmetry around the bismuth nuclei. Hence, the Bi lone pairs are stereochemically in-
 
![](./images/867752303501771025_3.jpg)

(a) Stability range

![](./images/867752303501771025_4.jpg)

FIG. 3. (a) The stability range of the different Cu–Bi polymorphs are shown as a function of pressure. The dashed line representing the CuBi phase indicates that it is only stable at elevated temperatures. (b) The convex hull of stability at 100 GPa (red) and at 300 GPa (blue). Thermodynamically stable phases are denoted by black circles.

active, in strong contrast to both  \( Cu_{11}Bi_{7} \)  and CuBi.

From the energetic point of view, cubic  \( Cu_{2}Bi \)  is metastable with respect to elemental decomposition by about 160 meV/atom at ambient conditions. Although this value is considerably higher than for  \( Cu_{11}Bi_{7} \)  (55 meV/atom) or CuBi (48 meV/atom), it is within the energy window of observed metastable materials \( ^{44} \) . In comparison, the recently predicted high-pressure phase  \( FeBi_{2} \)  (transition pressure 36 GPa) in a similar chemical system has a formation energy of above 240 meV/atom at 0 GPa \( ^{7} \) , but was nevertheless synthesized and quenched to as low as 3 GPa \( ^{8} \) . Since the MHM explores the energy landscape using physical MD moves, we additionally performed six short MHM simulation at ambient pressure to assess the kinetic stability of cubic  \( Cu_{2}Bi \) , starting from the C15 structure in a 12 atom cell. The lowest energy structure found within the first successful MD escape trial is roughly 30 meV/atom higher in energy than the C15 phase (found by 5 out of the 6 runs), requiring a kinetic energy corresponding to around 1200 K. Although this value doesn’t directly correspond to a physical temperature, it gives a rough estimate of the upper bound for the transition barrier. The preferred escape towards a higher energy state indicates that there is no direct downhill path to a lower energy structure, and therefore that the C15 structure is in a well of a funnel surrounded by high barriers \( ^{45} \) . Hence, we expect that cubic  \( Cu_{2}Bi \)  can be quenched and recovered to ambient pressure as a third metastable Cu–Bi phase.

Fig. 3a shows the pressure range of stability of all Cu–

![](./images/867752303501771025_5.jpg)

FIG. 4. The phonon band structure is shown along a path in the Brillouin zone. The color coding represents the factional mode contribution of the Cu and Bi atoms to the phonon eigenmodes in red and blue, respectively.

Bi phases known to date, together with the two  \( Cu_{2}Bi \)  structures, as a function of pressure, derived from the formation enthalpy at zero temperature. Note that the bar representing CuBi is drawn as dashed line to indicate that it is not a stable phase at 0 K, but only becomes thermodynamically accessible at elevated temperatures as we recently demonstrated in Ref. 25. A striking feature of Fig. 3a is that, already at moderate pressures up to 100 GPa, phases with a higher Cu content are favored as the pressure increases. This trend can be explained by a simple argument based on the large difference in atomic radii of Cu and Bi: a preferred high packing density at extreme pressures is only possible when the fraction of the smaller Cu atoms increases to fill the gaps between the large Bi atoms.

This trend carries on for the phase space at pressures exceeding 100 GPa, where we discovered at least three additional Cu–Bi compounds that become thermodynamically stable with even larger Cu content than  \( \frac{2}{3} \) , as shown in Fig. 3a. First, a  \( Cu_{4}Bi \)  phase touches the convex hull of stability at a pressure of about 130 GPa, which crystallizes in a monoclinic  \( P2_{1}/m \)  structure. At 148 GPa, a hexagonal structure with  \( P6_{3}/mmc \)  symmetry becomes stable at the  \( Cu_{3}Bi \)  composition. Finally, we find a  \( Cu_{6}Bi \)  phase in a  \( P2_{1}/m \)  structure at pressures above 267 GPa, as shown by the blue convex hull plot in Fig. 3b. The structural features of those three phases strongly differ from CuBi,  \( Cu_{11}Bi_{7} \)  and both  \( Cu_{2}Bi \)  phases. They all share the same motif of Bi atoms coordinated to 12 Cu atoms, which form the corners of a cuboctahedron. In fact, all structures are identical to those previously reported in the  \( XeNi_{n} \)  and  \( XeFe_{n} \)  systems \( ^{46} \) , where the individual cuboctahedra are linked together in different geometries. The detailed structural data are given in the supplemental materials.

Since cubic  \( Cu_{2}Bi \)  is the phase that becomes stable at the lowest pressure besides  \( Cu_{11}Bi_{7} \)  and CuBi with
 
![](./images/867752303501771025_6.jpg)

FIG. 5. The electron-phonon coupling properties are shown in the top panel as a function of the phonon frequency  \( \omega \) , where  \( \alpha^{2}F(\omega) \)  denotes the Eliashberg spectral function, while  \( \lambda(\omega) \)  is the electron-phonon coupling strength. In the bottom panel the total phonon density of states (PHDOS) is shown with the shaded area, whereas the partial density of states of the Cu and the Bi atoms are shown in red and blue, respectively.

a wide pressure range of stability, we will from hereon focus solely on a detailed characterization of this phase. To assess if cubic  \( Cu_{2}Bi \)  is dynamically stable at ambient conditions, i.e. if it corresponds to a local minimum on the energy landscape, we computed its phonon dispersion in the whole Brillouin zone using linear response calculations as implemented in the Quantum Espresso package \( ^{47} \) . Norm conserving pseudopotentials were used with a plane-wave cutoff energy of 150 Ry, and the force constants were evaluated on a q-grid of  \( 4 \times 4 \times 44 \) . Fig. 4 shows that all phonon frequencies are real, indicating that the structure is indeed dynamically stable. The bands are colored according to the contributions of the Cu and Bi atoms to the phonon eigenmodes at each wave vector. Similar to  \( Cu_{11}Bi_{7} \)  and CuBi, the low energy phonons are dominated by the vibration of the heavy Bi atoms, while the high-frequency modes stem mainly from the Cu atoms.

We find a remarkable feature in the phonon band structure, where the lowest energy, doubly degenerate transversal acoustic branch is highly localized and does not cross any optical bands. Such vibrations are often referred to as rattling modes and can significantly affect materials properties \( ^{48} \) . In clathrate materials such as  \( Ba_{8}Si_{46} \) , where the guest Ba atoms reside in the cages of the Si host structure, such rattling modes promote the electron-phonon coupling \( ^{49} \)  and lead to its high superconducting temperature of  \( T_{c} = 8 K^{50,51} \) . In a similar manner, the low energy Bi vibrations contribute to the electron-phonon coupling in cubic  \( Cu_{2}Bi \) , as we will show below.

The superconducting transition temperature was computed within the Allan-Dynes modified McMillan’s approximation of the Eliashberg equation \( ^{52} \) , using a Coulomb pseudopotential value of  \( \mu^{*}=0.13 \)  and a dense k-mesh of  \( 24\times24\times24 \) . The resulting overall electron-phonon coupling parameter  \( \lambda=0.68 \)  leads to a moderate  \( T_{c} \)  of 2.0 K at 0 GPa, which is slightly higher than in  \( Cu_{11}Bi_{7} \)  and CuBi. We can relate this difference in  \( T_{c} \)  to the different bonding behavior. As shown in Fig. 5, a large contribution to the electron-phonon coupling constant  \( \lambda \)  stems from a peak in the Eliashberg spectral function  \( \alpha^{2}F \) , located exactly at the frequency of the Bi rattling mode as shown in the lower panel. Although a similar electron-phonon coupling of Bi vibrations is observed both in  \( Cu_{11}Bi_{7}^{23} \)  and  \( CuBi^{25} \) , there is an additional contribution to  \( \lambda \)  from phonons between 2 and 4 THz in cubic  \( Cu_{2}Bi \) , giving rise to the higher value in  \( T_{c} \) .

In summary, we predict from ab initio calculations a set of high-pressure intermetallic compounds in the Cu–Bi system besides the previously synthesized phases, CuBi and  \( Cu_{11}Bi_{7} \) . The compound which becomes stable at the lowest pressures is tetragonal  \( Cu_{2}Bi \) , but the most promising candidate is cubic  \( Cu_{2}Bi \)  which crystallizes in a Laves structure above 59 GPa. In strong contrast to the recently reported  \( Cu_{11}Bi_{7} \)  and CuBi, which both contain voids to host the stereochemically active Bi lone pairs, the structure of cubic  \( Cu_{2}Bi \)  allows a dense packing of the constituent atoms. In agreement with the common perception that materials with voids and low-density structures become increasingly unfavorable at high pressures, cubic  \( Cu_{2}Bi \)  is predicted to be thermodynamically accessible at pressures exceeding 59 GPa due to its high volumetric density. Additionally, cubic  \( Cu_{2}Bi \)  is dynamically stable and we provide evidence that the system is trapped at the bottom of a funnel on the energy landscape, indicating that it can be recovered to ambient pressure. A rattling mode in the phonon band structure of cubic  \( Cu_{2}Bi \)  couples strongly to the electrons, leading to a conventional superconducting transition temperature of  \( T_{c} = 2.0 \)  K exceeding the values in  \( Cu_{11}Bi_{7} \)  and CuBi. At higher pressures above 100 GPa, three additional phases with an even higher copper content are predicted to become thermodynamically stable, namely  \( Cu_{3}Bi \) ,  \( Cu_{4}Bi \) , and  \( Cu_{6}Bi \) . These phases share the same structural motif of interlinked cuboctahedra with 12-coordinated Bi atoms. Overall, the current study contributes to the recent efforts in exploring the phase space of the ambient-immiscible Cu–Bi system, which still bears many potential high-pressure phases awaiting discovery.

## I. ACKNOWLEDGMENTS

M.A. acknowledges support from the Novartis Universitäts Basel Excellence Scholarship for Life Sciences and the Swiss National Science Foundation (P300P2-158407). C.W. acknowledges support by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, under Grant No. DE-FG02-07ER46433. Com-
 

puting resources from the following centers are gratefully acknowledged: the Swiss National Supercomputing Center in Lugano (project s700), the Extreme Science and Engineering Discovery Environment (XSEDE) (which is supported by National Science Foundation grant num-

 \( ^{*} \)  c-wolverton@northwestern.edu

 \( ^{1} \)  J.-F. Nie, Metall and Mat Trans A 43, 3891 (2012).

 \( ^{2} \)  S. C. Wang and M. J. Starink, International Materials Review 50, 193 (2005).

 \( ^{3} \)  J. Fidler, D. Suess, and T. Schrefl, in Handbook of Magnetism and Advanced Magnetic Materials (John Wiley & Sons, Ltd, 2007).

 \( ^{4} \)  J. J. Croat, J. F. Herbst, R. W. Lee, and F. E. Pinkerton, J. Appl. Phys. 55, 2078 (1984).

 \( ^{5} \)  M. Sagawa, S. Fujimura, N. Togawa, H. Yamamoto, and Y. Matsuura, J. Appl. Phys. 55, 2083 (1984).

 \( ^{6} \)  M. G. Benz and D. L. Martin, Appl. Phys. Lett. 17, 176 (1970).

 \( ^{7} \)  M. Amsler, S. S. Naghavi, and C. Wolverton, Chem. Sci. 8, 2226 (2017).

 \( ^{8} \)  J. P. S. Walsh, S. M. Clarke, Y. Meng, S. D. Jacobsen, and D. E. Freedman, ACS Cent. Sci. 2, 867 (2016).

 \( ^{9} \)  M. Sturza, F. Han, C. D. Malliakas, D. Y. Chung, H. Claus, and M. G. Kanatzidis, Phys. Rev. B 89, 054512 (2014).

 \( ^{10} \)  X. Dong and C. Fan, Sci. Rep. 5, 9326 (2015).

 \( ^{11} \)  G. Haegg and G. Funke, Z. Phys. Chem., Abt. B 6, 272 (1929).

 \( ^{12} \)  V. P. Glagoleva and G. S. Zhdanov, Zh. Eksp. Teor. Fiz. 26, 337 (1954).

 \( ^{13} \)  M. Ruck and T. Söhnel, Z. Naturforsch. 61b, 785 (2006).

 \( ^{14} \)  B. T. Matthias, A. Jayaraman, T. H. Geballe, K. Andres, and E. Corenzwit, Phys. Rev. Lett. 17, 640 (1966).

 \( ^{15} \)  U. Schwarz, S. Tencé, O. Janson, C. Koz, C. Krellner, U. Burkhardt, H. Rosner, F. Steglich, and Y. Grin, Angew. Chemie Int. Ed. 52, 9853 (2013).

 \( ^{16} \)  S. Tencé, O. Janson, C. Krellner, H. Rosner, U. Schwarz, Y. Grin, and F. Steglich, J. Phys. Condens. Matter 26, 395701 (2014).

 \( ^{17} \)  P. Sun, N. Oeschler, S. Johnsen, B. B. Iversen, and F. Steglich, Applied Physics Express 2, 091102 (2009).

 \( ^{18} \)  M. J. Buerger, Z. Kristallogr. – Cryst. Mater. 82, 165 (1932).

 \( ^{19} \)  G. Hägg, Z. Kristallogr., Kristallgeom., Kristallphys., Kristallchem. 68, 470 (1928).

 \( ^{20} \)  C. B. Satterthwaite and R. W. Ure, Phys. Rev. 108, 1164 (1957).

 \( ^{21} \)  A. R. Oganov, Modern Methods of Crystal Structure Prediction, 1st ed. (Wiley-VCH Verlag GmbH & Co. KGaA, 2010).

 \( ^{22} \)  L. Zhang, Y. Wang, J. Lv, and Y. Ma, Nature Reviews Materials 2, 17005 (2017).

 \( ^{23} \)  S. M. Clarke, J. P. S. Walsh, M. Amsler, C. D. Malliakas, T. Yu, S. Goedecker, Y. Wang, C. Wolverton, and D. E. Freedman, Angew. Chem. Int. Ed. 55, 13446 (2016).

 \( ^{24} \)  K. Guo, L. Akselrud, M. Bobnar, U. Burkhardt, M. Schmidt, J.-T. Zhao, U. Schwarz, and Y. Grin, Angew. Chem. Int. Ed., n/a (2017).

ber OCI-1053575), the Bridges system at the Pittsburgh Supercomputing Center (PSC) (which is supported by NSF award number ACI-1445606), the Quest high performance computing facility at Northwestern University, and the National Energy Research Scientific Computing Center (DOE: DE-AC02-05CH11231).

 \( ^{25} \)  S. M. Clarke, M. Amsler, J. P. S. Walsh, T. Yu, Y. Wang, Y. Meng, S. D. Jacobsen, C. Wolverton, and D. E. Freedman, Chem. Mater. (2017), 10.1021/acs.chemmater.7b01418.

 \( ^{26} \)  M. Amsler, Z. Yao, and C. Wolverton, arXiv:1704.03038 [cond-mat] (2017), arXiv: 1704.03038.

 \( ^{27} \)  S. Naka, K. Horii, Y. Takeda, and T. Hanawa, Nature 259, 38 (1976).

 \( ^{28} \)  S. Goedecker, J. Chem. Phys. 120, 9911 (2004).

 \( ^{29} \)  M. Amsler and S. Goedecker, J. Chem. Phys. 123, 224104 (2010).

 \( ^{30} \)  M. Amsler, J. A. Flores-Livas, L. Lehtovaara, F. Balima, S. A. Ghasemi, D. Machon, S. Pailhès, A. Willand, D. Caliste, S. Botti, A. San Miguel, S. Goedecker, and M. A. L. Marques, Phys. Rev. Lett. 108, 065501 (2012).

 \( ^{31} \)  J. A. Flores-Livas, M. Amsler, T. J. Lenosky, L. Lehtovaara, S. Botti, M. A. L. Marques, and S. Goedecker, Phys. Rev. Lett. 108, 117004 (2012).

 \( ^{32} \)  M. Amsler, J. A. Flores-Livas, T. D. Huan, S. Botti, M. A. L. Marques, and S. Goedecker, Phys. Rev. Lett. 108, 205505 (2012).

 \( ^{33} \)  S. Botti, M. Amsler, J. A. Flores-Livas, P. Ceria, S. Goedecker, and M. A. L. Marques, Phys. Rev. B 88, 014102 (2013).

 \( ^{34} \)  T. D. Huan, M. Amsler, R. Sabatini, V. N. Tuoc, N. B. Le, L. M. Woods, N. Marzari, and S. Goedecker, Phys. Rev. B 88, 024108 (2013).

 \( ^{35} \)  S. Roy, S. Goedecker, and V. Hellmann, Phys. Rev. E 77, 056707 (2008).

 \( ^{36} \)  M. Sicher, S. Mohr, and S. Goedecker, J. Chem. Phys. 134, 044106 (2011).

 \( ^{37} \)  P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

 \( ^{38} \)  G. Kresse, J. Non-Cryst. Solids 193, 222 (1995).

 \( ^{39} \)  G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).

 \( ^{40} \)  G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

 \( ^{41} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

 \( ^{42} \)  H. Auer-Welsbach, H. Nowotny, and A. Kohl, Monatshefte für Chemie 89, 154 (1958).

 \( ^{43} \)  T. Jurriaanse, Zeitschrift für Kristallographie - Crystalline Materials 90, 322 (2015).

 \( ^{44} \)  W. Sun, S. T. Dacek, S. P. Ong, G. Hautier, A. Jain, W. D. Richards, A. C. Gamst, K. A. Persson, and G. Ceder, Science Advances 2, e1600225 (2016).

 \( ^{45} \)  D. Wales, Energy Landscapes: Applications to Clusters, Biomolecules and Glasses, 1st ed. (Cambridge University Press, 2004).

 \( ^{46} \)  L. Zhu, H. Liu, C. J. Pickard, G. Zou, and Y. Ma, Nat Chem 6, 644 (2014).

 \( ^{47} \)  P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi,
 

R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, J. Phys. Condens. Matter 21, 395502 (2009).

 \( ^{48} \)  J. He, M. Amsler, Y. Xia, S. S. Naghavi, V. I. Hegde, S. Hao, S. Goedecker, V. Ozolins, and C. Wolverton, Phys.

Rev. Lett. 117, 046602 (2016).

 \( ^{49} \)  J. S. Tse, T. Iitaka, T. Kume, H. Shimizu, K. Parlinski, H. Fukuoka, and S. Yamanaka, Phys. Rev. B 72, 155441 (2005).

 \( ^{50} \)  S. Yamanaka, E. Enishi, H. Fukuoka, and M. Yasukawa, Inorg. Chem. 39, 56 (2000).

 \( ^{51} \)  K. Tanigaki, T. Shimizu, K. M. Itoh, J. Teraoka, Y. Moritomo, and S. Yamanaka, Nat Mater 2, 653 (2003).

 \( ^{52} \)  P. B. Allen and R. C. Dynes, Phys. Rev. B 12, 905 (1975).
 
