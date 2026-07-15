Journal of
Materials Chemistry C

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: X. Wang, Z.
Cheng, J. Wang and G. Liu, J. Mater. Chem. C, 2016, DOI: 10.1039/C6TC02526A.

![](./images/811158924873957376_1.jpg)

This is an Accepted Manuscript, which has been through the
Royal Society of Chemistry peer review process and has been
accepted for publication.

Accepted Manuscripts are published online shortly after
acceptance, before technical editing, formatting and proof reading.
Using this free service, authors can make their results available
to the community, in citable form, before we publish the edited
article. We will replace this Accepted Manuscript with the edited
and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the
Information for Authors.

Please note that technical editing may introduce minor changes
to the text and/or graphics, which may alter content. The journal's
standard Terms & Conditions and the Ethical guidelines still
apply. In no event shall the Royal Society of Chemistry be held
responsible for any errors or omissions in this Accepted Manuscript
or any consequences arising from the use of any information it
contains.

![](./images/811158924873957376_2.jpg)

www.rsc.org/materialsC

ARTICLE

# A full spectrum of spintronic properties demonstrated by $C1_b$-type Heusler compound $Mn_2Sn$ subjected to strain engineering

Xiaotian Wang, $^{ab}$ Zhenxiang Cheng, $^{*b}$ Jianli Wang $^{b}$ and Guodong Liu $^{*a}$

Zero-gap half-metallic fully-compensated ferrimagnets (ZG-HM-FCFs), and fully-compensated ferrimagnetic spin-gapless semiconductors (FCF-SGSs) are promising candidates for spintronic applications due to the complete (100%) spin polarization of electrons around the Fermi level. Motivated by recent experimental and theoretical findings on binary $Mn_2$-based $C1_b$-type Heusler compounds, by means of first-principles calculations, we find that $Mn_2Sn$ exhibits the metallic ferrimagnetism property. Most interestingly, under a uniform strain, there is a novel transition in the physics from a metallic ferrimagnet (MFi) to truly ZG-HM-FCF, HM-FCF, FCF-SGS, and then a fully-compensated ferrimagnetic semiconductor (FCF-S). Binary $Mn_2Sn$ compound remains MFi under a tetragonal distortion, however. We also reveal that the structure of $Mn_2Sn$ is stable, according to its mechanical properties, calculated cohesion energy, and formation energy. Our work demonstrates that $Mn_2Sn$ is potentially an all-round candidate for spintronic applications because it shows a full spectrum of spintronic properties under uniform strain.

## 1. Introduction

Half-metallic ferrimagnets (HMFis) $^{1}$, especially the ones with Heusler-type structure $^{3-15}$, have received considerable interest during the past thirty years. The energy band diagram for this type of material is presented in Fig. 1a. As shown in Fig 1a, the band structures of HMFis show metallic characteristics in one spin channel and semiconducting or insulating ones in the other spin channel, which results in full spin-polarization of electrons around the Fermi level. This material with such high spin polarization can be used as an ideal spin source material $^{16}$. Importantly, van Leuken and de Groot $^{17}$ predicted the possibility of realizing half-metallic antiferromagnets (HMAFMs), and the precise definition of HMAFMs is half-metallic fully-compensated ferrimagnets (HM-FCFs) $^{18, 19}$. As shown in Fig. 1b, HM-FCFs, unlike normal HMF systems, feature 100% spin polarization of the conduction electrons without showing a net magnetization. Therefore, HM-FCFs could be even more useful than normal HMFs in realistic spintronic applications for the following reasons $^{19}$: (i) most of these materials have a high magnetic transition temperature because of strong magnetic coupling; (ii) they are insensitive to external magnetic fields; (iii) no stray fields will be produced; and (iv) it will be easy to inject spins due to their small magnetic shape anisotropy.

$^{a}$ School of Material Sciences and Engineering, Hebei University of Technology, Tianjin 300130, PR China; *E-mail: gdliu1978@126.com
$^{b}$ Institute for Superconducting & Electronic Materials (ISEM), University of Wollongong, Wollongong 2500, Australia; *E-mail: cheng@uow.edu.au

This journal is © The Royal Society of Chemistry 20xx
J. Name., 2013, 00, 1-3 | 1

![](./images/811158924873957376_3.jpg)

Fig. 1 Schematic representation of the density of states (DOS) for various magnetic structures. N↑ (N↓) is the number of electrons occupying the spin-up (spin-down) states. When the populations of the two spin-electronic bands are equal (N↑=N↓) the compound behaves as a fully-compensated ferrimagnet. When the populations of the two spin-electronic bands are unequal (N↑≠N↓) the compound behaves as a usual ferrimagnet. Cases (a) and (b) correspond to the ferrimagnetic and fully-compensated ferrimagnetic half-metals, respectively. Cases (c) and (d) are the ferrimagnetic and fully-compensated ferrimagnetic spin-gapless semiconducting compounds, respectively. Cases (e) and (f) are the ferrimagnetic and fully-compensated ferrimagnetic zero-gap half-metals. Cases (g) and (h) are the ferrimagnetic and fully-compensated ferrimagnetic semiconductors.

In addition to the HM magnets, including HMFis and HM-FCFs, an interesting new class of materials, namely, spin-gapless semiconductors (SGSs)²⁰⁻²⁹, has also been widely investigated in the fields of solid-state physics and materials science because of their applications in a number of novel spintronic devices. As shown in Fig. 1c, for SGSs, there is a zero gap at the Fermi level in the majority spin channel and a band gap around the Fermi level in the minority spin channel. In SGSs, a small amount of energy is enough to excite electrons from the valence band to the conduction band. Furthermore, due to the complete (100%) spin polarization of both the electrons and holes, SGSs exhibit many unique transport properties, such as the coexistence of high resistance and a high Curie temperature. Up to now, SGSs have been theoretically predicted in Co-doped PbPdO₂²⁰, Fe and Cr co-doped boron nitride (BN) sheet³⁰, HgCr₂Se₄ under a pressure of 9 GPa³¹, BN nanoribbons with certain B or N vacancies³², monolayer MXene Ti₂C under a suitable biaxial strain³³, and some Heusler compounds³⁴⁻³⁹. Among these materials, some have been confirmed by experimental work. For example, Kim et al. and Choo et al.⁴⁰,⁴¹ investigated the electronic structures of Mn and Co doped PbPdO₂ polycrystalline films and confirmed their SGS behaviour, based on their magnetic and transport properties. Ouardi et al.⁴² prepared polycrystalline Mn₂CoAl compound by arc melting and confirmed the SGS characteristic by testing the magnetic and transport properties. Very recently, experimentalists and theorists have paid more attention to searching for a new class of materials, namely, fully-compensated ferrimagnetic spin-gapless semiconductors (FCF-SGS) (See Fig. 1d)⁴³⁻⁴⁵. Compared to SGSs, these FCF-SGSs will combine both the spin-gapless semiconductivity and the fully-compensated ferrimagnetism property in one compound. That is to say, FCF-SGSs show not only no net magnetization, but also the complete (100%) spin polarization of both the electrons and the holes. Therefore, compared to the normal SGSs, FCF-SGSs are a better class of spin-filter materials from the viewpoint of spintronic devices⁴⁶,⁴⁷.

Inspired by the relationship between HMFis and SGSs, Du et al.⁴⁸ proposed a new type of zero-gap material, zero-gap half-metallic materials (ZG-HMs). As shown in Fig. 1e, in contrast to the band structures of metallic ferrimagnets (MFis) and normal HMFis, for ZG-HMs, there is a zero gap at the Fermi level in the minority spin channel and a conducting property in the majority spin channel. In their work, the electronic structure and magneto-transport properties of the Heusler compound Fe₂CoSi were studied in detail. The calculated results revealed that the highly ordered inverse Heusler compound Fe₂CoSi has 100 % spin polarization, and the measured Curie temperature is very high, up to about 1038 K. Interestingly, a crossover from positive to negative magnetoresistance (MR) can be observed with increasing temperature. Note that this unique magnetoresistance behaviour of ZG-HM Fe₂CoSi is similar to that of a SGS candidate. The density-of-states (DOS) scheme in the case of the fully-compensated ferrimagnetic zero-gap half-metallic materials is also given in Fig. 1f.

DOS schemes of the magnetic semiconductors/fully-compensated ferrimagnetic semiconductors (MSs)/FCF-Ss are

![](./images/811158924873957376_4.jpg)

Fig. 2 (a) Crystal structures of $Mn_2Sn$ compound: (i) type I: $C1_b$-type structure, (ii) type II: $L2_1$-type structure. (b) Possible magnetic structures: (i) antiferromagnetic (AFM) state and (ii) ferromagnetic (FM) state. (Yellow arrows represent the spin directions of Mn (A) and Mn (B) atoms)

shown in Fig. 1g and 1h. We find that the band structures of MSs/FCF-Ss show semiconducting or insulating properties in both of the spin channels. Such materials can find versatile applications, e.g. as spin-filter materials in magnetic tunnel junctions$^{48}$. The SGSs/FCF-SGSs can be considered as an extreme case of MSs/FCF-Ss, and the charge carrier density in SGS/FCF-SGS is much higher than in classical MS/FCF-S. Therefore, SGSs and FCF-SGSs will offer novel functionalities in spintronic/magnetoelectronic devices.

To sum up, all the above-mentioned materials, the HMFis, HM-FCFs, SGSs, FCF-SGSs, ZG-HMs, FCF-ZG-HMs, MSs, and FCF- Ss, are important spintronic materials in terms of practical applications, especially in the cases of FCF-SGSs and FCF-ZG- HMs. Therefore, we should focus our attention on the search for these unique materials for spintronic applications. More importantly, we have raised a novel issue, namely, is it possible to find a material that exhibits different physics without the introduction of vacancies, doping, or an external electric field.

In this paper, we systematically investigate the electronic structure, magnetic properties, and structural stability of the $C1_b$-type Heusler compound $Mn_2Sn$. As is well known, cubic $Mn_2Ga$ films the with Heusler $C1_b$ structure have been grown on V (001) epitaxial films by Kurt et al.$^{50}$. Therefore, when grown by a special preparation method, i.e., film fabrication on special substrates, the $Mn_2Sn$ binary compound has a good chance of being practically fabricated in a cubic structure. We demonstrate using first-principles calculations that the metallic ferrimagnetism property can be obtained in $Mn_2Sn$ binary compound, and there are interesting and novel transitions in its physics from a MFi to truly FCF-HM, FCF-SGS, FCF-S, and even ZG-FCF-HM under a uniform strain. Furthermore, the effect of tetragonal distortion on the physics of the $Mn_2Sn$ compound and the stability of the structure, based on the mechanical properties, cohesion energy, and formation energy, are also discussed in detail.

### 2. Computational details

The electronic structure was calculated by means of CASTEP code based on the pseudopotential method with a plane-wave basis set$^{51,52}$. The interactions between the atomic core and the valence electrons were described by the ultrasoft pseudopotential$^{53}$. The generalized-gradient-approximation (GGA)$^{54}$ was adopted for the exchange-correction functional. In order to ensure the suitability of CASTEP for Heusler spin- gapless semiconductors with relatively subtle band structures, the band structures of $Mn_2CoAl$ and CoFeMnSi compounds, which have been confirmed as spin-gapless semiconductors$^{23}$, were first calculated by using CASTEP code. The CASTEP results show typical spin-gapless band structures of these two compounds in accordance with previous investigations. Therefore, in the present work, all calculations were reliably performed by using CASTEP code within the density functional theory (DFT). For all cases, a plane-wave basis set cut-off of 500 eV was used. A mesh of 15×15×15 k-points was employed for Brillouin zone integrations for the Heusler structure. These parameters ensured good convergence for the total energy. The convergence tolerance for the calculations was selected as a difference in total energy within $1 \times 10^{-6}$ eV/atom.

Furthermore, in this work, the electronic and magnetic properties of $Mn_2Sn$ under two kinds of strain, i.e. uniform strain and tetragonal distortion, were studied in detail. For varying uniform strain, the lattice constants tend to change, although the lattice retains its cubic close-packed structure. For the tetragonal distortion, we kept the unit-cell volume ($V_u = a \times b \times c$) the same as the equilibrium bulk volume ($V_e = a \times a \times a = a^3$), and then we changed the $c/a$ ratio. More details on the uniform strain and tetragonal distortion can be found in previous works$^{55,56}$.

In this work, we calculated the elastic constants of $Mn_2Sn$ by means of the stress-strain. For small strains, the system configuration changes from $X$ to $Y = JX$, where $J$ is the Jacobian matrix. As shown in Ref. 57, the associated

Lagrangian strain tensor is defined as $\eta = \frac{(U^TJ - 1)}{2}$. The internal energy can be expanded as $^{58}$

$$
E(X, \eta)=E(X, 0)+V(X) \times\left(\sum_{i j} \tau_{i j} \eta_{i j}+\frac{1}{2} \sum_{i j k l} C_{i j k l} \eta_{i j} \eta_{k l}+\cdots\right),
\tag{1}
$$

in which $\tau_{ij}$ are components of the stress tensor before deformation, and $C_{ijkl}$ are the elastic constants of the crystal at arbitrary pressure and can be obtained as follows:

$$
C_{i j k l}=\left(\frac{\partial \tau_{i j}(X, \eta)}{\partial \eta_{k l}}\right)_{\eta=0}=\frac{1}{V(X)}\left(\frac{\partial^{2} E(X, \eta)}{\partial \eta_{i j} \partial \eta_{k l}}\right)_{\eta=0}.
\tag{2}
$$

Because the stress and strain tensors are symmetric, the elastic constants have 21 independent components. Using the standard notation xx = 1, yy = 2, zz = 3, yz = 4, zx = 5, xy = 6, these elastic constants can be labelled as $C_{ij}=C_{ji}$, $i,j = 1,2,3,4,5,6$. For our Mn₂Sn compound, that is, a cubic crystal, the elastic constants are reduced to three independent components $^{59}$, i.e., $C_{11}$, $C_{22}$, and $C_{44}$. In detail, $C_{11}$ stands for the elasticity in length, while $C_{12}$ and $C_{44}$ stand for the elasticity in shape. By applying a small strain to our Mn₂Sn optimized unit cell, $C_{11}$, $C_{22}$, and $C_{44}$ can be obtained. Moreover, by the Voigt-Reuss-Hill (VRH) approximation $^{60}$, we can obtain the bulk modulus $B$, the shear modulus $G$, the Young's modulus $E$, and Poisson's ratio $\sigma$, and can further study other mechanical properties. In detail, the bulk modulus $B$ and the shear modulus $G$ are given by

$$
B=\frac{B_{V}+B_{R}}{2}, G=\frac{G_{V}+G_{R}}{2},
\tag{3}
$$

where the Voigt ($B_V$, $G_V$) and Reuss ($B_R$, $G_R$) expressions indicate the upper and lower limits for polycrystalline bulks, respectively. In the case of the cubic crystals, they are obtained from the elastic stiffness constants:

$$
B_{V}=B_{R}=\frac{\left(c_{11}+2 c_{12}\right)}{3},
\tag{4}
$$

$$
G_{V}=\frac{\left(c_{11}-c_{12}+3 c_{44}\right)}{5},
\tag{5}
$$

$$
G_{R}=\frac{5 c_{44}\left(c_{11}-c_{12}\right)}{4 c_{44}+3\left(c_{11}-c_{12}\right)},
\tag{6}
$$

The Young's modulus $E$ and Poisson's ratio $\sigma$ are calculated from $B$ and $G$ using the following formulas $^{61}$:

$$
E=\frac{9 G B}{3 B+G}, \sigma=\frac{3 B-2 G}{2(3 B+G)}.
\tag{7}
$$

## 3. Results and discussion

<table>
  <thead>
    <tr>
      <th>Compound</th>
      <th>$a$ (Å)</th>
      <th>$M_{tot}$ ($\mu_B$)</th>
      <th>$M_{Mn(A)}$ ($\mu_B$)</th>
      <th>$M_{Mn(B)}$ ($\mu_B$)</th>
      <th>$M_{Sn}$ ($\mu_B$)</th>
      <th>$E_{formation}$ (eV)</th>
      <th>$E_C$ (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mn₂Sn</td>
      <td>6.09</td>
      <td>-0.197</td>
      <td>4.12</td>
      <td>-4.28</td>
      <td>-0.04</td>
      <td>-2.715</td>
      <td>19.13</td>
    </tr>
  </tbody>
</table>

Table 1 Optimized lattice constant ($a$), calculated total ($M_{tot}$) and atomic magnetic moments per formula unit, and the cohesive ($E_C$) and formation ($E_f$) energies for the hypothetical binary C1ᵦ-type Heusler compound Mn₂Sn.

![](./images/811158924873957376_5.jpg)

Fig. 3 Calculated total energy as a function of the lattice constant for Mn₂Sn compound for both C1ᵦ-type (type I) and L2₁-type (type II) Heusler structures in the NM, AFM, and FM states. The minimum energy falls at 6.09 Å.

### 3.1 Magnetism and the electronic structure for equilibrium lattices

The highly ordered structure is very important for the physical properties of Heusler compounds. Normally, Heusler compounds are represented by the formula X₂YZ, where X and Y are two different transition metal elements, and Z is a main group element. The structure of Heusler compounds includes four interpenetrating face-centered cubic (fcc) lattices with atoms A, B, C, and D occupying positions (0,0,0), (0.25,0.25,0.25), (0.5,0.5,0.5), and (0.75,0.75,0.75), respectively in Wyckoff coordinates. In our current work, Mn₂Sn binary compound can be regarded as a special Heusler compound with one site (B or C) replaced by a vacant site. Therefore, there are two possible atomic orderings in the binary compound Mn₂Sn, as given in Fig. 2a: (i) Mn (A) and Mn (B) atoms occupy the A (0,0,0) and B (0.25,0.25,0.25) sites, the Sn atom occupies the D (0.75,0.75,0.75) site, and the C site remains vacant. Clearly, the crystal structure of type (i) can be regarded as the C1ᵦ-type Heusler structure with space group F-43m, No. 216. The sublattices of Mn (A) and Mn (B) atoms are inequivalent in the type (i) crystal structure. (ii) Mn (A) and Mn (B) atoms occupy the A (0,0,0) and C (0.5,0.5,0.5) sites, while the Sn atom occupies the D (,0.75,0.75,0.75) site, and the B site remains vacant. Obviously, this type of crystal structure is the L2₁ structure with space group Fm-3m, No. 225. The sublattices of Mn (A) and Mn (B) atoms are equivalent in the type (ii) crystal structure.

In this work, the non-magnetic (NM), ferromagnetic (FM), and antiferromagnetic (AFM) states for Mn₂Sn are taken into account to determine the stable ground state. As shown in Fig. 2b, for the AFM state, antiparallel coupled spin moments

![](./images/811158924873957376_6.jpg)

Fig. 4 Mn₂Sn band structure (top), and spin-polarized total and atom-resolved DOSs (bottom) at its equilibrium lattice constant. For the band structure, the black and red lines denote the majority and minority spin band structures, respectively.

between the two Mn atoms have been added, and for the case of the FM state, the parallel coupled spin moments between Mn (A) and Mn (B) have been given.

Before we go through the electronic structure and magnetic property calculations for the binary compound Mn₂Sn, we first present the calculated total energies of L2₁-type (type II) and C1ᵦ-type (type I) Mn₂Sn compound in NM, FM, and AFM magnetic structures as a function of the lattice constant in Fig. 3. We observe from Fig. 3 that the type I AFM state has the lowest total energy compared to the type I FM, type I NM, and type II states, and therefore, the AFM state with C1ᵦ-type Mn₂Sn compound is the most stable. From it, we also find that the optimized lattice constant in the AFM state is 6.09 Å for Mn₂Sn compound, which is in good agreement with the results of Fujii et al.⁶² (6.098 Å). Note that our result for the optimized lattice constant is somewhat larger than the result of Luo et al.⁶³ (5.69 Å), and the reason may be the effect of the so-called local density approximation (LDA) overbinding⁶³.

Table 1 shows the calculated total spin and atomic magnetic moments of C1ᵦ-type Mn₂Sn compound at its optimized lattice constant. Obviously, the total spin magnetic moment is -0.19 μB, while the atomic magnetic moments of the Sn atoms are very small (-0.04 μB) and only make a small contribution to the total magnetic moment. For this compound, the total magnetic moment mainly comes from Mn (A) and Mn (B) atoms. The atomic magnetic moment of Mn (A) and Mn (B) atoms is 4.12 μB and -4.28 μB, respectively. In Ref. 63, the atomic magnetic moments are -2.22 μB, 2.24 μB, and -0.02 μB, for Mn (A), Mn (B), and Sn, respectively. One can see that the values in their work are smaller than ours, and this can be traced back to the smaller optimized lattice constant in Ref. 63, which decreases the localization of Mn-d states and further decreases the total spin and atomic magnetic moments.

Fig. 4 presents the calculated band structure of Mn₂Sn compound along the main symmetry axis in the irreducible Brillouin zone. It is obvious that the band structures in both the majority and the minority spin channels have intersections with the Fermi level, which indicates that Mn₂Sn compound is a metal with a magnetic moment of -0.19 μB. Therefore, the binary C1ᵦ-type Mn₂Sn compound can be regarded as a metallic ferrimagnet (MFi). Our results for the electronic structures are consistent with the previous research work of Fujii et al.⁶² Note that, in the work of Ref. 63, Mn₂Sn compound is predicted to be a HM-FCF. Namely, the Fermi level is located in the band gap in the minority-spin channel and has an intersection with the conduction band in the majority-spin channel. This is different from our results. The reason for this is that the lattice constant in Ref. 63 is smaller than ours and Fujii et al.'s, as mentioned above. In Fig. 4, we also present the spin-projected total and atomic DOS of Mn₂Sn compound. One can see that the partial DOS (PDOS) curves of Mn (A) and Mn (B) have opposite configurations. In the majority states of Mn (B) the bonding peak is far below the Fermi level and occupied, while in the minority states, the antibonding peak is far above the Fermi level and unoccupied. In contrast, for the PDOS of Mn (A), the unoccupied antibonding peak is far above the Fermi level in the majority spin band structure, and the occupied minority bonding peak is far below the Fermi level. Therefore, the two Mn atoms are opposite to each other and further contribute to an antiparallel alignment of their spin moments. The antiparallel alignment between the Mn (A) and Mn (b) moments of binary C1ᵦ-type Mn₂Sn compound can also be observed in Refs. 62, 63.

### 3.2 Effects of strain

In this section, we will focus on the strain effects on the magnetic properties and electronic structures of binary C1<sub>b</sub>-type Mn₂Sn compound. Note that the effects of strain can tune the electronic structures and magnetic properties to a large extent in many materials with different crystal structures, e.g. full-Heusler based Ti₂CrSi and Co₂CrGa compounds⁶⁴,⁶⁵, half-Heusler based NiMnSb compound⁶⁴, monolayer transition-metal dichalcogenides, and monolayer M₂X³³. First, we will study the effects of uniform strain on the total magnetic moment and the atomic spin magnetic moments of Mn (A), Mn (B), and Sn atoms. As shown in Fig. 5, we can see that the total magnetic moment of Mn₂Sn compound decreases to 0 μ<sub>B</sub> as the lattice constant decreases to 5.8 Å, and therefore, the metallic ferrimagnetism property of Mn₂Sn vanishes, and the fully-compensated ferrimagnetism property appears. Furthermore, the fully-compensated total magnetic moment of Mn₂Sn remains 0 μ<sub>B</sub> from 5.4 Å to 5.8 Å, and therefore, the fully-compensated ferrimagnetism property remains unchanged over this range. Within this range, the calculated total spin moment for Mn₂Sn agrees well with the Slater-Pauling curve $M_{\text{t}} = Z_{\text{t}}$-18²³. That is to say, there are 18 valence electrons in Mn₂Sn, which equally occupy the majority and minority spin bands. The atomic spin moments of Mn (A) and Mn (B) are quite sensitive to the value of the lattice constant. The absolute values of the atomic magnetic moments of Mn in the two different crystallographic sites decrease monotonically if the lattice is compressed. Also, the effects of tetragonal distortion on the total and the atomic magnetic moments of Mn₂Sn compound have been presented in Fig. 5. Obviously, both the total and the atomic magnetic moments exhibit a low sensitivity to tetragonal deformation. That is, the values of the total and atomic magnetic moments remain nearly unchanged over the whole range of $c/a$ = 0.75-1.25.

![](./images/811158924873957376_7.jpg)

Fig. 5 Calculated total and atom-resolved spin magnetic moments of Mn₂Sn as functions of the lattice constant (top) and of the $c/a$ ratio (bottom), respectively.

![](./images/811158924873957376_8.jpg)

Fig. 6 Different physical transitions under uniform strain and tetragonal distortion.

![](./images/811158924873957376_9.jpg)

Fig. 7 Mn₂Sn band structures at different lattice constants. (The blue and red lines denote the majority and minority spin band structures, respectively.)

We now analyse the effects of uniform strain and tetragonal distortion on the possible transitions in the physics of Mn₂Sn by comparing a simple schematic representation (see Fig. 6) and the electronic band structures (see Figs. 7 and 8). From the comparison, we observe that there is an interesting and novel transition in the physics from MFi → FCF-HM → FCF-SGS → FCF-S → FCF-HM → ZG-FCF-HM → MFi under a uniform strain. Nevertheless, the physics remains that of a metallic ferrimagnet and exhibits a low sensitivity to the tetragonalization. In detail, as the lattice constant is compressed in the range of 5.8-5.52 Å, the valence bands at the G-point in the majority-spin channel move down gradually, and an indirect band gap (G-X) occurs (see the example of Mn₂Sn at the lattice constant of 5.8 Å in Fig. 7), that is, MFi Mn₂Sn becomes a FCF-HM under a compressive uniform strain larger than -4.7% and smaller than -9.3%. In the lattice constant range from 5.52 Å to 5.50 Å, the conduction bands at the X-point in the minority-spin channel move up, and the X and the L points touch the Fermi level, whereas the indirect band gap G-X in the majority-spin channel is maintained.

Therefore, the HM-FCF Mn₂Sn becomes a FCF-SGS under a compressive uniform strain larger than -9.3% and smaller than -9.6%. In the lattice constant range from 5.5 Å to 5.46 Å, the conduction bands at the X-point in the minority-spin channel move up and above the Fermi level, and two indirect band gaps can be observed in both the majority and the minority spin channels. Therefore, the FCF-SGS Mn₂Sn becomes a FCF-S under a compressive uniform strain ranging from -9.6% to -10.3%. In the lattice constant range from 5.46 Å to 5.43 Å, the FCF-S becomes a FCF-HM again because the conduction bands at the X-point in the majority-spin channel move down and cross the Fermi level. Most importantly, as the lattice constant is compressed, the conduction bands at the X-point in the minority-spin channel move down slightly, and a zero gap (X-L) can be found in the minority-spin channel. In the majority-spin channel, however, the conduction bands at the X-point also cross the Fermi level, and therefore, FCF-HM becomes a ZG-FCF-SGS. As shown in Fig. 8, however, the binary Mn₂Sn compound remains MFi under the tetragonalization from -25%

to 25% because the bands in both the majority and the minority spin channels cross the Fermi level.

The reason for the transitions in the physics of Mn₂Sn under uniform strain is mainly due to the different $d$-$d$ hybridization between the bonding $t_{2g}$ and the antibonding $e_g$ states of Mn atoms. In detail, because Mn (A) and Mn (B) form a diamond structure, $d$-orbitals of Mn (A) and Mn (B) split into the double degenerate orbitals $d_z^2$, $d_{x^2-y^2}$, and the triple degenerate orbitals $d_{xy}$, $d_{yx}$, $d_{zx}$. Then, the double degenerate orbitals $d_z^2$, $d_{x^2-y^2}$ of Mn (A) can only couple to those of Mn (B), resulting in double degenerate bonding orbitals denoted as $2e_g$ and double degenerate antibonding orbitals $2e_g$. Similar to the case of the degenerate orbitals $d_z^2$, $d_{x^2-y^2}$, the triple degenerate orbitals $d_{xy}$, $d_{yx}$, $d_{zx}$ of Mn (A) couple to those of Mn (B), resulting in triple degenerate bonding orbitals denoted as $3t_{2g}$ and triple degenerate antibonding orbitals $3t_{2g}$. The bonding orbitals have lower energy, and the antibonding have higher energy. Furthermore, the energy of the crystal field splitting of the bonding and antibonding states is $E(e_g) < E(t_{2g})$ because each Mn site is in the centre of a Mn tetrahedron. Therefore, the bonding $t_{2g}$ and antibonding $e_g$ states are near the Fermi level. If the lattice constant is decreased, the $d$-$d$ hydrization between Mn atoms will be decreased, and thus, the bonding $t_{2g}$ and antibonding $e_g$ states will be influenced. The change in the $e_g$-$t_{2g}$ states will cause the band structure of Mn₂Sn to change near the Fermi level, and furthermore, the physics of Mn₂Sn will change according to the different electronic band structures.

Note that this is the first time that FCF-SGS and ZG-FCF-HM transitions have been found in a Heusler compound. Due to the interesting and novel physics, namely, the half-metallic, fully-compensated ferrimagnetic, spin-gapless semiconducting, and even zero-gap half-metallic characteristics, binary C1_b-type Heusler Mn₂Sn compound would be useful in spintronic applications.

![](./images/811158924873957376_10.jpg)

Fig. 8 Mn₂Sn band structures with different $c/a$ ratios. (The blue and red lines denote the majority and minority spin band structures, respectively.)

**Table 2** Elastic constants $C_{ij}$, bulk modulus $B$, shear modulus $G$, Young's modulus $E$ (GPa), and Pugh's ratio $B/G$ for the hypothetical binary C1$_b$-type Heusler compound Mn$_2$Sn.

<table>
  <thead>
    <tr>
      <th>compound</th>
      <th>$C_{11}$</th>
      <th>$C_{12}$</th>
      <th>$C_{44}$</th>
      <th>$B$</th>
      <th>$G$</th>
      <th>$E$</th>
      <th>$B/G$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mn$_2$Sn</td>
      <td>100.93905</td>
      <td>53.01055</td>
      <td>37.32205</td>
      <td>68.98672</td>
      <td>31.97893</td>
      <td>62.45876</td>
      <td>2.15725542</td>
    </tr>
  </tbody>
</table>

**Table 3** Bulk modulus $B$, shear modulus $G$, Young's modulus $E$ (GPa), and Pugh's ratio $B/G$ for Mn$_2$CoAl, Mn$_2$Sn, and NiVSb.

<table>
  <thead>
    <tr>
      <th>compounds</th>
      <th>$B$</th>
      <th>$G$</th>
      <th>$E$</th>
      <th>$B/G$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mn$_2$Sn</td>
      <td>68.986</td>
      <td>31.978</td>
      <td>62.458</td>
      <td>2.157</td>
    </tr>
    <tr>
      <td>Mn$_2$CoAl</td>
      <td>185.778$^\text{a}$</td>
      <td>77.782$^\text{a}$</td>
      <td>204.768$^\text{a}$</td>
      <td>2.389$^\text{a}$</td>
    </tr>
    <tr>
      <td>NiVSb</td>
      <td>94.073$^\text{b}$</td>
      <td>30.814$^\text{b}$</td>
      <td>83.343$^\text{b}$</td>
      <td>3.053$^\text{b}$</td>
    </tr>
  </tbody>
</table>

$^\text{a}$ Ref. [67]; $^\text{b}$ Ref. [68].

### 3.3 Structural stability

It is well accepted that the elastic constant can help us to understand the mechanical properties and also provide very useful information to estimate the hardness of materials. As mentioned above, the elastic constants $C_{ij}$ and some other important information can be obtained from ground-state total energy calculations. Importantly, the $C_{ij}$ can also be used to test the phase stability of the binary Mn$_2$Sn compound. For cubic crystals, the traditional mechanical stability conditions are given by Born and Huang$^{66}$:

$$
c_{44}>0,\frac{(c_{11}-c_{12})}{2},B=\frac{(c_{11}+2c_{12})}{3}>0,c_{12}<B<c_{11}. \tag{8}
$$

From Table 2, the calculated three independent elastic constants obey the generalized elastic stability criteria given by Born and Huang, reflecting the mechanical stability of the binary C1$_b$-type Heusler compound Mn$_2$Sn.

Furthermore, we have collected the elastic properties of Mn$_2$CoAl (SGS) and NiVSb in Table 3. From it, one can see that the calculated Young's modulus $E$ for Mn$_2$Sn is 62.458 GPa, which is smaller than those for Mn$_2$CoAl (204.768 GPa) and NiVSb (83.343 GPa). The Young's modulus of a material is the usual property used to characterize stiffness. The higher the value of $E$, the stiffer is the material. That is, the relative stiffness order is Mn$_2$CoAl > NiVSb > Mn$_2$Sn. In order to predict the brittle or ductile behaviour of materials, Pugh proposed an approximate criterion using the ratio of $B/G$. Normally, the $B/G$ ratio is larger than 1.75 for ductile materials and less than 1.75 for brittle materials. From Table 3, one can observe that the obtained $B/G$ ratios for Mn$_2$Sn, Mn$_2$CoAl, and NiVSb are all larger than 1.75, suggesting that the three materials are all ductile. The relative ductility order is NiVSb > Mn$_2$CoAl > Mn$_2$Sn.

We should also test the stability of Mn$_2$Sn by calculating its cohesion energy and formation energy. The cohesion energy ($E_c$) is a measure of the strength of the force that binds atoms together in the solid state, which is correlated with the structural stability in the ground state. The cohesion energy of Mn$_2$Sn compound per formula unit can be calculated by

$$
E_c=2E_{Mn}^{iso}+E_{Sn}^{iso}-E_{Mn_2Sn}^{total}, \tag{9}
$$

where $E_{Mn_2Sn}^{total}$ is the equilibrium total energy calculated from first principles of the Mn$_2$Sn alloy per formula unit, and $E_{Mn}^{iso}$ and $E_{Sn}^{iso}$ are the energies of isolated Mn and Sn atoms, respectively. The calculated value of the cohesion energy is 19.13 eV. Such high cohesion energy indicates that Mn$_2$Sn crystal is expected to be stable due to the high energy of the chemical bonds.

On the other hand, the formation energy indicates the stability of the compound in regards to decomposition into its bulk constituents. The formation energy is calculated using the formula:

$$
E_f=E_{Mn_2Sn}^{total}-\left[2E_{Mn}^{bulk}+E_{Sn}^{bulk}\right], \tag{10}
$$

where $E_{Mn}^{bulk}$ and $E_{Sn}^{bulk}$ correspond to the total energy per atom for the Mn and Sn bulks, respectively. The calculated formation energy is -2.715 eV, which indicates that the C1$_b$-type Heusler Mn$_2$Sn compound is thermodynamically stable due to its negative formation energy.

### 4. Conclusions and outlook

In summary, FCF-SGSs and ZG-HM-FCFs have received considerable interest in the fields of solid-state chemistry and physics, as well as materials science, due to their potential applications in novel spintronic devices. In this paper, we have employed first-principles calculations to investigate the structural, electronic, elastic, and magnetic properties of the

binary C₁ᵦ-type Heusler compound Mn₂Sn. We find that the Mn₂Sn behaves as a MFi at the equilibrium lattice constant and becomes ZG-HM-FCF, FCF-SGS, FCF-HM, and FCF-S under a uniform strain. The metallic ferrimagnetism property of Mn₂Sn is maintained under a tetragonal distortion, however. Mn₂Sn compound is stable from the aspects of mechanical properties, cohesion energy, and formation energy, and therefore, this compound could be synthesized experimentally. Moreover, the total magnetic moment of Mn₂Sn decreases from -0.197 μᵦ to 0 μᵦ as the lattice constant decreases to 5.8 Å. The zero total moment comes from the antiparallel Mn spin moments and also obeys the Slater-Pauling rule: Mₜ = Zᵣ-18.

The search for ZG-FCF-HMs and FCF-SGSs has attracted ever-increasing attention in terms of materials design for spintronic applications. To the best of our knowledge, very recently, some materials, e.g. the full-Heusler-based compounds Zr₂MnAl and Ti₂CrSi²⁴,⁶⁵, monolayer Ti₂C³³, and hybrid C/BN nanoribbon²⁹ can be tuned into the SGS/FCF-SGS state by strain engineering. Furthermore, in our current work, a FCF-SGS and a ZG-FCF-HM transition have been predicted, based on the C₁ᵦ-type Heusler compound Mn₂Sn for the first time. Based on recent works by us and other authors, we suggest that strain engineering could be an effective approach to achieve SGS/FCF-SGS or ZG-HM/ZG-FCF-HM states. We also hope that the method of strain engineering can be widely applied to the design of new kinds of SGS and ZG-HM materials with Heusler-type structures or other structures. Experimental realizations of these compounds and these novel and interesting states are imminent.

## Acknowledgements

Many thanks are owed to Dr Tania Silver for critical reading of the manuscript. Zhenxiang Cheng thanks the Australian Research Council for support. Xiaotian Wang is grateful for financial support from the China Scholarship Council and the Graduate-level Innovation Project funded by Hebei Province. Guodong Liu acknowledges financial support from Chongqing City Funds for Distinguished Young Scientists (No. cstc2014jcyjjq50003) and the Program for Leading Talents in Science and Technology Innovation of Chongqing City (No. cstckjcxljrc19).

## References

1 R. A. de Groot, F. M. Mueller, P. G. Van Engen and K. H. J. Buschow, *Phys. Rev. Lett.*, 1983, **50**, 2024.
2. H. C. Kandpal, G. H. Fecher and C. Felser, *J. Phys. D: Appl. Phys.*, 2007, **40**, 6.
3. I. Galanakis, P. Mavropoulos and P. H. Dederichs, *J. Phys. D: Appl. Phys.*, 2006, **39**, 5.
4. M. Benkabou, H. Rached, A. Abdellaoui, D. Rached, R. Khenata, M. H. Elahmar, B. Abidri, N. Benkhettou and S. Bin-Omran, *J. Alloys Compd.*, 2015, **674**, 276-286.
5. I. Galanakis, K. Özdoğan, E. Şaşıoğlu and B. Aktaş, *Phys. Rev. B*, 2007, **75**, 172405.
6. R. Weht and W. E. Pickett, *Phys. Rev. B*, 1999, **60**, 13006.
7. X. T. Wang, Z. X. Cheng, J. L. Wang, L. Y. Wang, Z. Y. Yu, C. S. Fang, J. T. Yang and G. D. Liu, *RSC Adv.*, 2016, **6**, 57041-57047.
8. I. Galanakis, P. H. Dederichs and N. Papanikolaou, *Phys. Rev. B*, 2002, **66**, 174429.
9. T. Graf, C. Felser and S. S. P. Parkin, *Prog. Solid State Chem.*, 2011, **39**, 1-50.
10. G. Y. Gao, L. Hu, K. L. Yao, B. Luo and N. Liu, *J. Alloys Compd.*, 2013, **551**, 539-543.
11. J. Chen, G. Y. Gao, K. L. Yao and M. H. Song, *J. Alloys Compd.*, 2011, **509**, 10172-10178.
12. N. Kervan and S. Kervan, *J. Magn. Magn. Mater.*, 2012, **324**, 645-648.
13. E. Şaşıoğlu, L. M. Sandratskii, P. Bruno and I. Galanakis, *Phys. Rev. B*, 2005, **72**, 184415.
14. K. Özdogan, I. Galanakis, E. Şaşıoğlu and B. Aktaş, *J. Phys.: Cond. Matt.*, 2006, **18**, 2905.
15. L. Bainsla and K. G. Suresh, *Appl. Phys. Rev.*, 2016, **3**, 031101.
16. I. Zutic, J. Fabian and S. D. Sarma, *Rev. Mod. Phys.*, 2004, **76**, 323.
17. H. van Leuken and R. A. de Groot, *Phys. Rev. Lett.*, 1995, **74**, 1171.
18. X. Xu, *Adv. Mater.*, 2012, **24**, 294-298.
19. I. Galanakis, K. Ozdogan, E. Sasioglu and B. Aktas, *Phys. Rev. B.*, 2007, **75**, 092407.
20. X. L. Wang, *Phys. Rev. Lett.*, 2008, **100**, 156404.
21. X. L. Wang, S. X. Dou and C. Zhang, *NPG Asia Materials*, 2010, **2**, 31-38.
22. X. L. Wang, G. Peleckis, C. Zhang, H. Kimura and S. X. Dou, *Adv. Mater.*, 2009, **21**, 2196-2199.
23. X. T. Wang, Z. X. Cheng, J. L. Wang, X. L. Wang and G. D. Liu, *J. Mater. Chem. C*, 2016, DOI: 10.1039/c6tc01343k.
24. X. T. Wang, Z. X. Cheng, J. L. Wang, H. Rozale, L. Y. Wang, Z. Y. Yu, J. T. Yang and G. D. Liu, *J. Alloys Compd.*, 2016, **686**, 549-555.
25. L. Y. Wang, X. T. Wang, R. K. Guo, T. T. Lin and G. D. Liu, *Solid State Commun.*, 2016, **244**, 38-42.
26. S. B. Tang and X. R. Cao, *Phys. Chem. Chem. Phys.*, 2014, **16**, 23214-23223.
27. Y. F. Li, Z. Zhou, P. W. Shen and Z. F. Chen, *ACS Nano*, 2009, **3**, 1952-1958.
28. J. Guan, W. Chen, Y. F. Li, G. T. Yu, Z. M. Shi, X. R. Huang, C. Sun and Z. F. Chen, *Adv. Funct. Mater.*, 2013, **23**, 1507-1508.
29. S. Zhu and T. Li, *Phys. Rev. B*, 2016, **93**, 115401.
30. J. He, P. Zhou, N. Jiao, L. Z. Sun, X. Chen and W. Lu, *Half-Semiconductor Antiferromagnets and Spin-Gapless-Semiconductor Antiferromagnets*, *e-print arXiv:1308.0253*.
31. S. D. Guo and B. G. Liu, *J. Phys.: Condens. Matter*, 2012, **24**, 045502.
32. Y. Pan and Z. Yang, *Phys. Rev. B*, 2010, **82**, 195308.
33. G. Y. Gao, G. Q. Ding, J. Li, K. L. Yao, M. H. Wu and M. C. Qian, *Nanoscale*, 2016, **8**, 8986-8994.
34. H. Y. Jia, X. F. Dai, L. Y. Wang, R. Liu, X. T. Wang, P. P. Li, Y. T. Cui and G. D. Liu, *AIP Adv.*, 2014, **4**, 047113.
35. K. Özdoğan, E. Şaşıoğlu and I. Galanakis, *J. Appl. Phys.*, 2013, **113**, 193903.

36. G. Y. Gao and K. L. Yao, *Appl. Phys. Lett.*, 2013, **103**, 232409.

37. X. Yang, X. Wu, B. Wu, Y. Feng, P. Li and H. Huang, *Mat. Sci. Eng. B: Solid*, 2016, **209**, 45-50.

38. Q. Gao, H. H. Xie, L. Li, G. Lei, J. Deng and X. Hu, *Superlattice. Microst.*, 2015, **85**, 536-542.

39. S. Skaftouros, K. Özdoğan, E. Şaşıoğlu and I. Galanakis, *Appl. Phys. Lett.*, 2013, **102**, 022402.

40. D. H. Kim, J. Hwang, E. Lee, K. J. Lee, S. M. Choo, M. H. Jung, J. Baik, H. J. Shin, B. Kim, K. Kim, B. I. Min and J.-S. Kang, *Appl. Phys. Lett.*, 2014, **104**, 022411.

41. S. M. Choo, K. J. Lee, S. M. Park, J. B. Yoon, G. S. Park, C. Y. You and M. H. Jung, *Appl. Phys. Lett.*, 2015, **106**, 172404.

42. S. Ouardi, G. H. Fecher and C. Felser, *Phys. Rev. Lett.*, 2013, **110**, 100401.

43. Y. J. Zhang, Z. H. Liu, E. K. Liu, G. D. Liu, X. Q. Ma and G. H. Wu, *EPL*, 2015, **111**, 37009.

44. A. Birsan and V. Kuncser, *J. Magn. Magn. Mater.*, 2016, **406**, 282-288.

45. H. Y. Jia, X. F. Dai, L. Y. Wang, R. Liu, X. T. Wang, P. P. Li, Y. T. Cui and G. D. Liu, *J. Magn. Magn. Mater.*, 2014, **367**, 33-39.

46. W. Feng, X. Fu, C. Wan, Z. Yuan, X. Han, N. Van Quang and S. Cho, *Phys. Status Solidi RRL*, 2015, **9**, 641-645.

47. H. Z. Luo, Y. P. Xin, B. H. Liu, F. B. Meng, H. Y. Liu, E. K. Liu and G. H. Wu, *J. Alloys Compd.*, 2016, **665**, 180-185.

48. Y. Du, G. Z. Xu, X. M. Zhang, Z. Y. Liu, S. Y. Yu, E. K. Liu, W. H. Wang and G. H. Wu, *EPL*, 2013, **103**, 37011.

49. K. Özdoğan, E. Şaşıoğlu and I. Galanakis, *Comput. Mater. Sci.*, 2015, **110**, 77-82.

50. H. Kurt, K. Rode, P. Stamenov, M. Venkatesan, Y. C. Lau, E. Fonda and J. M. D. Coey, *Phys. Rev. Lett.*, 2014, **112**, 027201.

51. M. C. Payne, M. P. Teter, D. C. Allan, T. A. Arias and J. D. Joannopoolous, *Rev. Mod. Phys.*, 1992, **64**, 1065.

52. M. D. Segall, P. L. D. Lindan, M. J. Probert, C. J. Pickard, P. J. Hasnip, S. J. Clark and M. C. Payne, *J. Phys.: Cond. Matt.*, 2002, **14**, 2717.

53. D. Vanderbilt, *Phys. Rev. B*, 1990, **41**, 7892

54. J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865.

55. T. Block, M. J. Carey, B. A. Gurney and O. Jepsen, *Phys. Rev. B*, 2004, **70**, 205114.

56. M. Singh, H. S. Saini, J. Thakur, A. H. Reshak and M. K. Kashyap, *J. Alloys Compd.*, 2013, **580**, 201-204.

57. J. H. Wang, J. Li, S. Yip, S. Phillpot and D. Wolf, *Phys. Rev. B*, 1995, **52**, 12627.

58. G. V. Sin'ko and N. A. Smirnov, *J. Phys.: Condens. Matter*, 2002, **14**, 6989.

59. M. Prikhodko, M. S. Miao and W. R. Lambrecht, *Phys. Rev. B*, 2002, **66**, 125201.

60. R. Hill, *Proc. Phys. Soc. Lond. A*, 1952, **65**, 349.

61. A. F. Young, C. Sanloup, E. Gregoryanz, S. Scandolo, R. J. Hemley and H. K. Mao, *Phys. Rev. Lett.*, 2006, **96**, 155501.

62. S. Fujii, S. Ishida and S. Asano, *J. Phys. Soc. Jpn.*, 2010, **79**, 124702.

63. H. Z. Luo, G. D. Liu, F. B. Meng, W. H. Wang, G. H. Wu, X. X. Zhu and C. B. Jiang, *Physica B*, 2011, **406**, 4245.

64. A. van de Walle and G. Ceder, *Phys. Rev. B*, 1999, **59**, 14992.

65. L. Wang and Y. J. Jin, *J. Magn. Magn. Mater.*, 2015, **385**, 55-59.

66. M. Born and K. Huang, *Dynamical Theory of Crystal Lattices*, Clarendon, Oxford, 1954.

67. X. R. Chen, M. M. Zhong, Y. Feng, Y. Zhou, H. K. Yuan and H. Chen, *Phys. Status Solidi B*, 2015, **252**, 2830-2839.

68. J. B. Gu, C. J. Wang, Y. Cheng, L. Zhang, L. C. Cai and G. F. Ji, *Comput. Mater. Sci.*, 2015, **96**, 72-80.

---

This journal is © The Royal Society of Chemistry 20xx

*J. Name.*, 2013, **00**, 1-3 | **11**

# Graphical Abstract

![](./images/811158924873957376_11.jpg)