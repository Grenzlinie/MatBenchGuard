TYPE Original Research
PUBLISHED 17 August 2022
DOI 10.3389/fmats.2022.972364

![](./images/865006238969102603_1.jpg)

OPEN ACCESS

EDITED BY
Renhui Zhang,
East China Jiaotong University, China

REVIEWED BY
Yong Pan,
Southwest Petroleum University, China
Qiang Li,
Panzhihua University, China

*CORRESPONDENCE
Xiajin Rao,
3172663769@qq.com

SPECIALTY SECTION
This article was submitted to
Computational Materials Science,
a section of the journal
Frontiers in Materials

RECEIVED 18 June 2022
ACCEPTED 14 July 2022
PUBLISHED 17 August 2022

CITATION
Li D, Rao X, Zhang X, Peng B, Pan S,
Huang W and Ma S (2022), Calculation
of thermodynamic properties and
transport parameters of $C_{6}F_{12}O$.
Front. Mater. 9:972364.
doi: 10.3389/fmats.2022.972364

COPYRIGHT
© 2022 Li, Rao, Zhang, Peng, Pan,
Huang and Ma. This is an open-access
article distributed under the terms of the
Creative Commons Attribution License
(CC BY). The use, distribution or
reproduction in other forums is
permitted, provided the original
author(s) and the copyright owner(s) are
credited and that the original
publication in this journal is cited, in
accordance with accepted academic
practice. No use, distribution or
reproduction is permitted which does
not comply with these terms.

# Calculation of thermodynamic properties and transport parameters of $C_{6}F_{12}O$

Dajian Li $^{1,2}$, Xiajin Rao $^{1,2*}$, Xiaoxing Zhang $^{1,2}$, Boya Peng $^{1,2}$, Shaoming Pan $^{1,2}$, Wei Huang $^{1,2}$ and Shouxiao Ma $^{1,2}$

$^{1}$Electric Power Research Institute of Guangxi Power Grid Co. Ltd, Nanning, China, $^{2}$Guangxi Key Laboratory of Intelligent Control and Maintenance of Power Equipment, Nanning, China

$C_{6}F_{12}O$ has good insulating properties and has the potential to be used as an insulating medium in gas-insulated equipment. Previous researches show that thermodynamic properties and transport parameters can reflect the microscopic properties of plasma and evaluate the physical properties of gas during gas discharge. In this paper, the thermodynamic and transport properties of $C_{6}F_{12}O$ are calculated based on LTE conditions. According to the type of particles participating in the reaction and the thermal parameters, the number density of particles, the thermodynamic properties and transport parameters in the range of 300–30000 K are calculated. The results show that the conductivity of $C_{6}F_{12}O$ is higher than that of $CO_{2}$ and $N_{2}$ at lower temperatures, which is consistent with the properties of most electronegative gases. The thermal conductivity of $C_{6}F_{12}O$ has distinct peaks at 3500, 5500 and 16000 K, respectively. The calculation results can provide a data basis for the subsequent calculation of breakdown and interruption characteristics, which is significant to the design and development of gas insulating equipment.

KEYWORDS
C6F12O, partition function, collision ionization, thermodynamic properties, transport parameters

## Introduction

Gas insulation medium has the advantages of safety, reliability, long maintenance period and without aging, therefore, it plays a major role in the field of high voltage insulation (Xiao, 2016). Among various insulating gas media, $SF_{6}$ is widely used in electrical insulation equipment. Its insulation strength in uniform electric field is more than 2.5 times that of air (Tian et al., 2019a). Besides, it can recombine under the high temperature arc has excellent arc extinguishing performance. In terms of performance, $SF_{6}$ is a gas medium with excellent insulation, however, its global warming potential (GWP) of 23,500 can not be ignored (Hou et al., 2019; Zhang et al., 2020a). With the continuous development of the power industry, the content of $SF_{6}$ in the global atmosphere has increased by 20% in the past 5 years, which has a harmful impact on the environment. If it is left alone, it may cause the global average temperature to increase

![](./images/865006238969102603_2.jpg)

by 4°C or more until 2100 (Zhang et al., 2017a; Obama, 2017). Therefore, it is urgent to find an environmentally friendly insulating gas.

$C_6F_{12}O$ is non-toxic and nonflammable, which is in focus due to the original application of extinguishing agent (Linteris et al., 2013). The molecular structure is shown in Figure 1. Further research shows that its insulation performance is more than twice that of $SF_6$ and the GWP value is close to 1, which has little impact on the environment. However, the liquefaction temperature of $C_6F_{12}O$ is high, which needs to be mixed with buffer gas to meet the application requirements (Zhang et al., 2017b; Tian et al., 2018; Tian et al., 2019b; Wang et al., 2020a).

At present, the research on the related properties of $C_6F_{12}O$ has made preliminary progress. In 2014, the experimental studies conducted by ABB show that the mixture of $C_6F_{12}O$ and air or $CO_2$ has similar insulation performance to $SF_6$ under AC voltage and lightning impulse voltage (Mantilla et al., 2014). In recent years, some progress has been made in the domestic research on the insulation and decomposition properties of $C_6F_{12}O$. In 2017, Zhang et al. were the first to study the influence of the mixing ratio on the power frequency breakdown characteristics of $C_6F_{12}O/N_2$ mixture through experiments. The results show that the power frequency breakdown performance of 3% $C_6F_{12}O/N_2$ is 1.7 times that of pure $N_2$ under 0.1 MPa, which is very close to that of to $N_2$ after adding 10% $SF_6$ (Tian et al., 2018). Under this condition of pressure and mixing ratio, the products are mainly $CF_4$, $C_2F_6$, $C3F_8$, $C_4F_{10}$ and $C_5F_{12}$ after breakdown. When the buffer gas is $CO_2$, the breakdown voltage of 3% $C_6F_{12}O/CO_2$ mixture at 0.1-0.2 MPa is slightly higher than that of 10% $SF_6/CO_2$ mixture (Tian et al., 2019c). In further research, the team also studied the partial discharge characteristics of $C_6F_{12}O/$$CO_2$ mixture. Both the initial voltage and extinction voltage are positively correlated with the mixing ratio, and they are greatly influenced by the mixing ratio under the higher the pressure (Zhang et al., 2017b). In addition to the characteristics of the breakdown and decomposition, the team also studied thermal decomposition characteristics of $C_6F_{12}O$ (Yi et al., 2019). The results show that decomposition products are mainly $CF_4$, $C_2F_6$, $C_3F_8$, $C_3F_6$ and $C_5F_{12}$ at high temperatures. For the compatibility of $C_6F_{12}O$ and metal, existing studies have shown that the compatibility of $C_6F_{12}O$-air with aluminum is better than that of copper (Pan, 2021a; Pan, 2021b; Chen and Pan, 2022a; Chen and Pan, 2022b; Pan, 2022).

From a theoretical level, in 2020, Tian et al. calculated the total electron collision ionization cross section of the $C_6F_{12}O$ molecule to evaluate its dielectric strength by using the Deutsch-Märk formula (Tian et al., 2019b). In 2019, Tang et al. analyzed its bond energy and bond angle in detail from the molecular level, then, its thermal stability was preliminarily revealed (Tang et al., 2019). In 2020, Zhong et al. comprehensively analyzed the decomposition mechanism of $C_6F_{12}O$ through advanced quantum chemical calculations of DFT and TST on the basis of experimental research (Wang et al., 2020b). In 2021, Rao et al. calculated the formation process of $C_6F_{12}O$ decomposition products based on DFT, which explained the formation process of decomposition products from a theoretical level (Rao et al., 2021).

The above theoretical and experimental researches on the insulation and decomposition characteristics of $C_6F_{12}O$ have been carried out in a deeply study. Thermodynamic and transport parameters can be used to evaluate the interruption and breakdown characteristics of gas insulating media, now, some relevant calculations have been made in the study of other environmentally friendly insulating media (Zhang et al., 2020b; Zhang et al., 2020c). In this paper, the thermodynamic properties and transport parameters in the range of 300K-30000 K are calculated, which can provide a theoretical basis for the design and development of gas insulation equipment filled with $C_6F_{12}O$ and buffer gases.

## Calculation method

Based on the assumption that $C_6F_{12}O$ is in local thermodynamic equilibrium (LTE), it is assumed that the discharge is in an ideal gas environment. Based on the partition function of each particle, the law of mass action, the law of partial pressure of Dolton, the ionization equation and the dissociation equation, electric neutrality, and atomic conservation are combined to calculate the number density of each particle. Then, various thermodynamic parameters can be obtained directly by using standard thermodynamic relations (Wang et al., 2011). The transmission of particle mass, momentum, and energy in the plasma can be described by the Boltzmann equation, therefore, the transport coefficients can be obtained by the Chapman-Enskog expansion of this equation (Wang et al., 2012).

Specifically, the law of mass action is that the rate of chemical reaction is proportional to the effective mass of the

reactants. The law of partial pressure of Dolton is that the partial pressure in a gas mixture is equal to the pressure when it occupies the entire region alone at the same temperature, and the sum of the pressures of the components in the mixture is the mixture's pressure. The Saha ionization equation and Guldberg-Waage dissociation equation indicates that the atomic concentration and ion concentration are keep balance depending on ionization and recombination, which are calculated through formula (1) and (2).

$$
\begin{aligned}
\frac{n_{e}(T) \cdot n_{(z+1)^{+}}(T)}{n_{z^{+}}(T)}= & \frac{Q_{e}^{\text {int }} \cdot Q_{(z+1)^{+}}^{\text {int }}(T)}{Q_{z^{+}}^{\text {int }}(T)} \cdot\left(\frac{2 \pi m_{e} k_{b} T}{h^{2}}\right)^{\frac{3}{2}} \\
& \exp \left(-\frac{E_{\text {ion }}}{k_{b} T}\right)
\end{aligned}
$$

$$
\begin{aligned}
\frac{n_{A}(T) \cdot n_{B}(T)}{n_{A B}(T)}= & \frac{Q_{A}^{\text {int }} \cdot Q_{B}^{\text {int }}(T)}{Q_{A B}^{\text {int }}(T)} \cdot\left(\frac{m_{A} \cdot m_{B}}{m_{A}+m_{B}}\right)^{\frac{3}{2}} \cdot\left(\frac{2 \pi k_{b} T}{h^{2}}\right)^{\frac{3}{2}} \\
& \exp \left(-\frac{E_{\text {dis }}}{k_{b} T}\right)
\end{aligned}
$$

$Q^{\text {int }}$ is the internal partition function of the particle. $n_{i}$ is the number density of the particle, $m_{e}$ is the mass of the electron, $K_{b}$ is the Boltzmann constant, $h$ is the Planck constant and Eion is the ionization energy of the particle. $m_{A}, m_{B}$, and $m_{A B}$ are the masses of the particles and $E_{\text {dis }}$ is the dissociation energy.

For the partition function of a particle, it is significant in the calculation. It is the sum of the Boltzmann factors of its possible states in the system, which reflects the structural characteristics and thermal parameters of the particle. According to the molecular structure of $C_{6}F_{12}O$ and preliminary research, $C_{6}F_{12}O$ may decompose to a variety of different particles after discharge, which can be divided into monatomic and polyatomic particles to calculate the partition function, respectively. There are 13 kinds of monatomic particles: $\mathrm{C}, \mathrm{C}^{-}, \mathrm{C}^{+}, \mathrm{C}^{2+}, \mathrm{O}, \mathrm{O}^{-}, \mathrm{O}^{+}, \mathrm{O}^{2+}, \mathrm{F}, \mathrm{F}^{-}, \mathrm{F}^{+}, \mathrm{F}^{2+}$, e. Diatomic particles are 12 types: $\mathrm{C}_{2}, \mathrm{C}_{2}^{-}, \mathrm{F}_{2}, \mathrm{~F}_{2}{ }^{+}, \mathrm{O}_{2}, \mathrm{O}_{2}{ }^{-}, \mathrm{O}_{2}{ }^{+}$, $\mathrm{CF}^{+}, \mathrm{CF}, \mathrm{FO}, \mathrm{CO}, \mathrm{CO}^{+}$. Polyatomic particles are 34 types: $\mathrm{C}_{3}$, $\mathrm{CF}_{2}, \mathrm{CF}_{2}{ }^{+}, \mathrm{CO}_{2}, \mathrm{CFO}, \mathrm{F}_{2} \mathrm{O}, \mathrm{C}_{2} \mathrm{O}, \mathrm{FO}_{2}, \mathrm{~F}_{2} \mathrm{O}_{2}, \mathrm{C}_{4}, \mathrm{C}_{5}, \mathrm{C}_{2} \mathrm{~F}, \mathrm{C}_{2} \mathrm{~F}_{2}$, $\mathrm{CF}_{3}, \mathrm{C}_{2} \mathrm{~F}_{4}, \mathrm{C}_{3} \mathrm{~F}, \mathrm{C}_{3} \mathrm{~F}_{4}, \mathrm{C}_{3} \mathrm{~F}_{6}, \mathrm{C}_{3} \mathrm{~F}_{6} \mathrm{O}, \mathrm{C}_{3} \mathrm{O}_{2}, \mathrm{CF}_{4}, \mathrm{C}_{2} \mathrm{~F}_{6}, \mathrm{C}_{2} \mathrm{~F}_{6} \mathrm{O}$, $\mathrm{CF}_{2} \mathrm{O}, \mathrm{CF}_{4} \mathrm{O}, \mathrm{C}_{3} \mathrm{O}_{2}, \mathrm{C}_{3} \mathrm{~F}_{8}, \mathrm{C}_{3} \mathrm{~F}_{7}, \mathrm{C}_{4} \mathrm{~F}_{8} \mathrm{O}, \mathrm{C}_{4} \mathrm{~F}_{10} \mathrm{O}, \mathrm{C}_{5} \mathrm{~F}_{8}, \mathrm{C}_{5} \mathrm{~F}_{10}$, $\mathrm{C}_{5} \mathrm{~F}_{10} \mathrm{O}, \mathrm{C}_{6} \mathrm{~F}_{12} \mathrm{O}$.

The calculation methods of different types of particles are slightly different for the partition function. The atoms can be directly calculated according to Formula 1. In the formula: $Q_{i}^{\text {int }}$ is the internal partition function of particle i; $g_{n}$ is the degeneracy of the $n$th electron energy level; $\varepsilon_{n}$ is the energy value of the $n$th electron energy level.

$$
Q_{i}^{\text {int }}=\sum_{n} g_{n} \exp \left(-\frac{\varepsilon_{n}}{k_{b} T}\right)
$$

When calculating the partition function of diatomic particles, the vibrational energy level and the rotational energy level also need to be considered except the electronic excitation energy level, as shown in Formula 4.

$$
\begin{aligned}
Q_{i}^{\text {int }} & =Q_{i}^{\text {el }} \cdot Q_{i}^{v i b} \cdot Q_{i}^{r o t} \\
= & \frac{1}{\sigma} \sum_{T_{e}}\left\{g_{e} \exp \left(-\frac{T_{e}}{k_{b} T}\right) \sum_{v}^{v_{\max }}\left(g_{v} \exp \left(-\frac{G_{v}\left(T_{v}\right)}{k_{b} T}\right)\right)\right. \\
& \left.\sum_{J}^{J_{\max }}\left(g_{J} \exp \left(-\frac{F_{v}(J)}{k_{b} T}\right)\right)\right\}
\end{aligned}
$$

Where $Q_{i}^{\text {el }}$ is the electron internal partition function of particle $i$, $Q_{i}^{v i b}$ is the oscillation partition function of particle $i, Q_{i}^{r o t}$ is the rotational partition function of particle i, $T_{e}$ is the excitation energy level of the particle, $v$ is the vibrational energy level of the particle, and $J$ is the particle vibration energy level. The spectral data involved can be obtained from the NIST database.

For the calculation of the partition function of polyatomic particles needs to be divided into linear particles and nonlinear particles. During the calculation, some required vibration parameters and rotation parameters can be found in the JANAF thermochemical data manual. In addition, for the macromolecular particles $\mathrm{CF}_{4} \mathrm{O}, \mathrm{C}_{4} \mathrm{~F}_{8}, \mathrm{C}_{4} \mathrm{~F}_{10} \mathrm{O}, \mathrm{C}_{6} \mathrm{~F}_{12} \mathrm{O}, \mathrm{C}_{5} \mathrm{~F}_{8}$, $\mathrm{C}_{5} \mathrm{~F}_{10}, \mathrm{C}_{5} \mathrm{~F}_{10} \mathrm{O}, \mathrm{C}_{2} \mathrm{~F}_{6} \mathrm{O}$ and $\mathrm{C}_{3} \mathrm{~F}_{6} \mathrm{O}$, the models of them are built and the geometric optimizations are carried out in Materials Studio. Then, the vibration parameters and rotation parameters with the stable structures are calculated based on the density functional theory, the results are shown in Table 1.

Based on the partition functions of different particles, the nonlinear equations are obtained in combination with ionization equation, dissociation equation, electric neutrality principle, atomic conservation and Dalton's partial pressure law. The number density of each particle are calculated through Newton iterative method to get the thermodynamic parameters (Cressault, 2001; Cressault and Gleizes, 2004; Boulos et al., 2013).

The transport parameters of $C_{6}F_{10}O$ can be calculated based on the mass, momentum and energy transmission of the particles in the plasma. Based on the interaction potential, the collision integrals between different particles at different temperatures are analyzed and calculated, then, the Chapman-Enskog expansion is performed on them to obtain the transport coefficients. During the calculation of the collision effect, the required parameters of the binding energy, the distance between the two particles when the potential energy is zero and the polarization rate of most macromolecules can be obtained from literature (Cressault et al., 2011). In addition, for other macromolecules, the relevant parameters are calculated by quantum chemistry method in Materials Studio, the calculation results are shown in Table 2.

# Analysis of calculation results

## Number density of particles

The monatomic, diatomic and polyatomic particles can be produced after the ionization and dissociation of $C_{6}F_{12}O$ at

<table><caption>TABLE 1 Calculated values of vibration parameters and rotation parameters of polyatomic particles.</caption>
<thead>
<tr>
<th>Particles</th>
<th>$\boldsymbol{\nu(d)}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>CF₄O</td>
<td>1294.41(1), 1262.5(1), 947.3(1), 882.1(1), 679(1), 584.1(1), 433.7(1), 227.5(1), 1233.2(1), 607.5(1), 250(1)</td>
</tr>
<tr>
<td colspan="2">Ps = 1, $\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 1.1519E-113</td>
</tr>
<tr>
<td>C₄F₈O</td>
<td>1508.2(1), 1322.6(1), 1279.5(1), 1251(1), 1246.1(1), 1214.2(1), 1169(1), 1147.4(1), 1101.6(1), 1027.2(1), 981.3(1), 834.7(1), 765.2(1), 727.6(1), 711(1), 591.4(1), 583.1(1), 550.4(1), 535.8(1), 529.6(1), 519.8(1), 452.4(1), 331.5(1), 323.1(1), 315.5(1), 305.1(1), 290.5(1), 182(1), 164.7(1), 137.6(1), 45.1(1), 42.3(1)</td>
</tr>
<tr>
<td colspan="2">Ps = 1</td>
</tr>
<tr>
<td colspan="2">$\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 3.2371E-111</td>
</tr>
<tr>
<td>C₄F₁₀O</td>
<td>1332.3(1), 1287.8(1), 1276 (1), 1255.9(1), 1242(1), 1215.6(1), 1183.6(1), 1181.5(1), 1172.5(1), 1166.2(1), 1133.5(1), 986.2(1), 909.7(1), 768(1), 723.5(1), 708.2(1), 692.9(1), 609.5(1), 608.1(1), 559.4(1), 557.4(1), 533(1), 490.6(1), 475.4(1), 448.2(1), 347.5(1), 339.8(1), 337.7(1), 307.8(1), 305.8(1), 261.3(1), 216.1(1), 193.2(1), 163.3(1), 135.5(1), 91(1), 80.6(1), 40.3(1), 24.3(1)</td>
</tr>
<tr>
<td colspan="2">Ps = 1</td>
</tr>
<tr>
<td colspan="2">$\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 4.2567E-111</td>
</tr>
<tr>
<td>C₂F₆O</td>
<td>1318.4(1), 1267.0(1), 1248.9(1), 1231.5(1), 1197.5(1), 1144(1), 963.3(1), 845.1(1), 735.3(1), 688.1(1), 649.8(1), 355.5(1), 341(1), 170.7(1), 97.3(1), 31.9(1)</td>
</tr>
<tr>
<td colspan="2">Ps = 1, $\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 1.7203E-111</td>
</tr>
<tr>
<td>C₃F₆O</td>
<td>1553.4(1), 1351.1(1), 1263.6(1), 1213.5(1), 1193.3(1), 1155.8(1), 1132.8(1), 1014.7(1), 802.1(1), 768(1), 717.9(1), 609.5(1), 575.4(1), 565.1(1), 533.7(1), 503.8(1), 424.6(1), 307.2(1), 263.4(1), 247.4(1), 158.5(1), 132.1(1), 43.1(1)</td>
</tr>
<tr>
<td colspan="2">Ps = 1, $\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 2.0509E-111</td>
</tr>
<tr>
<td>C₅F₈</td>
<td>1802.2(1), 1387.9(1), 1375.4(1), 1315.6(1), 1281.6(1), 1203.1(1), 1162.7(1), 1137.7(1), 1134.9(1), 1100.2(1), 1006.4(1), 980.6(1), 861.1(1), 704.7(1), 665.1(1), 627.6(1), 612.3(1), 597.7(1), 501.8(1), 441.1(1), 428.8(1), 412.8(1), 344(1), 308.6(1), 306.5(1), 267.5(1), 257.1(1), 248.1(1), 243.2(1), 219.6(1), 174.4(1), 99.3(1), 39.6(1)</td>
</tr>
<tr>
<td colspan="2">Ps = 1</td>
</tr>
<tr>
<td colspan="2">$\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 3.1973E-111</td>
</tr>
<tr>
<td>C₅F₁₀</td>
<td>1394.2(1), 1322.6(1), 1299.7(1), 1280.2(1), 1244.7(1), 1227.4(1), 1223.2(1), 1182.2(1), 1166.2(1), 1077.9(1), 998.7(1), 950.8(1), 902.1(1), 868(1), 733.9(1), 671.3(1), 630.3(1), 593.5(1), 578.2(1), 543.5(1), 525.4(1), 456.6(1), 438.5(1), 356.5(1), 330.1(1), 311.3(1), 305.1(1), 278.7(1), 273.1(1), 258.5(1), 246.7(1), 239.7(1), 200.1(1), 191.8(1), 145.9(1), 120.9(1), 72.2(1), 39.6(1)</td>
</tr>
<tr>
<td colspan="2">Ps = 1</td>
</tr>
<tr>
<td colspan="2">$\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 4.0108E-111</td>
</tr>
<tr>
<td>C₅F₁₀O</td>
<td>1866.1(1), 1298.3(1), 1284.4(1), 1253.8(1), 1232.2(1), 1215.6(1), 1197.5(1), 1170.4(1), 1165.5(1), 1151.6(1), 1039.7(1), 982(1), 922.3(1), 759.6(1), 762.4(1), 727.6(1), 674.8(1), 633.1(1), 580.3(1), 554.6(1), 544.9(1), 536.5(1), 510.8(1), 472.6(1), 441.3(1), 373.9(1), 341.2(1), 328.7(1), 315.5(1), 304.4(1), 284.9(1), 122.3(1), 74.3(1), 61.16(1), 47.2(1), 27.1(1)</td>
</tr>
<tr>
<td colspan="2">Ps = 1</td>
</tr>
<tr>
<td colspan="2">$\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 3.5812E-111</td>
</tr>
<tr>
<td>C₆F₁₂O</td>
<td>1776(1), 1238(2), 1155(2), 1117(3), 1087(2), 1035(1), 945(2), 829(1), 720(2), 696(1), 652(1), 608(1), 550(3), 505(3), 435(1), 388(2), 342(2), 294(3), 258(3), 179(3), 122(3)</td>
</tr>
<tr>
<td colspan="2">Ps = 1, $\sigma$ = 1</td>
</tr>
<tr>
<td colspan="2">$I_A I_B I_C$ = 1.0161E-110</td>
</tr>
</tbody>
</table>

0.1 MPa. As shown in Figures 2A–C, it is the change of the number density of each particle at 300 K–30000 K. With a rise of temperature, some small molecular particles such as C₂, C₂F₄, C₃, C₃F₄, C₄, C₅, CF, CF₂, CF₂O, CF₃, CF₄, CFO, CO, CO₂ and F₂ are firstly dissociated from C₆F₁₂O between 300 and 3000 K. At the same time, the appearance of C, F and O are accompanied with ionization. As the temperature continuously rises, the number density of most particles begins to decrease and the secondary ionization process occurs. When the temperature is high enough, there are a large number of monatomic particles $C_2^+$, $F_2^+$ and $O_2^+$

<table>
 <thead>
  <tr>
   <th>
    Particles
   </th>
   <th>
    $\varepsilon_{0}/{\mathbf{k}}_{\boldsymbol{b}}$ (K)
   </th>
   <th>
    $\mathbf{α}$($\mathring{A}$)
   </th>
   <th>
    $\mathbf{ξ}$(A-3)
   </th>
   <th>
    Particles
   </th>
   <th>
    $\varepsilon_{0}/{\mathbf{k}}_{\boldsymbol{b}}$ (K)
   </th>
   <th>
    $\mathbf{α}$($\mathring{A}$)
   </th>
   <th>
    $\mathbf{ξ}$(A-3)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    C
   </td>
   <td>
    30.6
   </td>
   <td>
    3.385
   </td>
   <td>
    1.76
   </td>
   <td>
    CF
   </td>
   <td>
    94.2
   </td>
   <td>
    3.635
   </td>
   <td>
    2.317
   </td>
  </tr>
  <tr>
   <td>
    O
   </td>
   <td>
    106.7
   </td>
   <td>
    3.05
   </td>
   <td>
    0.802
   </td>
   <td>
    CF₂
   </td>
   <td>
    108
   </td>
   <td>
    3.977
   </td>
   <td>
    2.874
   </td>
  </tr>
  <tr>
   <td>
    F
   </td>
   <td>
    112.6
   </td>
   <td>
    2.968
   </td>
   <td>
    0.557
   </td>
   <td>
    CF₂O
   </td>
   <td>
    110.917
   </td>
   <td>
    3.473
   </td>
   <td>
    1.88
   </td>
  </tr>
  <tr>
   <td>
    C₂
   </td>
   <td>
    78.8
   </td>
   <td>
    3.913
   </td>
   <td>
    3.2
   </td>
   <td>
    CF₃
   </td>
   <td>
    134
   </td>
   <td>
    4.3
   </td>
   <td>
    3.431
   </td>
  </tr>
  <tr>
   <td>
    C₂F
   </td>
   <td>
    82.3
   </td>
   <td>
    3.256
   </td>
   <td>
    3.412
   </td>
   <td>
    CF₄
   </td>
   <td>
    134
   </td>
   <td>
    4.662
   </td>
   <td>
    3.838
   </td>
  </tr>
  <tr>
   <td>
    C₂F₂
   </td>
   <td>
    94.2
   </td>
   <td>
    3.635
   </td>
   <td>
    4.634
   </td>
   <td>
    CFO
   </td>
   <td>
    108.316
   </td>
   <td>
    3.279
   </td>
   <td>
    2.507
   </td>
  </tr>
  <tr>
   <td>
    C₂F₄
   </td>
   <td>
    108
   </td>
   <td>
    3.977
   </td>
   <td>
    5.748
   </td>
   <td>
    CO
   </td>
   <td>
    91.7
   </td>
   <td>
    3.69
   </td>
   <td>
    1.95
   </td>
  </tr>
  <tr>
   <td>
    C₂F₆
   </td>
   <td>
    195
   </td>
   <td>
    5.5
   </td>
   <td>
    6.82
   </td>
   <td>
    CO₂
   </td>
   <td>
    195.2
   </td>
   <td>
    3.941
   </td>
   <td>
    2.911
   </td>
  </tr>
  <tr>
   <td>
    C₂O
   </td>
   <td>
    57.867
   </td>
   <td>
    3.487
   </td>
   <td>
    3.2
   </td>
   <td>
    F₂
   </td>
   <td>
    112.6
   </td>
   <td>
    3.357
   </td>
   <td>
    1.38
   </td>
  </tr>
  <tr>
   <td>
    C₃
   </td>
   <td>
    48.33
   </td>
   <td>
    3.649
   </td>
   <td>
    4.9
   </td>
   <td>
    F₂O₂
   </td>
   <td>
    109.6
   </td>
   <td>
    3.417
   </td>
   <td>
    2.315
   </td>
  </tr>
  <tr>
   <td>
    C₃F
   </td>
   <td>
    73.76
   </td>
   <td>
    3.308
   </td>
   <td>
    6.028
   </td>
   <td>
    F₂O
   </td>
   <td>
    161
   </td>
   <td>
    3.878
   </td>
   <td>
    1.916
   </td>
  </tr>
  <tr>
   <td>
    C₃F₄
   </td>
   <td>
    41.5
   </td>
   <td>
    3.915
   </td>
   <td>
    7.508
   </td>
   <td>
    FO₂
   </td>
   <td>
    11.02
   </td>
   <td>
    3.2
   </td>
   <td>
    2.161
   </td>
  </tr>
  <tr>
   <td>
    C₃F₆
   </td>
   <td>
    67.155
   </td>
   <td>
    3.636
   </td>
   <td>
    8.888
   </td>
   <td>
    O₂
   </td>
   <td>
    106.7
   </td>
   <td>
    3.467
   </td>
   <td>
    1.5812
   </td>
  </tr>
  <tr>
   <td>
    C₃F₇
   </td>
   <td>
    47.947
   </td>
   <td>
    2.553
   </td>
   <td>
    9.445
   </td>
   <td>
    OF
   </td>
   <td>
    109.6
   </td>
   <td>
    3.412
   </td>
   <td>
    1.359
   </td>
  </tr>
  <tr>
   <td>
    C₃F₈
   </td>
   <td>
    85.57
   </td>
   <td>
    3.497
   </td>
   <td>
    10.134
   </td>
   <td>
    C₆F₁₂O
   </td>
   <td>
    103.2
   </td>
   <td>
    3.627
   </td>
   <td>
    12.34
   </td>
  </tr>
  <tr>
   <td>
    C₃O₂
   </td>
   <td>
    79.757
   </td>
   <td>
    3.538
   </td>
   <td>
    6.884
   </td>
   <td>
    C₄F₈O
   </td>
   <td>
    111.45
   </td>
   <td>
    3.782
   </td>
   <td>
    7.32
   </td>
  </tr>
  <tr>
   <td>
    C₄
   </td>
   <td>
    38.59
   </td>
   <td>
    3.517
   </td>
   <td>
    7.04
   </td>
   <td>
    C₄F₁₀O
   </td>
   <td>
    111.87
   </td>
   <td>
    3.957
   </td>
   <td>
    8.16
   </td>
  </tr>
  <tr>
   <td>
    C₅
   </td>
   <td>
    61.97
   </td>
   <td>
    3.781
   </td>
   <td>
    8.8
   </td>
   <td>
    C₅F₈
   </td>
   <td>
    79.53
   </td>
   <td>
    3.636
   </td>
   <td>
    8.24
   </td>
  </tr>
  <tr>
   <td>
    C₂F₆O
   </td>
   <td>
    131.863
   </td>
   <td>
    3.927
   </td>
   <td>
    4.65
   </td>
   <td>
    C₅F₁₀O
   </td>
   <td>
    109.71
   </td>
   <td>
    3.878
   </td>
   <td>
    9.65
   </td>
  </tr>
  <tr>
   <td>
    C₃F₆O
   </td>
   <td>
    84.55
   </td>
   <td>
    3.343
   </td>
   <td>
    5.68
   </td>
   <td>
    C₅F₁₀
   </td>
   <td>
    85.16
   </td>
   <td>
    3.806
   </td>
   <td>
    8.49
   </td>
  </tr>
  <tr>
   <td>
    CF₄O
   </td>
   <td>
    119.57
   </td>
   <td>
    3.856
   </td>
   <td>
    3.47
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
 </tbody>
</table>

TABLE 2 The key parameters of collision integral the main neutral particle (Yu et al., 2017; Zhong et al., 2017).

in the plasma. Therefore, the proportion of macromolecules is low at high temperature. For polyatomic particles produced during discharge, the number density is relatively low, which is less than $10^{14}$/m³.

As shown in Figure 2D, it is the mass density of C₆F₁₂O, which is obtained by summing the product of the number density and mass corresponding for the above particles. Under the constant pressure, with the increase of the temperature, the total number of particles increases due to the increasing decomposition of the plasma, which can increase the total volume of the system. Therefore, the mass per unit volume continuously decrease. Some small molecular particles appear at 300–3000 K, so the mass density of C₆F₁₂O decreases rapidly in this temperature range.

## Thermodynamic parameters

Based on the particle number density obtained above, the main thermodynamic parameters of enthalpy H, entropy S, specific heat Cₚ and sound velocity Vₛ of C₆F₁₂O are calculated. As shown in Figure 3, it is the calculation results of main thermodynamic parameters of C₆F₁₂O at 0.10 MPa.

As shown in Figure 3, it is the calculation results of main thermodynamic parameters of C₆F₁₂O at 0.10 MPa. Among them, the change trend of enthalpy, entropy and sound velocity is roughly the same as that of most other gases. The specific heat has an obvious peaks in the temperature range of 300–5000 K and 20000–25000 K. The position of the peak is generally considered to be caused by endothermic reaction processes of particles. Therefore, combined with the analysis of the change of particle number density, the peak can be considered to be caused by the dissociation between particles below 1000 K. At higher temperatures, the appearance of the peak is mainly due to the peak change caused by the ionization of atoms.

## Transportation parameters

### Conductivity

Conductivity $\sigma_{e}$ is a physical quantity used to characterize the electron conduction characteristics in plasma, which is closely related to the electron number density and ionization degree. The expression is as follow.

$$
\sigma_{e} = \frac{e^{2}n_{e}}{\sqrt{2m_{e}\pi T} \cdot n_{a}\sigma_{en}} \tag{5}
$$

Where $e$, $n_{e}$, $m_{e}$, $n_{a}$, $\sigma_{en}$ are the amount of elementary charge, number density of electron, electronic mass, number density of

![](./images/865006238969102603_3.jpg)

neutral particles and collision cross section between electrons and neutral particles, respectively. The internal conductivity of $\sigma$ can be obtained by the calculation of Chapman-Enskog third-order approximation. The conductivity of $C_{6}F_{12}O$, $CO_{2}$ and $N_{2}$ at 0.1 MPa is calculated by the above method, as shown in Figure 4. It can be seen that when the temperature is higher than 10000 K, the conductivity difference of the plasma formed by the three gases is small and the curves of them with temperature almost coincide. When the temperature is low, the curves show obvious differences with the change of temperature. Specifically, the curve of $C_{6}F_{12}O$ is higher than that of $CO_{2}$ and $N_{2}$, which is consistent with the properties of most electronegative gases.

Thermal conductivity

The Thermal conductivity $k$ characterizes the ability of a material to directly conduct heat, which is consisted of heavy particle thermal conductivity $k_{h}$, electron thermal conductivity $k_{e}$, internal thermal conductivity $k_{int}$ and reaction thermal conductivity $k_{reac}$. The $k_{h}$, $k_{e}$ and $k_{int}$ are calculated through the second approximation order, the third approximation order and the first approximation order of the Chapman-Enskog method, respectively. The $k_{reac}$ is obtained from the Butler and Brokaw theory. Among them, the internal thermal conductivity is caused by the change of heat transfer energy due to the internal degrees of freedom of particles. The specific calculation method can refer to Reference (Wang et al., 2020b).

Figure 5 shows the calculation results of each part and total thermal conductivity of $C_{6}F_{12}O$. It can be seen that the proportion of thermal conductivity of each part at different temperatures. When the temperature is low, the total thermal conductivity of $C_{6}F_{12}O$ mainly depends on the reaction thermal conductivity, which is related to the enthalpy of particle reaction. When the temperature is higher than 20000 K, the reaction thermal conductivity decreases to a lower level. When the temperature is higher than 7000 K, the electron thermal conductivity increases significantly with the increase of the

![](./images/865006238969102603_4.jpg)

FIGURE 3
The calculation results of main thermodynamic parameters of $C_{6}F_{12}O$.

![](./images/865006238969102603_5.jpg)

FIGURE 4
Conductivity of $C_{6}F_{12}O$, $CO_{2}$ and $N_{2}$.

![](./images/865006238969102603_6.jpg)

FIGURE 5
Calculation results of thermal conductivity of $C_{6}F_{12}O$.

temperature, which is mainly because of the enhancement of atomic ionization and the increase of the electron number density at higher temperature. When the temperature continuously rises to higher than 20,000 K, the contribution of electronic thermal conductivity to the total thermal conductivity is dominant.

![](./images/865006238969102603_7.jpg)

As shown in Figure 6, the thermal conductivities of $CO_2$ and $N_2$ are compared with that of $C_6F_{12}O$. The calculation results of thermal conductivities of $CO_2$ and $N_2$ are consistent with those in literature (Cressault and Gleizes, 2004). Since the types and number densities of particles formed by different gases at different temperatures are different, the thermal conductivities of different gases show different amplitudes for the peaks at different temperatures. At the same time, the number density of electron increases significantly with the gradual increase of temperature, and the change of the whole thermal conductivity shows an upward trend. The thermal conductivity of $C_6F_{12}O$ has three obvious peaks, which appear at 3500 K, 5500 K and 16000 K, respectively.

## Conclusion

In this paper, according to all possible particle types, the nonlinear equations are written through the conditions satisfied by LTE to obtain the number density of each particle. Then, the thermodynamic parameters are obtained with partition function and the transport parameters are obtained by calculating the collision cross sections between different particles. The specific conclusions are as follows:

(1) With the increase of temperature, small molecular particles $C_2$, $C_2F4$, $C_3$, $C_3F_4$, $C_4$, $C_5$, $CF$, $CF_2$, $CF_2O$, $CF_3$, $CF_4$, $CFO$, $CO$, $CO_2$, $F_2$, etc. firstly appear between 300 and 3000 K. At the same time, the appearance of C, F and O are accompanied with ionization. As the temperature continuously rises, the number densities of most particles begin to decrease and the secondary ionization process occurs. When the temperature is high enough, there are a large number of $C_2^+$, $F_2^+$ and $O_2^+$ in the plasma.

(2) When the temperature is higher than 10000 K, the conductivities of the plasma formed by $C_6F_{12}O$, $CO_2$ and $N_2$ at different temperatures are almost the same. At low temperature, the difference of the conductivities is obvious. Specifically, the conductivity of $C_6F_{12}O$ is higher than that of $CO_2$ and $N_2$, which is consistent with the properties of most electronegative gases.

(3) The thermal conductivity of different gases show peaks with different amplitudes at different temperatures and the overall thermal conductivity shows an upward trend. There are three obvious peaks in the thermal conductivity of $C_6F_{12}O$, which appear at 3500, 5500 and 16000 K, respectively.

## Data availability statement

The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding author.

## Author contributions

XR, DL, and XZ performed calculations on the data, BP and LZ performed statistical analysis, and YL and SM wrote the first draft of the paper. All authors contributed to manuscript revision, read, and approved the submitted version.

## Conflict of interest

Authors XR, DL, XZ, BP, LZ, YL, and SM were employed by Electric Power Research Institute of Guangxi Power Grid Co. Ltd.

The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

### References

Boulos, M. I., Fauchais, P., and Pfender, E. (2013). *Thermal plasmas: fundamentals and applications*[M]. New York, NY: Springer Science & Business Media.

Chen, Shuang, and Pan, Yong (2022). Enhancing catalytic properties of noble metal@MoS2/WS2 heterojunction for the hydrogen evolution reaction. *Appl. Surf. Sci.* 591, 153168. doi:10.1016/j.apsusc.2022.153168

Chen, Shuang, and Pan, Yong (2022). Mechanism of interlayer spacing on catalytic properties of MoS2 from *ab-initio* calculation. *Appl. Surf. Sci.* 599, 154041. doi:10.1016/j.apsusc.2022.154041

Cressault, Y., Connord, V., Hingana, H., Teulet, P., and Gleizes, A. (2011). Transport properties of CF3I thermal plasmas mixed with CO2, air or N2 as an alternative to SF6 plasmas in high-voltage circuit breakers[J]. *J. Phys. D. Appl. Phys.* 44 (49), 495202. doi:10.1088/0022-3727/44/49/495202

Cressault, Y., and Gleizes, A. (2004). Thermodynamic properties and transport hydrogene-cuivre [D]. Toulouse: Université Paul Sabatier-Toulouse III.

Cressault, Y., and Gleizes, A. (2004). Thermodynamic properties and transport coefficients in Ar-H2-Cu plasmas. *J. Phys. D. Appl. Phys.* 37 (4), 560-572. doi:10.1088/0022-3727/37/4/008

Hou, H., Yan, X., Yu, X., Liu, W., Liu, Z., and Wang, B. (2019). Theoretical investigation on the adsorption of C4F7N/CO2 dielectric gas and decomposition products in zeolite [J]. *High Volt. Eng.* 45 (04), 1040-1047.

Linteris, G. T., Babushok, V. I., Sunderland, P. B., Takahashi, F., Katta, V. R., Meier, O., et al. (2013). Unwanted combustion enhancement by C6F12O fire suppressant[J]. *Proc. Combust. Inst.* 34 (2), 2683-2690. doi:10.1016/j.proci.2012.06.050

Mantilla, J D., Gariboldi, N., Grob, S., and Claessens, M. (2014). "Investigation of the insulation performance of a new gas mixture with extremely low GWP[C]," in IEEE Electrical Insulation Conference, Philadelphia, PA, USA, 08-11 June 2014 (IEEE), 469-473.

Obama, B. (2017). The irreversible momentum of clean energy. *Science* 355 (6321), 126-129. doi:10.1126/science.aam6284

Pan, Yong (2022). First-principles investigation of structural stability, electronic and optical properties of suboxide (Zr3O). *Mater. Sci. Eng. B* 281, 115746. doi:10.1016/j.mseb.2022.115746

Pan, Yong (2021). Influence of N vacancy on the electronic and optical properties of bulk GaN from first principles investigations. *Int. J. Energy Res.* 45 (10), 15512-15520. doi:10.1002/er.6744

Pan, Yong (2021). The influence of Ag and Cu on the electronic and optical properties of ZrO from first-principles calculations. *Mater. Sci. Semicond. Process.* 135, 106084. doi:10.1016/j.mssp.2021.106084

Rao, X., Li, D., Xia, X., Su, Y., Lu, Y., Peng, B., et al. (2021). Study on discharge decomposition characteristics of environmentally friendly gas C6F12O/CO2 [J]. *Vacuum* 186 (5), 110004. doi:10.1016/j.vacuum.2020.110004

Tang, J., Lei, Z., Wan, Z., Yao, Q., Gao, K., and Zeng, F. (2019). "Reaction Thermodynamics of Overthermal Decomposition of C6F12O [J]," in Proceedings of the CSEE, Rome, Italy, April 7-9, 2019 (CSEE), 5257-5262+5306.

Tian, S., Zhang, X., Song, X., Deng, Z., Yi, L., Tang, J., et al. (2019). Experimental research on insulation properties of C6F12O/N2 and C6F12O/CO2 gas mixtures[J]. *Generation, Transmission & Distribution. IET Gener. Transm. &amp. Distrib.* 13 (3), 417-422. doi:10.1049/iet-gtd.2018.5474

Tian, S., Zhang, X., Song, X., Ran, Z., Wang, D., Deng, Z., et al. (2018). Breakdown characteristics and decomposition characteristics of C6F12O and N2 mixed gas under AC voltage [J]. *Proc. CSEE* 38 (10), 3125-3132. doi:10.13334/j.0258-8013.pcsee.170886

Tian, S., Zhang, X., Wang, Y., Rao, X., Song, X., Li, Y., et al. (2019). Partial discharge characteristics of C6F12O/CO2 mixed gas at power frequency AC voltage [J]. *AIP Adv.* 9 (9), 095057. doi:10.1063/1.5123903

Tian, S., Zhang, X., Yann, C., Hu, J., Wang, B., Song, X., et al. (2019). Research status of replacement gases for SF6 in power industry. *AIP Adv.* 45 (01), 109-116. doi:10.1063/1.5134727

Wang, F., Liu, J., Zhong, L., Hai, B., Zhou, Y., Tang, N., et al. (2020). Theoretical analysis of the decomposition pathways and species of environmentally friendly insulation gas C6F12O based on the DFT and TST[J]. *Plasma Chem. Plasma Process.* 41 (5), 1-21. doi:10.1007/s11090-020-10129-4

Wang, W. Z., Wu, Y., Rong, M. Z., and Yang, F. (2012). Theoretical computation studies for transport properties of air plasmas[J]. *ACTA Phys. SIN.* 61 (10), 105201. doi:10.7498/aps.61.105201

Wang, W., Rong, M., Murphy, A. B., Xu, W., Haibo, S., and Fei, Y. (2011). Calculation analysis on statistic thermodynamic properties of thermal arc plasmas [J]. *Hsi-An Chiao Tung Ta Hsueh/Journal Xi'an Jiaot. Univ.* 45 (4), 86-92.

Wang, Y., Tian, S., Zhang, X., Liu, W., and Zhang, G. (2020). Theoretical calculation of total electron-impact ionization cross section of C6F12O[J]. *AIP Adv.* 10 (3), 035217. doi:10.1063/1.5133830

Xiao, D. (2016). Development prospect of gas insulation based on environmental protection [J]. *High Volt. Eng.* 42 (04), 1035-1046. doi:10.13336/j.1003-6520.hve.20160405020

Yu, X., Hou, H., and Wang, B. (2017). Prediction on dielectric strength and boiling point of gaseous molecules for replacement of SF6[J]. *J. Comput. Chem.* 38 (10), 721-729. doi:10.1002/jcc.24741

Zhang, L., Ye, M., Lei, P., Zhang, Q., Su, Z., and Xu, X. (2020). Calculation of thermodynamic properties of C4F7N mixtures arc plasma [J]. *High Volt. Eng.* 46 (1), 362-368.

Zhang, X., Tian, S., Song, X., Deng, Z., Yi, L., Tang, J., et al. (2017). Insulation strength and decomposition characteristics of a C6F12O and N2 Gas Mixture[J]. *Energies* 10 (8), 1170. doi:10.3390/en10081170

Zhang, X., Wang, Y., Yi, L., Li, Y., Ye, F., Tian, S., et al. (2020). Thermal compatibility properties of C6F12O-air gas mixture with metal materials[J]. *AIP Adv.* 10 (5), 125024. doi:10.1063/1.5131724

Zhang, X., Xiao, H., Tang, J., Cui, Z., and Zhang, Y. (2017). Recent advances in decomposition of the most potent greenhouse gas SF6[J]. *Crit. Rev. Environ. Sci. Technol.* 47 (18), 1763-1782. doi:10.1080/10643389.2017.1400860

Zhang, Z., Lin, X., Yu, W., Xu, J., Zhang, J., and Su, Z. (2020). Thermodynamic calculation of physical properties of C4F7N/CO2 and C4F7N/N2 [J]. *High Volt. Eng.*46 (1), 250-256.

Zhong, L., Rong, M., Wang, X., Wu, J., Han, G., Han, G., et al. (2017). Compositions, thermodynamic properties, and transport coefficients of high-temperature C5F10O mixed with CO2 and O2 as substitutes for SF6 to reduce global warming potential[J]. *AIP Adv.* 7 (7), 075003. doi:10.1063/1.4993305

Yi, L., Zhang, X., Tian, S., Song, X., Li, Y., and Chen, D. (2019). Insight into the decomposition mechanism of C6F12O-CO2 gas mixture [J]. *Chemical Engineering Journal* 360, 929-940. doi:10.1016/j.cej.2018.10.167