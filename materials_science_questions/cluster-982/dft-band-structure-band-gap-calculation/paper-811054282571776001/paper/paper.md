# RSC Advances

PAPER
View Article Online
View Journal | View Issue

![](./images/811054282571776001_1.jpg)
Cite this: RSC Adv., 2017, 7, 14262

# The driving force for forming As-As bonding and its effect on the electronic structures and the thermoelectric properties of Zintl $Ca_{5} M_{2} As_{6}$ (M = Sn, Ga)

Dong Bao Luo and Yuan Xu Wang*

By using first-principles method, we studied the relation between the arrangement of the $MPn_{4}$ chains and the electronic structures for Zintl $Ca_{5} M_{2} As_{6}$ (M = Sn and Ga) compounds. It was found that the connecting forms between the adjacent chains in $Ca_{5} M_{2} As_{56}$ play a key role in determining their thermoelectric properties. The appearing of As-As bonding or not between adjacent covalent $MAs_{4}$ chains mainly depends on the different electron configuration between Pn and Ga (or Sn). Such As-As bonding in $Ca_{5} Ga_{2} As_{6}$ results in a sharp peak of density of states near the conduction band minimum, which will dramatically increase its n-type Seebeck effect. Moreover, the calculated band decomposed charge density demonstrates that the As-As bonding leads to a high charge accumulating along the $y$-direction for n-type $Ca_{5} Ga_{2} As_{6}$. Combined with the high electrical conductivity along the covalent anion chain direction, a high electrical conductivity may exist in n-type polycrystal of $Ca_{5} Ga_{2} As_{6}$. On the other hand, the absence of As-As bonding in $Ca_{5} Sn_{2} As_{6}$ results in a sharp peak of density of states near the valence band maximum, which can enhance its p-type Seebeck effect. For $Ca_{5} Sn_{2} As_{6}$, the small anisotropy of electrical conductivity may induce the high electrical value for its p-type polycrystal. Consequently, polycrystalline n-type $Ca_{5} Ga_{2} As_{6}$ and p-type $Ca_{5} Sn_{2} As_{6}$ may have good thermoelectric performance.

Received 17th January 2017
Accepted 23rd February 2017
DOI: 10.1039/c7ra00718c
rsc.l/rsc-advances

## I. Introduction

As pollution-free energy materials, thermoelectric materials have drawn more and more attentions. The thermoelectric efficiency of a material is governed by its figure of merit $ZT = S^{2}\sigma T/\kappa$, where $S$, $\sigma$, $T$, and $\kappa$ are the Seebeck coefficient, electrical conductivity, absolute temperature, and thermal conductivity (a sum of the electronic $(\kappa_{e})$ and lattice $(\kappa_{l})$ contributions), respectively. $^{1}$ A good thermoelectric material requires large $S$, $\sigma$, and low $\kappa$, simultaneously. However, $S$ and $\sigma$ have an opposite dependence on carrier concentration, which hinders the wide application of thermoelectric materials. Besides, the reduction of $\kappa$ usually causes the decrease of electronic mobility. Thus, ideally engineered thermoelectric materials should exhibit "phonon glass, electron crystal" behavior with high mobility and low lattice thermal conductivity, simultaneously. $^{2}$ It is very important to find methods to meet the specified conditions.

Zintl phases are prime candidates for applying the concept to obtain high $ZT$ thermoelectric materials. $^{2}$ For example, high thermoelectric efficiency has been demonstrated by a number of Zintl phases, such as $Yb_{14}MnSb_{11},^{3}$ $Ca_{3}AlSb_{3},^{4}$ $Sr_{3}AlSb_{3},^{5}$ $Sr_{3}GaSb_{3}.^{6}$ The excellent performance of these thermoelectric materials benefits from their complex crystal structures and unique electronic structures, which leads to a high electrical conductivity and a low lattice thermal conductivity. $^{7-10}$ Among the rich chemistry of Zintl compounds, $A_{5}M_{2}Pn_{6}$ (A = divalent alkaline-earth or rare-earth metals; M = triels; Pn = pnictogen elements) are considered as promising thermoelectric materials. One typical feature of these compounds is one- dimensional anion chains formed by $MPn_{4}$ tetrahedra. Such covalent polyanion chains have an important effect on their electronic structures and thermoelectric properties. For example, in $Ca_{5}Al_{2}Sb_{6},^{11}$ the lightest band mass is parallel to the chains of corner-linked $AlSb_{4}$, indicating a high electrical conductivity along this direction.

More interestingly, according to the connecting form of the chains, $A_{5}M_{2}Pn_{6}$ compounds can be divided into two types: first, the adjacent polyanion chains are connected by Pn-Pn dimers in $Ca_{5}Ga_{2}As_{6}$ structure type; $^{12}$ second, there is no Pn-Pn bonding in the structure of $Ca_{5}Sn_{2}As_{6}$ type. $^{13}$ The thermoelectric properties of the first $A_{5}M_{2}Pn_{6}$ type has been discussed by Alexandra Zevalkink $^{14}$ and many other researchers. They reported that the first $A_{5}M_{2}Pn_{6}$ type compounds exhibit excellent thermoelectric properties by p-type doping. The second type has the similar topology along the $c$-direction with the first type one, which may also be potential thermoelectric materials. For

Institute for Computational Materials Science, School of Physics and Electronics, Henan University, Kaifeng 475004, People's Republic of China. E-mail: wangyx@henu.edu.cn

14262 | RSC Adv., 2017, 7, 14262-14271
This journal is © The Royal Society of Chemistry 2017

example, the figure of merit of Eu₅Sn₂As₆ (the second structure type) is comparable to that of undoped Ca₅Al₂Sb₆ (the first structure type).¹⁵ However, the effect of formatting Pn-Pn bond or not on the electronic structures and the transport properties of A₅M₂Pn₆ is still an open question. This inspires us to investigate the relationships between the arrangement of MPn₄ chains, the electronic structures, and the thermoelectric properties. A₅Sn₂As₆ (A = Ca and Sr) and Ca₅Ga₂As₆ structures are good candidates for trying to ascertain Zintl structure-properties relationship between the first and second structure type. If so, the mechanisms for the high thermoelectric performance in Ca₅M₂As₆ may be uncovered.

In this work, we find that the appearing of As-As bonding or not between adjacent covalent chains mainly depends on the different electron configuration between Pn and Ga (or Sn). By using the first-principles calculations combined with the semiclassical Boltzmann transport theory, we studied the effect of As-As bonding on the thermoelectric transport behavior. Our results demonstrate that the appearing of As-As bonding or not plays a key role on affecting the Seebeck effect and the anisotropy of electrical conductivity. Such As-As bonding in Ca₅Ga₂As₆ results in a sharp peak of density of states near the bottom of the conduction bands, which will dramatically increase its n-type Seebeck effect. Moreover, the calculated band decomposed charge density of Ca₅Ga₂As₆ shows that the As-As bonding leads to a high charge accumulating along the bonding direction. Combined with the high electrical conductivity along the covalent anion chain direction, small anisotropy of electrical conductivity indicates a high electrical value for its n-type polycrystal. Hence, polycrystalline Ca₅Ga₂As₆ may have excellent thermoelectric performance by n-type doping. On the other hand, when there is no formation of As-As bonding in Ca₅Sn₂As₆, the electrons gathered around the As atoms produce a sharp peak of density of states near the top of the valence bands, which will largely enhance its p-type Seebeck effect. Moreover, small anisotropy of the electrical conductivity indicates a high electrical value for p-type polycrystal. Thus, the thermoelectric properties of polycrystalline Ca₅Sn₂As₆ may be enhanced by p-type doping.

## II. Computational detail

Vienna Ab initio Simulation Package (VASP)¹⁶ based on the projector augmented wave (PAW) method¹⁷ was utilized to optimize the geometry. We used the Perdew-Burke-Ernzerhof (PBE) generalized-gradient approximation (GGA)¹⁸ to describe the exchange-correlation function. Plane-wave cutoff energy was 450 eV and the energy convergence criterion was chosen to be 10⁻⁵ eV. The Hellmann-Feynman forces on each ion are less than 0.02 eV Å⁻¹, and the Brillouin zones of the unit cells were represented by the Monkhorst-Pack special *k*-point scheme with 5 × 4 × 14 and 4 × 4 × 12 grid meshes for Ca₅Sn₂As₆ and Ca₅Ga₂As₆, respectively.

The electronic structures were calculated by the full potential-linearized augmented plane wave (FLAPW) methods¹⁹ based on the density functional theory (DFT).²⁰,²¹ The modified Becke-Johnson (MBJ)²²,²³ semi-local exchange was employed to improve the band gap, as implemented in the WIEN2k.²⁴⁻²⁶ The *k* points of self-consistent calculations are 1000 in the Brillouin zone. The thermoelectric transport properties were calculated through the semiclass Boltzmann theory and rigid band approach, which were implemented in the BoltzTrap code.²⁷ With the Boltzmann theory, the constant scattering time approximation is used. This approximation, which is commonly applied for metals and degenerately doped semiconductors, is based on the assumption that the scattering time determining the electrical conductivity does not vary strongly with energy on the scale of *kT*. It does not involve any assumption about the possibly strong doping and temperature dependence of *τ*. In this way, Seebeck coefficient *S* does not dependent on relaxation time (*τ*), while the electrical conductivity *σ* and *κ*ₑ can only be evaluated with respect to the parameter (*τ*).

## III. Results and discussions

### A. Lattice structure and stability

Each optimized Ca₅Sn₂As₆ unit cell contains 26 atoms shown in Fig. 1(c), which is orthorhombic with the space group of *pbam* and belongs to Sr₅Sn₂P₆ structure type. The optimized lattice constants are $a = 11.83\ \mathring{\text{A}}$, $b = 13.64\ \mathring{\text{A}}$, and $c = 4.12\ \mathring{\text{A}}$. As seen in Fig. 1(b), there are chains of corner-shared SnAs₄ tetrahedron along the *z*-direction, which is similar to the infinite chains of corner-shared GaAs₄ tetrahedron along the same direction in Ca₅Ga₂As₆. However, there is no As-As bonding between the chains in Ca₅Sn₂As₆, which is different from Ca₅Ga₂As₆. As can be seen from Fig. 1(b) and (c), the optimized crystal structure of Ca₅Sn₂As₆ is composed of infinite chains of corner-shared SnAs₄ tetrahedron along the *c*-axis that is separated by Ca atoms. The As atoms have three non-equivalent positions, labeled as As1, As2, and As3. The structure along the *c*-axis is different from that along the *a*- and *b*-axis, which may induce a strong anisotropic transport properties along the three directions. In addition, the crystal structures of Ca₅Sn₂As₆ and Sr₅Sn₂As₆ are isomorphic with the different cations. As we know, the crystal structure determines its properties. It is worth investigating the relationship between the structure and transport properties of A₅Sn₂As₆ (A = Ca, Sr) and Ca₅Ga₂As₆.

The stability of Ca₅M₂As₆ (M = Sn, Ga) can be judged from their phonon frequency and formation energy. Dynamic stability is important for existing of a new structure because the appearance of soft phonon modes will lead to its distortion. The phonon dispersion curves of Ca₅M₂As₆ were calculated, as shown in Fig. 2. As seen from this figure, there is no imaginary phonon frequency at any of the wave vectors, which shows that they are dynamically stable. On the other hand, the formation energy is a more direct evidence of the stability of a material, which can be estimated from the following:

$$
\Delta E = E_{(\text{A}_5\text{M}_2\text{Pn}_6)} - 5E_{(\text{A})} - 2E_{(\text{M})} - 6E_{(\text{Pn})}, \tag{1}
$$

where $E_{(\text{A}_5\text{M}_2\text{Pn}_6)}$ is the total energy of A₅M₂Pn₆ at its most stable states. $E_{(\text{A})}$, $E_{(\text{M})}$, and $E_{(\text{Pn})}$ are the total energy per atom of A, M, and Pn, respectively. The calculated formation energy is

![](./images/811054282571776001_2.jpg)

Fig. 1 The chain of corner-shared (a) GaAs₄ (b) SnAs₄ tetrahedron along the c axis for Ca₅Ga₂As₆ and Ca₅Sn₂As₆, respectively. (c) The optimized crystal structure of Ca₅Sn₂As₆. Anthracite, red, and green spheres represent Ca, As, and Sn (Ga in (a)) atoms, respectively.

−11.29 eV for Ca₅Sn₂As₆, which is slight larger than that of Ca₅Ga₂As₆ (−11.35 eV). Thus, those compounds are very stable.

### B. Electronic structure
To check the difference in the bonding feature of Ca₅Sn₂As₆ and Ca₅Ga₂As₆, we calculated their electron localization function (ELF) and display it in Fig. 3 (the isosurface level of the two compounds are 0.79 and 0.77, respectively.). From Fig. 3(a), a certain degree of charge accumulation occurs midway between Sn and As atoms, suggesting that the Sn–As bonds have significant covalent character. More diffuse regions of charge between As and Ca atoms indicate their ionic bonding features. According to the characteristic infinite chains of lattice structure along the z-direction, Ca₅Sn₂As₆ is expected to have a high electron mobility along the As–Sn–As covalent bonding chains. Ca₅Ga₂As₆ has been reported to have high electrical conductivity along the z-direction due to its one-dimensional lattice structure.²⁸ Consistent with the lattice structure of Ca₅Ga₂As₆, there are some electrons between As1 atoms. Moreover, when the isosurface level is less 0.7, the adjacent GaAs₄ chains are shown to be markedly connected by electrons between the As1 atoms, indicating strong covalent As–As bonding. The forming of As–As bond or not in Ca₅Sn₂As₆ may be related to the electronic effect.

Classical Zintl phases are always considered to be valence precise semiconductors. Then, electron counting can analyse the structural difference between Ca₅Sn₂As₆ and Ca₅Ga₂As₆. Ca₅Sn₂As₆ consists of 5 Ca atoms and 2 covalent SnAs₃ repeat units, and the 5 Ca atoms donate 10 electrons. In polyanionic SnAs₃, to form 4 covalent bonds with adjoining 4 As, Sn brings 4 electrons to the table and is formally neutral. In addition, the two non-corner sharing As atoms need other 4 electrons and the one corner sharing As atom needs other 1 electron to fill octet rule. We thus conclude the SnAs₃ unit requires 5 electrons to satisfy valence. With two tetrahedra per formula unit, we achieve a net cation charge of +10 and polyanionic charge of −10. Valence satisfied and a semiconductor results. There are some difference shown in Ca₅Ga₂As₆. For covalent GaAs₃ repeat unit, Ga brings 4 electrons to form 4 covalent bonds with adjoining 4 As atoms, and is formally −1 from a covalent charge counting

![](./images/811054282571776001_3.jpg)

Fig. 2 Phonon dispersion curves of Ca₅M₂As₆ (M = Sn, Ga).

![](./images/811054282571776001_4.jpg)

Fig. 3 Calculated electron localization function of (a) $Ca_5Sn_2As_6$ and (b) $Ca_5Ga_2As_6$. The isosurface value are 0.79 and 0.77, respectively.

perspective. In the polyanion, there are 3 unique As atoms. For satisfying the octet rule, the non-corner sharing As needs other 2 electrons, and the corner sharing As needs other one electron, and the bridging As also needs additional one electron. Thus, the two $GaAs_3$ units per formula unit require 10 electrons to satisfy valence, which are corresponding to the 10 electrons donated by 5 Ca atoms. If $Ca_5Ga_2As_6$ formed in a chain structure without bridging bonds, the anion chains would require an additional electron per $GaAs_3$. In response, an additional Ca would be required. In fact, this yields the known $Ca_6Ga_2As_6$ structure, which is more commonly called the $Ca_3GaAs_3$. Thus, the difference in electron count between Ga and Sn determines the structural shift between $Ca_5Ga_2As_6$ and $Ca_5Sn_2As_6$. On the other hand, the structural changes can also be understood from the perspective of electronegativity. Here, we hope to use the ratio of the electronegativity of Pn to that of M to describe the electronegativity of polyanion $MPn_4$ tetrahedron for $A_5M_2Pn_6$. Table 1 lists the electronegativity values of related elements and polyanion $MPn_4$. For $Ca_5Ga_2As_6$ structure type with Pn-Pn bonding, the electronegativity ratios of $Ca_5Ga_2As_6$ (1.13), $Ca_5Al_2Sb_6$ (1.27), $Ca_5Ga_2Sb_6$ (1.13), $Ca_5In_2Sb_6$ (1.15), are above 1.13. For the $Sr_5Sn_2P_6$ structure type without Pn-Pn bonding, the electronegativity ratios of $Sr_5Sn_2P_6$ (1.12) and $Ca_5Sn_2As_6$ (1.11) are less than 1.12. Thus, the electronegativity of $MPn_4$ plays a key role for forming As-As dimmer bridging two adjacent $GaAs_4$ tetrahedron chains. In the case of the equal number of cations in different cells, when the electronegativity ratio is large, the anionic group can obtain more electrons from other atoms, which leads to the smaller cell volume of $Ca_5Ga_2As_6$ compared with $Ca_5Sn_2As_6$. Therefore, subtle changes in the lattice structures of $Ca_5Ga_2As_6$ to $Ca_5Sn_2As_6$ are possibly due to the changes of the ratio of the electronegativity of polyanion. Moreover, it is more important to relate the As-As bonding to the thermoelectric performance.

Now we turn to study the effect of As-As bonding on the electronic structures of $Ca_5M_2As_6$ (M = Ga, Sn). Fig. 4 shows the calculated DOS of $Ca_5M_2As_6$ compounds. As can be seen from Fig. 4, for $Ca_5Ga_2As_6$ with As-As bonding, a sharp DOS peak appears on the bottom of conduction bands and is mainly contributed by As1 p orbital. Thus, the As-As bonding makes a great contribution to the sharp DOS peak on the bottom of conduction bands. The thermopower is proportional to the derivative of the DOS. The great derivative of DOS near the Fermi level will result in a large thermopower. Thus, n-type doping should increase largely the Seebeck effect of $Ca_5Ga_2As_6$. As seen from Fig. 4(d), for $Ca_5Sn_2As_6$ without As-As bonding, a sharp DOS peak appears on the top of valence bands, which may increase its p-type Seebeck effect. Thus, the thermopower of p-type $Ca_5Sn_2As_6$ may be larger than that of n-type one, which is mainly contributed by the sharp DOS peak of As1 atoms near the valence band maximum (VBM). Therefore, the formation of As-As bonding or not leads to the different location of sharp DOS peaks in $Ca_5Ga_2As_6$ and $Ca_5Sn_2As_6$, which may strongly increase the Seebeck effect of n-type $Ca_5Ga_2As_6$ and p-type $Ca_5Sn_2As_6$.

For $Ca_5Ga_2As_6$, the valence bands maximum (VBM) is mainly dominated by As atoms by the order As1 > As2 > As3 from $-1$ to 0 eV, and the conduction bands minimum CBM is primarily dominated by Sn and As1 atoms from 0.75 to 1.5 eV. From 3 to 6 eV, the DOS is primarily formed by Ca atoms, which is consistent with the assumption that Ca atoms donate their valence electrons to the anionic substructure. From Fig. 4(b), the Sn s-orbit hybridizes with the As p state, which forms the bonding and anti-bonding states from $-4$ to $-1.5$ eV and 0.75 to 2 eV, respectively. The conduction bands, and, in particular, the conduction band minimum (CBM) states, are derived from the hybridizations of Sn s, As1 p, As2 p, As3 p, and Sn p orbits. From Fig. 3(a)-(c), the general situation of $Ca_5Sn_2As_6$ demonstrates that the As1 and Sn atoms play an important role in transport properties.

<table>
<caption>Table 1 The electronegativity value of each atom for the compounds in $Sr_5Sn_2P_6$ and $Ca_5Ga_2As_6$ type. Pn/M is the ratio of the electronegativity value of Pn to that of M</caption>
<thead>
<tr>
<th>Type</th>
<th>$A_5M_2Pn_6$</th>
<th>A</th>
<th>M</th>
<th>Pn</th>
<th>Pn/M</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">$Sr_5Sn_2P_6$ type</td>
<td>$Ca_5Sn_2As_6$</td>
<td>1.00</td>
<td>1.96</td>
<td>2.18</td>
<td>1.11</td>
</tr>
<tr>
<td>$Sr_5Sn_2As_6$</td>
<td>0.95</td>
<td>1.96</td>
<td>2.18</td>
<td>1.11</td>
</tr>
<tr>
<td>$Sr_5Sn_2P_6$</td>
<td>0.95</td>
<td>1.96</td>
<td>2.19</td>
<td>1.12</td>
</tr>
<tr>
<td rowspan="4">$Ca_5Ga_2As_6$ type</td>
<td>$Ca_5Ga_2Sb_6$</td>
<td>1.00</td>
<td>1.81</td>
<td>2.05</td>
<td>1.13</td>
</tr>
<tr>
<td>$Ca_5In_2Sb_6$</td>
<td>1.00</td>
<td>1.78</td>
<td>2.05</td>
<td>1.15</td>
</tr>
<tr>
<td>$Ca_5Ga_2As_6$</td>
<td>1.00</td>
<td>1.81</td>
<td>2.18</td>
<td>1.20</td>
</tr>
<tr>
<td>$Ca_5Al_2Sb_6$</td>
<td>1.00</td>
<td>1.61</td>
<td>2.05</td>
<td>1.27</td>
</tr>
</tbody>
</table>

![](./images/811054282571776001_5.jpg)

Fig. 4 Calculated density of states (DOS) of Ca₅Ga₂As₆ (left) and Ca₅Sn₂As₆ (right).

It is also interesting to explore the effect of As-As bonding on the electrical conductivity of Ca₅M₂As₆. The electrical conductivity of a material mainly depends on its states near the VBM and CBM. For Ca₅Ga₂As₆ with As-As bonding, near the bottom of conduction bands, the states of As pᵧ are much larger than those of As1 pₓ and As1 p_z, indicating the high electrical conductivity along the high electrical conductivity along the y-direction. Moreover, the electrical conductivity along the covalent chain direction should be also high. Thus, Ca₅Ga₂As₆ should have high electrical conductivity both along the y- and z-direction, which will induce a high electrical conductivity in n-type polycrystalline Ca₅Ga₂As₆. For Ca₅Sn₂As₆ without As-As bonding, near the top of valence bands, the states of As1 pᵧ are much larger than those of As1 pₓ and As1 p_z, which will increase the electrical conductivity along the y-direction by p-type doping. Combined with high electrical conductivity along the covalent chain direction, p-type polycrystalline Ca₅Sn₂As₆ might have a high electrical conductivity.

For further show the charge accumulation of the As-As bonding, we calculated the band decomposed charge densities of Ca₅Ga₂As₆ from -4 to -3 eV, -2.5 to -1.5 eV, -1.0 to 0 eV, and 0 to 1 eV shown in Fig. 5. It is clearly seen that the As1-As1 dimers form $\sigma$-bonding and $\sigma^*$-antibonding in Fig. 5(a) and (d), and weak $\pi$-bonding and $\pi^*$-antibonding as shown in Fig. 5(b) and (c), respectively. For the top of valence bands, the character of $\pi^*$-antibonding makes many electrons gathering along the anion chain direction, which is favorable to form a conductive path along this direction. On the other hand, for the bottom of conduction bands, the feature of $\sigma^*$-antibonding causes an accumulation of electrons along the y-direction (As-As bonding direction), which may lead to a higher electrical conductivity along this direction than that of Ca₅Sn₂As₆ without As1-As1 bonding along the same direction.

In addition to band shape near band edge, band gap also strongly affects electrical transport properties. As known, the MBJ semi-local exchange can obtain an accurate band gap approaching experimental value, such as the calculated band gap value (5.08 eV) of LiH is very agreement with the experimental value (5.0 eV).²⁹ Therefore, the band structures of Ca₅Sn₂As₆ and Ca₅Ga₂As₆ with the MBJ semi-local exchange employed in WIEN2k were calculated and shown in Fig. 6. In order to verify the reliability of the calculated band structures, we also calculated the band of Ca₅M₂As₆ with the MBJ semi-local exchange employed in VASP shown in Fig. 6(c) and (d). And, the band shape by VASP is very similar to that by WIEN2k. Moreover, it is interesting to discuss the difference in their band gap and the origin of such difference. From this figure, Ca₅Sn₂As₆ and Ca₅Ga₂As₆ are semiconductors with an indirect band gap and a direct band gap, respectively. Sr₅Sn₂As₆ is same with the former one.³⁰ The order of the band gaps is Ca₅Sn₂As₆ (0.72 eV) > Ca₅Ga₂As₆ (0.65 eV) > Sr₅Sn₂As₆ (0.55 eV), indicating the lowest intrinsic carrier concentration for Ca₅Sn₂As₆ at same temperature. As seen on the top of the valence bands of Ca₅Ga₂As₆, the three bands at $\Gamma$ point around -0.25 eV are close in energy. The three bands may be converged at high temperature, which may increase the Seebeck coefficient of Ca₅Ga₂As₆ at high temperature. For A₅M₂As₆ Zintl compounds, the cations donate electrons to the anions, which determines the location of the Fermi level, with a little effect on the band shape near the Fermi level.

![](./images/811054282571776001_6.jpg)

Fig. 5 Band decomposed charge density of $Ca_5Ga_2As_6$ from (a) -4 to -3 eV, (b) -2.5 to 1.5 eV, (c) -1 to 0 eV, and (d) 0 to 1 eV for the (100) plane, respectively.

The different band gaps of $Ca_5Sn_2As_6$ and $Sr_5Sn_2As_6$ are mainly due to the fact that the interaction between Ca and As atom is stronger than that between Sr and As atoms. The possible reason is that Ca and As atoms lie in the same period of Periodic Table of the Elements (PTE), which have close energy of valence electrons and consequently the lower bonding states and higher antibonding states in energy. Thus, $Ca_5Sn_2As_6$ will have a large band gap. This also appears in other similar compounds, such as that the band gap of $Sr_5Al_2Sb_6$ $(0.80\ eV)^{31}$ is larger than that of $Ca_5Al_2Sb_6$ $(0.50\ eV).^{11}$ Hence, A atoms affect the band gap strongly, while the M atom substitution has a large influence on the changing of band shape near the Fermi level.

### C. Thermoelectric transport properties

Based on the calculated band structures of $Ca_5M_2As_6$ (M = Sn, Ga), the thermoelectric transport properties can be evaluated by

![](./images/811054282571776001_7.jpg)

Fig. 6 Calculated band structures of $Ca_5M_2As_6$ (M = Sn, Ga) by (a) and (b) WIEN2k and (c) and (d) VASP.

using the semiclassical Boltzmann theory and rigid-band model. Although the predictive power of the model is limited by inducing constant relaxation time assumption, the results are valuable for comparison. Here, we just use them for confirming the conclusion obtained from the electronic structure above, and qualitative comparison of thermoelectric performance for these compounds. As well known, small difference in the band gaps of $Ca_{5}Sn_{2}As_{6}$, $Sr_{5}Sn_{2}As_{6}$, and $Ca_{5}Ga_{2}As_{6}$ will lead to a large degree difference on the transport properties. To have a good view of the trend, we calculated carrier concentration ($n$), Seebeck coefficient ($S$), electrical conductivity with respect to relaxation time ($\sigma/\tau$), and power factor with respect to relaxation time ($S^{2}\sigma/\tau$) as a function of temperature shown in Fig. 7. Fig. 7(a) shows that the carrier concentration of $A_{5}M_{2}As_{6}$ compounds increases with the increasing of temperature due to thermal excitation. It is known that a narrow band gap induces large carrier concentration. Hence, the order of the carrier concentration at same temperature is $Ca_{5}Sn_{2}As_{6} < Ca_{5}Ga_{2}As_{6} < Sr_{5}Sn_{2}As_{6}$, which is in agreement with the order of the band gaps. However, the carrier concentration of $Ca_{5}Sn_{2}As_{6}$ is larger than that of $Ca_{5}Ga_{2}As_{6}$ above 1000 K, which is mainly due to the fact that more bands near the VBM for $Ca_{5}Sn_{2}As_{6}$ may excite more electrons at high temperature.

![](./images/811054282571776001_8.jpg)

Fig. 7 Calculated thermoelectric properties of $Ca_{5}M_{2}As_{6}$ ($M = Sn, Ga$) as a function of temperature. (a) Carrier concentration, $n$ (unit in $10^{20}$ $cm^{-3}$); (b) Seebeck coefficient, $S$ (unit in $\mu V$ $K^{-1}$); (c) electrical conductivities relative to relaxation time, $\frac{\sigma}{\tau}$ (unit in $10^{18}\ \Omega^{-1}m^{-1}s^{-1}$); (d) power factor with respect to relaxation time, $\frac{S^{2}\sigma}{\tau}$ (unit in $10^{11}$ W $K^{-2}$ $m^{-1}s^{-1}$).

As can be seen in Fig. 7(b), the $S$ value is positive over the studied entire temperature range, indicating the p-type transport of $A_{5}M_{2}As_{6}$. $S$ increases with the increasing of temperature, and reaches the maximum values of 266 ($\mu V$ $K^{-1}$) at 390 K and 248 ($\mu V$ $K^{-1}$) at 500 K for $Ca_{5}Sn_{2}As_{6}$ and $Sr_{5}Sn_{2}As_{6}$, respectively, and then decreases. Nevertheless, $S$ of $Ca_{5}Ga_{2}As_{6}$ decreases first with the increasing of temperature, and reaches the minimum value of 201 ($\mu V$ $K^{-1}$) at 500 K, and then increases. Maximum $S$ is 234 ($\mu V$ $K^{-1}$) at 1050 K.

$$
S = \frac{8\pi^{2}k_{\mathrm{B}}^{2}}{3eh^{2}}m \times T\left(\frac{\pi}{3n}\right)^{2/3} \ . \tag{2}
$$

As can be explained from eqn (2), the decreasing of $S$ from 300 K to 500 K is mainly due to the increasing of carrier concentration, and the increasing of $S$ from 500 K to 1000 K is mostly due to the increasing of temperature. The increasing of temperature may induce the convergence of the bands at $\Gamma$ point on the top of valence bands of $Ca_{5}Ga_{2}As_{6}$. Consequently, the Seebeck coefficient of $Ca_{5}Ga_{2}As_{6}$ will be increased at high temperature. As indicated by the formula $ZT = \frac{rS^{2}}{L}$ ($r = \kappa_{\mathrm{e}}/\kappa$ and $L$ is the Lorentz constant), it is impossible to obtain high $ZT$ value without large $S.^{32}$ Hence, $Ca_{5}Sn_{2}As_{6}$ is a promising thermoelectric material due to its large Seebeck coefficient over a wide temperature range. For Fig. 6(c) and (d), $\sigma/\tau$ increases with the increasing of temperature, which means that the excited carriers increase. $S^{2}\sigma/\tau$ for $Ca_{5}Sn_{2}As_{6}$ increases with the increasing of temperature and then remains large values. It reaches the largest value of $3.9 \times 10^{11}$ W $K^{-2}$ $m^{-1}s^{-1}$ at 1050 K, which is smaller than that of $Ca_{5}Ga_{2}As_{6}$ ($4.5 \times 10^{11}$ W $K^{-2}$ $m^{-1}$ $s^{-1}$ at 1100 K). The relatively low $S^{2}\sigma/\tau$ of $Ca_{5}Sn_{2}As_{6}$ may be due to its low carrier concentration, which can be solved by doping. The simulation of doping along different directions will be considered in detail next.

The high anisotropy of the lattice structure for $Ca_{5}M_{2}As_{6}$ ($M$ = Sn, Ga) will cause a large difference in thermoelectric properties along different directions as shown in Fig. 8. Compared Fig. 8(a) and (d), the varying degree of bipolar reduction in the thermopower of the two compounds is different as the order is: $Ca_{5}Sn_{2}As_{6} < Ca_{5}Ga_{2}As_{6}$, which is consisting with the band gap of the compounds by the descending order. As well known, high $ZT$ value needs large Seebeck coefficient. The thermoelectric performance of $Ca_{5}Sn_{2}As_{6}$ may be promising. On the other hand, the small anisotropy of the Seebeck coefficient and the electrical conductivity appear in the p-type $Ca_{5}Sn_{2}As_{6}$ and n-type $Ca_{5}Ga_{2}As_{6}$, which indicates that the polycrystalline samples may have more excellent transport properties by doping. The large Seebeck coefficient for n-type $Ca_{5}Ga_{2}As_{6}$ and p-type $Ca_{5}Sn_{2}As_{6}$ comes from the sharp DOS peak appearing near the CBM and the VBM, respectively, which corresponds to the formation of the As-As bonding or not. In addition, $\sigma/\tau$ of $Ca_{5}Ga_{2}As_{6}$ for n-type along the $y$-direction is large shown in Fig. 8(e). The reason is the increased electrons gathered along the $y$-direction, which is caused by the As-As bonding discussed in Fig. 4(d). Then, the electrical conductivity of n-type

![](./images/811054282571776001_9.jpg)

Fig. 8 The anisotropy of $Ca_5M_2As_6$ ($M = Sn, Ga$) as a function of carrier concentration from $1 \times 10^{19}$ to $1 \times 10^{21}\ \text{cm}^{-3}$ at 950 K. (a) and (d) Seebeck coefficients, $S$ (unit in $\mu\text{V K}^{-1}$); (b) and (e) electrical conductivities to relaxation time, $\frac{\sigma}{\tau}$ (unit in $10^{20}\ \Omega^{-1}\text{ m}^{-1}\text{ s}^{-1}$); (c) and (f) thermal power factor with respect to relaxation time, $\frac{S^2\sigma}{\tau}$ (unit in $10^{11}\ \text{W K}^{-2}\text{ m}^{-1}\text{ s}^{-1}$).

polycrystalline $Ca_5Ga_2As_6$ may be large. It also exhibits small anisotropy of the electrical conductivity for p-type $Ca_5Sn_2As_6$, indicating the large electrical conductivity of p-type polycrystalline $Ca_5Sn_2As_6$. Moreover, both the Seebeck coefficient and the electrical conductivity along the $z$-direction are larger than those along the other two directions for p- and n-type $Ca_5Sn_2As_6$, and it also occurs in n-type $Sr_5Sn_2As_6$. We believe that high thermoelectric performance along the $z$-direction could be achieved in p- and n-type $Ca_5Sn_2As_6$ by doping. On the other hand, when $E - \mu \gg k_\text{B}T$, the Mott formula is given by:$^{33}$

$$
S = \left. \left( \frac{\pi^2k_\text{B}{}^2T}{3e\sigma} \right) \frac{\text{d}\sigma}{\text{d}E} \right|_{E=E_\text{f}} = \left. \left( \frac{\pi^2k_\text{B}{}^2T}{3e} \right) \frac{\text{dln}\ \sigma}{\text{d}E} \right|_{E=E_\text{f}} . \tag{3}
$$

Therefore, we can understand the Seebeck coefficient from the energy derivative of the log-scale conductivity $\left( \frac{\text{dln}\ \sigma}{\text{d}E} \right)$. We calculated $\frac{\text{dln}\ \sigma}{\text{d}E}$ as a function of carrier concentration near the Fermi level for $Ca_5Sn_2As_6$ at 950 K shown in Fig. 9. For p-type $Ca_5Sn_2As_6$, the $\frac{\text{dln}\ \sigma}{\text{d}E}$ are relatively close in all directions, which fits well with the variation of Seebeck coefficient shown in Fig. 8(a). For n-type $Ca_5Sn_2As_6$, the $\frac{\text{dln}\ \sigma}{\text{d}E}$ along the $z$-direction is larger than that along the $x$- or $y$-direction from $1 \times 10^{19}$ to $5 \times 10^{20}\ \text{cm}^{-3}$, and smaller than that along the $x$-direction from $5 \times 10^{20}$ to $1 \times 10^{21}\ \text{cm}^{-3}$. The Seebeck coefficient along the $z$-direction is larger than those along the $x$- or $z$-direction from $1 \times 10^{19}$ to $3 \times 10^{20}\ \text{cm}^{-3}$, and smaller than that along the $x$-direction from $3 \times 10^{20}$ to $1 \times 10^{21}\ \text{cm}^{-3}$, which accords with the change of $\frac{\text{dln}\ \sigma}{\text{d}E}$ along the $z$-direction for n-type $Ca_5Sn_2As_6$. Hence, $S$ and $\frac{\sigma}{\tau}$ along the $z$-direction are larger than those along

![](./images/811054282571776001_10.jpg)

Fig. 9 The energy derivative of the log-scale conductivity as a function of carrier concentration of $Ca_5Sn_2As_6$ from $1 \times 10^{19}$ to $1 \times 10^{21}\ \text{cm}^{-3}$ along $x$-, $y$-, and $z$-directions at 950 K.

other two directions for p- and n-type $Ca_5Sn_2As_6$, which is due to the larger energy derivative of the log-scale conductivity along the $z$-direction. It is similar to $Sr_5Sn_2As_6$ and $Ca_5Ga_2As_6$.

### D. Thermal property

As mentioned above, the total thermal conductivity ($\kappa$) in a typical thermoelectric material is the sum of electronic ($\kappa_\text{e}$) and lattice ($\kappa_\text{l}$) contributions. Different from $\kappa_\text{e}$, the lattice thermal conductivity is a parameter largely independent of the electrical transport properties, which should be minimized as much as possible for high $ZT$. The lattice thermal conductivity comes from lattice vibration (phonons). Above the Debye temperature ($\Theta_\text{D}$), the lattice thermal conductivity decreases with the $1/T$ temperature dependence expected when scattering is limited by Umklapp phonon-phonon scattering effect. This dependence relationship is maintained until the minimum lattice conductivity ($\kappa_\text{min}$) is reached, which can be approximately calculated by using the following formula:

$$
\kappa_{\min }=\frac{1}{2}\left(\frac{\pi}{6}\right)^{1 / 3} k_{\mathrm{B}} V^{-2 / 3}\left(2 \nu_{\mathrm{s}}+\nu_{\mathrm{l}}\right), \tag{4}
$$

where $V$ is the average volume of unit cell, $k_\text{B}$ is the Boltzmann constant, $\nu_\text{s}$ and $\nu_\text{l}$ are the shear and longitudinal velocities, respectively. Therefore, the $\kappa_\text{min}$ plays a key role in characterizing the value of lattice thermal conductivity. Then, we can calculate the longitudinal and shear sound velocities of $Ca_5Sn_2As_6$ and $Ca_5Ga_2As_6$ to get $\kappa_\text{min}$. The $\nu_\text{s}$ and $\nu_\text{l}$ are calculated by:

$$
\nu_{\mathrm{s}}=\sqrt{\frac{G}{d}}, \tag{5}
$$

$$
\nu_{\mathrm{l}}=\sqrt{\frac{K+\frac{4}{3} G}{d}}, \tag{6}
$$

where $d$ is the theoretical density. $G$ and $K$ are shear and bulk modulus, respectively. And, the two modulus can be calculated from the elastic constants by using the Voigt-Reuss-Hill approximation,³⁴

$$
K=\frac{1}{2}\left(B_{\mathrm{R}}+B_{\mathrm{v}}\right), \quad G=\frac{1}{2}\left(G_{\mathrm{R}}+G_{\mathrm{v}}\right) \tag{7}
$$

where $B_\text{R}$ and $B_\text{v}$ ($G_\text{R}$ and $G_\text{v}$) are the Reuss bulk modulus and Voigt bulk modulus (Reuss shear modulus and Voigt shear modulus), respectively. For orthorhombic systems, $B_\text{R}$ and $B_\text{v}$ ($G_\text{R}$ and $G_\text{v}$) can be calculated by:

$$
B_{\mathrm{R}}=\frac{1}{\left(s_{11}+s_{22}+s_{33}\right)+2\left(s_{12}+s_{13}+s_{23}\right)} \tag{8}
$$

$$
B_{\mathrm{v}}=\frac{1}{9}\left(c_{11}+c_{22}+c_{33}\right)+\frac{2}{9}\left(c_{12}+c_{13}+c_{23}\right) \tag{9}
$$

$$
G_{\mathrm{R}}=\frac{15}{4\left(s_{11}+s_{22}+s_{33}\right)-4\left(s_{12}+s_{13}+s_{23}\right)+3\left(s_{44}+s_{55}+s_{66}\right)} \tag{10}
$$

$$
G_{\mathrm{v}}=\frac{1}{15}\left(c_{11}+c_{22}+c_{33}\right)+\frac{1}{5}\left(c_{44}+c_{55}+c_{66}\right) \tag{11}
$$

where the $s_{ij}$ are the elastic compliance constants and the $c_{ij}$ are the elastic constants. The elastic constants were obtained by the stress-strain method. As can be seen in eqn (4), the small velocity of a material will results in a relative low minimum lattice thermal conductivity. The $\nu_\text{s}$ and $\nu_\text{l}$ of $Ca_5Ga_2As_6$ (2860 and $4780\ \text{m s}^{-1}$) respectively) are larger than that of $Ca_5Sn_2As_6$ ($\nu_\text{s}=2240$ and $\nu_\text{l}=4190\ \text{m s}^{-1}$), indicating the smaller lattice thermal conductivity ($\kappa_\text{min}$) of $Ca_5Sn_2As_6$ ($0.56\ \text{W m}^{-1}\ \text{K}^{-1}$) than that of $Ca_5Ga_2As_6$ ($0.70\ \text{W m}^{-1}\ \text{K}^{-1}$). Hence, $Ca_5Sn_2As_6$ may obtain a higher $ZT$ value than that of $Ca_5Ga_2As_6$. Moreover, in complex materials, the size of the unit cell is one of the most important factor for determining their lattice thermal conductivity, $\kappa_\text{l}$. The decreasing $\kappa_\text{l}$ with increasing unit cell volume has been proven by some Zintl antimonides.¹⁴ The volume of $Ca_5Sn_2As_6$ ($665\ \mathring{\text{A}}^3$) is larger than that of $Ca_5Ga_2As_6$ ($634\ \mathring{\text{A}}^3$), which may be not conducive to phonon scattering. Because, the lattice thermal conductivity can be decreased by increasing the lattice period thus providing a longer more "tortuous" path through the unit cell for the heat carrying phonons.³⁵

## IV. Conclusion

The different electron configuration between Pn and Ga (or Sn) determines whether the As-As bonding appears or not, which affects the Seebeck effect and the anisotropy of electrical conductivity strongly. When forming the As-As bond in $Ca_5Ga_2As_6$, a sharp peak of density of states appears near the bottom of the conduction bands, which will dramatically increase its n-type Seebeck effect. Moreover, the calculated band decomposed charge density shows that the As-As bonding leads to a high charge accumulating along the $y$-direction. Combined with the high electrical conductivity along the covalent anion chain direction, a high electrical conductivity may exist in n-type polycrystal of $Ca_5Ga_2As_6$. Hence, the n-type polycrystal of $Ca_5Ga_2As_6$ may have a good thermoelectric performance. However, for the absence of As-As bonding in $A_5Sn_2As_6$ ($\text{A}=\text{Ca}, \text{Sr}$), a sharp peak of density of states occurs on the top of the valence bands, which will largely enhance its p-type Seebeck effect. For $A_5Sn_2As_6$, the small anisotropy of electrical conductivity may induce the high electrical value for its p-type polycrystal. In addition, the comparison of the calculated band structures showed that partial A atom substitution can strongly affect the band gap, and the partial M atom substitution has an influence on the band shape near the Fermi level. As a consequence, the optimal band gap of $Ca_5Sn_2As_6$ results in the relatively small bipolar effect, which is also beneficial for obtaining large Seebeck coefficient. On the other hand, both the Seebeck coefficient and the electrical conductivity along the $z$-direction are larger than those along other directions for n- and p-type $Ca_5Sn_2As_6$, and n-type $Sr_5Sn_2As_6$, while not happen in $Ca_5Ga_2As_6$, which is mainly due to the larger energy derivative of the log-scale conductivity along the $z$-direction.

## Acknowledgements

This research was sponsored by the National Natural Science Foundation of China (No. 51371076 and 11674083), Excellent Youth Foundation of Henan Province (No. 154100510013).

### References

1 D. M. Rowe, *CRC handbook of thermoelectrics*, CRC press, 1995.

2 S. M. Kauzlarich, S. R. Brown and G. J. Snyder, *Dalton Trans.*, 2007, 2099-2107.

3 S. R. Brown, S. M. Kauzlarich, F. Gascoin and G. J. Snyder, *Chem. Mater.*, 2006, **18**, 1873-1877.

4 A. Zevalkink, E. S. Toberer, W. G. Zeier, E. Flage-Larsen and G. J. Snyder, *Energy Environ. Sci.*, 2011, **4**, 510-518.

5 A. Zevalkink, G. Pomrehn, Y. Takagiwa, J. Swallow and G. J. Snyder, *ChemSusChem*, 2013, **6**, 2316-2321.

6 A. Zevalkink, W. G. Zeier, G. Pomrehn, E. Schechtel, W. Tremel and G. J. Snyder, *Energy Environ. Sci.*, 2012, **5**, 9121-9128.

7 S. M. Kauzlarich, *Chemistry, structure, and bonding of Zintl phases and ions*, VCH, New York, 1996.

8 A. M. Mills, R. Lam, M. J. Ferguson, L. Deakin and A. Mar, *Coord. Chem. Rev.*, 2002, **233**, 207-222.

9 G. A. Slack, *Solid State Physics*, Academic, New York, 1979.

10 E. S. Toberer, A. Zevalkink and G. J. Snyder, *J. Mater. Chem.*, 2011, **21**, 15843-15852.

11 A. Zevalkink, G. S. Pomrehn, S. Johnson, J. Swallow, Z. M. Gibbs and G. J. Snyder, *Chem. Mater.*, 2012, **24**, 2091-2098.

12 P. Verdier, P. L'Haridon, M. Maunaye and Y. Laurent, *Acta Crystallogr., Sect. B: Struct. Crystallogr. Cryst. Chem.*, 1976, **32**, 726-728.

13 B. Eisenmann, H. Jordan and H. Schäfer, *Z. Anorg. Allg. Chem.*, 1985, **530**, 74-78.

14 A. Zevalkink, Ph.D. thesis, California Institute of Technology, 2014.

15 J. Wang, S.-Q. Xia and X.-T. Tao, *Inorg. Chem.*, 2012, **51**, 5771-5778.

16 G. Kresse and J. Hafner, *J. Phys.: Condens. Matter*, 1994, **6**, 8245.

17 P. E. Blöchl, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1994, **50**, 17953.

18 D. M. Ceperley and B. Alder, *Phys. Rev. Lett.*, 1980, **45**, 566.

19 D. Singh, *Plane waves, pseudopotentials and the LAPW method*, 1994.

20 L. H. Thomas, *Math. Proc. Cambridge Philos. Soc.*, 1927, 542-548.

21 E. Fermi, *Z. Phys.*, 1928, **48**, 73-79.

22 F. Tran and P. Blaha, *Phys. Rev. Lett.*, 2009, **102**, 226401.

23 E. Engel and S. H. Vosko, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1993, **47**, 13164.

24 D. Koelling and B. Harmon, *J. Phys. C: Solid State Phys.*, 1977, **10**, 3107.

25 P. Hohenberg and W. Kohn, *Phys. Rev.*, 1964, **136**, B864.

26 P. Blaha, K. Schwarz, G. Madsen, D. Kvasnicka and J. Luitz, *WIEN2k: An augmented plane wave+ local orbitals program for calculating crystal properties*, Vienna, 2001.

27 G. K. Madsen and D. J. Singh, *Comput. Phys. Commun.*, 2006, **175**, 67-71.

28 Y. L. Yan, Y. X. Wang and G. B. Zhang, *J. Mater. Chem.*, 2012, **22**, 20284-20290.

29 D. J. Singh, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2010, **82**, 205102.

30 D. B. Luo, Y. X. Wang, Y. L. Yan, G. Yang and J. M. Yang, *J. Mater. Chem. A*, 2014, **2**, 15159-15167.

31 A. Zevalkink, Y. Takagiwa, K. Kitahara, K. Kimura and G. J. Snyder, *Dalton Trans.*, 2014, **43**, 4720.

32 D. J. Singh and D. Parker, *J. Appl. Phys.*, 2013, **114**, 143703.

33 D. Guo, C. Hu, Y. Xi and K. Zhang, *J. Phys. Chem. C*, 2013, **117**, 21597-21602.

34 R. Hill, *Proc. Phys. Soc., London, Sect. A*, 1952, **65**, 349.

35 J. R. Sootsman, D. Y. Chung and M. G. Kanatzidis, *Angew. Chem., Int. Ed.*, 2009, **48**, 8616-8639.