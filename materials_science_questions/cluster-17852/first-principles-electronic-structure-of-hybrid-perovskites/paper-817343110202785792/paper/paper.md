ACCEPTED MANUSCRIPT

# Computational study of iron perovskite CH₃NH₃FeI₃ as an alternative to the lead perovskite CH3NH3PbI3 for application in solar cells

To cite this article before publication: Hassan Sabzyan *et al* 2020 *J. Phys.: Condens. Matter* in press https://doi.org/10.1088/1361-648X/ab9b4f

---

Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2020 IOP Publishing Ltd.

---

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere.

As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the [article online](article online) for updates and enhancements.

This content was downloaded from IP address 129.180.1.217 on 14/06/2020 at 18:31

# Computational study of iron perovskite $CH_3NH_3FeI_3$ as an alternative to the lead perovskite $CH_3NH_3PbI_3$ for application in solar cells

Hassan Sabzyan*, Forouzan Ghaderi

Department of Chemistry, University of Isfahan, Isfahan 81746-73441, I. R. Iran.

## ABSTRACT

Structural and optical properties of methylammonium iron iodide perovskite $CH_3NH_3FeI_3$ are studied at DFT-PBE(mBJ)/FP-LAPW+lo level of theory to assess feasibility of the replacement of the toxic lead with the non-toxic iron in the perovskite layer of solar cells. Starting from experimental crystal structure of the Pb perovskite, volume and aspect ratio (c/a) and atomic positions are optimized for the $CH_3NH_3FeI_3$ structure, and its electronic and optical characteristics are calculated. An index, measuring the raw optical performance of the light harvesting layer of a solar cell is introduced and calculated for the two Fe and Pb perovskites. Comparative values of this index shows that the iron perovskite $CH_3NH_3FeI_3$ has an acceptable optical performance, ~61% that of the Pb perovskite $CH_3NH_3PbI_3$. Analysis of the Brewster angles ($\theta_B$) calculated for the $TiO_2$/perovskite and perovskite/spiro interfaces shows that the Fe perovskite solar cell can have better optical harvesting performance by a factor of 1.32, which improves its comparative overall performance up to 80%. As a conclusion, application of iron perovskite $CH_3NH_3FeI_3$ is promising, especially due to its much lower costs and significantly alleviated environmental hazards of the incorporating solar cells.

**Keywords**: $CH_3NH_3FeI_3$; $CH_3NH_3PbI_3$; optical properties; absorption coefficient; perovskite solar cell (PSC); DFT-PBE; dielectric function.

* Corresponding author: H. Sabzyan (sabzyan@sci.ui.ac.ir).

### I. INTRODUCTION

Photovoltaic or solar cells (SC) are considered as the best and most reliable source of electrical energy with the least environmental side effects. Efficiency of solar cells has been extensively improved in the past decade and their applications have been extended to many aspects of our daily life. The cost of electricity produced by SCs should be low enough to be competitive over that produced worldwide by the oil, natural gas or nuclear sources. $^{1-3}$ Silicon or wafer based SCs are known as the first generation or traditional SCs. Power conversion efficiency (PCE) of monocrystalline silicon type of SCs have has reached nearly to 24.4%, $^{4}$ but mass production of silicon single crystals in large scales is very expensive, and thus this type of SC is not competitive. The next generations of solar cells, like organic photovoltaics, quantum dot and dye sensitized solar cells (DSSC), made it possible to produce efficient and less expensive devices. $^{1}$ Specifically, production of new SCs based on organohalide lead perovskites has also improved photovoltaic technology by achieving production of easily processable SCs with appropriate efficiencies. $^{3,5}$

Kojima et al. reported the first application of perovskites in the form of methylammonium lead halide with the general formula of $CH_3NH_3PbX_3$ (or simply $MAPbX_3$), with X= Cl, Br and I, as light harvester in conjunction with a mesoporous film of $TiO_2$ as an $n$-type semiconductor in liquid based DSSC. $^{6}$ This type of SC which is known also as perovskite solar cell (PSC) showed an initial PCE of 3.8%. The PCE of the PSCs is increased to 6.5% by modification of the $TiO_2$ surface. $^{7}$ Next, the chlorine perovskite (X=Cl) is used in conjunction with $Al_2O_3$ as a hole transport material (HTM) to attain a 10.9% PCE. $^{8}$ A 15.6% PCE is then achieved by applying graphene as electron transport medium (ETM) in PSCs. $^{9}$ Some other modifications such as applications of mixed (I, Br and Cl) halides and replaced or mixed metals, and change of the organic molecule (e.g. to formamide, FA) improved the PCE of PSCs, to ~14% for $FASn_{0.5}Pb_{0.5}I_3$$^{10}$ and ~17% for $MAPb_{0.85}In_{0.15}I_{3-x}Cl_x$, $^{11}$ as examples. A 20.1% PCE was then

obtained by applying polytriarylamine as a hole transport material in the design of PSC.¹² Then,
the efficiency of PSCs was improved to 22.1% by applying $CH_3NH_3PbI_{3-x}Cl_x$ as light
absorbing layer.¹³ Finally, a record of 26.7% is reported recently for PSCs made by combining
PSCs with conventional silicon solar cells in a tandem cell structure.¹⁴

The improvement trend in the PCE achieved in these works indicates that PSCs can still be
improved towards more economically competitive source of power by modification of the
incorporated perovskite.

The general chemical structure of perovskites can be represented as $OMX_3$, in which O is an
organic cation or a monovalent alkali metal ($Li^+$, $Na^+$, $K^+$, $Rb^+$, $Cs^+$), M is a divalent metal
cation ($Be^{2+}$, $Mg^{2+}$, $Ca^{2+}$, $Sr^{2+}$, $Ba^{2+}$, $Zn^{2+}$, $Ge^{2+}$, $Sn^{2+}$, $Pb^{2+}$, $Fe^{2+}$, $Co^{2+}$, $Ni^{2+}$) and X is a halide.¹⁵

The $OMX_3$ perovskite crystal structures consists of octahedral $MX_6$ units. Connection of $MX_6$
octahedral units along the three Cartesian directions form a three-dimensional network. The
most common form of PSCs is based on the methyl ammonium lead halides $CH_3NH_3PbCl_{3-x}I_x$,
in which x varies from 0 to 3.¹⁶ In these perovskites, the metal halide $MX_6$ unit has a $PbCl_{6-2x}I_{2x}$
stoichiometry. In the $CH_3NH_3PbI_3$ perovskite (i.e. $x=3$), the holes between the connected $MI_6$
octahedral units are occupied by the organic cations $CH_3NH_3^+$.¹⁷,¹⁸ The unit cell of the
tetragonal crystal structure of the $CH_3NH_3PbI_3$ perovskite is demonstrated in Fig. 1.¹⁹

The position, orientation and anisotropic interactions of the $CH_3NH_3^+$ cations with the $MX_6$
units induces a distortion in the coordination geometries of the $MX_6$ units and the extended
lattice structure. This distortion, which is the main cause of temperature-dependent tetragonal-
orthorhombic cubic phase transitions in the $MI_6$ network,¹⁷ results in wide valence and
conduction bands for the $MAPbI_3$ lattice, and consequently leads to broad and intense
absorption spectra of this perovskite and their excellent performance as light harvesters.

![](./images/817343110202785792_1.jpg)

Fig. 1: The crystal unit cell structure of the $CH_3NH_3PbI_3$ (i.e. M = Pb) perovskite derived from the data (a = b = 16.804 & c = 23.871 bohr) reported by Dang et al. $^{19}$ used as the initial structure of the $CH_3NH_3FeI_3$ (i.e. M = Fe) perovskite by Pb/Fe replacement. The lables on iodine atoms are used for structural characterization (Table S-1).

An important disadvantage of the perovskite based SCs (PSCs) is the presence of lead as a toxic metal in the heart of their photo-active part. $^{20}$ In spite of the growing trend of commercial use of perovskite photovoltaic devices, according to the 2011 European Union (EU) attachment on restriction of the use of hazardous substances in the manufacture of electronic and electrical equipments, the use of this type of SCs is limited in EU member countries. $^{21}$ In the presence of polar solvents such as water, the perovskite structure can be degraded to $PbI_2$ which is known as a carcinogen compound. $^{22}$

Generation of $1 \times 10^{12}$ W electric power per year by PSCs, requires $\sim 1 \times 10^7$ kg of lead. $^{23}$, and in the long term usage of lead perovskite SCs, lead will enter into the human life cycle via agricultural and animal products or even directly. Therefore, application of lead perovskite in the structure of SCs can become a serious environmental threat. $^{24}$ Since lead contamination, as an undesired result of the development of PSCs power generation fields, is an important

environmental and health issue, the next step of the improvement of this type of SCs should be the replacement of lead with less toxic metals. $^{25-27}$

Substitution of an appropriate metal in the structure of PSCs should be based on the criteria that optoelectronic properties, chemical and thermodynamic stabilities and structural features of the perovskite, as an absorbing layer in the photovoltaic cell, are preserved or even improved.
In this line, application of tin in the form of $Sn^{2+}$ is examined and reported to be a reliable alternative element to make lead-free PSCs. $^{28,29}$ Although, tin is not considered toxic or environmentally destructive as compared to lead, but in long term, its mass applications in the domestic and large-scale power plants is also harmful to environment and human health. $^{30}$
Furthermore, a number of computational works carried out at different levels of theory have been reported on the study of a variety of lead-free perovskites. $^{31,32}$ Advances in computational simulation and modelling of lead and lead-free pervoskites is reviewed in an article by Yu. $^{33}$
Krishnamoorthy et al. used computational methods based on DFT to replace Ge as a suitable candidate for replacing lead in halide perovskite materials for solar cell applications. $^{34}$

It should be mentioned here that computational methods have so far been used in the prediction and study of different properties of materials related to almost all types of solar cells, in addition to the PSCs. $^{35-37}$

In the present study, possibility of the use of iron in lieu of lead in the perovskite structure is studied using quantum computational methods. Iron is a nontoxic metal and as an abundant element on the earth surface is widely available and inexpensive. In this computational study, density functional method is used to optimize the tetragonal crystal structure for the proposed $CH_{3}NH_{3}FeI_{3}$ (MAFeI₃) iron perovskite, starting from that of the $CH_{3}NH_{3}PbI_{3}$ (MAPbI₃) lead perovskite. The electronic and optical properties of the optimized structure of the proposed iron perovskite are calculated and analysed in order to rank the proposed iron perovskite in comparison to the lead perovskite being used presently in the structure of PSCs.

In search of gapless semiconductors for spintronic applications, Huang et al. studied a cubic structure of the $MAMI_3$ series of perovskites (including M=Fe) computationally at DFT-D2 level of theory using PBE functional. They reported the $MAFeI_3$ perovskite as a stable half-metallic magnetic material with variable bandgaps under cubic structural strains tolerating a maximum $-5\%$ change in its lattice parameter.$^{38}$

Just recently, in the final stage of the preparation of this report, Zhu et al. published a paper$^{39}$ on the band structure and optical absorption of orthorhombic phase of $CH_3NH_3MI_3$ (M = Fe, Mn) in different (ferro- and antiferro-) magnetic states using DFT-GGA(+U) method. Note that, at room temperature, the tetragonal phase of the $CH_3NH_3PbI_3$ perovskite is stable.$^{20}$ As reported by Zhu et al., the band gap of $CH_3NH_3FeI_3$ vary from 0.602 to 1.215 eV depending on the spin or magnetic (ferromagnetic and antiferromagnetic) state of the system. In the discussion section, results of our present research are compared with those reported by Zhu et al.$^{39}$

The quests and attempts for preparation and prediction of the lead-free perovskite solar cells, discussed and addressed in the experimental and computational reports reviewed above, and in an editorial review by Kamat et al.$^{40}$ and a recent review article by Huiying$^{41}$ show the importance and challenges of replacing toxic and extremely hazardous lead perovskites by non-toxic and less-hazardous compounds such as that proposed in this study.

## II. COMPUTATIONAL METHOD

Among different possible crystal structures, the room temperature phase of $MAPbI_3$ having a tetragonal crystal structure proposed by Dang et al.$^{19}$ with the unit cell shown in Fig. 1 is adopted in this computational study. The unit cell parameters of this I4cm crystal structure are reported to be a = b = 16.804, c = 23.871 bohr and bond angles $\alpha = \beta = \gamma = 90^\circ$. The total

number of atoms in this particular unit cell is 12. Volume of the primitive unit cell⁴² of this tetragonal structure is thus 3370.5 bohr³.¹⁹

Starting from the experimental unit cell of the lead perovskite (G₀) described above, the unit cell parameters are optimized using density functional theory (DFT) within generalized gradient approximation (GGA) with PBE functional and full-potential (linearized) augmented plane waves plus local orbitals (FP-LAPW+lo), as implemented in the solid state quantum computational program WIEN2k ⁴². In these computations, a −7.0 Ry energy criterion is set to separate the core and valence electrons for which different wavefunction expansions are considered. The muffin-tin radii for the H, C, N, I and Pb atoms of the Pb based perovskite are considered to be 0.56, 1.22, 1.04 and 2.0 bohr, respectively.

The self-consistent field calculations are carried out with a charge convergence criterion of $10^{-5}$ electrons. The size of the wave vectors (kₓ,kᵧ,k_z) k-point mesh of the irreducible Brillouin zone of the reciprocal lattice is optimized to (9,9,10) by following energy of the lattice towards its asymptotic value, as shown in part (a) of Fig. S-1 of the Supplementary Materials.

The basis set used in these computations should be large enough to result in accurate wave functions and properties within reasonable computer calculation time. For this purpose, the cut-off parameter $R_{MT}K_{Max}$ is optimized to achieve the minimum energy plateau (Fig. S-1(b) of the Supplementary Materials).

Finally, size of the largest vector of the reciprocal space lattice $\overrightarrow{G}$ in the charge Fourier expansion (G_max) is optimized to obtain the total energy convergence. Extrapolation of this optimization (Fig. S-1(c) of the Supplementary Materials) resulted in $G_{max}=26\ Ry^{1/2}$.

After optimization of the computational parameters, volume and aspect ratio (c/a) of the unit cell are sequentially optimized by considering energy convergence criteria of $\Delta E=10^{-6}$ Ry. Birch-Murnaghan equation of state is used to fit the energy-volume curve, and to locate its minimum point which is then used for the next optimization steps. Results of the volume and

c/a optimizations are presented respectively in parts (a) and (b) of Fig. S-2 Supplementary Materials).

Due to the lack of any experimental data for the Fe based perovskite, the initial structure of the proposed $MAFeI_3$ perovskite ($G_0$) is built by replacing the lead atom in the tetragonal structure of the $MAPbI_3$ perovskite (Fig. 1) by the iron atom. The muffin-tin atomic radii of the H, C, N, I and Fe atoms of this iron perovskite structure are set respectively to 0.6, 1.24, 1.1, 2.0 and 2.0 bohr. The unit cell volume and c/a ratio for this proposed $MAFeI_3$ structure are optimized under similar conditions described above to obtain sequentially the volume optimized $G_1$ and then the c/a optimized $G_2$ geometries, respectively with fixed a/b/c ratio and fixed volume. Results of these optimizations are presented in Fig. S-2 and Table S-1 of the Supplementary Materials, along with those obtained for the $MAPbI_3$ perovskite. Analysis of the volume-energy and c/a-energy curves demonstrated in Fig. S-2 shows that the structure of the experimental Pb perovskite tetragonal lattice adopted as an initial guess for the structure of the proposed Fe perovskite is justified and has served as a very good and close estimate. Moreover, the inter-atomic distances in the fully-optimized structure of the Fe perovskite lattice are different from those of its initial structure (i.e. those of the original Pb perovskite) by a maximum of -5.1%, which is quite normal and can be attributed to the differences in the characteristics of the Pb and Fe elements.

Atomic positions of the two perovskites are also optimized to minimize forces on all atoms and to obtain the equilibrium geometry ($G_3$) of the lattice within convergence criterion of smaller than 1 mRy/a.u.

The changes in the lattice energy, and inter-atomic distances in each of the three optimization steps described above for the $MAFeI_3$ and $MAPbI_3$ structures are calculated and reported in Table S-1 of the Supplementary Materials. A review of the data reported in this Table indicates that the DFT- PBE/FP-LAPW+lo computations result in a geometry for the Pb perovskite

which is very close to the experimental structure within a maximum difference of $-0.7\%$ (for c/a). This small difference is quite justified because of imperfect DFT functionals and inaccuracies in the computational parameters and calculations inherent to this DFT method. Therefore, the PBE/FP-LAPW+lo method used in this study is reliable enough for the structural optimization and calculations of the properties of the $MAFeI_3$ perovskite.

The modified Becke-Johnson (mBJ) exchange potential functional, i.e. the mBJ/FP-LAPW+lo method, $^{43-46}$ is used to calculate band structures (BS) and density of states (DOS) of the optimized geometries obtained with the PBE/FP-LAPW+lo method for the two $MAFeI_3$ and $MAPbI_3$ perovskites. To investigate possible magnetic properties of the $MAFeI_3$ perovskite, the same mBJ approximation is carried out with spin-polarized DFT calculations to obtain the BSs and DOSs of its $\alpha$ and $\beta$ spin states. The spin-polarized calculations are carried out for the $MAPbI_3$ perovskite also as reference.

## III. RESULTS AND DISCUSSION

### a. Structural properties

Some details of the optimized geometries of the two $MAPbI_3$ and $MAFeI_3$ perovskites obtained by PBE/FP-LAPW+lo calculations described in the previous section are reported in Table S-1 of the Supplementary Materials. Analysis of these results shows that the Fe perovskite adopt more or less the same tetragonal structure as that of the Pb perovskite within maximum deviations of $-1.0\%$, $-2.5\%$ and $-4.9\%$ in the lattice parameters $a=b$, $c$ and the volume, respectively.

The unequal metal-iodine bond lengths $M-I_a$ and $M-I_b$, and unequal bond angles $I_a$-$M$-$I_b$, $I_b$-$M$-$I_c$ and $M$-$I_b$-$M$ and their deviation from perfect angles of the tetragonal structure, i.e. $90^\circ$, $90^\circ$ and $180^\circ$ angles, obtained for both perovskites clearly denote asymmetry of the $MI_6$ octahedrals (Table S-1 of the Supplementary Materials). This asymmetry is larger for the Fe

perovskite. These structural imperfections, i.e. deviation from the perfect six-coordinated tetragonal structure expected for the $PbI_{6}$ or $FeI_{6}$ units of the corresponding lattices, which exist for both perovskites, arise from the unavoidable asymmetric position of the methylammonium cation in the unit cell imposed by different interactions between of the $CH_{3}$ and $NH_{3}$ moieties of this cation with the atoms of the $MI_{6}$ units of the lattice.

### b. Electronic structure

The non-spin-polarized (non-SP) and spin-polarized (SP) band structures calculated for the Fe perovskite is presented in Fig. 2 where the corresponding data obtained for the reference Pb perovskite are also presented. Since, the $Fe^{2+}$ ion in the crystal field of six $I^{-}$ ion, which is the weakest ligand in the spectrochemical series, $^{47}$ has a more stable non-singlet state and thus has unpaired d-electrons in this distorted $D_{4h}$ tetragonal coordination structure. The total energy for the Fe perovskite calculated by SP method is 2.204 eV lower than that calculated by non-SP method. Band structures along the high symmetry path of the Brillouin zone calculated for the spin-up ($\alpha$) and spin-down ($\beta$) states of the Fe perovskite, presented in Fig. 2(a & b), shows that the $\alpha$ and $\beta$ states have different band structures which are also different from that of the non-SP calculations. This difference results in magnetic properties. $^{48}$ The BSs obtained by SP-mBJ method for the $\alpha$ and $\beta$ states of the $MAFeI_{3}$ perovskite display respectively 2.910 and 0.668 eV band gaps at the $\Gamma$ point of the reciprocal lattice. The band structures obtained with non-SP and SP ($\alpha$/$\beta$ spin states) calculations for the $MAPbI_{3}$ perovskite are identical and denote its non-magnetic nature, and thus only one BS plot is presented for this perovskite in Fig. 2(d).

The calculated band structures, plotted in Fig. 2, indicate that $MAFeI_{3}$ and $MAPbI_{3}$ are both direct bandgap systems at the $\Gamma$ point of the Brillouin zone having bandgap energies $E_{g}=0.668$ eV and 1.553 eV, respectively. In the first Brillouin zone of these perovskite structures, $R\equiv M$ and $A\equiv\Gamma$, and thus presentation of the R and A points on the BS paths is not necessary.

Calculated $E_{g}$ for the Pb perovskite is in agreement with the previous experimental data (1.595

eV)$^{49}$ and the PAW-DFT$^{50}$ and PBE-DFT$^{51}$ computational results (1.630 and 1.510 eV, respectively) reported for this perovskite. It should be noted here that computations on the Pb perovskite with the PBE method are repeated in this work, following Ahmed et al.,$^{51}$ as a benchmark for validation of the PBE computational results obtained for the proposed Fe perovskite of our interest, and also for direct access to numerical values of various quantities needed specifically for more detailed comparative studies intended in this work. The energy levels of the valence band (VB) structure just below the Fermi level obtained for the MAFeI$_3$ perovskite are obviously less crowded and less dispersed as compared to that obtained for the MAPbI$_3$ perovskite. The same trends had already been reported in the comparison of the MASnI$_3$ and MAPbI$_3$ perovskites.$^{52}$ Substitution of Pb by Fe results also in a ~0.9 eV shift in the conduction band (CB) edge to lower energies (Fig. 2(b)), and thus reduces the band gap. This reduction in the bandgap can be due partly to the smaller energy difference between the Fe $3d$ and I $5p$ levels as compared to that between the Pb $6p$ and I $5p$ levels, and the difference between the space geometries of the contributing Fe $3d$ and Pb $6p$ orbitals.

Differences in the unit cell parameters, and in the bonding and interaction characteristics of atoms in the unit cell can also contribute to the difference between the band gaps of the two MAFeI$_3$ and MAPbI$_3$ perovskites. The significantly smaller bandgap calculated for MAFeI$_3$ (0.66 eV), compared to the bandgap calculated for MAPbI$_3$(1.55 eV), is close to that reported for the Sn perovskite (0.61-1.2 eV)$^{53,54}$. Since, the Sn perovskite has already been examined in the structure of PSCs as a light absorber,$^{55,56}$ it can thus be concluded that MAFeI$_3$ can also be introduced as a candidate with smaller energy band gap for the use in these PSCs.

Interestingly, the bandgap for the tetragonal iron perovskite in its spin-down state obtained in the present study is 0.668 eV which is comparable with what reported by Zhu et al.$^{39}$ for the ferromagnetic state of the orthorhombic iron perovskite (i.e. 0.602 eV). These band gap values reflect properly the effect of the crystalline structure on the electronic properties of the iron perovskite.

The bulk chemical, physical and optical behavior of materials depend on the spatial distribution and energy levels of the molecular orbitals (valence and conduction bands) formed from the overlap of atomic orbitals in the crystal structure. The total and partial density of states (DOS & pDOS), derived with a 0.03 eV integration width from the results of the non-SP and SP mBJ calculations on the PBE optimized structures of the two perovskites, are plotted in Fig. 3. The contributions from individual atomic orbitals to the DOS are also calculated and plotted in Fig. S-3 of the Supplementary Materials.

![](./images/817343110202785792_2.jpg)

**Fig. 2:** The mBJ/FP-LAPW+lo band structures (BS) calculated for the PBE/FP-LAPW+lo optimized structures of the $MAFeI_3$ perovskite obtained by SP calculations for spin-up (a) and spin-down (b) states and non-SP calculations (c). The same set of data calculated for the $MAPbI_3$ perovskite (as reference) is presented in part (d). The direct bandgap energies (Eg) at the $\Gamma$ point of the Brillouin zone are also labelled in the plots of both perovskites.

Larger integration widths, usually used in the study of solids, result in broad bands and fades out details useful for comparative study. Therefore, we preferred to use a narrow integration width to reveal more details of the calculated DOS, as can be seen from Figs. 3 and S-3. It can be seen from these Figures that the two perovskites have distinctly different DOSs. Furthermore, the DOSs of the $\alpha$-spin and $\beta$-spin states of the $MAFeI_3$ perovskite are asymmetric and thus denote that this proposed perovskite will have magnetic feature. This is while, for the $MAPbI_3$ perovskite, the SP DOSs obtained for the two spin up ($\alpha$-spin) and spin down ($\beta$-spin) states are exactly identical, denoting that this perovskite is non-magnetic. As shown in Fig. 3, the band gaps $E_g$ obtained for the iron perovskite $MAFeI_3$ without and with spin polarization calculations are 0.315 eV and 2.209 eV ($\alpha$ spin) and 0.668 eV ($\beta$ spin), respectively. For the lead perovskite $MAPbI_3$, the bandgap $E_g$ is found to be 1.553 eV for $\alpha$ and $\beta$ spin SP and the non-SP calculations.

![](./images/817343110202785792_3.jpg)

![](./images/817343110202785792_4.jpg)

Fig. 3: Individual atomic (partial) density of states (pDOS) calculated with a 0.03 eV integration width for MAFeI₃ without (a) and with (b & c) spin polarization (SP) using the mBJ functional for the GGA-PBE optimized structures. The corresponding results obtained for the MAPbI₃ perovskite is presented in part (d) for comparison. The bandgaps are also labelled. For more resolution, the contribution of C and N atoms are multiplied by 50.

Comparison of parts (b) and (d) of Fig. 3 reveals that the edge of the conduction band (CB) for MAFeI₃ is significantly lower than that for MAPbI₃, denoting its determining contribution to the decrease in the bandgap of MAFeI₃ as compared to that of MAPbI₃. For more resolution, in Fig. 3(b) the contribution of C and N atoms are multiplied by 50.

The DOS of the Fe-$d$ electrons in the ferromagnetic state of the orthorhombic phase of the Fe perovskite reported by Zhu et al.,³⁹ is close to what obtained for the tetragonal phase of the Fe perovskite in this study.

Analysis of the contributions of the orbitals of the heavy atoms (Fe, I, N, C and Pb) to the valence and conduction bands (VB and CB), presented in Fig. S-3 of the Supplementary Materials, indicates that for both perovskites, the VB is dominated by the contributions from the iodine atomic $5p$ orbitals, while the CB is dominantly populated by the metal atom Fe (Pb) atomic $3d$ ($6p$) orbitals. Analysis of these contributions indicates that for both perovskites, the VB and CB are dominated by the contributions mainly from the Fe ($3d$) / Pb ($6p$) orbitals and partly from the I ($5p$) orbitals. Finally, the overlap of the I $5p$ and Fe $3d$ orbitals results in the

bonding orbitals (VB) of the (Fe $3d$ – I $5p$) type and the antibonding orbitals (CB) of the (Fe $3d$ – I $5p$)* type. Note that for both perovskites, contributions from the s and p orbitals of the C and N atoms to the DOSs of both VB and CB are negligible they are multiplied by 10 to make them more visible in Fig. S-3 (Supplementary Materials). It can also be seen in Fig. S-3 that energy of the Fe $3d$ orbitals is clearly lower than that of the Pb $6p$ orbitals.

The charge density distribution in the (110) $ab$ plane of the relaxed structures of the unit cells of the two perovskites are calculated and plotted in Fig. 4. Comparative analysis of these charge densities shows that the charge densities on the iodine atoms are larger in the Fe perovskites. Also, the partial $\mathrm{I^- \to M^{2+}}$ charge transfer (i.e. non-isolated $\mathrm{I^-}$ and $\mathrm{M^{2+}}$ species) is evidently stronger for the Pb perovskite, and thus charge densities of these two ions in this perovskite are more overlapped. It can be seen from Fig. 4 that the $\mathrm{M_4}$ (M = Pb or Fe) and $\mathrm{I_4}$ subunits in these relaxed structures are deviated from co-planarity. This deviation is more significant for the Pb perovskite.

![](./images/817343110202785792_5.jpg)

Fig. 4: Charge density distribution calculated for a typical plane containing $MI_4$ units (M = Fe & Pb) of the optimized structures of the two perovskites $CH_3NH_3FeI_3$ (a) & (c) and $CH_3NH_3PbI_3$ (b) & (d).

### c. Optical properties

Optical properties of the optimized structures of the $MAFeI_3$ and $MAPbI_3$ perovskites including dielectric function ($\varepsilon$), absorption coefficient ($\alpha$) and refractive index ($n$) are calculated over a wide range of wavelengths based on the wavefunctions (densities) obtained with the PBE/FP-LAPW+lo method. Because of the asymmetry of the coordination structures of the $MI_6$ units, all optical characteristics of the $MAMI_3$ lattice (M = Fe or Pb) are naturally anisotropic. Such anisotropy has already been reported for the $MAPbI_3$ perovskite both experimentally and computationally.$^{57}$

#### i. Validation

In order to validate the method used for the calculation of the optical properties, the quantities obtained for the Pb perovskite are compared with the corresponding experimental and computational results reported previously. In this way, the results obtained for the $MAPbI_3$ perovskite can serve as references to evaluate and rank the optical performance of the proposed $MAFeI_3$ perovskite, comparatively. In the following, results of this validation for the Pb perovskite are presented and discussed first.

The real and imaginary components of the complex dielectric function $(\omega) = \varepsilon_{re}(\omega) + i\ \varepsilon_{im}(\omega)$, which is considered as the main optical characteristic for a semiconductor material, are calculated and plotted in Fig. 5. These components can be used to calculate all other optical properties such as absorption coefficient $\alpha(\omega)$, and the refractive index $n(\omega)$,$^{56,57}$ which will be discussed later in this section. The dielectric function obtained for the $MAPbI_3$ perovskite are in agreement with the computational measured value reported for this perovskite by Filippetti et al $^{57}$ and the computational value reported by Shirayama et al.$^{58}$ Isotropic part of the $\varepsilon_{re}(0)$

tensor, known as the static dielectric function, for the MAPbI₃ perovskite, is also calculated to be $\varepsilon_{re}(0)=26.1$ which is in agreement with the value ($\varepsilon_{re}(0)=25.7$) calculated by DFT-PBEsol method reported by Brivio et al.⁵⁹ Comparison between our calculated values of the frequency (wavelength)-dependent absorption coefficients, $\alpha$ ($\omega$) or $\alpha$ ($\lambda$), and the previously reported computational and experimental values are summarized in Table 1. As can be deduced from data listed in this Table, our results, while matching well the results of the previous computational studies,⁵⁴,⁵⁷,⁵⁸ are in relatively good agreement with the experimental results.⁵⁷,⁶⁰,⁶¹ At 619 nm (2.00 eV), very good agreement is observed between our results and experimental data, even better than that observed for the GGA-PBE results of Tsea and Yua.⁵⁴ Note that because of application of periodic boundary condition in our DFT computations, our results should be compared with that of the thicker layer (350 nm) considered in the experimental works. Also GGA-PBE average values of the frequency-dependent refractive index ($n(\omega)$) calculated in this work for the MAPbI₃ perovskite (see Fig. 8) are in qualitative agreement with experimental data reported by Löper et al.⁶²

Table 1: Comparison between calculated values of the frequency or wavelength-dependent absorption coefficient, $\alpha$ ($\omega$) or $\alpha$ ($\lambda$), at certain wavelengths for the MAPbI₃ perovskite obtained in the present study and those reported in literature based on computational⁵⁴,⁵⁷,⁵⁸ and experimental⁵⁷,⁶⁰,⁶¹ studies.

<table>
<thead>
<tr>
<th rowspan="2">Wavelength (nm)</th>
<th rowspan="2">Energy (eV)</th>
<th colspan="3">$\alpha$ (cm⁻¹)</th>
</tr>
<tr>
<th colspan="2">Previous Studies, Methods</th>
<th>Present Study (GGA-PBE)</th>
</tr>
<tr>
<th></th>
<th></th>
<th>Computational</th>
<th>Experimental</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>401</td>
<td>3.10</td>
<td>6.5×10⁴<br>GGA-PBE ⁵⁴</td>
<td>2.02×10⁵<br>Ellipsometry ⁶⁰</td>
<td>6.8×10⁴</td>
</tr>
<tr>
<td>516</td>
<td>2.40</td>
<td>2.4×10⁵<br>LDA ⁵⁷</td>
<td>2.05×10⁵ ⁶¹</td>
<td>5.6×10⁵</td>
</tr>
<tr>
<td rowspan="2">619</td>
<td rowspan="2">2.00</td>
<td>6.2×10⁴<br>GGA-PBE ⁵⁷</td>
<td>3.8×10⁴<br>(d = 45 nm)*<br>Ellipsometry ⁵⁷</td>
<td rowspan="2">6.2×10⁴</td>
</tr>
<tr>
<td>5.1×10⁴<br>GGA-PBE ⁵⁴</td>
<td>6.8×10⁴<br>(d = 350 nm)*</td>
</tr>
</tbody>
</table>

### Ellipsometry $^{60}$

| 700 | 1.77 | $1.8×10^5$ <br> LDA $^{58}$ | $3.8×10^4$ <br> Ellipsometry $^{60}$ | $1.6×10^4$ |
|-----|------|-----------------------------|--------------------------------------|------------|

* d is the thickness of the perovskite film.

In the rest of this section, the optical characteristics obtained for the Fe and Pb perovskites are presented and analysed comparatively.

### ii. Dielectric function

Components of the real ($\varepsilon_{re}(\omega)$) and imaginary ($\varepsilon_{im}(\omega)$) parts of the frequency-dependent dielectric functions calculated for the $MAFeI_3$ and $MAPbI_3$ perovskites are plotted in Fig. 5. The peaks of these functions are attributed to various transitions from the valence band (I $5p$ orbitals) to the conduction band (Pb $6p$ or Fe $3d$ orbitals). The lowest frequency peak appears at 0.6 eV (~1.6 eV) for the $MAFeI_3$ ($MAPbI_3$) perovskites corresponds to the bandgap energies of these compounds (see Fig. 2(b & d)). Comparison of the frequency-dependent dielectric functions of the two perovskites shows that the overall patterns of their responses to the electromagnetic radiation of different frequencies are similar. Generally, the dielectric constant of $MAFeI_3$ is smaller than that of $MAPbI_3$ over the UV-Vis photon energy range.

![](./images/817343110202785792_6.jpg)

![](./images/817343110202785792_7.jpg)

Fig. 5: Spectra of the imaginary (a) and real (b) components of dielectric function, $\varepsilon_{re}(\omega)$ and $\varepsilon_{im}(\omega)$, calculated for the MAFeI₃ and MAPbI₃ perovskites in their GGA-PBE optimized tetragonal phase. Anisotropic feature of the dielectric function, with $\varepsilon_{xx} = \varepsilon_{yy} < \varepsilon_{zz}$, for both perovskites is evident.

### iii. Absorption coefficient

The wavelength-dependent (dynamic) absorption coefficient $\alpha(\lambda)$ is basically a measure of how far light with a specific wavelength (frequency or energy) can penetrate into the material before being absorbed. This absorption coefficient determines the penetration depth, i.e. $1/\alpha(\lambda)$ described by the decrease in the intensity of the light travelling in the medium (along the z direction) given by Beer-Lambert's law as $I(z) = I_0 \exp(-\alpha(\lambda)z)^{42}$. The dynamic absorption coefficient $\alpha(\lambda)$ is obtained directly from the dielectric functions using$^{42,63}$

$$
\alpha(\lambda)=\frac{2 \sqrt{2} \pi}{\lambda}\left[\sqrt{\varepsilon_{r e}(\lambda)^{2}+\varepsilon_{i m}(\lambda)^{2}}-\varepsilon_{r e}(\lambda)\right]^{1 / 2} \tag{1}
$$

where $c$ is the speed of light, and $\varepsilon_{re}(\lambda)$ and $\varepsilon_{im}(\lambda)$ are introduced earlier in this section.

Spectra of the average absorption coefficients $\bar{\alpha}(\lambda)=\frac{1}{3}\left(\alpha_{x x}(\lambda)+\alpha_{y y}(\lambda)+\alpha_{z z}(\lambda)\right)$ calculated for the MAFeI₃ and MAPbI₃ perovskites are demonstrated in Fig. 6. As can be seen in this Figure, values of $\bar{\alpha}(\lambda)$ are on the order of $10^{4}$-$10^{5} \mathrm{~cm}^{-1}$ in the visible light region.

![](./images/817343110202785792_8.jpg)

Fig. 6: Spectra of the average optical absorption coefficient, ($\bar{\alpha}(\lambda)=\frac{1}{3}(\alpha_{xx}(\lambda)+\alpha_{yy}(\lambda)+$
$\alpha_{zz}(\lambda))$), calculated by the PBE/FP-LAPW+lo method for the MAFeI₃ and MAPbI₃ perovskites.

Comparison of the absorption coefficient spectra calculated for the two Fe and Pb perovskites shows that in the 100-280 nm part of the UV region, absorption of the MAFeI₃ perovskite is generally lower than that of the traditional MAPbI₃ perovskite. This can be regarded as an advantage for the proposed Fe perovskite in that it reduces photodegradation and structural damage of the perovskite layer which may arise due to the absorption of the UV radiation. The $\bar{\alpha}(\lambda)$ spectra plotted in Fig. 6 show also that the two MAFeI₃ and MAPbI₃ perovskites have close absorptions in the visible light region, and therefore feasibility study of the replacement of the Pb metal with the Fe metal in the structure of the perovskites used in PSCs is justified.

The narrower bandgap obtained by GGA-PBE method for the iron perovskite, Fig. 2(b), results in a red-shift of the absorption peaks of the proposed iron perovskite to longer wavelengths in the visible light region compared to those of the lead perovskite.

A detailed comparative analysis of the optical performances of the two MAFeI₃ and MAPbI₃ perovskites can be carried out based on an optical correlation function $c_p(\lambda)$ defined as

$$
c_{p}(\lambda)=\bar{\alpha}_{p}(\lambda) \times \bar{I}_{s u n}(\lambda) \tag{2}
$$

in which $\bar{\alpha}_{p}(\lambda)$ is the average absorption coefficient at wavelength $\lambda$ calculated for the $p$ (MAFeI$_3$ or MAPbI$_3$) perovskite, and $\bar{I}_{sun}(\lambda)$ is the average irradiance of sun at wavelength $\lambda$ (plotted in Fig. 7(a)). The optical correlation function $c_{p}(\lambda)$ represents the extent of the match between absorption coefficient $\bar{\alpha}_{p}(\lambda)$ of the perovskite $p$ and the average irradiance of sun at each wavelength $\lambda$.

The wavelength-dependent optical correlation function is calculated for both perovskites and the results are plotted in Fig. 7(b). It can be seen from this Figure that the absorption coefficient of the proposed MAFeI$_3$ perovskite is more strongly correlated with the solar radiation spectrum in the 340-425 nm and $\lambda > 620$ nm ranges of wavelengths. While, the absorption coefficient of the traditional MAPbI$_3$ perovskite shows a stronger correlation in the ranges of $\lambda < 340$ nm and 480-580 nm (i.e. near the green-yellow light). Furthermore, weaker correlation of the absorption coefficient of the MAFeI$_3$ perovskite to the solar radiation irradiance in the UV region can be regarded as an advantage of this proposed perovskite for applied purposes, as discussed earlier.

The optical correlation function $c_{p}(\lambda)$, as described in Equation (3), has also been calculated for the orthorhombic phase of iron perovskite based on the absorption spectrum calculated by Zhu et al. using the GGA+U method. This correlation function is also plotted in Fig. 7(b). A comparative analysis shows that as compared to that of its tetragonal phase studied in this work, the orthorhombic phase of iron perovskite studied by Zhu et al. $^{39}$ has better optical performance over the most of the visible light spectrum, However, instability of this orthorhombic phase at room temperature is a critical disadvantage which overwhelm its better optical performance.

![](./images/817343110202785792_9.jpg)

Fig. 7: (a) The wavelength-dependent average irradiance of sun, $\bar{I}_{sun}(\lambda)$, derived from the data taken from Solar Radiation and Climate Experiment (SORCE). $^{64}$ (b) The wavelength-dependent optical correlation function $c_{p}(\lambda)$, defined in Eq. (2), calculated for the $MAFeI_{3}$ and $MAPbI_{3}$ perovskites. Optical correlation function has also been calculated for the orthorhombic phase of iron perovskite based on the absorption spectrum reported just recently by Zhu et al. $^{39}$

The overall optical correlation coefficient $C(p)$ for each perovskite $p$ can be obtained by integrating its wavelength-dependent optical correlation function over the whole range of solar spectrum, i.e.

$$
C(p)=\frac{\int_{\lambda_{1}}^{\lambda_{2}} \bar{\alpha}_{p}(\lambda) \times \bar{I}_{sun}(\lambda) d \lambda}{\int_{\lambda_{1}}^{\lambda_{2}} \bar{\alpha}_{p}(\lambda) d \lambda \times \int_{\lambda_{1}}^{\lambda_{2}} \bar{I}_{sun}(\lambda) d \lambda} \tag{3}
$$

In this equation, the integrals in the denominator are included to normalize the value of the overall correlation coefficient value. All integrals of Eq. (3) are carried out from $\lambda_{\text{min}}=310$ to $\lambda_{\text{max}}=830$. The $C(p)$ values calculated for the two perovskites are $C(MAFeI_{3})=84.2$ and

$C(MAPbI_3) = 138.3$. Based on these values, the raw relative optical performance $R_{Fe/Pb}$ of the two Fe and Pb perovskites can thus be defined and calculated as

$$
R_{Fe/Pb} = 100\left(\frac{C(MAFeI_3)}{C(MAPbI_3)}\right) \cong 61\% \tag{4}
$$

This relative optical performance shows that under equal conditions, in the tetragonal phase, the proposed Fe perovskite will have an efficiency ~61% that of the Pb perovskite. These relatively close performances show that the Fe perovskite can be considered as an appropriate alternative to replace the hazardous Pb perovskite in the sunlight absorbing layer of PSCs.

The overall optical correlation coefficient and relative optical performance calculated for the orthorhombic phase of Fe perovskite$^{31}$ are ~126 and ~91%, respectively, which shows its superiority over the tetragonal Fe perovskites studied in the present work, provided that it could be stable at room temperature.

### iv. Refractive Index

The wavelength-dependent average refractive indices $\bar{n}(\lambda) = \frac{1}{3}(n_{xx}(\lambda) + n_{yy}(\lambda) + n_{zz}(\lambda))$ of the two perovskites are calculated and plotted in Fig. 8. For comparison, the experimental refractive indices reported by Löper et al.$^{62}$ for the lead perovskite are also included in this Figure.

![](./images/817343110202785792_10.jpg)

Fig. 8: Average values of wavelength-dependent refractive index $\bar{n}(\lambda)=\frac{1}{3}(n_{xx}(\lambda)+$
$n_{yy}(\lambda)+n_{zz}(\lambda))$ obtained by GGA-PBE computations for the optimized structures of
the tetragonal phases of the $MAFeI_{3}$ and $MAPbI_{3}$ perovskites. Experimental data
reported by Löper et al. $^{62}$ for the $MAPbI_{3}$ perovskites are also presented for
comparison.

Comparative analysis of the computational and experimental values of the refractive indices
obtained for the $MAPbI_{3}$ perovskite, plotted in Fig. 8, shows that the present GGA-PBE method
systematically underestimates and has not be able to accurately predict the refractive indices.

It can also be seen in Fig. 8 that the overall shape of the calculated refractive indices of the two
$MAFeI_{3}$ and $MAPbI_{3}$ perovskites are similar except at the two limiting ranges of wavelengths.

Also, the proposed Fe perovskite has smaller refractive index in the visible region (400-800
nm). In the 400-540 nm range, values of the wavelength-dependence refractive indices of the
iron and lead perovskites are almost compatible.

### v. Brewster angle

Configuration of a PSC device involves a perovskite layer as the photoactive material
sandwiched between an indium tin oxide ITO coated glass as the anode, $TiO_{2}$ layer as the
electron transfer material (ETM) and a spiro-OMeTAD layer as the hole transfer material
(HTM) in the order of air/ITO/TiO$_{2}$/perovskite/spiro. $^{65}$ Since, the overall efficiency of a solar
cell depends on the reception and harvesting of more photons of the incident light crossing the
TiO$_{2}$/perovskite interface, a larger Brewster angle $(\theta_{B})$ at this interface favours this efficiency.

Also, higher reflectance of the un-absorbed photons from the perovskite/spiro interface back
into the perovskite layer increases the overall absorption efficiency of light. A larger Brewster
angle at the TiO$_{2}$/perovskite interface, corresponds to less reflection and higher intensity of the
incident light crossing this interface to enter the perovskite layer. While, a smaller Brewster
angle at the perovskite/spiro interface corresponds to more reflected light from this interface
back to the bulk of the perovskite layer to be harvested further. Under either or both of these

two conditions, efficiency of the solar cell is increased. This effect of Brewster angle is shown pictorially in Fig. 9.

![](./images/817343110202785792_11.jpg)

Fig. 9: Typical optical paths in a perovskite solar cell (PSC) showing the importance of appropriate relative refractive indices of the TiO₂, perovskite (MAPbI₃ or MAFel₃) and spiro layers, defining the Brewster angles of the TiO₂/perovskite and perovskite/spiro interfaces, in its overall optical performance.

The Brewster angles of the two TiO₂/perovskite and perovskite/spiro interfaces are calculated for the two MAFeI₃ and MAPbI₃ perovskites and plotted in Fig. 10 as functions of the wavelength of the light. A comparative analysis of this Figure shows that except for the 470-520 nm wavelength range, the proposed MAFeI₃ perovskite has smaller TiO₂/perovskite Brewster angle ($	heta_{\text{B}}$) referenced to that of the MAPbI₃ perovskite. This means that reflection from the TiO₂/perovskite interface for the MAFeI₃ perovskite results in larger loss of the received sunlight compared to that for the MAPbI₃ perovskite. This is while, smaller Brewster angle of the MAFeI₃/spiro interface in most parts of the visible range, except for the small 480-540 nm range, results in larger reflection of the un-absorbed sunlight from this interface back to the bulk of the perovskite. Therefore, smaller $	heta_{\text{B}}$ (MAFeI₃/spiro) compared to $	heta_{\text{B}}$ (MAPbI₃/spiro) compensates the inferiority of the iron perovskite due to smaller $	heta_{\text{B}}$ (TiO₂/MAFeI₃) compared to $	heta_{\text{B}}$ (TiO₂/MAPbI₃).

![](./images/817343110202785792_12.jpg)

**Fig. 10:** Calculated Brewster angles ($\theta_{\mathrm{B}}$) at the interface of the electron transfer material (ETM), $\mathrm{TiO}_{2}$ and perovskite, and between the hole transfer material (HTM) spiro and perovskite layers. The refractive indices at different wavelengths for $\mathrm{TiO}_{2}$ and Spiro - OMeTAD are taken respectively from the reports by Shannon et al.⁶⁶ and Filipic et al.⁶⁷ No experimental refractive index is available for $\mathrm{TiO}_{2}$ below 430 nm, and thus the Brewster angles $\theta_{\mathrm{B}}$ for the two $\mathrm{TiO}_{2}/\mathrm{MAPbI}_{3}$ and $\mathrm{TiO}_{2}/\mathrm{MAFeI}_{3}$ interfaces could not be calculated for this wavelength range.

The net relative optical performances of the two perovskites due to these Brewster angles are quantified as follows. Relative refraction/reflection performance of the Fe perovskite with respect to that of the Pb perovskite in a $\mathrm{L}_{1}/\mathrm{L}_{2}/\mathrm{L}_{3}$ set of layers, with $\mathrm{L}_{1}, \mathrm{L}_{2}, \mathrm{L}_{3}$ being respectively the $\mathrm{TiO}_{2}$, perovskite and spiro layers (Fig. 10), can be estimated based on the corresponding Brewster angles using $r_{12} = \frac{\theta_{B}^{L_{1}/L_{2}(Fe)}}{\theta_{B}^{L_{1}/L_{2}(Pb)}}$ and $r_{23} = \frac{\theta_{B}^{L_{2}/L_{3}(Pb)}}{\theta_{B}^{L_{2}/L_{3}(Fe)}}$ factors. For example, at $\lambda = 600$ nm, these factors are evaluated to be $r_{12} = 0.98$ and $r_{23} = 1.35$, and the net relative refraction/reflection performance $R_{B}$ due to the Brewster angles can be obtained by multiplication of these two factors as $\mathrm{R_{B}} = r_{12} \times r_{23} = 1.32$ which ranks higher the proposed tetragonal Fe perovskite. In case of the usage of adjustable rotating solar cell panels, the Brewster angle at the $\mathrm{TiO}_{2}$/perovskite interface becomes inactive, while the Brewster angle at

the perovskite/spiro remains still active for scattered light from the dispersed multi-crystalline perovskite and/or spiro surfaces.

Since no computational refractive index is reported for the orthorhombic phase of Fe perovskite,³⁹ relative refraction/reflection performance cannot be calculated for this phase of the Fe perovskite as a layer of solar cell.

## IV. Summary and conclusion

Electronic structures and optical properties of tetragonal phase of the perovskites CH₃NH₃MI₃ (M = Fe, Pb) as the optically active layer of a class of solar cells thus named perovskite solar cells (PSC) are calculated using the GGA-PBE/FP-LAPW+lo DFT method. In the first step, it was proved that these GGA-PBE calculations are able to reproduce the experimental structures and properties reported for the MAPbI₃ perovskite which is currently being used in the structure of efficient PSCs. Therefore, results of this DFT method can be regarded reliable for the accurate computational prediction of the properties of the considerable less expensive and non-toxic MAFeI₃ perovskite, proposed in this work. Larger supercells and more advanced methods can basically improve quality of the computations and allow to discover possible inter-unit tilting to achieve more realistic and more reliable results. However, the approach adopted in the present research remain valid regardless of the applied method and the size of supercell.

Band structures and total and partial densities of states in the spin up and spin down polarizations for both MAFeI₃ and MAPbI₃ perovskites are calculated and compared. For MAFeI₃, the difference between the two spin states is remarkable denoting magnetic characteristics of this perovskite. The calculated band structure (BS) diagrams indicate that MAFeI₃ perovskite is a direct bandgap lattice at the $\Gamma$ point with $\mathrm{E_g} = 0.66$ eV energy. The bandgap obtained for the Fe perovskite is narrow which is comparable with those experimentally reported for the Sn perovskite ($\mathrm{E_g}$ = 0.61-1.2 eV) candidated to be used in PSCs.

Although the calculated absorption coefficient spectra show that the MAFeI₃ perovskite has a weaker UV light harvester than the MAPbI₃ perovskite, the absorption of the Fe perovskite in the visible region is however high enough to be considered for application in solar cells, especially that it has less UV absorption as compared to the Pb perovskite, and thus undergoes less photodamage and thus is expected to have longer life time.

Analysis of an optical performance index, introduced and calculated in this work for measuring correlation of the UV-Vis absorption spectrum of any optically active material with the irradiance spectrum of sun, shows that the optical performance of iron perovskite is ~61% that of the lead perovskite. This value of relative performance puts the proposed iron perovskite in order for a thorough experimental investigation to prove feasibility of its synthesis and evaluation of its performance in PSCs under operating conditions as a nontoxic and less-expensive alternative of the common hazardous lead perovskite.

Analysis of the Brewster angle $	heta_B$ calculated based on the refractive indices calculated in this work for the two perovskites and those experimentally measured and reported for the TiO₂ and spiro layers of solar cells shows that the Brewster angle at the TiO₂/perovskite and perovskite/spiro interfaces are respectively in favour of the proposed MAFeI₃ perovskite and MAPbI₃ perovskite. For example, at $\lambda$=600 nm, the overall Brewster angle is by a factor of 1.32 in favor of the Fe perovskite.

In conclusion, the CH₃NH₃FeI₃ perovskite can be introduced as a promising material with much lower costs and without any environmental hazards to replace the environmentally hazardous CH₃NH₃PbI₃ perovskite as light absorber in solar cells.

### Acknowledgement

We would like to acknowledge Isfahan University of Technology for software and hardware facilities.

References:

1 C. Quarti, E. Mosconi and F. De Angelis, Structural and electronic properties of organohalide hybrid perovskites from ab initio molecular dynamics. Phys. Chem. Chem. Phys. 17, 9394-9409 (2015).

2 L. Fraas and L. Partain, Solar cells and their applications, $2^{nd}$ Ed., Wiley, 34-35 91995.

3 Z. Shi and A. H. Jayatissa, Perovskites-based solar cells: a review of recent progress, materials and processing methods. Materials 11, 729 (2018).

4 J. Zhao, A. Wang, M. A. Green and F. Ferrazza, 19.8% efficient honeycomb textured multicrystalline and 24.4% monocrystalline silicon solar cells. Appl. Phys. Lett. 73, 1991-1993 (1998).

5 T. Chien Sum and N. Mathews, Advancements in perovskite solar cells: photophysics behind the photovoltaics. Energy Environ. Sci. 7, 2518-2534 (2014).

6 A. Kojima, K. Teshima, Y. Shirai and T. Miyasaka, Organometal halide perovskites as visible-light sensitizers for photovoltaic cells. J. Am. Chem. Soc. 131, 6050-6051 (2009).

7 J. H. Im, C. R. Lee, J. W. Lee, S. W. Park and N. G. park, 6.5% efficient perovskite quantum-dot-sensitized solar cell. Nanoscale, 3, 4088-4093 (2011).

8 M. M. Lee, J. Teuscher, T. Miyasaka, T. N. Murakami and H. J. Snaith, Efficient hybrid solar cells based on meso-superstructured organometal halide perovskites. Science 338, 643-647 (2012).

9 J. T. W. Wang, J. M. Ball, E. M. Barea, A. Abate, J. A. Alexander-Webber, J. Huang, M. Saliba, I. Mora-Sero, J. Bisquert and H. J. Snaith, Low-temperature processed electron collection layers of graphene/TiO₂ nanocomposites in thin film PSCs. Nano Lett. 14, 724-730 (2014).

10 J. Liu, G. Wang, Z. Song, X. He, K. Luo, Q. Ye, C. Liao, J. Me, FAPb₁₋ₓSnₓI₃ mixed metal halide perovskite with improved light harvesting and stability for efficient planar heterojunction solar cells. J. Mater. Chem. A, 5, 9097-9106, (2019).

11 Z. K. Wang, M. Li, Y. G. Yang, H. Ma, X. Y. Gao and L. S. Liao, High efficiency Pb-In binary metal perovskite solar cells. Adv. Mater. 28, 6695-6703 (2016).

12 W. S. Yang, J. H. Noh, N. J. Jeon, Y. C. Kim, S. Ryu, J. Seo and S. I. Seok, High-performance photovoltaic perovskite layers fabricated through intramolecular exchange. Science 348, 1234-1237 (2015).

13 M. K. Nazeeruddin, In retrospect: twenty-five years of low-cost solar cells. Nature 538, 463-464 (2016).

14 C. O. Ramírez Quiroz, Y. M. Shen, Salvador, K. Forberich, N. Schrenker, G. D. Spyropoulos, T. Heumüller, B. Wilkinson, T. Kirchartz and E. Spiecker, Balancing electrical and optical

losses for efficient 4-terminal Si-PSCs with solution processed percolation electrodes. J. Mater. Chem. A 6, 3583 (2018).

15 P. Gao, M. Grätzel, M. K. Nazeeruddin, Organohalide lead perovskites for photovoltaic applications. Energy Environ. Sci. 7, 2448-2463 (2014).

16 Q. A. Lin, Armin, R. C. Raju Nagiri, P. L. Burn and P. Meredith, Electro-optics of perovskite solar cells. Nat. Photonics 9, 106-112 (2015).

17 Z. Cheng and J. Lin, Layered organic – inorganic hybrid perovskites: Structure, optical properties, film preparation, patterning and templating engineering. CrystEngComm. 12, 2646-2662 (2010).

18 M. Johnsson and P. Lemmens, Perovskites and thin films – crystallography and chemistry. J. Phys. Condens. Matter 20, 264001 (2008).

19 Y. Dang, X. Tao, Y. Liu, Y. Sun, D. Yuan, X. Liu, W. Lu, G. Liu and H. Xia, Bulk crystal growth of hybrid perovskite material $CH_3NH_3PbI_3$. CrystEngComm. 17, 665-670 (2015).

20 D. Zhou, T. Zhou, Y. Tian and X. Zhu, Perovskite-based solar cells: materials, methods and future perspectives. J. Nanomater. 8148072(1-15) (2018).

21 European Parliament and Council. Directive 2002/95/EC on the restriction of the use of certain hazardous substances in electrical and electronic equipment, Official J. Eur. Union 46, 19-23 (2003).

22 M. Grätzel, The light and shade of perovskite solar cells. Nat. Mater. 13, 838-842 (2014).

23 G. Hodes, Perovskite-Based Solar Cells. Science 342, 317-318 (2013).

24 A. Babayigit, D. D. Thanh, A. Ethirajan, J. Manca, M. Muller, H. G. Boyen and B. Conings, Assessing the toxicity of Pb- and Sn-based perovskite solar cells in model organism Danio rerio. Sci. Rep. 6, 18721(1-11) (2016).

25 C. Zuo and L. Ding, Lead-free perovskite materials $(NH_4)_3Sb_2I_xBr_{9-x}$. Angew. Chem. Int. Ed. 56, 6528-6532 (2017).

26 F. Hao, C. C. Stoumpos, D. H. Cao, R. P. H. Chang and M. G. Kanatzidis, Lead-free solid- state organic-inorganic halide PSCs. Nat. Photonics 8, 489-494 (2014).

27 D. Fabini, Quantifying the potential for lead pollution from halide perovskite photovoltaics. J. Phys. Chem. Lett. 6, 3546-3548 (2015).

28 N. K. Noel, S. D. Stranks, A. Abate, C. Wehrenfennig, S. Guarnera, A. A. Haghighirad, A. Sadhanala, G. E. Eperon, S. K. Pathak, M. B. Johnston A. Petrozza, et al. Lead-free organic- inorganic tin halide perovskites for photovoltaic applications. Energy Environ. Sci. 7, 3061-3068 (2014).

29 H. L. Zhu, J. Xiao, J. Mao, H. Zhang, Y. Zhao and W. C. H. Choy, Controllable crystallization of $CH_3NH_3Sn_{0.25}Pb_{0.75}I_3$ perovskites for hysteresis-free solar cells with efficiency reaching 15.2%. Adv. Funct. Mater. 27, 1605469 (2017).

$^{30}$ U.S. department of health and human services. Public health service agency for toxic substances and disease registry, toxicological profile for tin and tin compounds. https://www.atsdr.cdc.gov/toxprofiles/tp55.pdf, August, 25-36 (2005).

$^{31}$ S. Körbel, M. A. L. Marques and S. Botti, Stable hybrid organic-inorganic halide perovskites for photovoltaics from *ab initio* high-throughput calculations. J. Mater. Chem. A **6**, 6463-6475 (2018).

$^{32}$ M. Roknuzzaman, K. Ostrikov, H. Wang, A. Du and T. Tesfamichael, Towards lead-free perovskite photovoltaics and optoelectronics by *ab-initio* simulations. Sci. Rep. **7**, 14025 (2017).

$^{33}$ C. J. Yu, Advances in modelling and simulation of halide perovskites for solar cell applications. J. Phys. Energy 022001 (2019).

$^{34}$ T. Krishnamoorthy, H. Ding, C. Yan, W. L. Leong, T. Baikie, Z. Zhang, M. Sherburne, S. Li, M. Asta, N. Mathews and S. G. Mhaisalkarac, Lead-free germanium iodide perovskite materials for photovoltaic applications. J. Mater. Chem. A **3**, 23829-23832 (2015).

$^{35}$ V. Kumar and R. Santosh, First-principle calculations of structural, electronic, optical and thermodynamical properties of fluorinated graphene, MSEB **246**, 127-135 (2019).

$^{36}$ Bakhtiar Ul Haq, Rashid Ahmed and Souraya Goumri-Said, DFT characterization of cadmium doped zinc oxide for photovoltaic and solar cell applications. Sol. Energy Mater. Sol. Cells **130**, 6-14 (2014).

$^{37}$ M. P. Balanay and D. H. Kim, DFT/TD-DFT molecular design of porphyrin analogues for use in dye-sensitized solar cells. PCCP, **10**, 5121-5127 (2008).

$^{38}$ H. M. Huang, Z. Y. Jiang, Y. M. Lin, B. Zhou and C. Kun Zhang, Design of half-metal and spin gapless semiconductor for spintronics application via cation substitution in methylammonium lead iodide. Appl. Phys. Express **10**, 123002 (2017).

$^{39}$ H. X. Zhu, X. H. Wang and G. C. Zhuang, Electronic structure, magnetism properties and optical absorption of organometal halide perovskite $CH_3NH_3XI_3$ (X = Fe, Mn). Appl. Phys. A **125**, 45 (2019).

$^{40}$ P. V. Kamat, J. Bisquert and J. Buriak, Lead-free perovskite solar cells. ACS Energy Lett. **2**, 904-905 (2017).

$^{41}$ F. Huiying, Review of lead-free halide perovskites as light-absorbers for photovoltaic applications: From materials to solar cells. Sol. Energy Mater. Sol. Cells **193**, 107-132 (2019).

$^{42}$ M. Fox, Optical properties of solids. 2$^{nd}$ Ed., Oxford, New York, 354-355 (2010).

$^{43}$ K. Schwarz, P. Blaha and G. K. H. Madsen, Electronic structure calculations of solids using the WIEN2k package for material sciences. Comput. Phys. Commun. **147**, 71-76 (2002).

$^{44}$ L. P. J. Even, J. M. Jancu and C. Katan, Importance of spin-orbit coupling in hybrid organic/inorganic perovskites for photovoltaic applications. J. Phys. Chem. Lett. 4, 2999-3005 (2013).

$^{45}$ Y. Zhao and D. G. Truhlar, Calculation of semiconductor band gaps with the M06-L density functional. J. Chem. Phys. 130, 074101-074103 (2009).

$^{46}$ H. Xiao, J. Tahir-Kheli and W. A. Goddard, Accurate band gaps for semiconductors from density functional theory. J. Phys. Chem. Lett. 2, 212-217 (2011).

$^{47}$ J. E. Huheey, E.A. Keite and R.L. Keiter, Inorganic chemistry: principles of structure and reactivity, $4^{th}$ Ed., HarperCollins, New York, 394-398 (1993).

$^{48}$ P. Sharma and G. C. Kaphle, Electronic and magnetic properties of half metallic heusler alloy $Co_2$MnSi: a first-principles study. JNPS 4, 60-66 (2017).

$^{49}$ A. Yang, M. Bai, X. Bao, J. Wang, W. Zhang, Investigation of Optical and Dielectric Constants of Organic-Inorganic $CH_3NH_3PbI_3$ Perovskite Thin FilmsJ. Nanomed. Nanotechnol. 7, 407 (2016).

$^{50}$ E. Menéndez-Proupin, P. Palacios, P. Wahnón and J. C. Conesa, Investigation of optical and dielectric constants of organic-inorganic $CH_3NH_3PbI_3$ perovskite thin films. Phys. Rev. B 90, 045207 (2014).

$^{51}$ T. Ahmed, C. La-o-Vorakiat, T. Salim, Y. M. Lam, E. E. M. Chia and J. X. Zhu, Optical properties of organometallic perovskite: an ab initio study using relativistic GW correction and Bethe-Salpeter equation. EPLA 108, 6 (2014).

$^{52}$ S. X. Tao, X. Cao and P. A. Bobbert, Accurate and efficient band gap predictions of metal halide perovskites using the DFT-1/2 method: GW accuracy with DFT expense. Sci. Rep. 7, 14386 (2017).

$^{53}$ P. Umari, E. Mosconi and F. D. Angelis, Relativistic GW calculations on $CH_3NH_3PbI_3$ and $CH_3NH_3SnI_3$ perovskites for solar cell applications. Sci. Rep. 4, 4467 (2014).

$^{54}$ G. Tsea and D. Yua, First principle study: optical properties of $CH_3NH_3PbI_3$ and $CH_3NH_3SnI_3$ for perovskite photovoltaics. AJCEM 4, 49-55 (2015).

$^{55}$ Y. Takahashi, R. Obara, Z. Z. Lin, Y. Takahashi, T. Naito, T. Inabe, S. Ishibashib and K. Terakura, Charge-transport in tin-iodide perovskite $CH_3NH_3SnI_3$: origin of high conductivity. Dalton Trans. 40, 5563 (2011).

$^{56}$ F. Giustino and H. J. Snaith, Toward lead-free perovskite solar cells. ACS Energy Lett. 1, 133-1240 (2016).

$^{57}$ A. Filippetti and A. Mattoni, Hybrid perovskites for photovoltaics: insights from first principles. Phys. Rev. B 89, 125203 (2014).

$^{58}$ M. Shirayama, H. Kadowaki, T. Miyadera, T. Sugita, M. Tamakoshi, M. Kato, T. Fujiseki, D. Murata, S. Hara and T. N. Murakami, Optical transitions in hybrid perovskite solar cells: ellipsometry, density functional theory and quantum efficiency analyses for $CH_3NH_3PbI_3$. Phys. Rev. Appl. 5, 014012 (2016).

$^{59}$ F. Brivio, K. T. Butler and A. Aron Walsh, Relativistic quasiparticle self-consistent electronic structure of hybrid halide perovskite photovoltaic absorbers. Phys. Rev. B $\mathbf{89}$, 155204 (2014).

$^{60}$ L. J. Phillips, A. M. Rashed, R. E. Treharne, J. Kay, P. Yates, I. Mitrovic, A. S. Hall and K. Durose, Dispersion relation data for methylammonium lead triiodide perovskite deposited on a (100) silicon wafer using a two-step vapour-phase reaction processs. Mater. Sol. Cells. $\mathbf{5}$, 926-928 (2015).

$^{61}$ J. M. Ball, S. D. Stranks, M. T. Hörantner, S. Hüttner, W. Zhang, E. J. W. Crossland, I. Ramirez, M. Riede, M. B. Johnston, R. H. Friend and H. J. Snaith, Energy Environ. Sci. $\mathbf{8}$, 602-609 (2015).

$^{62}$ P. Löper, M. Stuckelberger, B. Niesen, J. Werner, M. Filipič, S. Moon, J. Yum, M. Topič, S. De Wolf and C. Ballif, Complex refractive index spectra of $CH_3NH_3PbI_3$ perovskite thin films determined by spectroscopic ellipsometry and spectrophotometry. J. Phys. Chem. Lett. $\mathbf{6}$, 66-71 (2015).

$^{63}$ A. Soni, A. Dashora, V. Gupta, C. Arora, M. Rérat, B. L. Ahuja and R. Pandey, Electronic and optical modeling of solar cell compounds CuGaSe$_2$ and CuInSe$_2$. J. Electron. Mater. $\mathbf{40}$, 2197-2208 (2011).

$^{64}$ Solar radiation and climate experiment SORCE, Laboratory for atmospheric and space physics, http://lasp.colorado.edu/home/sorce/, visited on Dec. $20^{th}$, (2018).

$^{65}$ H. J. Du, W. C. Wang and Y. F. Gu, Chin. Phys. B $\mathbf{26}$, 028803-028807 (2017).

$^{66}$ R. D. Shannon, R. C. Shannon, O. Medenbach and R. X. Fischer, Refractive index and dispersion of fluorides and oxides. J. Phys. Chem. $\mathbf{31}$, 931-970 (2002).

$^{67}$ M. Filipic, P. Löper, B. Niesen, S. De Wolf, J. Krc, C. Ballif and M. Topič, $CH_3NH_3PbI_3$ perovskite/silicon tandem solar cells: characterization based optical simulations. Optics Express $\mathbf{23}$, 263-278 (2015).

# Graphical Abstract

Iron perovskite $\text{CH}_3\text{NH}_3\text{FeI}_3$, with comparable optical performance, is a good candidate to replace lead perovskite $\text{CH}_3\text{NH}_3\text{PbI}_3$ in solar cells to reduce their prices and environmental hazards.

![](./images/817343110202785792_13.jpg)