**PAPER • OPEN ACCESS**

Room-temperature coefficient of thermal expansion of metals derived from the elastic constants

To cite this article: N A Palii and O K Belousov 2020 *J. Phys.: Conf. Ser.* **1431** 012042

View the [article online](article online) for updates and enhancements.

![](./images/812694129900257280_1.jpg)

# Room-temperature coefficient of thermal expansion of metals derived from the elastic constants

N A Palii and O K Belousov

A. A. Baikov Institute of Metallurgy and Materials Science, Leninskii pr. 49, 119334, Moscow, Russia

Email: palii@imet.ac.ru

**Abstract.** Room-temperature coefficients of thermal expansion (CTE), $\alpha$, of 27 metals and 2 semi-metals (Si and Ge) are derived from elastic constants (Young modulus, shear modulus, Poisson's ratio) coupled with a Debye treatment of the vibrating lattice. Theoretical values of $\alpha_{\text{calc}}$ show good agreement with the experimental ones.

## 1. Introduction
The large set of thermo-elastic data of pure metals and alloys can be derived from the first-principles electronic-structure calculations using quasi-harmonic approximation, ab initio total energy calculations, density functional method, and atomistic-continuum coupled model. Nevertheless, the precision computation of potential energy from the first principles and, on this basis, the calculation of coefficients of thermal expansion (CTE) is a formidable problem.

In this paper we propose a new method for calculating the CTE of metals by applying Debye-Grüneisen theorythrough the use of Young modulus ($E_\gamma$), shear modulus ($G$), and Poisson's ratio ($\mu$).

## 2. Computational method
The Debye-Grüneisen theory gain widespread acceptance in theoretical evaluation of the basic thermo-physical properties of metals, such as specific heats and linear CTE. According to the Grüneisen hypothesis, the dependence of the vibrational frequencies of atoms $v$ on the volume V is described by the expression [1]:

$$
-\frac{d \ln v_{j}}{d \ln V}=\gamma \tag{1},
$$

where $\gamma$ is the Grüneisen constant, the same for all normal modes. However, the dependence of $\gamma$ on temperature, pressure, and crystals direction was mentioned in the number of papers [1-3]. Moreover, the necessity of introducing two Grüneisen parameters $\gamma_{t}$ and $\gamma_{l}$ was pointed out in [1], and it was noted that the Grüneisen method describes partially the effects of anharmonicity. It is hard to take account of CTE contribution to higher order derivatives in the expansion of potential energy when describing small deviations from equilibrium, the difficulties arise in both choosing the exact value of the potential and the smallness of the calculated value [4]. The monograph [3] provides a great deal of

![](./images/812694129900257280_2.jpg)
Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
Published under licence by IOP Publishing Ltd

experimental data illustrating the deviations from the Grüneisen law and indicates that the equation given below requires clarification:

$$
\beta=\frac{\chi_{T} C_{V}}{V} \gamma \tag{2},
$$

where $\beta$ is the coefficient of volume expansion, $\chi_{T}$ is compressibility, $V$ is the specific volume, and $C_V$is the heat capacity at a constant volume.

Based on the Grüneisen equation (1), taking into account the interrelations between of the elastic constants $B$ (bulk modulus), $E_{Y}$ (Young's modulus), $G$ (shear modulus), we can write the equations for calculating $\alpha$ through the Poisson's ratio,$\mu$, (3) and the shear modulus (4):

$$
\alpha=\frac{(1-2 \mu) C_{V}}{E_{Y} V} \gamma \tag{3},
$$

$$
\alpha=\frac{(1-2 \mu) C_{V}}{2(1+\mu) G V} \gamma \tag{4}.
$$

The relationship between $C_{V}$ and $C_{P}$, the specific heat at constant pressure, is one of the most important equations resulting from the second law of thermodynamics, in order to calculate CTE it can be transformed [1, 5]:

$$
\alpha=\frac{1}{3}\left(\frac{C_{P}-C_{V}}{B V T}\right)^{1 / 2} \tag{5}.
$$

This equation does not include the Grüneisen coefficient $\gamma$, however, this parameter enters into the relation between $C_{V}$ and $C_{P}$: $C_{P}=C_{V}(1+\gamma \beta T)$ [1]. Since the $C_{P}$ value is very accurately measured on modern calorimeters, it was possible to calculate $\alpha$ from the equation (5).

### 3. Results
For copper (at $\gamma=2.03$) calculation according to equation (2) gives the exact values of $\alpha$ at low temperatures; namely, at 8 K, provided $\Theta_{D=} 344$, $B=142.0$ GPa, and $C_{V}$ is calculated from the $T^{3}$ Debye law: $C_{V}=(12 \pi^{4} / 5) R(T / \Theta)^{3}=3.82 \cdot 10^{-4} \mathrm{~J} / \mathrm{K}$, CTE is obtained as $\alpha_{calc}=1.6 \cdot 10^{-8} 1 / \mathrm{K}$, that is equal to $\alpha_{exp}=1.6 \cdot 10^{-8} 1 / \mathrm{K}$. At $10 \mathrm{~K}$ and $\Theta_{D}=340$, $\alpha_{calc}=3.3 \cdot 10^{-8} 1 / \mathrm{K}$ and it coincides with $\alpha_{exp}$. At $20 \mathrm{~K}$, $\alpha_{calc}=3.2 \cdot 10^{-7} 1 / \mathrm{K}$ ($\alpha_{exp}=3.2 \cdot 10^{-7} 1 / \mathrm{K}$). The discrepancy is observed only at $\mathrm{T}>50 \mathrm{~K}$ when the ratio $T / \Theta>0.153$, but these temperatures limit the range of applicability of the $\mathrm{T}^{3}$ Debye law.

Calculated according to equation (5), the values of $\alpha_{calc}$ were compared with the experimental ones, $\alpha_{exp}$; figure 1 represents the good agreement of their magnitudes at room temperature (RT), it can be seen that $\alpha_{calc}$ and $\alpha_{exp}$ for 27 metals and 2 semi-metals lie along the straight line $\mathrm{x}=\mathrm{y}$. These values of CTE are given in the table 1 along with other thermal and elastic properties of 29 elements. It bears mentioning that $\alpha_{calc}$, estimated in this work for $\mathrm{Li}, \mathrm{Nb}, \mathrm{Mo}, \mathrm{Cu}$, and $\mathrm{Al}$, fit better $\alpha_{exp}$ than CTE derived using quasi-harmonic approximation [6] and atomistic-continuum coupled (ACC) model (for $\mathrm{Au}$ and $\mathrm{Pb}$) [7].As can be seen from the table 1, the equation (5) describes adequately the thermal expansion of the most of metals and germanium. However, for polymorphous (Be, Ti), and for ferromagnetic (Fe, Ni)metals, as well as for silicon, the agreement with the experimental CTE is observed if½ of the calculated values is taken, i.e. $\alpha_{exp}=$α<sub>calc</sub>/2. As it was noted in [8, 9] the problem of precision computation of potential energy from the first principles and, on this basis, the calculation of

![](./images/812694129900257280_3.jpg)

Figure 1. Comparison of calculated ($\alpha_{calc}$) and experimental ($\alpha_{exp}$) [3] coefficients of thermal expansion at room temperature for 29 elements.

CTE is an extremely difficult task. Therefore, we present another approach to the problem - we express $\alpha$ in terms of the binding energy ($E_{B}$)and the energy of a longitudinal elastic wave ($\varepsilon_{l}$)as follows:

$$
\alpha=v \cdot C_{V}\left(\frac{1}{\varepsilon_{l} \cdot E_{B}}\right)^{1 / 2} \tag{6},
$$

where $\varepsilon_{l}=E_{l} \cdot V$ ($E_{l}$ - longitudinal elastic modulus of polycrystals), coefficient $v$ takes values from 0.4 to 0.5 for metals. A review of [4, 10, 11] suggests that $v$ corresponds to the relaxed value of Poisson's ratio, $\mu_{\mathrm{m}}$, at the critical points, which includes melting point ($\mathrm{T}_{\mathrm{m}}$) or polymorphic transformation ($\mathrm{T}_{\mathrm{c}}$); and it can be calculated according to McLaren empirical formula as:

$$
\mu_{m} \cong 0.83 \mu_{0}+0.14 \tag{7}.
$$

For example, for lithium we have $\mu_{0}=0.32$, therefore $v=0.40$, $E_{l}$=19.22 GPa, $\mathrm{C}_{\mathrm{V}}=3.41$ J/K, and $E_{B}$=1.65 eV/at.; we get $\alpha=47.3 \cdot 10^{-6} \mathrm{~K}^{-1}$, the experiment gives exactly the same. For potassium, a more fusible metal, for $v$, we take 0.50, then at $E_{l}$=5.73 GPA and $E_{B}$=0.93 eV/at we have $\alpha=81.4 \cdot 10^{-6} \mathrm{~K}^{-1}$,$\alpha_{\text {exp }}$ being$83.3 \cdot 10^{-6} \mathrm{~K}^{-1}$. It should be noted that equation (7) is approximate, and it does not always give exact results on the determination of $\mu_{\mathrm{m}}$, for example; for beryllium, apparently, the initial $\mu_{0}$ will be the value of $\mu$ at the polymorphic transformation point, i.e. one must resort to other methods of estimating $\mu_{\mathrm{m}}$. For lead and tungsten $\mu_{0}=0.43$ and $\mu_{0}=0.29$, correspondingly, thus we will have $v=$ 0,49 and $v=0.39$ (~ 0.4); then using the proper values$E_{l}=51.56$ GPa and $E_{l}=542.27$ GPa, as well as the binding energy of lead and tungsten $E_{B}=2.01$ eV and $E_{B}=9.38$ eV, we obtain, respectively, $\alpha=28.5 \cdot 10^{-6} 1 / \mathrm{K}$ and $\alpha=4.4 \cdot 10^{-6} 1 / \mathrm{K}$ (experiment gives exactly the same values). For fcc metals, copper and gold, $v=0.49$ and in so doing $\alpha_{\text {calc }}$ exactly matches the experiments. For beryllium, the calculations give accurate results only if we take $\mu_{\mathrm{m}}=2 \mu_{\text {calc }}$, apparently, this is the Poisson's ratio of the high-temperature phase of beryllium. It is likely that the mechanism of thermal expansion is shear, and thermal vibrations lead to shear reactions. This process of elastic relaxation is associated with
Table 1. Heat capacity at constant pressure ($C_{P}$) and volume ($C_{V}$), bulk compression modulus ($B$), Debye temperature ($\Theta_{t, r e l}$), Grüneisen constant ($\gamma_{\text {exp }}$) and coefficients of thermal expansion, calculated in this article ($\alpha_{calc}$) and experimental ones ($\alpha_{exp}$), for 27 metals and 2 semi-metals at room temperature.

<table>
<caption>Table 1. Elements properties</caption>
<thead>
<tr>
<th>Element</th>
<th>C<sub>P</sub></th>
<th>C<sub>V</sub></th>
<th>B</th>
<th>$\Theta_{t,rel}$</th>
<th>$\gamma_{exp}$</th>
<th>[3]</th>
<th>$\alpha_{calc}$</th>
<th>$\alpha_{calc}[6,7]$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Li</td>
<td>3.550</td>
<td>3.410</td>
<td>13.63</td>
<td>243</td>
<td>0.90</td>
<td>47.3</td>
<td>45.0</td>
<td>58.7</td>
</tr>
<tr>
<td>Na</td>
<td>1.20</td>
<td>1.081</td>
<td>7.21</td>
<td>99</td>
<td>1.33</td>
<td>71.5</td>
<td>77.0</td>
<td>70.3</td>
</tr>
<tr>
<td>K</td>
<td>0.74</td>
<td>0.637</td>
<td>3.99</td>
<td>69</td>
<td>1.34</td>
<td>83.3</td>
<td>90.0</td>
<td>91.0</td>
</tr>
<tr>
<td>V</td>
<td>0.48</td>
<td>0.475</td>
<td>155.87</td>
<td>282</td>
<td>1.38</td>
<td>7.8</td>
<td>9.3</td>
<td>6.8</td>
</tr>
<tr>
<td>Nb</td>
<td>0.26</td>
<td>0.257</td>
<td>187.50</td>
<td>180</td>
<td>1.60</td>
<td>7.2</td>
<td>7.3</td>
<td>5.4</td>
</tr>
<tr>
<td>Ta</td>
<td>0.137</td>
<td>0.136</td>
<td>206.10</td>
<td>183</td>
<td>1.70</td>
<td>6.6</td>
<td>6.6</td>
<td></td>
</tr>
<tr>
<td>Mo</td>
<td>0.250</td>
<td>0.248</td>
<td>285.20</td>
<td>324</td>
<td>1.67</td>
<td>5.3</td>
<td>4.9</td>
<td>4.9</td>
</tr>
<tr>
<td>W</td>
<td>0.132</td>
<td>0.131</td>
<td>338.30</td>
<td>257</td>
<td>1.60</td>
<td>4.4</td>
<td>4.6</td>
<td></td>
</tr>
<tr>
<td>Fe*</td>
<td>0.447</td>
<td>0.421</td>
<td>173.10</td>
<td>328</td>
<td>1.75</td>
<td>11.6</td>
<td>11.5</td>
<td></td>
</tr>
<tr>
<td>Ca</td>
<td>0.63</td>
<td>0.612</td>
<td>16.60</td>
<td>136</td>
<td>1.04</td>
<td>22.4</td>
<td>23.0</td>
<td>21.2</td>
</tr>
<tr>
<td>Ni*</td>
<td>0.44</td>
<td>0.400</td>
<td>186.50</td>
<td>329</td>
<td>1.87</td>
<td>13.3</td>
<td>13.1</td>
<td></td>
</tr>
<tr>
<td>Cu</td>
<td>0.384</td>
<td>0.373</td>
<td>137.20</td>
<td>238</td>
<td>2.00</td>
<td>16.8</td>
<td>16.8</td>
<td>13.4</td>
</tr>
<tr>
<td>Ag</td>
<td>0.235</td>
<td>0.226</td>
<td>100.10</td>
<td>154</td>
<td>2.50</td>
<td>18.9</td>
<td>18.3</td>
<td>18.8</td>
</tr>
<tr>
<td>Au</td>
<td>0.131</td>
<td>0.126</td>
<td>172.10</td>
<td>100</td>
<td>3.00</td>
<td>14.0</td>
<td>14.0</td>
<td>13.1</td>
</tr>
<tr>
<td>Al</td>
<td>0.913</td>
<td>0.883</td>
<td>76.40</td>
<td>286</td>
<td>2.30</td>
<td>22.9</td>
<td>20.0</td>
<td>17.3</td>
</tr>
<tr>
<td>Pb</td>
<td>0.128</td>
<td>0.120</td>
<td>40.37</td>
<td>49</td>
<td>2.60</td>
<td>28.5</td>
<td>28.8</td>
<td>24.3</td>
</tr>
<tr>
<td>Pd</td>
<td>0.240</td>
<td>0.230</td>
<td>192.30</td>
<td>197</td>
<td>2.3</td>
<td>11.7</td>
<td>15.1</td>
<td>10.8</td>
</tr>
<tr>
<td>Pt</td>
<td>0.130</td>
<td>0.126</td>
<td>274.80</td>
<td>154</td>
<td>2.6</td>
<td>9.9</td>
<td>9.9</td>
<td></td>
</tr>
<tr>
<td>Ir</td>
<td>0.126</td>
<td>0.125</td>
<td>370.20</td>
<td>280</td>
<td>-</td>
<td>6.4</td>
<td>4.5</td>
<td></td>
</tr>
<tr>
<td>Be*</td>
<td>1.983</td>
<td>1.916</td>
<td>125.80</td>
<td>850</td>
<td>-</td>
<td>9.3</td>
<td>9.5</td>
<td></td>
</tr>
<tr>
<td>Mg</td>
<td>1.020</td>
<td>0.989</td>
<td>33.26</td>
<td>259</td>
<td>1.60</td>
<td>25.8</td>
<td>24.6</td>
<td></td>
</tr>
<tr>
<td>Y*</td>
<td>0.297</td>
<td>0.276</td>
<td>46.94</td>
<td>141</td>
<td>1.57</td>
<td>10.8</td>
<td>13.5</td>
<td></td>
</tr>
<tr>
<td>Re</td>
<td>0.130</td>
<td>0.128</td>
<td>363.33</td>
<td>290</td>
<td>2.59</td>
<td>6.8</td>
<td>6.3</td>
<td></td>
</tr>
<tr>
<td>Ti*</td>
<td>0.520</td>
<td>0.503</td>
<td>123.56</td>
<td>196</td>
<td>1.19</td>
<td>7.1</td>
<td>7.6</td>
<td></td>
</tr>
<tr>
<td>Zn</td>
<td>0.389</td>
<td>0.373</td>
<td>58.39</td>
<td>208</td>
<td>1.98</td>
<td>28.3</td>
<td>27.3</td>
<td></td>
</tr>
<tr>
<td>Cd</td>
<td>0.231</td>
<td>0.220</td>
<td>43.60</td>
<td>134</td>
<td>2.28</td>
<td>29.9</td>
<td>29.3</td>
<td></td>
</tr>
<tr>
<td>In</td>
<td>0.230</td>
<td>0.216</td>
<td>39.24</td>
<td>85</td>
<td>2.34</td>
<td>30.5</td>
<td>30.6</td>
<td></td>
</tr>
<tr>
<td>Si*</td>
<td>0.705</td>
<td>0.702</td>
<td>98.10</td>
<td>670</td>
<td>0.50</td>
<td>2.5</td>
<td>2.5</td>
<td></td>
</tr>
<tr>
<td>Ge</td>
<td>0.320</td>
<td>0.319</td>
<td>75.40</td>
<td>371</td>
<td>0.75</td>
<td>5.8</td>
<td>5.6</td>
<td></td>
</tr>
<tr>
<td colspan="9">C<sub>P</sub>andC<sub>V</sub>in J/K, B - inGPa, $\alpha \cdot 10^{-6}$ 1/K, $\alpha$*=$\alpha$/2</td>
</tr>
</tbody>
</table>

increase in volume with increasing temperature. Polymorphism, as well as magnetic transitions, introduces corrections to the calculation of $\alpha$ according to equation (5);this is due to the mechanism of these phase transitions, which also have a shear character.

Figure 2 shows the results of CTE calculations, $\alpha_{calc}$, depending on the binding energy of the elements, $\varepsilon_{i}$ according to equation (6) and taking account of (7); as can be seen, with the increasing of binding energy, the $\alpha_{calc}$ decreases monotonically.

![](./images/812694129900257280_4.jpg)

Figure 2. Thermal expansion coefficients versus binding energy of the elements; line - calculated according to equation (6), $\alpha_{calc,}$ and cross + - experimental,$\alpha_{exp}$ [3].

### 4. Conclusions
A new method for calculating the TCE of metals using elastic constants is proposed, the calculated TCE values are in good agreement with the theoretical ones.

### Acknowledgements
The work was carried out according to the state task No. 075-00746-19-00.

### References
[1] Girifalco, L. A. (1973). *Statistical physics of materials*. John Wiley & Sons.
[2] Finkel, V. A. (1971). Low-Temperature X-ray Diffraction of Metals. *Metallurgy, Moscow*.
[3] Novikova, S. I. (1974). Thermal expansion of solids. *Moscow Izdatel Nauka*.
[4] Belousov, O. K. (1999). On the problem of estimating the theoretical mode I and shear strengths of crystals. *Izv. Ross. Akad. Nauk, Ser. Met.*, (4), 56-65.
[5] Lumsden, J. (1952). *Thermodynamics of alloys* (Vol. 11). Inst. of Metals.
[6] Moruzzi, V. L., Janak, J. F., & Schwarz, K. (1988). Calculated thermal properties of metals. *Physical Review B*, **37**(2), 790.
[7] Zhang, J., Cui, J., Yang, Z., & Yu, Y. (2019). Heat capacity and thermal expansion of metal crystalline materials based on dynamic thermal vibration. *Computational Mechanics*, 63(5), 971-984.
[8] Mitra, S. S., & Joshi, S. K. (1961). Thermal expansion of metals. *The Journal of Chemical Physics*, 34(4), 1462-1463.
[9] Ziman, J. M. (1972). *Principles of the Theory of Solids*. Cambridge university press.
[10] Belousov, O. K. (1994). Bonding energy calculation in metals and covalent crystals. *Izv AN SSSR Met.*, (1), 33-40.
[11] Belousov, O. K. (1993). On the Nature of the Enthalpy of Melting of Metals. *Izv. Ross. Akad. Nauk, Ser. Met.*, (3), 29-34.