![](./images/811139289885704193_1.jpg)

Molecular Physics
An International Journal at the Interface Between Chemistry and Physics

ISSN: 0026-8976 (Print) 1362-3028 (Online) Journal homepage: http://www.tandfonline.com/loi/tmph20

First-principles calculations of elastic, phonon and thermodynamic properties of W

Zhi-Cheng Guo, Fen Luo, Xiu-Lu Zhang, Chang-Ying Yuan, Cheng-An Liu & Ling-Cang Cai

To cite this article: Zhi-Cheng Guo, Fen Luo, Xiu-Lu Zhang, Chang-Ying Yuan, Cheng-An Liu & Ling-Cang Cai (2016): First-principles calculations of elastic, phonon and thermodynamic properties of W, Molecular Physics, DOI: 10.1080/00268976.2016.1234653

To link to this article: http://dx.doi.org/10.1080/00268976.2016.1234653

![](./images/811139289885704193_2.jpg)
Published online: 27 Sep 2016.

![](./images/811139289885704193_3.jpg)
Submit your article to this journal 

![](./images/811139289885704193_4.jpg)
Article views: 24

![](./images/811139289885704193_5.jpg)
View related articles 

![](./images/811139289885704193_6.jpg)
View Crossmark data

Full Terms & Conditions of access and use can be found at
http://www.tandfonline.com/action/journalInformation?journalCode=tmph20

Download by: [FU Berlin]
Date: 30 November 2016, At: 12:03

RESEARCH ARTICLE

# First-principles calculations of elastic, phonon and thermodynamic properties of W

Zhi-Cheng Guo $^{a}$, Fen Luo $^{a}$, Xiu-Lu Zhang $^{a,b}$, Chang-Ying Yuan $^{a}$, Cheng-An Liu $^{a}$ and Ling-Cang Cai $^{b}$

$^{a}$Laboratory for Extreme Conditions Matter Properties, Southwest University of Science and Technology, Mianyang, China; $^{b}$National Key Laboratory for Shock Wave and Detonation Physics Research, Institute of Fluid Physics, Chinese Academy of Engineering Physics, Mianyang, China

## ABSTRACT
We investigate the elastic properties, lattice dynamical, thermal equation of state and thermodynamic properties of bcc phase W under high pressure using density functional theory. The calculated high-pressure elastic constants of bcc phase W agree well with experimental and theoretical data. Under compression, the phonon dispersion curves of bcc phase W do not show any anomaly or instability. Our calculated zero-pressure phonon dispersion curves are in excellent agreement with experiments. Within the quasiharmonic approximation, we predict the thermal equation of state and other properties including the thermal expansion coefficient, adiabatic bulk modulus, specific heat at constant volume and entropy.

![](./images/811139289885704193_7.jpg)

## ARTICLE HISTORY
Received 26 June 2016
Accepted 26 August 2016

## KEYWORDS
Elastic properties;
thermodynamic properties;
density functional theory

## 1. Introduction

The molybdenum (Mo), tantalum (Ta) and tungsten (W), as the basis of the ultrahigh pressure scale in diamond anvil cell experiments, are especially interesting for their high melting points at ambient pressure and are stable as body-centred cubic (bcc) structure at high pressure at room temperature [1,2]. W has excellent mechanical strength and chemical resistant and has been widely used in aerospace industries and electronic industries [3]. For those important applications, scientific investigations on structural stability and phase diagram of tungsten have attracted tremendous experimental and theoretical interest [4–17].

The accurate thermal equation of state (EOS) and thermodynamic properties as a function of pressure and temperature can provide valuable information for understanding the phase diagram and dynamical response of materials under extreme conditions. By means of X-ray diffraction, the pressure–volume relations were determined under hydrostatic pressure to 100 kbar at room temperature [4]. Dewaele *et al.* [5] measured the volume of W in the range of 0–153 GPa at ambient temperature with X-ray diffraction. With shock-wave compression techniques [6], the shock-wave data have been obtained for W. The EOS data of W were obtained with ultrasonic measurement at high temperature or high pressure [7–10]. Recently, the *P-V-T* dataset for bcc-W at pressures from 0.0001 to 33.5 GPa and temperatures up to 1673 K were obtained by using MgO and Au pressure scales [11]. Theoretically, the relations of volume and pressure were obtained from all-electron, density-functional calcula-

---
CONTACT Zhi-Cheng Guo luofen@swust.edu.cn, zcguo1986@126.com
© 2016 Informa UK Limited, trading as Taylor & Francis Group

tions [12]. Wang *et al.* [13] reported Hugoniots and 293-K isotherms at pressures up to 1 TPa for W by using the classical mean-field approach. The pressure dependences of relative volume of W were investigated within density functional theory (DFT) [14,15]. Based on *ab initio* calculations, Xiang *et al.* [16] presented the relative volume and thermodynamic properties of W in a wide range of pressure and temperature. Koči *et al.* [17] calculated the elastic constants as a function of pressure for V, Nb, Ta, Mo and W with first-principles calculations. However, the investigations of thermodynamic properties of W under extreme conditions are still scarce. Thus, the investigation of the thermodynamic properties of W under high temperature and pressure will be still a requirement.

Density functional perturbation theory (DFPT) [18,19] is a well-established method for calculating the thermodynamic properties below the melting temperature from first principles in the framework of the quasiharmonic approximation (QHA). The crystal free energy is easily included by adding the phonon free energy to the static energy through the standard DFT calculation. The volume dependences of phonon frequencies contains the partial anharmonic effects. In the present work, we apply DFPT to the study of the elastic, lattice dynamical, thermal EOS and thermodynamic properties of bcc phase W. First, we discuss the structural and elastic properties of bcc phase W under high pressure. Then, based on phonon frequencies, we study thermal EOS and the thermodynamic properties of bcc phase W within the framework of QHA.

## 2. Computational details

According to QHA, the Helmholtz free energy is given by

$$
F(V, T)=E_{\text{static}}(V)+F_{\text{phon}}(V, T)+F_{\text{elec}}(V, T), \quad (1)
$$

where $E_{\text{static}} (V)$ is the energy of a static lattice at zero temperature $T$ and volume $V$, $F_{\text{elec}} (V,T)$ is the thermal free energy arising from electronic excitations and $F_{\text{phon}} (V,T)$ is the phonon contribution. Both $E_{\text{static}} (V)$ and $F_{\text{elec}} (V,T)$ can be evaluated via static first-principles calculations directly. The phonon vibrational contribution $F_{\text{phon}} (V,T)$ can be expressed as

$$
\begin{aligned}
F_{\text{phon}}(V, T) &= \frac{1}{2} \sum_{q,j} \hbar \omega_{j}\left(q, V\right) \\
&+ k_{B} T \sum_{q,j} \ln\left\{1-\exp\left[-\hbar \omega_{j}\left(q, V\right)/k_{B} T\right]\right\}, \quad (2)
\end{aligned}
$$

where $k_{B}$ is the Boltzmann constant, $\hbar$ is the Plank constant divided by $2\pi$, and $\omega_{j}(q,V)$ is the phonon frequency of the $j$th mode of wave vector $q$ in the first Brillouin zone. The phonon dispersion calculations of W have been performed within DFPT as implemented in the Quantum Espresso package [20]. The exchange correlation energy of the electrons is described in the framework of the generalised gradient approximation with the functional parametrisation of the Perdew-Burke-Ernzerhof [21]. A nonlinear core correction to the exchange-correlation energy function is introduced to generate an ultrasoft pseudopotential [22] for W with the valence electrons configuration $5s^25p^65d^46s^2$. To ensure the convergence of free energies, we make careful tests on $k$, $q$ grids and the kinetic energy cut-off. The plane wave cut-off for the wave functions is 60 Ry. The Monkhorst-Pack meshes [23] are $14 \times 14 \times 14$ for bcc phase W. The dynamical matrices are computed at 29 wave ($q$) vectors using $8 \times 8 \times 8$ $q$ grid in the irreducible wedge of the Brillouin zone. The geometric mean phonon frequency is defined by

$$
\ln \bar{\omega}=\frac{1}{N_{q j}} \sum_{q j} \ln \bar{\omega}_{q j}, \tag{3}
$$

where $\omega_{qj}$ is the phonon frequency of the branch $j$ at the wave vector $q$ and $N_{qj}$ is the number of branches times the total number of $q$ points in the sum. With this choice of parameters, the geometric mean phonon frequency $\omega$ was converged to $1\ \text{cm}^{-1}$.

<table>
<caption>Table 1. The equilibrium volume $V_0$ (Å³/atom), zero-pressure bulk modulus $B_0$ (GPa), pressure derivative $B'$ and elastic constants (GPa) of W at zero pressure, in comparison with the experimental data and other theoretical results.</caption>
<thead>
<tr>
<th>□</th>
<th>$V_0$</th>
<th>$B_0$</th>
<th>$B'$</th>
<th>$C_{11}$</th>
<th>$C_{12}$</th>
<th>$C_{44}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Present</td>
<td>16.211</td>
<td>301.038</td>
<td>4.042</td>
<td>512.4</td>
<td>194.6</td>
<td>141.9</td>
</tr>
<tr>
<td>Experiment $^a$</td>
<td>15.86</td>
<td>296</td>
<td>4.3</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Experiment $^b$</td>
<td></td>
<td></td>
<td></td>
<td>521.0</td>
<td>201.8</td>
<td>160.4</td>
</tr>
<tr>
<td>Theory $^c$</td>
<td>15.64</td>
<td></td>
<td></td>
<td>501.5</td>
<td>202.6</td>
<td>142.2</td>
</tr>
<tr>
<td>Theory $^d$</td>
<td>16.25</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="7">$^a$ The data come from Ref. [5]</td>
</tr>
<tr>
<td colspan="7">$^b$ The data come from Ref. [7].</td>
</tr>
<tr>
<td colspan="7">$^c$ The data come from Ref. [2].</td>
</tr>
<tr>
<td colspan="7">$^d$ The data come from Ref. [16].</td>
</tr>
</tbody>
</table>

## 3. Results and discussions

### 3.1. Structural and elastic properties

For bcc phase W, a series of different values of lattice constant are set to calculate the static energy $E$ and the corresponding primitive cell volumes $V$, and then obtained $E$-$V$ data are fitted to the fourth-order finite strain EOS [24]. The equilibrium volume $V$, the bulk modulus $B_0$ and its pressure derivative $B'$ are list in Table 1. Our results are also in excellent agreement with the available

experimental [5,7] and other calculated results [2,16], which implies the validity of the present calculations.

To examine the mechanical stability of the bcc phase W, the elastic properties are investigated in this work. The three elastic constants $C_{11}$, $C_{12}$ and $C_{44}$ completely describe the elastic behaviour of a cubic crystal. The relationship between the elastic constants and the bulk modulus can be written as

$$
B=(C_{11}+2C_{12})/3. \tag{4}
$$

To determine $C_{11}$ and $C_{12}$, we applied the following volume conserving strain matrix:

$$
\varepsilon(\delta)=\begin{pmatrix}
\delta & 0 & 0 \\
0 & \delta & 0 \\
0 & 0 & (1+\delta)^{-2}-1
\end{pmatrix}, \tag{5}
$$

where $\delta$ is the infinitesimal strain magnitude. Then the strain energy is written as a function of the strain,

$$
E(\delta)=E(0)+3(C_{11}-C_{12})V\delta^{2}+O(\delta^{3}), \tag{6}
$$

where $E(0)$ is the energy of the unstrained unit cell and $V$ is the corresponding volume. $C_{44}$ is deduced by applying the following volume-conserving strain matrix to the unit cell:

$$
\varepsilon(\delta)=\begin{pmatrix}
0 & \delta & 0 \\
\delta & 0 & 0 \\
0 & 0 & \delta^{-2}/(1-\delta^{-2})
\end{pmatrix}, \tag{7}
$$

and correspondingly the strain energy is

$$
E(\delta)=E(0)+2C_{44}V\delta^{2}+O(\delta^{4}). \tag{8}
$$

Then, $C_{44}$ is calculated by finding the quadratic coefficients. To calculate the elastic constants accurately, we use the $20\times20\times20$ Monkhorst-Pack [23] meshes in self-consistent calculations. The high-pressure elastic constants of bcc phase W are obtained by using the method described above. For elastic constants, we first derived the volume as a function of pressure by fitting a fourth-order finite strain EOS [24] to the calculated energy-volume data. The elastic constants of bcc phase W are presented in Table 1 and Figure 1(a), respectively. For a stable cubic structure, its three independent elastic constants $C_{ij}$ should satisfy the mechanical stability criteria, i.e. $\tilde{C}_{44}>0$, $\tilde{C}_{11}>|\tilde{C}_{12}|$, and$\tilde{C}_{11}+2\tilde{C}_{12}>0$, where $\tilde{C}_{\alpha\alpha}=C_{\alpha\alpha}-P(\alpha=1,4)$, and $\tilde{C}_{12}=C_{12}+P$. Clearly, these calculated elastic constants $C_{ij}$ satisfy the mechanical stability criteria, suggesting that bcc phase W is mechanically stable under the applied pressure.

From Table 1, one note that $C_{12}$ agrees well with experiment [7]. However, $C_{11}$ is underestimated by 1.65% and $C_{44}$ is underestimated by 11.53%, compared with experiment [7]. The three elastic constants increase as pressure increases and decrease with increasing temperature linearly. From Figure 1(a), one can see that the high-pressure elastic constants and their general trend are also in good agreement with theoretical data [17]. Based on the Voigt-Reuss-Hill approximation [25], we have calculated the corresponding bulk modulus $B$, shear modulus $G$ and Young's modulus $E$ from the single crystal elastic constants. The bulk modulus, shear modulus and Young's modulus increase monotonously with pressure increasing, as presented in Figure 1(b).

### 3.2. Thermal equation of state
With the framework of the DFPT, we obtained phonon dispersion curves of bcc phase W along high-symmetry directions. Figure 2 shows that the obtained dispersion curves at zero pressure agree well with the experimental dispersion curves [26] at room temperature. The bcc phase W is dynamically stable at zero pressure as the phonon frequencies do not show any anomaly. In order to obtain accurately Helmholtz free energy $F$ as a function of volume $V$ at a certain temperature, the $F$ at 19 atomic volumes (between $V=7$ and $19$ $\mathring{\text{A}}^{3}$/atom) for bcc phase W have been calculated. Figure 2 shows that the frequencies in the dispersion curves of bcc phase W increase with decreasing volume. We do not find soft modes in the applied range of volumes, and the phonon frequencies reflect the dynamic stability.

We obtained the Helmholtz free energy of bcc phase W as a function of volume $V$ and temperature $T$ from Equation (1). Figure 3 shows the Helmholtz free energy as a function of volume at temperatures from 0 to 3000 K. By fitting the Helmholtz free energy to the fourth-order finite strain EOS at each temperature, we get the theoretical isothermal compressional curves of bcc phase W, as shown in Figure 4. Our calculated results show excellent agreement with previous experimental [4] and theoretical [16] results. It is noted that the 0 K isotherm is almost the same as the 300 K one, and this is due to the small free energy contribution from the lattice vibrations at 300 K. Compared to the equilibrium volume at zero pressure, the volume of 300 K increases 2.9%.

The thermal pressure can be obtained from the pressure difference with the 0 K isotherm. The thermal pressure as a function of volume and temperature is shown in Figure 5(a,b). From Figure 5(a), one notes that the thermal pressures are small and essentially volume-independent at low temperatures. The thermal pressure increases significantly at elevated temperature. The thermal pressures as a function of temperature are shown in Figure 5(b). At a given volume, the thermal pressure

![](./images/811139289885704193_8.jpg)

Figure 1. (a) The high-pressure elastic constants for bcc phase W. The theoretical data [17] are plotted as the squares. (b) The polycrystalline aggregate properties of bulk modulus B, shear modulus G and Young's modulus E for bcc phase W.

![](./images/811139289885704193_9.jpg)

Figure 2. Phonon dispersion curves of bcc phase at different volumes ($V_0$ is the static equilibrium volume of bcc phase W). The squares are the experimental data by Chen et al. [26] at room temperature.

![](./images/811139289885704193_10.jpg)

Figure 3. The free energy versus volume curves of bcc phase W at temperatures from 0 to 3000 K with 500 K intervals.

increases linearly with temperature. The slopes of the thermal pressure show strong volume dependence. Many previous calculations for metals (such as Ta [27] and Be [28] and so on) also found that the slopes of the thermal pressure were strongly volume-dependent.

### 3.3. Thermodynamic properties

Thermal expansion coefficient $\alpha_V$ is a very important parametric quantity for interpreting the thermodynamic behaviours of solid. The thermal expansion coefficient $\alpha_V$ is defined as $\alpha_V = \frac{1}{V} (\frac{\partial V}{\partial T})_P$. The temperature and pressure dependences of the thermal expansion coefficient $\alpha_V$ of bcc phase W are indicated in Figure 6. Our zero pressure results are in excellent agreement with the experimental data [11,29]. At high temperature, our results seem much better than that from Litasov et al. [11]. From Figure 6, it can be seen that the calculated thermal expansion coefficient of bcc phase W decreases with the increase of pressure. As the pressure rises, the thermal expansion coefficient increases with temperature, and then turns almost linear at high temperature. The influence of temperature on thermal expansion coefficient is very small under high pressure. This is mainly because the anharmonic effect becomes less important under high pressures. Then, the validity of the QHA extends to higher temperatures at higher pressures.

![](./images/811139289885704193_11.jpg)

Figure 4. Isothermal compression curves of bcc phase W at different temperatures, compared with experimental [4] and theoretical data [16].

![](./images/811139289885704193_12.jpg)

Figure 5. Calculated thermal pressures of bcc phase W (a) as a function of volume and (b) temperature.

The isothermal bulk modulus $B_T$ can be obtained from$B_T = \frac{1}{\alpha}(\frac{\partial P}{\partial T})_V$.The adiabatic bulk modulus $B_S$ correlates with $B_T$ via $B_S - B_T = -\alpha\gamma B_T T$. Figure 7 shows the adiabatic bulk modulus of bcc phase W as a function of temperature and pressure. Our zero-pressure adiabatic bulk modulus are consistent with the experimental data [11,30]. The adiabatic bulk modulus decreases with increasing temperature at fixed pressures and increases with increasing pressure at different temperatures. The temperature dependence of the adiabatic bulk modulus becomes weaker and weaker with increasing pressure.

![](./images/811139289885704193_13.jpg)

Figure 6. The thermal expansion coefficient $\alpha_V$ of bcc phase W as a function of temperature at different pressures, in comparison with experimental data [11,29].

![](./images/811139289885704193_14.jpg)

Figure 7. The adiabatic bulk modulus $B_S$ of bcc phase W vs. temperature at different pressures, in comparison with experimental data [11,30].

The knowledge of the specific heat at constant volume $C_V$ can provide an essential insight into the vibrational properties of solids. The specific heat at constant volume is defined by $C_V = (\frac{\partial U}{\partial T})_V$, where $U$ is the internal energy of the system. Figure 8 shows the specific heat at constant volume $C_V$ of bcc phase W as a function of temperature at various pressures. It can be seen that $C_V$ increases exponentially with the temperature when temperature is below 500 K. At intermediate temperatures, the temperature dependences of $C_V$ are governed by the details of vibrations of the atoms. With the temperature increasing, $C_V$ increases slowly and approaches a constant $3R$ at high temperature due to the Dulong-Petit limit. It is clear that the increased tendency of $C_V$ at different pressures is similar. The entropy $S$ can be calculated with $S = -(\frac{\partial F}{\partial T})_V$.

![](./images/811139289885704193_15.jpg)

Figure 8. The specific heat at constant volume $C_V$ of bcc phase W as a function of temperature at different pressures.

![](./images/811139289885704193_16.jpg)

Figure 9. The entropy $S$ of bcc phase W as a function of temperature at different pressures, in comparison with experimental data [11,31].

The temperature and pressure dependences of entropy $S$ of bcc phase W are indicated in Figure 9. The calculated $S$ of bcc phase W is in agreement with the experimental data [11,31]. It can be clearly seen that the entropy $S$ increases with the temperature. For a given temperature, the entropy $S$ decreases slightly with the pressure increasing.

## 4. Conclusions

We have employed the DFPT to investigate the elastic properties, lattice dynamical, thermal EOS and thermodynamic properties of the bcc phase W. By comparing the static energy-volume for bcc phase W, the lattice parameters, bulk modulus and its pressure derivative for bcc phase W are obtained. All the results are well consistent with the experimental data and other theoretical results. From the elastic constants at high pressure, we find that bcc phase W is stable. Bulk modulus, shear modulus and Young's modulus as a function of pressure are obtained.

Our calculated phonon dispersion curve of bcc phase at zero pressure agrees extremely well with experiment. Under compression, the dispersion curves of bcc phase W do not show any anomaly or instability. With the QHA, the thermal EOS, thermal expansion coefficient, adiabatic bulk modulus, specific heat at constant volume and entropy are obtained successfully. The zero-pressure temperature dependences of thermal expansion coefficient, adiabatic bulk modulus and entropy are found to be in a good agreement with the experimental results. These investigations concerning the thermal properties in the present work will be very useful for experts to study W under high pressure and high temperature.

## Acknowledgments

The authors would like to thank Prof. Dr X. R. Chen for his useful suggestions.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## Funding

The authors acknowledge the financial support of the National Natural Science Foundation of China [grant number 11547239], [grant number 11604272]; Doctor Foundation of Southwest University of Science and Technology [grant number 14zx7167], [grant number 13zx7137]; Basic Research of Science and Technology Program of China [grant number JSHS2014404B002].

## ORCID

Zhi-Cheng Guo http://orcid.org/0000-0001-9022-4523

## References

[1] J.A. Moriarty, Phys. Rev. B 45, 2004 (1992).
[2] C.M. Liu, X.R. Chen, C. Xu, L.C. Cai, and F.Q. Jing, J. Appl. Phys. 112, 013518 (2012).
[3] F. Luo, Z.C. Guo, X.L. Zhang, C.Y. Yuan, and L.C. Cai, Phil. Mag. Lett. 95, 211 (2015).
[4] L.C. Ming and M.H. Manghnani, J. Appl. Phys. 49, 208 (1978).
[5] A. Dewaele, P. Loubeyre, and M. Mezouar, Phys. Rev. B 70, 094112 (2004).
[6] R.S. Hixson and J.N. Fritz, J. Appl. Phys. 71, 1721 (1992).
[7] D.I. Bolef and J. De Klerk, J. Appl. Phys. 33, 2311 (1962).
[8] F.H. Featherston and J.R. Neighbours, Phys. Rev. 130, 1324 (1963).
[9] R. Lowrie and A.M. Gonas, J. Appl. Phys. 38, 4505 (1967).
[10] K.W. Katahara, M.H. Manghnani, and E.S. Fisher, J. Phys. F 9, 773 (1979).

[11] K.D. Litasov, P.N. Gavryushkin, P.I. Dorogokupets, I.S. Sharygin, A. Shatskiy, Y.W. Fei, S.V. Rashchenko, Y.V. Seryotkin, Y. Higo, K. Funakoshi, and E. Ohtani, J. Appl. Phys. 113, 133505 (2013).

[12] A.L. Ruoff, C.O. Rodriguez, and N.E. Christensen, Phys. Rev. B 58, 2998 (1998).

[13] Y. Wang, D.Q. Chen, and X.W. Zhang, Phys. Rev. Lett. 84, 3220 (2000).

[14] A. Debernardi, M. Alouani, and H. Dreysse, Phys. Rev. B 63, 064305 (2001).

[15] C. Bercegeay and S. Bernard, Phys. Rev. B 72, 214101 (2005).

[16] S.K. Xiang, F. Xi, Y. Bi, J.a. Xu, H.Y. Geng, L.C. Cai, and F. Q. Jing, Phys. Rev. B 81, 014301 (2010).

[17] L. Koči, Y. Ma, A.R. Oganov, P. Souvatzis, and R. Ahuja, Phys. Rev. B 77, 214101 (2008).

[18] S. Baroni, P. Giannozzi, and A. Testa, Phys. Rev. Lett. 58, 1861 (1987).

[19] S. Baroni, S.D. Gironcoli, A.D. Corso, and P. Giannozzi, Rev. Mod. Phys. 73, 515 (2001).

[20] S. Baroni, A.D. Corso, S. de Gironcoli, P. Giannozzi, C. Cavazzoni, G. Ballabio, S. Scandolo, G. Chiarotti, P. Focher, A. Pasquarello, K. Laasonen, A. Trave, R. Car, N. Marzari, and A. Kokalj. http://www.pwscf.org.

[21] J.P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[22] D. Vanderbilt, Phys. Rev. B 41, 7892 (1990).

[23] H.J. Monkhorst and J.D. Pack, Phys. Rev. B 13, 5188 (1976).

[24] F. Birch, J. Geophys. Res. 91, 4949 (1986).

[25] R. Hill, Proc. Phys. Soc. Lond. 65, 350 (1952).

[26] S.H. Chen and B.N. Brockhouse. Solid State Commun. 2, 73 (1964).

[27] Z.L. Liu, L.C. Cai, X.R. Chen, Q. Wu, and F.Q. Jing, J. Phys.: Condens. Matter 21, 095408 (2009).

[28] F. Luo, L.C. Cai, X.R. Chen, F.Q. Jing, and D. Alfe, J. Appl. Phys. 111, 053503 (2012).

[29] Y.S. Touloukian, R.K. Kirby, R.E. Taylor, and P.D. Desai, Thermal Expansion: Metallic Elements and Alloys (Plenum Press, New York, 1975).

[30] R. Lowrie and A.M. Gonas, J. Appl. Phys. 36, 2189 (1965).

[31] I. Barin, Thermochemical Data of Pure Substances (VCH Verlagsgesellschaft mbH, Weinheim, 1989).