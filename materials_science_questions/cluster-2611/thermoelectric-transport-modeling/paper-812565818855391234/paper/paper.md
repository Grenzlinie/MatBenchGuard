PAPER
View Article Online
View Journal

![](./images/812565818855391234_1.jpg)

Cite this: DOI: 10.1039/d0cp03226c

# First-principles investigation on the transport properties of quaternary CoFeRGa (R = Ti, V, Cr, Mn, Cu, and Nb) Heusler compounds†

Beibei Shi, $^{a}$ Jingyu Li, $^{b}$ Chi Zhang, $^{c}$ Wenya Zhai, $^{a}$ Shujuan Jiang, $^{a}$ Wenxuan Wang, $^{a}$ Dong Chen, $^{a}$ Yuli Yan, $^{a}$ Guangbiao Zhang $^{a}$ and Peng-Fei Liu $^{d}$

The Heusler alloys CoFeRGa (R = Ti, V, Cr, Mn, Cu, and Nb) have similar chemical compositions, but exhibit remarkably distinct electronic structures, magnetism and transport properties. These structures cover an extensive range of spin gapless semiconductors, half-metals, semiconductors and metals with either ferromagnetic, ferrimagnetic, antiferromagnetic, or nonmagnetic states. The Heusler alloys have three types of structures, namely, type-l, type-ll, and type-lll. By means of first-principles calculation combined with the Boltzmann equation within the consideration of spin-freedom, we explore the transport feature of the most stable structure (type-II). In addition, we provide evidence that all the considered materials are mechanically and dynamically stable, possessing high strength and toughness to resist compression and tensile strain. Moreover, the distinct electronic (metallic, insulating, and half-metallic) properties and magnetic behaviors originate mainly from a cooperative electron transfer and electronic structures have been verified by our calculation. Finally, we found that the tunable electronic structure with varied atomic numbers has significant influence on the spin-Seebeck effect. Correspondingly, the calculated spin-Seebeck coefficient of CoFeCrGa is $-60.29\ \mu V\ K^{-1}$ at 300 K, which is larger than that of other quaternary Heusler compounds. Our results provide a band-engineering platform to design Heusler structures with different electronic behaviors in isomorphic compounds, which provide the way for accelerating the pre-screening of materials to advance and for using the quaternary Heusler compounds for potential applications in spin caloritronic devices.

Received 16th June 2020,
Accepted 14th September 2020
DOI: 10.1039/d0cp03226c
rsc.li/pccp

## 1. Introduction
Thermoelectric (TE) energy conversion from waste heat sources is expected to play a crucial role in determining the economic, technological, and environmental urgency. $^{1}$ In recent years, the combination of TE and the complex interplay of different interactions with cross-coupling among orbital, spin, charge, and lattice degrees of freedom has driven growing prosperity in the study of obtaining superior TE properties. $^{2-5}$ The TE performance of a material critically depends on the Seebeck coefficient. In particular, the electronic structure of a material plays a pivotal role in dominantly controlling its transport performance. Previously, effective strategies and concepts on TE materials have been proposed to produce various novel electronic properties such as valence band convergence, resonance level, band engineering, modulation doping, and exploration for materials of different dimensions. $^{5-8}$ These strategies were a great success with regard to the artificial high-performance TE materials such as $SnTe,^{9} MgAgSb,^{10} PbTe,^{11} Cu_{2}Se,^{12}$ and BiCuSeO. $^{13}$ Accordingly, a common feature with a high Seebeck coefficient is that they have large bandgap and high degeneracy. Interestingly, since the increased atomic mass and weak correlation effects are associated with the widening of the bandwidth, the more the outermost electrons of the transition metal, the larger the band gap. In addition, the additional spin degree of freedom for manipulating the band structures of these Heusler materials have gained great interest in the fields of spin-Seebeck effects. $^{14-17}$ Therefore, it is essential to improve our understanding and manipulation capabilities of the electronic structure for Seebeck effects in a magnetic material.

$^{a}$ Institute for Computational Materials Science, School of Physics and Electronics, International Joint Research Laboratory of New Energy Materials and Devices of Henan Province, Henan University, Kaifeng 475004, China.
E-mail: gbzhang@vip.henu.edu.cn
$^{b}$ Key Laboratory of Materials Physics, Institute of Solid State Physics, Chinese Academy of Sciences, Hefei 230031, China
$^{c}$ College of Electrical Engineering, Henan University of Technology, Zhengzhou 450001, China
$^{d}$ Spallation Neutron Source Science Center, Institute of High Energy Physics, Chinese Academy of Sciences, Dongguan 523803, China. E-mail: pflu@ihep.ac.cn
† Electronic supplementary information (ESI) available. See DOI: 10.1039/ d0cp03226c

This journal is © the Owner Societies 2020
Phys. Chem. Chem. Phys.

The Heusler compounds have gained considerable research interest because of their diverse and intriguing electronic properties, which can be utilized in different applications such as spintronics, TE effects, magnetic shape memory effects, and superconductivity.¹⁸⁻²⁰ The Heusler structures are compatible with conventional semiconductors (CS) (zinc blende and rocksalt-type structures), and most of them have above-room-temperature ferromagnetism.²¹,²² A prominent example is that the quaternary Heusler alloy CoFeCrGa with the LiMgPdSn prototype has been predicted to exhibit spin gapless semiconductors (SGS) determined by first-principles calculations.²³ Besides, the Heusler alloy CoFeCrGa as a promising candidate in magnetotransport measurements exhibits a desirable SGS behavior below high Curie temperature. Compared with the ternary or quaternary Heusler half-metals (HMs), quaternary ones with a 1:1:1:1 stoichiometry can easily maintain the ordered phase,²⁴⁻²⁶ which results in a relatively strong half-metallicity and a high magnetoresistance ratio. Unfortunately, quaternary SGS CoFeCrGa has a bandgap of approximately 0.28 eV of the spin-down channel, which means that the half-metallicity is not stable and can be destroyed by applying strain. Therefore, it is necessary to search a new quaternary Heusler material with a large bandgap of the spin-down channel for promising applications in spin caloritronics. To design materials in the Heusler alloys, XX'YZ is realized by exchanging the elements X, X', Y, and Z or substituting them with other elements.²⁷ We have substituted Ti, V, Mn, Cu, and Nb for Cr in CoFeCrGa with the aim of improving its properties such as bandgap, Curie temperature, and spin polarization, as well as modulating its band structure. Despite similar chemical compositions, same electronic configurations, comparable electronic correlation, and accordant spin orbit coupling strength, the Heusler alloys CoFeRGa (R = Ti, V, Cr, Mn, Cu, and Nb) exhibit strikingly different electronic and magnetic properties. Besides, these stable compounds with large bandgaps, high spin polarizations, and high Curie temperatures can be desirable in spin caloritronics.

In this work, we use first-principles calculations based on density functional theory (DFT) to study the electronic and magnetic properties of the Heusler compounds CoFeRGa. Our results show that this series of stable bulks possess a wide range of magnetic phases, which includes SGS, HM, CS, and metals with either ferromagnetic (FM), ferrimagnetic (FiM), antiferromagnetic (AFM), or nonmagnetic (NM) configurations. Notably, the spin-Seebeck coefficient of CoFeCrGa is larger than that of other Heusler compounds. In particular, the spin-Seebeck coefficient of CoFeCrGa is −60.29 μV K⁻¹ at 300 K, which is mainly due to its novel SGS transmission behavior. Moreover, as HM and SGS materials are widely used in spintronics, we systematically investigated how structure, magnetism, and electronic structure affect the electrical transport properties of these Heusler materials.

## 2. Computational details

The structural optimization of a series of compounds, CoFeRGa, is performed using the Vienna *Ab initio* Simulation Package (VASP), which depends on the first-principles plane-wave pseudopotential method.²⁸⁻³¹ The calculations were carried out by employing the generalized gradient approximation (GGA)³² and Perdew–Burke–Ernzerhof (PBE) functional for exchange-correlation potential in spin-polarized and non-spin-polarized modes. The recommended potentials of all elements were used for both geometry optimization and internal coordinate relaxation. These calculations were performed with a 16 × 16 × 16 Γ-centered grid and a 500 eV plane-wave cutoff energy. The most stable structural type of all studied compounds was determined in terms of energy, which was conducive to the development of other properties. The self-consistent convergence conditions were set as follows: the total energy was 1 × 10⁻⁸ eV per atom and the force was less than 0.02 eV Å⁻¹. The elastic constants and Bader charge are obtained after self-consistent calculations. The phonon dispersion was calculated based on density functional perturbation theory (DFPT)³³ implemented in a phonopy code³⁴ with a 2 × 2 × 2 k-point mesh for a supercell of 128 atoms.

In this work, for the DFT implementation in the WIEN2k code,³⁵ the full-potential linearized augmented plane-wave (FP-LAPW) method was adopted to determine the equilibrium spin-dependent electronic structure including band structures and density of states (DOS) of the compounds CoFeRGa. The obtained results for the spin-dependent electronic structure and transport features were determined by considering the modified Becke–Johnson potential (mBJ),³⁶ due to the high efficiency and accuracy. The Muffin-tin radii $R_{\text{MT}}$ of the muffin tin separates into two parts: one is the average value inside the spheres and the other is the average volume in the interstitial region. In order to converge the energy, $R_{\text{MT}} \times K_{\text{MAX}} = 7.0$ was taken into account. The core electron orbitals were excluded and electron orbitals with energy −6.0 Ry were considered in the calculations. A k-point mesh of 20 × 20 × 20 is used for sampling of first irreducible Brillouin zone for all calculations.

For the spin-dependent transport calculations, the Boltzmann theory under the mBJ potential was employed within the BoltzTraP code³⁷ to obtain the Seebeck coefficient, electrical conductivity, and transmission spectra of CoFeRGa. These properties were determined by the variation in temperature and chemical potential. A larger k-point of 50 × 50 × 50 was used to obtain the convergence in the Brillouin zone because of the sensitivity of transport properties. In this spin-resolved transport calculations, computed electronic structures were used to investigate the transport properties as to provide the spin-resolved transmission ($T_{\sigma}(E)$), electrical conductivity ($\sigma_{\sigma}(T)$) within the constant relaxation time ($\tau$) and the Seebeck coefficient ($S_{\sigma}$). Then, the spin-Seebeck coefficient can be expressed as follows:³⁸

$$
S_{\text{s}} = \frac{\sigma_{\uparrow}S_{\uparrow} - \sigma_{\downarrow}S_{\downarrow}}{\sigma_{\uparrow} + \sigma_{\downarrow}} \tag{1}
$$

where "↑" is the spin-up channel and "↓" is the spin-down channel.

## 3. Results and discussions

### 3.1 Crystal structures and magnetism properties

The quaternary Heusler alloys CoFeRGa with XX'YZ composition crystallize in the Y-type structure(space group $F\overline{4}3m$). Their

primitive cell possesses four atomic sites with Wyckoff positions 4a (0, 0, 0), 4b (0.5, 0.5, 0.5), 4c (0.25, 0.25, 0.25) and 4d (0.75, 0.75, 0.75). According to the arrangement of four kinds of elements randomly occupying these four Wyckoff positions, there are three possible non-degenerate atomic configurations of the Heusler alloys CoFeRGa. The three resulting atomic arrangements are noted by type-I, type-II, and type-III. The primitive cells of crystal structures with the corresponding types are displayed in Fig. 1(a). In CoFeRGa compounds, there are five special band structures resulting in all kinds of magnetic orders (FM, FiM, and AFM) in magnetic semiconductors depending on their chemical composition and type-number. We provide the schematic diagram of five band structures, namely, CS, HM, nearly-HM, SGS, and metal in Fig. 1(b). HM and SGS materials are considered as important candidates in spintronic fields due to their 100% spin polarization at the Fermi level.

The total energy per unit cell and equilibrium lattice constants of the most stable structure among the three types of crystal structures of the spin-polarized state are listed in Table 1, and the results of other relatively unstable structures with higher energies in both spin-polarized and non-spin-polarized phases are displayed in Table S1 (ESI†). Obviously, with the exception of the CoFeTiGa compound, the total energy of the spin-polarized state is lower than that of the NM one in all the three types of structures of the Heusler alloys CoFeRGa. From Table 1, the type-I structure has the lowest value of energy for CoFeVGa, CoFeCrGa, CoFeMnGa, and CoFeNbGa, while CoFeCuGa is the most stable in type-II structure. CoFeCuGa belongs to type-II structure along the [111] direction as Ga-Cu-Fe-Co. Accordingly, the lattice constant of type-I structure decreases from 5.94 Å to 5.71 Å with R atoms from Nb to Mn attributed to the decrease in the atomic radius (Nb: 148 pm, Ti: 147 pm, V: 134 pm, Cr: 130 pm, and Mn: 127 pm). Abnormally, the lattice constant of CoFeCuGa is 5.79 Å on account of the type-II structure.

The Slater-Pauling rule is a prerequisite criterion for judging the HM and SGS materials within the Heusler alloys. The HM Heusler alloys have integer total magnetic moments following the Slater-Pauling rule:

$$
M_{\text{tot}} = Z - 2N_{\downarrow}, \tag{2}
$$

where $M_{\text{tot}}$ is the total magnetic moment, $Z$ is the number of the total valence electrons and $N_{\downarrow}$ is the number of spin-down valence electrons. In Table 1, we also describe the total magnetic moments per formula unit $M_{\text{tot}}$ ($\mu_{\text{B}}$ per f.u.) and atomic magnetic moments $M_{\text{a}}$ ($\mu_{\text{B}}$ per atom) of the quaternary Heusler alloys CoFeRGa in a stable configuration. The total magnetic moments for CoFeRGa are 0, 1.03, 1.97, 3.04, 3.59, and 1.06 $\mu_{\text{B}}$ per f.u., respectively. CoFeTiGa has zero values of all the total and atom-projected magnetic moments (in Table 1). The result indicated that CoFeTiGa is a non-spin-polarized material. CoFeVGa, CoFeCrGa, CoFeMnGa, and CoFeNbGa have approximately integer magnetic moments. It is evident that the HM or SGS gaps exist following the Slater-Pauling rule. The total magnetic moment of CoFeCuGa is 3.59 $\mu_{\text{B}}$ disobeying the Slater-Pauling rule. The local magnetic moments of Co and Fe in CoFeCuGa alloys show ferromagnetic coupling, whereas Fe atoms have large contribution contrary to Cu and Ga atoms. In the case of CoFeCrGa and CoFeMnGa alloys, Cr and Mn atoms have the largest magnetic moments value ($M_{\text{Cr}} = 1.81$ $\mu_{\text{B}}$ per atom and $M_{\text{Mn}} = 2.61$ $\mu_{\text{B}}$ per atom). Cr/Mn atoms are antiferromagnetically coupled with Fe atoms, and ferromagnetically with their nearest neighbor Co atoms. In addition, the

![](./images/812565818855391234_2.jpg)

Fig. 1 Crystal structures and density of states of CoFeRGa (R = Ti, V, Cr, Mn, Cu, and Nb). (a) A four-atom primitive cell of the quaternary Heusler alloys CoFeRGa with three types. (b) Schematic of the density of states of several kinds of materials (CS, HM, nearly-HM, SGS, and metal). Arrows indicate the spin-up ("↑") and spin-down ("↓") states.

<table><thead><tr><th rowspan="2">Alloys</th><th rowspan="2">Type</th><th rowspan="2">$E_{\text{tot}}$ (FM)</th><th rowspan="2">$a$</th><th colspan="4">Atomic magnetic moment</th><th rowspan="2">$M_{\text{tot}}$</th><th rowspan="2">Species</th></tr><tr><th>$M_{\text{Co}}$</th><th>$M_{\text{Fe}}$</th><th>$M_{\text{R}}$</th><th>$M_{\text{Ga}}$</th></tr></thead><tbody><tr><td>CoFeTiGa</td><td>I</td><td>$-111.65249$</td><td>5.81</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>CS</td></tr><tr><td>CoFeVGa</td><td>I</td><td>$-113.05718$</td><td>5.74</td><td>0.57</td><td>0.59</td><td>$-0.11$</td><td>$-0.02$</td><td>1.03</td><td>HM</td></tr><tr><td>CoFeCrGa</td><td>I</td><td>$-111.74014$</td><td>5.72</td><td>0.94</td><td>$-0.74$</td><td>1.81</td><td>$-0.04$</td><td>1.97</td><td>SGS</td></tr><tr><td>CoFeMnGa</td><td>I</td><td>$-110.62398$</td><td>5.71</td><td>0.72</td><td>$-0.24$</td><td>2.61</td><td>$-0.05$</td><td>3.04</td><td>Nearly-HM</td></tr><tr><td>CoFeCuGa</td><td>II</td><td>$-88.486647$</td><td>5.79</td><td>1.05</td><td>2.61</td><td>$-0.01$</td><td>$-0.06$</td><td>3.59</td><td>Metal</td></tr><tr><td>CoFeNbGa</td><td>I</td><td>$-117.98365$</td><td>5.94</td><td>0.57</td><td>0.62</td><td>$-0.11$</td><td>$-0.02$</td><td>1.06</td><td>HM</td></tr></tbody></table>

main contribution for the total magnetic moment in CoFeVGa and CoFeNbGa alloys comes from Co and Fe atoms, while V/Nb atoms carry a few of the magnetic moments aligned anti-parallel to those of Co and Fe atoms. For these five alloys, Ga atoms show negligible magnetic moments. The opposite signs indicate that the spin moments of Co and Cr/Mn are anti-parallel to that of Fe atoms in CoFeCrGa and CoFeMnGa alloys, and the spin moments of Co and Fe are anti-parallel to that of V/Nb atoms for CoFeVGa and CoFeNbGa alloys, resulting in the ferromagnetic configuration. Except for CoFeTiGa, other Heusler materials may show the behaviors of HM, nearly-HM, SGS, and metal, which could be utilized as a promising candidate for producing superior electronic and magnetic transport properties.

### 3.2 Elastic and phonon properties

To determine the intrinsic mechanical behavior of CoFeRGa, we applied DFPT³⁹ simulations to explore their elastic properties under applied strain. Elastic constant defines the abilities of materials that recover to their original shapes after applied stress. It bridges between the mechanical and dynamical behaviors to confirm the phase stability of the involved compounds. The cubic CoFeRGa have independent elastic constants $c_{11}$, $c_{12}$ and $c_{44}.^{40}$ Under the Voigt approximation,⁴¹ the Voigt shear modulus ($G_{\text{V}}$) and Voigt bulk modulus ($B_{\text{V}}$) are defined using the following formula:

$$
G_{\mathrm{V}}=\frac{1}{5}\left(c_{11}-c_{12}+3 c_{44}\right),\qquad(3)
$$

$$
B_{\mathrm{V}}=\frac{1}{3}\left(c_{11}+2 c_{12}\right).\qquad(4)
$$

According to the Reuss approximation,⁴² the Reuss shear modulus ($G_{\text{R}}$) and Reuss bulk modulus ($B_{\text{R}}$) can be rewritten as follows:

$$
G_{\mathrm{R}}=\frac{5 c_{44}\left(c_{11}-c_{12}\right)}{4 c_{44}+\left(c_{11}-c_{12}\right)},\qquad(5)
$$

$$
B_{\mathrm{R}}=\frac{1}{3}\left(c_{11}+2 c_{12}\right)=B_{\mathrm{V}}.\qquad(6)
$$

In the Hill empirical average,⁴³ the shear modulus ($G$) and bulk modulus ($B$) are obtained using the following equations:

$$
G=\frac{1}{2}\left(G_{\mathrm{V}}+G_{\mathrm{R}}\right),\qquad(7)
$$

$$
B=\frac{1}{2}\left(B_{\mathrm{V}}+B_{\mathrm{R}}\right).\qquad(8)
$$

Therefore, Young's modulus ($Y$) and Poisson's ration ($\nu$) are described as follows:

$$
Y=\frac{9 B G}{3 B+G};\qquad(9)
$$

$$
\nu=\frac{3 B-2 G}{2(3 B+G)}.\qquad(10)
$$

The results of elastic properties for the Heusler alloys CoFeRGa are displayed in Table 2. For cubic crystals, the Born criteria is reported as $((c_{11}-c_{12})>0,c_{11}>0,c_{44}>0,(c_{11}+2c_{12})>0,c_{12}<B<c_{11}).^{44}$ According to the Born criteria, the quaternary compounds CoFeRGa are mechanically stable. Compared with the resistance and the unidirectional compression, CoFeRGa offer a weaker resistance to pure shear deformation because $c_{11}$ is larger than $c_{44}$. The larger the $c_{11}$ value, the stronger the resistance for the unidirectional compression. CoFeTiGa possesses the most resistance to unidirectional compression in CoFeRGa.

Excellent mechanical properties are essential for the reliability of TE or spin-transport devices. The stiffness of the material is related to the size of $G$. As shown in Table 2, CoFeTiGa exhibits the largest value $G$ with 143.21 GPa, while CoFeCuGa has the least $G$ (42.17 GPa). Accordingly, CoFeTiGa is the stiffest of all the studied compounds, while CoFeCuGa is

<table><thead><tr><th>Alloys</th><th>$c_{11}$</th><th>$c_{12}$</th><th>$c_{44}$</th><th>$G_{\text{V}}$</th><th>$G_{\text{R}}$</th><th>$G$</th><th>$B$</th><th>$Y$</th><th>$\nu$</th><th>$B/G$</th></tr></thead><tbody><tr><td>CoFeTiGa</td><td>316.24</td><td>125.56</td><td>125.75</td><td>113.59</td><td>172.84</td><td>143.21</td><td>189.12</td><td>171.52</td><td>0.20</td><td>1.32</td></tr><tr><td>CoFeVGa</td><td>242.18</td><td>191.65</td><td>112.96</td><td>77.88</td><td>56.81</td><td>67.35</td><td>208.49</td><td>91.20</td><td>0.35</td><td>3.09</td></tr><tr><td>CoFeCrGa</td><td>228.15</td><td>161.64</td><td>120.01</td><td>85.31</td><td>73.02</td><td>79.16</td><td>183.81</td><td>103.84</td><td>0.56</td><td>2.32</td></tr><tr><td>CoFeMnGa</td><td>260.52</td><td>197.15</td><td>165.11</td><td>112.74</td><td>77.45</td><td>95.10</td><td>214.94</td><td>248.63</td><td>0.31</td><td>2.26</td></tr><tr><td>CoFeCuGa</td><td>166.08</td><td>151.17</td><td>105.59</td><td>66.34</td><td>18.00</td><td>42.17</td><td>156.14</td><td>58.03</td><td>0.54</td><td>3.70</td></tr><tr><td>CoFeNbGa</td><td>257.03</td><td>176.04</td><td>106.96</td><td>80.37</td><td>85.13</td><td>82.75</td><td>203.04</td><td>218.56</td><td>0.32</td><td>2.45</td></tr></tbody></table>

less stiffer. In CoFeRGa compounds, the sequence of $B$ from high to low is: $B(\text{Mn}) > B(\text{V}) > B(\text{Nb}) > B(\text{Ti}) > B(\text{Cr}) > B(\text{Cu})$. The $B/G$ ratio is the condition to judge the ductility or brittle- ness of the material proposed by Pugh *et al.*,⁴⁵ and the critical value separating ductile from brittle materials is approximately 1.75. From the results of CoFeRGa, these compounds except for CoFeTiGa are ductile materials. $Y$ is defined as the ratio between stress and strain, which can be used for the measure- ment of stiffness of materials, whereas the larger $Y$ value corresponds to higher stiffness. $Y$ of CoFeCuGa is larger than $B$ of the compounds. CoFeCuGa is stiffer than any other studied materials. Poisson's ratio $\nu$ is the measure of compressibility to provide information to quantify the stability of the crystal. It is clear from Table 2 that CoFeTiGa, CoFeVGa, CoFeMnGa, and CoFeNbGa are stable against external deformation. It is sensi- tive to external deformation that $\nu$ of CoFeCrGa and CoFeCuGa is greater than 0.5.

In order to prove the dynamic stability, the phonon spectra of CoFeRGa is presented in Fig. S1 (ESI†). There are sixteen atoms per unit cell of the $F\overline{4}3m$ phase of CoFeRGa. Thus, it has forty-eight corresponding modes of vibration containing three acoustical modes and forty-five optical modes. As can be seen from the phonon curves, the Heusler alloys CoFeRGa have no imaginary phonon frequency in the entire Brillouin zone.

### 3.3 Electronic structure
We offer the spin-resolved band structure along with the high symmetry directions of the Brillouin zone for the CoFeRGa alloys, as shown in Fig. 2. The quaternary alloys CoFeRGa except CoFeTiGa and CoFeCuGa compounds have indirect energy gaps from the $\Gamma$-point at the valence band maximum (VBM) to the $X$-point at the conduction band minimum (CBM) in the spin-down channel. The bandgap of the spin-down channel gradually increases from 0.28 eV, 0.34 eV to 0.99 eV, when the R atom goes along $\text{V} \rightarrow \text{Cr} \rightarrow \text{Mn}$. From Fig. 2(a), CoFeTiGa is a traditional semiconductor with a 0.30 eV direct bandgap at the $\Gamma$-point. This means that the spin-Seebeck effect is gone. From the band structure of CoFeCuGa given in Fig. 2(f), it is obvious that the material has metallic behavior in both the spin-up and spin-down channels, which will pro- duce a small spin-dependent Seebeck effect. For the spin-up states, these four Heusler alloys CoFeVGa, CoFeMnGa, and CoFeNbGa show a metallic overlap near the Fermi level, while CoFeCrGa has a zero gap between VBM and CBM. According to their unique band structures, CoFeVGa, CoFeMnGa, and CoFeNbGa are viewed as HM FiMs, and CoFeCrGa alloy possesses a SGS feature. Therefore, the SGS and HM with 100% spin polarization have promised transport properties, which can be designed as important candidates in the spin transport field.

We calculate spin-dependent total density of states (TDOS) and projected density of states (PDOS) for CoFeRGa, as shown in Fig. 3. Fig. 3(a) shows that CoFeTiGa is a nonmagnetic semiconductor, because the number of electrons in spin-up and spin-down channels are almost equal. Fig. 3(c) displays that CoFeCrGa exhibits the SGS behavior, namely, an open bandgap in spin-up channel and a closed bandgap in the others. CoFeVGa, CoFeMnGa and CoFeNbGa exhibit half- metallicity, as shown in Fig. 3(b), (d), and (f), since the spin- up TDOS crosses the Fermi level, while the spin-down channel

![](./images/812565818855391234_3.jpg)

Fig. 2 Spin-polarized electronic structure of the quaternary Heusler compounds CoFeRGa (R = Ti, V, Cr, Mn, Cu, and Nb) (a–f). The spin-up and spin- down band structures are denoted by black and red lines, respectively. The spin-down bandgap is marked in blue font.

has a bandgap. According to the PDOS, the hybridizations of Co, Fe, and R atoms in CoFeVGa, CoFeMnGa, CoFeCuGa and CoFeNbGa are responsible for its half-metallicity, respectively. Otherwise, the TDOS of CoFeCrGa is mainly dominated by Cr atoms at the Fermi level. Ga atoms make negligible contributions to the property at the Fermi level for all CoFeRGa bulk. In addition, we further analyzed the influence of atomic orbitals and found that the Co-d, Fe-d, and R-d states have a major role in their PDOS, as shown in Fig. S2 (ESI†). Moreover, compared with HM and SGS, we found that Cr plays a dominant role in transport properties of CoFeCrGa.

In order to understand the nature of interaction between the constituent atoms, we calculated the electron localization function⁴⁶ (ELF) and Bader charge.⁴⁷ The ELF of compounds qualitatively estimates the bonding properties of different atoms. The values of ELF are between 0 and 1. If the value of ELF is 1, the electrons are entirely localized. The material possesses fully covalent bonding. When the value of ELF is 0.5, the behavior of electrons is primarily delocalized. This accounts for the formation of the metallic bond. If the value of ELF ranges from 0 to 0.5, the electrons are bound. The ionic bond will appear. The ionic bonds are generated between R atoms and the nearest Co, Fe, and Ga atoms, as shown in Fig. 4. For CoFeVGa and CoFeNbGa, the interactions between V/Nb atoms and other atoms are stronger than that between other compounds. The atomic charge transfer distributions were calculated using the Bader method summarized in Table 3. The charges of the transition metal atoms vary considerably, while only minor changes are observed for those of the Ga atoms. The Bader charge reveals that in the type-I structure, R atoms lose charge and Co or Fe atoms play the role of gaining the charge. CoFeCuGa with the type-II structure has the opposite site states.

### 3.4 Electronic transport properties
In Fig. 5, we present the spin-Seebeck coefficient of CoFeRGa with the temperature. Since the quaternary CoFeVGa, CoFeCrGa, CoFeMnGa, and CoFeNbGa are metallic in the spin-up channel, the Seebeck coefficient has the small Seebeck coefficient. Accordingly, the calculated Seebeck coefficient of bulk CoFeCuGa is merely $-1.55\ \mu\mathrm{V\ K^{-1}}$ at 300 K. The HM materials possess two spin channels, one is metallic and the other has a bandgap around the Fermi energy. In this work, CoFeVGa, CoFeMnGa, and CoFeNbGa exhibit HM behaviors, the Seebeck coefficient shows a significant difference in two spin channels. In the spin-up channel, the Seebeck coefficient of CoFeVGa increases linearly with the temperature from $3.51\ \mu\mathrm{V\ K^{-1}}$ (at 100 K) to $18.31\ \mu\mathrm{V\ K^{-1}}$ (at 800 K). The Seebeck coefficient of CoFeNbGa increases from $2.24\ \mu\mathrm{V\ K^{-1}}$ (at 100 K) to $11.03\ \mu\mathrm{V\ K^{-1}}$ (at 570 K), and then decreases to $10.46\ \mu\mathrm{V\ K^{-1}}$ (at 800 K). The Seebeck coefficient of CoFeMnGa converts from $21.93\ \mu\mathrm{V\ K^{-1}}$ (at 100 K) to $-9.34\ \mu\mathrm{V\ K^{-1}}$ (at 800 K). In terms of the spin-down channel, the Seebeck coefficient of CoFeVGa decreases from $1327.59\ \mu\mathrm{V\ K^{-1}}$ (at 100 K) to $160.53\ \mu\mathrm{V\ K^{-1}}$ (at 800 K). Meanwhile, there is comparatively a rapid decrease from $1922.36\ \mu\mathrm{V\ K^{-1}}$ (at 100 K) and then it reaches $401.03\ \mu\mathrm{V\ K^{-1}}$ (at 800 K) for CoFeNbGa. However, the Seebeck coefficient of CoFeMnGa increases with the increase in temperature from $46.32\ \mu\mathrm{V\ K^{-1}}$ (100 K) to $171.65\ \mu\mathrm{V\ K^{-1}}$ (800 K). At room temperature, the Seebeck coefficients of CoFeVGa, CoFeNbGa and CoFeMnGa are $9.76\ \mu\mathrm{V\ K^{-1}}$, $9.06\ \mu\mathrm{V\ K^{-1}}$ and $17.11\ \mu\mathrm{V\ K^{-1}}$ in the spin-up channel, respectively. Correspondingly, the

![](./images/812565818855391234_4.jpg)

Fig. 3 Spin-dependent total density of states and partial density of states of the Heusler alloys CoFeRGa (R = Ti, V, Cr, Mn, Cu, and Nb) at the ground state (a-f). The positive and negative values of the density of states correspond to the spin-up and spin-down channels, respectively.

![](./images/812565818855391234_5.jpg)

Fig. 4 (a-f) Calculated electron localization function of the Heusler alloys CoFeRGa in the most stable structure.

<table>
<thead>
<tr>
<th colspan="7">Table 3 Bader charge of the Heusler alloys CoFeRGa. "$\Delta$" refers to the transfer of Bader charge for each atomic species in compounds. The "+" and "$-$" mean gaining and losing charge respectively</th>
</tr>
<tr>
<th>Alloys</th>
<th>$\Delta$(Ti)</th>
<th>$\Delta$(V)</th>
<th>$\Delta$(Cr)</th>
<th>$\Delta$(Mn)</th>
<th>$\Delta$(Cu)</th>
<th>$\Delta$(Nb)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Co</td>
<td>+0.72</td>
<td>+0.54</td>
<td>+0.40</td>
<td>+0.36</td>
<td>+0.36</td>
<td>+0.55</td>
</tr>
<tr>
<td>Fe</td>
<td>+0.49</td>
<td>+0.41</td>
<td>+0.32</td>
<td>+0.17</td>
<td>−0.21</td>
<td>+0.46</td>
</tr>
<tr>
<td>R</td>
<td>−1.23</td>
<td>−0.90</td>
<td>−0.59</td>
<td>−0.39</td>
<td>+0.16</td>
<td>−0.97</td>
</tr>
<tr>
<td>Ga</td>
<td>+0.02</td>
<td>−0.05</td>
<td>−0.13</td>
<td>−0.15</td>
<td>−0.21</td>
<td>−0.04</td>
</tr>
</tbody>
</table>

Seebeck coefficients with the spin-down channel are $382.04\ \mu\text{V K}^{-1}$, $789.21\ \mu\text{V K}^{-1}$ and $113.37\ \mu\text{V K}^{-1}$, respectively. The Seebeck coefficient of the spin-down channel is much greater than that of the spin-up channel, which attributes to semiconductor properties in the spin-down channel. The variation in the spin-Seebeck coefficient is consistent with the Seebeck coefficient of the spin-up channel for CoFeVGa, CoFeMnGa, and CoFeNbGa. The calculated spin-Seebeck coefficients of CoFeVGa, CoFeNbGa, and CoFeMnGa are $9.72\ \mu\text{V K}^{-1}$, $9.05\ \mu\text{V K}^{-1}$, and $10.15\ \mu\text{V K}^{-1}$ at room temperature, respectively. As far as these three HM compounds are concerned, CoFeMnGa has the highest Seebeck coefficient, which attributes to the relatively large energy gap. The Heusler alloy CoFeCrGa is SGS with a zero-gap in the spin-up channel. The Seebeck coefficient decreases with the increase in temperature from $-74.36\ \mu\text{V K}^{-1}$ (at 130 K) to $-12.84\ \mu\text{V K}^{-1}$ (at 800 K) in the spin-up channel, and that for the spin-down channel decreases from $836.94\ \mu\text{V K}^{-1}$ (at 100 K) to $242.09\ \mu\text{V K}^{-1}$ (at 800 K). At room temperature, the Seebeck coefficients of two spin channels for CoFeCrGa are $-58.78\ \mu\text{V K}^{-1}$ (the spin-up channel) and $442.88\ \mu\text{V K}^{-1}$ (the spin-down channel). The Seebeck coefficient of the spin-down channel is about 7.5 times than that of the spin-up channel. The spin-Seebeck coefficient of CoFeCrGa decreases with the increase in temperature from $-74.43\ \mu\text{V K}^{-1}$ (at 130 K) to $-22.16\ \mu\text{V K}^{-1}$ (at 800 K), and the value is $-60.29\ \mu\text{V K}^{-1}$ at room temperature. It is evident that the spin-up and spin-Seebeck coefficients of CoFeCrGa are probably 5-6 times larger than those of CoFeVGa, CoFeMnGa, and CoFeNbGa. In the HM materials, the spin-up band shows the typical metallic behavior. There is a zero gap in the spin-up channel for SGS CoFeCrGa. The transmission coefficients of CoFeCrGa have strong asymmetry near the Fermi level in the spin-up channel contrary to other materials. Therefore, SGS CoFeCrGa has a large value of

![](./images/812565818855391234_6.jpg)

Fig. 5 Seebeck coefficient of the Heusler alloys CoFeRGa except for CoFeTiGa as a function of temperature.

![](./images/812565818855391234_7.jpg)

Fig. 6 Calculated transmission coefficients of the quaternary Heusler compounds: (a) CoFeVGa, (b) CoFeMnGa, (c) CoFeNbGa, and (d) CoFeCrGa at their equilibrium lattice constants.

Seebeck coefficient in the spin-up channel. Otherwise, since the spin-up band of CoFeCrGa has a zero gap semiconducting char- acteristic, no threshold energy is required to move the electrons from occupied states to empty states. As the temperature increases, the semiconductor phase of CoFeCrGa transforms into the metallic phase. Thus, the variation in the Seebeck coefficient of CoFeCrGa with temperature in the spin-up channel is obviously larger than that of other Heusler compounds. The spin-Seebeck coefficient originates from two counteracting spin contributions. The Heusler alloys CoFeRGa have a larger Seebeck coefficient in the spin-down channel attributed to the semiconductor feature, but have almost negligible electrical conductivity. According to eqn (1) of the spin-Seebeck coefficient, the variation in the spin-Seebeck coefficient of CoFeRGa is identified with the spin-up Seebeck coefficient. Therefore, the unique band structure with the SGS behavior possesses superior transport properties to nearly-HM, HM, and metal phases.

To explore the reason for the large spin-Seebeck effect with elevated temperatures, we further calculate the spin-resolved transmission coefficients of HM CoFeVGa, CoFeMnGa, and CoFeNbGa and SGS CoFeCrGa, as depicted in Fig. 6. The reason for the high spin-down Seebeck coefficient is that there exists a gap in the spin-down channel attributed to the semiconductor feature. The calculated bandgap value of CoFeCrGa compounds with the spin-down channel is lower than those of CoFeVGa, CoFeMnGa, and CoFeNbGa. Correspondingly, the Seebeck coeffi- cient is not larger than those of CoFeVGa, CoFeMnGa, and CoFeNbGa. In terms of CoFeCrGa, no threshold energy is required to move the electrons from occupied states to empty states on account of the zero bandgap in the spin-up channel. The SGS nature results in a relatively large negative Seebeck coefficient with the spin-up channel. Besides, the transmission coefficients of CoFeCrGa have converse asymmetry in spin-up or spin-down channel because of its novel band structure. Therefore, CoFeCrGa with the SGS behavior exhibits promising spin-transport proper- ties compared with other HM compounds.

## 4. Conclusions
By using the first-principles calculation combined with spin- resolved Boltzmann transport theory, all types (including type-I, type-II, and type-II) of high spin-Seebeck effects are realized in stable CoFeRGa (R = Ti, V, Cr, Mn, Cu, and Nb) materials via tunable band structures. Our results indicated that CoFeCrGa naturally possesses an SGS character, and its spin-Seebeck coefficient achieves $-60.29\ \mu V\ K^{-1}$ at 300 K. This value is significantly larger than those of the other CoFeRGa. In addi- tion, this class of Heusler materials contains CS, metal, HM, SGS within FM, FiM, AFM and NM states, which is endowed with a great opportunity to expand spin caloritronic applica- tions. This work not only provides an example to investigate the novel transport properties with diverse electron behaviors but also gives enormous potential for many applications such as spintronics or thermoelectrics.

## Data availability statement
The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Conflicts of interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements
This research was supported by the National Natural Science Foundation of China (No. 11674083, 21603056, 11305046), and Foundation of Henan Province (No. 182106000023 and 182300410227).

## References
1 L. E. Bell, Cooling, heating, generating power, and recover- ing waste heat with thermoelectric systems, *Science*, 2008, 321, 1457-1461.

2 M. Walter, J. Walowski, V. Zbarsky, M. Münzenberg, M. Schäfers, D. Ebke, G. Reiss, A. Thomas, P. Peretzki, M. Seibt, J. S. Moodera, M. Czerner, M. Bachmann and C. Heiliger, Seebeck effect in magnetic tunnel junctions, *Nat. Mater.*, 2011, 10, 742-746.

3 H. X. Wang, L. S. Mao, X. Tan, G. Q. Liu, J. Xu, H. Shao, H. Hu and J. Jiang, Nontrivial thermoelectric behavior in cubic SnSe driven by spin-orbit coupling, *Nano Energy*, 2018, 51, 649-655.

4 J. Li, G. Zhang, C. Peng, W. Wang, J. Yang and Z. Cheng, Magneto-Seebeck effect in $Co_2FeAl/MgO/Co_2FeAl$: First- principles calculations, *Phys. Chem. Chem. Phys.*, 2019, 21, 5803-5812.

5 A. Banik, U. S. Shenoy, S. Anand, U. V. Waghmare and K. Biswas, Mg alloying in SnTe facilitates valence band

convergence and optimizes thermoelectric properties,
Chem. Mater., 2015, 27, 581-587.

6 L. Wu, X. Li, S. Wang, T. Zhang, J. Yang, W. Zhang, L. Chen
and J. Yang, Resonant level-induced high thermoelectric
response in indium-doped GeTe, NPG Asia Mater., 2017,
9, e343.

7 G. Tan, L. D. Zhao, F. Shi, J. W. Doak, S. H. Lo, H. Sun,
C. Wolverton, V. P. Dravid, C. Uher and M. G. Kanatzidis,
High thermoelectric performance of p-Type SnTe via a
synergistic band engineering and nanostructuring
approach, J. Am. Chem. Soc., 2014, 136, 7006-7017.

8 Y. L. Pei, H. Wu, D. Wu, F. Zheng and J. He, High thermo-
electric performance realized in a BiCuSeO system by
improving carrier mobility through 3D modulation doping,
J. Am. Chem. Soc., 2014, 136, 13902-13908.

9 Z. Ma, C. Wang, J. Lei, D. Zhang, Y. Chen, J. Wang, Z. Cheng
and Y. Wang, High thermoelectric performance of SnTe by
the synergistic effect of alloy nanoparticles with elemental
elements, ACS Appl. Energy Mater., 2019, 2, 7354-7363.

10 P. Ying, X. Liu, C. Fu, X. Yue, H. Xie, X. Zhao, W. Zhang and
T. J. Zhu, High performance $\alpha$-MgAgSb thermoelectric
materials for low temperature power generation, Chem.
Mater., 2015, 27, 909-913.

11 J. He, J. R. Sootsman, S. N. Girard, J. C. Zheng, J. Wen,
Y. Zhu, M. G. Kanatzidis and V. P. Dravid, On the origin of
increased phonon scattering in nanostructured PbTe based
thermoelectric materials, J. Am. Chem. Soc., 2010, 132,
8669-8675.

12 L. Yang, Z. G. Chen, G. Han, M. Hong, Y. Zou and J. Zou,
High-performance thermoelectric $Cu_2Se$ nanoplates
through nanostructure engineering, Nano Energy, 2015, 16,
367-374.

13 F. Li, J. F. Li, L. D. Zhao, K. Xiang, Y. Liu, B. P. Zhang,
Y. H. Lin, C. W. Nan and H. M. Zhu, Polycrystalline BiCuSeO
oxide as a potential thermoelectric material, Energy Environ.
Sci., 2012, 5, 7188.

14 P. Niu, L. Liu, X. Su, L. Dong and H. G. Luo, Spin Seebeck
effect in a metal-single-molecule-magnet-metal junction,
AIP Adv., 2018, 8, 015215.

15 J. Li, Y. Wang, G. Zhang, H. Yin, D. Chen, W. Sun, B. Shi and
Z. Cheng, Seeking large Seebeck effects in LaX(X = Mn and
Co)$O_3$/SrTiO$_3$ superlattices by exploiting high spin-polarized
effects, Phys. Chem. Chem. Phys., 2019, 21, 14973-14983.

16 S. Bosu, Y. Sakuraba, K. Uchida, K. Saito, T. Ota, E. Saitoh
and K. Takanashi, Spin Seebeck effect in thin films of the
Heusler compound $Co_2$MnSi, Phys. Rev. B: Condens. Matter
Mater. Phys., 2011, 83, 224401.

17 M. Czerner, M. Bachmann and C. Heiliger, Spin caloritronics
in magnetic tunnel junctions: Ab initio studies, Phys. Rev. B:
Condens. Matter Mater. Phys., 2011, 83, 132405.

18 L. Bainsla, M. M. Raja, A. K. Nigam and K. G. Suresh,
CoRuFeX(X = Si and Ge) Heusler alloys: High $T_C$ materials
for spintronic applications, J. Alloys Compd., 2015, 651,
631-635.

19 B. Wang, X. Zhang, Y. Zhang, S. Yuan, Y. Guo, S. Dong and
J. Wang, Prediction of a two-dimensional high-$T_C$ f-electron
ferromagnetic semiconductor, Mater. Horiz., 2020, 7,
1623-1630.

20 H. Yin, C. Liu, G. P. Zheng, Y. Wang and F. Ren, Ab initio
simulation studies on the room-temperature ferroelectricity
in two-dimensional $\beta$-phase GeS, Appl. Phys. Lett., 2019,
114, 192903.

21 Z. Feng, Y. Fu, Y. Zhang and D. J. Singh, Characterization of
rattling in relation to thermal conductivity: Ordered half-
Heusler semiconductors, Phys. Rev. B, 2020, 101, 064301.

22 Y. Yan, J. Yang, J. Li, Y. Wang and W. Ren, High thermo-
electric properties in full-Heusler $X_2YZ$ alloys (X = Ca, Sr,
and Ba; Y = Au and Hg; Z = Sn, Pb, As, Sb, and Bi), J. Phys. D:
Appl. Phys., 2019, 52, 495303.

23 L. Bainsla, A. I. Mallick, M. M. Raja, A. A. Coelho,
A. K. Nigam, D. D. Johnson, A. Alam and K. G. Suresh,
Origin of spin gapless semiconductor behavior in
CoFeCrGa: Theory and Experiment, Phys. Rev. B: Condens.
Matter Mater. Phys., 2015, 92, 045201.

24 V. Alijani, J. Winterlik, G. H. Fecher, S. S. Naghavi and
C. Felser, Quaternary half-metallic Heusler ferromagnets for
spintronics applications, Phys. Rev. B: Condens. Matter
Mater. Phys., 2011, 83, 184428.

25 V. Alijani, S. Ouardi, G. H. Fecher, J. Winterlik, S. S. Naghavi,
X. Kozina, G. Stryganyuk, C. Felser, E. Ikenaga, Y. Yamashita,
S. Ueda and K. Kobayashi, Electronic, structural, and magnetic
properties of the half-metallic ferromagnetic quaternary Heusler
compounds CoFeMnZ (Z = Al, Ga, Si, Ge), Phys. Rev. B: Condens.
Matter Mater. Phys., 2011, 84, 224416.

26 Enamullah and S. C. Lee, High-efficient and defect tolerant
$Co_2$MnSb ternary Heusler alloy for spintronic application,
J. Alloys Compd., 2018, 765, 1055-1060.

27 C. Felser and A. Hirohata, Heusler Alloys: Properties, Growth,
Applications, Springer International Publishing, 2016,
pp. 193-216.

28 J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson,
M. R. Pederson, D. J. Singh and C. Fiolhais, Atoms, mole-
cules, solids, and surfaces: Applications of the generalized
gradient approximation for exchange and correlation, Phys.
Rev. B: Condens. Matter Mater. Phys., 1992, 46, 6671-6687.

29 P. E. Blöchl, Projector augmented-wave method, Phys. Rev.
B: Condens. Matter Mater. Phys., 1994, 50, 17953-17979.

30 G. Kresse and J. Furthmüller, Efficient iterative schemes for
ab initio total-energy calculations using a plane-wave basis set,
Phys. Rev. B: Condens. Matter Mater. Phys., 1996, 54, 11169-11186.

31 G. Kresse and D. Joubert, From ultrasoft pseudopotentials
to the projector augmented-wave method, Phys. Rev. B:
Condens. Matter Mater. Phys., 1999, 59, 1758-1775.

32 J. P. Perdew, K. Burke and M. Ernzerhof, Generalized
gradient approximation made simple, Phys. Rev. Lett.,
1996, 77, 3865-3868.

33 S. Baroni, S. de Gironcoli, A. Dal Corso and P. Giannozzi,
Phonons and related crystal properties from density-functional
perturbation theory, Rev. Mod. Phys., 2001, 73, 515-562.

34 S. Baroni, P. Giannozzi and A. Testa, Green's-function
approach to linear response in solids, Phys. Rev. Lett.,
1987, 58, 1861-1864.

35 P. Blaha, K. Schwarz, P. Sorantin and S. B. Trickey, Full-potential, linearized augmented plane wave programs for crystalline systems, *Comput. Phys. Commun.*, 1990, **59**, 399-415.

36 F. Tran and P. Blaha, Accurate band gaps of semiconductors and insulators with a semilocal exchange-correlation potential, *Phys. Rev. Lett.*, 2009, **102**, 226401.

37 G. K. H. Madsen and D. J. Singh, BoltzTraP. A code for calculating band-structure dependent quantities, *Comput. Phys. Commun.*, 2006, **175**, 67-71.

38 B. Geisler, P. Kratzer and V. Popescu, Interplay of growth mode and thermally induced spin accumulation in epitaxial Al/Co₂TiSi/Al and Al/Co₂TiGe/Al contacts, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2014, **89**, 184422.

39 L. Triguero, L. G. M. Pettersson and H. Ågren, Calculations of near-edge X-ray-absorption spectra of gas-phase and chemisorbed molecules by means of density-functional and transition-potential theory, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1998, **58**, 8097.

40 F. Mouhat and F. X. Coudert, Necessary and sufficient elastic stability conditions in various crystal systems, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2014, **90**, 224104.

41 W. Voigt, *Lehrbuch der kristallphysik*, Leipzig, Teubner, 1928.

42 A. Reuss, Berechnung der Fließgrenze von Mischkristallen auf Grund der Plastizitätsbedingung für Einkristalle, *Z. Angew. Math. Mech.*, 1929, **9**, 49-58.

43 R. Hill, Theory of mechanical properties of fibre-strengthened materials—III. self-consistent model, *J. Mech. Phys. Solids*, 1965, **13**, 189-198.

44 G. V. Sin'ko and N. A. Smirnov, *Ab initio* calculations of elastic constants and thermodynamic properties of bcc, fcc, and hcp Al crystals under pressure, *J. Phys.: Condens. Matter*, 2002, **14**, 6989-7005.

45 S. F. Pugh, Relations between the elastic moduli and the plastic properties of polycrystalline pure metals, *Lond. Edinb. Dubl. Phil. Mag.*, 1954, **45**, 823-843.

46 A. Savin, R. Nesper, S. Wengert and T. E. Fassler, ELF: The electron localization function, *Angew. Chem., Int. Ed. Engl.*, 1997, **36**, 1808-1832.

47 E. Sanville, S. D. Kenny, R. Smith and G. Henkelman, Improved grid-based algorithm for Bader charge allocation, *J. Comput. Chem.*, 2007, **28**, 10.