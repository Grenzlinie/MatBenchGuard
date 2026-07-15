# Theoretical design of a strain-controlled nanoporous CN membrane for helium separation

Yong-Chao Rao, Zhao-Qin Chu, Xiao Gu, Xiang-Mei Duan*

Department of Physics, Faculty of Science, Ningbo University, Ningbo-315211, P.R. China

---

## Abstract
Designing an efficient membrane for He purification is quite crucial in scientific and industrial applications. Ultrathin membranes with intrinsic pores are highly desirable for gas purification because of their controllable aperture and homogeneous hole distribution. Based on the first-principles density function theory and molecular dynamics simulations, we demonstrate that the compressively strained graphitic carbon nitride (CN) can effectively purify He from Ne and Ar. Under a $-6\%$ strain, the CN monolayer with a suitable pore size presents an easily surmountable barrier for He (0.11 eV) but formidable for Ne (0.51 eV) and Ar (2.45 eV) passing through the membrane, and it exhibits exceptionally high selectivity of $5.17 \times 10^{6}$ for He/Ne and $1.89 \times 10^{39}$ for He/Ar, as well as excellent He permeance of $1.94 \times 10^{7}$ GPU at room temperature, superior to those of porous graphene and $\text{C}_{2}\text{N}$ membrane. Our results confirm that strain-tuned CN membrane could be potentially utilized for He separating from other noble gases.

**Keywords:** CN membrane; Helium separation; Selectivity and permeance; First-principles calculations; Molecular dynamics simulations

---

$^*$Corresponding author
Email address: duanxiangmei@nbu.edu.cn (Xiang-Mei Duan*)

---

Preprint submitted to Journal of ${\rm \LaTeX}$ Templates
November 28, 2018

### 1. Introduction

With various properties, such as lower density than air, incombustibility and low index of refraction, the lightest noble gas, helium, has been extensively applied in the fields of semiconductors, airships and solar telescopes.[1, 2] However, He immediately drifts up during the extraction from the natural gas, resulting in its irreversibly losing on earth. And the traditional physical methods of producing He, like cryogenic distillation or pressure–swing adsorption of natural gas, is hard to obtain high enough concentration to meet the commercial utilization of He.[3] Due to the low cost and easy operation, membrane separation technology has been increasingly used in gas separation and sewage purification.[4] The gas permeability are quite sensitive to the thickness of membrane materials.[5, 6, 7] Therefore, the ideal membrane should be as thin as possible to receive maximum flux, mechanically robust to prevent cracking, and with well–defined pore sizes to increase selectivity. It is highly desirable to design the efficient He separation membrane having atomic thickness and sub–nanometer pores.

The single atomic thickness makes two–dimensional (2D) materials ideal for gas separation compared to conventional membranes.[8, 9] For gas purification, the hole size of the material plays a dominated role in determining the selectivity and permeability. Although the introduction of vacancy defects on the pristine graphene, silicene and germanene ecane which are impermeable to gas molecules, could provide a suitable pore size for gas separation.[10, 11, 12] However, it remains difficulties in controlling the size and number of pores experimentally.[13] Excitingly, some 2D porous films with uniform sub–nanopores, such as graphitic carbon nitride ($\text{C}_3\text{N}_4$,[14] $\text{C}_2\text{N}$[8]) and stanene,[7] can act as natural molecular sieves and have great potential for future He purification. To meet the increasing demand of He, researchers are focusing on designing more efficient and accurate molecular sieves. Based on the characteristics that porous membranes are sensitive to mechanical strain, the multi–stage gas separation approach by strain–modulating pore size has attracted great interest.[15, 16, 17]

As one of the graphitic carbon nitride family, the experimentally prepared

porous CN has fascinated considerable attention owing to its potential applications in energy storage and catalysts.[18, 19, 20] CN possesses honeycomb-like structure similar to graphene but with six-membered carbon-nitride ring in units [see Fig. 1 (a)], which makes it a candidate for gas separation. As reported, the stability of CN was confirmed by calculating the phonon dispersion spectrum, and CN membrane could separate $H_2$ from mixed composition including $CO$, $N_2$ and $CH_4$.[21] To the best of our knowledge, research on the utilization of CN for efficient He purification is still lacking.

In this work, we propose that the CN sheet, under a biaxial compressive-strain of 6%, is a good candidate for He separation. The microscopic permeation processes of He, Ne and Ar are discussed in terms of minimum energy passway, energy profile, and electron density isosurface. In addition, the diffusion and separation capacity are judged from permeance and selectivity at room temperature.

## 2. Computational details

The first-principles density functional theory (DFT) calculations are performed to optimize the structure of the porous CN, describe the electron density isosurfaces for noble gas molecules interacting with the porous CN monolayer, and carry out the energy barrier of noble gases permeating through CN membrane by using the VASP package.[22] The perdew-Burke-Ernzerhof (PBE) functional[23] under the generalized gradient approximation (GGA) with van der Waals correction proposed by Grimme (DFT-D2)[24] is employed by the spin-unrestricted all-electron DFT calculations. The electron wave-functions are expanded by plane waves with cut-off energies of 500 eV, and the convergence criteria for electronic and ionic interactions during structure relaxation are set to be $10^{-4}$ eV and 0.01 eV, respectively. The Monkhorst-Pack meshes of $7 \times 7 \times 1$ are used in sampling the Brillouin zone for $2 \times 2$ supercells of CN, and a $20$ Å vacuum thickness is introduced to avoid interlayer interactions. For the transition state calculations, we have performed minimum energy path pro-


filing using the climbing image nudged elastic band (CI−NEB) method[25] as implemented in the VASP transition state tools.

At the various temperatures, the He permeance of porous CN monolayer are investigated using MD simulations in the NVT ensemble, where the tem- perature of the system is controlled by the Andersen thermostat method. A condensed−phase optimized molecular potential for atomistic simulation stud- ies (COMPASS) in the Material Studio software is used for describing the in- teratomic interaction.[26]

## 3. Results and discussion

### 3.1. Pore size and stability of CN nano−sheet

Figure 1(a) presents a top view of a fully relaxed $2 \times 2$ CN supercell. The C−C and C−N bond lengths are 1.51 and $1.34\ \text{\AA}$, respectively, and the optimized lattice parameter is $7.12\ \text{\AA}$, consistent with previous literature.[20] The hole size, with a diameter of $5.47\ \text{\AA}$, are illustrated by the dashed interior circle. The electron density isosurface plot, shown in Fig. 1(b), indicates that the pore size of CN monolayer is characterized by the effective diameter of the inscribed circle, $3.28\ \text{\AA}$, which is much larger than the kinetic diameters of He ($2.6\ \text{\AA}$) and a little bit larger than that of Ne molecules ($3.2\ \text{\AA}$).[27] Therefore, it offers the possibility to reduce the pore width in-between kinetic diameters of He and Ne molecules and makes CN sheet as an efficient He−isolating membrane. The biaxial compressive strain is defined as $\varepsilon = (\iota - \iota_0)/\iota_0 \times 100\%$ , where $\iota$ and $\iota_0$ are the strained and original lengths of the monolayer along one of strain direction (the sample is compressed in two distinct directions with the same strain), respectively.

We investigate the He separation performance in the absence/presence of compressive strain on CN monolayer. Under compressive strain, the structural stability of CN is a key issue. As presented in Fig. 1(c), CN can sustain a biaxial compressive strain up to $-24\%$, which means that the structure of the membrane is robust under a small compression. Then, we figure out the

cohesive energies of CN membrane under different strains. The cohesive energy is expressed by:[28]

$$
E_{\mathrm{coh}}=\left(n_{\mathrm{C}} E_{\mathrm{C}}+n_{\mathrm{N}} E_{\mathrm{N}}-E_{\mathrm{CN}}\right) /\left(n_{\mathrm{C}}+n_{\mathrm{N}}\right) \tag{1}
$$

Where $E_{\mathrm{C}}$, $E_{\mathrm{N}}$ and $E_{\mathrm{CN}}$ are the energy of single C atom, single N atom, total CN membrane, respectively; and $n_{\mathrm{C}}$, $n_{\mathrm{N}}$ are the total number of C and N atoms. Fig. 1(c) shows that $E_{\mathrm{coh}}$ decreases with the increasing strain, while $E_{\mathrm{coh}}$ under 6% compressive strain is 6.05 eV per atom, which is still much lower than that of silicene (3.17 eV per atom).[29] And the strain energy of the system ($E_{\mathrm{s}}$, the energy difference between strained and equilibrium states), which actually equals to $E_{\mathrm{s}}=-\left[E_{\mathrm{coh}}\left(\varepsilon_{i}\right)-E_{\mathrm{coh}}\left(\varepsilon_{0}\right)\right] \times\left(n_{\mathrm{C}}+n_{\mathrm{N}}\right)$, increases with strain monotonically until the strain reaches the critical value of $-24 \%$. Note that silicene can be successfully used as gas separation membrane,[30] therefore CN under moderate mechanical strain is stable enough for He separation.

### 3.2. Diffusion energy barrier of the noble molecule

Before exploring the transition state and energy barrier, we first optimize the energetically most stable state (SS) of gas molecules on the surface of CN monolayer. The atomic structures of He atom adsorbed on CN surface with and without strain are presented in Fig. 2. The interaction energy between a noble gas molecule and CN membrane is defined by:

$$
E_{\mathrm{int}}=E_{\mathrm{gas} / \mathrm{CN}}-E_{\mathrm{gas}}-E_{\mathrm{CN}} \tag{2}
$$

Where $E_{\mathrm{gas} / \mathrm{CN}}$, $E_{\mathrm{gas}}$ and $E_{\mathrm{CN}}$ represent the total enegy of gas/CN system, isolated gas molecule and pure CN monolayer, respectively. The interaction energy and adsorption height of the SS under different compressive strains are summarized in Table 1. The interaction energy and adsorption height are in the range of $-6.9$ to $-25.5$ meV and 1.05 to $2.61 \mathring{\mathrm{A}}$, respectively, indicating the gas molecules are all physically adsorbed on the CN monolayer via weak van der Waals interaction. The magnitude of adsorption energy is comparable to those of the noble gases adsorbed on $\mathrm{C}_{3} \mathrm{~N}_{4}$ ($-17$ to $-99$ meV) and $\mathrm{C}_{2} \mathrm{~N}$ sheet ($-60$

to −90 meV). The general trend is that as the compressive strain increases, the reduction in pore size would enhance the repulsion interaction between the gas molecules and the CN membrane, leading to an increase in molecular adsorption height. Specifically, Ar has the highest adsorption height, which is due to the relatively large kinetic diameter.

When the gas migrates from the most stable adsorption site to the CN film, due to the symmetry, the transition state (TS) should be which the gas molecules are at the center of the cavity and in the same plane as the film. The TS state is confirmed using the NEB approach. The energy barrier (Eᵦ) is defined as:

$$
E_{\mathrm{b}}=E_{\mathrm{TS}}-E_{\mathrm{SS}} \tag{3}
$$

Where $E_{\mathrm{TS}}$ and $E_{\mathrm{SS}}$ represents the energy between gas molecules and CN membrane at the TS and SS, respectively. The energy profiles and barriers of He, Ne and Ar passing through the pore under different compressive strain are shown in Fig. 3. The barrier for He, Ne and Ar passing through the pristine CN is 0.03, 0.18 and 1.13 eV, respectively. Clearly, the relatively low penetration barrier for both He and Ne make it impracticable to purify He via unstrained CN membrane. Fortunately, the energy barrier increases as the compressive strain is exerted. In particular, when the strain is reached to −6%, the barrier for He, Ne and Ar is further increased to 0.11, 0.51 and 2.45 eV, respectively. The unexpectedly lower penetration barrier for He is within the threshold barrier for gas penetration (0.50 eV),[31] while the values for the other two noble gases are lager than 0.50 eV, suggesting that the He separation performance of CN can be significantly improved by inducing a 6% compressive strain.

To deeply understand of the change of energy barrier when the molecules pass strain−modified CN film, we show the electron density isosurface of noble gases interacting with CN at TS under −6% strain. Intuitively, large electron density overlap would induce strong repulsion which hinder the movement of gas molecules through the pore. From Fig. 4(a), it can be seen that there is no overlap between the electron density of He and the CN, therefore He could easily move through the membrane. However, the electron density overlap increases

for Ne and Ar, as presented in Fig. 4(b) and (c), the Ar molecule and the porous CN sheet completely overlap in electron density, so the Ar gas molecules cannot pass through the film. The effective diameter of strained CN [shown in the inscribed circle of Fig. 4(a)] is now 2.99 Å, which is between the kinetic diameter of He and Ne. Hence the compressed membrane only allows He to penetrate.

The He separation efficiency of the porous CN membrane can be quantita- tively examined through the Arrhenius-equation.[32] The selectivity (S) for He over other two noble gas molecules is estimated by:

$$
S_{\mathrm{He} / \mathrm{gas}}=\frac{\gamma_{\mathrm{He}}}{\gamma_{\mathrm{gas}}}=\frac{A_{\mathrm{He}} exp(-E_{\mathrm{He}} / RT)}{A_{\mathrm{gas}} exp(-E_{\mathrm{gas}} / RT)} \tag{4}
$$

Where $\gamma$ is the diffusion rate, the diffusion prefactor, $A$, is set to $10^{11}\ s^{-1}$,[27] $R$ and $T$ are the Boltzmann constant and the absolute temperature, respectively. $E$ is the diffusion energy barrier. The temperature-dependent diffusion rates of noble gas molecules and He selectivity relative to Ne and Ar are depicted in Fig. 5(a) and (b), respectively. Generally, with the temperature increasing, the dif- fusion rate of the molecules increases, while the He selectivity of CN membrane relative to Ne and Ar decreases. The main reason is that, when the temperature rises, the kinetic energy of the inert gas molecule is greatly increased, make it possible to overcome the energy barriers and pass the CN film. Significantly, at a certain temperature, the enhanced compressive strain reduces down the He diffusion rate [Fig. 5(a)] but greatly increases the selectivity for He/Ne and He/Ar [Fig. 5(b)], which demonstrates the appropriate compressive strain can effectively accelerate the separation of He from Ne and Ar. As summarized in Table 2, at room temperature, the selectivity for He/Ne and He/Ar are about $5.17 \times 10^{6}$ and $1.89 \times 10^{39}$ by subjecting to a $-6\%$ strain, respectively. The values are much superior than that of other theoretical results and surely acceptable for the industrial application.[8, 30, 33]

### 3.3. He separation by MD simulations

Permeability is another critical criterion to characterize the separation performance of CN membrane. Based on MD simulations, we investigate the gas flow to estimate the permeability of CN membrane quantitatively at room temperature, which is defined as:[34]

$$
F = \frac{\nu}{S \times t \times \Delta P} \tag{5}
$$

Where $\nu$ and $S$ represent the moles of gas molecules in the permeate side and the area of CN membrane, $t$ is the time duration, and the pressure drop $(\Delta P)$ is set to 1 bar across the pore.

As shown in the Fig. 6, the $4 \times 4$ supercell with a height of $90$ $\mathring{A}$ is divided into three parts of the same capacity. Periodic boundary conditions along the lateral directions are imposed to mimic the infinite film. At the beginning of each simulation, the gas reservoir, consisting of 40 He molecules, 40 Ne molecules and 40 Ar molecules, is initially located in the middle part of the supercell, that is, between the two monolayers of CN. The van der Waals interactions and Ewald electrostatic interactions are applied with a cutoff distance of $9.5$ $\mathring{A}$. Each simulation is carried out for a time period of $10$ $ns$ with a time-step of $1$ $fs$. In the process of simulations, due to the existing of difference in gas concentration among different spaces, the molecules are pushed cross the sheet into the vacuum region. After $10$ $ns$ simulation, the final configurations under $0\%$, $-3\%$ and $-6\%$ strain at room temperature are shown in Fig. 6. Some of Ne atoms pass through the pristine CN membrane [see Fig. 6(a)], and there are still several Ne atoms penetrate the membrane under a small strain of $-3\%$ [see Fig. 6(b)], which are consistent with the low penetration barriers in Fig. 3(a) and (b). However, under a $-6\%$ strain [see Fig. 6(c)], 27 He in 40 molecules pass through CN film to the vacuum space, without any Ne and Ar penetrating. The MD simulations further confirm that the strain-controlled nanoporous CN membrane can be applied in the purification of He from other noble gas molecules.

The calculated He permeance of porous CN monolayer under $-6\%$ strain with area of $28.48 \times 28.48$ $\mathrm{\AA}^2$ together with that of the previously proposed porous monolayer are summarized in Table 3. The strain-modified CN membrane exhibits a He permeability as high as $1.94 \times 10^7$ GPU at $300\ K$, which is almost twice that of $\mathrm{C_2N}$, and 270 times greater than that of the porous graphene (PG), far much higher than the industrially acceptable gas separation value of 20.[33]

### 4. Conclusions

Combining DFT-D2 calculations and classical MD simulation, we predict that strained porous CN monolayer can be used for He separation with high selectivity and permeability. The pristine CN is permeable for both He and Ne because of the lower barriers than threshold value. The energy barriers of gas molecules can be effectively modulated by biaxial compressive strain to the membrane. Subjecting the CN membrane to a $-6\%$ strain results in non-passability of Ne and exceptionally high selectivity for He/Ne (Ar) at $300\ K$. Meanwhile, the MD simulations further verify that the strained CN membrane exhibits a high He permeance of $1.94 \times 10^7$ GPU, which is superior to those of PG and $\mathrm{C_2N}$ sheets. Our results demonstrate that strain is an efficient strategy to tune the separation performance of low-dimensional materials and reveal that strain-controlled CN monolayer has great potential application in He separation.

### Acknowledgments

This research is supported by the Natural Science Foundation of China (grant No. 11574167), the New Century 151 Talents Project of Zhejiang Province and the KC Wong Magna Foundation in Ningbo University.

### Conflict of interest

The authors declare they have no conflict of interest

### References

### References

[1] K. H. Kaplan, Helium shortage hampers research and industry, Phys. Today 60 (2007) 31-32. doi:10.1063/1.2754594.

[2] A. Cho, Helium-3 shortage could put freeze on low-temperature research., Science 326 (2009) 778-779. doi:10.1126/science.326-778.

[3] N. K. Das, H. Chaudhuri, R. K. Bhandari, D. Ghose, P. Sen, B. Sinha, Purification of helium from natural gas by pressure swing adsorption, Curr. Sci. 95 (2008) 1684-1687.
URL http://www.jstor.org/stable/24105328

[4] P. Pandey, R. S. Chauhan, Membranes for gas separation, Prog. Polym. Sci. 26 (2001) 853-893. doi:org/10.1016/S0079-6700(01)00009-0.

[5] B. Díez, P. Cuadrado, A. MarcosFernández, P. Prádanos, A. Tena, L. Pala- cio, A. E. Lozano, A. Hernández, Helium recovery by membrane gas separa- tion using poly(o-acyloxyamide)s, Ind. Eng. Chem. Res. 53 (2014) 12809-12818. doi:10.1021/ie501649b.

[6] N. Kosinov, C. Auffret, V. G. P. Sripathi, C. Güçüyener, J. Gascon, F. Kapteijn, E. J. M. Hensen, Influence of support morphology on the detemplation and permeation of ZSM-5 and SSZ-13 zeolite membranes, Microporous Mesoporous Mater. 197 (2014) 268-277. doi:10.1016/j.micromeso.2014.06.022.

[7] F. Cao, C. Zhang, Y. Xiao, H. Huang, W. Zhang, D. Liu, C. Zhong, Q. Yang, Z. Yang, X. Lu, Helium recovery by a Cu-BTC metal-organic-framework membrane, Ind. Eng. Chem. Res. 51 (2012) 11274-11278. doi:10.1021/ie301445p.

[8] L. Zhu, Q. Xue, X. Li, T. Wu, Y. Jin, W. Xing, $C_2N$: an excellent two-dimensional monolayer membrane for He separation, J. Mater. Chem. A 3 (2015) 21351-21356. doi:10.1039/C5TA05700K.


[9] Y. Jiao, A. Du, S. C. Smith, Z. Zhu, S. Qiao, $H_2$ purification by functionalized graphdiyne-role of nitrogen doping, J. Mater. Chem. A 3 (2015) 6767-6771. doi:10.1039/C5TA01062D.

[10] J. S. Bunch, S. S. Verbridge, J. S. Alden, A. M. v. d. Zande, J. M. Parpia, H. G. Craighead, P. L. McEuen, Impermeable atomic membranes from graphene sheets, Nano Lett. 8 (2008) 2458-2462. doi:10.1021/n1801457b.

[11] A. W. Hauser, P. Schwerdtfeger, Nanoporous graphene membranes for efficient $^3$He/$^4$He separation, J. Phys. Chem. Lett. 3 (2) (2012) 209-213. doi:10.1021/jz201504k.

[12] L. Zhu, X. Chang, D. He, Q. Xue, X. Li, Y. Jin, H. Zheng, C. Ling, Defective germanenene as a high-efficiency helium separation membrane: a first-principles study, Nanotech. 28 (2017) 135703. doi:10.1088/1361-6528/aa5fae.

[13] S. P. Koenig, L. Wang, J. Pellegrino, J. S. Bunch, Selective molecular sieving through porous graphene, Nat. Nanotech. 7 (2012) 728-732. doi:10.1038/nnano.2012.162.

[14] F. Li, Y. Qu, M. Zhao, Efficient helium separation of graphitic carbon nitride membrane, Carbon 95 (2015) 51-57. doi:10.1016/j.carbon.2015.08.013.

[15] G. Gao, Y. Jiao, F. Ma, L. Kou, A. Du, Calculations of helium separation via uniform pores of stanene-based membranes, Beilstein J. Nanotech. 6 (2015) 2470-2476. doi:10.3762/bjnano.6.256.

[16] S. W. D. Silva, A. Du, W. Senadeera, Y. Gu, Strained graphitic carbon nitride for hydrogen purification, J. Membr. Sci. 528 (2017) 201-205. doi:10.1016/j.memsci.2017.01.034.

[17] L. Zhu, Y. Jin, Q. Xue, X. Li, H. Zheng, T. Wu, C. Ling, Theoretical study of a tunable and strain-controlled nanoporous graphenylene membrane for

multifunctional gas separation, J. Mater. Chem. A 4 (2016) 15015-15021.
doi:10.1039/C6TA04456E.

[18] J. Li, C. Cao, J. Hao, H. Qiu, Y. Xu, H. Zhu, Self-assembled one-dimensional carbon nitride architectures, Diamond Relat. Mater. 15 (2006) 1593-1600. doi:10.1016/j.diamond.2006.01.013.

[19] Y. D. Chen, S. Yu, W. H. Zhao, S. F. Li, X. M. Duan, A potential mate- rial for hydrogen storage: a Li decorated graphitic-CN monolayer, Phys. Chem. Chem. Phys. 20 (2018) 13473-13477. doi:10.1039/C8CP01145A.

[20] D. Liang, T. Jing, Y. Ma, J. Hao, G. Sun, M. Deng, The photocatalytic properties of $g-\mathrm{C}_{6}\mathrm{N}_{6}/g-\mathrm{C}_{3}\mathrm{N}_{4}$ heterostructure: a theoretical study, J. Phys. Chem. C 120 (2016) 24023-24029. doi:10.1021/acs.jpcc.6b08699.

[21] Z. Ma, X. Zhao, Q. Tang, Z. Zhen, Computational prediction of experimen- tally possible $g-\mathrm{C}_{3}\mathrm{N}_{3}$ monolayer as hydrogen purification membrane, Int. J. of Hydrogen Energy 39 (2014) 5037-5042. doi:10.1016/j.ijhydene. 2014.01.046.

[22] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comp. Mater. Sci. 6 (1996) 15-50. doi:10.1016/0927-0256(96)00008-0.

[23] J. P. Perdew, M. Ernzerhof, K. Burke, Rationale for mixing exact exchange with density functional approximations, J. Chem. Phys. 105 (1996) 9982-9985. doi:10.1063/1.472933.

[24] S. Grimme, Semiempirical GGA-type density functional constructed with a lon-range dispersion correction, J. Comp. Phys. 27 (2010) 1787-1799. doi:10.1002/jcc.20495.

[25] G. Henkelman, A climbing image nudged elastic band method for finding saddle points and minimum energy paths, J. Chem. Phys. 113 (2000) 9901-9904. doi:10.1063/1.1329672.

[26] H. Sun, Compass: An ab initio force-field optimized for condensed-phase applications-overview with details on alkane and benzene compounds, J. Phys. Chem. B 102 (1998) 7338-7364. doi:10.1021/jp980939v.

[27] S. Blankenburg, M. Bieri, R. Fasel, K. Müllen, C. A. Pignedoli, D. Passerone, Porous graphene as an atmospheric nanofilter, Small 6 (2010) 2266. doi:10.1002/smll.201001126.

[28] E. Perim, R. Paupitz, P. A. S. Autreto, D. S. Galvao, Inorganic grapheny- lene: a porous two-dimensional material with tunable band gap, J. Phys. Chem. C 118 (2014) 23670-23674. doi:10.1021/jp502119y.

[29] Y. Li, Y. Liao, Z. Chen, $Be_2C$ monolayer with quasi-planar hexacoordinate carbons: a global minimum structure, Angew. Chem. Int. Ed. 53 (2014) 7248-7252. doi:10.1002/anie.201403833.

[30] W. Hu, X. Wu, Z. Li, J. Yang, Helium separation via porous silicene based ultimate membrane, Nanoscale 5 (2013) 9062-9066. doi:10.1039/ C3NR02326E.

[31] J. Schrier, Helium separation using porous graphene membranes, J. Phys. Chem. Lett. 1 (2010) 2284-2287. doi:10.1021/jz100748x.

[32] D. Jiang, V. R. Cooper, S. Dai, Porous graphene as the ultimate mem- brane for gas separation, Nano Lett. 9 (2009) 4019-4024. doi:10.1021/ nl9021946.

[33] Z. Zhu, Permeance should be used to characterize the productivity of a polymeric gas separation membrane, J. Membr. Sci. 281 (2006) 754-756. doi:10.1016/j.memsci.2006.04.040.

[34] H. Du, J. Li, J. Zhang, G. Su, X. Li, Y. Zhao, Separation of hydrogen and nitrogen gases with porous graphene membrane, J. Phys. Chem. C 115 (2011) 23261-23266. doi:10.1021/jp206258u.

[35] A. M. Brockway, J. Schrier, Noble gas separation using PG-ESX ($X=1$,
2, 3) nanoporous two-dimensional polymers, J. Phys. Chem. C 117 (2013)
393-402. doi:10.1021/jp3101865.

![](./images/867746557213016554_1.jpg)

Figure 1: (a) Fully optimized $2 \times 2$ supercell of CN sheet. (b) Electron density isosurface of CN sheet with an isovalue of $0.015\ \text{e}/\text{\AA}^3$. The brown and blue balls represent the C and N atoms, respectively. (c) The stress (black triangles) and the cohesive energy (blue squares) as a function of strain. The long dashed lines between the symbols are guides to the eyes. The vertical short dashed line indicates the critical strain.

![](./images/867746557213016554_2.jpg)

Figure 2: The geometrical structures of He adsorbed on CN sheet in the absence and presence of strain. The yellow, brown and blue balls represent He, C and N atoms, respectively.

![](./images/867746557213016554_3.jpg)

Figure 3: Energy profiles for He, Ne and Ar penetrating through CN membrane under (a) 0%, (b) −3% and (c) −6% strain.

![](./images/867746557213016554_4.jpg)

Figure 4: Electron density isosurface for (a) He, (b) Ne and (c) Ar at transition state under $-6\%$ strain. The isovalue is $0.015\ \text{e}/\mathring{\text{A}}^3$.

![](./images/867746557213016554_5.jpg)

Figure 5: (a) Diffusion rate for the noble gas molecules, and (b) the selectivity of He relative to Ne and Ar molecules, as a function of temperature.

![](./images/867746557213016554_6.jpg)

Figure 6: Final configuration of the mixed gases permeating through the CN membrane at room temperature under a strain of (a) 0%, (b) $-3\%$ and (c) $-6\%$, respectively. Color code: yellow, He; pink, Ne; green, Ar.

<table>
<caption>Kinetic diameter D₀ (Å) of the gas molecules, the interaction energy $E_{\text{int}}$ (meV) and the adsorption height H₀ ( Å) of CN membrane with gas molecules.</caption>
<thead>
<tr>
<th></th>
<th>D₀</th>
<th>Strain</th>
<th>$E_{\text{int}}$</th>
<th>H₀</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">He</td>
<td rowspan="3">2.6</td>
<td>0%</td>
<td>−9.5</td>
<td>1.05</td>
</tr>
<tr>
<td>−3%</td>
<td>−18.0</td>
<td>1.26</td>
</tr>
<tr>
<td>−6%</td>
<td>−25.5</td>
<td>1.33</td>
</tr>
<tr>
<td rowspan="3">Ne</td>
<td rowspan="3">3.2</td>
<td>0%</td>
<td>−7.1</td>
<td>1.64</td>
</tr>
<tr>
<td>−3%</td>
<td>−17.6</td>
<td>1.81</td>
</tr>
<tr>
<td>−6%</td>
<td>−24.8</td>
<td>1.92</td>
</tr>
<tr>
<td rowspan="3">Ar</td>
<td rowspan="3">3.4</td>
<td>0%</td>
<td>−6.9</td>
<td>2.42</td>
</tr>
<tr>
<td>−3%</td>
<td>−16.3</td>
<td>2.56</td>
</tr>
<tr>
<td>−6%</td>
<td>−24.0</td>
<td>2.61</td>
</tr>
</tbody>
</table>

Table 2: The selectivity (S) of He toward Ne and Ar penetrating through CN membrane under $-6\%$ strain at room temperature. The results of previously studied membranes $\text{C}_2\text{N}$ and silicene are also included for comparison.

<table>
  <thead>
    <tr>
      <th></th>
      <th>CN</th>
      <th>$\text{C}_2\text{N}$ (Ref.[8])</th>
      <th>Silicene (Ref.[30])</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>S(He/Ne)</td>
      <td>$5.17 \times 10^6$</td>
      <td>$3 \times 10^3$</td>
      <td>$2 \times 10^3$</td>
    </tr>
    <tr>
      <td>S(He/Ar)</td>
      <td>$1.89 \times 10^{39}$</td>
      <td>$4 \times 10^{18}$</td>
      <td>$1 \times 10^{18}$</td>
    </tr>
  </tbody>
</table>

Table 3: The He permeance (GPU) of CN monolayer under $-6\%$ strain at 300 K, and the comparison with those of porous graphene (PG) and $\text{C}_2\text{N}$.
$[1\ \text{GPU}=3.35 \times 10^{-10}\ mol/(m^2 \cdot s \cdot Pa)]$

<table>
  <thead>
    <tr>
      <th></th>
      <th>CN</th>
      <th>$\text{C}_2\text{N}$ (Ref.[8])</th>
      <th>PG (Ref.[35])</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Permeance</td>
      <td>$1.94 \times 10^7$</td>
      <td>$1 \times 10^7$</td>
      <td>$7 \times 10^4$</td>
    </tr>
  </tbody>
</table>