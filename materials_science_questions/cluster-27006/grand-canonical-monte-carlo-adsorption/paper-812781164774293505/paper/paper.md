# Dehydration Pathways of Gypsum and the Rehydration Mechanism of Soluble Anhydrite $\gamma$-CaSO$_4$

Yongbo Tang, $^{\dagger}$ Jianming Gao, $^{*, \dagger, \ddagger}$ Chuanbei Liu, $^{\dagger}$ Xuemei Chen, $^{\dagger}$ and Yasong Zhao $^{\dagger}$

$^{\dagger}$School of Materials Science and Engineering, Southeast University, Nanjing 211189, China
$^{\ddagger}$JiangSu Key Laboratory of Construction Materials, Nanjing 211189, China

S Supporting Information

## ABSTRACT:
The dehydration products of gypsum under different temperature and water vapor pressure were investigated by thermodynamic theory. Additionally, the rehydration mechanism of soluble anhydrite was also studied by Monte Carlo (MC) simulations. The thermodynamic calculation results reveal that the dehydration mechanism of gypsum significantly depended on ambient temperature and water vapor pressure. In the high-temperature and low water vapor pressure region, gypsum dehydrates to form $\gamma$-CaSO$_4$ in a single-step process ($\text{CaSO}_4{\cdot}2\text{H}_2\text{O} \rightarrow \gamma\text{-CaSO}_4$); with increasing water vapor pressure, gypsum undergoes the $\text{CaSO}_4{\cdot}2\text{H}_2\text{O} \rightarrow \gamma\text{-CaSO}_4 \rightarrow \beta\text{-CaSO}_4{\cdot}0.5\text{H}_2\text{O}$ reaction path and as water vapor pressure increases further, the occurrence of a two-step conversion path $\text{CaSO}_4{\cdot}2\text{H}_2\text{O} \rightarrow \beta\text{-CaSO}_4{\cdot}0.5\text{H}_2\text{O} \rightarrow \gamma\text{-CaSO}_4$ was observed. It was also found that gypsum is stable in the low-temperature and high water vapor pressure region and does not dehydrate to form any calcium sulfate hemihydrate. Finally, the rehydration mechanism of soluble anhydrite was studied by MC simulations. The simulation results are in agreement with the experimental data and support the finding that $\gamma$-CaSO$_4$ rehydration forms $\text{CaSO}_4{\cdot}0.67\text{H}_2\text{O}$ in high relative humidity. Another important result revealed by the MC simulation is that $\gamma$-CaSO$_4$ has an extraordinary ability to capture water molecules from an extremely dry atmosphere, which is very useful in some fields, such as in drying processes and even for extracting liquid water from extremely dry atmosphere.

![](./images/812781164774293505_1.jpg)

## INTRODUCTION
Gypsum is one of the most important minerals on earth, and its dehydration product, plaster of paris, is mainly used as a building material. Furthermore, there are abundant deposits of gypsum mineral in nature; moreover, recent studies have indicated that Mars also has an abundance of gypsum mineral as well as other mineral calcium sulfate phases ($\beta\text{-CaSO}_4{\cdot}0.5\text{H}_2\text{O}$). $^{1-6}$ Furthermore, both the phosphate industry and thermal power plants generate large amounts of byproduct gypsum (phospho- gypsum, flue gas desulfurization gypsum, etc.). Extensive efforts have been made to studying the process of gypsum dehydration. However, the dehydration mechanisms of gypsum that have been reported in previous studies still remain confusing and even contradictory. Some researchers have argued that gypsum undergoes a two-stage dehydration process, where $\beta\text{-CaSO}_4{\cdot}0.5\text{H}_2\text{O}$ is formed first and then $\gamma$-CaSO$_4$ is obtained by further dehydration of $\beta\text{-CaSO}_4{\cdot}0.5\text{H}_2\text{O}.^{7-10}$ McAdie $^{11}$ studied the gypsum dehydration process at $124.3\ ^\circ\text{C}$ under different water vapor partial pressures. Their experimental results reveal that gypsum dehydration proceeds through only a single $\text{CaSO}_4{\cdot}2\text{H}_2\text{O} \rightarrow \gamma\text{-CaSO}_4$ step when the ambient water vapor pressure is less than 26664 Pa; however, a two-step process of $\text{CaSO}_4{\cdot}2\text{H}_2\text{O} \rightarrow \beta\text{-CaSO}_4{\cdot}0.5\text{H}_2\text{O} \rightarrow \gamma\text{-CaSO}_4$ is observed if the practical water vapor pressure is greater than 40 130 Pa. Badens et al. $^{12}$ investigated the dehydration process of gypsum using a combination of controlled transformation rate thermal analysis and Laue diffraction, concluding that there is only one dehydration step from gypsum to $\gamma$-CaSO$_4$ at 500 Pa or below; whereas $\beta\text{-CaSO}_4{\cdot}0.5\text{H}_2\text{O}$ is an intermediate product when the practical water vapor pressure reaches 900 Pa. Ball and Norwood $^{13}$ have argued that $\gamma$-CaSO$_4$ is directly obtained during gypsum dehydration at a water vapor partial pressure range of $1.33 \times 10^{-2}$ to 6000 Pa and at a temperature below 115 $^\circ\text{C}$. Lou et al. $^{14}$ studied the dehydration mechanisms of flue gas desulfurization gypsums and pointed out that gypsum dehydration proceeds through a one-step process at a negligible partial water vapor pressure and below $100\ ^\circ\text{C}$, while two-step processes are observed at an autogenous water vapor pressure and a temperature of approximately $100\ ^\circ\text{C}$. Abriel et al. $^{15}$ studied the dehydration mechanism of gypsum using neutron and X-ray diffraction (XRD) and proposed a novel gypsum dehydration pathway of $\text{CaSO}_4{\cdot}2\text{H}_2\text{O} \rightarrow \text{CaSO}_4{\cdot}0.75\text{H}_2\text{O} \rightarrow \gamma\text{-CaSO}_4$. Prasad et al. $^{16}$ and Carbone et al. $^{17}$ investigated the dehydration mechanism of gypsum using in situ micro-Raman

Received: December 12, 2018
Accepted: April 16, 2019
Published: April 26, 2019

and energy-dispersive XRD, respectively, and concluded that $\gamma$-
CaSO₄ was first obtained in the gypsum dehydration process,
and then the formed $\gamma$-CaSO₄ was transformed into $\beta$-CaSO₄·
0.5H₂O by a rehydration reaction in which 0.5H₂O water
molecules reentered into the crystal structure of $\gamma$-CaSO₄.

To date, much effort has been made to researching the
dehydration pathways of gypsum; however, it is still not well
understood. In this study, a theoretical thermodynamics
approach was employed to elucidate the dehydration pathways
of gypsum.

## THEORETICAL AND SIMULATION METHODS
**Monte Carlo Simulations.** The number of sorbates is
allowed to vary in the grand canonical ensemble ($\mu VT$). In view
of this, adsorption isotherms were calculated using grand
canonical Monte Carlo (GCMC) simulations with the
Metropolis algorithm.¹⁸ The GCMC simulations were carried
out using periodic boundary conditions of $3 \times 3 \times 3$ unit cells of
$\gamma$-CaSO₄.

The water molecules used in the simulation calculations are
rigid molecules. The force field plays a key role in MC
simulations. In this work, the DREIDING force field¹⁹ was
employed to model all interactions between water molecules
and the $\gamma$-CaSO₄ lattice. The theoretical formulae of the
nonbonded interactions in the DREIDING force field are
represented by the 12-6 LJ potential and Coulombic terms

$$
\sum_{i j} 4 \varepsilon_{i j}\left[\left(\frac{r_{i j}^{\mathrm{o}}}{r_{i j}}\right)^{12}-\left(\frac{r_{i j}^{\mathrm{o}}}{r_{i j}}\right)^{6}\right]+\frac{q_{i} q_{j}}{4 \pi \varepsilon_{\mathrm{o}} r_{i j}}
\tag{1}
$$

$$
r_{i j}^{\mathrm{o}}=\left[\frac{\left(r_{i}^{\mathrm{o}}\right)^{6}+\left(r_{j}^{\mathrm{o}}\right)^{6}}{2}\right]^{1 / 6}
\tag{2}
$$

$$
\varepsilon_{i j}=2 \sqrt{\varepsilon_{i} \cdot \varepsilon_{j}}\left[\frac{\left(r_{i}^{\mathrm{o}}\right)^{3} \cdot\left(r_{j}^{\mathrm{o}}\right)^{3}}{\left(r_{i}^{\mathrm{o}}\right)^{6} \cdot\left(r_{j}^{\mathrm{o}}\right)^{6}}\right]
\tag{3}
$$

where $r_{ij}$ and $\sigma_{ij}$ are the actual and reference distances between
atoms $i$ and $j$, respectively; $\varepsilon_{\mathrm{o}}$ is the permittivity of free space ($\varepsilon_{\mathrm{o}}$
$= 8.8543 \times 10^{-12} \mathrm{C}^{2} \mathrm{~J}^{-1} \mathrm{~m}^{-1}$); $\varepsilon_{ij}$ is the potential well-depth; and
$q_{i}$ and $q_{j}$ are the value of the charge on atoms $i$ and $j$. The LJ
interactions between unlike atoms are treated with the sixth-
order mixing rule.²⁰

The atom-based summation method with a cutoff distance of
0.15 nm was employed to compute both the Coulombic
interactions and the van der Waals interactions between the
water molecules, the calcium sulfate framework, and the
hydrogen bond terms in the system (spline width: 0.1 nm;
buffer width: 0.05 nm). The MC simulations were performed at
215 and 298 K. The coupling to the heating bath was carried out
using a Nose thermostat.

**Thermodynamic Data for CaSO₄·2H₂O, $\boldsymbol{\beta}$-CaSO₄·
0.5H₂O, and H₂O(g).** Thermodynamics is a rigorous theory
and is widely used in chemistry, materials science, metallurgy,
and other fields. The large number of thermodynamic
calculations used in this work is very helpful for determining
the gypsum dehydration pathways.

The standard Gibbs energy of formation values of CaSO₄·
2H₂O, $\beta$-CaSO₄·0.5H₂O, $\gamma$-CaSO₄, and H₂O(g) can be
obtained from the literature;²¹,²² these thermodynamic data
are crucial for calculating the phase equilibrium of the CaSO₄−
H₂O system. Thermodynamic data are generally tabulated in the
literature at the interval of 100 K, which is inconvenient for
thermodynamic calculations. Therefore, it was necessary to fit
the values of the standard Gibbs energy of formation of CaSO₄·
2H₂O, $\beta$-CaSO₄·0.5H₂O, and H₂O(g) using polynomial
functions of the temperature; the numerical calculations were
performed by MATLAB, $T$ represents the numerical value of
Kelvin temperature, and it was found that the results could be
represented by the following equations

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}\left(\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}\right) \\
& \quad=\Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\gamma-\mathrm{CaSO}_{4}\right)+2 \Delta_{\mathrm{f}} G_{\mathrm{m}}\left(\mathrm{H}_{2} \mathrm{O}\right)+2 R T \\
& \quad \ln \left(P_{\mathrm{H}_{2} \mathrm{O}} / P^{\mathrm{o}}\right)
\end{aligned}
\tag{4}
$$

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{CaSO}_{4}\right) / \mathrm{kJ} \cdot \mathrm{mol}^{-1} \\
& \quad=-1414+0.3228 T+1.1620 \times 10^{-4} T^{2} \\
& \quad \quad-7.0810 \times 10^{-8} T^{3}
\end{aligned}
\tag{5}
$$

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\beta-\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}\right) / \mathrm{kJ} \cdot \mathrm{mol}^{-1} \\
& \quad=-1566+0.44029 T+1.4600 \times 10^{-4} T^{2} \\
& \quad \quad-1.0480 \times 10^{-7} T^{3}
\end{aligned}
\tag{6}
$$

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{H}_{2} \mathrm{O}\right) / \mathrm{kJ} \cdot \mathrm{mol}^{-1} \\
& \quad=-241.1+0.03874 T-1.0580 \times 10^{-5} T^{2}
\end{aligned}
\tag{7}
$$

**Correction of the Gibbs Free Energy of Formation of $\boldsymbol{\gamma}$-
CaSO₄.** The water molecules in the air can easily enter into the
$\gamma$-CaSO₄ lattice because of its honeycomb structure. Because of
this, pure $\gamma$-CaSO₄ without a trace of crystal water is difficult to
obtain. Therefore, the value of the Gibbs free energy of
formation of $\gamma$-CaSO₄ tabulated in the literature is not
sufficiently accurate. To obtain exact thermodynamic data, it is
necessary to make a correction for the Gibbs free energy of
formation of $\gamma$-CaSO₄. Kevin²³ studied the effect of relative
humidity on the number of combined water molecules in the
calcium sulfate subhydrate unit cell at a temperature of 298 K,
and the experimental result indicates that the total number of
combined water is strictly equal to 0.5 when the relative
humidity is maintained at 0.1%. Additionally, CaSO₄·2H₂O
began to dehydrate when it was heated to 459 K under a water
vapor partial pressure of 1 atm. On the basis of these
experimental results, the numerical values of the Gibbs free
energy of formation of $\gamma$-CaSO₄ at 298 and 459 K can be
calculated using eq 9, obtaining $-1311.74$ and $-1250.19$ kJ·
mol⁻¹, respectively.

The process of $\gamma$-CaSO₄ transformation into $\beta$-CaSO₄·
0.5H₂O by absorbing the water vapor in the air can be expressed
by the following reaction

$$
\gamma-\mathrm{CaSO}_{4}+0.5 \mathrm{H}_{2} \mathrm{O}(\mathrm{g})=\beta-\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}
\tag{8}
$$

To calculate the standard Gibbs energy of formation of $\gamma$-
CaSO₄, we write

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\gamma-\mathrm{CaSO}_{4}\right)=\Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\beta-\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}\right) \\
& \quad-0.5 \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{H}_{2} \mathrm{O}\right)-0.5 R T \ln \left(P_{\mathrm{H}_{2} \mathrm{O}} / P^{\mathrm{o}}\right)
\end{aligned}
\tag{9}
$$

To obtain the accurate expression of the Gibbs free energy of
formation of $\gamma$-CaSO₄ at the temperature of interest, eq 5 can be
transformed into the following form

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\gamma-\mathrm{CaSO}_{4}\right) / \mathrm{kJ} \cdot \mathrm{mol}^{-1} \\
& \quad=a+b T+1.1620 \times 10^{-4} T^{2}-7.0810 \times 10^{-8} T^{3}
\end{aligned}
$$

where the symbol $a$ and the symbol $b$ in eq 10 are the two undetermined parameters. By substituting the values of the standard Gibbs energy of formation of $\gamma-\mathrm{CaSO}_{4}$ at 298 and 459 $\mathrm{K}$ for parameters $a$ and $b$ successively, a matrix equation was derived.

$$
\left(\begin{array}{ll}
1 & 198 \\
1 & 459
\end{array}\right)\left(\begin{array}{l}
a \\
b
\end{array}\right)=\left(\begin{array}{l}
-1310.29 \\
-1267.82
\end{array}\right)
$$

The numerical values of parameters $a$ and $b$ were obtained by solving the above matrix equation, and the calculation reads

$$
a=-1417.12, \quad b=0.3253
$$

By inserting the numerical values of $a$ and $b$ into eq 10, the accurate expression for the Gibbs free energy of formation of $\gamma$ $\mathrm{CaSO}_{4}$ was rewritten as follows

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\gamma-\mathrm{CaSO}_{4}\right) / \mathrm{kJ} \cdot \mathrm{mol}^{-1}=-1417+0.3253 T \\
& \quad+1.1620 \times 10^{-4} T^{2}-7.0810 \times 10^{-8} T^{3}
\end{aligned}
$$

### Gibbs Free Energy of Formation of $\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}$.
The framework of $\gamma-\mathrm{CaSO}_{4}$ has a honeycomb structure; $^{24}$ therefore, $\gamma-\mathrm{CaSO}_{4}$ quite easily rehydrates to form calcium sulfate subhydrate $\left(\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}\right)$

$$
\mathrm{CaSO}_{4}+n \mathrm{H}_{2} \mathrm{O}=\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}
$$

Karni argued that the number of combined water in $\mathrm{CaSO}_{4}$. $n \mathrm{H}_{2} \mathrm{O}$ can range from 0 to $0.67 .^{25}$

The Gibbs free energies of $\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}, \beta-\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}$, and $\gamma-\mathrm{CaSO}_{4}$ at different temperatures can be calculated using eqs 4,6 and 13, and the calculation results are tabulated in Table 1.

The standard molar Gibbs free energy of formation of $\mathrm{CaSO}_{4}$. $n \mathrm{H}_{2} \mathrm{O}$ is not available in literature studies. Valero $^{26}$ proposed an approximation method and provided a mathematic expression to calculate the thermodynamic properties of the hydrated substance, as in eq 15.

$$
\Delta G_{\mathrm{f}, \mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}}^{o}=\Delta G_{\mathrm{f}, \mathrm{CaSO}_{4}}^{o}+n \Delta G_{\mathrm{f}, \mathrm{H}_{2} \mathrm{O}}^{o}+\Delta G_{\mathrm{hydr}, \mathrm{A}}^{o} \quad(15)
$$

where $\Delta G_{\mathrm{f}, \mathrm{CaSO}_{4}}^{o}$ and $\Delta G_{\mathrm{f}, \mathrm{H}_{2} \mathrm{O}}^{o}$ are the standard molar Gibbs free energies of formation of $\gamma-\mathrm{CaSO}_{4}$ and $\mathrm{H}_{2} \mathrm{O}$, respectively; $\Delta G_{\text {hydr,A }}^{o}$ is the standard molar hydration Gibbs free energy of $\mathrm{CaSO}_{4}$; and $n$ is the total number of the water molecules in the $\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}$ phase.

Table 1. Standard Molar Gibbs Free Energy of Formation of $\gamma-\mathrm{CaSO}_{4}, \beta-\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}$, and $\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}$ at Temperatures Ranging from 300 to $400 \mathrm{~K}$; Herein $T$ Is the Unit of Kelvin Temperature

| $T(\mathrm{~K})$ | the standard molar Gibbs free energy of formation $\left(\mathrm{kJ} \cdot \mathrm{mol}^{-1}\right)$ |  |  |
| :---: | :---: | :---: | :---: |
|  | $\mathrm{CaSO}_{4}(\gamma)$ | $\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}(\beta)$ | $\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}$ |
| 300 | $-1310.98$ | $-1435.10$ | $-1795.72$ |
| 320 | $-1303.45$ | $-1425.77$ | $-1780.59$ |
| 340 | $-1295.87$ | $-1416.44$ | $-1765.45$ |
| 360 | $-1288.26$ | $-1407.12$ | $-1750.32$ |
| 380 | $-1280.61$ | $-1397.80$ | $-1735.19$ |
| 400 | $-1272.94$ | $-1388.42$ | $-1720.01$ |
| 420 | $-1265.24$ | $-1379.02$ | $-1704.80$ |
| 440 | $-1257.52$ | $-1369.63$ | $-1689.60$ |
| 460 | $-1249.79$ | $-1360.25$ | $-1674.42$ |
| 480 | $-1242.03$ | $-1350.87$ | $-1659.25$ |
| 500 | $-1234.27$ | $-1341.51$ | $-1644.10$ |
| 520 | $-1226.50$ | $-1332.18$ | $-1628.98$ |
| 540 | $-1218.72$ | $-1322.86$ | $-1613.89$ |
| 560 | $-1210.95$ | $-1313.58$ | $-1598.83$ |
| 580 | $-1203.17$ | $-1304.32$ | $-1583.81$ |
| 600 | $-1195.40$ | $-1295.09$ | $-1568.82$ |

While the above formula is accurate and its associated deviation rarely exceeds $\pm 2 \%$, it still does not meet the requirements for the exact thermodynamic calculation in this work. Expression (15) is only a first-order linear function of the independent variable $n$, and consequently, its precision is limited. The values presented in Table 1 indicate that the standard molar Gibbs free energy of formation of the $\mathrm{CaSO}_{4}$. $n \mathrm{H}_{2} \mathrm{O}$ phase depends on the two independent variables, namely, the temperature $(\mathrm{K})$ and total water content $(n)$. This implies that nonlinear multiple regression is suitable for evaluating the standard molar hydration Gibbs free energy of the $\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}$ phase. Therefore, the following polynomial for the $\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}$ phase was employed (Figure 1)

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}\right) / \mathrm{kJ} \cdot \mathrm{mol}^{-1} \\
& \quad=a+b T+c T^{2}+d n+e n^{2}+f T n+g T^{2} n^{2}+h T^{3} n^{3}
\end{aligned}
$$

![](./images/812781164774293505_2.jpg)

Figure 1. Standard Gibbs energy of formation of $\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}$ as a function of temperature $(T)$ and combined water content $(n)$.

where $a, b, c, d, e, f$, and $g$ are all underdetermined parameters. MATLAB was used to fit the nonlinear function, given by eq 16 , to the data presented in Table 1, and the calculation results indicate that the values of coefficients $a, b, c, d, e, f$, and $n$ are $-1426.73,3.8422 \times 10^{-1}, 1.6603 \times 10^{-6},-292.72,2.1002 \times$ $10^{-1}, 1.4389 \times 10^{-1}, 5.0550 \times 10^{-5}$, and $-1.9774 \times 10^{-8}$, respectively. Inserting these values into eq 16 yields

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}\right) / \mathrm{kJ} \cdot \mathrm{mol}^{-1} \\
& =-1426.73+3.8422 \times 10^{-1} T+1.6603 \times 10^{-6} T^{2} \\
& \quad-292.72 n+2.1002 \times 10^{-1} n^{2}+1.4389 \times 10^{-1} T n \\
& \quad+5.0550 \times 10^{-5} T^{2} n^{2}-1.9774 \times 10^{-8} T^{3} n^{3}
\end{aligned}
$$

## RESULTS AND DISCUSSION

Thermodynamic Analysis of the Pathway of Gypsum Dehydration. Each of the below three chemical reactions may be spontaneous when gypsum is heated in ambient condition. However, the question of which dehydration reaction of gypsum will occur in practice requires further analysis of the thermodynamic calculations and the experimental results.

$$\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}=\beta-\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}+1.5 \mathrm{H}_{2} \mathrm{O}(\mathrm{g})\qquad(18)$$

$$\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}=\gamma-\mathrm{CaSO}_{4}+2 \mathrm{H}_{2} \mathrm{O}(\mathrm{g})\qquad(19)$$

$$\beta \text {-CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}=\gamma \text {-CaSO}_{4}+0.5 \mathrm{H}_{2} \mathrm{O}(\mathrm{g})\qquad(20)$$

The standard Gibbs energy for a chemical reaction is the difference in standard molar Gibbs energies of the products and reactants in their standard states; it is easy to obtain the standard Gibbs energy of reaction by using the appropriate combination

$$\Delta_{\mathrm{r}} G_{\mathrm{m}}=\sum_{i} \nu_{i} \Delta_{\mathrm{f}} G_{\mathrm{m}}^{o}+\sum_{i} \gamma_{i} R T \ln \left(p_{i} / P^{\mathrm{o}}\right)\qquad(21)$$

When a system is in equilibrium, its standard Gibbs energy of reaction is equal to zero, that is,

$$\Delta_{\mathrm{r}} G_{\mathrm{m}}=0\qquad(22)$$

Substituting eqs 22 into 21 yields

$$\sum_{i} \nu_{i} \Delta_{\mathrm{f}} G_{\mathrm{m}}^{o}+\sum_{i} \gamma_{i} R(T / K) \ln \left(p_{i} / P^{\mathrm{o}}\right)=0\qquad(23)$$

By applying the above-mentioned formula 23 to reactions 18-20 successively, we obtain

$$\begin{gathered}
\Delta_{\mathrm{f}} G_{\mathrm{m}}\left(\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}\right)=\Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\beta-\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}\right) \\
+1.5 \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{H}_{2} \mathrm{O}\right)+1.5 R T \ln \left(P_{\mathrm{H}_{2} \mathrm{O}} / P^{\mathrm{o}}\right)
\end{gathered}\qquad(24)$$

$$\begin{gathered}
\Delta_{\mathrm{f}} G_{\mathrm{m}}\left(\mathrm{CaSO}_{4} \cdot 0.5 \mathrm{H}_{2} \mathrm{O}\right)=\Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\gamma-\mathrm{CaSO}_{4}\right) \\
+0.5 \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{H}_{2} \mathrm{O}\right)+0.5 R T \ln \left(P_{\mathrm{H}_{2} \mathrm{O}} / P^{\mathrm{o}}\right)
\end{gathered}\qquad(25)$$

$$\begin{gathered}
\Delta_{\mathrm{f}} G_{\mathrm{m}}\left(\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}\right) \\
=\Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\gamma-\mathrm{CaSO}_{4}\right)+2 \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{H}_{2} \mathrm{O}\right)+2 R T \ln \left(P_{\mathrm{H}_{2} \mathrm{O}} / P^{\mathrm{o}}\right) \\
(26)
\end{gathered}$$

By inserting the polynomials 4, 6, 7, and 9 into eqs 24-26 separately and by simplifying the result, we obtain the following three expressions

$$\begin{aligned}
& P_{\mathrm{H}_{2} \mathrm{O}(\text { gypsum-hemihydrate })} / P^{\mathrm{o}} \\
& \quad=\exp \left\{80.19 \times\left[-86.35+0.2316 T-0.2970 \times 10^{-5} T^{2}\right.\right. \\
& \left.\left.\quad-0.2110 \times 10^{-7} T^{3}\right] / T\right\}
\end{aligned}\qquad(27)$$

$$\begin{aligned}
& P_{\mathrm{H}_{2} \mathrm{O}(\text { gypsum-anhydrate })} / P^{\mathrm{o}} \\
& \quad=\exp \left\{60.14 \times\left[-114.70+0.2898 T+0.2154\right.\right. \\
& \left.\left.\quad \times 10^{-4} T^{2}-0.5509 \times 10^{-7} T^{3}\right] / T\right\}
\end{aligned}\qquad(28)$$

$$\begin{aligned}
& P_{\mathrm{H}_{2} \mathrm{O}(\text { hemihydrate-anhydrate })} / P^{\mathrm{o}} \\
& \quad=\exp \left\{240.60 \times\left[-28.33+0.05823 T+0.2451\right.\right. \\
& \left.\left.\quad \times 10^{-4} T^{2}-0.3399 \times 10^{-7} T^{3}\right] / T\right\}
\end{aligned}\qquad(29)$$

where $P_{H_{2} O (gypsum-hemihydrate) }$ is the equilibrium water vapor pressure of the reaction for the transformation of $CaSO_{4} \cdot 2 H_{2} O$ into $\beta-CaSO_{4} \cdot 0.5 H_{2} O, P_{H_{2} O (gypsum-anhydrate) }$ represents the dissociation pressure of $\beta-CaSO_{4} \cdot 0.5 H_{2} O$ dehydrated to form $\gamma-CaSO_{4}$ , and $P_{H_{2} O (hemihydrate-anhydrate) }$ naturally denotes the equilibrium water vapor pressure of the transformation of $\beta$  $CaSO_{4} \cdot 0.5 H_{2} O$ into $\gamma-CaSO_{4}$ .

To show the results of thermodynamic calculations more clearly, expressions 27-29 are simultaneously plotted in Figure2.

![](./images/812781164774293505_3.jpg)

Figure 2. Dehydration boundaries of the gypsum- $H_{2} O$ system in the range of 300-460 K. The symbols represent the experimental data of Kelley: $^{27}$ open circles and diamond denote the water vapor partial pressure of gypsum-hemihydrate and hemihydrate-soluble anhydrite equilibrium, respectively. Symbol A is the intersection of red, green, and blue curves and the axis of ordinates, B, C, and D, are the intersections of red, green, and blue curves and the horizontal line in Figure 2, respectively.

Three curves of the equilibrium water vapor pressure plotted versus the changes in temperature divide Figure 2 into four parts. It is easy to conclude that $CaSO_{4} \cdot 2 H_{2} O$ is stable and does not dehydrate to form $\beta-CaSO_{4} \cdot 0.5 H_{2} O$ or $\gamma-CaSO_{4}$ when the temperature and water vapor partial pressure are located in thezone above curve AB. With the increase of temperature, $CaSO_{4}$  $2 H_{2} O$ will partially lose its combined water and produce $\beta$  CaSO4-0.5H2O. If the temperature and water vapor pressure increase further, that is, if the coordinate point defined by the two values of both the temperature and water vapor pressure isin the ACD zone, $CaSO_{4} \cdot 2 H_{2} O$ first dehydrates to form $\gamma$  $CaSO_{4}$ and then the formed $\gamma-CaSO_{4}$ absorbs the water molecules in the autogenous or ambient atmosphere. Con- sequently, the water molecules reenter the $\gamma-CaSO_{4}$ framework to generate $\beta-CaSO_{4} \cdot 0.5 H_{2} O$ . In the region below curve AD, both $\beta-CaSO_{4} \cdot 0.5 H_{2} O$ and $\gamma-CaSO_{4}$ are thermodynamicallyunfavorable; hence, gypsum dehydrates to directly form $\gamma$  $CaSO_{4}$ in a single-step process $(CaSO_{4} \cdot 2 H_{2} O \to \gamma-CaSO_{4})$ .

The open circles and diamond denote the experimental water vapor partial pressure of gypsum-hemihydrate and hemi- hydrate-soluble anhydrite equilibrium, respectively. It is clear that the experimental results agree well with the result of the thermodynamic calculations.

Thermodynamic Analysis for the Transformation of Gypsum into the $CaSO_{4} \cdot n H_{2} O$ Phase. Over the past decades, many studies have proposed the existence of various subhydrates with a general chemical formula of $CaSO_{4} \cdot n H_{2} O$ , where the numerical value of $n$ ranges from 0 to $0.67.^{25,28}$ If the dehydration product $CaSO_{4} \cdot n H_{2} O$ occurs upon the heating of

gypsum, then the dehydration reaction of gypsum can be expressed as the following reaction

$$\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}=\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}+(2-n) \mathrm{H}_{2} \mathrm{O}\qquad(30)$$

Considering that reaction (30) is at equilibrium if the total difference in the Gibbs free energy is equal to zero, that is,

$$
\begin{aligned}
& \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{CaSO}_{4} \cdot 2 \mathrm{H}_{2} \mathrm{O}\right)=\Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}\right) \\
& +(2-n) \Delta_{\mathrm{f}} G_{\mathrm{m}}^{\mathrm{o}}\left(\mathrm{H}_{2} \mathrm{O}\right)+(2-n) R T \ln \left(P_{\mathrm{H}_{2} \mathrm{O}} / P^{\mathrm{o}}\right)
\end{aligned}
$$

By inserting (4), (7), and (17) into (31), the expression is simplified to

$$
\begin{aligned}
P_{\mathrm{H}_{2} \mathrm{O}}= & \exp \left(\left[-0.3069 T+1.112 \times 10^{-5} T^{2}\right.\right. \\
& +2.439 \times 10^{-8} T^{3}-\left(2.350 \times 10^{-5} T^{2}-0.1613 T\right. \\
& +71.20) \times n+5.466 n^{2}+118.3] \\
& \left./\left[\left(8.3140 \times 10^{-3} n-1.6630 \times 10^{-2}\right) \times T\right]\right)
\end{aligned}
$$

Figure 3 shows an overview of the effect of the temperature and water vapor pressure on the combined water number $n$ in

![](./images/812781164774293505_4.jpg)

Figure 3. (a) Surfaces of the equilibrium water vapor pressure calculated by eq 29 and of the saturated vapor pressure of water. (b) Projections of the intersection of different relative humidity water vapor surfaces and the equilibrium water vapor surface obtained from eq 32.

the $\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}$ phase formed by the dehydration of gypsum. In the higher relative humidity and lower temperature zone, the thermodynamic calculation results favor the occurrence of the $\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}(n>0.5)$ phase and the combined water number $n$ can approach its maximum of 0.67 because of the effect of the steric hindrances associated with the $\mathrm{H}_{2} \mathrm{O}-\mathrm{H}_{2} \mathrm{O}$ bond distance in the channel of the $\gamma-\mathrm{CaSO}_{4}$ lattice. $^{29}$ In fact, the occurrence of the $\mathrm{CaSO}_{4} \cdot 0.67 \mathrm{H}_{2} \mathrm{O}$ phase has been confirmed by the in situ XRD, and the initial dehydration product of gypsum was the $\mathrm{CaSO}_{4} \cdot 0.67 \mathrm{H}_{2} \mathrm{O}$ phase. $^{1}$

If the ambient temperature is low and the relative humidity is high, gypsum is stable and does not decompose to form any calcium sulfate hemihydrate. Furthermore, gypsum is thermodynamically unstable when the ambient temperature and relative humidity are high.

MC Simulation of Adsorption Water Vapor in the $\gamma$ $\mathrm{CaSO}_{4}$ Lattice. The $\gamma-\mathrm{CaSO}_{4}$ lattice consists of $\mathrm{Ca}^{2+}$ ions and a $\mathrm{SO}_{4}{ }^{2-}$ tetrahedron, and the alternating $\mathrm{Ca}^{2+}$ and $\mathrm{SO}_{4}{ }^{2-}$ ions in chains $-\mathrm{Ca}-\mathrm{SO}_{4}-\mathrm{Ca}-\mathrm{SO}_{4}{ }^{-}$form straight chains running along the [001] direction $^{30,31}$ such that these chains present a periodic arrangement and show a honeycomb structure. The faveolate voids appear to give the $\gamma-\mathrm{CaSO}_{4}$ framework the ability to absorb water molecules from the air, forming a $\mathrm{CaSO}_{4} \cdot n \mathrm{H}_{2} \mathrm{O}$ phase. In fact, the study of the adsorption phenomenon has a significant benefit for the manufacturing of plaster of paris and for obtaining the water vapor content in very dry areas, such as the desert or even Mars (Figure 4).

![](./images/812781164774293505_5.jpg)

Figure 4. Projection of the $\gamma-\mathrm{CaSO}_{4}$ lattice along the [001] vector, illustrating that the channels consist of six chains of alternating $\mathrm{Ca}^{2+}$ and $\mathrm{SO}_{4}{ }^{2-}$ perpendicular to the plane of the paper.

Figure 5 shows the adsorption isotherms of water in the $\gamma$ $\mathrm{CaSO}_{4}$ framework, along with the experimental data. It is clear that the MC simulation calculations agree well with the experimental results; $^{28,29}$ therefore, the relevant parameter setting employed in the simulation calculation processes is a suitable and powerful tool for investigating and predicting the adsorption isotherms of water vapor on the $\gamma-\mathrm{CaSO}_{4}$ lattice at different ambient temperatures and relative humidities, especially in a very low temperature and humidity environment that is very difficult to be achieved in the laboratory.

The experimental and calculated results presented in Figures 5 and 6 indicated that $\gamma-\mathrm{CaSO}_{4}$ has an excellent ability to adsorb water vapor at fairly low relative humidities in the temperature range of $215-298 \mathrm{~K}$. $\gamma-\mathrm{CaSO}_{4}$ can rehydrate to form $\mathrm{CaSO}_{4}$. $0.5 \mathrm{H}_{2} \mathrm{O}$ by adsorbing water vapor from the air when the relative humidity is as low as approximately $1 \%$ at $298 \mathrm{~K}$; however, the number of combined water in the $\gamma-\mathrm{CaSO}_{4}$ lattice approaches 0.67 when the relative humidity is more than $80 \%$ at $298 \mathrm{~K}$. Additionally, the MC simulation results also reveal the conformation of the water molecules distributed in the channel of the $\gamma-\mathrm{CaSO}_{4}$ framework.

![](./images/812781164774293505_6.jpg)

Figure 5. (a) Cumulative $H_2O$ occupancy for the $CaSO_4{\cdot}nH_2O$ ($0 < n < 0.67$) phase from 0 to 100 RH % derived from Rietveld refinements¹ and simulation at 298 K. (b) Density maps for water vapor molecules in a $\gamma$-CaSO₄ framework.

![](./images/812781164774293505_7.jpg)

Figure 6. Cumulative $H_2O$ occupancy for the $CaSO_4{\cdot}nH_2O$ ($0 < n < 0.67$) phase from 0 to 0.07 kPa derived from the simulation at 215 K.

It is obvious that $\gamma$-CaSO₄ has a strong adsorption ability under low water vapor pressure and at low temperature, although the amount of water adsorbed of $\gamma$-CaSO₄ is less than MOF-801 (a porous metal−organic framework, $Zr_6O_4(OH)_4(fumarate)_6$).³² With further decreases in the ambient temperature, $\gamma$-CaSO₄ can still capture 0.5 combined water molecules per $CaSO_4$ unit cell at about 0.04 Pa water vapor pressure and 215 K; these numbers show clearly that it may be utilized to harvest water from the extremely dry Martian atmosphere. Because the water vapor mixing ratio and atmospheric pressure on the surface of Mars are circa 600 ppm³³ and 610 Pa, respectively,³⁴ it is easy to draw the conclusion that the water vapor pressure on the Martian surface is approximately equal to 0.366 Pa. The MC simulation result (Figure 6) indicates that $\gamma$-CaSO₄ has the ability to absorb water molecules to form $CaSO_4{\cdot}nH_2O$ phases from the extremely dry Martian atmosphere; the numerical value of crystal water $n$ increases from 0 to 0.5 when the water vapor pressure ranges from 0 to 0.04 Pa at the average surface temperature of 215 K on Mars. Obviously, the water vapor pressure on Mars is far higher than the equilibrium water vapor pressure for $\gamma$-CaSO₄ rehydration to transform $CaSO_4{\cdot}0.5H_2O$. Thus, $\gamma$-CaSO₄ has a great potential to be used as a key material to indigenously obtain water on Mars. Additionally, the structures of $\gamma$-CaSO₄ and $CaSO_4{\cdot}0.5H_2O$ are highly similar as both crystal lattices provide honeycomb channels of 0.4 nm diameter.³⁵,³⁶ As a result, the faveolate framework of $\gamma$-CaSO₄ can remain almost unchanged throughout many cycles of the dehydration and water absorption processes of $\gamma$-CaSO₄.

## CONCLUSIONS
In this work, the dehydration pathways of gypsum and the rehydration mechanism of soluble anhydrite were mainly investigated by thermodynamic modeling and MC simulations. The dehydration pathways of gypsum are largely determined by ambient temperature and water vapor pressure. In the low- temperature and high water vapor zone above curve AB in Figure 2, gypsum is thermodynamically stable; in the ABC zone, $CaSO_4{\cdot}2H_2O$ will partially dehydrate its crystal water to form $\beta$-CaSO₄·0.5H₂O, and as the temperature is increased, gypsum undergoes a two-step dehydration process ($CaSO_4{\cdot}2H_2O \rightarrow \gamma$-CaSO₄ $\rightarrow \beta$-CaSO₄·0.5H₂O). In the region below curve AD, both $\beta$-CaSO₄·0.5H₂O and $\gamma$-CaSO₄ are all thermodynamically unfavorable; therefore, gypsum dehydrates to directly form $\gamma$-CaSO₄ in a single-step process ($CaSO_4{\cdot}2H_2O \rightarrow \gamma$-CaSO₄). Additionally, in the processes of gypsum dehydration and $\gamma$-CaSO₄ rehydration, the maximum $n$, which is the number of crystal water of the formed $CaSO_4{\cdot}nH_2O$, approaches 0.67; furthermore, MC simulations have successfully predicted the occupation of water molecules in the $\gamma$-CaSO₄ framework.

$\gamma$-CaSO₄ has an extraordinary ability to capture water molecules from extremely dry atmosphere, endowing $\gamma$-CaSO₄ a great potential to become a key material used to extract liquid water from very dry air. Moreover, it could also be used to industrial drying processes at room temperature in many fields because of its remarkable ability to absorb water vapor.

## ASSOCIATED CONTENT
### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acsomega.8b03476.

Matlab program for plotting Figure 3a and the lowest energy conformation for $CaSO_4{\cdot}0.67H_2O$ (PDF)

## AUTHOR INFORMATION
### Corresponding Author
*E-mail: jmgao@seu.edu.cn.

### ORCID
Yongbo Tang: 0000-0002-2771-6020

### Author Contributions
All authors have given approval to the final version of the manuscript.

### Notes
The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS
This work was financially supported by the National Natural Science Foundation of China (51578141), 973 Program (2015CB655102), and Ministry of Science and Technology of China (2016YFE0118200).

## ■ REFERENCES
(1) Robertson, K.; Bish, D. Constraints on the distribution of CaSO4· nH2O phases on Mars and implications for their contribution to the hydrological cycle. *Icarus* **2013**, 223, 407−417.

(2) Rapin, W.; Meslin, P.-Y.; Maurice, S.; Vaniman, D.; Nachon, M.; Mangold, N.; Schröder, S.; Gasnault, O.; Forni, O.; Wiens, R. C.; Martínez, G. M.; Cousin, A.; Sautter, V.; Lasue, J.; Rampe, E. B.; Archer, D. Hydration state of calcium sulfates in Gale crater, Mars: Identification of bassanite veins. *Earth Planet. Sci. Lett.* **2016**, 452, 197−205.

(3) Fishbaugh, K. E.; Poulet, F.; Chevrier, V.; Langevin, Y.; Bibring, J. P. On the origin of gypsum in the Mars north polar region. *J. Geophys. Res.* **2007**, 112, No. E07002.

(4) Palacio, S.; Azorín, J.; Montserrat-Martí, G.; Ferrio, J. P. The crystallization water of gypsum rocks is a relevant water source for plants. *Nat. Commun.* **2014**, 18, 4660.

(5) Gendrin, A.; Mangold, N.; Bibring, J. P.; Langevin, Y.; Gondet, B.; Poulet, F.; Bonello, G.; Quantin, C.; Mustard, J.; Arvidson, R.; LeMouélic, S. Sulfates in Martian Layered Terrains: The OMEGA/ Mars Express View. *Science* **2005**, 307, 1587−1591.

(6) Stawski, T. M.; Driessche, A. E. S.; Ossorio, M.; Rodriguez-Blanco, J. D.; Besselink, R.; Benning, L. G. Fromation of calcium sulfate through the aggregation of sub-3 nanometre primary species. *Nat. Commun.* **2016**, 7, 11177.

(7) Putnis, A.; Winkler, B.; Fernandez-Diaz, L. In situ IR spectroscopic and thermogravimetric study of the dehydration of gypsum. *Mineral. Mag.* **1990**, 54, 123−128.

(8) Chang, H.; Jane Huang, P.; Hou, S. C. Application of thermo- Raman spectroscopy to study dehydration of CaSO4·2H2O and CaSO4·0.5H2O. *Mater. Chem. Phys.* **1999**, 58, 12−19.

(9) Ballirano, P.; Melis, E. Thermal behavior and kinetics of dehydration of gypsum in air from in situ real-time laboratory parallel-beam X-ray powder diffraction. *Phys. Chem. Miner.* **2009**, 36, 391−402.

(10) Weiser, H. B.; Milligan, W. O.; Ekholm, W. C. The mechanism of the Dehydration of Calcium Sulfate Hemihydrate. *J. Am. Chem. Soc.* **1936**, 58, 1261−1265.

(11) McAdie, H. G. The effect of water vapor upon the dehydration of CaSO4·2H2O. *Can. J. Chem.* **1964**, 42, 792−801.

(12) Badens, E.; Llewellyn, P.; Fulconis, J. M.; Jourdan, C.; Veesler, S.; Boistelle, R.; Rouquerol, F. Study of gypsum dehydration by controlled transformation rate thermal analysis (CRTA). *J. Solid State Chem.* **1998**, 139, 37−44.

(13) Ball, M. C.; Norwood, L. S. Study in the system calcium sulphate- water. Part I. Kinetics of dehydration of calcium sulphate dihydrate. *J. Chem. Soc. A* **1969**, 0, 1633−1637.

(14) Lou, W.; Guan, B.; Wu, Z. Dehydration behavior of FGD gypsum by simultaneous TG and DSC analysis. *J. Therm. Anal. Calorim.* **2011**, 104, 661−669.

(15) Abriel, W.; Reisdorf, K.; Pannetier, J. Dehydration reactions of gypsum: A neutron and X-ray diffraction study. *J. Solid State Chem.* **1990**, 85, 23−30.

(16) Prasad, P. S. R.; Pradhan, A.; Gowd, T. N. In situ micro-raman investigation of dehydration mechanism in natural gypsum. *Curr. Sci.* **2001**, 80, 1203−1207.

(17) Carbone, M.; Ballirano, P.; Caminiti, R. Kinetics of gypsum dehydration at reduced pressure: an energy dispersive X-ray diffraction study. *Eur. J. Mineral.* **2008**, 20, 621−627.

(18) Metropolis, N.; Rosenbluth, A. W.; Rosenbluth, M. N.; Teller, A. H.; Teller, E. Equation of state calculation by fast computing machines. *J. Chem. Phys.* **1953**, 21, 1087−1092.

(19) Mayo, S. L.; Olafson, B. D.; Goddard, W. A. DREIDING: A generic force field for molecular simulations. *J. Phys. Chem.* **1990**, 94, 8897−8909.

(20) Waldman, M.; Hagler, A. T. New combining rules for rare gas van der Waals parameters. *J. Comput. Chem.* **1993**, 14, 1077−1084.

(21) Barin, I.; Platzki, G. *Thermochemical Data of Pure Substances*, 3nd ed.; Wiley-VCH Verlag GmbH: Weinheim, 1995; pp 484−485.

(22) DeKock, C. W. *Thermodynamic Properties of Selected Metal Sulfates and Their Hydrates*; United States Department of the interior: Washington, D C, 1986; pp 22−25.

(23) Robertson, K. The stability and crystallography of Mars relevant hygroscopic salts: implications for environmental conditions of formation and their subsequent role in the H₂O cycle. Ph.D. Dissertation, Indiana University, Indiana, U.S., 2011.

(24) Bezou, C.; Nonat, A.; Mutin, J.-C.; Christensen, A. N.; Lehmann, M. S. Investigation of the crystal structure of $\gamma$-CaSO₄, CaSO₄·0.5H₂O, and CaSO₄·0.6H₂O by powder difiiraction methods. *Solid State Chem.* **1995**, 117, 165−176.

(25) Karni, J.; Karni, E. Y. Gypsum in construction: origin and properties. *Mater. Struct.* **1995**, 28, 92−100.

(26) Valero, A.; Valero, A.; Vieillard, P. The thermodynamic properties of the upper continental crust: Energy, Gibbs free energy and enthalpy. *Energy* **2012**, 41, 121−127.

(27) Kelley, K. K.; Southard, J. C.; Anderson, C. T. *Thermodynamic Properties of Gypsum and Its Dehydration Products*; United States Bureau of Mines: Washington D. C., 1941; pp 22−29.

(28) Schmidt, H.; Paschke, I.; Freyer, D.; Voigt, W. Water channel structure of bassanite at high air humidity: crystal structure of CaSO₄·0.625H₂O. *Acta Crystallogr.* **2011**, 67, 467−475.

(29) Lager, G. A.; Armbrster, T.; Rotella, F. J.; Jorgensen, J. D.; Hinks, D. G. A crystallographic study of the low-temperature dehydration products of gypsum, CaSO₄·2H₂O: hemihydrates CaSO₄·0.5H₂O, and $\gamma$-CaSO₄. *Am. Mineral.* **1984**, 69, 910−918.

(30) Ballirano, P.; Melis, E. The thermal behaviour of $\gamma$-CaSO₄. *Phys. Chem. Miner.* **2009**, 36, 319−327.

(31) Kong, B.; Guan, B.; Yates, M. Z.; Wu, Z. Control of $\alpha$-Calcium sulfate hemihydrate morphology using reverse microemulsions. *Langmuir* **2012**, 28, 14137−14142.

(32) Kim, H.; Yang, S.; Rao, S. R.; Narayanan, S.; Kapustin, E. A.; Furukawa, H.; Umans, A. S.; Yaghi, O. M.; Wang, E. N. Water harvesting from air with metal-Organic frameworks powered by natural sunlight. *Science* **2017**, 356, 430−434.

(33) Montmessin, F. Modeling the annual cycle of HDO in the martian atmosphere. *J. Geophys. Res.* **2005**, 110, No. E03006.

(34) David, C. C. Mars Atmosphere: History and Surface Interactions. In *Encyclopedia of the Solar System*, 3rd ed.; Spohn, T., Breuer, D., Johnson, T. V., Eds.; Elsevier: Oxford, 2014; pp 343−357.

(35) Seufert, S.; Hesse, C.; Goetz-Neunhoeffer, F.; Neubauer, J. Quqntitative determination of anhydrite III from dehydrated gypsum by XRD. *Cem. Concr. Res.* **2009**, 39, 936−941.

(36) Christensen, A. N.; Olesen, M.; Cerenius, Y.; Jensen, T. R. Formation and Transformation of Five Different Phases in the CaSO₄- H₂O System: Crystal Structure of the Subhydrate $\beta$- CaSO₄·0.5H₂O and Soluble Anhydrate CaSO₄. *Chem. Mater.* **2008**, 20, 2124−2132.