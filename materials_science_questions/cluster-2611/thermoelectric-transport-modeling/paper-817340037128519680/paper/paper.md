Journal of Physics: Condensed Matter

ACCEPTED MANUSCRIPT

# Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A computational study

To cite this article before publication: Enamullah Enamullah *et al* 2020 *J. Phys.: Condens. Matter* in press https://doi.org/10.1088/1361-648X/ab96f0

Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2020 IOP Publishing Ltd.

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere.
As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the article online for updates and enhancements.

This content was downloaded from IP address 128.83.214.19 on 31/05/2020 at 14:35

# Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A computational study

Enamullah$^{1*}$, Sunil Kumar Sharma$^{2*}$ and Sameh S Ahmed $^{3,4}$

$^{1}$Department of Physics, School of Applied Sciences
University of Science and Technology, Meghalaya, India- 793101
$^{2}$ College of Computer and Information Science,
Majmaah University, Majmaah, Saudi Arabia- 11952
$^{3}$ Department of Civil and Environmental Engineering,
Majmaah University, Majmaah, Saudi Arabia- 11952
$^{4}$ On leave: Department of Mining Engineering
Assiut University, Egypt

E-mail: enamiitg09@gmail.com and s.sharma@mu.edu.sa

Abstract. A systematic study of electronic structure, mechanical and transport properties of RuV-based half-Heusler alloys (RuVZ, Z=As, P, Sb) have been presented using *ab-initio* Density Functional and Boltzmann transport theory. The electronic structures are obtained using generalized gradient approximation(GGA) with Perdew-Burke-Ernzerhof(PBE) functional. All the compounds are crystallized in face centered cubic(fcc) phase with space group #216. Our preliminary electronic structure simulations reveal that all the alloys are non-magnetic semiconductors. Additionally, the phonon dispersion and elastic constants (along with the related elastic moduli) also verify mechanical stability of the alloys. Due to strong dependence on the electronic bandgap in thermoelectric materials, we have estimated bandgap using more accurate hybrid functional i.e. Heyd-Scuseria-Ernzerhof(HSE). The transport coefficients (e.g. Seebeck, electrical conductivity, thermal conductivity due to electrons) are calculated by solving the Boltzmann transport equation for charge carriers as implemented in BoltzTraP software under constant relaxation time approximation. The lattice thermal conductivity due to phonons is calculated using more reliable shengBTE code based upon the Boltzmann transport equation for phonons. We have calculated the more reliable value of the thermoelectric figure of merit, $ZT$ (related to the conversion efficiency) for all the compounds. The obtained $ZT$ for RuVAs, RuVP and RuVSb is 0.41(0.32), 0.21(0.16) and 0.70(0.61) for $p(n)$-type behavior at $900K$. The corresponding carrier concentrations are also predicted. High value of $ZT$ is obtained for RuVSb alloy due to low lattice thermal conductivity. Among these compounds, RuVSb emerged out as a most suitable candidate for thermoelectric power generation device. Minimum lattice thermal conductivity in theoretical limit along with the corresponding maximum value of $ZT$ is also predicted in these alloys.

PACS numbers: 31.15.A-, 85.75.-d, 75.50.Cc, 61.72.-y

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

Keywords: Ab-initio simulations, Heusler alloys, Halfmetallicity, Intrinsic defects
Submitted to: J. Phys. A: Math. Gen.

### 1. Introduction

Thermoelectric materials are most researched stuff among the scientific community due to conversion efficiency from waste heat into useful electrical energy. The conversion efficiency($\eta_m$) of thermoelectric device is related to the intrinsic property of material (known as dimensionless figure of merit, $ZT$) as,

$$
\eta_{m}=\frac{\sqrt{(1+Z T)}-1}{\sqrt{(1+Z T)}+\left(\frac{T_{1}}{T_{2}}\right)}\left(1-\frac{T_{1}}{T_{2}}\right),
$$

where, $\eta_m$, $T_1$, $T_2$ and $T$ are the conversion efficiency, cold side, hot side and operating temperatures respectively. The intrinsic $ZT$ is defined as; $ZT=\frac{S^{2}\sigma}{\kappa_{e}+\kappa_{lat}}$, where, $S$, $\sigma$ and $\kappa_e$($\kappa_{lat}$) are the Seebeck coefficient, electrical conductivity and thermal conductivity due to electrons(phonons) respectively. High value of $ZT$ defines the better conversion efficiency. The optimization of $ZT$ is a tedious task, since the electrical conductivity is proportional to electronic thermal conductivity as; $\kappa_e=L\sigma T$, know as Wiedmann-Franz law, where $L$ is the Lorentz number.

Heusler alloys specially half-Heusler with 18 number of valance electrons gain special interest for the thermoelectric research due to mechanical stability, thermal and electrical properties[1, 2, 3, 4, 5, 6]. Half-Heusler alloys with 18-valence electrons count follow the Slater-Pauling rule ($m_{tot}=(Z-18)\mu_B$[7, 8], where, $m_{tot}$, $Z$ and $\mu_B$ are total magnetic moment, total number of valance electrons and Bohr magneton respectively) and consequently show the semiconducting characteristics exhibiting good Seebeck coefficient and decent band gap. Recent literatures show how the scientific communities are attracted towards the investigation of transport/thermoelectric properties of various half-Heusler alloys using both theoretical tools[9, 10, 11, 12, 13] and experimental technique[14]. For example, the phase stability, electronic structure and magnetic properties of 378 half-Heusler compounds are investigated among which 27 compounds are found to be semiconducting having 18 valence electrons[15]. High value of $ZT\approx1.0$ has been reported for both $n$-type ZNiSn and $p$-type ZCoSb ($Z=$ Zr,Hf,Ti) half-Heusler alloys around 1000K[16, 17, 18, 19]. Due to some of the very peculiar properties of Heusler alloys it also drew a tremendous attraction in wide range of other practical applications e.g. spin valve, spin torque based random access memories, spin injectors, light emitting diodes, spintronics, magnetic tunnel junctions, optoelectronics etc.[20, 21, 22]. Also, half-Heusler alloys can be used in non-contaminant solid-state cooling technologies [23]. Recently, the bandgap of 27 half-Heusler alloys have been predicted accurately using more sophisticated Hybrid density functional theory [24]. The transport characteristics of RuVSb have been investigated recently[25, 26]. Also, the thermoelectric properties of RuVAs, RuVP and RuVSb have been studied by the

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

group of Chibani et al.[27]. However, in order to calculate the most reliable value of $ZT$, the determination of lattice thermal conductivity is highly required. Calculation of lattice thermal conductivity is a bit tedious and computationally expensive task. These issues are the primary focus of our present study.

The objective of our current study is to investigate electronic, mechanical, vibrational and thermoelectric properties of a set of RuVZ(Z=As,P,Sb) half-Heusler alloys using combined framework of first-principles and Boltzmann transport theory. The paper is organized as follows; simulation details are presented in Section 2 (Simulation details), phase stability, electronic structure analysis, mechanical stability, phonon dispersion, transport properties (including Seebeck coefficient, electrical and thermal conductivities) are contained in section 3 (Computational results). Finally the outcome of our findings are summarized in section 4 (Summary and conclusion).

## 2. Simulation details

The density of states(DOS) due to electrons and band structures of present compounds are calculated using projected augmented wave(PAW) technique as implemented in Density Functional theory (DFT) based Vienna ab-initio simulation Package(VASP)[28, 29, 30, 31, 32]. The exchange and correlation energy is approximated by generalized gradient approximation(GGA) under Perdew-Burke-Ernzerh(PBE) scheme[33]. The atomic structures(e.g. atomic positions, cell volume and shape) for all the compounds are fully relaxed by conjugate gradient algorithm up to the converging criterion of force/energy to $10^6$ eV per cell. The energy cut-off of 500eV for plane wave along with accurate precession have been adopted for the simulation. A $\Gamma$-centered $k$-mesh of $16 \times 16 \times 16$ is used for the Brillouin zone integration. In particular, for reliable estimation of electronic bandgap a more accurate Heyd-Scuseria-Ernzerhof (HSE06) functional is adopted[34]. For HSE simulation, the screening($\omega$) parameter of $0.2$ $\text{\AA}^{-1}$ and mixing($\alpha$) 25% are used.

The dispersion relation due to phonons is plotted using PHONOPY package[35] after obtaining harmonic $2^{nd}$ order interatomic force constants(IFCs). The IFCs are obtained using linear response method based upon Density Functional perturbation theory(DFPT) as implemented in VASP package. We have used $2^3$ supercell obtained from the primitive cell having 3 atoms. For Brillouin zone integration, we used $8 \times 8 \times 8$ $k$-mesh and 500 eV cutoff criteria for plane wave basis set.

Mechanical stability of the present alloys are discussed by performing lattice dynamic simulation. The calculated elastic constants($C_{ij}$) satisfy the stability criteria due to Born and Huang [36] given as (for the cubic crystal),

$$
\frac{C_{11}-C_{12}}{2}>0, \quad \frac{C_{11}+2 C_{12}}{3}>0, \quad C_{44}>0. \tag{1}
$$

Transport coefficients are calculated using Boltzmann transport theory(BTT) of charge carriers as implemented in BoltzTraP package[37]. In BoltzTraP code, band structure data (as obtained from the DFT simulation) are considered as input for

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu
transport study. Comparatively denser $k$-mesh is required to calculate the transport
properties accurately. Hence, a high dense $k$-mesh of $46 \times 46 \times 46$ is used to get DFT
band structure data. The transport coefficient tensors (e.g. Seebeck $(S_{\alpha \beta})$, electrical
conductivity $(\sigma_{\alpha \beta})$ and thermal conductivity due to charge carriers $(\kappa_{\alpha \beta}))$ are calculated
according to the semi-classical Boltzmann transport equation as,

$$
S_{\alpha \beta}(T, \mu)=\frac{1}{e \Omega T \sigma_{\alpha \beta}(T, \mu)} \int \overline{\sigma}_{\alpha \beta}(\epsilon)(\epsilon-\mu)\left\{-\frac{\partial f_{\mu}(T, \epsilon)}{\partial \epsilon}\right\} d \epsilon,
$$

$$
\sigma_{\alpha \beta}(T, \mu)=\frac{1}{\Omega} \int \overline{\sigma}_{\alpha \beta}(\epsilon)\left\{-\frac{\partial f_{\mu}(T, \epsilon)}{\partial \epsilon}\right\} d \epsilon,
$$

$$
\kappa_{\alpha \beta}^{e}(T, \mu)=\frac{1}{e^{2} \Omega T \sigma_{\alpha \beta}(T, \mu)} \int \overline{\sigma}_{\alpha \beta}(\epsilon)(\epsilon-\mu)^{2}\left\{-\frac{\partial f_{\mu}(T, \epsilon)}{\partial \epsilon}\right\} d \epsilon,
$$

where, the electrical conductivity tensor is defined as,

$$
\overline{\sigma}_{\alpha \beta}(\epsilon)=\frac{e^{2}}{N} \Sigma_{i, k} v_{\alpha}(i, k) \cdot v_{\beta}(i, k) \cdot \tau \cdot \frac{\delta\left(\epsilon-\epsilon_{i, k}\right)}{d \epsilon}
$$

$$
v(i, k)=\frac{1}{\hbar} \frac{\delta \epsilon(i, k)}{\partial k_{\alpha}},
$$

where, $f, \Omega, e, T, \mu, v_{\alpha(\beta)}$, and $\tau$ are the Fermi-Dirac distribution function, volume
of the unit cell, electronic charge, absolute temperature, chemical potential (or, Fermi
level), group velocity of charge carriers and relaxation time respectively. The relaxation
time can be estimated either from the experiment or using the Deformation potential
introduced by Bardeen and Shockley[38].

Thermal conductivity (due to phonons) has been computed by solving the
Boltzmann transport equation for phonons as implemented in shengBTE software[39].
The software is based upon the iterative solution of Boltzmann transport equation.
The $3^{rd}$ inter-atomic force constants(IFCs) are calculated by thirdorder.py module
of shengBTE code. Third order IFCs are calculated using $4 \times 4 \times 4$ supercell and
considering inter-atomic interactions upto the fourth nearest neighbor having Brillouin
zone sampling with $\Gamma$-point only. The Born effective charges on each atoms and
macroscopic dielectric tensor are calculated using primitive cell by DFPT method as
implemented in VASP.

## 3. Computational results

### 3.1. Phase stability, density of states and band structure analysis

Phase stability of all the compounds (RuVZ; $Z=$ As, P, Sb) has been analyzed in
various atomic, magnetic and non-magnetic configurations. Among the different atomic
and magnetic phases, a configuration with atomic occupancy i.e. Ru occupies at $4c$, $V$ at
$4b$ and $X$ at $4a$ Wyckoff position respectively with non-magnetic fcc cubic (space group
$F m \overline{3} m$, no. 216) phase emerged out to be most stable. In general, the half-Heusler

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

<table>
<thead>
<tr>
<th>Alloys</th>
<th>$a_{rlp}$(PBE) (Å)</th>
<th>$a_{rlp}$(HSE06) (eV)</th>
<th>$\Delta E_{g}$(PBE) (eV)</th>
<th>$\Delta E_{g}$(HSE06) (eV)</th>
<th>Atomic position</th>
</tr>
</thead>
<tbody>
<tr>
<td>RuVP</td>
<td>5.63<br>5.65 [24]</td>
<td>5.59</td>
<td>0.10</td>
<td>1.62<br>1.19[24]</td>
<td>Ru @ (1/4,1/4,1/4)<br>V @ (1/2,1/2,1/2)<br>and P @ (0,0,0)</td>
</tr>
<tr>
<td>RuVAs</td>
<td>5.78<br>5.80 [24]</td>
<td>5.73</td>
<td>0.14</td>
<td>1.54<br>1.25[24]</td>
<td>Ru @ (1/4,1/4,1/4)<br>V @ (1/2,1/2,1/2)<br>and As @ (0,0,0)</td>
</tr>
<tr>
<td>RuVSb</td>
<td>6.04<br>6.05 [24]</td>
<td>5.98</td>
<td>0.17</td>
<td>1.44<br>1.25[24]</td>
<td>Ru @ (1/4,1/4,1/4)<br>V @ (1/2,1/2,1/2)<br>and Sb @ (0,0,0)</td>
</tr>
</tbody>
</table>

Table 1. The bandgap ($\Delta E_g$) using PBE and HSE06 functionals and the atomic position obtained at optimized lattice parameter ($a_{rlp}$).

alloys follow the Slater-Pauling rule[7, 8]. According to the rule, magnetic moment can be predicted using the formula, $m_t=(z_v - 18)\mu_B$, where, $m_t$, $z_v$ and $\mu_B$ are the total magnetic moment, number of valence electrons and Bohr magnaton respectively. In the present case, the total number of valence electrons are 18 in each alloy, indicating zero magnetic moment and eventually leads to a non-magnetic characteristics.

![](./images/817340037128519680_1.jpg)

Figure 1. Crystal structure of RuVZ ($Z=$ As, P and Sb) in the most stable form. The atom, Ru(off-white sphere) occupies at (1/4,1/4,1/4), V(red sphere) occupies at (1/2,1/2,1/2) and X(green sphere) occupies at (0,0,0) Wyckoff site. The crystallographic axis are represented by $a$, $b$ and $c$ respectively.

The electronic structures have been analyzed using both PBE and HSE06 functional as depicted in Fig.2. It has been observed that the bandgap is underestimated in case of PBE functional due to occurrence of non physical Coulomb repulsion[40, 41]. However, the self-Coulomb interaction(repulsion) reduces after incorporating the accurate Hartree-Fock exchange[42]. Therefore more accurate/sophisticated HSE06

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

Electronic DOS using PBE functional

![](./images/817340037128519680_2.jpg)

Electronic DOS using HSE06 functional

![](./images/817340037128519680_3.jpg)

Figure 2. The electronic structure of RuVAs, RuVP and RuVSb compounds using both PBE (UP) and HSE06 (DOWN) functional . All compounds reveal a finite bandgap around the Fermi level ($E_F$) concluding to semiconducting characteristics.

Electronic band structure using PBE functional

![](./images/817340037128519680_4.jpg)

Electronic band structure using HSE06 functional

![](./images/817340037128519680_5.jpg)

Figure 3. Band structure plots for RuVAs(left), RuVP(middle) and RuVSb(right) compounds using both PBE(UP) and HSE06(DOWN) functionals. All the compounds reveal a finite bandgap around the Fermi level represented by the dashed line.

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

functional has been used to evaluate the electronic bandgap. The electronic structure using HSE06 functional has been obtained using HSE06-optimized lattice parameter. The HSE06-optimized lattice parameters are 5.73 $\mathring{A}$, 5.59 $\mathring{A}$ and 5.98 $\mathring{A}$ for RuVAs, RuVP and RuVSb respectively. For comparison, the electronic DOS is presented in Fig.2 and the bandgap values are shown in Table1. In all the cases, the band structure plots (i.e. Fig.3) reveals that the maxima of valance band lies at $L$, whereas, minima of conduction band lies at $X$ point concluding an indirect bandgap semiconductor.

### 3.2. Mechanical stability analysis and phonon dispersion

In this section, mechanical stabilities of all the cubic alloys have been analyzed by calculating of elastic constants (e.g. $C_{11}$, $C_{12}$ and $C_{44}$). The elastic constants are calculated using optimized lattice parameter as listed in Table2. These elastic constants are calculated by applying different kinds of strain, e.g. rhombohedral distortion and change in volume. It has been clearly demonstrated that the elastic constants (as listed in Table2) satisfy the Born-Huang criteria of mechanical stability (as shown in Eq.1). From table2, it is clear that Young's modulus($Y$) is higher than bulk modulus($B$) for all the compounds, indicating material's resistance from broken. The elastic moduli such as $Y$, $B$ and shear modulus($G$) are estimated using the following formula,

$$
B=\frac{1}{3}(c_{11}+2 c_{12}),\quad G=\frac{1}{2}(G_{1}+G_{2}),\quad G_{1}=\frac{1}{2}(c_{11}-c_{12}),\quad G_{2}=c_{44},
$$

$$
Y=\frac{9 B G}{3 B+G}
$$

The calculated values are shown in Table2. Among all the Heusler alloys, RuVP shows the hardest resistance among others (due to larger value of $B$). The bulk modulus is also a measure of compressibility of the material[43]. The larger the value, the less compressible the compound. Among the presented alloys, the least compressible compound is RuVP. The stiffness of a material is determined by Young's modulus and change in the angle of bond under external stress is determined by the Shear modulus. In addition, the Poisson ratio ($\nu$), anisotropy factor ($A$), the Pugh's ratio (i.e. $B/G$) and the Shear constant $(C_{s})$ are also evaluated using the following formulae,

$$
\nu=\frac{3 B-Y}{6 B},\quad A=\frac{2 C_{44}}{C_{11}-C_{12}},\quad C_{s}=\frac{1}{2}(C_{11}-C_{12})
$$

The characteristics of the material (e.g. Brittle and ductile) is determined by the ratio $B/G$. If B/G > 1.75 then the material is defined as ductile nature, whereas, <1.75 indicates the brittle nature. The table2 clearly indicates that all the alloys are ductile in nature which is also supported by the Poisson's ratio. All the alloys are found to be anisotropic in nature ($A\neq1$). The shear constant$(C_{s}=C_{11}-C_{12})$ indicates the dynamical stability if the criteria $C_{s}>0$ satisfies. The isotropic longitudinal velocity($v_{l}$), directional dependent longitudinal velocities ($v_{l}[100]$, $v_{l}[110]$, $v_{l}[111]$), transverse velocity ($v_{t}$), directional dependent transverse velocities ($v_{t}[100]$,

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu
$v_t[110], v_t[111])$, average velocity $(v_s)$ and the Debye temperature are calculated using
following formulae,

$$
v_l = \sqrt{\frac{(3B + 4G)}{3\rho}},
$$

$$
v_l[100] = \sqrt{\frac{C_{11}}{\rho}}, v_l[110] = \sqrt{\frac{C_{11} + C_{12} + 2C_{44}}{2\rho}}, v_l[111] = \sqrt{\frac{C_{11} + 2C_{12} + 4C_{44}}{3\rho}},
$$

$$
v_t = \sqrt{\frac{G}{\rho}},
$$

$$
v_t[100] = \sqrt{\frac{C_{44}}{\rho}}, v_t[110] = \sqrt{\frac{C_{11} - C_{12}}{\rho}}, v_t[111] = \sqrt{\frac{C_{11} - C_{12} + C_{44}}{3\rho}},
$$

$$
v_s = \left\{ \frac{1}{3} \left( \frac{2}{v_t^3} + \frac{1}{v_l^3} \right) \right\}^{-1/3},\ \Theta_D = \frac{\hbar}{k_B} \left( 6\pi^2 \frac{n}{V} \right)^{1/3} v_s
$$

where, $\hbar$, $\rho$, $n$, $V$, and $\Theta_D$ represent reduced Plank constant, mass density of material,
number of atom per unit formula, volume of unit cell and the Debye temperature
respectively.

<table>
<thead>
<tr>
<th>Alloys</th>
<th>$C_{11}$
($GPa$)</th>
<th>$C_{12}$
($GPa$)</th>
<th>$C_{44}$
($GPa$)</th>
<th>$B$
($GPa$)</th>
<th>$G$
($GPa$)</th>
<th>$Y$
($GPa$)</th>
<th>$B/G$</th>
<th>$\nu$</th>
<th>$A$</th>
<th>$\kappa_{min}$
($W/m-K$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>RuVP</td>
<td>262.06</td>
<td>172.63</td>
<td>80.67</td>
<td>202.44</td>
<td>62.69</td>
<td>170.48</td>
<td>3.22</td>
<td>0.359</td>
<td>1.80</td>
<td>1.15</td>
</tr>
<tr>
<td>RuVAs</td>
<td>243.13</td>
<td>153.40</td>
<td>61.33</td>
<td>183.31</td>
<td>53.10</td>
<td>145.27</td>
<td>3.45</td>
<td>0.368</td>
<td>1.37</td>
<td>0.95</td>
</tr>
<tr>
<td>RuVSb</td>
<td>234.29</td>
<td>127.63</td>
<td>40.59</td>
<td>163.18</td>
<td>46.96</td>
<td>128.55</td>
<td>3.47</td>
<td>0.369</td>
<td>0.76</td>
<td>0.80</td>
</tr>
</tbody>
</table>

Table 2. Various elastic constants, $c_{ij}$, Bulk modulus($B$), Shear modulus($G$), Young's
modulus($Y$), Pugh's ratio($B/G$), Poisson ratio($\nu$), anisotropy factor($A$) and theoretical
limit of minimum lattice thermal conductivity($\kappa_{min}$) for the present compounds.

<table>
<thead>
<tr>
<th>Alloys</th>
<th>$v_l$
($GPa$)</th>
<th>$v_t$
($GPa$)</th>
<th>$v_s$
($GPa$)</th>
<th>$v_l[100]$
($GPa$)</th>
<th>$v_l[110]$
($GPa$)</th>
<th>$v_l[111]$
($GPa$)</th>
<th>$v_t[100]$
($m/s$)</th>
<th>$v_t[110]$
($m/s$)</th>
<th>$v_t[111]$
($m/s$)</th>
<th>$\Theta_D$
($K$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>RuVP</td>
<td>6481.71</td>
<td>3024.53</td>
<td>3416.22</td>
<td>6204.18</td>
<td>6617.11</td>
<td>6749.14</td>
<td>3444.15</td>
<td>3624.31</td>
<td>2886.62</td>
<td>411.94</td>
</tr>
<tr>
<td>RuVAs</td>
<td>5704.65</td>
<td>2607.70</td>
<td>2939.00</td>
<td>5580.08</td>
<td>5765.73</td>
<td>5826.56</td>
<td>2802.58</td>
<td>3389.92</td>
<td>2539.42</td>
<td>345.28</td>
</tr>
<tr>
<td>RuVSb</td>
<td>5224.3</td>
<td>2382.50</td>
<td>2685.49</td>
<td>5321.64</td>
<td>5174.93</td>
<td>5125.10</td>
<td>2215.02</td>
<td>3590.62</td>
<td>2435.77</td>
<td>302.14</td>
</tr>
</tbody>
</table>

Table 3. The longitudinal($v_l$), transverse($v_t$), and average/mean($v_s$) sound velocities
and Debye temperature($\Theta_D$) derived from the elastic constants. The sound velocities
and Debye temperature are measured in $m/s$ and $K$ respectively.

The crystal vibrations in the material for low and high temperature regimes are
determined by the Debye temperature ($\Theta_D$). From the above expressions, it is clear
that the velocities are inversely proportional to the mass density. The calculated
mass densities are $7808.33\ Kg/m^3$, $6808.2\ Kg/m^3$, $8272.98\ Kg/m^3$ for RuVAs, RuVP

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

![](./images/817340037128519680_6.jpg)

Figure 4. Phonon dispersion and density of states for RuVAs(lest), RuVP(right) and RuVSb(bottom).

and RuVSb respectively. Hence, velocities are highest and lowest in RuVP and RuVSb compounds respectively. The directional dependent longitudinal and transverse velocities are significantly different in different directions such as [100], [110] and [111].

The phonon dispersion graphs for RuVZ ($Z =$ As, P, Sb) are presented in Fig.4. The phonon plots are considered along the high symmetric $k$-directions such as $X \to K \to \Gamma \to L \to W$. It has been observed from the graph that no negative or imaginary frequency occurs in the considered range of Brillouin zone, which confirms the mechanical stability of all the alloys. There are three atoms in the primitive cell, which generate nine phonon modes, out of which three are acoustic and remaining six are optical modes. The acoustic modes of vibrations are two-fold degenerate along $\Gamma \to L$ or $\Gamma \to K$ directions except for RuVSb. The degeneracy has been lifted out in the different wave vector directions. In optical modes, there exists a significant bandgap (except RuVP and RuVAs) because of the mass difference among the constituent elements. The phonon bandgap exists (in between the acoustic and optical modes) only in RuVSb system.

### 3.3. Transport properties

The characteristic feature of electronic bands near $E_F$ and the electronic bandgap play a decisive role in predicting the thermoelectric/transport properties of a material. In general, sudden/high rise in electronic density of states (or flat topology of band

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

dispersion) leads to high value of Seebeck coefficient($S$) and high band effective mass, which eventually becomes one of the key factor in enhancing figure of merit. However, according to the relation, $\mu = \tau e/m^*$, high effective band mass($m^*$) is inversely proportional to the electrical mobility($\mu$) of charge carrier. Low mobility decreases electrical conductivity significantly.

From the valance band in the electronic band dispersion plot, it is observed that energies corresponding to valley points arising at $W$, $L$ and $\Gamma$ are nearly close, indicating hole transport enhancement. The conduction band along $W \rightarrow L \rightarrow \Gamma$ high symmetric line is nearly flat indicating electronic transport enhancement. It has been observed that the topology of band structure is same as in both the PBE and HSE06 functional except the bandgap values (in both the cases). Also, bandgap obtained from the HSE06 functional is more accurate than the PBE functional. Hence, more reliable thermoelectric response of the alloys are estimated by shifting the bandgap obtained in PBE functional by matching with hybrid functional(HSE06). This type of rigid shift in the bandgap is often used to evaluate thermoelectric properties of the material. One can predict the upper limit of $ZT$ (excluding thermal conductivity due to phonons) using the formula; $ZT = \frac{ZT_e}{(1+\kappa_{lat}/(\kappa_{el}/\tau))}$, where, $ZT_e = \frac{S^2(\sigma/\tau)}{(\kappa_e/\tau)}$, is known as the upper limit of $ZT$.

![](./images/817340037128519680_7.jpg)

Figure 5. Thermoelectric coefficient versus chemical potential. The Seebeck coefficient $(S)$, scaled electrical $(\sigma/\tau)$ and thermal $(\kappa_e/\tau)$ conductivities are measured in $\mu - V/K$, $10^{20}\ (\Omega m s)^{-1}$ and $10^{16}\ (W/m K s)$.

The transport coefficients(e.g. $S$, $\kappa_e/\tau$, $\sigma/\tau$ and $ZT_e$) versus chemical potential ($\mu$) of the alloys are studied and depicted in Fig.5 at different fixed temperature, 300K, 500K, 700K and 900K. The label of $x$-axis, $\mu - E_F = 0$ implies that the Fermi level lies exactly

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

at middle of the bandgap and eventually leads to pristine/undoped semiconductors.
However, in $n(p)$-type doping $E_F$ lies near to conduction(valance) band. The transport coefficients (e.g. $S$, $\sigma/\tau$, and $\kappa_e/\tau$) are directional dependent tensors of rank 2 with 9 directional components. Our simulation shows that contribution from the diagonal terms are more significant than off-diagonal terms. Therefore, we have considered the average value of diagonal components. From Seebeck coefficient plot depicted in Fig.5 (lower panel), the maximum value of $S$ occurs near the Fermi level. The negative and positive values of $S$ signify $n$- and $p$-type characteristics respectively. The peak value of $S$ for $n$- and $p$-type occurs at 300K for all the compound. The maximum value of $ZT_e$ corresponds to a particular value of $\mu$ which eventually leads to a certain carrier concentration. Also, it is evident from the $ZT_e$ plot, that maximum value leads to a range of chemical potential which gives a window of optimal carrier concentration $\mathbb{N}$. For RuVAs, the optimal $\mathbb{N}$ is $-6.28 \times 10^{17} \frac{1}{cm^3}$ and $1.09 \times 10^{18} \frac{1}{cm^3}$ for $n$- and $p$-type characteristics respectively. Whereas, for RuVP, the optimal $\mathbb{N}$ is $-3.39 \times 10^{17} \frac{1}{cm^3}$ and $6.43 \times 10^{17} \frac{1}{cm^3}$ for $n$- and $p$-type behavior respectively. For RuVSb, the optimal $\mathbb{N}$ is $-1.33 \times 10^{18} \frac{1}{cm^3}$ and $2.49 \times 10^{18} \frac{1}{cm^3}$ for $n$- and $p$-type channel. Due to generation of more electron-hole pairs at higher temperature, lattice thermal conductivity gets reduced, however due to increase in mean free path and scattering of phonons lattice thermal conductivity reduced drastically. Thus, in higher temperature limit, figure of merit can be estimated as,

$$
ZT = \frac{ZT_e}{\left(1+\kappa_{lat}/(\kappa_{el}/\tau)\right)}, where, ZT_e = \frac{S^2(\sigma/\tau)}{(\kappa_e/\tau)},
$$

At higher temperature limit, $\kappa_{lat}/\kappa_e <<1$,

$$
ZT \approx ZT_e = \frac{S^2}{L}, \quad L = \frac{\kappa_e}{\sigma T},
$$

where, $L$ is the Lorentz number. From the above expression it is clear that at higher temperature, figure of merit is significantly dominated by the Seebeck coefficient. The value of Seebeck coefficient depends upon the electronic density of states. From Fig.2, it is evident that the electronic DOS near $E_F$ is comparatively higher for $p$-type than $n$-type channel. Hence, we expect higher $S$ from $p$-type channel to the $n$-type channel and indeed it has been supported by the plot (lower panels of Fig.6,7,8). In addition, it is expected that $p$-type behavior is more promising than $n$-type behavior for all the compound. The value of $ZT_e$ reaches to unity for all the alloys (upper panel of Fig.6,7,8), however this exclude the thermal conductivity due to phonons. In order to get the more reliable $ZT$ value, thermal conductivity due to phonons has to be incorporated.

The plot of various transport parameters (e.g. $S$, $\sigma/\tau$ and $\kappa_e/\tau$) versus temperature($T$) are shown in Fig.6,7,8. The magnitude of $S$ (i.e. $|S|$) increases for both $n$-type and $p$-type due to the transport of majority charge carriers. From the nature of Seebeck plots, it is clear that only majority charge carriers play significant role in transport for all the alloys. For example, electrons(holes) are the main carriers for the transportation in $n(p)$-type characteristics. The electrical conductivity($\sigma/\tau$) and

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

lattice thermal conductivity due to electrons $(\kappa_{e}/\tau)$ are decreasing and increasing due to thermally excited carriers respectively(middle plots of Fig.6,7,8).

![](./images/817340037128519680_8.jpg)

Figure 6. Thermoelectric coefficient versus temperature. The Seebeck coefficient $(S)$(bottom panel), electrical conductivity $(\sigma/\tau)$(lower) and electronic thermal conductivity$(\kappa_{e}/\tau)$(lower) are measured in $\mu-V/K$, $10^{15}\ (\Omega ms)^{-1}$ and $10^{15}\ (W/mKs)$ respectively.

![](./images/817340037128519680_9.jpg)

Figure 7. Same as Fig.6

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

![](./images/817340037128519680_10.jpg)

Figure 8. Same as Fig.6

3.3.1. Phonon thermal conductivity and figure of merit: Lattice thermal conductivity($\kappa$) plays a decisive role in predicting thermoelectric figure of merit. Hence, we have calculated $\kappa_{lat}$ using shengBTE package as presented in Fig. 9. In all the cases, $\kappa_{lat}$ decreases as the temperature increases. This happens due to the reduction in mean free path of thermally excited phonons and consequently increase scattering rate of phonons. In the plotted range of temperature, the maximum(minimum) values are 18.18(6.07), 31.7(10.76) and 8.57(2.86) $W/(m-K)$ obtained at 300K(900K) for RuVAs, RuVP and RuVSb respectively. Among the present alloys, minimum lattice thermal conductivity is obtained for RuVSb alloy. We have also calculated the theoretical limit or minimum lattice thermal conductivity using formula, $k_{min} = \frac{1}{2} \left(\frac{\pi}{6}\right)^{1/3} k_B (V/n)^{-2/3} (2v_t + v_l)$[44] and the values are listed in the last column of Table2. The theoretical cut-off limit or minimum value of $\kappa$ (i.e. $\kappa_{min}$) is obtained for RuVSb.

Following Fig. 6,7,8, the upper limit of figure of merit i.e. $ZT_e$ approaches to 1, which is independent of $\kappa_{lat}$ and $\tau$. Hence, one can expect that alloys might be promising for thermoelectric applications at moderate temperature. We have calculated the reliable value of $ZT$, which includes the effect of $\kappa_{lat}$ also. Not only the thermal conductivity(due to phonons) but also the relaxation time($\tau$) of charge carriers is very important parameter to determine the $ZT$ value accurately. Unfortunately, the estimation of relaxation time from first-principles simulation is tough task to evaluate due to various scattering mechanism[45]. Hence, in practice, $\tau$ is either obtained from the experiment or by comparing theoretical $\sigma/\tau$ to experimental electronic conductivity. However, in present case both scenario is not possible due to unavailability of experimental $\sigma$ or experimental $\tau$. Hence, we have considered the two values of $\tau$,

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

i.e. $\tau_1 = 245$ and $\tau_2 = 121$ femto second from other cases of Heusler alloys[46, 47] to vaticinate $ZT$. In case of RuVAs, the $p(n)$-type thermoelectric response gives $ZT$ value of $0.32(0.19)$ and $0.41(0.26)$ at $\tau_1$ and $\tau_2$ respectively. For, RuVP, $ZT$ values for $p(n)$-type are $0.21(0.12)$ and $0.16(0.08)$ at $\tau_1$ and $\tau_2$ respectively. However, for RuVSb alloy, the highest $ZT$ of $0.70(0.55)$ and $0.61(0.44)$ are obtained for $p(n)$-type characteristics at $\tau_1$ and $\tau_2$ respectively. All the values of $ZT$ (mentioned above) are obtained at 900K. Lowest value of $ZT$ is obtained for RuVAs and RuVP because of the high lattice thermal conductivity (Fig.9). As expected from the DOS plot that the $p$-type thermoelectric response is more dominating than $n$-type which has also been supported from the above values. Our analysis reveals that RuVSb is the most promising thermoelectric Heusler alloy for practical application.

![](./images/817340037128519680_11.jpg)

Figure 9. Plot of lattice thermal conductivity($\kappa_{lat}$) versus temperature($T$) for RuVAs(top), RuVP(middle) and RuVSb(bottom). Comparatively minimum $\kappa_{lat}$ is obtained for RuVSb.

### 4. Summary and conclusions

In framework of DFT and BTT for electrons and phonons, we have examined the mechanical stability, electronic structure, vibrational and thermoelectric characteristics of RuVAs, RuVP and RuVSb half-Heusler alloys. Phase stability analysis reveals that all the alloys are crystallize in face centered cubic structure with #216 space group. Electronic structure simulation shows that the alloys are indirect band gap semiconductors. The indirect band gap occurs at $L$ and $X$ high symmetry points. The mechanical stability is confirmed by the elastic constant calculations (Born-Huang

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

criteria) which is also supported by the phonon dispersion plots. The vibrational properties of all the alloys are investigated in detailed. The longitudinal and transverse velocity (along with its directional dependent components), the elastic moduli, and the Debye temperature are calculated. In addition, all the compounds are ductile in nature as indicated by the Pughs and Poisson's ratios. One of the important characteristics, the bandgap, which affect the thermoelectric properties very significantly, has been rectified by the more accurate HSE06 functional. For all the alloys, upper limit of figure of merit (i.e. $ZT_{e}$) is approximately equal to 1 for both $n$- and $p$-type channels. The optimal carrier concentration for alloys corresponding to $n$- and $p$-type behavior is also calculated (see Computational result section). Lattice thermal conductivities for the compounds are obtained using shengBTE software. The calculated value of minimum $\kappa_{lat}$ is $2.86\ W/mK$ is obtained for RuVSb at 900K. We have also predicted the theoretical limit of $\kappa_{lat}$ for all the compound (as depicted in the last column of table2). Lattice thermal conductivity can be reduced further by the different mechanism (e.g. extrinsic/intrinsic defects and external doping) which certainly enhance $ZT$ value. Among all alloys, the highest value of $ZT$ is obtained for RuVSb. These values are 0.70(0.55) and 0.61(0.44) for $p(n)$-type channel at 245 and 121 femto second respectively. For all the other compounds, the predicted $ZT$ are contained in Computational results section. Comparatively flat topology of the band structure (specially valance band) and corresponding $ZT$ value of RuVSb suggest that the alloy is very promising for thermoelectric application. Hence, it is highly recommended to the our experimental colleagues to carry out the experimental verification of our theoretical findings.

Acknowledgement

The authors extend their appreciation to the deanship of Scientific Research at Majmaah University for funding this work under project number RGP-2019-25. Enamullah would like to acknowledges the Honorable Chancellor, Mr. M. Hoque, University of Science and Technology, Meghalaya for his encouragement. Enamullah is grateful to his colleague Ramizuddin Ahmed for the fruitful discussion.

References

[1] Yu C, Zhu T J, Shi R Z, Zhang Y, Zhao X B and He J 2009 *Acta Mater.* **57** 2757

[2] Birkel C S, Zeier W G, Douglas J E, Lettiere B R, Mills C E, Seward G, Birkel A, Snedaker M L, Zhang Y C, Snyder G J, Pollock T M, Seshadri R and Stucky G D, 2012 *Chem. Mater.* **24** 2558

[3] Xie H H, Wang H, Pei Y Z, Fu C G, Liu X H, Snyder G J, Zhao X B and Zhu T J 2013 *Adv. Funct. Mater.* **23** 5123

[4] Chen S, and Ren Z F 2013 *Mater. Today* **16** 387

[5] Zhu T J, Fu C G, Xie H H, Liu Y T and Zhao X B 2015 *Adv. Energy Mater.* **5** 1500588

[6] Rogl G, Grytsiv A, Grth M, Tavassoli A, Ebner C, Wnschek A, Puchegger S, Soprunyuk V, Schranz W, Bauer E, Mller H, Zehetbauer M, and Rogl P 2016 *Acta Mater.* **107** 178

[7] Slater J C 1936 *Phys. Rev.* **49**, 931

[8] Pauling L 1938 *Phys. Rev.* **54** 899

Transport properties of RuV-based half-Heusler semiconductors for thermoelectric applications: A compu

[9] Joshi H, Rai D, Verma K, Bhamu K and Thapa R 2017 J. Alloy. Comp. 726 1155

[10] Benallou Y, Amara K, Doumi B, Arbouche O, Zemouli M, Bekki B 2017 J. Comput. Electron. 16

[11] Kaur K and Kaur J 2017 J. Alloy. Comp. 715 297

[12] Kaur K, Rai D, Thapa R and Srivastava S 2017 J. Appl. Phys. 122 045110

[13] Vikram, Kangsabanik J, Enamullah and Alam A 2017 J. Mater. Chem. A. 5 6131

[14] Chen L, Liu Y, He J, Tritt T M, Poon S J 2017 AIP Adv. 7 065208

[15] Ma J, Hegde V I, Munira K, Xie Y, Keshavarz S, Mildebrath D T, Wolverton C, Ghosh A W,
Butler W 2017 Phys. Rev. B 95 024411

[16] Yan X, Liu W S, Wang H, Chen S, Shiomi J, Esfarjani K, Wang H Z, Wang D Z, Chen G and
Ren Z F 2012 Energy Environ. Sci. 5 , 7543

[17] Chen S, Lukas K C, Liu W S, Opeil C P, Chen G and Ren Z F 2013 Adv. Energy Mater. 3 1210

[18] Yan X, Liu W. S, Chen S, Wang H, Zhang Q, Chen G and Ren Z F 2013 Adv. Energy Mater. 3

[19] Liu Y T, Xie H H, Fu C G, Snyder G J, Zhao X B and Zhu T J 2015 J. Mater. Chem. A 3 22716

[20] Amudhavalli A, Rajeswarapalanichamy R, Iyakutti K et al 2018 Comp. Condens. Matter 14 55

[21] Kandpal H C, Felserand C, Seshadr R 2006 J Phys D: Appl. Phys. 39 776

[22] Larson P, Mahanti S D, Kanatzidis M G 2000 Phy. Rev. B 62 12754

[23] Sagotra A K et al. 2017 Nat. Commun. 8 963.

[24] Shi F, Si M, Xie J, Mi K, Xiao C, Luo Q, 2017 J. Appl. Phys. 122 215701

[25] Fang T, Zheng S, Zhou T, Yan L, Zhang P 2017 Phys. Chem. Chem. Phys. 19 4411

[26] Xing G, Sun J, Li Y, Fan X, Zheng W, Singh D J 2017 Phys. Rev. Materials 1 065405

[27] Chibani S, Arbouche O, Zemouli M, Benallou Y, Amara K, Chami N, Ameri M, El Keurti M 2018
Comp. Cond. Matt. 16 e00312

[28] Hohenberg P and Kohn W 1964 Phys. Rev. 136 B865

[29] Kresse G and Furthmller J 1996 Comput. Mater. Sci. 6 15

[30] Kresse G and Furthmller J, 1996 Phys. Rev. B: Condens. Matter Mater. Phys. 54 011169

[31] Kresse G and Hafner J 1993 Phys. Rev. B: Condens. Matter Mater. Phys. 47 558

[32] Blochl P E 1994 Phys. Rev. B: Condens. Matter Mater. Phys. 50 17953

[33] Perdew J P, Burke K and Ernzerhof M 1996 Phys. Rev. Lett. 77 3865

[34] Krakau A V, Vydrov O A, Izmaylov A F and Scuseria G E 2006 J. Chem. Phys. 125 224106

[35] Togo A and Tanaka I 2015 Scr. Mater. 108 15

[36] Born M and Huang K, Dynamical Theory of Crystal Lattices, Oxford University Press, Oxford,
UK, 1954

[37] Madsen G K H and Singh D J 2006 Comput. Phys. Commun. 175 67

[38] Bardeen J. and Shockley W 1950 Phys. Rev. 80 72

[39] Li W, Carrete J, Katcho N A and Mingo N 2014 Comput. Phys. Commun. 185 1747

[40] Perdew J P and Zunger A 1981 Phys. Rev. B: Condens. Matter Mater. Phys. 23 5048

[41] Perdew J P and Levy M 1983 Phys. Rev. Lett. 51 1884

[42] Perry J K, Tahir-Kheli J and Goddard W. A 2001 Phys. Rev. B: Condens. Matt. 63 144510

[43] D. Errandonea et al. 2012 Phys. Rev. B 85, 144103.

[44] Cahill D G, Watson S K, Ro P 1992 Phys. Rev. B 46 6131

[45] Gorai P, Stevanovic V and Toberer E S 2017 Nat. Rev. Mater. 2 201753

[46] Zou D F, Xie S H, Liu Y Y, Lin J G and Li J Y 2013 J. Appl. Phys. 113 193705

[47] Hong A J, Li L, He R, Gong J J, Yan Z B, Wang K F, Liu J -M and Ren Z F 2016 Sci. Rep. 6
22778