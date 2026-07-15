PAPER

# Physical Properties of Group 14 in $P6_222$ Phase: First-Principles Calculations

To cite this article: Ying-Bo Zhao *et al* 2019 *Commun. Theor. Phys.* **71** 1036

View the [article online] for updates and enhancements.

This content was downloaded from IP address 129.25.131.235 on 22/08/2019 at 23:07

# Physical Properties of Group 14 in $P6_222$ Phase: First-Principles Calculations*

Ying-Bo Zhao (赵颖博),$^{1}$ Wei Zhang (张伟),$^{2}$ and Qing-Yang Fan (樊庆扬)$^{3,\dagger}$

$^{1}$School of Mechanical and Electrical Engineering, Xi'an University of Architecture and Technology, Xi'an 710055, China
$^{2}$School of Microelectronics, Xidian University, Xi'an 710071, China
$^{3}$School of Information and Control Engineering, Xi'an University of Architecture and Technology, Xi'an 710055, China

(Received March 18, 2019; revised manuscript received May 2, 2019)

**Abstract** Two new Group IV element allotropes $Si_3$ and $Ge_3$ in $P6_222$ phase are predicted in this work and their physical properties are investigated using the density functional theory. Each of the newly predicted allotropes has a superdense structure, which is mechanically, dynamically, and thermodynamically stable, as verified by elastic constants, phonon dispersion spectra and relative enthalpies, respectively. The mechanical anisotropy properties are studied in detail by illustrating the directional dependence of Young's modulus, discussing the universal anisotropic index, and calculating shear anisotropy factors together with bulk moduli. It shows that $P6_222$-$Si_3$ exhibits the greater anisotropy than $P6_222$-$Ge_3$, and interestingly both of the newly predicted crystals appear to be isotropic in the (001) plane. Additionally, the Debye temperature, sound velocities, and the minimum thermal conductivity are examined to evaluate the thermodynamic properties of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase, and the electronic band structures are achieved by HSE06 hybrid functional, which indicate that $P6_222$-$C_3$ and -$Si_3$ are indirect band gap semiconductors and $P6_222$-$Ge_3$ exhibits the metallic feature.

DOI: 10.1088/0253-6102/71/8/1036

**Key words:** group 14 element allotropes, mechanical properties, electronic properties, elastic anisotropy properties

## 1 Introduction

Due to increasing concerns about the limited supply of current and future fossil fuels, a lot of work has been undertaken to find clean and sustainable energy sources over the past several decades. The effort to search new element allotropes has been continuously made to solve the fossil energy crisis and reduce the pollution from fossil fuel consumption. Among which, the search for new Group IV element (C, Si, and Ge) allotropes has been extensively studied,$^{[1-10]}$ owing to their importance in fundamental science and various possible applications in virtue of their special physical and chemical properties exhibited.

Carbon is known as the most plentiful element on earth, and pure carbon is mainly in graphite and diamond forms, which owns some of the strongest bonds naturally as ever known. The carbon allotropes have been investigated previously and show an extremely wide range of structures from super-hard semiconductors to ultra-soft semimetals with advanced mechanical and electronic properties, due to their special abilities to form $sp$, $sp^2$, and $sp^3$ hybridized bonds.$^{[11-16]}$ The bct $C_4$ was investigated by Umemoto, *et al.*$^{[14]}$ based on first-principle calculations. It was reported that $C_4$ appears to be transparent and dynamically stable at zero pressure, and beyond 18.6 GPa exhibiting more stability than graphite. Wei, *et al.*$^{[15]}$ studied the mechanical and electronic properties of *Imma*-carbon, which is a super-hard $sp^3$ carbon allotrope, and it was found that *Imma*-carbon is a direct semiconductor with a band gap of 4.17 eV and a high bulk modulus of 440 GPa. Recently, Fan *et al.*$^{[16]}$ investigated Lonsdaleite C, Si, and Ge and Lonsdaleite C–Si and Si–Ge alloys, and found that Lonsdaleite $C_{0.25}Si_{0.75}$ exhibits metallic properties and Lonsdaleite $Si_{0.25}Ge_{0.75}$ is a narrow direct semiconductor with a band gap of 0.76 eV. For the minimum thermal conductivity, Lonsdaleite $C_{0.75}Si_{0.25}$ and Lonsdaleite $C_{0.5}Si_{0.5}$ are greater than that of diamond–C.

Silicon is the second most plentiful element on earth and considered the cornerstone of the semiconductor industry. It is known that silicon exists in a great deal of allotropes, including the most stable cubic diamond–Si and several metastable silicon allotropes.$^{[17-25]}$ For example, four novel silicon allotropes were proposed by us,$^{[23]}$ including three indirect gap phases: $C2/m$-16, $C2/m$-20, $I$-4, and one quasi-direct gap phase: *Amm2* phases. Six metastable silicon allotropes were predicted by Wang, *et al.*,$^{[24]}$ utilizing ab initio calculations at ambient pressure, and these structures appear attractive features as being capable of absorbing sunlight with different frequencies. Fan, *et al.*$^{[25]}$ a while ago proposed a new silicon allotrope $t$-Si$_{64}$, which is a metastable structure in $I4_1/amd$ phase.

---

*Supported by the National Natural Science Foundation of China under Grant No. 61804120, and the Talent Science and Technology Foundation of Xi'an University of Architecture and Technology under Grant No. RC1612
$^\dagger$Corresponding author, E-mail: qyfan_xidian@163.com
© 2019 Chinese Physical Society and IOP Publishing Ltd

http://www.iopscience.iop.org/ctp http://ctp.itp.ac.cn

Since the minimum thermal conductivity of $t$-Si₆₄ was found to be much smaller than that of diamond-Si, it was reported that the Si-Ge alloys in $I4_1/amd$ phase are potential thermoelectric materials.

For germanium allotropes, many works have been done to investigate their properties.[²⁶⁻³²] Nguyen, *et al.*[³⁰] found a new dynamically stable germanium in a distorted $sp^3$-hybridized framework structure with $P4_2/mnm$ symmetry. Saleev, *et al.*[³¹] predicted six new allotropes of silicon and germanium, and examined their structural, elastic, electronic and optical properties using ab initio quantum mechanical methods. The results showed that some allotropes of Ge might be metallic and these phases might be high-temperature variants. Bautista-Hernandez, *et al.*[³²] proposed elastically and vibrationally stable silicon and germanium in the monoclinic and orthorhombic phases, with energies slightly larger than that of diamond-Si and -Ge.

All the previous works have laid solid foundations for us to a broader search for new allotropes of Group IV element that possibly exhibit novel properties. In this work, two new Group IV element allotropes $Si_3$ and $Ge_3$ in $P6_222$ phase with superdense structures are predicted. The crystal structures of $P6_222$-$Si_3$ and -$Ge_3$ are composed of a lattice similar to that of carbon,[³³] with silicon and germanium atoms substituting carbon atoms. Densities of $P6_222$-$Si_3$ and -$Ge_3$ are $2.574\ \text{g/cm}^3$ and $5.647\ \text{g/cm}^3$, which are 10.1% and 8.1% higher than those in diamond phase, respectively, thus making them superdense crystals. The mechanical, dynamic and thermodynamic stabilities of these newly predicted crystals are verified, and other important physical properties are systematically investigated.

## 2 Calculation Method
This work was carried out in the framework of density functional theory (DFT)[³⁴⁻³⁵] based on Cambridge Serial Total Energy Package (CASTEP) plane-wave code.[³⁶] All of the theoretical calculations were performed with the generalized gradient approximation (GGA) in the form of the Perdew-Burke-Ernzerhof (PBE)[³⁷] functional and the Perdew-Burke-Ernzerhof functional for solids (PBEsol), and the local density approximation (LDA) in the form of Ceperly and Alder, as parameterized by Perdew and Zunger (CA-PZ)[³⁸⁻³⁹] exchange correlation potential. The structural parameters were obtained using the Broyden-Fletcher-Goldfarb-Shenno (BFGS)[⁴⁰] minimization technique. The interactions of core electrons were represented with ultrasoft pseudopotentials. Besides, the Voigt-Reuss-Hill approximation was employed to estimate elastic moduli including the bulk modulus, shear modulus, and Young's modulus. The phonon frequency was achieved based on liner response theory.[⁴¹] Additionally, the Heyd-Scuseria-Ernzerhof (HSE06) hybrid functional[⁴²] was utilized to calculate the electronic band structures of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase. The $k$ points over the Brillouin zone were selected using the Monkhorst-Pack scheme,[⁴³] with a grid spacing less than $0.025\ \text{Å}$. Energy cutoffs of 400 eV, 340 eV, and 240 eV were used for the wave function expansion and the high-density $k$-point sampling for $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase, respectively, in order to ensure good convergences of computed phases and energies of these three Group IV element allotropes.

## 3 Results and Discussion
### 3.1 Structural Properties

![](./images/812743477371600896_1.jpg)

Fig. 1 (Color online) (a) The crystal structure of $P6_222$-$X_3$ (X=C, Si, Ge), (b) the structural view along the [110] direction, and (c) the structural view along the [001] direction.

The crystal structure of $C_3$ with the space group of $P6_222$ (No. 180) phase is shown in Fig. 1, and the structure observed is comprised of several zigzag six-membered carbon rings. For $P6_222$-$Si_3$ and -$Ge_3$, their crystal structures are similar to the one of $P6_222$-$C_3$,[³³] which were obtained by replacing carbon atoms with silicon and germanium atoms, respectively. There are three atoms per conventional cell of $P6_222$-$X_3$ (X=C, Si, Ge) in hexagonal symmetry, and the atoms occupy the crystallographic 3c sites with the atomic position of (0.500, 0.000, 0.000). When viewed along the [110] and [001] direction, the crystal structures are shown in Figs. 1(b) and 1(c), respec-

tively. Densities of these three Group IV element al- lotropes are $3.647\ \text{g/cm}^3$ ($\text{C}_3$), $2.574\ \text{g/cm}^3$ ($\text{Si}_3$), and $5.647\ \text{g/cm}^3$ ($\text{Ge}_3$), which are 3.6%, 10.1%, and 8.1% higher than those in diamond ($Fd$-$3m$, No. 227) phase, re- spectively, thus making them superdense crystals. At am- bient pressure, the lattice parameters of $\text{C}_3$, $\text{Si}_3$, and $\text{Ge}_3$ in $P6_222$ phase and in diamond phase are listed in Table 1. As can be seen, the lattice constants of $P6_222$-$\text{C}_3$ calcu- lated from the PBE are $a = b = 2.602\ \mathring{\text{A}}$and $c = 2.797\ \mathring{\text{A}}$, which indeed show a good correlation with the reference data ($a = b = 2.605\ \mathring{\text{A}}$and $c = 2.801\ \mathring{\text{A}}$).$^{[33]}$ And for the lattice parameters of diamond–C ($a = 3.566\ \mathring{\text{A}}$), –Si ($a = 5.465\ \mathring{\text{A}}$), and –Ge ($a = 5.694\ \mathring{\text{A}}$), the theoretical values are in excellent agreement with the experimental data (C: $a = 3.567\ \mathring{\text{A}}$,$^{[44]}$ Si: $a = 5.430\ \mathring{\text{A}}$,$^{[45]}$ and Ge: $a = 5.660\ \mathring{\text{A}}^{[45]}$). Apparently, the values obtained from the PBE are closer to the reported data, and thus the PBE method will be primarily utilized for the following discussions.

It is worth to note that in dense covalent systems the bulk modulus ($B$ in GPa) is strongly correlating with the average interatomic distance, and the larger the value of $B$ is, the shorter the average distance between adja- cent atoms gets.$^{[46-47]}$ The bond length of $P6_222$-$\text{C}_3$ ap- pears to be uniform of $1.601\ \mathring{\text{A}}$, and the bulk modulus is 426 GPa. For the silicon and germanium allotropes in $P6_222$ phase, the uniform bond lengths are $2.386\ \mathring{\text{A}}$and $2.520\ \mathring{\text{A}}$, and the corresponding bulk moduli are 94 GPa and 64 GPa, respectively. These three bond lengths in $P6_222$ phase mentioned above are all longer than those in diamond phase correspondingly (C–C: $1.535\ \mathring{\text{A}}$,$^{[2]}$ Si–Si: $2.373\ \mathring{\text{A}}$,$^{[23]}$ and Ge–Ge: $2.484\ \mathring{\text{A}}^{[27]}$), therefore resulting in a relatively smaller $B$ than that in diamond phase (C: 431 GPa, Si: 98 GPa, and Ge: 73 GPa) as can be seen in Table 2.

<table>
<caption>Table 1 The density ($\rho$ in $\text{g/cm}^3$) and lattice parameters (in $\mathring{\text{A}}$) of $\text{C}_3$, $\text{Si}_3$, and $\text{Ge}_3$ in $P6_222$ phase.</caption>
<thead>
<tr>
<th colspan="2" rowspan="2">Space group</th>
<th rowspan="2">$\rho$</th>
<th colspan="2">PBE</th>
<th colspan="2">CA-PZ</th>
<th>Experimental</th>
</tr>
<tr>
<th>$a$</th>
<th>$c$</th>
<th>$a$</th>
<th>$c$</th>
<th>$a$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$P6_222$</td>
<td>$\text{C}_3$</td>
<td>3.647</td>
<td>2.602</td>
<td>2.797</td>
<td>2.575</td>
<td>2.763</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>$2.605^{\text{a}}$</td>
<td>$2.801^{\text{a}}$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$\text{Si}_3$</td>
<td>2.574</td>
<td>3.904</td>
<td>4.118</td>
<td>3.842</td>
<td>4.034</td>
<td></td>
</tr>
<tr>
<td></td>
<td>$\text{Ge}_3$</td>
<td>5.647</td>
<td>4.110</td>
<td>4.377</td>
<td>3.971</td>
<td>4.222</td>
<td></td>
</tr>
<tr>
<td>$Fd$-$3m$</td>
<td>C</td>
<td>3.519</td>
<td>3.566</td>
<td></td>
<td>3.526</td>
<td></td>
<td>$3.567^{\text{b}}$</td>
</tr>
<tr>
<td></td>
<td>Si</td>
<td>2.322</td>
<td>5.465</td>
<td></td>
<td>5.374</td>
<td></td>
<td>$5.430^{\text{c}}$</td>
</tr>
<tr>
<td></td>
<td>Ge</td>
<td>5.224</td>
<td>5.694</td>
<td></td>
<td>5.578</td>
<td></td>
<td>$5.660^{\text{c}}$</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="8">${}^{\text{a}}$Ref. [33]; ${}^{\text{b}}$Ref. [44]; ${}^{\text{c}}$Ref. [45].</td>
</tr>
</tfoot>
</table>

<table>
<caption>Table 2 The elastic constants (in GPa) and elastic moduli (in GPa) of $\text{C}_3$, $\text{Si}_3$, and $\text{Ge}_3$ in $P6_222$ phase.</caption>
<thead>
<tr>
<th>Space group</th>
<th></th>
<th>$C_{11}$</th>
<th>$C_{33}$</th>
<th>$C_{44}$</th>
<th>$C_{66}$</th>
<th>$C_{12}$</th>
<th>$C_{13}$</th>
<th>$B$</th>
<th>$G$</th>
<th>$B/G$</th>
<th>$E$</th>
<th>$\nu$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$P6_222$</td>
<td>$\text{C}_3$</td>
<td>1161</td>
<td>1142</td>
<td>534</td>
<td>541</td>
<td>80</td>
<td>52</td>
<td>426</td>
<td>540</td>
<td>0.79</td>
<td>1139</td>
<td>0.05</td>
</tr>
<tr>
<td></td>
<td>$\text{Si}_3$</td>
<td>185</td>
<td>156</td>
<td>78</td>
<td>70</td>
<td>45</td>
<td>58</td>
<td>94</td>
<td>68</td>
<td>1.38</td>
<td>164</td>
<td>0.21</td>
</tr>
<tr>
<td></td>
<td>$\text{Ge}_3$</td>
<td>123</td>
<td>113</td>
<td>55</td>
<td>47</td>
<td>28</td>
<td>40</td>
<td>64</td>
<td>48</td>
<td>1.33</td>
<td>115</td>
<td>0.20</td>
</tr>
<tr>
<td>$Fd$-$3m$</td>
<td>C</td>
<td>1053</td>
<td></td>
<td>563</td>
<td></td>
<td>120</td>
<td></td>
<td>431</td>
<td>522</td>
<td>0.83</td>
<td>1116</td>
<td>0.07</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$1076^{\text{a}}$</td>
<td></td>
<td>577</td>
<td></td>
<td>125</td>
<td></td>
<td>462</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Si</td>
<td>165</td>
<td></td>
<td>87</td>
<td></td>
<td>65</td>
<td></td>
<td>98</td>
<td>70</td>
<td>1.40</td>
<td>170</td>
<td>0.21</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$166^{\text{b}}$</td>
<td></td>
<td>80</td>
<td></td>
<td>64</td>
<td></td>
<td>102</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Ge</td>
<td>121</td>
<td></td>
<td>62</td>
<td></td>
<td>49</td>
<td></td>
<td>73</td>
<td>50</td>
<td>1.46</td>
<td>122</td>
<td>0.22</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$129^{\text{b}}$</td>
<td></td>
<td>67</td>
<td></td>
<td>48</td>
<td></td>
<td>77</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="13">${}^{\text{a}}$Ref. [48]; ${}^{\text{b}}$Ref. [49].</td>
</tr>
</tfoot>
</table>

### 3.2 Stability

As the stability plays an inevitable role in deciding whether or not new materials can exist under certain conditions, some important values are analyzed in de- tail to examine the mechanical, dynamic, and thermo- dynamic stability of the new crystals. The calculated elastic constants, the elastic moduli of $\text{C}_3$, $\text{Si}_3$, and $\text{Ge}_3$ in $P6_222$ phase and in diamond phase are listed in Ta- ble 2. The structure in this work consists of five inde- pendent elastic constants ($C_{11}$, $C_{33}$, $C_{44}$, $C_{12}$, and $C_{13}$), and these elastic constants obey the following generalized Born's mechanical stability criteria for hexagonal crystals as shown:$^{[50]}$ $C_{11}$>0, $C_{44}$>0, $C_{11}$>$|C_{12}|$, $(C_{11}+C_{22})C_{33}-2C_{13}^2$ >0, which indicates these new crystals are mechan-

ically stable.

As for the elastic moduli, which refer to the bulk modulus $B$, shear modulus $G$, Young's modulus $E$, and Poisson's ratio $v$, they are obtained by different methods. Bulk modulus $B$ and shear modulus $G$ are achieved using the Voigt-Reuss-Hill approximation, where $B$ is the arithmetic mean of $B_R$ and $B_V$, $G$ the arithmetic mean of $G_R$ and $G_V$. For Young's modulus $E$, and Poisson's ratio $v$, these two values are calculated based on $E$=$9BG/(3B+G)$, $v$=$(3B-2G)/(6B+G),^{[51-52]}$ respectively. For the $P6_222$ phase, the elastic constants and the elastic moduli including $B$, $G$, and $E$ are decreased basically in the sequence of $C_3$, $Si_3$, and $Ge_3$. By comparing the elastic constants $C_{11}$, $C_{44}$, and $C_{12}$ with those of diamond phase, it is found that $C_{11}$ of $P6_222$ phase ($C_3$: 1161 GPa, $Si_3$: 185 GPa, and $Ge_3$: 123 GPa) is slightly larger than that of diamond phase (C: 1053 GPa, Si: 165 GPa, and Ge: 121 GPa), whereas $C_{44}$ and $C_{12}$ of $P6_222$ phase are all smaller than those of diamond phase, respectively. In addition, the elastic moduli of diamond-C, -Si, and -Ge are compared with Refs. [48] and [49], and the values are clearly in excellent agreement with reported experimental data. Moreover, Pugh$^{[53]}$ proposed that the ratio of bulk to shear modulus ($B/G$) is an indicator distinguishing between the ductility and brittleness of crystal materials, that materials usually show obvious ductile property with a $B/G$ value greater than 1.75, otherwise the brittle property exhibited. Also, it should be noted that Poisson's ratio $v$ is basically related to the $B/G$ value, and thus $v$ can be used to quantify the malleability. The ductile property will be displayed with $v$ greater than 0.26, and in contrast the brittleness will behave with $v$ less than 0.26.$^{[54]}$

From Table 2, it can be seen that all of $v$ are less than 0.26, and hence all materials demonstrate the brittle feature. This is consistent with the discussion above about the implication of $B/G$ value, since diamond-Ge has the maximum $B/G$ value equaling 1.46 among all materials (and the maximum $v$ of 0.22 as well). Therefore, it is easily found that diamond-Ge has the most brittle feature, while $P6_222$-$C_3$ has the least brittle feature.

Dynamic stabilities of $P6_222$-$Si_3$ and $-Ge_3$ are verified by their phonon dispersion spectra calculations at ambient pressure as illustrated in Fig. 2, and can be seen there are no imaginary frequencies at any wave vectors, indicating $P6_222$-$Si_3$ and $-Ge_3$ are dynamically stable. Then, the relative enthalpies of $P6_222$-$Si_3$ and $-Ge_3$ are calculated to investigate their thermodynamic stabilities. The relative enthalpies are obtained by the formula of $\Delta H$=$H_{\text{newphase}}/n_1$-$H_{\text{diamond-Si(Ge)}}/n_2$, where $n_1$ and $n_2$ are the number of Si (Ge) atoms in the new phase and diamond phase, respectively.

Figure 3 shows the calculated relative enthalpies of reported silicon structures including $C2/m$-$16$ Si,$^{[23]}$ $hP12$-Si, $oF16$-Si,$^{[24]}$ lonsdaleite-Si,$^{[29]}$ $M$-Si, $Z$-Si,$^{[32]}$ and experimentally known $\beta$-Sn phase Si, compared to diamond-Si and $P6_222$-$Si_3$ at ambient pressure. It is found that diamond-Si remains the most stable than other phases at ambient pressure. The metastable lonsdaleite-Si is second to diamond phase in terms of thermodynamic stability, with the energy of 0.017 eV/atom.

![](./images/812743477371600896_2.jpg)

Fig. 2 (Color online) The phonon spectra of $Si_3$ and $Ge_3$ in $P6_222$ phase at ambient pressure.

![](./images/812743477371600896_3.jpg)

Fig. 3 (Color online) Calculated enthalpies of different Si structures compared to diamond-Si at ambient pressure.

The newly predicted crystal $P6_222$-Si$_3$ is higher in energy than diamond-Si by 0.198 eV/atom. By comparison with $t$P16-Si,$^{[24]}$ it is seen that $t$P16-Si is higher in energy than diamond-Si by 0.269 eV/atom, which is 35.9% energetically higher than our $P6_222$-Si$_3$. And $P2_13$-Si$^{[17]}$ is higher in energy than our $P6_222$-Si$_3$ by 0.102 eV/atom, which is due to the reason that a more severe distortion of the tetrahedron in the metastable structure leads to higher energies. For $P6_222$-Ge$_3$, it is higher in energy than diamond-Ge by a smaller value of 0.168 eV/atom. Generally, it can be concluded that the new crystals are thermodynamically stable.

### 3.3 Mechanical Anisotropy Properties
The mechanical anisotropy is one of the most important properties in crystal materials. The anisotropy of crystal lattice along different directions, which is due to the arrangement of atoms with periodic and different stacking spares degrees, leads to a variety of crystal properties along different axes, for instance the hardness, fracture resistance, thermal expansion coefficient, thermal conductivity, mobility, effective mass, and elastic modulus. Also, it is well known that the mechanical anisotropy is an important implication in engineering science and crystal physics, and detailed analysis about this issue is especially helpful to understand the mechanisms of crystal materials' micro-cracks and durability.

Firstly, we focus on the three-dimensional (3D) surface construction of Young's modulus $E$ for C$_3$, Si$_3$, and Ge$_3$ in $P6_222$ phase as shown in Fig. 4, and it can be used as an effective tool to directly describe the mechanical anisotropy of these three Group IV element allotropes. For an isotropic structure, the 3D image should exhibit a spherical shape, which indicates the physical, chemical and other natural aspects of the material will not change to different directions. When the deviation from the spherical shape occurs, the anisotropic property will show,$^{[55]}$ and it is self-evident that the amount of deviation from the spherical shape reflects the level of anisotropy. Clearly, $P6_222$-Si$_3$ and -Ge$_3$ exhibit the greater anisotropy than $P6_222$-C$_3$, as the 3D surface construction of Young's modulus for $P6_222$-C$_3$ appears almost in a perfect spherical shape shown in Fig. 4(a). However, it is difficult to compare $P6_222$-Si$_3$ with -Ge$_3$ regarding the anisotropy, as the deviations from the spherical shape shown in Figs. 4(b) and 4(c) are very similar. Therefore, the two-dimensional (2D) representation of Young's modulus is used to make a more detailed analysis in different planes, which can give us a quantitative assessment of C$_3$, Si$_3$, and Ge$_3$ in $P6_222$ phase in terms of anisotropic properties.

In Fig. 5, the black-, red-, blue-, and green- lines depict the value of Young's modulus in the (001), (010), (100), and (111) planes, respectively. It can be obviously seen in Fig. 5(a) that the 2D representations of Young's modulus for $P6_222$-C$_3$ in the four planes are almost the same in a circular shape, indicating the greatest isotropy than that of $P6_222$-Si$_3$ and -Ge$_3$. Interestingly, both of $P6_222$-Si$_3$ and -Ge$_3$ also show the isotropic property in the (001) plane with only one value of Young's modulus existed (Si$_3$: 159 GPa and Ge$_3$: 106 GPa), as we can clearly see from Figs. 5(b) and 5(c) that the black line indeed forms a perfect circle.

![](./images/812743477371600896_4.jpg)

Fig. 4 (Color online) The directional dependence of Young's modulus for C$_3$ (a), Si$_3$ (b), and Ge$_3$ (c) in $P6_222$ phase.

![](./images/812743477371600896_5.jpg)

Fig. 5 (Color online) 2D representation of Young's modulus for C₃ (a), Si₃ (b), and Ge₃ (c) in P6₂22 phase. The black-, red-, blue-, and green-lines depict the value of Young's modulus in the (001), (010), (100), and (111) planes, respectively.

At the same time, it is found that the (010) and (100) planes are similar in Young's modulus for both of P6₂22-Si₃ and -Ge₃ as the red and blue lines are symmetrically displayed. By comparing the ratios of the maximum Young's modulus ($E_{\text{max}}$) to the minimum Young's modulus ($E_{\text{min}}$) among the four planes, it is also found that both P6₂22-Si₃ and -Ge₃ have the greatest anisotropy appearing in the (010) and (100) planes with the largest $E_{\text{max}}/E_{\text{min}}$ value of 1.40 (Si₃: 177/126) and 1.36 (Ge₃: 124/91), respectively. Finally, we can draw the conclusion related to the anisotropic properties in different planes that all of the three crystals exhibit the isotropy in the (001) plane, and P6₂22-Si₃ shows the greatest anisotropy appearing in the (010) and (100) planes.

Then, the universal anisotropic index $A^{U}$ is used to further analyze the anisotropy of these three crystals. In this work, the parameters ($A^{U}$) of the three crystals including C₃, Si₃, and Ge₃ in P6₂22 phase are calculated. The equation of $A^{U}$ combines the shear and bulk modulus based on the Voigt and Reuss averages, expressed as $A^{U}{=5G_{V}/G_{R}{+B_{V}/B_{R}}-6,^{[56]}}$ where the subscript $V$ denotes the Voigt approximation and the subscript $R$ represents the Reuss approximation. For an isotropic structure, $A^{U}$ must be 0; and any fluctuation the value of $A^{U}$ varies from 0, the anisotropic property shows. The bulk modulus $B$ of P6₂22-Si₃ is $B_{V}$=94.411 GPa when using the Voigt approximation and $B_{R}$=94.231 GPa when using the Reuss approximation. For P6₂22-Ge₃, $B_{V}$=63.927 GPa, and $B_{R}$=63.917 GPa, it can be seen that the difference in bulk modulus between $B_{V}$ and $B_{R}$ is significantly small for both P6₂22-Si₃, and -Ge₃. While for P6₂22-Si₃, the difference (1.696 GPa) in shear modulus between the $G_{V}$ (69.087 GPa) and $G_{R}$ (67.391 GPa) is greater compared to that in bulk modulus. And for P6₂22-Ge₃, the difference between the $G_{V}$ (48.130 GPa) and $G_{R}$ (46.985 GPa) is 1.145 GPa. Through calculation, it is found that the $A^{U}$ values of C₃, Si₃, and Ge₃ in P6₂22 are 0.001, 0.128, and 0.122, respectively. Thus, P6₂22-Si₃ has the greatest anisotropy as the $A^{U}$ is the largest, and P6₂22-C₃ has the least anisotropy as the $A^{U}$ is nearly equal to 0. Obviously, what the results show is consistent with the description in terms of Young's modulus above.

Lastly, the shear anisotropy factors $A_1$, $A_2$, and $A_3$ are utilized, which provide a measurement of mechanical anisotropy degree in the bonding between atoms in different planes, to better characterize the anisotropy of the newly predicted crystals. The equations of $A_1$, $A_2$ and $A_3$ are expressed as:$^{[57]}$ $A_1$=$4C_{44}/(C_{11}{+C_{33}}{-2C_{13}})$, $A_2$=$4C_{55}/(C_{22}{+C_{33}}{-2C_{23}})$, and $A_3$=$4C_{66}/(C_{11}{+C_{22}}{-2C_{12}})$, where $A_1$ represents the [011] to [010] direction in the (100) shear plane, $A_2$ represents the [101] to [001] direction in the (010) shear plane, and $A_3$ represents the [110] to [010] in the (001) shear plane. In hexagonal symmetry, $A_1$ is equal to $A_2$. For an isotropic structure, these three factors of $A_1$, $A_2$, and $A_3$ must be 1.00, and any fluctuation of these values indicates the content of anisotropy. Furthermore, another five bulk moduli ($A_{Ba}$, $A_{Bc}$, $B_a$, $B_b$, and $B_c$) are considered together with $A_1$, $A_2$, and $A_3$ to describe the anisotropy of crystals. The equations of $A_{Ba}$ and $A_{Bc}$, expressed as below,$^{[58]}$ are the bulk moduli along the $a$-axis and $c$-axis with respect to $b$-axis, respectively, when with the value of 1.00, indicating the isotropic property exhibited. $B_a$, $B_b$, and $B_c$ are the bulk moduli along $a$, $b$, and $c$ axes, which are also listed below.$^{[58]}$ From Table 3, it is seen that C₃, Si₃, and Ge₃ in P6₂22 phase exhibit the anisotropy symmetrically along $a$-axis and $b$-axis, and P6₂22-Si₃ has the greatest anisotropy in the (100) and (010) shear planes, while P6₂22-C₃, -Si₃, and -Ge₃ exhibit almost the isotropy in the (001) shear plane. And the anisotropy in the (100) and (010) shear planes increases in the sequence of C₃, Si₃ and Ge₃. Again, what the data show in Table 3 is obviously consistent with the mechanical anisotropy discussion as mentioned before.

Table 3 The shear anisotropic factors $A_1$, $A_2$, and $A_3$, and the bulk moduli $A_{B_a}$, $A_{B_c}$, $B_a$, $B_b$, and $B_c$ of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase.

|     | $A_1$ | $A_2$ | $A_3$ | $A_{B_a}$ | $A_{B_c}$ | $B_a$/GPa | $B_b$/GPa | $B_c$/GPa |
|-----|-------|-------|-------|-----------|-----------|-----------|-----------|-----------|
| $C_3$ | 0.97  | 0.97  | 1.00  | 1.00      | 0.96      | 1293.90   | 1293.90   | 1244.10   |
| $Si_3$ | 1.41  | 1.41  | 1.00  | 1.00      | 0.87      | 296.23    | 296.23    | 257.59    |
| $Ge_3$ | 1.39  | 1.39  | 0.99  | 1.00      | 1.05      | 189.74    | 189.74    | 199.23    |

$$
A_{B_{a}}=\frac{B_{a}}{B_{b}},\tag{1}
$$

$$
A_{B_{c}}=\frac{B_{c}}{B_{b}},\tag{2}
$$

$$
B_{a}=a \frac{\mathrm{d} P}{\mathrm{~d} a}=\frac{\wedge}{1+\alpha+\beta},\tag{3}
$$

$$
B_{b}=b \frac{\mathrm{d} P}{\mathrm{~d} b}=\frac{B_{a}}{\alpha},\tag{4}
$$

$$
B_{c}=c \frac{\mathrm{d} P}{\mathrm{~d} c}=\frac{B_{a}}{\beta},\tag{5}
$$

$$
\wedge=C_{11}+2 C_{12} \alpha+C_{22} \alpha^{2}+2 C_{13} \beta+C_{33} \beta^{2}+2 C_{23} \alpha \beta,\tag{6}
$$

$$
\alpha=\frac{\left(C_{11}-C_{12}\right)\left(C_{33}-C_{13}\right)-\left(C_{11}-C_{12}\right)\left(C_{33}-C_{13}\right)}{\left(C_{33}-C_{13}\right)\left(C_{22}-C_{12}\right)-\left(C_{11}-C_{12}\right)\left(C_{33}-C_{13}\right)},\tag{7}
$$

$$
\beta=\frac{\left(C_{22}-C_{12}\right)\left(C_{11}-C_{13}\right)-\left(C_{11}-C_{12}\right)\left(C_{23}-C_{12}\right)}{\left(C_{22}-C_{12}\right)\left(C_{33}-C_{13}\right)-\left(C_{12}-C_{23}\right)\left(C_{13}-C_{23}\right)}.\tag{8}
$$

### 3.4 Electronic Properties

As the electronic band structure describes the forbidden or allowed energy of electrons caused by the quantum dynamics of electron diffraction in periodic lattices, many fundamental properties of materials in solid-state physics can be further investigated by analyzing the electronic band structure. Therefore, the electronic band structures of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase are examined shown in Fig. 6. As can be seen, the dashed line represents the Fermi level (0 eV), and the minimal-energy state in the conduction band and the maximum-energy state in the valence band are each characterized by a certain crystal momentum ($k$-vector) in the Brillouin zone. It can be found that the valence band maximums (VBMs) of both $P6_222$-$C_3$ and -$Si_3$ are located at the A point, and the conduction band minimums (CBMs) are located at the M point. Therefore, both $P6_222$-$C_3$ and -$Si_3$ are indirect band gap semiconductors, and with the band gap of 2.88 eV and 0.28 eV, respectively. As shown in Fig. 6(c), the CBM of $P6_222$-$Ge_3$ is located at the K point; however its valence bands along A-H direction show the metallic feature as the top dispersive band crossing the Fermi level to the upper region with positive energies.

![](./images/812743477371600896_6.jpg)

Fig. 6 (Color online) The electronic band structures of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase.

### 3.5 Thermodynamic Properties

The Debye temperature $\Theta_D$, sound velocities, and the thermal conductivity $\kappa_{\text{min}}$ are primarily discussed in this work to evaluate the thermodynamic properties of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase. Debye temperature $\Theta_D$ can be obtained by formula (9) as below:$^{[60]}$

$$
\Theta_{D}=\frac{h}{k_{B}}\left[\frac{3 n}{4 \pi}\left(\frac{N_{A} \rho}{M}\right)\right]^{1 / 3} v_{m}, \quad(9)
$$

where $h$ is Planck's constant, $k_{B}$ is Boltzmann's constant, $n$ is the number of atoms in the molecule, $N_{A}$ is Avogadro's number, $\rho$ is the density, and $M$ is the molecular weight. In this formula, $v_{m}$ represents the mean sound velocity, which is expressed by formula (10): $^{[60]}$

$$
v_{m}=\frac{1}{3} \sum_{i=1}^{3} \int \frac{1}{v_{i}^{3}(\theta, \varphi)} \frac{\mathrm{d} \Omega}{4 \pi}=\left[\frac{1}{3}\left(\frac{1}{v_{l}^{3}}+\frac{2}{v_{t}^{3}}\right)\right]^{-1 / 3}, \quad(10)
$$

where $\theta$ and $\varphi$ are angular coordinates ($\mathrm{d} \Omega=\sin \theta \mathrm{d} \theta \mathrm{d} \varphi$). $v_{l}$ and $v_{t}$ are the longitudinal and transverse sound velocities, respectively. If the bulk modulus $B$, shear modulus $G$, and the density $\rho$ of crystals are known, these two parameters can be simply calculated by Navier's equation, expressed as $v_{l}=[(3 B+4 G) / 3 \rho]^{1 / 2}$ and $v_{t}=(G / \rho)^{1 / 2} \cdot{ }^{[61]}$

<table>
<caption>Table 4 The Debye temperature ($\Theta_D$ in K), and the longitudinal, transverse, mean sound velocity ($v_l$, $v_t$, and $v_m$ in m/s) of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase.</caption>
<thead>
<tr>
<th>Space group</th>
<th></th>
<th>$\Theta_D$</th>
<th>$v_l$</th>
<th>$v_t$</th>
<th>$v_m$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$P6_222$</td>
<td>$C_3$</td>
<td>2141</td>
<td>17727</td>
<td>12168</td>
<td>13251</td>
</tr>
<tr>
<td></td>
<td>$Si_3$</td>
<td>625</td>
<td>8470</td>
<td>5140</td>
<td>5679</td>
</tr>
<tr>
<td></td>
<td>$Ge_3$</td>
<td>345</td>
<td>4761</td>
<td>2916</td>
<td>3219</td>
</tr>
<tr>
<td>$Fd$-$3m$</td>
<td>C</td>
<td>2230</td>
<td>17903</td>
<td>12184</td>
<td>13283</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$2220^a$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Si</td>
<td>639</td>
<td>8727</td>
<td>5303</td>
<td>5859</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$652^a$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Ge</td>
<td>360</td>
<td>5220</td>
<td>3119</td>
<td>3452</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$374^a$</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="6">$^{\mathrm{a}}$Ref. [59].</td>
</tr>
</tfoot>
</table>

The calculated Debye temperature and sound velocities of these three Group IV element allotropes in $P6_222$ phase and in diamond phase are listed in Table 4. Since densities of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase are correspondingly higher than those in diamond phase, while the bulk modulus and shear modulus of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase are slightly smaller than those in diamond phase (see Table 2), and consequently sound velocities ($v_l$, $v_t$, and $v_m$) of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase are all lower than those in diamond phase. Meanwhile, it is seen that the values of $\Theta_D$ in $P6_222$ phase are decreased from $C_3$ to $Ge_3$, and this is due to the fact that mean sound velocities acted as dominant factors are correspondingly reduced from $C_3$ to $Ge_3$. Moreover, it is found that the values of $\Theta_D$ in $P6_222$ phase are slightly smaller than those in diamond phase, and the values of $\Theta_D$ in diamond phase are in excellent agreement with the reported work. $^{[59]}$

Since sound waves travel at different speeds in different directions for crystal materials, anisotropic sound velocities need to be further discussed. According to Brugger, $^{[62]}$ the single-crystal elastic constants can be used to calculate the phase velocity in pure longitudinal and transverse modes. The directions associated with sound traveling in crystals are basically classified into two categories, as the propagation direction and the polarizing direction. For hexagonal symmetry, sound velocities along the [001] and [100] propagation direction can be obtained by formula (11) and (12), respectively, as listed: $^{[63]}$

$$
[001]:[001] v_{l}=\sqrt{\frac{C_{33}}{\rho}},
$$

$$
[100] v_{t 1}=[010] v_{t 2}=\sqrt{\frac{C_{44}}{\rho}}, \quad(11)
$$

$$
[100]:[100] v_{l}=\sqrt{\frac{C_{11}-C_{12}}{2 \rho}},
$$

$$
[010] v_{t 1}=\sqrt{\frac{C_{11}}{\rho}}, \quad[001] v_{t 2}=\sqrt{\frac{C_{44}}{\rho}}, \quad(12)
$$

where $v_l$ is the longitudinal sound velocity, and $v_{t1}$ and $v_{t2}$ are the transverse sound velocities in the first and second mode, respectively. As seen in these two formulas above, $C_{33}$ and $C_{44}$ determine the longitudinal and transverse sound velocities along the [001] propagation direction, respectively, and $C_{11}$ and $C_{44}$ dominate sound velocities along the [100] propagation direction. The calculated anisotropic sound velocities of $C_3$, $Si_3$, and $Ge_3$ in $P6_222$ phase are listed in Table 5. It can be seen that the highest sound velocity among these three Group IV element allotropes is 17843 m/s appeared in $P6_222$-$C_3$, and the lowest sound velocity is 2900 m/s appeared in $P6_222$-$Ge_3$, both of which are exhibited in the [100] propagation direction. In the [001] propagation direction, each of these three crystals demonstrates the symmetrical transverse sound velocity in the first and second mode. Meanwhile, it is obvious that the highest sound velocity along different directions is the longitudinal sound velocity in the [001] propagation direction, and the transverse sound velocity in the first mode in the [100] propagation direction. In addition, since the density of $P6_222$-$C_3$ (5.647 g/cm$^3$) is the highest while its elastic constants (see Table 2) are the smallest among these three crystals, its sound velocities along different directions are certainly lower than those of $P6_222$-$C_3$ and $Si_3$ as shown in Table 5. The sound velocities along different directions of $P6_222$-$C_3$ are all largely higher than those of $P6_222$-$Si_3$, which is due to the fact that the dominant elastic constants ($C_{11}$, $C_{33}$, and $C_{44}$) of $P6_222$-$C_3$ largely outweigh those of $P6_222$-$Si_3$, even though the density of $P6_222$-$Si_3$ (2.574 g/cm$^3$) smaller than that of $P6_222$-$C_3$ (3.647 g/cm$^3$).

The minimum thermal conductivity $\kappa_{\text{min}}$, which is another important physical parameter to evaluate the thermodynamic properties of materials, can be calculated based on Cahill's model by formula (13) as below: $^{[64]}$

$$
\kappa_{\text {min }}=\left(\frac{\pi}{6}\right)^{1 / 3} k_{B} N^{2 / 3} \sum_{i} v_{i}\left(\frac{T}{\Theta_{i}}\right)^{2}
$$

$$
\times \int_{0}^{\Theta_{i} / T} \frac{x^{3} \mathrm{e}^{x}}{\left(\mathrm{e}^{x}-1\right)^{2}} \mathrm{~d} x,
\tag{13}
$$

where $N$ is the number density of atoms, $v_{i}$ represents three sound wave velocities (including one longitudinal and two transverse sound wave velocities), and $\Theta_{i}$ expressed as $v_{i}[h/(2\pi k_{B})](6\pi^{2}N)^{1/3}$ is the cut-off frequency for each polarization. Figure 7 shows the variations of the minimum thermal conductivities $\kappa_{\text{min}}$ affected by the temperature (from 0 K to 2000 K) of $\text{C}_{3}$, $\text{Si}_{3}$, and $\text{Ge}_{3}$ in $P6_{2}22$ phase. It is seen that $\kappa_{\text{min}}$ is increased in the sequence of $\text{C}_{3}$, $\text{Si}_{3}$, and $\text{Ge}_{3}$ in low temperature region (0 K $<T<$ 110 K), while $\kappa_{\text{min}}$ of $P6_{2}22$–$\text{C}_{3}$ begins to be far larger than those of $P6_{2}22$–$\text{Si}_{3}$ and –$\text{Ge}_{3}$ above 230 K. In high temperature region ($T>$ 800 K), the minimum thermal conductivities of $P6_{2}22$–$\text{Si}_{3}$ and –$\text{Ge}_{3}$ are almost constant, and $\kappa_{\text{min}}$ of $P6_{2}22$–$\text{Si}_{3}$ is steadily larger than that of $P6_{2}22$–$\text{Ge}_{3}$. Among these three Group IV element allotropes, $P6_{2}22$–$\text{C}_{3}$ owns the largest value of $\kappa_{\text{min}}$ (1.70 W/cmK), while $P6_{2}22$–$\text{Ge}_{3}$ owns the smallest value of $\kappa_{\text{min}}$ (0.71 W/cmK) at 300 K.

Table 5 The calculated anisotropic sound velocities (in m/s) of $\text{C}_{3}$, $\text{Si}_{3}$, and $\text{Ge}_{3}$ in $P6_{2}22$ phase.

<table>
  <thead>
    <tr>
      <th>Propagation direction</th>
      <th colspan="3">[001]</th>
      <th colspan="3">[100]</th>
    </tr>
    <tr>
      <th>Polarization direction</th>
      <th>[001]$v_{l}$</th>
      <th>[100]$v_{t1}$</th>
      <th>[010]$v_{t2}$</th>
      <th>[100]$v_{l}$</th>
      <th>[010]$v_{t1}$</th>
      <th>[001]$v_{t2}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\text{C}_{3}$</td>
      <td>17696</td>
      <td>12101</td>
      <td>12101</td>
      <td>12174</td>
      <td>17843</td>
      <td>12101</td>
    </tr>
    <tr>
      <td>$\text{Si}_{3}$</td>
      <td>7785</td>
      <td>5505</td>
      <td>5505</td>
      <td>5214</td>
      <td>8478</td>
      <td>5505</td>
    </tr>
    <tr>
      <td>$\text{Ge}_{3}$</td>
      <td>4473</td>
      <td>3121</td>
      <td>3121</td>
      <td>2900</td>
      <td>4667</td>
      <td>3121</td>
    </tr>
  </tbody>
</table>

![](./images/812743477371600896_7.jpg)

Fig. 7 (Color online) The minimum thermal conductivities $\kappa_{\text{min}}$ of $\text{C}_{3}$, $\text{Si}_{3}$, and $\text{Ge}_{3}$ in $P6_{2}22$ phase.

Furthermore, the minimum thermal conductivities are studied in detail by analyzing them in different primary directions. The values of $\kappa_{\text{min}}$ in different directions at 300 K are all listed in Table 6. As can be seen, the values of $\kappa_{\text{min}}$ in primary directions are all slightly larger than those in all directions, and the values of $\kappa_{\text{min}}$ in the [001] direction are generally equal to those in the [100] direction. Moreover, the minimum thermal conductivities of $\text{C}_{3}$, $\text{Si}_{3}$, and $\text{Ge}_{3}$ in $P6_{2}22$ phase are compared with those in diamond phase. It is obviously shown that $\kappa_{\text{min}}$ of $P6_{2}22$–$\text{C}_{3}$ and –$\text{Ge}_{3}$ are very close to those of diamond–C and –Ge, while $\kappa_{\text{min}}$ of $P6_{2}22$–$\text{Si}_{3}$ is slightly larger than that of diamond–Si. In addition, by comparing $\kappa_{\text{min}}$ of $P6_{2}22$–$\text{Si}_{3}$ with other related silicon allotropes including $C2/m$-16 Si, $C2/m$-20 Si, $P2_{1}/m$ Si and $I4_{1}/amd$ t–$\text{Si}_{64}$, it is found that for most of silicon allotropes, their minimum thermal conductivities are approximately equal to 1 W/cmK.$^{[25]}$ Since the minimum thermal conductivities of $\text{C}_{3}$, $\text{Si}_{3}$, and $\text{Ge}_{3}$ in $P6_{2}22$ phase are all close to those of diamond–C, –Si, and –Ge, it is known that these three Group IV element allotropes have great thermal conductivity and can be used as materials of microelectronic devices due to their good heat radiation characteristics.

Table 6 The minimum thermal conductivities ($\kappa_{\text{min}}$ in W/cmK) in all directions and in different primary directions of $\text{C}_{3}$, $\text{Si}_{3}$, and $\text{Ge}_{3}$ in $P6_{2}22$ phase at 300 K.

<table>
  <thead>
    <tr>
      <th>Space group</th>
      <th></th>
      <th>All</th>
      <th>[001]</th>
      <th>[100]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$P6_{2}22$</td>
      <td>$\text{C}_{3}$</td>
      <td>1.70</td>
      <td>1.72</td>
      <td>1.71</td>
    </tr>
    <tr>
      <td></td>
      <td>$\text{Si}_{3}$</td>
      <td>1.18</td>
      <td>1.20</td>
      <td>1.20</td>
    </tr>
    <tr>
      <td></td>
      <td>$\text{Ge}_{3}$</td>
      <td>0.71</td>
      <td>0.72</td>
      <td>0.72</td>
    </tr>
    <tr>
      <td>$Fd-3m$</td>
      <td>C</td>
      <td>1.68</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Si</td>
      <td>1.13</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Ge</td>
      <td>0.72</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

## 4 Conclusion

Two new Group IV element allotropes $\text{Si}_{3}$ and $\text{Ge}_{3}$ in $P6_{2}22$ phase were reported in this work. First-principles computations were utilized to investigate the physical properties, including the structural properties, stability, mechanical anisotropy properties, electronic properties, and thermodynamic properties. There are three atoms per conventional cell of the crystal structure in hexagonal symmetry, and densities of the newly predicted crystals are correspondingly higher than those in diamond phase.

The mechanical, dynamic, and thermodynamic stabilities of the newly predicted crystals were verified. By plotting the 3D and 2D directional dependence of Young's modu- lus, discussing the universal anisotropic index, and calcu- lating shear anisotropy factors together with bulk moduli, we found that $P6_{2}22-Si_{3}$ exhibits the greatest anisotropy while $P6_{2}22-C_{3}$ exhibits the isotropy, and interestingly all these three Group IV element allotropes in $P6_{2}22$ phase appear to be isotropic in the (001) plane. Furthermore, the electronic band structures were calculated by HSE06 hybrid functional, indicating that $P6_{2}22-C_{3}$ and $-Si_{3}$ are indirect band gap semiconductors with the band gap of 2.88 eV and 0.28 eV, respectively, and $P6_{2}22-Ge_{3}$ exhibit ing the metallic feature. Lastly, the thermodynamic prop- erties of $C_{3}, Si_{3}$ , and $Ge_{3}$ in $P6_{2}22$ phase were discussed, and it was found that these three Group IV element al- lotropes have possible applications in microelectronic in- dustry due to their great thermal conductivity.

## References

[1] Q. Wei, Q. Zhang, H. Y. Yan, and M. G. Zhang, J. Mater. Sci. 52 (2017) 2385.
[2] M. J. Xing, B. H. Li, Z. T. Yu, and Q. Chen, J. Mater. Sci. 50 (2015) 7104.
[3] M. J. Xing, B. H. Li, Z. T. Yu, and Q. Chen, Commun. Theor. Phys. 64 (2015) 237.
[4] M. G. Zhang, Q. Wei, H. Y. Yan, *et al.*, Phys. Chem. C 118 (2014) 3202.
[5] Y. G. Guo, Q. Wang, Y. Kawazoe, and P. Jena, Sci. Rep. 5 (2016) 14342.
[6] Q. Y. Fan, C. C. Chai, Q. Wei, and Y. T. Yang, Phys. Chem. Chem. Phys. 18 (2016) 12905.
[7] D. Y. Kim, S. Stefanoski, O. O. Kurakevych, and T. A. Strobel, Nat. Mater. 14 (2015) 169.
[8] Q. Y. Fan, C. C. Chai, Q. Wei, *et al.*, J. Solid. State. Chem. 233 (2016) 471.
[9] S. Q. Wang and H. Q. Ye, J. Phys. Condens. Matter 15 (2003) L197.
[10] S. Q. Wang and H. Q. Ye, J. Phys. Condens. Matter 15 (2003) 5307.
[11] Q. Wei, Q. Zhang, M. G. Zhang, *et al.*, Front. Phys. 13 (2018) 136105.
[12] J. T. Wang, C. F. Chen, E. Wang, and Y. Kawazoe, Sci. Rep. 4 (2014) 4339.
[13] M. J. Xing, B. H. Li, Z. T. Yu, and Q. Chen, Materials 9 (2016) 484.
[14] K. Umemoto, R. M. Wentzcovitch, S. Saito, and T. Miyake, Phys. Rev. Lett. 104 (2010) 125504.
[15] Q. Wei, M. G. Zhang, H. Y. Yan, *et al.*, Europhys. Lett. 107 (2014) 27007.
[16] Q. Y. Fan, C. C. Chai, Q. Wei, *et al.*, J. Mater. Sci. 53 (2018) 2785.
[17] H. J. Xiang, B. Huang, E. J. Kan, *et al.*, Phys. Rev. Lett. 110 (2013) 118702.
[18] C. P. Tang, J. Cao, and S. J. Xiong, Physica B Condens. Matter 466-467 (2015) 59.
[19] C. Y. He, C. X. Zhang, J. Li, *et al.*, Phys. Chem. Chem. Phys. 18 (2016) 9682.
[20] I. H. Lee, Y. J. Oh, S. Kim, *et al.*, Comput. Phys. Com- mun. 203 (2016) 110.
[21] M. Amsler, S. Botti, M. A. L. Marques, *et al.*, Phys. Rev. B 92 (2015) 014101.
[22] L. A. Jantke, S. Stegmaier, A. J. Karttunen, and T. F. Fassler, Chem. Eur. J. 23 (2017) 2734.
[23] Q. Y. Fan, C. C. Chai, Q. Wei, *et al.*, J. Appl. Phys. 118 (2015) 185704.

[24] Q. Q. Wang, B. Xu, J. Sun, *et al.*, J. Am. Chem. Soc. 136 (2014) 9826.
[25] Q. Y. Fan, R. Niu, W. Z. Zhang, *et al.*, Chem. Phys. Chem. 20 (2019) 128.
[26] Q. Y. Fan, C. C. Chai, Q. Wei, *et al.*, Mater. Des. 132 (2017) 539.
[27] Q. Y. Fan, C. C. Chai, Q. Wei, *et al.*, Mater. Sci. Semi- cond. Process. 43 (2016) 187.
[28] A. Mujica, C. J. Pickard, and R. J. Needs, Phys. Rev. B 91 (2015) 21410.
[29] A. De and C. Y. Pryor, J. Phys. Condens. Matter 26 (2014) 045801.
[30] M. C. Nguyen, X. Zhao, C. Z. Wang, and K. M. Ho, Phys. Rev. B 89 (2014) 184112.
[31] V. A. Saleev, A. V. Shipilova, D. M. Proserpio, and G. Fadda, Eur. Phys. J. B 90 (2017) 150.
[32] A. Bautista-Hernandez, T. Range, A. H. Romero, *et al.*, J. Appl. Phys. 113 (2013) 193504.
[33] Q. Zhu, A. R. Oganov, M. A. Salvado, *et al.*, Phys. Rev. B 83 (2011) 193410.
[34] P. Hohenberg and W. Kohn, Phys. Rev. 136 (1964) B864.
[35] W. Kohn and L. J. Sham, Phys. Rev. 140 (1965) A1133.
[36] S. J. Clark, M. D. Segall, C. J. Pickard, *et al.*, Z. Kristal- logr. 220 (2005) 567.
[37] J. P. Perdew, K. Burk, and M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.
[38] D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45 (1980) 566.
[39] P. Perdew and A. Zunger, Phys. Rev. B 23 (1981) 5048.
[40] B. G. Pfrommer, M. Cote, S. G. Louie, and M. L. Cohen, J. Comput. Phys. 131 (1997) 233.
[41] S. Baroni, S. De Gironcoli, A. Dal Corso, and P. Gian- nozzi, Rev. Mod. Phys. 73 (2001) 515.
[42] J. Heyd, G. E. Scuseria, and M. J. Ernzerhof, J. Chem. Phys. 118 (2003) 8207.
[43] H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13 (1976) 5188.
[44] M. L. Petrescu, Diam. Relat. Mater. 13 (2004) 1848.
[45] D. R. Lide, *Handbook of Chemistry and Physics*, 73rd ed, Chemical Rubber, Florida (1994).
[46] M. L. Cohen, Phys. Rev. B 32 (1985) 7988.
[47] Z. Z. Li, J. T. Wang, L. F. Xu, and C. F. Chen, Phys. Rev. B 94 (2016) 174102.
[48] M. Grimsditch, E. S. Zouboulis, and A. Polian, J. Appl. Phys. 76 (1994) 832.
[49] R. Gomez-Abal, X. Li, M. Scheffler, and C. Ambrosch- Draxl, Phys. Rev. Lett. 101 (2008) 106404.

[50] B. B. Karki, G. J. Ackland, and J. Crain, J. Phys. Con- dens. Matter **9** (1997) 8579.

[51] R. Hill, Proc. Phys. Soc. Lond. Sect. A **65** (1952) 349.

[52] Q. Y. Fan, W. Z. Zhang, S. N. Yun, *et al.*, Chem. Eur. J. **24** (2018) 17280.

[53] S. F. Pugh, Philos. Mag. **45** (1954) 823.

[54] Q. Y. Fan, Q. Wei, H. Y. Yan, *et al.*, Acta Phys. Pol. A **126** (2014) 740.

[55] W. C. Hu, Y. Liu, D. J. Li, *et al.*, Comput. Mater. Sci. **83** (2014) 27.

[56] S. I. Ranganathan and M. Ostoja-Starzewski, Phys. Rev. Lett. **101** (2008) 055504.

[57] Q. Y. Fan, Q. Wei, H. Y. Yan, *et al.*, Comput. Mater. Sci. **85** (2014) 80.

[58] P. Ravindran, L. Fast, P. A. Korzhavyi, *et al.*, J. Appl. Phys. **84** (1998) 4891.

[59] H. Siethoff and K. Ahiborn, Phys. Status. Solidi. B **190** (1995) 179.

[60] O. L. Anderson, J. Phys. Chem. Solids. **24** (1963) 909.

[61] K. B. Panda and K. S. Ravi, Comput. Mater. Sci. **35** (2006) 134.

[62] K. Brugger, J. Appl. Phys. **36** (1965) 768.

[63] Y. H. Duan, Y. Sun, M. J. Peng, and S. G. Zhou, J. Alloys. Compd. **595** (2014) 14.

[64] D. G. Cahill, K. S. Wastson, and R. O. Pohl, Phys. Rev. B **46** (1992) 6131.