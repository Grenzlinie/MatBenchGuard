# Critical Evaluation and Thermodynamic Optimization of the Al-P and Fe-Al-P Systems

Zhimin You¹ · In-Ho Jung²

Submitted: 20 May 2020
© ASM International 2020

## Abstract
The Al-P system and Fe-Al-P system have been thermodynamically optimized using the CALculation of PHAse Diagrams (CALPHAD) method based on critical evaluation of all available experimental data. The liquid phases and solid solutions were modeled using the Modified Quasichemical Model and Compound Energy Formalism, respectively. The Gibbs energies of stoichiometric AlP compound and liquid Al-P solution were critically optimized to reproduce the melting point of AlP and the liquidus of Al-P system on the Al-rich corner. In the ternary Fe-Al-P system, the behavior of P in the liquid was also well optimized with introduction of Toop interpolation technique (Al as an asymmetric component). In addition, various phase equilibria of Fe-Al-P alloys containing up to 30 wt.%Al and 15 wt.%P, isothermal sections at 450, 650 and 800 °C, and the solubility of P in BCC_A2 Fe-Al alloys were excellently described, compared to experimental data. According to the present optimization, an accurate and consistent thermodynamic database of the Fe-Al-P system has been developed.

Keywords AlP · Al-P system · CALPHAD · Fe-Al-P system · thermodynamic database

✉ Zhimin You
zhimin.you@mail.mcgill.ca

In-Ho Jung
in-ho.jung@snu.ac.kr

¹ Department of Mining and Materials Engineering, McGill University, 3610 University Street, Montreal, QC H3A 0C5, Canada
² Department of Materials Science and Engineering, and Research Institute of Advanced Materials (RIAM), Seoul National University, 1 Gwanak-ro, Gwanak-gu, Seoul 08826, South Korea

---

## 1 Introduction
With increasingly high demand for the safety and energy-efficiency of automotive, light alloy such as Al is often added into the new generation automotive steels for reducing the weight and improving the mechanical properties simultaneously. To further enhance the corrosion resistance, paintability and also the weldability of steels, the galvannealings were always applied on the steel plate surface.⁽¹⁾ In high Al steels, phosphorus on one hand plays a positive role in solid solution strengthening and corrosion resistance of the steels, but on the other hand, enrichment of P in the grain boundary inhibits formation of coating layers.⁽²⁾ Besides, the galvannealing coating layer pulverization and flaking off the substrate are very challenging difficulties during the stamping process, which largely increase the defective and repairing rate. Moreover, P, as the typical metalloid impurity of steels, can also cause unexpected steel defects like brittleness and inner cracks. Therefore, it is very necessary to tightly control the P impurity of the steels below the allowed level. In the Fe-Al alloys containing high concentration of P, formation of aluminum phosphide (AlP) and various iron phosphides depends on the temperature and composition. As is well known, AlP is highly toxic compound widely used as rodenticide, insecticide, fumigant.⁽³⁾ Hence, very cautious attention needs to be paid to the application of high Al and high P materials. Nevertheless, aluminum phosphide and iron phosphides are also widely applied in high power and high frequency manufacturing, such as semiconductor diodes.⁽⁴,⁵⁾ To explore as much application potential as possible without sacrificing their mechanical properties, it is very essential to understand the thermodynamic behaviors of the Fe-Al-P system in terms of service conditions.

---

Published online: 13 July 2020
![](./images/812590248524513280_1.jpg)

Previously, many experimental and computational studies have been conducted to investigate the sub-systems of the Fe-Al-P system. Besides, reviews on the Fe-P system were given by Okamoto $^{[6]}$ and Schlesinger, $^{[7]}$ the Al-P system by McAlister $^{[8]}$ and Okamoto, $^{[9]}$ and the Fe-Al-P system by Raghavan, $^{[10-12]}$ and Schmid-Fetzer and Tomashik. $^{[13]}$ The Fe-P system was thermodynamically assessed in many studies $^{[14-18]}$ and by the present authors. $^{[19]}$ The Al-P system and the Fe-Al-P system was optimized by Ansara et al., $^{[20]}$ Tu et al., $^{[21]}$ Wu et al., $^{[22]}$ Liang and Schmid-Fetzer, $^{[23,24]}$ Cao et al., $^{[17]}$ and Miettinen et al. $^{[25]}$ Although the Al-P system is a simple system containing the only stoichiometric AlP compound, inconsistency among available experimental data has not been resolved in the previous assessments. $^{[17,20-24]}$ In the recent assessment by Miettinen et al., $^{[25]}$ experimental data of the binary Al-P system was reasonably reproduced, but the accuracy was not maintained when extending to the ternary Fe-Al-P system, compared with available experimental data. Therefore, it is necessary to resolve the discrepancies left in previous modeling by reoptimizing the Fe-Al-P system.

Thermodynamic database based on the CALculation of PHAse Diagrams (CALPHAD) method is a powerful tool for new materials design and process optimization. The database of target system is developed by means of thermodynamic modeling (optimization), aiming at obtaining one set of consistent Gibbs energies of all phases as functions of temperature and composition. In the optimization, all available phase equilibria and thermodynamic data such as activity, entropy, enthalpy, and Gibbs energy, etc. are critically evaluated simultaneously. The discrepancy between available data are resolved in the critical evaluation process, and the Gibbs energy functions for all related phases in target system are derived. Prediction on unexplored thermodynamic properties and phase equilibria can be possible by interpolations and extrapolations in a thermodynamically correct manner.

In the present study, the liquid phases and solid solutions of the binary Al-P and ternary Fe-Al-P systems were described using the Modified Quasichmical Model (MQM) $^{[26,27]}$ and Compound Energy Formalism (CEF), $^{[28]}$ respectively. The Fe-Al system originally optimized by Sundman et al. $^{[29]}$ with recent modification by Phan et al., $^{[30,31]}$ and the Fe-P system reassessed by present authors $^{[19]}$ were adopted in the present study. The solubility of P in liquid Al, thermodynamic properties of stoichiometric AlP compound, various isopleth diagrams, isothermal diagrams, liquid surface projection and the activity of P in molten Fe-Al-P alloys will be optimized to reproduce reliable experimental data. All the calculations were performed using FactSage software. $^{[32]}$

![](./images/812590248524513280_2.jpg)

## 2 Thermodynamic Models

### 2.1 Pure Elements and Stoichiometric Compounds

The Gibbs energies of elemental Fe, Al and P were taken from Scientific Group Thermodata Europe (SGTE) database. $^{[33]}$ The Gibbs energies of stoichiometric compounds involved in the Fe-Al-P system were determined based on available thermodynamic data including heat capacity, standard enthalpy of formation and standard entropy at 298.15 K. In the present study, the Gibbs energies of stoichiometric compounds were calculated as follows:

$$
\begin{aligned}
G_{T}^{\circ}= & \left(\Delta H_{298.15 \mathrm{K}}^{\circ}+\int_{298.15 \mathrm{K}}^{T} C_{\mathrm{P}} d T\right) \\
& -T\left(S_{298.15 \mathrm{K}}^{\circ}+\int_{298.15 \mathrm{K}}^{T} \frac{C_{\mathrm{P}}}{T} d T\right)
\end{aligned}
\qquad \text{(Eq 1)}
$$

where $G_{T}^{\circ}$ is the Gibbs energy (J/mol) at temperature $T(\mathrm{K})$, $\Delta H_{298.15 \mathrm{K}}^{\circ}$ and $S_{298.15 \mathrm{K}}^{\circ}$ are standard enthalpy of formation (J/mol) and standard entropy (J/mol/K) at 298.15 K, respectively, and $C_{\mathrm{P}}$ is the heat capacity (J/mol/K). The heat capacity of each stoichiometric compound was expressed as a function of temperature by fitting experimental $C_{\mathrm{P}}$ data. For the compounds with no available experimental data, their $C_{\mathrm{P}}$ functions were estimated using Neumann-Kopp (NK) rule $^{[34]}$ or based on determined $C_{\mathrm{P}}$ of neighboring compounds in the same system.

When a pure element or stoichiometric compound exhibits magnetic behavior, an additional Gibbs energy of magnetic contribution term $G^{\mathrm{mg}}$ will be applied. In the Fe-Al-P system, the magnetic contribution terms for Fe (BCC_A2, FCC_A1) and $\mathrm{Fe}_{3} \mathrm{P}$ were determined using the empirical expression proposed by Inden $^{[35]}$ and modified by Hillert and Jarl $^{[36]}$:

$$
G^{m g}=R T \ln (\beta+1) g(\tau) \qquad \text{(Eq 2)}
$$

where $\tau$ is expressed as $T / T^{*}$ and $T^{*}$ is the critical temperature of magnetic transition associated with Curie temperature $T_{C}$ for ferromagnetic materials or Neel temperature $T_{N}$ for antiferromagnetic materials. $\beta$ is the average magnetic moment per mole of atoms in Bohr magnetons. $g(\tau)$ is a polynomial function derived by Hillert and Jarl., $^{[36]}$ as expressed below:

$$
g(\tau)=1-\left[\frac{79 \tau^{-1}}{140 P}+\frac{474}{497}\left(\frac{1}{P}-1\right)\left(\frac{\tau^{3}}{6}+\frac{\tau^{9}}{135}+\frac{\tau^{15}}{600}\right)\right] / D \quad \tau \leq 1
\qquad \text{(Eq 3)}
$$

$$
g(\tau)=-\left(\frac{\tau^{-5}}{10}+\frac{\tau^{-15}}{315}+\frac{\tau^{-25}}{1500}\right) / D \quad \tau>1
\qquad \text{(Eq 4)}
$$

where $D=\frac{518}{1125}+\frac{11692}{15975}\left(\frac{1}{P}-1\right)$, and the value of $P$ can be considered as the fraction of the magnetic enthalpy absorbed above the critical temperature depending on the

structure. $P$ is 0.40 for the simple BCC_A2 phase while $P$ is 0.28 for other common phases.

### 2.2 Solid Solutions

In the binary Fe-P system, solid solutions including disordered FCC_A1 and BCC_A2 were considered in the present study. $^{[19]}$ As is well known, P is not soluble in solid Al, so no stable solid solution is taken into account in the binary Al-P system. In the binary Fe-Al system, the BCC phase undergoes a long-range ordering from disordered BCC_A2 structure to ordered BCC_B2 structure transition. Another ordered D0₃ phase $^{[29]}$ in maximized Fe₃Al composition was not considered in this work for keeping the consistency in extending to multicomponent systems. Besides, disordered FCC_A1, Al₈Fe₅ and Al₁₃Fe₄ solid solutions are also taken into account. In the ternary Fe-Al-P system, Al can substitute the Fe atoms of Fe₃P and Fe₂P to form Me₃P and Me₂P solid solutions in the formulas (Fe, Al)₃P and (Fe, Al)₂P, respectively. The Gibbs energies of all solid solutions in the sub-systems of the Fe-Al-P system were described using the Compound Energy Formalism (CEF) $^{[28]}$ considering their crystallographic structures.

#### 2.2.1 FCC_A1 Solid Solutions

The disordered FCC_A1 solid solution was modeled with the formula (Fe, Al, P)₁(Va)₁, and its Gibbs energy was calculated using the following equation:

$$
\begin{aligned}
G_{S}^{\text{disorder}} =& \sum_{i=\text{Fe,Al,P}} x_{i}G_{i}^{o} + RT \sum_{i=\text{Fe,Al,P}} x_{i} \ln x_{i} \\
&+ \sum_{m=0,1,2...} x_{\text{Fe}}x_{\text{P}}L_{\text{Fe,P}}^{m} + \sum_{k=0,1,2...} x_{\text{Al}}x_{\text{P}}L_{\text{Al,P}}^{k} \\
&+ \sum_{p=0,1,2...} x_{\text{Fe}}x_{\text{Al}}L_{\text{Fe,Al}}^{p} + \sum_{q=0,1,2...} x_{\text{Fe}}x_{\text{Al}}x_{\text{P}}L_{\text{Fe,Al,P}}^{q} \\
&+ G^{mg}
\end{aligned}
\qquad (\text{Eq 5})
$$

where $x_i$ is the mole fraction of component $i$ and $G_i^o$ is the molar Gibbs energy (J/mol) of pure solid $i$ ($i$ = Fe, Al, P); $R$ and $T$ are the gas constant (8.314 J/mol K) and temperature in Kelvin (K); $L_{\text{Fe,P}}^{m}$, $L_{\text{Al,P}}^{k}$, $L_{\text{Fe,Al}}^{p}$ and $L_{\text{Fe,Al,P}}^{q}$ are the adjustable interaction parameters of corresponding binary and ternary systems; $G^{\text{mg}}$ is the magnetic contribution to the Gibbs energy (J/mol).

#### 2.2.2 Disordered/Ordered BCC Solid Solutions

The BCC phase exhibits a transition from disordered to ordered crystallographic structure. The Gibbs energy of BCC solution was modeled combining the disordered part with the model (Fe, Al, P)₁(Va)₃ and the ordered part with the model (Fe, Al, P)₀.₅(Fe, Al, P)₀.₅(Va)₃. The Gibbs energy of the disordered part was calculated using Eq 5, which is the same as that for disordered FCC_A1 phase. The Gibbs energy contribution from the ordered part was calculated as follows:

$$
\Delta G_{BCC}^{order} = G_{BCC}^{order}(y_{i}', y_{j}'') - G_{BCC}^{order}(y_{i}', y_{j}'')_{y_{k}'=y_{k}''}
\qquad (\text{Eq 6})
$$

$$
\begin{aligned}
G_{BCC}^{order}(y_{i}', y_{j}'') =& y_{\text{Fe}}'y_{\text{Fe}}'G_{\text{Fe:Fe}} + y_{\text{Al}}'y_{\text{Al}}'G_{\text{Al:Al}} + y_{\text{P}}'y_{\text{P}}'G_{\text{P:P}} \\
&+ y_{\text{Fe}}'y_{\text{Al}}''G_{\text{Fe:Al}} + y_{\text{Al}}'y_{\text{Fe}}''G_{\text{Al:Fe}} + y_{\text{Fe}}'y_{\text{P}}''G_{\text{Fe:P}} \\
&+ y_{\text{Al}}'y_{\text{P}}''G_{\text{Al:P}} + y_{\text{P}}'y_{\text{Fe}}''G_{\text{P:Fe}} + y_{\text{P}}'y_{\text{Al}}''G_{\text{P:Al}} \\
&+ 0.5RT\left(y_{\text{Fe}}' \ln y_{\text{Fe}}' + y_{\text{Al}}' \ln y_{\text{Al}}' + y_{\text{P}}' \ln y_{\text{P}}'\right) \\
&+ 0.5RT\left(y_{\text{Fe}}'' \ln y_{\text{Fe}}'' + y_{\text{Al}}'' \ln y_{\text{Al}}'' + y_{\text{P}}'' \ln y_{\text{P}}''\right) \\
&+ \sum_{i,j,k} y_{i}'y_{j}'y_{k}''L_{i,j:k} + \sum_{i,j,k} y_{k}'y_{i}''y_{j}''L_{k:i,j} + G^{mg}
\end{aligned}
\qquad (\text{Eq 7})
$$

here $i, j, k$ are the component symbols of Fe, Al, P. $y_{i}', y_{j}', y_{k}'$ and $y_{i}'', y_{j}'', y_{k}''$ are site fractions of component $i, j, k$ in the first and second lattice of the formula (Fe, Al, P)₀.₅(Fe, Al, P)₀.₅(Va)₃. The total Gibbs energy of the BCC solid solution combining contribution from both disordered and ordered parts was determined using Eq 8:

$$
G_{BCC}^{sol.} = G_{S}^{\text{disorder}} + \Delta G_{BCC}^{order}
\qquad (\text{Eq 8})
$$

When the site fractions of component $i$ in the first sublattice equals to that in the second sublattice ($y_{i}' = y_{i}''$), then the ordering contribution $\Delta G_{BCC}^{order}$ is nil and the Gibbs energy of BCC phase can be calculated using Eq 5. However, in the case of $y_{i}' \neq y_{i}''$, then the ordering contribution $\Delta G_{BCC}^{order}$ becomes negative and the Gibbs energy of BCC_B2 phase can be described with Eq 8.

#### 2.2.3 Other Solid Solutions ($Al_8Fe_5$, $Al_{13}Fe_4$, $Me_3P$, $Me_2P$)

The solid solutions including Al₈Fe₅, Al₁₃Fe₄, Me₃P and Me₂P were also modeled using the formulas (Al, Fe)₈(Al, Fe)₅, (Al)₃₂(Fe)₁₂(Al, Va)₇, (Fe, Al)₃P, and (Fe, Al)₂P, respectively, on the basis of CEF. $^{[28]}$ The Gibbs energy of Al₈Fe₅ was calculated using the equation below:

$$
\begin{aligned}
G_{\text{Al}_8\text{Fe}_5}^{sol.} =& y_{\text{Al}}'y_{\text{Al}}''G_{\text{Al:Al}} + y_{\text{Fe}}'y_{\text{Fe}}''G_{\text{Fe:Fe}} \\
&+ y_{\text{Al}}'y_{\text{Fe}}''G_{\text{Al:Fe}} + y_{\text{Fe}}'y_{\text{Al}}''G_{\text{Fe:Al}} \\
&+ 8RT\left(y_{\text{Al}}' \ln y_{\text{Al}}' + y_{\text{Fe}}' \ln y_{\text{Fe}}'\right) \\
&+ 5RT\left(y_{\text{Al}}'' \ln y_{\text{Al}}'' + y_{\text{Fe}}'' \ln y_{\text{Fe}}''\right) \\
&\sum_{\substack{i=\text{Al,Fe} \\ m=0,1,2...}} y_{\text{Al}}'y_{\text{Fe}}'y_{i}''L_{\text{Al,Fe}:i}^{m} \\
&+ \sum_{\substack{j=\text{Al,Fe} \\ n=0,1,2...}} y_{j}'y_{\text{Al}}''y_{\text{Fe}}''L_{j:\text{Al,Fe}}^{n}
\end{aligned}
\qquad (\text{Eq 9})
$$

![](./images/812590248524513280_3.jpg)

where $G_{\text{Al:Al}}$, $G_{\text{Fe:Fe}}$, $G_{\text{Al:Fe}}$, $G_{\text{Fe:Al}}$ are the end-member Gibbs energies (J/mol); $y_{\text{Al}}'$, $y_{\text{Al}}''$, $y_{\text{Fe}}'$, $y_{\text{Fe}}''$ are the site fractions of Al and Fe in specified lattice; $L_{\text{Al,Fe}:i}^{m}$, $L_{j:\text{Al,Fe}}^{n}$ are the adjustable interaction parameters. The Gibbs energy of $\text{Al}_{13}\text{Fe}_{4}$ was calculated as follows:

$$
\begin{aligned}
G_{\text{Al}_{13}\text{Fe}_{4}}^{\text{sol.}} &= y_{\text{Al}}G_{\text{Al:Fe:Al}} + y_{\text{Va}}G_{\text{Al:Fe:Va}} \\
&\quad + 7RT(y_{\text{Al}} \ln y_{\text{Al}} + y_{\text{Va}} \ln y_{\text{Va}}) \\
&\quad + \sum_{m=0,1,2...} y_{\text{Al}}y_{\text{Va}}L_{\text{Al:Fe:Al,Va}}^{m}
\end{aligned} \tag{Eq 10}
$$

where $G_{\text{Al:Fe:Al}}$ and $G_{\text{Al:Fe:Va}}$ are end-member Gibbs energies (J/mol); $y_{\text{Al}}$, $y_{\text{Va}}$ are site fractions of Al and vacancies in the third sublattice; $L_{\text{Al:Fe:Al,Va}}^{m}$ is the adjustable interaction parameter. The Gibbs energies of $\text{Me}_{3}\text{P}$ and $\text{Me}_{2}\text{P}$ phases are expressed as follows:

$$
\begin{aligned}
G_{\text{Me}_{n}\text{P}}^{\text{sol.}} &= y_{\text{Fe}}G_{\text{Fe}_{n}\text{P}}^{\circ} + y_{\text{Al}}G_{\text{Al}_{n}\text{P}} \\
&\quad + nRT(y_{\text{Fe}} \ln y_{\text{Fe}} + y_{\text{Al}} \ln y_{\text{Al}}) \\
&\quad + \sum_{m=0,1,2...} y_{\text{Fe}}y_{\text{Al}}L_{\text{Fe,Al:P}}^{m} + G^{\text{mg}}
\end{aligned} \tag{Eq 11}
$$

where $n$ is the number of substitutional site within the formulas $\text{Me}_{3}\text{P}(n=3)$ and $\text{Me}_{2}\text{P}(n=2)$; $\text{G}_{\text{Fe}_{3}\text{P}}^{\circ}$ and $\text{G}_{\text{Fe}_{2}\text{P}}^{\circ}$ are optimized Gibbs energies (J/mol) of stoichiometric $\text{Fe}_{3}\text{P}$ and $\text{Fe}_{2}\text{P}$ compounds respectively in the Fe-P system $^{[19]}$; $G_{\text{Al}_{3}\text{P}}$ and $G_{\text{Al}_{2}\text{P}}$ are Gibbs energies (J/mol) of the end-members $\text{Al}_{3}\text{P}$ and $\text{Al}_{2}\text{P}$, respectively; $y_{\text{Fe}}$ and $y_{\text{Al}}$ are site fractions of Fe and Al respectively in the substitutional sublattice; $L_{\text{Fe,Al:P}}^{\text{m}}$ is the adjustable interaction parameter; $G^{\text{mg}}$ is the magnetic contribution to the Gibbs energy (J/mol).

### 2.3 Liquid Solution

The liquid solution was described using the Modified Quasichemical Model (MQM)$^{[26,27]}$ accounting for the short-range ordering of the nearest-neighbor atoms explicitly. Comparing to the conventional Bragg-Williams Random Mixing Model (BWRMM), the MQM gives more realistic description of the entropy of liquid solution. In the MQM, the Gibbs energy of pair formation can be expanded as a polynomial in the pair fraction rather than the component fraction, and the coordination number of each component is allowed to vary with composition for reproducing the short-range ordering of liquid solution with less parameters, providing greater flexibility in reproducing experimental data of the binary liquids and higher-order systems.

In the case of the binary $A$-$B$ liquid solution, the atoms $A$ and $B$ are distributed over the quasilattice sites. The atom pair exchanging reaction of liquid $A$-$B$ solution can be expressed as follows:

$$(A-A)+(B-B)=2(A-B) ; \Delta g_{A B} \tag{Eq 12}$$

here, $(i-j)$ represents the nearest-neighbor pair between components $i$ and $j$, and $\Delta g_{A B}$ is the Gibbs energy change (J/mol) of forming 2 mol $(A-B)$ pairs. The Gibbs energy of liquid solution was calculated:

$$G_{A B}^{L}=\left(n_{A} G_{A}^{\circ}+n_{B} G_{B}^{\circ}\right)-T \Delta S_{A B}^{\text {conf. }}+n_{A B}\left(\Delta g_{A B} / 2\right) \tag{Eq 13}$$

where $n_{A}$ and $n_{B}$ are the numbers of moles of A atoms and B atoms, and $G_{A}^{\circ}$ and $G_{B}^{\circ}$ are the molar Gibbs energies (J/mol) of pure liquid A and B. $\Delta S_{A B}^{\text {conf. }}$ is the configurational entropy (J/mol/K) of mixing given by random distribution of the $(A$-$A)$, $(B$-$B)$ and $(A$-$B)$ pairs as follows:

$$
\begin{aligned}
\Delta S_{A B}^{\text {conf. }} &= -R\left(n_{A} \ln X_{A}+n_{B} \ln X_{B}\right) \\
&-R\left[n_{A A} \ln \left(\frac{X_{A A}}{Y_{A}^{2}}\right)+n_{B B} \ln \left(\frac{X_{B B}}{Y_{B}^{2}}\right)+n_{A B} \ln \left(\frac{X_{A B}}{2 Y_{A} Y_{B}}\right)\right]
\end{aligned} \tag{Eq 14}
$$

here $n_{A A}$, $n_{B B}$ and $n_{A B}$ are the numbers of moles of $(A$-$A)$, $(B$-$B)$ and $(A$-$B)$ pairs; $X_{A A}$, $X_{A B}$ and $X_{A B}$ are the pair fraction of the corresponding atom pairs; $Y_{A}$ and $Y_{B}$ are the coordination equivalent fractions of atoms $A$ and $B$. The pair fractions $X_{A A}$, $X_{A B}$, $X_{B B}$ and coordination equivalent fractions $Y_{A}$, $Y_{B}$ were calculated as follows:

$$X_{A A}=n_{A A} /\left(n_{A A}+n_{A B}+n_{B B}\right) \tag{Eq 15}$$

$$X_{A B}=n_{A B} /\left(n_{A A}+n_{A B}+n_{B B}\right) \tag{Eq 16}$$

$$X_{B B}=n_{B B} /\left(n_{A A}+n_{A B}+n_{B B}\right) \tag{Eq 17}$$

$$Y_{A}=X_{A A}+\frac{1}{2} X_{A B} \tag{Eq 18}$$

$$Y_{B}=X_{B B}+\frac{1}{2} X_{A B} \tag{Eq 19}$$

$\Delta g_{A B}$ in Eqs 12 and 13 is the model parameter for reproducing the Gibbs energy of the binary $A$-$B$ solution, which can be expanded as a polynomial based on the atomic pair fractions $X_{A A}$ and $X_{B B}$ as follows:

$$\Delta g_{A B}=\Delta g_{A B}^{\circ}+\sum_{i \geq 1} g_{A B}^{i 0} X_{A A}^{i}+\sum_{j \geq 1} g_{A B}^{0 j} X_{B B}^{j} \tag{Eq 20}$$

where $\Delta g_{A B}^{\circ}$, $g_{A B}^{i 0}$ and $g_{A B}^{0 j}$ are the adjustable model parameters that can be functions of the temperature. In the MQM, the coordination numbers of $A$ and $B$, $Z_{A}$ and $Z_{B}$, can be varied with composition to reproduce the short-range ordering of the solution:

$$\frac{1}{Z_{A}}=\frac{1}{Z_{A A}^{A}}\left(\frac{2 n_{A A}}{2 n_{A A}+n_{A B}}\right)+\frac{1}{Z_{A B}^{A}}\left(\frac{n_{A B}}{2 n_{A A}+n_{A B}}\right) \tag{Eq 21}$$

![](./images/812590248524513280_4.jpg)

$$
\frac{1}{Z_{B}}=\frac{1}{Z_{B B}^{B}}\left(\frac{2 n_{B B}}{2 n_{B B}+n_{A B}}\right)+\frac{1}{Z_{B A}^{B}}\left(\frac{n_{A B}}{2 n_{B B}+n_{A B}}\right) \qquad \text{(Eq 22)}
$$

here, $Z_{A A}^{A}$ is the value $Z_{A}$ when all nearest neighbors of an $A$ atom are $A$ atoms and $Z_{A B}^{A}$ is the value of $Z_{A}$ when all nearest neighbors of an $A$ atom are $B$ atoms. $Z_{B B}^{B}$ and $Z_{B A}^{B}$ are defined in an analogous manner. When extending from the binary systems to the ternary system, the Gibbs energy of ternary liquid solution can be predicted using a proper geometric interpolation technique based on the nature of all involved binary liquid solutions. If necessary, ternary correction terms can also be introduced to give more precise description of phase equilibria and thermodynamic properties of the ternary liquid solution. In the Fe-Al-P system, the liquid Fe-P exhibits much more negative deviation from ideal mixing, compared to liquid Al-P and Fe-Al solutions. Therefore, the Toop-type interpolation technique $^{[27]}$ with $\mathrm{Al}$ as the asymmetric component was applied to the liquid Fe-Al-P solution. The Gibbs energy and configurational entropy of mixing of liquid Fe-Al-P solution were calculated as follows:

$$
\begin{aligned}
G_{\mathrm{FeAlP}}^{L}= & \sum_{i=\mathrm{Fe}, \mathrm{Al}, \mathrm{P}} n_{i} G_{i}^{\circ}-T \Delta S_{\mathrm{FeAlP}}^{\text {conf. }}+\sum_{j, k=\mathrm{Fe}, \mathrm{Al}, \mathrm{P}}^{j \neq k}\left(n_{j k} / 2\right) \Delta g_{j k} \\
& \qquad \text{(Eq 23)}
\end{aligned}
$$

$$
\begin{aligned}
\Delta S_{\mathrm{FeAlP}}^{\text {conf. }}= & -R \sum_{i=\mathrm{Fe}, \mathrm{Al}, \mathrm{P}} n_{i} \ln X_{i}-R\left[\sum_{j=\mathrm{Fe}, \mathrm{Al}, \mathrm{P}} n_{j j}\left(\frac{X_{j j}}{Y_{j}^{2}}\right)\right. \\
& \left.+\sum_{k, m=\mathrm{Fe}, \mathrm{Al}, \mathrm{P}}^{k \neq m} n_{k m} \ln \left(\frac{X_{k m}}{2 Y_{k} Y_{m}}\right)\right] \qquad \text{(Eq 24)}
\end{aligned}
$$

where each pair formation Gibbs energy $\Delta g_{\mathrm{FeP}}, \Delta g_{\mathrm{AIP}}$ and $\Delta g_{\mathrm{FeAl}}$ depends on the symmetry of each component (Fe, $\mathrm{Al}, \mathrm{P})$ in the ternary solution. Therefore, $\Delta g_{\mathrm{AIP}}$ and $\Delta g_{\mathrm{AlFe}}$ between asymmetric components can be described as follows:

$$
\begin{aligned}
\Delta g_{\mathrm{FeAl}}= & \Delta g_{\mathrm{FeAl}}^{\circ}+\sum_{(i+j) \geq 1} g_{\mathrm{FeAl}}^{i j} x_{\mathrm{AlAl}}^{i}\left(x_{\mathrm{FeFe}}+x_{\mathrm{FeP}}+x_{\mathrm{PP}}\right)^{j} \\
& +\sum_{i \geq 0, j \geq 0, k \geq 1} g_{\mathrm{FeAl}(\mathrm{P})}^{i j k} x_{\mathrm{AlAl}}^{i}\left(x_{\mathrm{FeFe}}+x_{\mathrm{FeP}}+x_{\mathrm{AlAl}}\right)^{j}\left(\frac{Y_{\mathrm{P}}}{Y_{\mathrm{Fe}}+Y_{\mathrm{P}}}\right)^{k} \\
& \qquad \text{(Eq 25)}
\end{aligned}
$$

$$
\begin{aligned}
\Delta g_{\mathrm{AIP}}= & \Delta g_{\mathrm{AIP}}^{\circ}+\sum_{(i+j) \geq 1} g_{\mathrm{AIP}}^{i j} x_{\mathrm{AlAl}}^{i}\left(x_{\mathrm{FeFe}}+x_{\mathrm{FeP}}+x_{\mathrm{PP}}\right)^{j} \\
& +\sum_{i \geq 0, j \geq 0, k \geq 1} g_{\mathrm{AIP}(\mathrm{Fe})}^{i j k} x_{\mathrm{AlAl}}^{i}\left(x_{\mathrm{FeFe}}+x_{\mathrm{FeP}}+x_{\mathrm{AlAl}}\right)^{j}\left(\frac{Y_{\mathrm{Fe}}}{Y_{\mathrm{Fe}}+Y_{\mathrm{P}}}\right)^{k} \\
& \qquad \text{(Eq 26)}
\end{aligned}
$$

and $\Delta g_{\mathrm{FeP}}$ between symmetric $\mathrm{Fe}$ and $\mathrm{P}$ was calculated as follows:

$$
\begin{aligned}
\Delta g_{\mathrm{FeP}}= & \Delta g_{\mathrm{FeP}}^{\circ}+\sum_{(i+j) \geq 1} g_{\mathrm{FeP}}^{i j}\left(\frac{x_{\mathrm{FeFe}}}{x_{\mathrm{FeFe}}+x_{\mathrm{FeP}}+x_{\mathrm{PP}}}\right)^{i} \\
& \times\left(\frac{x_{\mathrm{PP}}}{x_{\mathrm{FeFe}}+x_{\mathrm{FeP}}+x_{\mathrm{PP}}}\right)^{j}+\sum_{i \geq 0, j \geq 0, k \geq 1} g_{\mathrm{FeP}(\mathrm{Al})}^{i j k} \\
& \times\left(\frac{x_{\mathrm{FeFe}}}{x_{\mathrm{FeFe}}+x_{\mathrm{FeP}}+x_{\mathrm{PP}}}\right)^{i}\left(\frac{x_{\mathrm{PP}}}{x_{\mathrm{FeFe}}+x_{\mathrm{FeP}}+x_{\mathrm{PP}}}\right)^{j} Y_{\mathrm{Al}}^{k} \\
& \qquad \text{(Eq 27)}
\end{aligned}
$$

where $g_{\mathrm{AIP}}^{i j}, g_{\mathrm{FeAl}}^{i j}, g_{\mathrm{FeP}}^{i j}$ are the binary liquid parameters; $g_{\mathrm{FeAl}(\mathrm{P})}^{i j k}, g_{\mathrm{AIP}(\mathrm{Fe})}^{i j k}$ and $g_{\mathrm{FeP}(\mathrm{Al})}^{i j k}$ are the ternary liquid parameters.

<table><caption>Table 1 Summary of crystal structure information of all solid phases in the Fe-Al-P system</caption>
<thead>
  <tr>
    <th>Phase</th>
    <th>Structure</th>
    <th>Prototype</th>
    <th>Space group</th>
    <th>Pearson symbol</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>FCC_A1</td>
    <td>Cubic</td>
    <td>Cu</td>
    <td>Fm3m</td>
    <td>cF4</td>
  </tr>
  <tr>
    <td>BCC_A2</td>
    <td>Cubic</td>
    <td>W</td>
    <td>Im3m</td>
    <td>cI2</td>
  </tr>
  <tr>
    <td>BCC_B2</td>
    <td>Cubic</td>
    <td>CsCl</td>
    <td>Pm3m</td>
    <td>cP8</td>
  </tr>
  <tr>
    <td>Fe₃Al</td>
    <td>Cubic</td>
    <td>BiF3</td>
    <td>Fm3m</td>
    <td>cF16</td>
  </tr>
  <tr>
    <td>Me₃P</td>
    <td>Tetragonal</td>
    <td>Ni₃P</td>
    <td>I4</td>
    <td>tI32</td>
  </tr>
  <tr>
    <td>Me₂P</td>
    <td>Hexagonal</td>
    <td>Fe₂P</td>
    <td>P62m</td>
    <td>hP9</td>
  </tr>
  <tr>
    <td>FeP</td>
    <td>Orthorhombic</td>
    <td>MnP</td>
    <td>Pnma</td>
    <td>oP8</td>
  </tr>
  <tr>
    <td>FeP₂</td>
    <td>Orthorhombic</td>
    <td>FeS₂</td>
    <td>Pnnm</td>
    <td>oP6</td>
  </tr>
  <tr>
    <td>AIP</td>
    <td>Hexagonal</td>
    <td>ZnS</td>
    <td>F43m</td>
    <td>cF8</td>
  </tr>
  <tr>
    <td>Al₂Fe</td>
    <td>Rhombohedral</td>
    <td>FeAl2</td>
    <td>P1</td>
    <td>aP18</td>
  </tr>
  <tr>
    <td>Al₅Fe₂</td>
    <td>Orthorhombic</td>
    <td>Al₅Fe₂</td>
    <td>Cmcm</td>
    <td>oC16</td>
  </tr>
  <tr>
    <td>Al₈Fe₅</td>
    <td>Cubic</td>
    <td>Zn₈Cu₅</td>
    <td>I43m</td>
    <td>cI52</td>
  </tr>
  <tr>
    <td>Al₁₃Fe₄</td>
    <td>Monoclinic</td>
    <td>Al₁₃Fe₄</td>
    <td>C2/m</td>
    <td>mC102</td>
  </tr>
  <tr>
    <td>White P</td>
    <td>Cubic</td>
    <td>P₄</td>
    <td>I43m</td>
    <td>C*8</td>
  </tr>
  <tr>
    <td>Red P</td>
    <td>…</td>
    <td>P</td>
    <td>…</td>
    <td>C*66</td>
  </tr>
</tbody>
</table>

![](./images/812590248524513280_5.jpg)

<table>
<caption>Table 2 Optimized model parameters for the Fe-Al-P system (J/mol, J/mol K)</caption>
<thead>
<tr>
<th>Phase</th>
<th>Model parameters</th>
</tr>
</thead>
<tbody>
<tr>
<td>Liquid (Fe, Al, P)</td>
<td>$Z_{\text{FeFe}}^{\text{Fe}} = Z_{\text{AlAl}}^{\text{Al}} = Z_{\text{PP}}^{\text{P}} = 6^{[30,31,*]}$</td>
</tr>
<tr>
<td></td>
<td>$Z_{\text{PFe}}^{\text{P}} = Z_{\text{PAl}}^{\text{P}} = Z_{\text{FeAl}}^{\text{Fe}} = Z_{\text{AlFe}}^{\text{Al}} = Z_{\text{AlP}}^{\text{Al}} = 6, ^{[19,30,31,*]} Z_{\text{FeP}}^{\text{Fe}} = 3^{[19]}$</td>
</tr>
<tr>
<td></td>
<td>$\Delta g_{\text{FeP}} = -56902 + 6.569T + (5481 + 3.033T)X_{\text{FeFe}} + (-11966 + 2.51T)X_{\text{FeFe}}^{2} - 9623X_{\text{PP}}^{[19]}$</td>
</tr>
<tr>
<td></td>
<td>$\Delta g_{\text{AlP}} = -21443 + 6.9036T$ [*]</td>
</tr>
<tr>
<td></td>
<td>$\Delta g_{\text{FeAl}} = -20292 + 3.347T - (1674 + 1.255T)X_{\text{FeFe}} - 1046X_{\text{FeFe}}^{2} - (10460 - 4.184T)X_{\text{AlAl}}^{[30,31]}$</td>
</tr>
<tr>
<td></td>
<td>$g_{\text{FeP(Al)}}^{101} = -20920 + 5.6484T$, $g_{\text{FeP(Al)}}^{011} = -104600$</td>
</tr>
<tr>
<td></td>
<td>“Toop-type” interpolation with Al as an asymmetric component [*]</td>
</tr>
<tr>
<td>FCC_A1 (Fe,Al,P)₁(Va)₁</td>
<td>$G_{\text{Fe:Va}}^{\text{FCC}} = G_{\text{Fe(FCC)}}^{\circ}$, $G_{\text{Al:Va}}^{\text{FCC}} = G_{\text{Al(FCC)}}^{\circ}$, $G_{\text{P:Va}}^{\text{FCC}} = G_{\text{P(FCC)}}^{\circ}$ [*]</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,P:Va}}^{\text{FCC}} = -139787.44 + 6.4852T^{[19]}$</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Al,P:Va}}^{\text{FCC}} = -18828$ [*]</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,Al:Va}}^{\text{FCC}} = -105855 + 30.65T - (29017 - 4.91T)(x_{\text{Fe}} - x_{\text{Al}}) + (32200 - 17T)(x_{\text{Fe}} - x_{\text{Al}})^{2[30,31]}$</td>
</tr>
<tr>
<td></td>
<td>$T_{\text{CFe:Va}} = -201$, $\beta_{\text{Fe:Va}} = -2.1^{[37]}$</td>
</tr>
<tr>
<td>BCC_A2 (Fe,Al,P)₁(Va)₃</td>
<td>$G_{\text{Fe:Va}}^{BCC\_A2} = G_{\text{Fe(BCC)}}^{\circ}$, $G_{\text{Al:Va}}^{BCC\_A2} = G_{\text{Al(BCC)}}^{\circ}$, $G_{\text{P:Va}}^{BCC\_A2} = G_{\text{P(BCC)}}^{\circ}$ [*]</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,P:Va}}^{BCC\_A2} = -203476.3 + 15.4808T + 33472(y_{\text{Fe}} - y_{\text{P}})^{[19]}$</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Al,P:Va}}^{BCC\_A2} = -6276$ [*]</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,Al:Va}}^{BCC\_A2} = -123044 + 31.99T - 2945(x_{\text{Fe}} - x_{\text{Al}}) - 3347(x_{\text{Fe}} - x_{\text{Al}})^{2[30,31]}$</td>
</tr>
<tr>
<td></td>
<td>$T_{\text{CFe,P:Va}} = -285, ^{[19]} T_{\text{CFe,Al:Va}} = -438 + 1720(y_{\text{Fe}} - y_{\text{Al}})^{[30,31]}$</td>
</tr>
<tr>
<td></td>
<td>$T_{\text{CFe:Va}} = 1043$, $\beta_{\text{Fe:Va}} = 2.22^{[37]}$</td>
</tr>
<tr>
<td>BCC_B2</td>
<td>$G_{\text{Fe:Al:Va}}^{BCC\_B2} = G_{\text{Al:Fe:Va}}^{BCC\_B2} = -14462 - 3.973T^{[29-31]}$</td>
</tr>
<tr>
<td>(Fe,Al,P)₀.₅(Fe,Al,P)₀.₅(Va)₃</td>
<td>$G_{\text{Fe:Va}}^{BCC\_B2} = G_{\text{Al:Va}}^{BCC\_B2} = 0^{[30,31]} G_{\text{P:P:Va}}^{BCC\_B2} = G_{\text{Fe:P:Va}}^{BCC\_B2} = G_{\text{Al:P:Va}}^{BCC\_B2} = G_{\text{P:Fe:Va}}^{BCC\_B2} = G_{\text{P:Al:Va}}^{BCC\_B2} = 0$ [*]</td>
</tr>
<tr>
<td></td>
<td>$T_{\text{CFe:Al:Va}} = T_{\text{CAl:Fe:Va}} = -250,^{[29]} \beta_{\text{Fe:Al:Va}} = \beta_{\text{Al:Fe:Va}} = -2.72^{[29]}$</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,Al:Al}}^{BCC\_B2} = 1665.37 - 4T + 524(y_{\text{Fe}} - y_{\text{Al}}) - 1560(y_{\text{Fe}} - y_{\text{Al}})^{2[29]}$</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Al:Fe,Al}}^{BCC\_B2} = 1665.37 - 4T + 524(y_{\text{Fe}} - y_{\text{Al}}) - 1560(y_{\text{Fe}} - y_{\text{Al}})^{2[29]}$</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,Al:Fe}}^{BCC\_B2} = -5346 - 1.6T + 524(y_{\text{Fe}} - y_{\text{Al}}) - 1560(y_{\text{Fe}} - y_{\text{Al}})^{2[29]}$</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe:Fe,Al}}^{BCC\_B2} = -5346 - 1.6T + 524(y_{\text{Fe}} - y_{\text{Al}}) - 1560(y_{\text{Fe}} - y_{\text{Al}})^{2[29]}$</td>
</tr>
<tr>
<td></td>
<td>$T_{\text{CFe,Al:Al:Va}} = T_{\text{CFe,Al:Fe:Va}} = T_{\text{CFe:Fe,Al:Va}} = T_{\text{CAl:Fe,Al:Va}} = -250^{[29]}$</td>
</tr>
<tr>
<td></td>
<td>$\beta_{\text{Fe,Al:Al:Va}} = \beta_{\text{Fe,Al:Fe:Va}} = -0.6 + 1.6(y_{\text{Fe}} - y_{\text{Al}}) + 0.4(y_{\text{Fe}} - y_{\text{Al}})^{2[29]}$</td>
</tr>
<tr>
<td></td>
<td>$\beta_{\text{Fe:Fe,Al:Va}} = \beta_{\text{Al:Fe,Al:Va}} = -0.6 + 1.6(y_{\text{Fe}} - y_{\text{Al}}) + 0.4(y_{\text{Fe}} - y_{\text{Al}})^{2[29]}$</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,Al:Fe,Al:Va}}^{BCC\_B2} = -16800 - 3.6T^{[29-31]}$</td>
</tr>
<tr>
<td>Al₈Fe₅ (Al, Fe)₈(Al, Fe)₅</td>
<td>$G_{\text{Al:Al}} = 13G_{\text{Al(BCC)}}^{\circ},^{[29]} G_{\text{Fe:Fe}} = 13G_{\text{Fe(BCC)}}^{\circ} + 13000^{[29]}$</td>
</tr>
<tr>
<td></td>
<td>$G_{\text{Al:Fe}} = 8G_{\text{Al(BCC)}}^{\circ} + 5G_{\text{Fe(BCC)}}^{\circ} - 384500 + 30T^{[29-31]}$</td>
</tr>
<tr>
<td></td>
<td>$G_{\text{Fe:Al}} = 8G_{\text{Fe(BCC)}}^{\circ} + 5G_{\text{Al(BCC)}}^{\circ} + 200000 + 30T^{[29-31]} L_{\text{Al:Al,Fe}}^{\text{Al}_8\text{Fe}_5} = -133888,^{[30,31]}$</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Al,Fe:Fe}}^{\text{Al}_8\text{Fe}_5} = -174000^{[29]}$</td>
</tr>
<tr>
<td>Al₁₃Fe₄ (Al)₃₂(Fe)₁₂(Al,Va)₇</td>
<td>$G_{\text{Al:Fe:Al}} = 39G_{\text{Al(FCC)}}^{\circ} + 12G_{\text{Fe(BCC)}}^{\circ} - 1564680 + 377T^{[29]}$</td>
</tr>
<tr>
<td></td>
<td>$G_{\text{Al:Fe:Va}} = 32G_{\text{Al(FCC)}}^{\circ} + 12G_{\text{Fe(BCC)}}^{\circ} - 1433100 + 377T^{[29]}$</td>
</tr>
<tr>
<td>Me₃P</td>
<td>$G_{\text{Fe:P}}^{\text{Me}_3\text{P}} = G_{\text{Fe}_3\text{P}}^{\circ} ^{[19]}$</td>
</tr>
<tr>
<td>(Fe, Al)₃(P)₁</td>
<td>$G_{\text{Al:P}}^{\text{Me}_3\text{P}} = 3G_{\text{Al(FCC)}}^{\circ} + G_{\text{P(White)}}^{\circ} - 14830 + 85T$ [*]</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,Al:P}}^{\text{Me}_3\text{P}} = -346025 + 50T$ [*]</td>
</tr>
<tr>
<td>Me₂P (Fe, Al)₂(P)₁</td>
<td>$G_{\text{Fe:P}}^{\text{Me}_2\text{P}} = G_{\text{Fe}_2\text{P}}^{\circ} ^{[19]}$</td>
</tr>
<tr>
<td></td>
<td>$G_{\text{Al:P}}^{\text{Me}_2\text{P}} = 2G_{\text{Al(FCC)}}^{\circ} + G_{\text{P(White)}}^{\circ} + 50000$ [*]</td>
</tr>
<tr>
<td></td>
<td>$L_{\text{Fe,Al:P}}^{\text{Me}_2\text{P}} = -175728$ [*]</td>
</tr>
</tbody>
</table>

![](./images/812590248524513280_6.jpg)

<table>
<caption>Table 2 continued</caption>
<thead>
<tr>
<th>Phase</th>
<th>Model parameters</th>
</tr>
</thead>
<tbody>
<tr>
<td>FeP[¹⁹] (Fe)₁(P)₁</td>
<td>$\Delta H_{298.15K}^{\circ}=-126100$, $S_{298.15K}^{\circ}=47.77$<br>$C_{P}=43.7878+0.01985T-232000T^{-2}$</td>
</tr>
<tr>
<td>FeP₂[¹⁹] (Fe)₁(P)₂</td>
<td>$\Delta H_{298.15K}^{\circ}=-191100$, $S_{298.15K}^{\circ}=51.05$<br>$C_{P}=77.52563+0.009348T-443846T^{-2}-1.1\times10^{-6}T^{2}$</td>
</tr>
<tr>
<td>AlP [*] (Al)₁(P)₁</td>
<td>$\Delta H_{298.15K}^{\circ}=-163000$, $S_{298.15K}^{\circ}=40.34$<br>$C_{P}=48.53+0.00457T-690000T^{-2}$</td>
</tr>
<tr>
<td>Al₂Fe[³⁰,³¹]<br>(Al)₂(Fe)₁</td>
<td>$G_{\text{Al}_2\text{Fe}}^{\circ}=2G_{\text{Al(FCC)}}^{\circ}+G_{\text{Fe(BCC)}}^{\circ}-94850+13.42T$</td>
</tr>
<tr>
<td>Al₅Fe₂[³⁰,³¹]<br>(Al)₅(Fe)₂</td>
<td>$G_{\text{Al}_5\text{Fe}_2}^{\circ}=5G_{\text{Al(FCC)}}^{\circ}+2G_{\text{Fe(BCC)}}^{\circ}-217301+34.83T$</td>
</tr>
</tbody>
</table>

*Optimized in the present study

## 3 Critical Evaluation and Thermodynamic Optimization

Thermodynamic optimization of the Fe-Al-P system was performed using the CALPHAD approach based on critical evaluation of all available phase equilibria and thermodynamic data. The liquid and solid solutions of all sub-systems were described using MQM[²⁶,²⁷] and CEF,[²⁸] respectively. White P were selected as the reference state of P in the solid phases. The crystal structure information of all solid phases in the Fe-Al-P system is summarized in Table 1. The optimized model parameters of the Fe-Al-P system are summarized in Table 2.

### 3.1 The Fe-P and Fe-Al Systems

The Fe-P system was optimized by present authors[¹⁹] using the CALPHAD approach. The Fe-Al system assessed by Sundman et al.[²⁹] was modified by Phan et al.[³⁰,³¹] In particular, they used the MQM to model the liquid phase. The optimized parameters of the above Fe-P and Fe-Al systems were adopted in the present study. The calculated phase diagrams of the Fe-P and Fe-Al systems are plotted in Fig. 1. With suppression of gas phase, 3 solutions including liquid, FCC_A1 and BCC_A2 phases and 4 stoichiometric compounds including Fe₃P, Fe₂P, FeP and FeP₂ are considered in the Fe-P system.[¹⁹] P is soluble in $\gamma$-Fe and $\alpha$-Fe of the Fe-rich region, as shown in Fig. 1(a). In the Fe-Al system, 5 solutions including liquid, FCC_A1, BCC_A2, BCC_B2, Al₈Fe₅, Al₁₃Fe₄ and 2 stoichiometric compounds Al₂Fe, Al₅Fe₂ are taken into account.

### 3.2 The Al-P System

In the Al-P system, AlP is well known as the only stable stoichiometric compound. White and Bushey[³⁸] adopted a few approaches to produce AlP and eventually confirmed AlP as the only stable intermediate stoichiometric aluminum phosphide in the Al-P system, which was also supported by Panish and Ilegems,[³⁹] and Ilegems and Panish.[⁴⁰,⁴¹] The crystal structure of AlP was characterized as ZnS-blende cubic type.[³⁸,⁴²,⁴³] The melting point of AlP was experimentally determined at $2530\pm30$ °C by Kischio.[⁴⁴] The liquidus of the Al-rich region was investigated experimentally by Panish et al.,[⁴⁵] Beer,[⁴⁶] and Lescuyer et al.[⁴⁷] The present Al-P phase diagram is compared with previous one in Fig. 2 along with experimental data. According to the present optimization, the melting temperature of AlP is calculated to be 2532 °C, compared to 2557 °C by Ansara et al.,[²⁰] 2528 °C by Tu et al.,[²¹] 2539 °C by Wu et al.,[²²] 2529 °C by Cao et al.,[¹⁸] 2522 °C by Liang et al.,[²³] 2360 °C by Liang and Schmid-Fetzer,[²⁴] and 2534 °C by Miettinen et al.[²⁵] That is, the melting point of AlP reported by Kischio[⁴⁴] was basically favored in all assessments except in the recent one by Liang and Schmid-Fetzer.[²⁴] However, the liquidus of the Al-rich and P-rich regions are very scattering among the assessments. As indicated in Fig. 2(b), the experimental data of P dissolution in molten Al were neglected by Tu et al.,[²¹] Wu et al.,[²²] and Cao et al.[¹⁸] Liang and Schmid-Fetzer[²⁴] modified their earlier result[²³] with respect to the experiments conducted by Lescuyer et al.,[⁴⁷] but at the sacrifice of accuracy in reproducing the melting point of AlP. Beer[⁴⁶] equilibrated AlP with molten Al at 900 to 1200 °C to measure the solubility of P in quenched samples using colorimetric phosphovanadomolybdate method (CPM). The accuracy of his experimental data relies too much on the dissolution and reprecipitation of AlP crystals in the liquid. Panish et al.[⁴⁵] estimated the solubility of P in liquid Al based on the solubility of P in Ga-rich Ga-Al liquid solution with assumption of ideal mixing of Ga and Al. This assumption can result in big errors in the solubility of P in pure Al despite of small interaction between liquid Ga and Al. Lescuyer et al.[⁴⁷] measured the concentration

![](./images/812590248524513280_7.jpg)

Fig. 1 The optimized phase diagrams of the (a) Fe-P system¹⁹ and (b) Fe-Al system³⁰

![](./images/812590248524513280_8.jpg)

of P in two types of samples: a few hundred grams of isothermally filtered liquid Al-P metal and isolated isothermally filtered liquid Al-P drops. The accuracy of their experimental results can be ensured by two analyses. As can be seen in Fig. 2(b), the data by Lescuyer et al.⁴⁷ are favored in the present study and by Miettinen et al.²⁵ No experimental data are available in the P-rich region due to high vaporization of P.

The heat capacity of AlP compound is plotted in Fig. 3 along with a few sets of data obtained from calorimetry experiments.⁴⁸⁻⁵⁰ The constant heat capacity from 300 to 1200 K by Cox and Pool⁴⁸ is less likely. In contrast, the data by Peviak and Sandulova⁴⁹ and Itagaki and Yamaguchi⁵⁰ are more favored in this work to obtain the $C_P$ of stoichiometric AlP compound.

The standard enthalpy of formation $\Delta H_{298.15K}^\circ$ and standard entropy $S_{298.15K}^\circ$ of AlP are summarized in Tables 3 and 4, respectively. As listed in Table 3, Wang et al.⁴³ obtained $\Delta H_{298.15K}^\circ=-138.80\pm8.37$ kJ/mol as the standard enthalpy of AlP by means of oxygen bomb calorimetry. Peviak and Sandulova⁴⁹ determined a much more negative value ($\Delta H_{298.15K}^\circ=-180.33\pm9.62$ kJ/mol) from the heat of reaction $3\text{H}_2\text{SO}_4+\text{AlP}=\text{Al}_2(\text{SO}_4)_3+2\text{PH}_3$. In comparison, $\Delta H_{298.15K}^\circ=$

![](./images/812590248524513280_9.jpg)

Fig. 2 The Al-P phase diagram
in the (a) full composition and
(b) Al-rich region

![](./images/812590248524513280_10.jpg)

$-165.27\pm 2.09$ by Kischio$^{[44]}$ using HCl solution calorimetry method and $163.15\pm 1.72$ kJ/mol by Martosudirdjo and Pratt$^{[51]}$ using precipitation calorimetry method are more favored in the present optimization ($\Delta H_{298.15\mathrm{K}}^{\circ}=-163.15$ kJ/mol).

There was no available experimental data on the standard entropy ($S_{298.15\mathrm{K}}^{\circ}$) of stoichiometric AlP compound. Various estimations$^{[53-56]}$ and assessments$^{[18,21-25]}$ of $S_{298.15\mathrm{K}}^{\circ}$ of AlP range from 36.00 to 57.39 J/mol/K, excluding an incredibly high value (175.32 J/mol/K) given by Ansara et al.$^{[20]}$ In the present study, the standard entropy ($S_{298.15\mathrm{K}}^{\circ}$) of AlP was determined as 40.34 J/mol/K, as listed in Table 4. According to the currently optimized $\Delta H_{298.15\mathrm{K}}^{\circ}$, $S_{298.15\mathrm{K}}^{\circ}$ and $C_{\mathrm{P}}$ of AlP, the partial pressures of Al(g) and $\mathrm{P}_{2}(\mathrm{g})$ in equilibrium with solid AlP, which were obtained from Knudsen effusion experiments by Maria et al.,$^{[57]}$ were well reproduced along with a wide temperature range, as shown in Fig. 4.

### 3.3 The Fe-Al-P System

In the ternary Fe-Al-P system, the liquid phase, solid solutions including BCC_A2, BCC_B2, FCC_A1, $\mathrm{Al}_{8}\mathrm{Fe}_{5}$, $\mathrm{Al}_{13}\mathrm{Fe}_{4}$, $\mathrm{Me}_{3}\mathrm{P}$ and $\mathrm{Me}_{2}\mathrm{P}$, and stoichiometric compounds

![](./images/812590248524513280_11.jpg)

![](./images/812590248524513280_12.jpg)

Table 3 Standard enthalpy of
formation ($\Delta H_{298.15K}^\circ$) of AlP in
the Al-P system

<table>
  <thead>
    <tr>
      <th>$\Delta H_{298.15K}^\circ$, kJ/mol</th>
      <th>Methods</th>
      <th>References</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$-138.80\pm8.37$</td>
      <td>Oxygen Bomb Calorimetry</td>
      <td>Wang et al.$^{[43]}$</td>
    </tr>
    <tr>
      <td>$-165.27\pm2.09$</td>
      <td>Acid Solution Calorimetry</td>
      <td>Kischio$^{[44]}$</td>
    </tr>
    <tr>
      <td>$-180.33\pm9.62$</td>
      <td>Acid Solution Calorimetry</td>
      <td>Peviak and Sandulova$^{[49]}$</td>
    </tr>
    <tr>
      <td>$-163.15\pm1.72$</td>
      <td>Precipitation Calorimetry</td>
      <td>Martosudirdjo and Pratt$^{[51]}$</td>
    </tr>
    <tr>
      <td>$-148.56$</td>
      <td>Assessment</td>
      <td>Ansara et al.$^{[20]}$</td>
    </tr>
    <tr>
      <td>$-102.00$</td>
      <td>Assessment</td>
      <td>Tu et al.$^{[21]}$</td>
    </tr>
    <tr>
      <td>$-166.52$</td>
      <td>Assessment</td>
      <td>Wu et al.$^{[22]}$</td>
    </tr>
    <tr>
      <td>$-148.00$</td>
      <td>Assessment</td>
      <td>Cao et al.$^{[18]}$</td>
    </tr>
    <tr>
      <td>$-163.20$</td>
      <td>Assessment</td>
      <td>Liang et al.$^{[23]}$</td>
    </tr>
    <tr>
      <td>$-163.20$</td>
      <td>Assessment</td>
      <td>Liang and Schmid-Fetzer$^{[24]}$</td>
    </tr>
    <tr>
      <td>$-163.69$</td>
      <td>Assessment</td>
      <td>Miettinen et al.$^{[25]}$</td>
    </tr>
    <tr>
      <td>$-163.15$</td>
      <td>Assessment</td>
      <td>This work</td>
    </tr>
  </tbody>
</table>

including FeP, FeP₂, AlP, Al₂Fe and Al₅Fe₂ were taken into account. The parameters of FCC_A1, BCC_A2 and BCC_B2 phases in the Al-P system were optimized to reproduce phase equilibria of the ternary Fe-Al-P system. In addition, the solubility of Al in Fe₃P and Fe₂P were also calculated. It should be noted that no ternary parameter was necessary for FCC_A1, BCC_A2 and BCC_B2 solid solutions.

### 3.3.1 Phase Diagram

Vogel and Klose$^{[58]}$ carried out a series of experiments to study the liquidus and solidus of the ternary Fe-Al-P system by means of differential thermal analysis (DTA) and microscopic analysis (MA). Experimental results of the Fe-Al-P isopleths at the composition of wt.%P = 6 and 9 and wt.%Al = 10 and 25 were compared with present calculations in Fig. 5. As can be seen in the figure, the experimental data up to 30 wt.%Al and 15 wt.%P were excellently reproduced.

The solubility of P in $\alpha$-Fe (BCC_A2) with addition of Al at 1000 °C was investigated by Kaneko et al.$^{[59]}$ using chemical analysis (CA) and x-ray diffraction (XRD) techniques. It was found that saturation of P in BCC_A2 solution resulted in precipitation of the ternary phosphide Me₃P, which is in the Ni₃P-prototype crystal structure. In this work, the isothermal section of the Fe-Al-P system at 1000 °C on the Fe-rich corner was calculated and

![](./images/812590248524513280_13.jpg)

compared with experimental results in Fig. 6. As shown in the figure, the solubility of P in ferrite Fe-Al alloys decreases from 2.28 to 1.0 in weight percent with the added Al increases up to 5 in weight percent, and the present calculation is in good agreement with the experimental data.

Figure 7 shows the isothermal phase diagrams of the Fe-Al-P system at the temperatures of 450, 650 and 800 °C. The phase equilibria of the Fe-Al-P system was studied by Wu et al. $^{[22]}$ and Huang $^{[1]}$ by annealing various compositions of alloys within 20 at.%P at 450 and 650 °C for 60 days. The equilibrated specimens were analyzed using scanning electron microscopy (SEM) coupled with energy dispersive spectroscopy (EDS) and x-ray diffraction (XRD). In their experiments, $^{[1,22]}$ the $Al_{2}Fe$, $Al_{5}Fe_{2}$, $Al_{13}Fe_{4}$, $Me_{3}P$, $Me_{2}P$, AlP, disordered BCC_A2 and ordered BCC_B2 phases were observed, which has also been verified by the present database, as shown in Fig. 7(a) and (b). Kaneko et al. $^{[59,60]}$ found that $Fe_{3}P$ containing 1.1wt.%Al was in equilibrium with the ferrite alloy in the composition of Fe-0.49wt.%Al-0.96wt.%P at 800 °C. In order to reproduce this data, the Gibbs energy of $Al_{3}P$ in $Me_{3}P$ was optimized.

<table>
<caption>Table 4 Standard entropy ($S_{298.15K}^\circ$) of AlP in the Al-P system</caption>
<thead>
<tr>
<th>$S_{298.15K}^\circ$, J/mol/K</th>
<th>Methods</th>
<th>References</th>
</tr>
</thead>
<tbody>
<tr>
<td>38.06</td>
<td>Estimation</td>
<td>Sharifov$^{[52]}$</td>
</tr>
<tr>
<td>39.36</td>
<td>Estimation</td>
<td>Karapetyants and Karapetyants$^{[53]}$</td>
</tr>
<tr>
<td>$46.89\pm2.51$</td>
<td>Estimation</td>
<td>Marina et al.$^{[54]}$</td>
</tr>
<tr>
<td>47.28</td>
<td>Estimation</td>
<td>Voronin and Nashelskii$^{[55]}$</td>
</tr>
<tr>
<td>47.30</td>
<td>Estimation</td>
<td>Kubaschewski and Alcock$^{[56]}$</td>
</tr>
<tr>
<td>175.32</td>
<td>Assessment</td>
<td>Ansara et al.$^{[20]}$</td>
</tr>
<tr>
<td>57.39</td>
<td>Assessment</td>
<td>Tu et al.$^{[21]}$</td>
</tr>
<tr>
<td>47.28</td>
<td>Assessment</td>
<td>Wu et al.$^{[22]}$</td>
</tr>
<tr>
<td>55.11</td>
<td>Assessment</td>
<td>Cao et al.$^{[18]}$</td>
</tr>
<tr>
<td>40.39</td>
<td>Assessment</td>
<td>Liang et al.$^{[23]}$</td>
</tr>
<tr>
<td>36.00</td>
<td>Assessment</td>
<td>Liang and Schmid-Fetzer$^{[24]}$</td>
</tr>
<tr>
<td>42.11</td>
<td>Assessment</td>
<td>Miettinen et al.$^{[25]}$</td>
</tr>
<tr>
<td>40.34</td>
<td>Assessment</td>
<td>This work</td>
</tr>
</tbody>
</table>

### 3.3.2 Liquid Surface Projection

The liquid projection of the Fe-Al-P system is predicted in Fig. 8. All predicted invariant reactions are summarized in Table 5. Besides, the available experimental data$^{[58]}$ representing the quasi-peritectic reaction $\mathrm{L}+\mathrm{Me}_{3}\mathrm{P}=\mathrm{Me}_{2}\mathrm{P}+\mathrm{BCC\_A2}$ and eutectic reaction $\mathrm{L}=\mathrm{AlP}+\mathrm{Me}_{2}\mathrm{P}+\mathrm{BCC\_B2}$ are imposed for comparison. As can be seen in the figure, the calculated eutectic reaction ($\mathrm{L}=\mathrm{AlP}+\mathrm{Me}_{2}\mathrm{P}+\mathrm{BCC\_B2}$) is in satisfactory agreement with the experimental datapoint **E1**. However, the prediction of the quasi-peritectic reaction at point **U1** is deviated from the experimental result. This is mainly ascribed to the stability of $Me_{3}P$ phase relative to $Me_{2}P$ and BCC_A2 phases. This discrepancy cannot be avoided unless sacrificing the accuracy of phase equilibria presented in Fig. 5 and 6. In addition, other invariant reactions at points **U2**, **U3**, **U4**, **U5**, **U6**, **U7**, **U8**, **U9** and **E2** involved in the Fe-Al-P system are also predicted based on the optimized thermodynamic database, as shown in Fig. 8 and Table 5. To

![](./images/812590248524513280_14.jpg)

Fig. 5 Calculated isopleths of
the Fe-Al-P system at
(a) wt.%P = 6, (b) wt.%P = 9,
(c) wt.%Al = 10, and
(d) wt.%Al = 25, compared to
the experimental data$^{[58]}$

![](./images/812590248524513280_15.jpg)

Fig. 5 continued

![](./images/812590248524513280_16.jpg)

Fig. 6 Isothermal phase
diagram of the Fe-Al-P system
on the Fe-rich corner at
1000 °C, compared with the
experimental data $^{[59]}$

![](./images/812590248524513280_17.jpg)

validate these predictions, further experimental studies are still necessary.

### 3.3.3 Activity of P in Liquid Fe-Al-P Solution

Yamada and Kato $^{[61,62]}$ investigated the influence of Al on the activity coefficient of P in molten Fe at 1600 °C using Knudsen effusion method (KEM). In their experiments, the concentration of P in the samples was maintained at 1 wt.% while that of Al was increased up to 5 wt.%. They calculated the activity coefficient interaction parameter $\varepsilon_{\mathrm{Al}}^{\mathrm{P}} = 4.6 \pm 0.7$ at 1600 °C based on their experimental results. In comparison, Ban-ya et al. $^{[63]}$ measured the vapor pressure of phosphorus above the Fe-Al-P melts containing 2.46 to 2.97 wt.%Al at 1400 °C using transportation method (TM), and calculated $\varepsilon_{\mathrm{Al}}^{\mathrm{P}} = 3.57 \pm 0.33$ for this temperature. These experimental results are compared with present calculations in Fig. 9. As shown in the figure, the present calculations are in reasonable agreement with the experimental data. $^{[61-63]}$ According to present optimization, the activity coefficient interaction parameters are determined as $\varepsilon_{\mathrm{Al}}^{\mathrm{P}} = 2.878$ at 1600 °C and $\varepsilon_{\mathrm{Al}}^{\mathrm{P}} = 2.655$ at 1400 °C.

![](./images/812590248524513280_18.jpg)

![](./images/812590248524513280_19.jpg)

![](./images/812590248524513280_20.jpg)

![](./images/812590248524513280_21.jpg)

Fig. 7 Isothermal phase diagrams of the Fe-Al-P system at the temperatures of (a) 450 °C, (b) 650 °C, and (c) 800 °C

![](./images/812590248524513280_22.jpg)

Fig. 8 Liquid projection of the Fe-Al-P system together with experimental data $^{[58]}$

## 4 Summary

The binary Al-P and ternary Fe-Al-P systems have been thermodynamically optimized in the full composition range based on critical evaluation of available thermodynamic and phase equilibria data. The Modified Quasichemical Model (MQM) and Compound Energy Formalism (CEF) were used to model the liquid and solid solutions, respectively. Dissolution of P in liquid Al, the melting point of stoichiometric AlP compound, and thermodynamic properties of AlP compound in the binary Al-P system were accurately described. The optimized parameters of binary Al-P system and recently optimized Fe-Al and Fe-P systems were combined to describe the ternary Fe-Al-P system. The Gibbs energy of liquid solution was determined with very few parameters by adopting the Toop-type interpolation technique. Besides, the thermodynamic properties and phase equilibria of the Fe-Al-P system have

**Table 5** Invariant reactions of
the Fe-Al-P system with
experimental data⁵⁸⁾

<table>
  <thead>
    <tr>
      <th>Code</th>
      <th>Invariant reactions</th>
      <th>x<sub>Fe</sub></th>
      <th>x<sub>Al</sub></th>
      <th>x<sub>P</sub></th>
      <th>T, °C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>U1</td>
      <td>L + Me₃P = Me₂P + BCC_A2</td>
      <td>0.720</td>
      <td>0.089</td>
      <td>0.191</td>
      <td>1035</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.677</td>
      <td>0.140</td>
      <td>0.183</td>
      <td>1020⁵⁸⁾</td>
    </tr>
    <tr>
      <td>E1</td>
      <td>L = AlP + Me₂P + BCC_B2</td>
      <td>0.547</td>
      <td>0.264</td>
      <td>0.189</td>
      <td>989</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.556</td>
      <td>0.275</td>
      <td>0.169</td>
      <td>995⁵⁸⁾</td>
    </tr>
    <tr>
      <td>E2</td>
      <td>L = FeP + Me₂P + AlP</td>
      <td>0.546</td>
      <td>0.061</td>
      <td>0.393</td>
      <td>1208</td>
    </tr>
    <tr>
      <td>U2</td>
      <td>L + FeP = FeP₂ + AlP</td>
      <td>0.297</td>
      <td>0.028</td>
      <td>0.675</td>
      <td>1170</td>
    </tr>
    <tr>
      <td>U3</td>
      <td>L + Fe₂Al₅ = Al₈Fe₅ + Fe₂Al</td>
      <td>0.322</td>
      <td>0.668</td>
      <td>0.01</td>
      <td>1142</td>
    </tr>
    <tr>
      <td>U4</td>
      <td>L + Fe₂Al₅ = Al₁₃Fe₄ + AlP</td>
      <td>0.253</td>
      <td>0.737</td>
      <td>0.01</td>
      <td>1139</td>
    </tr>
    <tr>
      <td>U5</td>
      <td>L + Fe₂Al₅ = Fe₂Al + AlP</td>
      <td>0.331</td>
      <td>0.646</td>
      <td>0.023</td>
      <td>1130</td>
    </tr>
    <tr>
      <td>U6</td>
      <td>L + Fe₂Al = Al₈Fe₅ + AlP</td>
      <td>0.372</td>
      <td>0.591</td>
      <td>0.037</td>
      <td>1118</td>
    </tr>
    <tr>
      <td>U7</td>
      <td>L + Al₈Fe₅ = BCC_B2 + AlP</td>
      <td>0.412</td>
      <td>0.531</td>
      <td>0.057</td>
      <td>1099</td>
    </tr>
    <tr>
      <td>U8</td>
      <td>L + BCC_A2 = Me₂P + BCC_B2</td>
      <td>0.653</td>
      <td>0.162</td>
      <td>0.185</td>
      <td>1030</td>
    </tr>
    <tr>
      <td>U9</td>
      <td>L + Al = Al₁₃Fe₄ + AlP</td>
      <td>0.008</td>
      <td>0.992</td>
      <td>0</td>
      <td>1099</td>
    </tr>
  </tbody>
</table>

**Fig. 9** Effect of Al on the
activity coefficient of P in the
liquid Fe-Al-P solution at 1400
and 1600 °C, compared with
experimental data⁶¹⁻⁶³⁾

![](./images/812590248524513280_23.jpg)

been accurately and consistently reproduced, compared to
available experimental data. The thermodynamic database
of the Fe-Al-P system developed in the present study will
be used as part of new FSstel database in FactSage 8.0
version.

Acknowledgment We would like to gratefully acknowledge the
Steelmaking Consortium Members, Hyundai Steel, Tata Steel Europe,
Posco, Doosan Heavy Industry and Construction, SeAh Besteel,
Nucor Steel, RioTinto, JFE Steel, Nippon Steel, RHI, Voestalpine,
and Natural Science and Engineering Research Council of Canada for
supporting the present project. This work was also supported by the
National Research Foundation of Korea (NRF) grant funded by the
Korean government (MSIT) (No. NRF-2020R1A5A6017701). We
would also like to thank the McGill Engineering Doctorate Award
(MEDA) program.

### References

1. W.M. Huang, The Phase Relations of the Fe-Al-P Ternary Sys-
tem and the Galvannealed Process of Zn-Coating, Master Dis-
sertation, Xiangtan University, China, 2011

2. P.D. Mercer, Factors Which Affect the Alloy Growth Rate in
Galvannealed Coatings. In *Galvatech'92: 2nd International
Conference on Zinc and Zinc Alloy Coated Steel Sheet*, Centre de
Recherches Metallurgiques (CRM), Sept. 8–10, 1992 (Amster-
dam), p 204–208

3. Y. Singh, S.C. Joshi, V. Satyawali, and A. Gupta, Acute Alu-
minium Phosphide Poisoning, What is New? *Egypt. J. Intern.
Med.*, 2014, **26**(3), p 99-103

4. S.W. Fan, L. Yang, and G.Y. Gao, The Electronic Structures and
Properties for Carbon Doped Aluminum Phosphide, *Phys. Lett. A*,
2019, **383**(25), p 3138-3142

5. M. Sharon and G. Tamizhmani, Transition Metal Phosphide
Semiconductors for Their Possible Use in Photoelectrochemical

![](./images/812590248524513280_24.jpg)

Cells and Solar Chargeable Battery (Saur Viddyut Kosh V, J. Mater. Sci., 1986, 21(6), p 2193-2201

6. H. Okamoto, The Fe-P (Iron-Phosphorus) System, Bull. Alloy Phase Dia., 1990, 11(4), p 404-412

7. M.E. Schlesinger, The Thermodynamic Properties of Phosphorus and Solid Binary Phosphides, Chem. Rev., 2002, 102(11), p 4267-4302

8. A.J. McAlister, The Al-P (Aluminum-Phosphorus) System, Bull. Alloy Phase Dia., 1985, 6(3), p 222-224

9. H. Okamoto, Supplemental Literature Review of Binary Phase Diagrams: Al-P, B-Ga, B-Nd, Ba-Ga, Bi-Cs, Ca-Ga, Cd-Gd, Cr-Mo, Gd-Ni, Ni-Pb, Ni-Sc, and Sc-Sn, J. Phase Equilib. Diffus., 2015, 36(5), p 518-530

10. V. Raghavan, The Al-Fe-P (Aluminium-Iron-Phosphorus) Sys-tem, Phase Diagr. Ternary Iron Alloys, 1988, 3, p 9-16

11. V. Raghavan, The Al-Fe-P (Aluminium-Iron-Phosphorus) Sys-tem, J. Alloy Phase Dia., 1989, 5(1), p 32-39

12. V. Raghavan, Phase Diagram Updates and Evaluations of the Al-Fe-P, B-Fe-U, Bi-Fe-Zn, Cu-Fe-Zn, Fe-Si-Zn and Fe-Ti-V Sys-tems, J. Phase Equilib. Diffus., 2013, 34(3), p 230-243

13. R. Schmid-Fetzer and V. Tomashik, Aluminium-Iron-Phosphorus, Iron Systems, Part 1, Springer, Berlin, 2008, p 172-183

14. P. Gustafson, Internal Report IM-2549, Swedish Institue for Metals Research, Stockholm, 1990

15. J.H. Shim, C.S. Oh, and D.N. Lee, Thermodynamic Properties and Calculation of Phase Diagram of the Fe-P System, J. Korean. Inst. Met. Mater., 1996, 34(11), p 1385-1393

16. H. Ohtani, N. Hanaya, M. Hasebe, S.I. Teraoka, and M. Abe, Thermodynamic Analysis of the Fe-Ti-P Ternary System by Incorporating First-principles Calculations into the CALPHAD Approach, CALPHAD, 2006, 30(2), p 147-158

17. Z.M. Cao, K.P. Wang, Z.Y. Qiao, and G.W. Du, Thermodynamic Reoptimization of the Fe-P System, Acta Phys. Chim. Sin., 2012, 28(1), p 37-43

18. Z.M. Cao, W. Xie, K.P. Wang, C.J. Niu, G.W. Du, and Z.Y. Qiao, Thermodynamic Optimization of the Al-Fe-P Ternary System, Acta Phys. Chim. Sin., 2013, 29(10), p 2148-2156

19. Z.M. You and I.H. Jung, Critical Evaluation and Optimization of the Fe-P System, Metall. Mater. Trans. B, 2020. (revised versionin reviewing)

20. I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida, and T.G. Chart, A Binary Database for III-V Compound Semiconductor Systems, CALPHAD, 1994, 18(2), p 177-222

21. H. Tu, F. Yin, X. Su, Y. Liu, and X. Wang, Experimental Investigation and Thermodynamic Modeling of the Al-P-Zn Ternary System, CALPHAD, 2009, 33(4), p 755-760

22. C. Wu, W. Huang, X. Su, H. Peng, J. Wang, and Y. Liu, Experimental Investigation and Thermodynamic Calculation of the Al-Fe-P System at Low Phosphorus Contents, CALPHAD,2012, 38, p 1-6

23. S.M. Liang and R. Schmid-Fetzer, Thermodynamic Assessment of the Al-P System Based on Original Experimental Data,CALPHAD, 2013, 42, p 76-85

24. S.M. Liang and R. Schmid-Fetzer, Corrigendum to "Thermody-namic Assessment of the Al-P System Based on Original Experimental Data" [CALPHAD 42 (2013) 76-85], CALPHAD,2014, 100(45), p 251-253

25. J. Miettinen, S. Louhenkilpi, and G. Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems Part 9: Fe-Al-P, J. Phase Equilib. Diffus., 2015, 36(4), p 317-326

26. D. Pelton, S.A. Degterov, G. Eriksson, C. Robelin, and Y. Des-sureault, The Modified Quasichemical Model I-Binary Solutions,Metall. Mater. Trans. B, 2000, 31(4), p 651-659

27. D. Pelton and P. Chartrand, The Modified Quasi-chemical Model:Part II. Multicomponent Solutions, Metall. Mater. Trans. A, 2001,32(6), p 1355-1360

28. M. Hillert, The Compound Energy Formalism, J. Alloys Comp.,2001, 320(2), p 161-176

29. B. Sundman, I. Ohnuma, N. Dupin, U.R. Kattner, and S.G. Fries,An Assessment of the Entire Al-Fe System Including D03Ordering, Acta Mater., 2009, 57(10), p 2896-2908

30. A.T. Phan, M.K. Paek, and Y.B. Kang, Phase Equilibria and Thermodynamics of the Fe-Al-C System: Critical Evaluation,Experiment and Thermodynamic Optimization, Acta Mater.,2014, 79, p 1-15

31. A.T. Phan, M.K. Paek, and Y.B. Kang, Corrigendum to "Phase Equilibria and Thermodynamics of the FeAlC System: Critical Evaluation, Experiment and Thermodynamic Optimization"[Acta Mater. 79 (2014) 1-15], Acta Mater., 2016, 100(115),p 476-477

32. W. Bale, P. Chartrand, S.A. Degterov, G. Eriksson, K. Hack, R.B.Mahfoud, and S. Petersen, FactSage Thermochemical Software and Databases, CALPHAD, 2002, 26(2), p 189-228

33. T. Dinsdale, SGTE Data for Pure Elements, CALPHAD, 1991,15(4), p 317-425

34. P. Vonka Leitner, D. Sedmidubsky, and P. Svoboda, Application of Neumann-Kopp Rule for the Estimation of Heat Capacity of Mixed Oxides, Thermoch Acta, 2010, 497(12), p 7-13

35. G. Inden, Project Meeting CALPHAD V, Max-Planck-InstEisenforschung, GmbH, Dusseldorf, 1976, p 111

36. M. Hillert and M. Jarl, A Model for Alloying in Ferromagnetic Metals, CALPHAD, 1978, 2(3), p 227-238

37. W. Huang, An Assessment of the Fe-Mn System, CALPHAD,1989, 13(3), p 243-252

38. W.E. White and A.H. Bushey, Aluminum Phosphide-Preparation and Composition, J. Am. Chem. Soc., 1944, 66(10), p 1666-1672

39. B. Panish and M. Ilegems, Phase Equilibria in Ternary III-V Systems, Prog. Solid State Chem., 1972, 7, p 39-83

40. M. Ilegems and M.B. Panish, Phase Diagram of the System Al-Ga-P, J. Cryst. Growth, 1973, 20(2), p 77-81

41. M. Ilegems and M.B. Panish, Phase Equilibria in III-V Quater-nary Systems-Application to Al-Ga-P-As, J. Phys. Chem. Solids,1974, 35(3), p 409-420

42. V.M. Goldschmidt, Geochemical Distribution Laws of the Ele-ments. VIII. Researches on the Structure and Properties of Crystals, Skr. Akad. Oslo, 1927, 1926(8), p 7-156

43. C. Wang, M. Zaheeruddin, and L.H. Spinar, Preparation and Properties of Aluminum Phosphide, J. Inorg. Nuclear Chem.,1963, 25(3), p 326-327

44. W. Kischio, Formation Enthalpy of Aluminum Phosphide, J.Inorg. Nuclear Chem., 1965, 27(3), p 750-751

45. M.B. Panish, R.T. Lynch, and S. Sumski, Phase and Thermody-namic Properties of the Ga-Al-P System-Solution Epitaxy of Gaxal 1-Xp and AIP AND, Trans. Met. Soc. AIME, 1969, 245(3),p 559-563

46. S.Z. Beer, The Solution of Aluminum Phosphide in Aluminum, J.Electrochem. Soc., 1969, 116(2), p 263-265

47. H. Lescuyer, M. Allibert, and G. Laslaz, Solubility and Precipi-tation of AIP in Al-Si Melts Studied with a Temperature Con-trolled Filtration Technique, J. Alloys Compd, 1998, 279(2),p 237-244

48. R.H. Cox and M.J. Pool, Heat Contents and Heats of Fusion of III-V Compounds, J. Chem. Eng. Data, 1967, 12(2), p 247-248

49. S. Seviak and A. Sandulova, Thermodynamic Characteristics of Aluminum Phosphide, Izv. Akad. Nauk SSSR Neorg. Mater.,1974, 10, p 146-147

50. K. Itagaki and K. Yamaguchi, High Temperature Heat Contents of III-V Semiconductor Systems, Thermochim. Acta, 1990, 163,p 1-12

51. S. Martosudirdjo and J.N. Pratt, Calorimetric Studies of the Heats of Formation of IIIB-VB Adamantine Phases, Thermochim. Acta,1974, 10(1), p 23-31

![](./images/812590248524513280_25.jpg)

52. K.A. Sharifov, Calculation of Entropy of Solids, *Russ. J. Phys. Chem. USSR*, 1990, **40**(1), p 113

53. M.K. Karapetyants and M.L. Karapetyants, Tables of Some Thermodynamic Properties of Various Substances, *Khim. Tekh. Inst. Moscow*, 1961, **34**, p 166

54. L.I. Marina, A.Y. Nashel’skii, and B.A. Sakharov, Heats of Atomization and Some Thermochemical Constants of A III B V Compounds. Chem. Bonds in Solids, Springer, Boston, MA, 1972, p 124-129

55. G.F. Voronin, Estimation of the Standard Entropies of Chemical Compounds, *Zhur Fiz Khim*, 1970, **44**(12), p 3013-3017

56. O. Kubaschewski and C.B. Alcock, *Metallurgical Thermochemistry*, 5th ed., Pergamon Press, Elmsford, 1979, p 360

57. G.D. Maria, K.A. Gingerich, and V. Piacente, Vaporization of Aluminum Phosphide, *J. Chem. Phys.*, 1968, **49**(10), p 4705-4710

58. R. Vogel, The Diagram of State Iron-Iron Phosphide-Aluminum Phosphide-Aluminum, *Arch. Eisenhuetten.*, 1952, **23**, p 287-291

59. H. Kaneko, T. Nishizawa, K. Tamaki, and A. Tanifuji, Solubility of Phosphorus in $\alpha$ and $\gamma$-Iron, *Nippon Kinzoku Gakkai-Si*, 1965, **29**, p 166-170

60. H. Kaneko, Phosphide-Phases in Ternary Alloys of Iron, Phosphorus and Other Elements, *J. Jpn. Inst. Met.*, 1965, **29**, p 159-165

61. K. Yamada and E. Kato, Mass Spectrometric Determination of Activities of Phosphorus in Liquid Fe-P-Si, Al, Ti, V, Cr, Co, Ni, Nb, and Mo Alloys, *Tetsu-to-Hagané*, 1979, **65**(2), p 273-280

62. K. Yamada and E. Kato, Effect of Dilute Concentrations of Si, Al, Ti, V, Cr Co, Ni, Nb and Mo on the Activity Coefficient of P in Liquid Iron, *Trans. Iron Steel Ins. Jpn.*, 1983, **23**(1), p 51-55

63. S. Ban-ya, N. Maruyama, and S. Fujino, The Effects of C, Si, Al, and B on the Activity of Phosphorus in Liquid Iron, *Tetsu-to-Hagané*, 1983, **69**(8), p 921-928

Publisher's Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812590248524513280_26.jpg)