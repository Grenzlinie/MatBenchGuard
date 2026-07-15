# Two-Dimensional Phosphorus Oxides as Energy and Information Materials

Wei Luo and Hongjun Xiang*

**Abstract:** Phosphorene is a rising star in electronics. Recently,2D phosphorus oxides with higher stability have been synthe-sized. In this study, we theoretically explored the structures and properties of 2D phosphorus oxides. We found that the structural features of $P_xO_y$ vary with the oxygen content. When the oxygen content is low, the most stable $P_xO_y$ material can be obtained by the adsorption of O atoms on phosphorene. Otherwise, stable structures are no longer based on phosphor-ene and will contain P-O-P motifs. We found that $P_4O_4$ has a direct band gap (about 2.24 eV), good optical absorption, and high stability in water, so it may be suitable for photo-chemical water splitting. $P_2O_3$ adopts two possible stable ferroelectric structures ($P_2O_3$-I and $P_2O_3$-II) with electric polarization perpendicular and parallel to the lateral plane, respectively, as the lowest-energy configurations, depending on the layer thickness. We propose that $P_2O_3$ could be used in novel nanoscale multiple-state memory devices.

Two-dimensional (2D) materials have attracted a lot of interest because of their novel physical properties and potential applications. $^{[1]}$ Graphene is a representative 2D material $^{[1a-d]}$ in which many exotic phenomena were discov ered owing to the presence of a Dirac-type band dispersion. However, the absence of a band gap unfortunately limits its application in electronic and optoelectronic devices. Subse-quently, monolayer transition-metal dichalcogenides (TMDs) were studied extensively owing to their intrinsic direct band gaps. $^{[1e-g]}$ Despite multiple studies in which electronic and optoelectronic devices based on monolayer TMDs have shown high on/off ratios and high responsivity, the carrier mobility of these TMDs is still much lower than that of graphene. $^{[2]}$ Most recently, 2D monolayer black phosphorus(BP), that is, phosphorene, has attracted much attention, since it not only has a direct band gap of about $2.0 eV,^{[3]}$ but also high carrier mobility. $^{[4]}$ Interestingly, other phosphorene-like materials were predicted to display high carrier mobilities and a broad range of band gaps. $^{[5]}$ These unique properties make phosphorene superior to graphene in electronic and opto-electronic applications. In fact, it was demonstrated that a field-effect transistor (FET) made of few-layer black phosphorus presented a high on/off ratio. $^{[4a]}$ A photodetector made of multilayer black phosphorus also exhibited high-contrast images both in the visible and the infrared spectral regime. $^{[6]}$ Owing to the inherent orthorhombic waved struc ture of phosphorene, the carrier mobility is highly aniso-tropic, $^{[7]}$ and its electronic properties can be readily tuned by strain, which could be useful in some special applications. $^{[8]}$

Although phosphorene is a promising material with many novel properties, it has a well-known drawback. It degradesreadily in a humid environment in the presence of oxygen. $^{[9]}$  Therefore, it is important to understand the oxidation mechanism of phosphorene. This mechanism is difficult to investigate directly through experiments since oxidation may lead to amorphous structures that can not be probed by diffraction, and since most techniques that measure the real-space structure lead to further sample degradation. Theoret-ically, Ziletti et al. found that a single O atom tended to adsorb on one phosphorus atom to form the dangling-type structure. $^{[9a]}$ This behavior is observed because the electron lone pair of the $sp^{3}$-hybridized P atom can interact with an oxygen atom, which needs two more electrons to satisfy the octet rule. Thus, the interaction mechanism between phos-phorene and a few oxygen molecules and oxygen atoms is now clear. $^{[10]}$ However, the structure and properties of recently synthesized layered phosphorus oxide compounds($P_xO_y$) with a high oxygen concentration are not well under-stood. $^{[11]}$ Although some model structures for 2D phosphorus oxides have been built manually, $^{[12]}$ it is possible that these model structures are not necessarily stable. On the other hand, like graphene oxides, $^{[13]}$ 2D phosphorus oxides them selves may serve as novel functional materials with fascinating properties. In fact, Lu et al. experimentally demonstrated that phosphorus oxides and suboxides not only have tunable band gaps, but also are much more stable than pristine phosphor-ene under ambient conditions. They further showed that these2D phosphorus oxides could be used in multicolored-display and toxic-gas-sensor applications. $^{[14]}$ Thus, a detailed under standing of the structure of 2D phosphorus oxides will not only provide deeper insight into the degradation mechanism, but also may lead to the discovery of new functional 2D materials.

In this study, we systematically predicted the lowest-energy structures of 2D phosphorus oxides through our newly developed global optimization approach $^{[15a-c]}$ based on the particle swarm optimization (PSO) technique. $^{[15d]}$ We found that 2D phosphorus oxides keep the phosphorene framework with dangling P=O motifs when the oxygen concentration is low, whereas P-O-P motifs will exist when the oxygen concentration is higher than one third. In the most stable

---

[*] W. Luo, Prof. Dr. H. J. Xiang
Key Laboratory of Computational Physical Sciences (Ministry of Education), State Key Laboratory of Surface Physics and Department of Physics, Fudan University
Shanghai 200433 (China)
and
Collaborative Innovation Center of Advanced Microstructures
Nanjing 210093 (China)
E-mail: hxiang@fudan.edu.cn

![](./images/813491590864568321_1.jpg)
Supporting information for this article can be found under:
http://dx.doi.org/10.1002/anie.201602295.

Angew. Chem. 2016, 128, 8717-8722
© 2016 Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim
Wiley Online Library

structures of $P_{4}O_{4}$ and $P_{2}O_{3}$ with a thickness less than $3.2\ \mathring{A}$, there are only P-O-P motifs and no dangling P=O motif. Interestingly, the most stable structure of 2D $P_{4}O_{4}$, that is, $P_{4}O_{4}$-I, has a direct band gap of 2.24 eV, good optical absorption, appropriate band edge positions, and high stability in water, thus suggesting that it may be used for photocatalytic water splitting. For 2D $P_{2}O_{3}$, there are two stable ferroelectric structures (namely, $P_{2}O_{3}$-I and $P_{2}O_{3}$-II) with non-zero out-of-plane and in-plane polarization, respectively, thus suggesting that 2D $P_{2}O_{3}$ may be used in novel multiple-state memory devices. Our study shows that 2D phosphorus oxides could act as novel functional materials.

We searched the stable structures of 2D phosphorus oxides with different oxygen concentrations through a global optimization approach. For some oxygen concentrations, we found new structures with total energies lower than those of the previously proposed structures. Herein, we first discuss the structural features of 2D phosphorus oxides as revealed by PSO simulations. We then focus on 2D $P_{4}O_{4}$ and $P_{2}O_{3}$ to demonstrate that they are promising materials for use in photochemical water splitting and ferroelectric multiple-state memory, respectively.

From our PSO simulations, we found that the stable structures of phosphorus oxides displayed different motifs when the oxygen concentration varied. This behavior is observed because the Coulomb interactions between oxygen ions will destabilize the dangling-BP-type structure in the case of a high oxygen concentration. To be more specific, the lowest-energy structures of $P_{8}O_{1}$ and $P_{6}O_{1}$ are of the dangling-BP type (Figure 1). The 2D structure of $P_{4}O_{1}$ also belongs to the dangling-BP type, which was first proposed by Wang et al. $^{[12a]}$ (see Figure 1). However, surprisingly and interestingly, we found that $P_{4}O_{1}$ has another special one-dimensional (1D) tubular structure (see Figure S1 in the Supporting Information). This 1D structure has lower total energy (about 14 meV/atom) than its 2D configuration. The 1D $P_{4}O_{1}$ with a $3.3\ \mathring{A}$ diameter may be the smallest nanotube, since the smallest experimentally observed carbon nanotube has a diameter of $4\ \mathring{A}.^{[16]}$ $P_{2}O_{1}$ contains not only the dangling P=O motifs but also the P-O-P motifs (hereafter referred to as $P_{2}O_{1}$-I; see Figure 1). Its total energy is lower than that of the previously proposed $P_{2}O_{1}$ structure (referred as $P_{2}O_{1}$-IV; see Figure S4) $^{[12a]}$ by about 174 meV/atom despite of the fact that the $P_{2}O_{1}$-I structure is thinner than the previous $P_{2}O_{1}$ structure by about $1.0\ \mathring{A}$. $P_{2}O_{1}$-I is unusual and complicated. There exist four-membered rings and eight-membered rings formed by phosphorus atoms. Since its framework is completely different from that of phosphorene, it is almost impossible to build it manually, thus indicating that our global optimization approach is powerful. The most stable structures of $P_{4}O_{4}$ and $P_{2}O_{3}$ are shown in Figure 2 a and 5b, respectively.

![](./images/813491590864568321_2.jpg)

Figure 1. The lowest-energy structures of $P_{8}O_{1}$, $P_{6}O_{1}$, $P_{4}O_{1}$, and $P_{2}O_{1}$ with a thickness less than $3.2\ \mathring{A}$. For $P_{8}O_{1}$, $P_{6}O_{1}$, and $P_{4}O_{1}$, they are still based on the phosphorene structure. However, the lowest-energy structure of $P_{2}O_{1}$ (i.e., $P_{2}O_{1}$-I) is no longer based on the phosphorene structure and has a P-O-P motif besides the P=O motifs.

![](./images/813491590864568321_3.jpg)

Figure 2. a) The lowest-energy structure of $P_{4}O_{4}$ with a thickness less than $3.2\ \mathring{A}$. The $P_{1}$ and $P_{2}$ atoms are highlighted by a black ellipse. b) Another structure of $P_{4}O_{4}$. $P_{4}O_{4}$-II has a similar topology to that of $P_{4}O_{4}$-I, but no twisting of $P_{6}O_{4}$ rings. $P_{4}O_{4}$-II has a higher energy by 11 meV/atom than $P_{4}O_{4}$-I. The distance "d" is the thickness of the 2D structures.

We can find that both have the bridge-type structure without P=O motifs. Previously, it was suggested that the band gap of phosphorus oxides increases monotonously with the oxygen concentration. $^{[12b,14]}$ In this study, we found that this hypothesis is not necessarily true: The band gap of our $P_{2}O_{1}$ structure is about 2.85 eV, which is larger than that (2.24 eV) of the stable structure of $P_{4}O_{4}$ (i.e. $P_{4}O_{4}$-I). This result suggests that 2D phosphorus oxides have rich structural and electronic properties. As expected, the average binding energy per phosphorus atom increases with the oxygen concentration (see Figure S2).

The lowest-energy structure of $P_{4}O_{4}$ (i.e., $P_{4}O_{4}$-I) up to a thickness of $3.2\ \mathring{A}$ only contains P-O-P bridge motifs (Figure 2a). Six phosphorus atoms and four oxygen atoms form a ring. There are two P-P dimers in a primitive cell. Each oxygen atom is twofold coordinated, and each phosphorus atom bonds with one phosphorus atom and two oxygen atoms. The phosphorus atom is $sp^{3}$-hybridized with an electron lone pair, whereas there are two electron lone pairs for each $sp^{3}$-hybridized oxygen atom. This chemical bonding analysis suggests that $P_{4}O_{4}$-I is a semiconductor. The calculated band structure indeed confirms the semiconducting nature. $P_{4}O_{4}$-I has a direct band gap of 2.24 eV at the $\Gamma$ point (Figure 3a). The valence-band maximum (VBM) is located at the $\Gamma$ point because of the interaction between the P-P $\sigma$-bonding states (see the Supporting Information for a detailed analysis).

![](./images/813491590864568321_4.jpg)

Figure 3. a) Band structure of $P_{4}O_{4}$-I from the HSE06 calculation.
There is a direct band gap of about 2.24 eV at the $\Gamma$ point. b) Band
structure of $P_{4}O_{4}$-II from the HSE06 calculation. c) VBM wave function
of $P_{4}O_{4}$-I, to which the P-P bonding state contributes. d) CBM wave
function of $P_{4}O_{4}$-I, which is mainly distributed around $P_{1}$ and $P_{2}$
atoms. e) VBM wave function of $P_{4}O_{4}$-II. As for $P_{4}O_{4}$-I, there is
a contribution from the P-P bonding state. f) CBM wave function of
$P_{4}O_{4}$-II. Unlike for $P_{4}O_{4}$-I, the main contributions are from $\pi$ bonds of
the P-P dimer.

Moreover, we found that the band dispersion near the $\Gamma$ point
is large, thus indicating a high mobility. The electron effective
mass with the local density approximation (LDA) functional
was computed to be $0.58\ m_{0}$, which is even smaller than that
$(0.68\ m_{0})$ of phosphorene. The optical absorption spectrum
calculated with the HSE functional is plotted in Figure 4b.
From it, we can see an absorption starting from 2.24 eV, thus
indicating that the dipole transition between the conduction-
band minimum (CBM) and VBM is allowed. The dipole
transition between the band-edge states can be understood in
terms of point-group theory: The point group of $P_{4}O_{4}$-I is $C_{2h}$,
which has four one-dimensional irreducible representations.
We found that the wave functions of CBM and VBM belong
to odd $A_{u}$ and even $B_{g}$ representations, respectively.

As we mentioned above, the band gap of $P_{4}O_{4}$-I is even
smaller than that of $P_{2}O_{1}$-I. To understand this unusual
phenomenon, we plotted wave functions of the VBM and
CBM states of $P_{4}O_{4}$-I (Figure 3c,d). We found that mainly the
P-P $\sigma$-bonding states contribute to the VBM state, whereas
for the CBM state, the wave function is mainly distributed
between one phosphorus atom and its next-nearest neighbor
(namely, atoms $P_{1}$ and $P_{2}$) in a ring containing six phosphorus
atoms. The interaction between atoms $P_{1}$ and $P_{2}$ is very
important to the low energy of the CBM state and is thus
responsible for the small band gap of $P_{4}O_{4}$-I. The uncommon
long-range P-P interaction is due to the twisting of $P_{6}O_{4}$ rings
in $P_{4}O_{4}$-I (for more detailed discussions, see the Supporting
Information).

Our above results indicate that $P_{4}O_{4}$-I may be appropriate
for photoelectrochemical (PEC) water-splitting applica-
tions. $^{[17]}$ In a good material for photochemical water splitting,
the positions of band edges should be suitable for solar-driven
water splitting. $^{[18]}$ The estimated band-edge positions with
respect to the vacuum level are shown in Figure 4a. The
hydrogen-evolution potential and oxygen-evolution potential
are marked with a black dot and a green dot, respectively. It
can be seen that the CBM of $P_{4}O_{4}$-I is higher than the
hydrogen-evolution potential by about 0.67 eV, and the VBM
of $P_{4}O_{4}$-I is below the oxygen-evolution potential by about
0.37 eV. These band-edge positions are suitable for PEC
water splitting. We investigate the interaction between water
and $P_{4}O_{4}$-I with a first-principles molecular-dynamics (MD)
simulation (see Figure S3). Our results show that $P_{4}O_{4}$-I can
be stable in water at room temperature. Furthermore, the
adsorption energies of a water molecule on $P_{4}O_{4}$-I and
phosphorene were found to be -256 and -283 meV, respec-
tively, which suggests that $P_{4}O_{4}$-I is more stable than
phosphorene in water. $^{[19]}$

![](./images/813491590864568321_5.jpg)

Figure 4. a) $P_{4}O_{4}$-I and $P_{4}O_{4}$-II band edges, calculated with the HSE06
functional and referenced to the vacuum level. The green and black
dots indicate the oxygen- and hydrogen-evolution potential at pH=0,
respectively. b) Imaginary part of the dielectric function of $P_{4}O_{4}$-I from
the HSE06 calculation. It suggests that the optical absorption
increases rapidly above the band gap.

Three-dimensional ferroelectric materials have been
widely explored both experimentally and theoretically. $^{[20]}$ In
two dimensions, the depolarizing field was believed to
suppress the ferroelectric dipoles perpendicular to the film
surface, thus leading to the disappearance of ferroelectricity
for thicknesses less than a certain value. $^{[21]}$ For this reason,
only a few studies have focused on 2D ferroelectric materials
in the past. $^{[20b,22]}$ Recently, the 1T monolayer $MoS_{2}$ and 2D
honeycomb binary compounds were predicted to be 2D
ferroelectric materials. $^{[22a]}$ However, their ferroelectric prop-
erties still await experimental confirmation. Therefore, the

discovery of new 2D ferroelectric materials will not only help us to understand a new physical mechanism for 2D ferroelec- tricity, but also accelerate the development of applications of 2D ferroelectric materials.

From our PSO simulation, we found two kinds of ferro- electric structures for $P_{2}O_{3}$ (namely, $P_{2}O_{3}$-I and $P_{2}O_{3}$-II; Figure 5a,b). $P_{2}O_{3}$-I is the lowest-energy structure with a thickness less than $1.4$ Å. The phosphorus atoms form

![](./images/813491590864568321_6.jpg)

Figure 5. a) Top and side views of $P_{2}O_{3}$-I, which is the lowest-energy $P_{2}O_{3}$ structure with a thickness less than $1.4$ Å. Each phosphorus atom is surrounded by three oxygen atoms. $P_{2}O_{3}$-I is ferroelectric with an out-of-plane electric polarization. b) Top and side views of $P_{2}O_{3}$-II, which is the lowest-energy $P_{2}O_{3}$ with a thickness less than $3.2$ Å. $P_{2}O_{3}$- II is ferroelectric with an in-plane electric polarization. c) Top and side views of the paraelectric $P_{2}O_{3}$ structure (i.e., $P_{2}O_{3}$-III). Oxygen atoms are inversion centers.

a honeycomb lattice, and each phosphorus atom is sur- rounded by three oxygen atoms. Thus, there are only P-O $\sigma$ bonds, which results in a large band gap (about 5.79 eV). All phosphorus atoms are located in the top plane, and all oxygen atoms are located in the bottom plane. Hence, $P_{2}O_{3}$-I has a non-zero electric polarization perpendicular to the lateral plane. The presence of a perpendicular ferroelectric polar- ization in $P_{2}O_{3}$-I can be explained as follows: Although the pure electrostatic interaction between the $P^{3+}$ ion and $O^{2-}$ ion favors a flat structure, flat $P_{2}O_{3}$ is unstable owing to the presence of the lone-pair electrons of the $P^{3+}$ ion. As shown in Figure 6, the interaction between P $3p_{z}$ and 3s orbitals in flat $P_{2}O_{3}$ is forbidden by symmetry. In contrast, P $3p_{z}$ orbitals can mix with P 3s orbitals to lower the energy level in $P_{2}O_{3}$-I. Since this level will be occupied by the lone-pair electrons, the total energy becomes lower than that of flat $P_{2}O_{3}$. This behavior is rather similar to the mechanism of the buckling of the $NH_{3}$ molecule. The ferroelectric mechanism in $P_{2}O_{3}$-I is different from that in hexagonal ABC hyperferroelectrics, $^{[23]}$ in which small effective charges and large dielectric constants play a role. According to Garrity et al., $^{[23]}$ the term hyper ferroelectrics refers to a class of proper ferroelectrics which polarize even when the depolarization field is unscreened. In this sense, $P_{2}O_{3}$-I is the thinnest hyperferroelectric material as the result of a new lone-pair mechanism.

$P_{2}O_{3}$-II is the lowest-energy structure of $P_{2}O_{3}$ with a thickness less than $3.2$ Å. Its topology is similar to that of $P_{2}O_{3}$-I. However, unlike in $P_{2}O_{3}$-I, the phosphorus atoms are no longer in the same plane, and neither are the oxygen atoms, thus leading to zero polarization perpendicular to the lateral plane. $P_{2}O_{3}$-II does, however, have a non-zero in-plane polarization due to the collective oxygen displacements along the $y$ axis (see Figure 5b). The total energy of $P_{2}O_{3}$-II is lower than that of $P_{2}O_{3}$-I by about 34 meV/atom. However, $P_{2}O_{3}$-II has a larger thickness than $P_{2}O_{3}$-I (1.46 vs. $0.80$ Å). To estimate the switching barrier and magnitude of electric polarization, we considered a paraelectric phase of $P_{2}O_{3}$ ($P_{2}O_{3}$-III in Figure 5c) in which the oxygen plane is sand- wiched between the two phosphorus planes. The paraelectric phase $P_{2}O_{3}$-III is a semiconductor with a LDA band gap of 3.41 eV. The energy barrier between ferroelectric $P_{2}O_{3}$-I ($P_{2}O_{3}$-II) and the paraelectric phase is about 75 meV/atom (109 meV/atom). Thus, it is possible to switch the ferroelectric phase to the paraelectric phase by applying an external electric field. The electric polarization of $P_{2}O_{3}$-I and $P_{2}O_{3}$-II was found to be $2.4 \times 10^{-12}$ and $1.2 \times 10^{-12} Cm^{-}$, respectively.

![](./images/813491590864568321_7.jpg)

Figure 6. Schematic diagrams of the highest occupied molecule orbi- tals of $NH_{3}$ and $P_{2}O_{3}$. For the flat configuration, the $p_{z}$ orbitals of phosphorus atoms can not hybridize with the s orbitals, whereas for the buckled configuration, the $p_{z}$ orbitals can mix with s orbitals to lower the total energy.

In the case of $P_{2}O_{3}$-I, the electric polarization can be either along the $z$ or $-z$ direction. For $P_{2}O_{3}$-II, there are six possible ferroelectric states with in-plane electric polariza- tions because of the sixfold symmetry of the paraelectric state. Therefore, there are eight different ferroelectric states in total for 2D $P_{2}O_{3}$. With an electric field, we could change the direction of electric polarization, and a nanoscale multiple- state (eight-state) memory device could possibly be created (Figure 7).

These 2D phosphorus oxides are thermally and kinetically stable (see Figure S6). We propose two possible ways to synthesize these materials. One way to obtain $P_{4}O_{4}$ and $P_{2}O_{3}$ is to partially oxidize the phosphorenene with ozone or oxygen plasma with a controlled oxygen concentration. Another way is to reduce the phosphorus oxides with a high oxygen concentration by chemical reduction. Such a method was successfully adopted to synthesize partially oxidized gra- phene. $^{[24]}$

In conclusion, we systematically predicted the lowest- energy structures of 2D $P_{8}O_{1}$, $P_{6}O_{1}$, $P_{4}O_{1}$, $P_{2}O_{1}$, $P_{4}O_{4}$, and

![](./images/813491590864568321_8.jpg)

Figure 7. Schematic illustration of the concept of multiple-state memory based on 2D $P_2O_3$. In total, there are eight possible ferroelectric states in 2D $P_2O_3$.

$P_2O_3$ by a global optimization method. We found that the features of stable structures vary with the oxygen concentration. If the oxygen concentration is low, 2D $P_xO_y$ structures are based on phosphorene with dangling P═O motifs, as reported by Ziletti et al. $^{[9a]}$ With an increase in the oxygen concentration, 2D $P_xO_y$ structures will most likely exhibit P–O–P motifs. We further showed that 2D $P_xO_y$ may have unique properties for functional materials. $P_4O_4$-I may be a good candidate for PEC water splitting, since it has an appropriate band gap, good optical absorption, and high stability in water. Both $P_2O_3$-I and $P_2O_3$-II are 2D ferroelectrics. In particular, $P_2O_3$-I may be the thinnest hyper-ferroelectric material as a result of a new mechanism. We propose that 2D $P_2O_3$ could be used in nanoscale multiple-state memory devices in the future.

## Acknowledgements

This research was supported by the NSFC, the Special Funds for Major State Basic Research, the Research Program of Shanghai Municipality and the MOE, the Program for Professor of Special Appointment (Eastern Scholar), the Qing Nian Ba Jian Program, and Fok Ying Tung Education Foundation.

Keywords: ab initio calculations · ferroelectricity · phosphorus oxides · photochemistry · two-dimensional materials

How to cite: Angew. Chem. Int. Ed. 2016, 55, 8575-8580
Angew. Chem. 2016, 128, 8717-8722

[1] a) A. K. Geim, K. S. Novoselov, Nat. Mater. 2007, 6, 183-191;
b) K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I. V. Grigorieva, S. V. Dubonos, A. A. Firsov, Nature 2005, 438, 197-200; c) K. S. Novoselov, E. McCann, S. V. Morozov, V. I. Fal'ko, M. I. Katsnelson, U. Zeitler, D. Jiang, F. Schedin, A. K. Geim, Nat. Phys. 2006, 2, 177-180; d) Y. Zhang, Y. W. Tan, H. L. Stormer, P. Kim, Nature 2005, 438, 201-204;
e) B. Radisavljevic, A. Radenovic, J. Brivio, V. Giacometti, A. Kis, Nat. Nanotechnol. 2011, 6, 147-150; f) Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, M. S. Strano, Nat. Nanotechnol. 2012, 7, 699-712; g) K. F. Mak, C. Lee, J. Hone, J. Shan, T. F. Heinz, Phys. Rev. Lett. 2010, 105, 136805.

[2] a) M. S. Fuhrer, J. Hone, Nat. Nanotechnol. 2013, 8, 146-147;
b) H. Fang, S. Chuang, T. C. Chang, K. Takei, T. Takahashi, A. Javey, Nano Lett. 2012, 12, 3788-3792.

[3] V. Tran, R. Sokolski, Y. Liang, L. Yang, Phys. Rev. B 2014, 89, 235319.

[4] a) L. Li, Y. Yu, G. J. Ye, O. Ge, X. Ou, H. Wu, D. Feng, X. H. Chen, Y. Zhang, Nat. Nanotechnol. 2014, 9, 372-377; b) H. Liu, A. T. Neal, Z. Zhu, Z. Luo, X. F. Xu, D. Tománek, P. D. Ye, ACS Nano 2014, 8, 4033-4041; c) F. Xia, H. Wang, Y. Jia, Nat. Commun. 2014, 5, 4458; d) J. Qiao, X. Kong, Z. X. Hu, F. Yang, W. Ji, Nat. Commun. 2014, 5, 4475; e) W. Hu, J. Yang, J. Phys. Chem. C 2015, 119, 20474-20480; f) R. Zhang, B. Li, J. Yang, J. Phys. Chem. C 2015, 119, 2871-2878.

[5] a) S. L. Zhang, M. Q. Xie, F. Y. Li, Z. Yan, Y. F. Li, E. J. Kan, W. Liu, Z. F. Chen, H. B. Zeng, Angew. Chem. Int. Ed. 2016, 55, 1666-1669; Angew. Chem. 2016, 128, 1698-1701; b) S. L. Zhang, Z. Yan, Y. F. Li, Z. F. Chen, H. B. Zeng, Angew. Chem. Int. Ed. 2015, 54, 3112-3115; Angew. Chem. 2015, 127, 3155-3158.

[6] M. Engel, M. Steiner, P. Avouris, Nano Lett. 2014, 14, 6414-6417.

[7] X. Wang, A. M. Jones, K. L. Seyler, V. Tran, Y. Jia, H. Zhao, H. Wang, L. Yang, X. Xu, F. Xia, Nat. Nanotechnol. 2015, 10, 517-521.

[8] a) A. S. Rodin, A. Carvalho, A. H. Castro Neto, Phys. Rev. Lett. 2014, 112, 176801; b) R. Fei, L. Yang, Nano Lett. 2014, 14, 2884-2889.

[9] a) A. Ziletti, A. Carvalho, D. K. Campbell, D. F. Coker, A. H. Castro Neto, Phys. Rev. Lett. 2015, 114, 046801; b) J. Kang, J. D. Wood, S. A. Wells, J.-H. Lee, X. Liu, K.-S. Chen, M. C. Hersam, ACS Nano 2015, 9, 3596-3604; c) G. X. Wang, W. J. Slough, R. Pandey, S. P. Karna, ArXiv: 2015, 1508, 07461; d) D. Hanlon, C. Backes, E. Doherty, C. S. Cucinotta, N. C. Berner, C. Boland, K. Lee, A. Harvey, P. Lynch, Z. Gholamvand, S. Zhang, K. Wang, G. Moynihan, A. Pokle, O. M. Ramasse, N. McEvoy, W. J. Blau, J. Wang, G. Abellan, F. Hauke, A. Hirsch, S. Sanvito, D. D. O'Regan, G. S. Duesberg, V. Nicolosi, J. N. Coleman, Nat. Commun. 2015, 6, 8563.

[10] a) J. Dai, X. C. Zeng, RSC Adv. 2014, 4, 48017-48021; b) Y. Q. Cai, Q. Q. Ke, G. Zhang, Y. W. Zhang, J. Phys. Chem. C 2015, 119, 3102-3110.

[11] A. Favron, E. Gaufres, F. Fossard, A.-L. Phaneuf-L'Heureux, N. Y.-W. Tang, P. L. Lévesque, A. Loiseau, R. Leonelli, S. Francoeur, R. Martel, Nat. Mater. 2015, 14, 826-832.

[12] a) G. Wang, R. Pandey, S. P. Karna, Nanoscale 2015, 7, 524-531;
b) A. Ziletti, A. Carvalho, P. E. Trevisanutto, D. K. Campbell, D. F. Coker, A. H. Castro Neto, Phys. Rev. B 2015, 91, 085407.

[13] a) G. Eda, G. Fanchini, M. Chhowalla, Nat. Nanotechnol. 2008, 3, 270-274; b) H. A. Becerril, J. Mao, Z. F. Liu, R. M. Stoltenberg, Z. N. Bao, Y. S. Chen, ACS Nano 2015, 2, 463-470.

[14] J. P. Lu, J. Wu, A. Carvalho, A. Ziletti, H. W. Liu, J. Y. Tan, Y. F. Chen, A. H. Castro Neto, B. Ozyilmaz, C. H. Sow, ACS Nano 2015, 9, 10411-10421.

[15] a) W. Luo, Y. Ma, X. Gong, H. Xiang, J. Am. Chem. Soc. 2014, 136, 15992-15997; b) W. Luo, H. Xiang, Nano Lett. 2015, 15, 3230-3235; c) X. Luo, J. Yang, H. Liu, X. Wu, Y. Wang, Y. Ma, S. H. Wei, X. Gong, H. Xiang, J. Am. Chem. Soc. 2011, 133, 16285-16290; d) Y. Wang, J. Lv, L. Zhu, Y. Ma, Phys. Rev. B 2010, 82, 094116.

[16] Z. M. Li, Z. K. Tang, H. J. Liu, N. Wang, C. T. Chan, R. Saito, S. Okada, G. D. Li, J. S. Chen, N. Nagasawa, S. Tsuda, Phys. Rev. Lett. 2001, 87, 127401.

[17] M. Ni, M. K. H. Leung, D. Y. C. Leung, K. Sumathy, Renewable Sustainable Energy Rev. 2007, 11, 401-425.

[18] H. R. Liu, J. H. Yang, Y. Y. Zhang, S. Chen, A. Walsh, H. Xiang, X. Gong, S. H. Wei, Phys. Chem. Chem. Phys. 2013, 15, 1778-1781.

Angew. Chem. 2016, 128, 8717-8722
© 2016 Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim
www.angewandte.de

[19] A. Castellanos-Gomez, L. Vicarelli, E. Prada, J. Island, K. L. Narasimha-Acharya, S. I. Blanter, D. J. Groenendijk, M. Buscema, G. A. Steele, J. V. Alvarez, H. W. Zandbergen, J. J. Palacios, H. S. J. van der Zant, 2D Mater. 2014, 1, 025001.

[20] a) M. Kenzelmann, A. B. Harris, S. Jonas, C. Broholm, J. Schefer, S. B. Kim, C. L. Zhang, S. W. Cheong, O. P. Vajk, J. W. Lynn, Phys. Rev. Lett. 2005, 95, 087206; b) H. J. Xiang, S. H. Wei, M. H. Whangbo, J. L. Da Silva, Phys. Rev. Lett. 2008, 101, 037209; c) T. C. S. Lee, Y. J. Choi, V. Kiryukhin, S. W. Cheong, Science 2009, 324, 63-66.

[21] a) M. Trieloff, E. K. Jessberger, I. Herrwerth, J. Hopp, C. Fieni, M. Ghelis, M. Bourot-Denise, P. Pellas, Nature 2003, 422, 502-506; b) A. V. Bune, V. M. Fridkin, S. Ducharme, L. M. Blinov, S. P. Palto, A. V. Sorokin, S. G. Yudin, A. Zlatkin, Nature 1998, 391, 874-877; c) D. D. Fong, G. B. Stephenson, S. K. Streiffer, J. A. Eastman, O. Auciello, P. H. Fuoss, C. Thompson, Science 2004, 304, 1650-1653.

[22] a) S. N. Shirodkar, U. V. Waghmare, Phys. Rev. Lett. 2014, 112, 157601; b) D. Di Sante, A. Stroppa, P. Barone, M.-H. Whangbo, S. Picozzi, Phys. Rev. B 2015, 91, 161401.

[23] K. F. Garrity, K. M. Rabe, D. Vanderbilt, Phys. Rev. Lett. 2014, 112, 127601.

[24] S. Park, J. An, R. Piner, I. Jung, D. Yang, A. Velamakanni, S. Nguyen, R. Ruoff, Chem. Mater. 2008, 20, 6592-6594.

Received: March 6, 2016
Revised: April 15, 2016
