
# Pressure induced novel compounds in the Hf-O system from first-principles calculations

Jin Zhang \( ^{*} \) 

Department of Geosciences, Center for Materials by Design, and Institute for Advanced Computational Science, State University of New York, Stony Brook, NY 11794-2100, USA

Artem R. Oganov \( ^{\dagger} \) 

Skolkovo Institute of Science and Technology,

Skolkovo Innovation Center, 5 Nobel St., Moscow, 143026, Russia.

Department of Geosciences, Center for Materials by Design,

and Institute for Advanced Computational Science,

State University of New York, Stony Brook, NY 11794-2100, USA

Science and Technology on Thermostructural Composite Materials Laboratory,

International Center for Materials Discovery,

School of Materials Science and Engineering,

Northwestern Polytechnical University,

Xi'an, Shaanxi 710072, PR China and

Moscow Institute of Physics and Technology,

Dolgoprudny, Moscow Region 141700, Russia

Xinfeng Li

State Key Laboratory for Mechanical Behavior of Materials,

School of Materials Science and Engineering,

Xi'an Jiaotong University, Xian, 710049, PR China

Kan-Hao Xue

School of Optical and Electronic Information,

Huazhong University of Science and Technology, Wuhan 430074, China

Zhenhai Wang
 

Peter Grünberg Research Center, Nanjing University of Posts and Telecommunications, Nanjing, Jiangsu 210003, China

Huafeng Dong

College of Physics and Optoelectronic Engineering,

Guangdong University of Technology, Guangzhou 510006, China

## Abstract

Using first-principles evolutionary simulations, we have systematically investigated phase stability in the Hf-O system at pressure up to 120 GPa. New compounds  \( Hf_{5}O_{2} \) ,  \( Hf_{3}O_{2} $ , HfO and  \( HfO_{3} \)  are discovered to be thermodynamically stable at certain pressure ranges and a new stable high-pressure phase is found for  \( Hf_{2}O \)  with space group Pnnm and anti- \( CaCl_{2} \) -type structure. Both  \( P\bar{6}2m \) -HfO and  \( P\bar{4}m2 \) - \( Hf_{2}O_{3} \)  show semimetallic character. Pnnm- \( HfO_{3} \)  shows interesting structure, simultaneously containing oxide  \( O^{2-} \)  and peroxide  \( [O-O]^{2-} \) . Remarkably, it is  \( P\bar{6}2m \) -HfO rather than OII- \( HfO_{2} \)  that exhibits the highest mechanical characteristics among Hf-O compounds. Pnnm- \( Hf_{2}O \) ,  \( Imm2 \) - \( Hf_{5}O_{2} \) ,  \( P\bar{3}1m \) - \( Hf_{2}O \)  and  \( P\bar{4}m2 \) - \( Hf_{2}O_{3} \)  phases also show superior mechanical properties, these phases can be quenched to ambient pressure and their properties can be exploited.
 

## I. INTRODUCTION

Hafnium oxide  \( HfO_{2} \)  has a wide range of technological applications. In electronics industry, hafnium oxide-based material is currently used as an excellent high-k gate dielectric \( ^{1} \)  and oxygen-deficient hafnium oxide also received additional interest for resistive-switching memories \( ^{2} \) . As for other applications, even though the hardness of hafnia ( \( HfO_{2} \) ) is not that high for it to be considered as a superhard material \( ^{3} \) , it still attracts attention as a potential candidate for hard oxide-based materials \( ^{4} \) . Unlike carbides or nitrides, oxides are more stable in the oxygen atmosphere at high temperature, which is valuable for many applications, Many oxide ceramics, especially those involving transition metals, are promising for application as hard coatings, since metal d electrons and strong bonds define their remarkable mechanical properties (high hardness, good chemical resistance, high tensile strength, and good fracture toughness) \( ^{5} \) . As compared to most transition metal oxide ceramics, hafnium oxide ceramics exhibit enhanced mechanical properties (higher fracture toughness) and structural stability (low thermal conductivity). Here, we want to explore all possible stable compounds of Hf-O system at pressure up to 120 GPa.

Under ambient temperature, experiments \( ^{6,7} \)  indicated that pure Hf is stable in the  \( \alpha \) -phase (hexagonal close-packed structure, space group:  \( P6_{3}/mmc \) ) and transforms to  \( \omega \) -phase (hexagonal structure, space group:  \( P6/mmm \) ) at 46-58 GPa and then to  \( \beta \) -Hf (body centered cubic, space group:  \( Im\overline{3}m \) ) at 71.1 GPa-78.4 GPa. Our GGA calculated results indicate the transition pressures:  \( \alpha \) -phase  \( \rightarrow \)   \( \omega \) -phase at 49 GPa and  \( \omega \) -phrase  \( \rightarrow \)   \( \beta \) -Hf at 70 GPa, which are in accord with above experimental results. It has been suggested that the solubility of oxygen in the octahedral interstitial sites of  \( \alpha \) -Hf (hcp-Hf) can be as high as 20 at. \( \%^{8} \) , while solubility of oxygen in  \( \beta \) -Hf (bcc-Hf) is only 3 at. \( \%^{9} \) . Several experimental \( ^{10,11} \)  and theoretical studies \( ^{12,13} \)  have investigated the interstitial oxygen in hcp-Hf. Now it is well established that three stoichiometric compositions  \( Hf_{6}O \) ,  \( Hf_{3}O \)  and  \( Hf_{2}O \)  can be formed with increasing occupation of the octahedral-interstitial positions in hcp-Hf by oxygen atoms.  \( Hf_{2}O_{3} \)  was theoretically predicted to form upon increasing the concentration of oxygen vacancies in monoclinic  \( HfO_{2} \)  \( ^{14} \) .

The phase sequence of  \( HfO_{2} \)  at ambient temperature with increasing pressure is: bad-deleyite (monoclinic, space group:  \( P2_{1}/c \) ) → orthorhombic I (orthorhombic, space group:  \( Pbc_{a} \) , OI) → orthorhombic II (orthorhombic, space group:  \( Pnma \) , OII) \( ^{15-17} \) . Orthorhombic
 

OII-HfO \( _{2} \)  with experimentally reported hardness between 6-13 GPa \( ^{18} \)  has been speculated to be much harder than the low-pressure phases (baddelyite and OI-HfO \( _{2} \) ) because of its comparatively high bulk modulus \( ^{5,19} \) .

In this study, we systematically investigate the structure and stability of Hf-O compounds up to a pressure of 120 GPa by the first-principles evolutionary algorithm USPEX. Several new stoichiometries in the Hf-O system have been predicted under high pressure. Furthermore, we verify the dynamical and mechanical stability of these new high-pressure phases at 0 GPa by calculating their phonons and elastic constants. To better understand the correlations between hardness and O content, we estimate the hardness of these phases at 0 GPa using Chen's hardness model \( ^{20} \) . Quenchable high-pressure phases often possess superior mechanically properties, and we indeed find novel hafnium oxides with unusual mechanical properties.

## II. COMPUTATIONAL METHODOLOGY

Searching the stable high-pressure structures in Hf-O system was done using first-principles evolutionary algorithm (EA) as implemented in the USPEX code \( ^{21-23} \)  combined with ab initio structure relaxations using density functional theory (DFT) with the PBE-GGA functional \( ^{24} \) , as implemented in the VASP package \( ^{25} \) . In our work, variable-composition structure searches \( ^{23} \)  for the Hf-O system with up to 20 atoms in the unit cell were performed at 0 GPa, 10 GPa, 20 GPa, 30 GPa, 40 GPa, 50 GPa, 60 GPa, 70 GPa, 80 GPa, 90 GPa, 100 GPa, 110 GPa and 120 GPa. The initial generation of structures was produced randomly using space group symmetry, each subsequent generation was obtained by variation operators including heredity (40%), lattice mutation (20%), random (20%) and transmutation (20%). The electron-ion interaction was described by the projector-augmented wave (PAW) pseudopotentials \( ^{26} \) , with  \( 5p^{6}6s^{2}5d^{4} \)  and  \( 2s^{2}2p^{4} \)  shells treated as valence for Hf and O, respectively. The generalized gradient approximation (GGA) in the Perdew-Burke-Ernzerhof form \( ^{24} \)  was utilized for describing exchange-correlation effects. The plane-wave energy cutoff was chosen as 600 eV and  \( \Gamma \) -centered uniform k-meshes with resolution  \( 2\pi \times 0.06 \, \AA^{-1} \)  were used to sample the Brillouin zone, resulting in excellent convergence. Phonon dispersions were calculated using the finite-displacement method with the Phonopy code \( ^{27} \) .
 

## III. RESULTS AND DISCUSSIONS

## A. Crystal structure prediction for the Hf-O system

(a)

![](./images/867760589416431851_1.jpg)

(b)

![](./images/867760589416431851_2.jpg)

(c)

![](./images/867760589416431851_3.jpg)

(d)

![](./images/867760589416431851_4.jpg)

![](./images/867760589416431851_5.jpg)

(f)

![](./images/867760589416431851_6.jpg)

FIG. 1. Convex hull diagrams for the Hf-O system at (a) 0 GPa, (b) 20 GPa, (c) 30 GPa, (d) 40 GPa, (e) 50 GPa, and (f) 110 GPa, respectively. Solid squares denote stable phases while open squares represent metastable phases.

Thermodynamic convex hull, which defines stable compounds, is based on the free energies (at T = 0 K, enthalpies) of the compounds and pure elements in their stable forms. The high-pressure convex hull and pressure-composition phase diagram of the Hf-O system are depicted in Fig. 1 and Fig. 2, respectively. Besides the three well-known phases of  \( HfO_{2} \)  and three suboxides ( \( R\bar{3} \) -Hf \( _{6} \) O,  \( R\bar{3}c \) -Hf \( _{3} \) O and  \( P\bar{3}1m \) -Hf \( _{2} \) O), our structure searches found hitherto unknown compounds with new stoichiometries, including  \( Hf_{5}O_{2} \) ,  \( Hf_{3}O_{2} $ , HfO
 
![](./images/867760589416431851_7.jpg)

FIG. 2. Pressure-composition phase diagram of the Hf-O system.

and  \( HfO_{3} \) . Note that a new high-pressure phase of  \( Hf_{2}O \)  (denoted as  \( P_{nnm}-Hf_{2}O \) ) was also found by our searches. Recent work \( ^{28} \)  indicated that  \( Hf_{12}O_{5} \)  is a stable compound at low temperature, disproportionate above 220 K, therefore it is not expected to be observed experimentally. Our work indicates that  \( Hf_{12}O_{5} \)  is actually stable only in the pressure range from 8 GPa to 37 GPa.

Our calculation confirms that  \( Hf_{2}O_{3} \)  proposed by Xue \( ^{14} \)  can exist as a metastable phase (it is dynamically and mechanically stable at 0 GPa), and shows that it should be a stable phase in the pressure range 20-23 GPa. The predicted transition from monoclinic- \( HfO_{2} \)  to OI- \( HfO_2 \)  occurs at 10 GPa, which is coincides with experimental observations \( ^{15} \) . The transition from OI- \( HfO_{2} \)  to OII- \( HfO_2 \)  occurs at 18 GPa, which is lower than the experimental result 30-37 GPa \( ^{3,15} \)  but in good agreement with other theoretical estimates of 17 GPa \( ^{3} \) . Furthermore, our calculated result shows that OII- \( HfO_2 \)  is stable up to at least 120 GPa, which agrees with previous experimental work \( ^{3} \) . According to our predictions, only baddelyeite-type  \( HfO_2 \)  and  \( R\bar{3} \) - \( Hf_{6}O \)  are stable at 0 GPa, in contrast with the Zr-O system ( \( Zr_{6}O \) ,  \( Zr_{3}O \) ,  $ Zr_{2}O, ZrO and ZrO_{2} are stable at 0 GPa) \( ^{29} \) .
 
![](./images/867760589416431851_8.jpg)

FIG. 3. (Color online) Equation of state of  \( Hf_{2}O \) . Our calculations were fit to a third-order Birch-Murnaghan equation of state to find  \( B_{0} \)  and  \( B_{0}^{\prime} \) .

In order to study the ordering of interstitial oxygen atoms in hcp- \( HfO_{x} \) , Hirabayashi et al. \( ^{[10]} \)  used electron, neutron and X-ray diffraction to analyze single crystals containing 13.4 at % O and 15.8 at % O and found two types of interstitial superstructures:  \( HfO_{\frac{1}{6}}^{-} \) and  \( HfO_{\frac{1}{6}}^{-} \) below 600 K. The space group of  \( HfO_{\frac{1}{6}}^{-} \) reported by Hirabayashi \( ^{[10]} \)  is  \( R\bar{3} \) , which is identical to our findings. The space group of  \( HfO_{\frac{1}{6}}^{-} \) is  \( P\bar{3}1c \)  in Hirabayashi' experiment \( ^{[10]} \) . At 0 K and 0 GPa, our results produce three energetically competitive phases for  \( Hf_{3}O \)  and their ordering by energy is  \( R\bar{3}c-Hf_{3}O \)  (-10.075 eV/atom) <  \( P\bar{3}1c-Hf_{3}O \)  (-10.072 eV/atom) <  \( P6_{3}22-Hf_{3}O \)  (-10.069 eV/atom). Therefore, one can note that  \( P\bar{3}1c-Hf_{3}O \)  ( \( P\bar{3}1c-Zr_{3}O \)  type), exhibits very close but higher energy than  \( R\bar{3}c-Hf_{3}O \)  at 0 GPa and 0 K. In order to consider the effects of temperature, quasi-harmonic free-energy of  \( R\bar{3}c-Hf_{3}O \)  and  \( P\bar{3}1c-Hf_{3}O \)  were calculated using the Phonopy code \( ^{[27]} \) . The results indicate that free energy of  \( P\bar{3}1c-Hf_{3}O \)  decreases faster than that of  \( R\bar{3}c-Hf_{3}O \)  with temperature, enabling  \( P\bar{3}1c-Hf_{3}O \)  to become more stable than  \( R\bar{3}c-Hf_{3}O \)  at 1000 K, thus explaining experimental result.

 \( Hf_{2}O \)  undergoes a trigonal-to-orthorhombic phase transition at 58 GPa. The crystal structure of the new high-pressure phase  \( P_{nmm}-Hf_{2}O \)  is of anti- \( CaCl_{2} \) -type. The Birch-
 
![](./images/867760589416431851_9.jpg)

![](./images/867760589416431851_10.jpg)

![](./images/867760589416431851_11.jpg)

(c) C2/m-Hf3O2

![](./images/867760589416431851_12.jpg)

(d) P62m-HfO

![](./images/867760589416431851_13.jpg)

(e) P4m2-Hf2O3

![](./images/867760589416431851_14.jpg)

(f) Pnmm-HfO3

FIG. 4. (Color online) Calculated phonon dispersion curves for the (a)  \( Imm2-Hf_{5}O_{2} \)  at 0 and 60 GPa (b)  \( Pnnm-Hf_{2}O \)  at 0 and 80 GPa (c)  \( C2/m-Hf_{3}O_{2} \)  at 0 and 90 GPa (d)  \( P\overline{62}m-HfO \)  at 0 and 50 GPa (e)  \( P\overline{4}m2-Hf_{2}O_{3} \)  at 0 and 20 GPa (f)  \( Pnnm-HfO_{3} \)  at 0 and 110 GPa. The solid black and dashed blue lines represent the results at zero and high pressures, respectively.

Murnaghan equation of state \( ^{30} \)  was used to fit the compressional behavior of the predicted  \( Hf_{2}O \)  phases (Fig. 3.). The third-order Birch-Murnaghan EOS is given as

 \[ P(V)=\frac{3B_{0}}{2}\left[\left(\frac{V}{V_{0}}\right)^{-\frac{7}{3}}-\left(\frac{V}{V_{0}}\right)^{-\frac{5}{3}}\right]\left\{1+\frac{3}{4}(B_{0}^{^{\prime}}-4)\left[\left(\frac{V}{V_{0}}\right)^{-\frac{2}{3}}-1\right]\right\} \quad (1) \] 

Three parameters are used to describe the EOS: the volume at 0 GPa  \( (V_{0}) \) , the bulk modulus at 0 GPa  \( (B_{0}) \) , and the first pressure derivative of the bulk modulus at 0 GPa  \( (B_{0}^{\prime}) \) . Most materials have  \( 3 \leq B_{0}^{\prime} \leq 6^{31,32} \) . The  \( B_{0}^{\prime} \)  of  \( P\bar{3}1m-Hf_{2}O \)  and  \( Pnnm-Hf_{2}\bar{O} \)  is 4.0 and 3.8, respectively.

## B. Structure character in Hf-O compounds

Table I lists the detailed crystallographic data of  \( Imm2-Hf_{5}O_{2} \) ,  \( Pnnm-Hf_{2}O \) ,  \( C2/m-Hf_{3}O_{2} \) ,  \( P\overline{62}m-HfO \) ,  \( C2/m-Hf_{2}O_{3} \)  and  \( Pnnm-HfO_{3} \) compounds at 0 GPa. The dynamical stabilities of all the new phases are checked by calculating phonon dispersion. As shown in Fig.4, except for  \( HfO_{3} \) , no imaginary phonon frequencies are found in the whole Brillouin zone at both ambient and high pressure, which means that they are dynamically stable and probably quenchable to ambient pressure. In contrast,  \( HfO_{3} \)  is stable only at high pressure, but at 0 GPa shows total dynamical instability and most likely decomposes. The special electronic structure of  \( HfO_{3} \)  will be discussed below. The weighted average lengths of Hf-Hf and Hf-O bonds in Hf-O compounds are plotted in Fig. 5.
 

TABLE I. Structural parameters of Imm2- Hf_{5}O_{2}, Pnnm- Hf_{2}O, C2/m-Hf_{3}O_{2}, P62m-HfO, C2/m-Hf_{2}O_{3} and Pnnm-HfO_{3} at 0 GPa.

<table><tr><td colspan="8">Compound Space group Enthalpy of formation Lattice constants Wyckoff positions</td></tr><tr><td></td><td></td><td>(eV/atom)</td><td>(Å)</td><td></td><td></td><td></td><td></td></tr><tr><td>Hf5O2</td><td>Imm2</td><td>-1.52</td><td>a=14.455</td><td>Hf 4c</td><td>0.711</td><td>0.50</td><td>0.566</td></tr><tr><td></td><td></td><td></td><td>c=3.141</td><td>Hf 2b</td><td>0.00</td><td>0.50</td><td>0.098</td></tr><tr><td></td><td></td><td></td><td></td><td>Hf 4c</td><td>0.097</td><td>0.00</td><td>0.594</td></tr><tr><td></td><td></td><td></td><td>c=5.082</td><td>O 4c</td><td>0.645</td><td>0.00</td><td>0.818</td></tr><tr><td>Hf2O</td><td>Pnnm</td><td>-1.76</td><td>a=5.092</td><td>Hf 4g</td><td>0.263</td><td>0.341</td><td>0.50</td></tr><tr><td></td><td></td><td></td><td>b=5.723</td><td>O 2c</td><td>0.00</td><td>0.50</td><td>0.00</td></tr><tr><td></td><td></td><td></td><td>c=3.175</td><td></td><td></td><td></td><td></td></tr><tr><td>Hf3O2</td><td>C2/m</td><td>-2.04</td><td>a=11.967</td><td>Hf 4i</td><td>0.625</td><td>0.50</td><td>0.007</td></tr><tr><td></td><td></td><td></td><td>b=3.131</td><td>Hf 4i</td><td>0.465</td><td>0.00</td><td>0.346</td></tr><tr><td></td><td></td><td></td><td>c=11.198</td><td>Hf 4i</td><td>0.286</td><td>0.00</td><td>0.676</td></tr><tr><td></td><td></td><td></td><td>\( \beta = 99.67^{\circ} \)</td><td>O 4i</td><td>0.378</td><td>0.50</td><td>0.607</td></tr><tr><td></td><td></td><td></td><td></td><td>O 4i</td><td>0.787</td><td>0.00</td><td>0.192</td></tr><tr><td>HfO</td><td>P62m</td><td>-2.60</td><td>a=5.230</td><td>Hf 1b</td><td>0.00</td><td>0.00</td><td></td></tr><tr><td></td><td></td><td></td><td>c=3.187</td><td>Hf 2c</td><td>0.667</td><td>0.333</td><td>0.00</td></tr><tr><td></td><td></td><td></td><td></td><td>O 3g</td><td>0.00</td><td>0.592</td><td>0.50</td></tr><tr><td>Hf2O3</td><td>P4m2</td><td>-3.11</td><td>a=3.137</td><td>Hf 2g</td><td>0.00</td><td>0.50</td><td>0.744</td></tr><tr><td></td><td></td><td></td><td>c=5.638</td><td>O 2g</td><td>0.00</td><td>0.50</td><td>0.135</td></tr><tr><td></td><td></td><td></td><td></td><td>O 1c</td><td>0.50</td><td>0.50</td><td></td></tr><tr><td>HfO3</td><td>Pnnm</td><td>-2.22</td><td>a=5.554</td><td>Hf 4c</td><td>0.246</td><td>0.110</td><td>0.250</td></tr><tr><td></td><td></td><td></td><td>b=6.457</td><td>O 4c</td><td>0.359</td><td>0.426</td><td>0.250</td></tr><tr><td></td><td></td><td></td><td>c=3.307</td><td>O 4c</td><td>0.025</td><td>0.339</td><td>0.750</td></tr></table>

Structurally, hafnium oxides can be divided into four groups: suboxides with oxygen interstitials in hcp-Hf (Hf \( _{6} \) O, Hf \( _{3} \) O, H \( _{12} \) O \( _{5} \)  and P \( _{31} \) m-Hf \( _{2} \) O); other suboxides (Hf \( _{5} \) O \( _{2} \) , Pnnm-Hf \( _{2} \) O and HfO); normal oxides (Hf \( _{2} \) O \( _{3} \) , HfO \( _{2} \) ) and oxide peroxide (HfO \( _{3} \) ). The octahedral
 
![](./images/867760589416431851_15.jpg)

FIG. 5. (Color online) Average bond lengths in Hf-O compounds at 0 GPa.

sites of hcp hafnium metal are depicted in Fig.6. Oxygen atoms prefer to occupy these octahedral sites and form ordered structures  \( R\bar{3} \) -Hf \( _{6} \) O,  \( R\bar{3} \) c-Hf \( _{3} \) O,  \( R\bar{3} \) -Hf \( _{12} \) O \( _{5} \)  and  \( P\bar{3}1m \) -Hf \( _{2} \) O, as shown in Fig. 7 (a) (b) (c) and (d), where Hf atom sites are omitted. The polyhedral representation of these structures is shown in Fig. 6 (e) (f) (g) and (h). Anti-CaCl \( _{2} \) -type (Pnnm) structure of Hf \( _{2} \) O can also be represented as an hcp-sublattice (distorted) of Hf atoms, where half of octahedral voids are occupied by O atoms. The structure of Hf \( _{3} \) O \( _{2} \)  can be considered to be defective because each layer lacks some Hf atoms to form a Hf-graphene layer. These vacancies are responsible for low values of the mechanical properties of Hf \( _{3} \) O \( _{2} \) .

Similar with ZrO, the structure of HfO contains Hf-graphene layers stacked on top of each other (Zr-Zr distances within the layer are 3.01 Å, and between the layers 3.18 Å), as illustrated in Fig. 8(b), as well as additional Hf and O atoms. The structure can be represented as  \( \omega \) -phase of Hf, intercalated with oxygen atoms. This structure, therefore, is built by a 3D-framework of short and strong Hf-O bonds, reinforced by rather strong
 
![](./images/867760589416431851_16.jpg)

FIG. 6. (Color online) Octahedral voids in hcp hafnium.

Hf-Hf bonds. The former lead to high hardness, the latter may improve toughness due to semimetallic behavior.  \( P\overline{4}m2-Hf_{2}O_{3} \) , which was firstly proposed by Xue \( ^{14} \) , has 8-fold and 6-fold coordination of Hf atoms, as shown in Fig 8.

Pnnm-HfO \( _{3} \)  becomes stable at pressures above to 110 GPa. This high-pressure phase originally derives from oxygen atom dissolving in both octahedral and tetrahedral voids of a heavily distorted hcp-Hf, as shown in Fig 9(a). However, due to short distances between tetrahedral voids in the hcp structures, some O atoms form pairs and as a result HfO \( _{3} \)  simultaneously contains oxide O \( ^{2-} \)  and peroxide  \( [O-O]^{2-} \)  anions, and can be described as "oxide peroxide". The O-O bond length in HfO \( _{3} \)  is 1.44 Å at 110 GPa, which is a little smaller than the O-O bond length in peroxide  \( [O-O]^{2-} \)  ion with 1.47 Å \( ^{33} \)  at ambient conditions. It seems that peroxides and oxide peroxides (e.g. Al \( _{4} \) O \( _{7} \)  and AlO \( _{2} \) ) become stabilized in many systems under pressure \( ^{34} \) .
 
![](./images/867760589416431851_17.jpg)

FIG. 7. (Color online) Oxygen sublattice representation (arrangement of oxygen atoms in the octahedral interstitial sites) and polyhedral representation of (a)&(b)  \( R\overline{3} \) -Hf \( _{12} \) O \( _{5} \)  (c)&(d)  \( P\overline{3} \) 1m-Hf \( _{2} \) O (e)&(f)  \( R\overline{3} \) -Hf \( _{6} \) O (g)&(h)  \( R\overline{3} \) c-Hf \( _{3} \) O. Oxygen-centered octahedra and oxygen vacancies are shown in red and pink polyhedra, respectively. Oxygen sublattice representations (b, d, f, h) show only oxygen atoms (filled circles) and vacancies (open circles).

![](./images/867760589416431851_18.jpg)

FIG. 8. (Color online) Crystal structures of (a)  \( Imm2-Hf_{5}O_{2} \)  (b)  \( P\overline{6}2m-HfO \)  (c)  \( P\overline{4}m2-Hf_{2}O_{3} \)  and (d)  \( P\overline{4}m2-Hf_{2}O_{3} \) . O-centered octahedra and O-centered tetrahedra are shown in red and blue polyhedra, respectively. Large spheres-Hf atoms; small spheres-O atoms.
 
![](./images/867760589416431851_19.jpg)

FIG. 9. (Color online) Crystal structure of (a)  \( Pnnm-HfO_{3} \)  (b)  \( Pnnm-Hf_{2}O \) ; (c)  \( Pnnm-HfO_{3} \)  (d)  \( Pnnm-Hf_{2}O \) .

## C. Mechanical properties of Hf-O compounds

Previous studies \( ^{15,19,35} \)  suggested that dense high-pressure phase OII-HfO \( _{2} \)  is quenchable to ambient conditions and has a high bulk modulus, and might be superhard (H > 40 GPa). However, recent study \( ^{3} \)  reported that the hardness of OII-HfO \( _{2} \)  is well below 40 GPa and therefore this phase is not superhard. Interestingly, our systematic results not only confirm known hardness of HfO \( _{2} \)  polymorphs: H(OII) < H(MI) < H(OI), but also suggest that HfO has the highest hardness among all hafnium oxides, see Fig. 10(f). In addition, Pnnm-Hf \( _{2} \) O and Imm2-Hf \( _{5} \) O \( _{2} \)  also exhibit higher hardness than other Hf-O compounds, as shown in Tab II. The hardness of Hf-O compounds does not monotonically change with O content, but a maximum at HfO.

The calculated modulus B, shear modulus G, Young’s modulus E, Poisson’s ratio v, and hardness of all stable Hf–O compounds are depicted in TableII and Fig.10 (for comparison, the elastic data of the high-pressure phase Pnnm-HfO \( _{3} \)  are reported at 0 GPa although it is unstable at 0 GPa.) From Fig.10 we can conclude that the high O content in the crystal does not guarantee high hardness of Hf-O compounds and the structure plays an important role in determining mechanical properties as we discussed above. The Vickers hardness was calculated according to Chen’s model \( ^{20} \) :

 \[ H_{V}=2*(k^{2}*G)^{0.585}-3 \quad (2) \]
 

TABLE II. Calculated bulk modulus B, shear modulus G, Young's modulus E, Poisson's ratio v and hardness of Hf-O compounds, compared with literature data for  \( HfO_{2} \)  at 0 GPa. All properties are in GPa (except dimensionless G/B and v).

<table><tr><td colspan="2">Compound</td><td>Space group</td><td>P</td><td>B_{H}</td><td>G_{H}</td><td>E</td><td>G/B</td><td>v</td><td>H_{v}</td></tr><tr><td>Hf_{6}O</td><td>This work</td><td>R\bar{3}</td><td>0</td><td>129.2</td><td>72.8</td><td>183.8</td><td>0.56</td><td>0.26</td><td>9.55</td></tr><tr><td>Hf_{3}O</td><td>This work</td><td>R\bar{3}c</td><td>0</td><td>150.3</td><td>78.8</td><td>201.3</td><td>0.52</td><td>0.28</td><td>9.1</td></tr><tr><td>Hf_{5}O_{2}</td><td>This work</td><td>Imm2</td><td>0</td><td>150.0</td><td>95.3</td><td>235.9</td><td>0.64</td><td>0.24</td><td>13.9</td></tr><tr><td>Hf_{12}O_{5}</td><td>This work</td><td>R\bar{3}</td><td>0</td><td>163.3</td><td>94.5</td><td>237.7</td><td>0.58</td><td>0.26</td><td>12.1</td></tr><tr><td>Hf_{2}O</td><td>This work</td><td>P\bar{3}1m</td><td>0</td><td>175.2</td><td>103.1</td><td>258.6</td><td>0.59</td><td>0.25</td><td>13.2</td></tr><tr><td>Hf_{2}O</td><td>This work</td><td>Pnnm</td><td>0</td><td>173.0</td><td>110.3</td><td>272.9</td><td>0.64</td><td>0.23</td><td>15.5</td></tr><tr><td>Hf_{3}O_{2}</td><td>This work</td><td>C^{2}/m</td><td>0</td><td>154.2</td><td>75.9</td><td>195.6</td><td>0.49</td><td>0.29</td><td>8.0</td></tr><tr><td>HfO</td><td>This work</td><td>P\bar{6}2m</td><td>0</td><td>210.7</td><td>128.1</td><td>319.5</td><td>0.61</td><td>0.25</td><td>16.1</td></tr><tr><td>Hf_{2}O_{3}</td><td>This work</td><td>P\bar{4}m2</td><td>0</td><td>243.9</td><td>127.1</td><td>324.8</td><td>0.52</td><td>0.28</td><td>12.9</td></tr><tr><td>HfO_{2}</td><td>This work</td><td>P2_{1}/c</td><td>0</td><td>203.6</td><td>99.2</td><td>256.1</td><td>0.49</td><td>0.29</td><td>9.7</td></tr><tr><td></td><td>Experiment^{36}</td><td></td><td>0</td><td></td><td></td><td></td><td></td><td>9.9</td><td></td></tr><tr><td>HfO_{2}</td><td>This work</td><td>Pbca</td><td>0</td><td>225.9</td><td>115.8</td><td>296.6</td><td>0.51</td><td>0.28</td><td>11.7</td></tr><tr><td>HfO_{2}</td><td>This work</td><td>Pnma</td><td>0</td><td>226.3</td><td>93.8</td><td>247.3</td><td>0.41</td><td>0.31</td><td>7.2</td></tr><tr><td></td><td>Experiment^{37}</td><td></td><td>0</td><td></td><td></td><td></td><td></td><td>6-13</td><td></td></tr><tr><td>HfO_{3}</td><td>This work</td><td>Pnnm</td><td>0</td><td>171.1</td><td>73.6</td><td>193.0</td><td>0.43</td><td>0.31</td><td>6.2</td></tr></table>

We calculated the elastic anisotropy of five special phases:  \( P\bar{6}2m-HfO \) ,  \( Pnnm-Hf_{2}O \) ,  \( Imm2-Hf_{5}O_{2} \) ,  \( P\bar{3}1m-Hf_{2}O \)  and  \( P\bar{4}m2-Hf_{2}O_{3} \) . As shown in Fig. 11, all of these five phases exhibit a moderate amount of anisotropy of Young's modulus. The directional dependence of the Young's modulus for hexagonal, orthorhombic, trigonal and tetragonal crystals can be calculated as:

 \[ \frac{1}{E_{hex}}=s_{11}(1-l_{3}^{2})^{2}+s_{33}l_{3}^{4}+(2s_{13}+s_{44})l_{3}^{2}(1-l_{3}^{2}) \quad (3) \] 

 \[ \frac{1}{E_{ortho}}=s_{11}(l_{1})^{4}+s_{22}(l_{2})^{4}+s_{33}(l_{3})^{4}+l_{2}^{2}l_{3}^{2}(2s_{23}+s_{44})+l_{1}^{2}l_{3}^{2}(2s_{13}+s_{55})+l_{2}^{2}l_{1}^{2}(2s_{12}+s_{66}) \quad (4) \]
 
![](./images/867760589416431851_20.jpg)

FIG. 10. (Color online) Compositional dependence of the computed mechanical properties of Hf-O compounds. The blue open circle represents  \( Pnnm-Hf_{2}O \) ; red open triangle represents  \( OI-HfO_{2} \) ; green open square represents  \( OII-HfO_{2} \) .

 \[ \frac{1}{E_{t r i}}=(1-l_{3}^{2})s_{11}+l_{3}^{4}s_{33}+l_{3}^{2}(1-l_{3}^{2})(2s_{13}+s_{44})+2l_{2}l_{3}(3l_{1}^{2}-l_{2}^{2})s_{14}, \quad (5) \] 

 \[ \frac{1}{E_{t e t r a}}=s_{11}(l_{1}^{4}+l_{2}^{4})+s_{33}l_{3}^{4}+(2s_{12}+s_{66})l_{1}^{2}l_{2}^{2}+(2s_{13}+s_{44})l_{3}^{2}(1-l_{3}^{2}) \quad (6) \] 

where  \( s_{11} \) ,  \( s_{12} \) , etc., are the elastic compliance constants and  \( l_{1} \) ,  \( l_{2} \) ,  \( s_{3} \)  are the direction cosines of a particular crystallographic orientation to coordinate axes  \( x_{1} \) ,  \( x_{2} \)  and  \( x_{3} \) , respectively.
 
![](./images/867760589416431851_21.jpg)

![](./images/867760589416431851_22.jpg)

![](./images/867760589416431851_23.jpg)

![](./images/867760589416431851_24.jpg)

![](./images/867760589416431851_25.jpg)

FIG. 11. (Color online) Orientational dependence of Young's moduli (in GPa) of (a)  \( P\bar{6}2m-HfO \)  (b)  \( Pnnm-Hf_{2}O \)  (c)  \( Imm2-Hf_{5}O_{2} \)  (d)  \( P\bar{3}1m-Hf_{2}O \)  and (e)  \( P\bar{4}m2-Hf_{2}O_{3} \) .

## D. Electronic structure of Hf-O compounds

Fig. 13 shows band structures of Hf-O compounds at 0 GPa (including phases stable at both zero and high pressure). Total and partial densities of states (DOS) are presented in Fig. 14.  \( R\bar{3} \) -Hf \( _{6} \) O,  \( R\bar{3} \) c-Hf \( _{3} \) O, Imm2- Hf \( _{5} \) O \( _{2} \) ,  \( R\bar{3} \) -Hf \( _{12} \) O \( _{5} \) ,  \( P\bar{3} \) 1m-Hf \( _{2} \) O, Pnnm- Hf \( _{2}O \)  and C2/m-Hf \( _{3} \) O \( _{2} \)  are predicted to be metallic with a sizable density of states at the Fermi level. The DOSs of  \( R\bar{3} \) -Hf \( _{6} \) O,  \( R\bar{3} \) c-Hf \( _{3} \) O, Imm2- Hf \( _{5} \) O \( _{2} \) ,  \( R\bar{3} \) -Hf \( _{12} \) O \( _{5} \) ,  \( P\bar{3} \) 1m-Hf \( _{2} \) O, Pnnm- Hf \( _{2}O \)  and C2/m-Hf \( _{3} \) O \( _{2} \)  below E \( _{F} \)  are mainly due to Hf-d and O-p orbitals, and the interactions between the Hf-d orbitals are responsible for metallicity.

![](./images/867760589416431851_26.jpg)

FIG. 12. (Color online) ELF isosurface (ELF = 0.62) for  \( HfO_{3} \) . Blue and red atoms represent oxide  \( O^{2-} \)  and peroxide  \( [O-O]^{2-} \) , ions, respectively.
 
![](./images/867760589416431851_27.jpg)

FIG. 13. (Color online) Band structures of hafnium oxides at 0 GPa. The Fermi energy is set to zero.

Unlike regular metals, semimetals possess both electronic and hole conduction, which can be seen in the band structure as overlap of the partially vacant valence band top and occupied conduction band bottom located at different points in the Brillouin Zone \( ^{14} \) . Moreover, the upper limit of electron and hole density for a semimetal should be below  \( 10^{22} \)  cm \( ^{-3} \) . The carrier concentrations of the most common semimetals, for example Bi, Sb and As are  \( 3 \times 10^{17} \)  cm \( ^{-3} \) ,  \( 5 \times 10^{19} \)  cm \( ^{-3} \) , and  \( 2 \times 10^{20} \)  cm \( ^{-338,39} \) , respectively. Semimetallic behavior of  \( P\bar{6}2m \) -HfO and  \( P\bar{4}m2 \) -Hf \( _{2} \) O \( _{3} \)  can be reflected in the calculated band structures, as shown in Fig. 12(h,i) and in the DOS diagrams (Fig. 14(h,i)), showing very few states at the Fermi level. For the band structure of  \( P\bar{6}2m \) -HfO, there are small electron and hole pockets at  \( \Gamma \)  and M, respectively, but there are no band crossings between the lowest unoccupied bands and the highest occupied bands. Both band edges are mostly derived from Hf 5d states. In the case of  \( P\bar{4}m2 \) -Hf \( _{2} \) O \( _{3} \) , partially occupied valence band top and conduction band bottom correspond to different high symmetry points R and Z, respectively. The electron and hole densities can be estimated by integrating the occupation numbers in the 3D Brillouin zone. The electron
 
![](./images/867760589416431851_28.jpg)

FIG. 14. (Color online) The normalized (per electron) total (TDOS) and partial densities of states (PDOS) of hafnium oxides at 0 GPa. The Fermi energy is set to zero.

and hole densities of HfO are both  \( 1.1 \times 10^{20} \)  cm \( ^{-3} \)  by integrating their occupation of the blue and green bands shown in Fig. 13(h), respectively. For  \( P\overline{4}m2-Hf_{2}O_{3} \) , the electron and hole densities are both  \( 2.1 \times 10^{21} \)  cm \( ^{-3} \) , which is very close to  \( 1.8 \times 10^{21} \)  cm \( ^{-3} \)  obtained in Xue's work \( ^{14} \) .

The DFT band gaps of  \( P2_{1}/c-HfO_{2} \) ,  \( Pbca-HfO_{2}, Pnma-HfO_{2} \)  and  \( Pnnm-HfO_{3} \)  are 4.01 eV, 4.18 eV, 3.36 eV and 1.92 eV, respectively, and the highest occupied states are all derived mainly from O-p orbitals, as shown in Fig. 14(j, k, l and m). Therefore, according to their electronic character, Hf-O compounds can be divided into three types: metallic, including  \( R\overline{3}-Hf_{6}O \) ,  \( R\overline{2}c-Hf_{3}O \) ,  $ Imm2-Hf_{5}O_{2}, R\overline{3}-Hf_{12}O_{5}, P\overline{3}1m-Hf_{2}O, Pnnm-Hf_{2}

ization function (ELF) clearly reveals special feature of  \( HfO_{3} \) , the coexistence of oxide  \( O^{2-} \)
 

and peroxide  \( [O-O]^{2-} \)  anions (Fig. 12). The peroxide is responsible for gap states, which significantly reduce the electronic band gap of  \( HfO_{2} \)  (Fig. 14 (m)). To obtain further insight, we applied the Atoms in Molecules (AIM) theory developed by Bader \( ^{40} \) . Bader charges are +2.5 for Hf, -0.68 for peroxide anion and -1.16 for oxide anion in  \( HfO_{3} \)  at 110 GPa, which shows a significantly ionic character of bonding.

## IV. CONCLUSIONS

We have systematically predicted stable compounds and crystal structures in the Hf-O system at pressures up to 120 GPa using ab initio evolutionary algorithm USPEX. Several new stable compounds, including  \( Imm2-Hf_{5}O_{2} \) ,  \( C^{2}/m-Hf_{3}O_{2} \) ,  \( P\bar{6}2m-HfO \)  and  \( Pnnm-HfO_{3} \)  are found for the first time.  \( Pnnm-Hf_{2}O \) , which is the new high-pressure phase of  \( Hf_{2}O \) , is also discovered.  \( HfO_{3} \)  shows interesting structure, simultaneously containing oxide  \( O^{2-} \)  and peroxide  \( [O-O]^{2-} \) . Semimetallic properties of  \( P\bar{6}2m-HfO \)  and  \( P\bar{4}m2-Hf_{2}O_{3} \)  are demonstrated through their band structures, as well as low densities of conduction electrons and holes. Our results demonstrate that  \( Hf_{3}O_{2} \)  is more ductile than other Hf-O compounds, and the hardest compound is HfO instead of OII-HfO \( _{2} \) . The superior mechanical properties of  \( P\bar{6}2m-HfO \) , such as bulk modulus B, shear modulus G, Young's modulus E and hardness  \( H_{v} \) , can be attributed to the peculiar combination of strong Hf-O and Hf-Hf bonds.  \( Pnnm-Hf_{2}O \) ,  \( Imm2-Hf_{5}O_{2} \) ,  \( P\bar{3}1m-Hf_{2}O \)  and  \( P\bar{4}m2-Hf_{2}O_{3} \)  also show excellent mechanical properties. Clearly, high O content is not a key factor affecting the mechanical properties of Hf-O compounds. Suboxides:  \( Hf_{6}O \) ,  \( Hf_{3}O \) ,  $ Hf_{1}O_{5} and  \( P\bar{3}1m-Hf_{2}O \)  based on hcp-Hf sublattice provide easy pathways for absorbing or desorbing oxygen. The recognition of the common structural features between  \( P\bar{6}2m-HfO \)  and  \( \omega-Hf \)  gives further insight into the physical properties and suggests that HfO can be made as a hard semimetallic coating on  \( \omega-Hf \)  substrate.  \( Pnnm-Hf_{2}O \) ,  \( Imm2-Hf_{5}O_{2} \) ,  \( P\bar{3}1m-Hf_{2}O \)  and  \( P\bar{4}m2-Hf_{2}O_{3} \)  phases in particular can be quenched to ambient pressure and can be candidates for applications requiring mechanically strong materials.
 

## V. ACKNOWLEDGMENTS

This work was supported by the National Science Foundation (EAR-1114313), DARPA (Grants No. W31P4Q1210008), the Basic Research Foundation of NWPU (No. JCY20130114), the Natural Science Foundation of China (No. 51372203, 51332004), the Foreign Talents Introduction, the Academic Exchange Program of China (No. B08040) and the Government (No. 14.A12.31.0003) of Russian Federation. The computational resources at High Performance Computing Center of NWPU are also gratefully acknowledged.

 \( ^{*} \)  Jin.Zhang.1@stonybrook.edu

 \( ^{\dagger} \)  artem.oganov@stonybrook.edu

 \( ^{1} \)  J. Choi, Y. Mao, and J. Chang, Mater. Sci. Eng., R 72, 97 (2011).

 \( ^{2} \)  K.-L. Lin, T.-H. Hou, J. Shieh, J.-H. Lin, C.-T. Chou, and Y.-J. Lee, J. Appl. Phys. 109, 084104 (2011).

 \( ^{3} \)  Y. Al-Khatatbeh, K. K. Lee, and B. Kiefer, Phys. Rev. B 82, 144106 (2010).

 \( ^{4} \)  Y.-W. Chung and W. D. Sproul, MRS Bull. 28, 164 (2003).

 \( ^{5} \)  J. Lowther, MRS Bull. 28, 189 (2003).

 \( ^{6} \)  H. Xia, G. Parthasarathy, H. Luo, Y. K. Vohra, and A. L. Ruoff, Phys. Rev. B 42, 6736 (1990).

 \( ^{7} \)  R. Ahuja, J. M. Wills, B. Johansson, and O. Eriksson, Phys. Rev. B 48, 16269 (1993).

 \( ^{8} \)  T. Tsuji, J. Nucl. Mater. 247, 63 (1997).

 \( ^{9} \)  T. B. Massalski, H. Okamoto, P. Subramanian, and L. Kacprzak, ASM Int., 1990, 1485 (1990).

 \( ^{10} \)  M. Hirabayashi, S. Yamaguchi, and T. Arai, J. Phys. Soc. Jpn. 35, 473 (1973).

 \( ^{11} \)  M. Hirabayashi, S. Yamaguchi, T. Arai, H. Asano, and S. Hashimoto, J. Phys. Soc. Jpn. 32, 1157 (1972).

 \( ^{12} \)  A. Ruban, V. Baykov, B. Johansson, V. Dmitriev, and M. Blanter, Phys. Rev. B 82, 134110 (2010).

 \( ^{13} \)  B. Paul Burton, A. van de Walle, and H. T. Stokes, J. Phys. Soc. Jpn. 81 (2011).

 \( ^{14} \)  K.-H. Xue, P. Blaise, L. R. Fonseca, and Y. Nishi, Phys. Rev. Lett. 110, 065502 (2013).

 \( ^{15} \)  S. Desgreniers and K. Lagarec, Phys. Rev. B 59, 8467 (1999).
 

 \( ^{16} \)  J. Tang, M. Kai, Y. Kobayashi, S. Endo, O. Shimomura, T. Kikegawa, and T. Ashida, Prop. Earth Planet. Sci. Mater. High Press. Temp., 401 (1998).

 \( ^{17} \)  J. Kang, E.-C. Lee, and K. Chang, Phys. Rev. B 68, 054106 (2003).

 \( ^{18} \)  D. M. Adams, S. Leonard, D. R. Russell, and R. J. Cernik, J. Phys. Chem. Solids 52, 1181 (1991).

 \( ^{19} \)  O. Ohtaka, H. Fukui, T. Kunisada, T. Fujisawa, K. Funakoshi, W. Utsumi, T. Irifune, K. Kuroda, and T. Kikegawa, J. Am. Ceram. Soc. 84, 1369 (2001).

 \( ^{20} \)  X.-Q. Chen, H. Niu, D. Li, and Y. Li, Intermetallics 19, 1275 (2011).

 \( ^{21} \)  A. R. Oganov and C. W. Glass, J. Chem. Phys. 124, 244704 (2006).

 \( ^{22} \)  A. O. Lyakhov, A. R. Oganov, H. T. Stokes, and Q. Zhu, Comput. Phys. Commun. 184, 1172 (2013).

 \( ^{23} \)  A. R. Oganov, A. O. Lyakhov, and M. Valle, Acc. Chem. Res. 44, 227 (2011).

 \( ^{24} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

 \( ^{25} \)  G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

 \( ^{26} \)  P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

 \( ^{27} \)  A. Togo, F. Oba, and I. Tanaka, Phys. Rev. B 78, 134106 (2008).

 \( ^{28} \)  B. P. Burton and A. van de Walle, Calphad 37, 151 (2012).

 \( ^{29} \)  J. Zhang, A. R. Oganov, X. Li, H. Dong, and Q. Zeng, Phys. Chem. Chem. Phys. (2015).

 \( ^{30} \)  F. Birch, J. Geophys. Res. 57, 227 (1952).

 \( ^{31} \)  R. Jeanloz, Phys. Rev. B 38, 805 (1988).

 \( ^{32} \)  F. Birch, J. Geophys. Res. 83, 1257 (1978).

 \( ^{33} \)  A. F. Wells, Structural Inorganic Chemistry (Clarendon, 1986).

 \( ^{34} \)  Y. Liu, A. R. Oganov, S. Wang, Q. Zhu, X. Dong, and G. Kresse, Sci. Rep. 5 (2015).

 \( ^{35} \)  J. Haines, J. M. Léger, S. Hull, J. P. Petitet, A. S. Pereira, C. A. Perottoni, and J. A. Jornada, J. Am. Ceram. Soc. 80, 1910 (1997).

 \( ^{36} \)  M. Okutomi, M. Kasamatsu, K. Tsukamoto, S. Shiratori, and F. Uchiyama, Appl. Phys. Lett. 44, 1132 (1984).

 \( ^{37} \)  J. Haines, J. Leger, M. Schmidt, J. Petitet, A. Pereira, and J. da Jornada, (1997).

 \( ^{38} \)  Y. Liu and R. E. Allen, Physical Review B 52, 1566 (1995).

 \( ^{39} \)  N. Ashcroft and N. Mermin, Holt-Saunders, Philadelphia 16 (1976).
 

 \( ^{40} \)  R. F. W. Bader, Atoms in Molecules: A Quantum Theory (Oxford University Press, Oxford, 1990).
 
