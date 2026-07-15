
# Rare-earth defects in GaN: A systematic investigation of the lanthanide series

Khang Hoang \( ^{*} \) 

Center for Computationally Assisted Science and Technology & Department of Physics, North Dakota State University, Fargo, North Dakota 58108, United States (Dated: March 15, 2022)

Rare-earth (RE) doped GaN is of interest for optoelectronics and spintronics and potentially for quantum applications. A fundamental understanding of the interaction between RE dopants and the semiconductor host is key to realizing the material's full potential. This work reports an investigation of lanthanide (Ln) defects in GaN using hybrid density-functional defect calculations. We find that all the Ln dopants incorporated at the Ga lattice site,  \( Ln_{Ga} \)  (Ln = La–Lu), are stable as trivalent ions, but Eu and Yb can also be stabilized as divalent and Ce, Pr, and Tb as tetravalent. The location of Ln-related defect levels and the Ln 4f states in the energy spectrum of the host material is determined from first principles. We elucidate the interplay between defect formation and electronic structure, including the Ln–N interaction, and the effect of doping on the local lattice environment. Optical properties are investigated by considering possible defect-to-band and band-to-defect transitions involving  \( Ln_{Ga} \)  defects with in-gap energy levels, including broad “charge-transfer” transitions. These defects can also act as carrier traps and mediate energy transfer from the host into the 4f-electron core of the Ln ion which leads to sharp intra-f luminescence.

## I. INTRODUCTION

Rare-earth (RE) doped semiconductors have long been of interest for optoelectronics and spintronics [1]. In the RE impurities, the 4f-electron core is well shielded by the outer  \( 5s^{2} \)  and  \( 5p^{6} \)  electron shells, resulting in very sharp intra-f optical transitions at wavelengths from infrared to ultraviolet. GaN doped with Pr, Eu, Er, or Tm, for example, emits light in a few narrow bands in the visible spectrum [2]. In addition to the 4f-4f transitions, "charge-transfer" and 5d-4f transitions can also occur in RE-doped luminescent materials [3]. GaN has also been identified as a promising host material for defect-based qubits [4, 5], mainly due to its wide band gap and weak spin-orbit coupling. Defects suitable for quantum applications are not limited to native point defects and non-RE impurities but can also be RE impurities which, in addition to the sharp optical transitions, have excellent spin coherence properties. Although there has been intensive research on RE-doped complex oxide insulators for quantum computing and optical quantum memories [6–8], prospects of RE-doped GaN for quantum applications were discussed only recently [9]. Whether a RE dopant is being harnessed for traditional optical applications or novel quantum technologies, having a fundamental understanding of the interaction between the dopant and the host material is key to realizing its potential.

The location of RE-related defect levels in the energy spectrum of the semiconductor host is important information to understand and predict the material's properties. Yet, in RE-doped GaN, direct information from experiments has been limited. McHale et al. [10] reported that the occupied Gd, Er, and Yb 4f states are deep in the valence band in GaN thin films. There were reports of a broad “charge-transfer” excitation or absorption band associated with the Eu defect in Eu-doped GaN [11–16], which can provide the location of the  \( Eu^{3+/2+} \)  level. On the basis of an semi-empirical model, Dorenbos and van der Kolk proposed a scheme with the location of all lanthanide impurity levels in GaN [17]. Although such a scheme has been fairly successful in explaining certain properties of the material, a more rigorous methodology and, more importantly, a deeper understanding of RE-related defect structure and energetics are needed if further advances are to be made in understanding and designing RE-doped functional materials. First-principles calculations based on density functional theory (DFT) can be extremely useful in supporting such progress.

Computational studies of RE-doped semiconductors and insulators have been very challenging, however. This is due to the requirement to properly describe both the host states, including the band gap, and the impurity states, including the highly localized RE 4f states, in the doped materials. Standard DFT calculations within the local-density (LDA) or generalized gradient (GGA) approximation  \( [18, 19] \)  are not suitable for systems with partially filled 4f orbitals. Even the Hubbard-corrected DFT+U method  \( [20] \)  fails to satisfactorily describe their basic defect physics  \( [21] \) , mainly due to the fact that the Hubbard U term is applied on the RE 4f states only and all other orbitals are left uncorrected. Only recently, a hybrid DFT/Hartree-Fock approach  \( [22] \)  has been applied successfully to provide reliable results for Eu- and Er-related defects in GaN  \( [21, 23, 24] \)  (See the cited references for a thorough comparison of the results obtained in calculations using hybrid functional vs. other DFT-based methods. Previously, the hybrid functional approach was also reported to provide a “balanced description” of the electronic properties of bulk materials such as RE oxides  \( [25] \) ). Many other RE defects with potentially interesting and useful properties remain to be explored.

We herein present an investigation of RE defects in wurtzite GaN using hybrid density-functional defect cal-
 

culations where all orbitals in the material are treated on equal footing. Specific calculations are carried out for substitutional lanthanide (Ln) impurities at the Ga lattice site, i.e.,  \( Ln_{Ga} \)  (Ln = La–Lu). The interstitial Ln defects are not considered here because they are expected to have high formation energies and thus unlikely to form. On the basis of our results, we discuss the atomic and electronic structure, energetics, and optical properties of  \( Ln_{Ga} \) . Comparison with experiments and previous computational work will be included where appropriate.

## II. METHODOLOGY

Point defects are modeled using a supercell approach in which a defect is included in a periodically repeated finite volume of the host material. The formation energy of a general defect X in charge state q (with respect to the host lattice) is defined as [26]

 \[ \begin{aligned}E^{f}(X^{q})=\quad E_{\mathrm{tot}}(X^{q})-E_{\mathrm{tot}}(\mathrm{bulk})-\sum_{i}n_{i}\mu_{i}^{*}\\ +q(E_{\mathrm{v}}+\mu_{e})+\Delta^{q},\end{aligned} \quad (1) \] 

where  \( E_{\mathrm{tot}}(X^{q}) \)  and  \( E_{\mathrm{tot}}(\mathrm{bulk}) \)  are the total energies of the defect-containing and bulk supercells.  \( n_{i} \)  is the number of atoms of species i that have been added ( \( n_{i} > 0 \) ) or removed ( \( n_{i}<0 \) ) to form the defect.  \( \mu_{i}^{*} \)  is the atomic chemical potential, representing the energy of the reservoir with which atoms are being exchanged, and referenced to the total energy per atom of i in its elemental phase at 0 K; e.g.,  \( \mu_{\mathrm{Ga}}^{*} = E_{\mathrm{tot}}(\mathrm{Ga}) + \mu_{\mathrm{Ga}} \) , with  \( E_{\mathrm{tot}}(\mathrm{Ga}) \)  being the total energy per atom of metallic Ga, and  \( \mu_{Ga} \leq 0 \)  eV.  \( \mu_{e} \)  is the chemical potential of electrons, i.e., the Fermi level, representing the energy of the electron reservoir, and referenced to the valence-band maximum (VBM) in the bulk ( \( E_{v} \) ).  \( \Delta^{q} \)  is the correction term to align the electrostatic potentials of the bulk and defect-containing supercells and to account for finite-size effects on the total energies of charged defects [27, 28].

The thermodynamic transition level between charge states q and  \( q' \)  of a defect,  \( \epsilon(q/q') \) , is defined as the Fermi-level position at which the formation energy of the defect in charge state q is equal to that in state  \( q' \)  [26], i.e.,

 \[ \epsilon(q/q^{\prime})=\frac{E^{f}(X^{q};\mu_{e}=0)-E^{f}(X^{{q^{\prime}}};\mu_{e}=0)}{q^{\prime}-q}, \quad (2) \] 

where  \( E^{f}(X^{q};\mu_{e}=0) \)  is the formation energy of the defect X in charge state q when the Fermi level is at the VBM ( \( \mu_{e}=0 \) ). This  \( \epsilon(q/q') \)  level [also referred to as the  \( (q/q') \)  level], corresponding to a defect energy level (or, simply, defect level), would be observed in experiments where the defect in the final charge state  \( q' \)  fully relaxes to its equilibrium configuration after the transition.

From the defect formation energy, one can also calculate the optical transition level  \( E_{opt}^{q/q'} \) , which is employed to characterize defect-to-band and band-to-defect optical

TABLE I. Formation enthalpies of rare-earth mononitrides, calculated at 0 K. All the LnN binaries are assumed to be in the  \( Fm\overline{3}m \)  space group. The standard heats of formation are also included. The unit is in eV per formula unit

<table><tr><td></td><td>Magnetic order</td><td>\( \Delta H \)  (calc.)</td><td>\( \DeltaH \)  (expt.) \( ^{a} \)</td></tr><tr><td>LaN</td><td>NM</td><td>-2.98</td><td>-3.13  \( \pm \)  0.56</td></tr><tr><td>CeN</td><td>FM</td><td>-3.98</td><td>-3.39  \( \pm \)  0.74</td></tr><tr><td>PrN</td><td>AF-I</td><td>-3.50</td><td>-3.01  \( \pm \)  0.50</td></tr><tr><td>NdN</td><td>FM</td><td>-3.30</td><td>-3.10  \( \pm \)  0.49</td></tr><tr><td>PmN</td><td>AF-II</td><td>-3.43</td><td>-3.32  \( \pm \)  0.65</td></tr><tr><td>SmN</td><td>AF-I</td><td>-2.79</td><td>-3.35  \( \pm \)  0.16</td></tr><tr><td>EuN</td><td>AF-I</td><td>-1.25</td><td>-2.02  \( \pm \)  0.12</td></tr><tr><td>GdN</td><td>FM</td><td>-3.42</td><td>-3.18  \( \pm \)  0.22</td></tr><tr><td>TbN</td><td>FM</td><td>-3.63</td><td>-3.10  \( \pm \)  0.54</td></tr><tr><td>DyN</td><td>AF-I</td><td>-3.83</td><td>-3.42  \( \pm \)  0.53</td></tr><tr><td>HoN</td><td>AF-II</td><td>-3.96</td><td>-3.53  \( \pm \)  0.20</td></tr><tr><td>ErN</td><td>AF-II</td><td>-4.37</td><td>-3.71  \( \pm \)  0.23</td></tr><tr><td>TmN</td><td>AF-I</td><td>-3.84</td><td>-3.70  \( \pm \)  0.53</td></tr><tr><td>YbN</td><td>AF-II</td><td>-2.48</td><td>-3.74  \( \pm \)  0.14</td></tr><tr><td>LuN</td><td>NM</td><td>-3.86</td><td>-3.02  \( \pm \)  0.54</td></tr></table>

 \( ^{a} \) Ref. 31

transitions. The level is defined similarly to  \( \epsilon(q/q') \)  but with the total energy of the final state  \( q' \)  calculated using the lattice configuration of the initial state q [26].

The total-energy electronic structure calculations are based on DFT with the Heyd-Scuseria-Ernzerhof (HSE) functional [22], the projector augmented wave method [29], and a plane-wave basis set, as implemented in the Vienna Ab Initio Simulation Package (VASP) [30]. We use the standard PAW potentials in the VASP (pot-paw_PBE_54) database which treat the Ln 4f electrons explicitly as valence electrons. Like in our previous work [21, 24], the Hartree-Fock mixing parameter ( \( \alpha \) ) is set to 0.31 and the screening length to the default value of 10 Å to match the host's experimental band gap ( \( \sim \) 3.5 eV). RE defects in the GaN host are simulated using a 96-atom supercell. In such a supercell model for the substitutional Ln impurity ( \( Ln_{Ga} \) ), one Ga atom is substituted with Ln and thus the chemical composition is  \( LnGa_{47}N_{48} \) ; i.e., the doping concentration is  \( \sim \) 2%. In the defect calculations, the lattice parameters are fixed to the calculated bulk values but all the internal coordinates are relaxed. All structural relaxations are performed with HSE and the force threshold is chosen to be 0.02 eV/Å. The plane-wave basis-set cutoff is set to 400 eV and spin polarization is included. Spin-orbit coupling (SOC) is not included; it was previously shown that SOC had negligible effects on the defect transition levels [21]. We employ a  \( 2\times2\times2 \)  Monkhorst-Pack k-point mesh for the integrations over the Brillouin zone, except in the calculations to obtain the electronic density of states where a denser,  \( \Gamma \) -centered  \( 3\times3\times3 \)  k-point mesh is used.

The chemical potentials of Ga and N vary over a range determined by the calculated formation enthalpy of GaN:
 
![](./images/867768638382277377_1.jpg)

![](./images/867768638382277377_2.jpg)

![](./images/867768638382277377_3.jpg)

FIG. 1. Formation energies of  \( LnGa_{3} \)  in GaN, plotted as a function of the Fermi level from the VBM (at 0 eV) to the conduction-band minimum (CBM, at 3.53 eV): (a)  \( Ln = Ho \) , Er, Tm, Yb, and Lu, (b)  \( Ln = La \) , Nd, Pm, Sm, Eu, Gd, and Dy, and (c)  \( Ln = Ce \) , Pr, and Tb. For each defect, only segments of the formation energy lines corresponding to the lowest-energy charge states are shown. The slope of these segments indicates the charge state q: positively (negatively) charged defect configurations have positive (negative) slopes; horizontal segments correspond to neutral defect configurations. The dotted formation energy lines correspond to defect configurations ( \( Ln_{Ga}^{+} \) , not indicated in the figure) that consist of an Ln ion at the Ga site and an electron hole localized at a nearby N site. Large dots connecting two segments with different slopes, if present, mark the defect levels in the host band gap [i.e., the thermodynamic transition level  \( \epsilon(q/q') \) , calculated according to Eq. (2)].

 \( \mu_{Ga} + \mu_{N} = \Delta H(\mathrm{GaN})(-1.23 \, \mathrm{eV} \, \mathrm{at} \, 0 \, \mathrm{K}) \) . The extreme Ga-rich and N-rich conditions correspond to  \( \mu_{Ga} = 0 \, eV \)  and  \( \mu_{N} = 0 \, eV \)  where GaN is assumed to be in equilibrium with metallic Ga and an isolated  \( N_{2} \)  molecule, respectively. With a given  \( \mu_{N} \)  value, the atomic chemical potential of  \( Ln \) ,  \( \mu_{Ln} \) , is obtained by assuming equilibrium with  \( LnN \)  (space group  \( Fm\overline{3}m \) ). Table I lists the formation enthalpy of  \( LnN \)  calculated within the HSE functional (with  \( \alpha = 0.31 \) ); the lowest-energy magnetic structure of  \( LnN \)  is found to be either type-I (AF-I) or type-II (AF-II) antiferromagnetic [32, 33], ferromagnetic (FM), or nonmagnetic (NM). Given the phase equilibrium assumption, the formation energy of  \( LnGa_{3} \)  is the same for the Ga-rich and N-rich conditions.

Finally, it should be noted that the thermodynamic and optical transition levels are independent of the choice of the chemical potentials. Also, effects of possible corrections to the total energies beyond the level of theory employed in the current work are expected to be small due to cancellation between different terms in Eq. (2).

## III. RESULTS AND DISCUSSION

We begin by summarizing the basic properties of the host material. In wurtzite GaN, Ga is tetrahedrally coordinated with N atoms: one along the c-axis and three in the basal (ab) plane. The calculated axial and basal Ga–N bond lengths are 1.958 Å and 1.952 Å, respectively, which are consistent with the experimental values (1.956 Å and 1.949 Å) [34]. There is thus a small  \( C_{3v} \)  distortion at the Ga lattice site. The calculated band gap is 3.53 eV, a direct gap at the  \( \Gamma \)  point. In the following, we discuss the energetics of the RE defects and how the structural, electronic, and optical properties of the host material is modified by the presence of a RE dopant.

## A. Defect energy levels

Figure 1 shows the formation energies of  \( Ln_{Ga} \)  in GaN. We divide the substitutional defects into three groups (A, B, and C) based on characteristics of the defects' energetics near the VBM. As it becomes clearer later, the features near the VBM (which consists predominantly of the N 2p states) strongly reflect the  \( Ln-N \)  interaction.

Group A consists of Ln = Ho, Er, Tm, Yb, and Lu, i.e., the last five elements in the lanthanide series. In this group,  \( LnGa_{x} \) , except Ln = Yb, is structurally, electronically, and energetically stable only as  \( Ln_{Ga}^{0} \)  (i.e., the trivalent  \( Ln^{3+} \)  at the Ga site) and does not have any defect level in the host band gap; see Fig. 1(a).  \( Yb_{Ga} \)  is structurally and electronically stable as  \( Yb_{0}^{0} \)  (i.e., the trivalent  \( Yb^{3+} \)  at the Ga site) and  \( Yb_{Ga}^{-} \)  (i.e., the divalent  \( Yb^{2+} \)  at the Ga site), and the valence change occurs at the  \( (0/-) \)  level at 0.05 eV below the CBM (i.e., 3.48 eV above the VBM); see Fig. 1(a) and Table II.  \( Yb_{Ga}^{0} \)  is thus energetically more favorable than  \( Yb_{Ga}^{-} \)  in almost the entire range of the Fermi-level values from the VBM to the CBM, except in a very small range below the CBM in which  \( Yb_{Ga}^{-} \)  is more favorable. Figure 2(a) clearly shows the lattice geometry of and the charge density associated
 
![](./images/867768638382277377_4.jpg)

![](./images/867768638382277377_5.jpg)

![](./images/867768638382277377_6.jpg)

FIG. 2. Structure of representative  \( Ln_{Ga} \)  configurations: (a)  \( Yb_{Ga}^{-} \) , (b)  \( La_{Ga}^{+} \) , and (c)  \( Ce_{Ga}^{+} \) . The charge density, taken with respect to that of the respective neutral defect configuration but calculated using the lattice environment of the charged one, shows a localized (Yb 4f) electron (in the case of  \( Yb_{Ga}^{-} \) ), (N 2p) hole ( \( La_{Ga}^{+} \) ), or (Ce 4f) hole ( \( Ce_{Ga}^{+} \) ). The isovalue for the charge-density isosurface is set to 0.02 e/ \( \mathring{A}^{3} \) . Large (red/green) spheres are  \( Ln/Ga \)  and small (gray) spheres are N.

TABLE II. Electronically stable Ln ions (and their spin S) in the  \( Ln_{Ga} \)  defect and thermodynamic transition levels of  \( Ln_{Ca} \)  in the host band gap (in eV, with respect to the VBM).

<table><tr><td>Defect</td><td colspan="2">Ln ion</td><td>Spin</td><td>\( \epsilon(+/0) \)</td><td>\( \epsilon(0/-) \)</td></tr><tr><td>LaGa</td><td>La3+</td><td>4f0</td><td>0</td><td>0.47</td><td></td></tr><tr><td rowspan="2">CeGa</td><td>Ce4+</td><td>4f0</td><td>0</td><td></td><td></td></tr><tr><td>Ce3+</td><td>4f1</td><td>1/2</td><td>2.37</td><td></td></tr><tr><td rowspan="2">PrGa</td><td>Pr4+</td><td>4f1</td><td>1/2</td><td></td><td></td></tr><tr><td>Pr3+</td><td>4f2</td><td>1</td><td>1.16</td><td></td></tr><tr><td>NdGa</td><td>Nd3+</td><td>4f3</td><td>3/2</td><td>0.30</td><td></td></tr><tr><td>PmGa</td><td>Pm3+</td><td>4f4</td><td>2</td><td>0.28</td><td></td></tr><tr><td>SmGa</td><td>Sm3+</td><td>4f5</td><td>5/2</td><td>0.16</td><td></td></tr><tr><td rowspan="2">EuGa</td><td>Eu3+</td><td>4f6</td><td>3</td><td>0.21</td><td></td></tr><tr><td>Eu2+</td><td>4f7</td><td>7/2</td><td></td><td>3.10</td></tr><tr><td>GdGa</td><td>Gd3+</td><td>4f7</td><td>7/2</td><td>0.08</td><td></td></tr><tr><td rowspan="2">TbGa</td><td>Tb4+</td><td>4f7</td><td>7/2</td><td></td><td></td></tr><tr><td>Tb3+</td><td>4f8</td><td>3</td><td>0.54</td><td></td></tr><tr><td>DyGa</td><td>Dy3+</td><td>4f9</td><td>5/2</td><td>0.14</td><td></td></tr><tr><td>HoGa</td><td>Ho3+</td><td>4f10</td><td>2</td><td></td><td></td></tr><tr><td>ErGa</td><td>Er3+</td><td>4f11</td><td>3/2</td><td></td><td></td></tr><tr><td>TmGa</td><td>Tm3+</td><td>4f12</td><td>1</td><td></td><td></td></tr><tr><td rowspan="2">YbGa</td><td>Yb3+</td><td>4f13</td><td>1/2</td><td></td><td></td></tr><tr><td>Yb2+</td><td>4f14</td><td>0</td><td></td><td>3.48</td></tr><tr><td>LuGa</td><td>Lu3+</td><td>4f14</td><td>0</td><td></td><td></td></tr></table>

with the localized  \( (4f) \)  electron in  \( Yb_{Ga}^{-} \) , thus confirming the stabilization of  \( Yb^{2+} \) . In general, we determine the valence of a RE ion in a defect configuration by examining the total and local magnetic moments, electron occupation, and local lattice environment. Note that the charge-density behavior of  \( Yb_{Ga}^{-} \)  is similar to that of the “atomic-like dopant” described in Lyons et al. [35].

Group B consists of  \( Ln = La, Nd, Pm, Sm, Eu, Gd, and Dy \) . Each of the  \( Ln_{Ga} \)  defects in this group introduces a defect level,  \( (+/0) \) , just above the VBM; see Fig. 1(b) and the  \( \epsilon(+/0) \)  values explicitly listed in Table II. Above the  \( (+/0) \)  level,  \( Ln_{Ga} \)  is energetically more favorable as  \( Ln_{0_{Ga}}^{0} \)  (i.e.,  \( Ln^{3+} \)  at the Ga site); below the  \( (+/0) \)  level,  \( Ln_{Ga} \)  is more favorable as  \( Ln_{Ca}^{+} \) . It is, however, noted that  \( Ln_{Ca}^{+} \)  here is not a true charge state of  \( Ln_{Ga} \) , but a defect complex consisting of  \( Ln^{0}_{Ga} \)  and an electron hole localized on the N atom (hereafter referred to as  \( h^{*} \) , with spin S = 1/2) that is basally bonded to  \( Ln \) ; thus  \( Ln_{Ca}^{+} = Ln_{0_{Ga}}^{0} + h^{*} \) . Figure 2(b) shows the lattice geometry of  \( La_{Ga}^{+} \)  and the charge density associated with  \( h^{*} \) . The charge density for  \( Nd_{Ga}^{+} \) ,  \( Pm_{Ga}^{+} \)  \( , Sm_{Ga}^{+} \) ,  \( Eu_{Ga}^{+} \)  \( , Gd_{Ga}^{+} \) , and  \( Dy_{Ga}^{+} \)  is similar to that for  \( La_{Ga}^{+} \) . Note that the localized hole state (and hence the  \( Ln_{Ga}^{+} \)  configuration) is stable even in HSE calculations with smaller mixing parameters (e.g.,  \( \alpha = 0.25 \) ). Given the charge-density characteristic, these  \( Ln_{Ga}^{+} \)  defects are thus similar to the “polaronic dopant” discussed in Ref. 35.  \( Eu_{Ga} \)  introduces another defect level,  \( (0/-) \) , at 0.43 eV below the CBM (i.e., 3.10 eV above the VBM), above which  \( Eu_{Ga}^{-} \)  (i.e.,  \( Eu^{2+} \)  at the Ga site) is energetically more favorable than  \( Eu_{Ga}^{0} \) . The charge density for  \( Eu_{Ga}^{-} \)  is similar to that for  \( Yb_{Ga}^{-} \)   \( [Fig. 2(a)] \) ; and, like  \( Yb_{Ga}^{-} \) ,  \( Eu_{Ga}^{-} \)  is similar to the “atomic-like dopant” [35].

Group C consists of  \( Ln = Ce, Pr, and Tb \) . Each of these  \( Ln_{Ga} \)  defects introduces one defect level,  \( (+/0) \) , in the host band gap; see Fig. 1(c) and the  \( \epsilon(+/0) \)  values explicitly listed in Table II. Above the  \( (+/0) \)  level,  \( Ce_{Ga} \) ,  \( Pr_{Ga} \) , and  \( Tb_{Ga} \)  are energetically more favorable as  \( Ce_{Ga}^{0} \) ,  \( Pr_{Ga}^{0} = 0 \) , and  \( Tb_{Ga}^{0} \) , i.e., the trivalent  \( Ln^{3+} \)  ion at the Ga site; below the  \( (+/0) \)  level, they are more favorable as  \( Ce_{Ga}^{+} \) ,  \( Pr_{Ga}^{+} \)  and  \( Tb_{Ga}^{+} \) , i.e., the tetravalent  \( Ln^{4+} \)  ion at the Ga site. The  \( Ln_{Ga}^{+} \)  configuration here is, therefore, a true charge state of  \( Ln_{Ga} \) . The transition from the neutral to positive charge state is thus associated with valence change on the lanthanide ion. Figure 2(c) shows the lattice geometry of and the charge density associated with the localized  \( (4f) \)  hole in  \( Ce_{Ga}^{+} \) . The charge density for  \( Pr_{Ga}^{+} \)  and  \( Tb_{Ga}^{+} \) is similar to that for  \( Ce_{Ga}^{+} \) .
 

charge-density behavior of  \( Ce_{Ga}^{+} \) ,  \( Pr_{Ga}^{+} \)  and  \( Tb_{Ga}^{+} \) is thus similar to that of the “atomic-like dopant” [35].

Among the non-trivalent RE ions in GaN, the tetravalent  \( Ce^{4+} \) ,  \( Pr^{4+} \)  and  \( Tb^{4+} \) are expected to be predominant over their trivalent counterparts in doped GaN samples prepared under or close to p-type conditions, i.e., when the Fermi level is closer to the VBM; see Fig. 1(c).  \( Ce^{4+} \) , in particular, has a very large range of the Fermi-level values, from  \( E_{v} \)  to  \( E_{v}+2.37 \)  eV, in which it is energetically more favorable than  \( Ce^{3+} \) . The divalent  \( Eu^{2+} \)  and  \( Yb^{2+} \) , on the other hand, are expected to be predominant over the trivalent ions in samples prepared under n-type conditions. Note, however, that given the very small  \( Yb^{2+} \) -favorable range that is very close to the CBM, see Fig. 1(a), the divalent  \( Yb^{2+} \)  is expected to be much harder to achieve during synthesis. It may, for example, be photogenerated under irradiation.

The stability of these non-trivalent RE ions was previously suggested by Dorenbos and van der Kolk on the basis of a semi-empirical model [17]. The authors fixed the  \( Eu^{2+} \)  level at 3.1–3.2 eV above the VBM, which happens to coincide with the thermodynamic transition level  \( (0/-) \)  of  \( Eu_{Ga} \)  we report earlier in Fig. 1(b) and Table II. The  \( Ce^{3+} \) ,  \( Pr^{3+} \)  \( , Tb^{3+} \) , and  \( Yb^{2+} \)  levels proposed in Ref. 17 are qualitatively consistent with our results for the  \( (+/0) \)  level of  \( Ce_{Ga} \) ,  \( Pr_{Ga} \) , and  \( Tb_{Ga} \)  and the  \( (0/-) \)  level of  \( Yb_{Ga} \) , respectively; the difference is  \( \sim0.5-0.8 \)  eV. The semi-empirical model, however, offers no information on the  \( (+/0) \)  level associated with the localized hole on the basal N atom we find in the other early and middle lanthanide defects. Through DFT-based calculations, Svane et al. [36] found (in self-interaction corrected, spin-polarized LDA calculations) that the  \( (0/-) \)  level of  \( Ln_{Ga} \)  ( \( Ln = Nd \) , Pm, Sm, Eu, Ho, Er, Tm, and Yb) is above the band gap. Such a finding is in contrast to our results for  \( Ln = Eu \)  and Yb, and not consistent with the fact that the  \( (0/-) \)  level of the other  \( Ln_{Ga} \)  defects in the group is electronically unstable. Sanna et al. [37] (who adopted an LDA+U scheme within a density-functional-based tight-binding method), on the other hand, found the  \( (0/-) \)  level of  \( Ln_{Ga} \)  ( \( Ln = Eu \) , Er, and Tm) to be within the host band gap, which is also in contrast to our results for  \( Ln = Er \)  and Tm; their calculated level for  \( Ln \approx Eu \)  is too far from the CBM and thus not consistent with experimental observations (see Ref. 21 for a more detailed discussion). Note that our current results for  \( Ln = Eu \)  and Er are in agreement with those we reported previously [21, 23]; small discrepancies, if present, can be due to the different versions of the PAW potentials used in the previous and current work.

Experimentally, Eu is known to be mixed-valence in GaN, and significant  \( Eu^{2+} \)  concentrations (e.g.,  \( c(\mathrm{Eu}^{2+})/c(\mathrm{Eu}^{3+}) > 1 \) ) have been achieved in GaN via co-doping with O and Si and tuning the growth conditions [38, 39]. As we discussed in detail in Ref. 21, the O and Si co-doping, in which  \( O_{N} \)  and  \( Si_{Ga} \)  act as shallow donors, (i) shifts the Fermi level toward the CBM (“the global effect”), thus placing it in or close to the Fermi-

![](./images/867768638382277377_7.jpg)

FIG. 3. Axial and basal  \( Ln-N \)  bond lengths (in Å) in the isolated  \( Ln_{Ga}^{+} \) ,  \( Ln_{Ca}^{0} \) , or  \( Ln_{Ga}^{-} \) defect configuration. The valence of the RE ion ( \( 2^{+} \) ,  \( 3^{+} \) , or  \( 4^{+} \) ) is indicated. The dotted lines connecting the symbols are to guide the eyes. The (dark red and blue) dotted lines near the bottom of the figure mark the axial and basal Ga–N bond length values in bulk GaN.

level range in which  \( Eu^{2+} \)  is energetically more favorable than  \( Eu^{3+} \) , and (ii) extends the  \( Eu^{2+} \) -favorable range via defect association (“the local effect”); the relatively low growth temperature also benefits high concentrations of defect complexes between  \( Eu_{Ga} \)  and  \( O_{N} \)  (or  \( Si_{Ga} \) ) [21]. We are not yet aware of any experimental report on the presence of  \( Ce^{4+} \) ,  \( Pr^{4+} \)  \( , Tb^{4+} \) , and  \( Yb^{2+} \)  in GaN.

In the following, we describe in detail the local lattice environment of the RE defects and analyze the electronic structure to understand why only certain defect configurations are electronically and energetically stable.

## B. Local lattice environment

Figure 3 shows the Ln–N bond lengths in defect configurations  \( Ln_{Ga}^{+} \) ,  \( Ln_{Ca}^{0} \) , and  \( Ln_{Ga}^{-} \) . For each charge state, we find that the calculated axial and basal bond lengths decrease monotonically as Ln goes from La to Lu. Compared to the Ga–N bonds in bulk GaN, the Ln–N bonds are longer due to the outward relaxation of Ln's neighboring N atoms. In addition, the difference between the axial and basal Ln–N bonds is larger and there is a small variation among the basal Ln–N bonds. The Ln ion is slightly off-center. In the  \( Ln_{Ga}^{0} \)  configuration, for example, the  \( Ln^{3+} \)  ion moves away from the original Ga site and predominantly toward the basal plane; the off-centering is smallest for Ln = La ( \( \sim0.03\ \AA \) ) and largest for Ln = Tm (0.08 Å). The local distortion at the Ga site where the Ln dopant is incorporated is thus more pronounced and slightly deviates from the  \( C_{3v} \)  symmetry. Such significant local lattice distortion should relax the Laporte selection rules, making intra-f optical transitions possible even for isolated RE centers in the host.

In the  \( Ln_{Ga}^{+} \) configuration of group B defects (i.e., Ln
 
![](./images/867768638382277377_8.jpg)

FIG. 4. Total and Ln 4f-projected densities of states (DOS) of Ln-doped GaN, i.e., the  \( Ln_{Ga}^{0} \)  defect configuration, obtained in HSE calculations. The spin-majority spectrum is on the +y axis, and the spin-minority spectrum is on the -y axis. The number of Ln 4f electrons at the projected DOS peaks is indicated. The zero of energy is set to the highest occupied state.

= La, Nd, Pm, Sm, Eu, Gd, and Dy), not included in Fig. 3, the local lattice distortion is a combination of those of the constituent defects ( \( Ln_{Ga}^{0} \)  and  \( h^{*} \) ). The presence of the localized hole on the N atom elongates the Ln–N bond, making that basal bond even longer than the axial Ln–N bond. The difference between the elongated basal Ln–N bond and the axial Ln–N bond is smallest for  \( Ln = Dy (0.01 \AA) \)  and largest for  \( Ln = Eu (0.07 \AA) \) . Due to the bond elongation, the other two basal Ln–N bonds are slightly shortened. The axial Ln–N bond length in these  \( Ln_{Ga}^{+} \) defects are almost the same as that in  \( Ln_{Ga}^{0} \) .

## C. Electronic structure

Figure 4 shows the electronic density of states (DOS) of Ln-doped GaN, specifically the  \( Ln_{Ga}^{0} \)  defect configuration described earlier. Note that by using the same
 

96-atom supercell model and thus a small ( \( \sim2\% \) ) dopant concentration, we avoid possible spurious Ln-Ln interaction caused by the use of periodic boundary conditions and focus on the electronic structure of Ln-doped GaN at the dilute doping limit. We find that Ln in  \( Ln_{Ga}^{0} \)  donates three outer electrons and becomes  \( Ln^{3+} \) , consistent with our analysis in Sec. III A. The Ln 4f-projected DOS reveals the evolution of the electronic structure across the lanthanide series: Starting with  \( La_{Ga}^{0} \)  ( \( 4f^{0} \) ) where the spin-up and spin-down 4f states are unoccupied and deep in the conduction band, these states move down toward the valence band one by one, first with the spin-up 4f states, as the number of the 4f electrons increases. In  \( Gd_{Ga}^{0} \)  ( \( 4f^{7} \) ), there is a narrow peak with seven spin-up 4f electrons in the valence band and another with seven spin-down 4f electrons in that conduction band. From  \( Tb_{Ga}^{0} \) , the spin-down 4f states start moving toward the valence band until all the 4f states are occupied and deep in the valence band (in the case of  \( Lu_{Ga}^{0} \) ,  \( 4f^{14} \) ).

In addition to confirming the electronic stability of  \( Ln_{Ga}^{0} \)  (i.e., the trivalent  \( Ln^{3+} \) ) for all the elements in the lanthanide series, the calculated electronic structure also reveals if other charge states can be stabilized. We start with  \( Ln_{Ga}^{0} \) ,  \( Ln = Ce \) , Pr, or Tb, which has the occupied 4f states in the host band gap. Upon removing one electron from this neutral configuration, the electron is removed from the highest occupied state (which is an  \( Ln\ 4f \)  state). This results in  \( Ln^{3+} \)  being oxidized to the tetravalent  \( Ln^{4+} \) , thus explaining the stabilization of the  \( Ln_{Ga}^{+} \) defects (i.e.,  \( Ln^{4+} \)  at the Ga site) in group C.  \( Yb_{Ga}^{0} \)  (group A) and  \( Eu_{Ga}^{0} \(  (group B) also have in-gap 4f states, but they are unoccupied. In this case, upon adding an electron to the neutral charge state, the electron is added to the lowest unoccupied state (an  \) Ln\ 4f \(  state). This results in  \) Ln^{3+} \(  being reduced to the divalent  \) Ln^{2+} \( , thus explaining the stabilization of  \) Yb_{Ga}^{-} \(  and  \) Eu_{Ga}^{-} $ .

For all other  \( Ln_{Ga}^{0} \)  defect configurations whose electronic structure does not have Ln 4f states in the host band gap, a true  \( Ln_{Ga}^{+} \)  or  \( Ln_{G\alpha}^{-} \)  charge state cannot be stabilized. This is because upon removing or adding an electron, the electron is removed from the VBM or added to the CBM that consists of delocalized host states. In other words, valence change cannot occur on the RE ion. Note that the nature of the removed electron (i.e., the electron hole) in the group B defects is different. Instead of being delocalized like in the late lanthanide (i.e., group A) defects, the hole is localized on a basal N atom in the case of  \( Ln_{Ga}^{+} \)  with Ln = La, Nd, Pm, Sm, Eu, Gd, or Dy, due to strong Ln–N interaction. An examination of the electronic structure of the neutral charge state of these  \( Ln_{Ga}^{+} \)  defects shows that, indeed, there is stronger mixing between the N 2p states and the Ln states at the VBM (not clearly seen in Fig. 4 due to the limited resolution) compared to that found in the late lanthanide defects. This explains why the configuration  \( Ln_{Ga}^{+} = Ln_{Ga}^{0} + h^{*} \)  can be stabilized in group B, but not in group A.

Overall, defect formation is determined by the electronic structure, as it has also been discussed in other

![](./images/867768638382277377_9.jpg)

FIG. 5. Configuration-coordinate diagram illustrating optical absorption (up arrow) and emission (down arrow) processes involving (a)  \( Pr_{Ga} \)  and (b)  \( Eu_{Ga} \)  in GaN. The dash-dotted line indicates the thermal energy (i.e., ZPL). The values sandwiched between two dotted lines are the relaxation energies (i.e., the Franck-Condon shifts). Axes are not to scale.

classes of materials [40]. Through a careful examination and detailed discussion of the electronic structure of Ln-doped GaN, we explain why certain  \( Ln_{Ga} \)  defect configurations can be stabilized in GaN while others cannot. Further discussion of the electronic structure vis-à-vis defect formation in the case of Ln = Eu and Er can be found in our previous work [21, 24]. It is important to note that the Ln-derived peaks in the DOS (Fig. 4) are not defect energy levels associated with  \( Ln_{Ga} \) . Indeed, those Kohn-Sham levels cannot directly be identified with any defect levels that can be observed in experiments [26]. The defect energy levels of  \( Ln_{Ga} \)  in the host band gap, if present, must be calculated using the total energies of the charge states of  \( Ln_{Ga} \)  as described and reported in Sec. III A.

Experimental data on the location of the RE 4f states in the electronic structure of RE-doped GaN has been scarce. Through resonant photoemission experiments on RE-doped GaN thin films, McHale et al. [10] found that the occupied Gd, Er, and Yb 4f states are deep in the host's valence band, which is consistent with our results for Gd-, Er-, and Yb-doped GaN reported in Fig. 4.

## D. Defect-mediated optical transitions

Like native defects and non-RE impurities that possess defect levels in the host band gap, certain isolated  \( Ln_{Ga} \)  defects in GaN can act as carrier traps in defect-to-band and band-to-defect transitions, including photoionization and radiative capture. Of these optical processes, those involving valence change on the Ln ion have also been referred to as “charge-transfer” (CT) transitions in the literature (as opposed to the 4f-4f and 5d-4f transitions) [3]. Transitions involving the  \( (+/0) \)  level of group B defects, see Fig. 1(b), are not strictly of the CT type as the trapped hole is localized at the N site and not on the Ln ion. As discussed later, the  \( Ln_{Ga} \)  defects can also act as carrier traps for the intra-f luminescence.

Figure 5 shows examples of absorption and emission transitions involving  \( Pr_{Ga} \)  and  \( Eu_{Ga} \) . Under illumina-
 

TABLE III. Optical transitions associated with  \( LnG_{a} \)  defects in GaN. The right (left) arrows are for the absorption (emission) processes; Y(es) and N(o) are used to indicate whether or not the transitions are of the “charge-transfer” (CT) type. The thermal ( \( E_{therm} \) ), absorption ( \( E_{abs} \) ), and emission ( \( E_{em} \) ) energies are all in eV.  \( S_{\{e,g\}} \)  are the estimated Huang-Rhys factors; see the text. Absorption peaks that fall outside the host band gap are also included (and italicized).

<table><tr><td>Optical transition</td><td>CT</td><td>E_{therm}</td><td>E_{abs}</td><td>S_{e}</td><td>E_{em}</td><td>S_{g}</td></tr><tr><td>La_{Ga}^{0} \rightleftharpoons La_{Ga}^{+} + e^{-}</td><td>N</td><td>3.06</td><td>3.54</td><td>16.1</td><td>2.53</td><td>17.7</td></tr><tr><td>Ce_{Ga}^{0} \rightleftharpoons Ce_{Ga}^{+} + e^{-}</td><td>Y</td><td>1.16</td><td>1.70</td><td>18.2</td><td>0.69</td><td>15.6</td></tr><tr><td>Ce_{Ga}^{+} \rightleftharpoons Ce_{Ga}^{0} + h^{+}</td><td>Y</td><td>2.37</td><td>2.84</td><td>15.6</td><td>1.83</td><td>18.2</td></tr><tr><td>Pr_{Ga}^{0} \rightleftharpoons Pr_{Ga}^{+} + e^{-}</td><td>Y</td><td>2.38</td><td>2.95</td><td>19.0</td><td>1.83</td><td>18.2</td></tr><tr><td>Pr_{Ga}^{+} \rightleftharpoons Pr_{Ga}^{0} + h^{+}</td><td>Y</td><td>1.16</td><td>1.70</td><td>18.2</td><td>0.59</td><td>19.0</td></tr><tr><td>Nd_{Ga}^{0} \rightleftharpoons Nd_{Ga}^{+} + e^{-}</td><td>N</td><td>3.23</td><td>3.59</td><td>11.9</td><td>2.70</td><td>17.7</td></tr><tr><td>Pm_{Ga}^{0} \rightleftharpoons Pm_{Ga}^{+} + e^{-}</td><td>N</td><td>3.25</td><td>3.74</td><td>16.3</td><td>2.73</td><td>17.2</td></tr><tr><td>Sm_{Ga}^{0} \rightleftharpoons Sm_{Ga}^{+} + e^{-}</td><td>N</td><td>3.37</td><td>3.74</td><td>12.2</td><td>2.88</td><td>16.1</td></tr><tr><td>Eu_{Ga}^{0} \rightleftharpoons Eu_{Ga}^{+} + e^{-}</td><td>N</td><td>3.32</td><td>3.75</td><td>14.2</td><td>2.83</td><td>16.3</td></tr><tr><td>Eu_{Ga}^{0} \rightleftharpoons Eu_{Ga}^{0} + h^{+}</td><td>Y</td><td>3.10</td><td>3.93</td><td>27.6</td><td>2.67</td><td>14.5</td></tr><tr><td>Gd_{Ga}^{0} \rightleftharpoons Gd_{Ga}^{+} + e^{-}</td><td>N</td><td>3.45</td><td>3.75</td><td>10.0</td><td>2.94</td><td>17.1</td></tr><tr><td>Tb_{Ga}^{0} \rightleftharpoons Tb_{Ga}^{+} + e^{-}</td><td>Y</td><td>2.99</td><td>3.49</td><td>16.7</td><td>2.54</td><td>14.9</td></tr><tr><td>Dy_{Ga}^{0} \rightleftharpoons Dy_{Ga}^{+} + e^{-}</td><td>N</td><td>3.40</td><td>3.75</td><td>12.0</td><td>2.94</td><td>15.3</td></tr><tr><td>Yb_{Ga}^{0} \rightleftharpoons Yb_{Ga}^{+} + h^{+}</td><td>Y</td><td>3.48</td><td>3.87</td><td>13.0</td><td>3.15</td><td>10.8</td></tr></table>

tion, for example, the isolated  \( Pr_{Ga}^{0} \)  can absorb a photon and become ionized to  \( Pr_{Ga}^{+} \)  with the removed electron being excited into the conduction band. The peak absorption energy ( \( E_{abs} \) ) corresponding to the optical transition level  \( E_{opt}^{0/+} \)  (i.e., the formation energy difference between  \( Pr_{Ga}^{0} \)  and  \( Pr_{Ga}^{+} \)  in the lattice configuration of  \( Pr_{Ga}^{0} \) ) is calculated to be 2.95 eV, with a relaxation energy (i.e., the Franck-Condon shift in the excited state,  \( d_{FC}^{e} \) ) of 0.57 eV.  \( Pr_{Ga}^{+} \)  can then capture an electron from the CBM (e.g., previously excited from  \( Pr_{Ga}^{0} \)  to the conduction band) or from a shallow donor level and emit a photon; here, we assume that the recombination is radiative. The peak emission energy ( \( E_{em} \) ) corresponding to the optical transition level  \( E_{opt}^{+0} \)  (i.e., the formation energy difference between  \( Pr_{Ga}^{+} \)  and  \( Pr_{Ga}^{0} \)  in the lattice configuration of  \( Pr_{Ga}^{+} \) ) is 1.83 eV, with a relaxation energy (i.e., the Franck-Condon shift in the ground state,  \( d_{FC}^{e} \) ) of 0.55 eV; see Fig. 5(a). The thermal energy [ \( E_{therm} \) , also referred to as the zero-phonon line (ZPL) energy] of the  \( Pr_{Ga}^{0} \rightleftharpoons Pr_{Ga}^{+} + e^{-} \)  transitions is 2.38 eV, related to the thermodynamic transition level  \( \epsilon(+/0) \)  of  \( Pr_{Ga} \) . The ZPL marks the initial onset of the absorption band. Transitions between the  \( (+/0) \)  level of  \( Pr_{Ga} \)  and an electron hole at the VBM, i.e.,  \( Pr_{Ga}^{+} \rightleftharpoons Pr_{Ga}^{0} + h^{+} \) , are also possible and would lead to a different set of the thermal, absorption, and emission energies as seen in Table III. In the case of  \( Eu_{Ga} \) , the emission process involves  \( Eu_{Ga}^{-} \)  capturing an electron hole either from the VBM or some shallow acceptor level; assuming that the recombination is radiative, the peak emission energy is calculated to be 2.67 eV, with a relaxation energy ( \( d_{FC}^{g} \) ) of 0.43 eV; see Fig. 5(b). The thermal energy of the  \( Eu_{Ga}^{0} \rightleftharpoons Eu_{Ga}^{-} + h^{+} \)  transitions is 3.10 eV, related to the thermodynamic transition level  \( \epsilon(0/-) \)  of  \( Eu_{Ga} \) . Transitions involving the  \( (+/0) \)  level of  \( Eu_{Ga} \)  are also possible; see Table III.

Optical transitions involving the other RE defects with in-gap levels are investigated similarly, and all the results are listed in Table III. The Franck-Condon shifts ( \( d_{FC}^{e} \)  and  \( d_{FC}^{g} \) ) can be obtained from the reported values for the thermal ( \( E_{therm} \) ), absorption ( \( E_{abs} \) ), and emission ( \( E_{em} \) ) energies using the following relations [41]

 \[ E_{\mathrm{a b s}}=E_{\mathrm{t h e r m}}+d_{\mathrm{F C}}^{\mathrm{e}}, \quad (3) \] 

 \[ E_{\mathrm{e m}}=E_{\mathrm{t h e r m}}-d_{\mathrm{F C}}^{\mathrm{g}}. \quad (4) \] 

The Stokes shift, i.e., the difference between the absorption and emission energies, is the sum of the Franck-Condon shifts in the excited and ground states [41]:

 \[ E_{\mathrm{a b s}}-E_{\mathrm{e m}}=d_{\mathrm{F C}}^{\mathrm{e}}+d_{\mathrm{F C}}^{g}. \quad (5) \] 

Note that for optical processes involving exchange of electrons (holes) with the CBM (VBM), the thermal, absorption, and emission energies are measured relative to the CBM (VBM). For all the processes listed in Table III, we find that  \( d_{\mathrm{FC}}^{\mathrm{(e,g)}} = 0.30 - 0.83 \, \mathrm{eV} \) . Given the rather large calculated relaxation energies, the absorption and emission are expected to be broad. For comparison, Dorenbos [42] estimated (semi-empirically) that the relaxation energy is of the order of 0.6 eV for CT transitions in various RE-doped materials. And for transition-metal defects in GaN, Wickramaratne et al. [43] reported  \( d_{\mathrm{FC}}^{\mathrm{(e,g)}} = 0.32 - 0.40 \, \mathrm{eV} \)  for optical processes involving  \( Fe_{Ga} \)  defects.

The Huang-Rhys (HR) factor [44], which characterizes the electron-phonon coupling strength, is given by [41]

 \[ S_{\{e,g\}}=\frac{d_{\mathrm{FC}}^{\{e,g\}}}{\hbar\omega_{\{e,g\}}}, \quad (6) \] 

where  \( \omega_{e} \)  and  \( \omega_{g} \)  are the effective phonon frequencies in the excited and ground state. If we assume  \( \hbar\omega_{e} = \hbar\omega_{g} = 30 \)  meV (a typical phonon frequency in GaN [41]), the HR factors are estimated to be  \( S_{\{e,g\}} = 10.0 - 27.6 \) ; see Table III. With such large HR factors ( \( S_{\{e,g\}} \gg 1 \) ), the defects can be considered as having large electron-phonon coupling. In this case, the peak absorption or emission energy coincides with the optical transition level  \( E_{opt}^{q/q'} \)  [41, 45], thus justifying our earlier peak assignment.

It should be noted that for all the emission processes listed in Table III we assume radiative recombination of the trapped electron (hole) and the free hole (electron). This is illustrated in Fig. 6(a) for the case of electron trapping. For CT-type processes, however, the CT emission (which is the reverse of the CT absorption) may not be observed. This is because the recombination energy can quickly be absorbed by the 4f-electron core of the Ln ion. Figure 6(b) illustrates such a process where the
 
![](./images/867768638382277377_10.jpg)

FIG. 6. Schematic illustration of possible optical processes involving a  \( Ln_{Ga} \)  defect with an in-gap energy level (D) in GaN following a band-to-band excitation of the host. The recombination of the excited electron trapped at D and a free hole can be (a) radiative or (b) nonradiative; see the text. Optical processes involving hole trapping are similar.

trapped electron recombines nonradiatively with a free hole, and the recombination energy is transferred to the 4f-electron core which then excites the Ln ion and leads to intra-f luminescence (not explicitly considered in this work). The competition between the two mechanisms illustrated in Fig. 6 is expected to be dependent on specific defect configurations, including the energy difference between the carrier trap level (D) and the excited 4f states [46]. That should apply to defects not just of CT-type transitions but also of non-CT type, including both isolated Ln defects and Ln-related defect complexes (such as those Eu-related complexes reported in Ref. 21).

Let us take the  \( Eu_{Ga}^{-} + h^{+} \rightarrow Eu_{Ga}^{0} \)  transition as an example. After a nonradiative recombination of the electron (trapped at  \( Eu_{Ga}^{-} \) ) and a free hole ( \( h^{+} \) ), the defect becomes  \( Eu_{Ga}^{0} \)  with an electron being promoted from the ground  \( {}^{7}F_{J} \)  state to the excited  \( {}^{5}D_{J} \)  state of the  \( Eu^{3+} \)  4f manifold. The subsequent relaxation from the excited  \( {}^{5}D_{J} \)  state to the ground state would result in a sharp red luminescence, as opposed to a broad blue luminescence as one would observe with the CT emission illustrated in Fig. 5(b). For further discussion of the role of  \( Eu_{Ga} \)  and Eu-related defect complexes as carrier traps for  \( Eu^{3+} \)  intra-f luminescence in GaN, see Ref. 21.

Experimentally, although defect-to-band and band-to-defect optical transitions in RE-doped GaN likely affect the performance of the material, they have apparently not been well discussed, except probably in the case of  \( Ln=Eu \) . There have been reports of a Eu-related, broad CT excitation band centered at about 3.0–3.2 eV above the VBM in the photoluminescence excitation (PLE) spectra of Eu-doped GaN [11–14] or of a CT absorption peak at 0.37 eV below the CBM [15, 16]. The excitation band appears to largely overlap with the host lattice excitation band [11, 12, 16]. The initial onset of the excitation band is at about 2.9–3.0 eV [11–13, 16], which is in reasonable agreement with the ZPL ( \( E_{therm}=3.10 \)  eV) obtained for the  \( Eu_{Ga}^{0}\rightarrow Eu_{Ga}^{-}+h^{+} \)  transition (see Table III) and consistent with the presence of the defect level (0/−) of  \( Eu_{Ga} \)  discussed in Sec. III A.

There have been no experimental reports of CT emission in Eu-doped GaN. This may suggest that the mechanism illustrated in Fig. 5(b) is predominant. Indeed, the mentioned defect level has been thought to play an important role in the  \( Eu^{3+} \)  intra-f luminescence [12–16]. The isolated  \( Eu_{Ga} \)  defect is unlikely the only luminescent  \( Eu^{3+} \)  center, however, and there may be Eu-related defect complexes in Eu-doped GaN samples that are more efficient for nonresonant excitation of  \( Eu^{3+} \)  [21].

Finally, it should be noted that although CT emission appears to be rare  \( [42, 46] \) , it has been observed in various Yb-doped materials  \( [46–48] \)  and in  \( Sr_{2}CeO_{4} \)   \( [49] \) .

## IV. CONCLUSIONS AND OUTLOOK

We have carried out a systematic study of lanthanide (La–Lu) defects in GaN using hybrid density-functional defect calculations. We find that all the Ln dopants, when incorporated into the host material at the Ga site ( \( Ln_{Ga} \) ), are stable as trivalent ions. In addition to the trivalent state, Eu and Yb are also electronically stable as divalent and Ce, Pr, and Tb as tetravalent. The mixed-valence dopants are characterized by having unoccupied (Eu and Yb) or occupied (Ce, Pr, and Tb) 4f states in the host band gap and possessing defect levels that are associated with valence change on the Ln ion. The early and middle lanthanide (La–Dy) dopants, except those (Ce, Pr, and Tb) that can be stabilized in the tetravalent state, introduce a defect level just above the VBM. This level is not associated with valence change on the Ln ion but with the formation of a localized hole on the N atom basally bonded to Ln. That localized state (and hence the defect level) is absent in the late lanthanide (Ho–Lu) defects due to the weaker Ln–N interaction. The location of the Ln-related defect energy levels and the Ln 4f states in the energy spectrum of the host material thus has been now determined from first principles. We also find that all the Ln defects significantly distort the local lattice environment, thus relaxing the selection rules and allowing for parity-forbidden intra-f transitions.

The optical properties are investigated by considering band-to-defect and defect-to-band optical transitions involving the RE defects. We find that the isolated  \( Ln_{Ga} \)  defects (except  \( Ln = Ho, Er, Tm, and Lu \)  with no localized in-gap levels) can be the source of broad absorption and emission bands. The emission bands, especially those of “charge-transfer” type, however, may not be observed due to a competing mechanism in which the recombination energy is transferred into the 4f-electron core of the Ln ion. The defects thus can also act as carrier traps for intra-f luminescence through nonresonant excitation of the Ln ion. Further computational and experimental studies are needed to characterize these transitions and to better understand their impact on the performance of the material. These may include first-principles calculations of photoionization and carrier capture rates [50, 51] which can provide a more quantitative understanding.
Finally, the results reported in this work can serve
 

as the benchmark for calculations using computationally light–and often with limited predictive power–methods such as DFT+U as well as more compute-intensive, post-DFT approaches. They also form the basis for further studies of RE-related defects in GaN, including direct interaction between the Ln dopant and native defects and/or impurities that may be present in the host material. As seen in the case of Er [23, 24] and Eu [21] dopants in GaN, defect association can significantly modify the electronic behavior of a defect and may thus offer inter-

[1] K. O'Donnell and V. Dierolf, eds., Rare Earth Doped III-Nitrides for Optoelectronic and Spintronic Applications, Topics in Applied Physics, Vol. 124 (Springer, Dordrecht, 2010).

[2] A. Steckl and J. Zavada, Optoelectronic Properties and Applications of Rare-Earth-Doped GaN, MRS Bull. 24, 33 (1999).

[3] G. Blasse and B. C. Grabmaier, Luminescent Materials (Springer-Verlag, Berlin, 1994).

[4] J. R. Weber, W. F. Koehl, J. B. Varley, A. Janotti, B. B. Buckley, C. G. Van de Walle, and D. D. Awschalom, Quantum computing with defects, Proc. Natl. Acad. Sci. 107, 8513 (2010).

[5] L. Gordon, J. R. Weber, J. B. Varley, A. Janotti, D. D. Awschalom, and C. G. Van de Walle, Quantum computing with defects, MRS Bull. 38, 802-807 (2013).

[6] C. Thiel, T. Böttger, and R. Cone, Rare-earth-doped materials for applications in quantum information storage and signal processing, J. Lumin. 131, 353 (2011).

[7] N. Kunkel and P. Goldner, Recent Advances in Rare Earth Doped Inorganic Crystalline Materials for Quantum Information Processing, Z. Anorg. Allg. Chem. 644, 66 (2018).

[8] T. Zhong and P. Goldner, Emerging rare-earth doped material platforms for quantum nanophotonics, Nanophotonics 8, 2003 (2019).

[9] B. Mitchell, H. Austin, D. Timmerman, V. Dierolf, and Y. Fujiwara, Temporally modulated energy shuffling in highly interconnected nanosystems, Nanophotonics 10, 851 (2021).

[10] S. McHale, J. McClory, J. Petrosky, J. Wu, R. Palai, Y. Losovyj, and P. Dowben, Resonant photoemission of rare earth doped GaN thin films, Eur. Phys. J. Appl. Phys. 56, 11301 (2011).

[11] S. Morishima, T. Maruyama, M. Tanaka, and K. Aki-moto, Growth of Eu Doped GaN and Electroluminescence from MIS Structure, phys. status solidi (a) 176, 113 (1999).

[12] M. Tanaka, S. Morishima, H. Bang, J. S. Ahn, T. Sekiguchi, and K. Akimoto, Low-energy charge-transfer state and optical properties of  \( Eu^{3+} \) -doped GaN, phys. status solidi (c) 0, 2639 (2003).

[13] E. E. Nyein, U. Hömmerich, J. Heikenfeld, D. S. Lee, A. J. Steckl, and J. M. Zavada, Spectral and time-resolved photoluminescence studies of Eu-doped GaN, Appl. Phys. Lett. 82, 1655 (2003).

[14] S. Higuchi, A. Ishizumi, J. Sawahata, K. Aki-moto, and Y. Kanemitsu, Luminescence and energy-transfer mechanisms in  \( Eu^{3+} \) -doped GaN epitaxial films,

esting physics useful for electrical and optical control.

## ACKNOWLEDGMENTS

This work made use of resources in the Center for Computationally Assisted Science and Technology (CCAST) at North Dakota State University, which were made possible in part by NSF MRI Award No. 2019077.

Phys. Rev. B 81, 035207 (2010).

[15] Z. Li, H. Bang, G. Piao, J. Sawahata, and K. Akimoto, Growth of Eu-doped GaN by gas source molecular beam epitaxy and its optical properties, J. Cryst. Growth 240, 382 (2002).

[16] J. Sawahata, H. Bang, J. Seo, and K. Akimoto, Optical processes of red emission from Eu doped GaN, Sci. Technol. Adv. Mater. 6, 644 (2005).

[17] P. Dorenbos and E. van der Kolk, Location of lanthanide impurity levels in the III-V semiconductor GaN, Appl. Phys. Lett. 89, 061122 (2006).

[18] D. M. Ceperley and B. J. Alder, Ground State of the Electron Gas by a Stochastic Method, Phys. Rev. Lett. 45, 566 (1980).

[19] J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approximation for exchange and correlation, Phys. Rev. B 46, 6671 (1992).

[20] V. I. Anisimov, J. Zaanen, and O. K. Andersen, Hubbard-corrected density-functional theory, Phys. Rev. B 44, 943 (1991).

[21] K. Hoang, Tuning the valence and concentration of europium and luminescence centers in GaN through co-doping and defect association, Phys. Rev. Materials 5, 034601 (2021).

[22] J. Heyd, G. E. Scuseria, and M. Ernzerhof, Hybrid functionals based on a screened Coulomb potential, J. Chem. Phys. 118, 8207 (2003).

[23] K. Hoang, Hybrid density functional study of optically active  \( Er^{3+} \)  centers in GaN, Phys. Status Solidi RRL 9, 722 (2015).

[24] K. Hoang, First-principles identification of defect levels in Er-doped GaN, Phys. Status Solidi RRL 10, 915 (2016).

[25] J. L. F. Da Silva, M. V. Ganduglia-Pirovano, J. Sauer, V. Bayer, and G. Kresse, Hybrid functionals applied to rare-earth oxides: The example of ceria, Phys. Rev. B 75, 045121 (2007).

[26] C. Freysoldt, B. Grabowski, T. Hickel, J. Neugebauer, G. Kresse, A. Janotti, and C. G. Van de Walle, First-principles calculations for point defects in solids, Rev. Mod. Phys. 86, 253 (2014).

[27] C. Freysoldt, J. Neugebauer, and C. G. Van de Walle, Fully Ab Initio Finite-Size Corrections for Charged-Defect Supercell Calculations, Phys. Rev. Lett. 102, 016402 (2009).

[28] C. Freysoldt, J. Neugebauer, and C. G. Van de Walle, Electrostatic interactions between charged defects in supercells, phys. status solidi (b) 248, 1067 (2011).
 

[29] G. Kresse and D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59, 1758 (1999).

[30] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).

[31] J. Kordis and K. A. Gingerich, Heats of vaporization and standard heats of formation of rare earth mononitrides, J. Nucl. Mater. 66, 197 (1977).

[32] M. K. Phani, J. L. Lebowitz, and M. H. Kalos, Monte Carlo studies of an fcc Ising antiferromagnet with nearest- and next-nearest-neighbor interactions, Phys. Rev. B 21, 4027 (1980).

[33] K. Hoang, S. D. Mahanti, J. R. Salvador, and M. G. Kanatzidis, Atomic Ordering and Gap Formation in Ag-Sb-Based Ternary Chalcogenides, Phys. Rev. Lett. 99, 156403 (2007).

[34] H. Schulz and K. H. Thiemann, Crystal structure refinement of AlN and GaN, Solid State Commun. 23, 815 (1977).

[35] J. L. Lyons, D. Wickramaratne, and C. G. Van de Walle, A first-principles understanding of point defects and impurities in GaN, J. Appl. Phys. 129, 111101 (2021).

[36] A. Svane, N. E. Christensen, L. Petit, Z. Szotek, and W. M. Temmerman, Electronic structure of rare-earth impurities in GaAs and GaN, Phys. Rev. B 74, 165204 (2006).

[37] S. Sanna, W. G. Schmidt, T. Frauenheim, and U. Gerstmann, Rare-earth defect pairs in GaN:  \( LDA+U \)  calculations, Phys. Rev. B 80, 104120 (2009).

[38] B. Mitchell, A. Koizumi, T. Nunokawa, R. Wakamatsu, D. Lee, Y. Saitoh, D. Timmerman, Y. Kuboshima, T. Mogi, S. Higashi, K. Kikukawa, H. Ofuchi, T. Honma, and Y. Fujiwara, Synthesis and characterization of a liquid Eu precursor  \( \left(\mathrm{EuCp}_{2}^{\mathrm{m}}\right) \)  allowing for valence control of Eu ions doped into GaN by organometallic vapor phase epitaxy, Mater. Chem. Phys. 193, 140 (2017).

[39] T. Nunokawa, Y. Fujiwara, Y. Miyata, N. Fujimura, T. Sakurai, H. Ohta, A. Masago, H. Shinya, T. Fukushima, K. Sato, and H. Katayama-Yoshida, Valence states and the magnetism of Eu ions in Eu-doped GaN, J. Appl. Phys. 127, 083901 (2020).

[40] K. Hoang and M. D. Johannes, Defect physics in complex energy materials,

J. Phys.: Condens. Matter 30, 293001 (2018).

[41] A. Alkauskas, M. D. McCluskey, and C. G. Van de Walle, Defects in semiconductors—Combining experiment and theory, J. Appl. Phys. 119, 181101 (2016).

[42] P. Dorenbos, Charge transfer bands in optical materials and related defect level location, Opt. Mater. 69, 8 (2017).

[43] D. Wickramaratne, J.-X. Shen, C. E. Dreyer, A. Alkauskas, and C. G. Van de Walle, Electrical and optical properties of iron in GaN, AlN, and InN, Phys. Rev. B 99, 205202 (2019).

[44] K. Huang and A. Rhys, Theory of light absorption and non-radiative transitions in F-centres, Proc. R. Soc. Lond. A 204, 406 (1950).

[45] A. Alkauskas, J. L. Lyons, D. Steiauf, and C. G. Van de Walle, First-Principles Calculations of Luminescence Spectrum Line Shapes for Defects in Semiconductors: The Example of GaN and ZnO, Phys. Rev. Lett. 109, 267401 (2012).

[46] L. van Pieterson, M. Heeroma, E. de Heer, and A. Meijerink, Charge transfer luminescence of  \( Yb^{3+} \) , J. Lumin. 91, 177 (2000).

[47] E. Nakazawa, Charge-transfer type luminescence of  \( Yb^{3+} \)  ions in  \( LuPO_{4} \)  and  \( YPO_{4} \) , Chem. Phys. Lett. 56, 161 (1978).

[48] E. Nakazawa, Charge transfer type luminescence of  \( Yb^{3+} \)  ions in  \( RPO_{4} \)  and  \( R_{2}O_{2}S \)  (R=Y, La, and Lu), J. Lumin. 18-19, 272 (1979).

[49] E. Danielson, M. Devenney, D. M. Giaquinta, J. H. Golden, R. C. Haushalter, E. W. McFarland, D. M. Poo-jary, C. M. Reaves, W. H. Weinberg, and X. D. Wu, A Rare-Earth Phosphor Containing One-Dimensional Chains Identified Through Combinatorial Methods, Science 279, 837 (1998).

[50] L. Razinkovas, M. Maciaszek, F. Reinhard, M. W. Doherty, and A. Alkauskas, Photoionization of negatively charged NV centers in diamond: Theory and ab initio calculations, Phys. Rev. B 104, 235301 (2021).

[51] C. E. Dreyer, A. Alkauskas, J. L. Lyons, and C. G. Van de Walle, Radiative capture rates at deep defects from electronic structure calculations, Phys. Rev. B 102, 085305 (2020).
 
