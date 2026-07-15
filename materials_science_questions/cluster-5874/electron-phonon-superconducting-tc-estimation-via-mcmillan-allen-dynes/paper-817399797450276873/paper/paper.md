PHYSICAL REVIEW B 101, 214501 (2020)

# Isotope effect in superconducting lanthanum hydride under high compression

Artur P. Durajski, $^{1,*}$ Radosław Szcześniak, $^{1}$ Yinwei Li, $^{2}$ Chongze Wang, $^{3}$ and Jun-Hyung Cho $^{3,\dagger}$

$^{1}$ Institute of Physics, Częstochowa University of Technology, Ave. Armii Krajowej 19, 42-200 Częstochowa, Poland
$^{2}$ Laboratory of Quantum Materials Design and Application, School of Physics and Electronic Engineering, Jiangsu Normal University, Xuzhou 221116, China
$^{3}$ Department of Physics, Research Institute for Natural Science, and HYU-HPSTAR-CIS High Pressure Research Center, Hanyang University, 222 Wangsimni-ro, Seongdong-Ku, Seoul 04763, Republic of Korea

![](./images/817399797450276873_1.jpg)
(Received 10 December 2019; revised manuscript received 12 May 2020; accepted 14 May 2020; published 1 June 2020)

Recently, the discovery of room-temperature superconductivity (SC) was experimentally realized in the fcc phase of $LaH_{10}$ under megabar pressure. Specifically, the isotope effect of $T_{c}$ was measured by the replacement of hydrogen (H) with deuterium (D), demonstrating a driving role of phonons in the observed room-temperature SC. Herein, based on the first-principles calculations within the harmonic approximation, we reveal that (i) the identical electron-phonon coupling constants of fcc $LaH_{10}$ and $LaD_{10}$ decrease monotonously with increasing pressure and (ii) the isotope effect of $T_{c}$ is nearly proportional to $M^{-\alpha}$ ($M$: ionic mass) with $\alpha \approx 0.465$, irrespective of pressure. The predicted value of $\alpha$ agrees well with the experimental one ($\alpha=0.46$) measured at around 150 GPa. Thus, our findings provide a theoretical confirmation of the conventional electron-phonon coupling mechanism in a recently discovered room-temperature superconductor of compressed $LaH_{10}$.

DOI: 10.1103/PhysRevB.101.214501

## I. INTRODUCTION

Ever since the first discovery of superconductivity (SC) in 1911 [1], the realization of room-temperature SC has been the holy grail of physics. Based on the Bardeen-Cooper-Schrieffer (BCS) theory [2], Ashcroft [3] proposed that the metallic hydrogen formed under high pressures over $\sim$400 GPa [4,5] would be an ideal candidate for room-temperature SC. To achieve the metallization of hydrogen lattices at relatively lower pressures attainable in the diamond anvil cells [6,7], many binary hydrides have been theoretically searched [8–18]. Due to the *chemical precompression*, such hydrides can have high superconducting transition temperatures $T_{c}$ at relatively lower pressures. For instance, theoretically predicted [9,19] and then experimentally realized cubic structure of hydrogen sulfide $H_{3}S$ with a crystalline symmetry of the space group $Im\overline{3}m$ exhibits SC with a $T_{c}$ of $\sim$203 K at a pressure of 155 GPa [20,21]. Furthermore, the pairing mechanism of SC in $H_{3}S$ is associated with the conventional electron-phonon interaction because the measurements of $T_{c}$ for $H_{3}S$ and its deuterium counterpart $D_{3}S$ showed a strong isotope effect: i.e., $T_{c}$ of $D_{3}S$ shifts towards a lower temperature [20].

Recently, two experimental groups synthesized a lanthanum hydride $LaH_{10}$ with a clathrate-like structure at megabar pressures and measured a $T_{c}$ between 250 and 260 K at a pressure of $\sim$170 GPa [22,23]. This record of $T_{c}$ is the highest among the so far experimentally available superconducting materials [20,24–26], which will bring a new era of high-$T_{c}$ SC. The x-ray diffraction and optical studies of lanthanum hydrides showed the existence of the fcc lattice at $\sim$170 GPa upon heating to $\sim$1000 K [27], consistent with the earlier predicted metallic fcc phase of $LaH_{10}$ having cages of 32 H atoms surrounding a La atom [11,12,28,29]. To reveal the underlying mechanism of the observed room-temperature SC in fcc $LaH_{10}$, a pronounced isotope shift was measured by the substitution of deuterium for hydrogen, thereby providing a direct evidence of the conventional phonon-mediated pairing mechanism [23]. Based on the relation of $T_{c} \propto M^{-\alpha}$ [30], where $M$ is ionic mass, the isotope coefficient $\alpha$ can be estimated. According to the experimental data of $T_{c}=249$ (180) K for fcc $LaH_{10}$ (fcc $LaD_{10}$) at a pressure of $\sim$150 GPa [23], the estimated value of $\alpha$ amounts to 0.46, close to that ($\alpha \approx 0.5$) obtained from the BCS theory [2].

In this paper, using first-principles density-functional theory (DFT) calculations within the harmonic approximation, we investigate the isotope effect of fcc $LaH_{10}$ and fcc $LaD_{10}$ as a function of pressure. We find that the electron-phonon coupling (EPC) constant $\lambda$, which is invariant with respect to the H isotope substitution, decreases with increasing pressure as 2.38, 1.82 and 1.54 at 250, 300, and 350 GPa, respectively. By solving the Eliashberg equations, $T_{c}$ of $LaH_{10}$ ($LaD_{10}$) decreases almost linearly as 234 (169), 214 (155), 195 (142) K at 250, 300, and 350 GPa, respectively. As a result, the isotope coefficient is estimated to be $\sim$0.465, irrespective of pressure. This estimated value is in good agreement with the experimental measurement [23] of $\alpha=0.46$ at around 150 GPa. Therefore, our first-principles calculations strongly support a conventional electron-phonon coupling mechanism in the observed room-temperature SC of fcc $LaH_{10}$.

*adurajski@wip.pcz.pl
†chojh@hanyang.ac.kr

2469-9950/2020/101(21)/214501(6)
214501-1
©2020 American Physical Society

## II. THEORETICAL MODEL AND COMPUTATIONAL METHODS

All the numerical calculations were performed using the DFT as implemented in the QUANTUM ESPRESSO software package [31,32]. The ultrasoft pseudopotentials were used for all atoms and the exchange-correlation energy was described by the Perde-Burke-Ernzerhof (PBE) functional based on the generalized gradient approximation (GGA). To obtain the optimized geometry of lanthanum hydride systems at high pressure, the atomic positions and cell vectors were fully relaxed by using the Broyden-Fletcher-Goldfarb-Shanno (BFGS) quasi-Newton algorithm [33] up to the convergence criteria of less than $10^{-10}$ Ry and $10^{-8}$ kbar for total energy and pressure, respectively. On the basis of convergence tests, the kinetic energy cutoff for the wave functions and charge density were taken as 80 and 1000 Ry, respectively. For self-consistent calculations, the $24 \times 24 \times 24$ $k$-point meshes were used. Phonon spectra and electron-phonon interactions were calculated using the density functional perturbation theory [34]. Here, the first Brillouin zone was sampled using the $6 \times 6 \times 6$ $q$-point meshes and the denser $36 \times 36 \times 36$ $k$-point meshes, respectively.

The thermodynamic properties of superconducting states in compressed $\text{LaH}_{10}$ and $\text{LaD}_{10}$ were obtained by solving the isotropic Eliashberg equations with the superconducting order parameter function $\varphi_n = \varphi(i\omega_n)$ and the electron mass renormalization function $Z_n = Z(i\omega_n)$. The set of isotropic Eliashberg equations defined on the imaginary-frequency axis gives the following forms [35,36]:

$$
\varphi_n = \frac{\pi}{\beta} \sum_{m=-M_f}^{M_f} \frac{\lambda_{n,m} - \mu^{\star}\theta(\omega_c - |\omega_m|)}{\sqrt{\omega_m^2 Z_m^2 + \varphi_m^2}} \varphi_m, \tag{1}
$$

$$
Z_n = 1 + \frac{1}{\omega_n} \frac{\pi}{\beta} \sum_{m=-M_f}^{M_f} \frac{\lambda_{n,m}}{\sqrt{\omega_m^2 Z_m^2 + \varphi_m^2}} \omega_m Z_m, \tag{2}
$$

where the electron-phonon interaction pairing kernel is given by

$$
\lambda_{n,m} = 2 \int_{0}^{\infty} d\omega \frac{\omega}{(\omega_n - \omega_m)^2 + \omega^2} \alpha^2 F(\omega). \tag{3}
$$

Hence, the superconducting order parameter is defined by the ratio $\Delta_n = \varphi_n/Z_n$. The effective screened Coulomb repulsion constant $\mu^{\star}$ was chosen in the range of 0.1-0.2, which can be adjusted with the comparison of the measured $T_c$ [37,38]. The Heaviside step function $\theta$ is determined by a frequency cutoff $\omega_c = 3$ eV, which is typically ten times larger than the maximum phonon frequency. The value of $\beta$ is given by $\beta = 1/k_B T$, where $k_B$ is the Boltzmann constant. The Eliashberg spectral function $\alpha^2 F(\omega)$, which is the main input element to the Eliashberg equations, is defined as

$$
\alpha^2 F(\omega) = \frac{1}{2\pi N(\varepsilon_F)} \sum_{\mathbf{q}\mathbf{v}} \delta(\omega - \omega_{\mathbf{q}\mathbf{v}}) \frac{\gamma_{\mathbf{q}\mathbf{v}}}{\hbar \omega_{\mathbf{q}\mathbf{v}}}, \tag{4}
$$

with

$$
\begin{aligned}
\gamma_{\mathbf{q}\mathbf{v}} &= 2\pi \omega_{\mathbf{q}\mathbf{v}} \sum_{ij} \int \frac{d^3 k}{\Omega_{BZ}} |g_{\mathbf{q}\mathbf{v}}(\mathbf{k}, i, j)|^2 \delta(\epsilon_{\mathbf{q},i} - \epsilon_F) \\
&\quad \times \delta(\epsilon_{\mathbf{k+q},j} - \epsilon_F), \tag{5}
\end{aligned}
$$

where $N(\varepsilon_F)$, $\gamma_{\mathbf{q}\mathbf{v}}$, and $g_{\mathbf{q}\mathbf{v}}(\mathbf{k}, i, j)$ are the density of states at the Fermi energy $\varepsilon_F$, the phonon linewidth, and the electron-phonon matrix element, respectively. The integrated EPC constant $\lambda(\omega)$ is obtained by the integration of $\alpha^2 F(\omega)$:

$$
\lambda(\omega) = 2 \int_{0}^{\omega} d\omega' \alpha^2 F(\omega')/\omega', \tag{6}
$$

where the total EPC constant is calculated as $\lambda(\omega \to \infty)$.

The Eliashberg equations are solved iteratively in a self-consistent way with a maximal error of $10^{-10}$ between two successive iterations. The convergence and precision are controlled by using the sufficiently high number $(M_f = 1100)$ of Matsubara frequencies: $\omega_n = (\pi/\beta)(2n - 1)$, where $n = 0, \pm 1, \pm 2, \dots, \pm M_f$. For further details about the implementation and derivation of the methods adopted herein, see Refs. [39-42].

## III. RESULTS AND DISCUSSION

We first determine the geometry of the $Fm\overline{3}m$ $\text{LaH}_{10}$ phase in the pressure range of 250-350 GPa using the first-principles DFT calculations. Here we consider three different pressures 250, 300, and 350 GPa, because the experimentally observed fcc $\text{LaH}_{10}$ phase becomes unstable at lower pressures below 220 GPa (see Fig. S1 in the Supplemental Material [43]). The calculated pressure-volume data show the nearly linear reduction of volume with a slope of $dV/dp = -0.029$ $\text{\AA}^3$/GPa, where we obtain 28.484, 26.891, and 25.564 $\text{\AA}^3$ at 250, 300, and 350 GPa, respectively. Figure 1(a) compares the calculated electronic band structures of fcc $\text{LaH}_{10}$ at 250, 300, and 350 GPa, whereas their corresponding densities of states around $\varepsilon_F$ are displayed in Fig. 1(b). It is seen that the dispersions of the bands around $\varepsilon_F$ change very little with respect to pressure. Consequently, the pressure dependence of the density of states (DOS) at $\varepsilon_F$ is minor, compared to those at the energy regions away from the $\varepsilon_F$. The present results of electronic band structure and DOS with respect to pressure agree well with those obtained using the Vienna ab initio simulation package with the projector augmented-wave method [44]. As shown in Fig. 1(b), the DOS at $\varepsilon_F$ reaches 0.83-0.86 states/eV in the range of 250-350 GPa, which are comparable with that (0.63-0.90 states/eV) of compressed $\text{H}_3\text{S}$ having a $T_c$ of $\sim$203 K at 155 GPa [45,46]. It is thus likely that both compressed $\text{LaH}_{10}$ and $\text{H}_3\text{S}$ with high DOS at $\varepsilon_F$ would be equally expected to have high-$T_c$ SC, as observed by experiments [20-23]. We note that the electronic band structure of fcc $\text{LaD}_{10}$ is identical to that of fcc $\text{LaH}_{10}$ because of the same Kohn-Sham effective potentials in both systems.

Figures 2(a), 2(b), and 2(c) display the calculated phonon dispersions of fcc $\text{LaH}_{10}$ at 250, 300, and 350 GPa, respectively, together with the overlap of the corresponding results for fcc $\text{LaD}_{10}$. For each structure, there are no imaginary phonon frequencies, indicating that fcc $\text{LaH}_{10}$ and $\text{LaD}_{10}$ are dynamically stable in the pressure range between 250 and 350 GPa. In Fig. 2(d), we plot the phonon DOS projected onto La and H atoms at 250 and 350 GPa. We find that the acoustic phonon modes with lower frequencies below $\sim$45 meV arise from La atoms, which are well separated from the optical phonon modes of H or D atoms. It is noticeable that

![](./images/817399797450276873_2.jpg)

FIG. 1. Calculated electronic band structures of fcc LaH₁₀ at 250, 300, and 350 GPa: (a) The electronic dispersion along the high-symmetry lines in the Brillouin zone and (b) the total DOS per formula unit. The Fermi level $\epsilon_{F}$ is set to zero. The inset of (b) shows the Brillouin zone for cubic (fcc) clathrate-type structure with special $k$-point paths.

the D-derived optical phonon modes shift towards lower frequencies, relative to the corresponding H-derived modes. For instance, at 250, 300, and 350 GPa, the lowest optical modes at the $\Gamma$ point shift from 109.44, 118.36, and 123.12 meV in LaH₁₀ to 77.52, 83.44, and 86.93 meV in LaD₁₀, respectively. Thus, we can say that the frequencies of the H- and D-derived optical phonon modes are nearly inversely proportional to the square root of the ionic mass, as discussed below.

Figure 3 shows the results of Eliashberg function $\alpha^{2}F(\omega)$ and integrated EPC constant $\lambda(\omega)$ as a function of phonon frequency, calculated at 250, 300, and 350 GPa. We find that the La-derived acoustical phonon modes contribute to only about 11% of the total $\lambda$. This result indicates that H atoms play a dominant role in contributing to electron-phonon coupling, which in turn gives rise to a room-temperature SC in fcc LaH₁₀. The calculated total $\lambda$ values of LaH₁₀ and LaD₁₀ are equally as 2.38, 1.82 and 1.54 at 250, 300, and 350 GPa, respectively. Interestingly, as pressure increases, the total $\lambda$ decreases monotonously, consistent with the decrease of $T_{c}$ measured by a recent experiment of fcc LaH₁₀ [23]. Because of such large EPC constants larger than 1, we adopt the Eliashberg theory to understand the properties of the superconducting state through the conventional EPC mechanism.

We calculate the temperature dependence of the superconducting energy gap $\Delta$ by solving the Eliashberg equations on the imaginary- and real-frequency axes [36]. Figure 4 shows the calculated $\Delta$ versus temperature curves at 250, 300, and 350 GPa, together with the real and imaginary parts of $\Delta(\omega,T=0)$ as a function of frequency. Based on these data, we estimate $T_{c}$, $\Delta(0)$, and the universal dimensionless ratio $2\Delta(0)/k_{B}T_{c}$, all of which are influenced by pressure and the Coulomb pseudopotential $\mu^{\star}$ [47]. The results are listed in Table I. We find that at 250 GPa, $T_{c}$ is estimated as high as

![](./images/817399797450276873_3.jpg)

FIG. 2. Calculated phonon dispersions of fcc LaH₁₀ and fcc LaD₁₀ at (a) 250, (b) 300, and (c) 350 GPa. (d) Projected phonon density of states (PhDOS) onto La (red-color region) and H/D (gray-color region) atoms at 250 and 350 GPa.

![](./images/817399797450276873_4.jpg)

FIG. 3. Calculated Eliashberg spectral functions $\alpha^{2}F(\omega)$ of fcc LaH₁₀ and LaD₁₀ at 250, 300, and 350 GPa, together with the corresponding integrated EPC constant $\lambda(\omega)$.

![](./images/817399797450276873_5.jpg)

FIG. 4. Real and imaginary parts of the superconducting energy gap as a function of frequency at zero temperature and $\mu^{\star}=0.15$ (left panel), and the corresponding superconducting energy gap as a function of temperature and Coulomb pseudopotential (right panel) determined from the relation $\Delta(T)=\operatorname{Re}[\Delta(\omega=\Delta(T), T)]$.

269 and 191 K for $\mathrm{LaH}_{10}$ and $\mathrm{LaD}_{10}$, respectively. Further, $T_{c}$ is found to decrease almost linearly with increasing pressure, reaching 237 K for $\mathrm{LaH}_{10}$ and 170 K for $\mathrm{LaD}_{10}$ at 350 GPa. As shown in Table I, the larger value of $\lambda$, the higher is the $2 \Delta(0) / k_{B} T_{C}$ ratio. Moreover, $2 \Delta(0) / k_{B} T_{C}$ considerably exceeds the universal value of 3.53 predicted by the BCS theory [2], which reflects the strong EPC and retardation effects in fcc $\mathrm{LaH}_{10}$ and $\mathrm{LaD}_{10}$.

In Fig. 5, we compare the calculated $T_{c}$ versus pressure results with the experimental data. In the case of $\mathrm{LaH}_{10}$, the open black circles represent the experimentally observed

<table>
<caption>TABLE I. Calculated EPC constant $\lambda$, $T_{c}$, $\Delta(0)$, and dimensionless ratio $2 \Delta(0)/k_{B}T_{C}$ of fcc $\mathrm{LaH}_{10}$ and $\mathrm{LaD}_{10}$ at 250, 300, and 350 GPa.</caption>
<thead>
<tr>
<th rowspan="2">$p$ (GPa)</th>
<th rowspan="2">$\mu^{\star}$</th>
<th rowspan="2">$\lambda$</th>
<th colspan="2">$T_{c}$ (K)</th>
<th colspan="2">$\Delta(0)$ (meV)</th>
<th colspan="2">$2\Delta(0)/k_{B}T_{C}$</th>
</tr>
<tr>
<th>$\mathrm{LaH}_{10}$</th>
<th>$\mathrm{LaD}_{10}$</th>
<th>$\mathrm{LaH}_{10}$</th>
<th>$\mathrm{LaD}_{10}$</th>
<th>$\mathrm{LaH}_{10}$</th>
<th>$\mathrm{LaD}_{10}$</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">250</td>
<td>0.10</td>
<td rowspan="3">2.38</td>
<td>269</td>
<td>191</td>
<td>59.74</td>
<td>42.80</td>
<td>5.15</td>
<td>5.20</td>
</tr>
<tr>
<td>0.15</td>
<td>249</td>
<td>179</td>
<td>54.71</td>
<td>39.44</td>
<td>5.10</td>
<td>5.11</td>
</tr>
<tr>
<td>0.20</td>
<td>234</td>
<td>169</td>
<td>50.79</td>
<td>36.85</td>
<td>5.04</td>
<td>5.06</td>
</tr>
<tr>
<td rowspan="3">300</td>
<td>0.10</td>
<td rowspan="3">1.82</td>
<td>252</td>
<td>180</td>
<td>51.42</td>
<td>36.94</td>
<td>4.74</td>
<td>4.76</td>
</tr>
<tr>
<td>0.15</td>
<td>231</td>
<td>166</td>
<td>46.30</td>
<td>33.52</td>
<td>4.65</td>
<td>4.69</td>
</tr>
<tr>
<td>0.20</td>
<td>214</td>
<td>155</td>
<td>42.33</td>
<td>30.90</td>
<td>4.59</td>
<td>4.63</td>
</tr>
<tr>
<td rowspan="3">350</td>
<td>0.10</td>
<td rowspan="3">1.54</td>
<td>237</td>
<td>170</td>
<td>45.71</td>
<td>32.95</td>
<td>4.48</td>
<td>4.50</td>
</tr>
<tr>
<td>0.15</td>
<td>214</td>
<td>154</td>
<td>40.55</td>
<td>29.49</td>
<td>4.40</td>
<td>4.44</td>
</tr>
<tr>
<td>0.20</td>
<td>195</td>
<td>142</td>
<td>36.56</td>
<td>26.85</td>
<td>4.35</td>
<td>4.39</td>
</tr>
</tbody>
</table>

![](./images/817399797450276873_6.jpg)

FIG. 5. Estimated $T_{c}$ as a function of pressure using the Eliashberg theory with $\mu^{\star}=0.1,0.15,0.2$. The experimental data [23] are also given for comparison.

$T_{c}$ [23]. Due to the difficulty in the synthesis of fcc $\mathrm{LaD}_{10}$, there was only one experimental data of $T_{c}$ measured at 150 GPa (see the red open circle in Fig. 5) [23]. It is noteworthy that for $\mathrm{LaH}_{10}$, the estimated $T_{c}$ decreases almost linearly with increasing pressure, irrespective of the chosen $\mu^{\star}$ values of $0.1,0.15$, and 0.2. This linear variation of $T_{c}$ with respect to pressure seems to be consistent with the experimental data. Interestingly, we emphasize that $\mathrm{H}_{3} \mathrm{~S}$ and $\mathrm{H}_{3} \mathrm{~S}_{1-x} \mathrm{P}_{x}$ mixture [48,49] also exhibited similar behavior of $T_{c}$ decrease with increasing pressure between 150 and 350 GPa. As shown in Fig. 5, the calculated $T_{c}$ versus pressure relation with $\mu^{\star}=$ 0.2 is in better agreement with the measurements (see the black dashed line). For $\mathrm{LaD}_{10}$, there was only one experimental datum at 150 GPa, which can be well extrapolated by our results obtained using $\mu^{\star}=0.2$ (see the red dashed line in Fig. 5). It is noted that the experimental values of $T_{c}$ are well reproduced by the present harmonic approximation with $\mu^{\star}=0.2$, larger than that $(\mu^{\star}=0.1)$ of a recent anharmonic calculation [50]. It is thus likely that the proper $\mu^{\star}$ value for $\mathrm{LaH}_{10}$ would change with including anharmonic phonons. The present theory and previous experimental data showing that $T_{c}$ varies with the isotopic mass provide a strong evidence for the interaction between the electrons and lattice vibrations [51-53]. Indeed, this conventional electron-phonon coupling mechanism contrasts with the recent proposal that $\mathrm{LaH}_{10}$ is an unconventional superconductor [54]. We further analyze the isotope effect of $T_{c}$ in terms of the isotope coefficient $(\alpha)$, which is given by the following relation:

$$
\alpha=-\frac{\ln \left[T_{C}\right]_{\mathrm{LaD}_{10}}-\ln \left[T_{C}\right]_{\mathrm{LaH}_{10}}}{\ln [M]_{\mathrm{D}}-\ln [M]_{\mathrm{H}}}. \tag{7}
$$

Here $[M]_{\mathrm{H}}$ and $[M]_{\mathrm{D}}$ are the atomic mass of hydrogen and deuterium, respectively. It is noteworthy that the BCS theory for weak-coupling superconductors gives a $\alpha$ value of 0.5, while the McMillan-Allen-Dynes or Migdal-Eliashberg equations with harmonic phonons have predicted $\alpha$ values lower than 0.5 for strong-coupling superconductors: e.g.,

<table>
<caption>TABLE II. Estimated $T_c$ with $\mu^\ast=0.2$, the isotope effect coefficient $\alpha$, and the average isotope effect coefficient $\overline{\alpha}$ of fcc LaH$_{10}$ and LaD$_{10}$ at 250, 300, and 350 GPa.</caption>
<tbody>
<tr>
<td rowspan="2">Pressure (GPa)</td>
<td colspan="2">$T_c$ (K)</td>
<td rowspan="2">$\alpha$</td>
<td rowspan="2">$\overline{\alpha}$</td>
</tr>
<tr>
<td>LaH$_{10}$</td>
<td>LaD$_{10}$</td>
</tr>
<tr>
<td>250</td>
<td>234</td>
<td>169</td>
<td>0.470</td>
<td rowspan="3">0.465</td>
</tr>
<tr>
<td>300</td>
<td>214</td>
<td>155</td>
<td>0.466</td>
</tr>
<tr>
<td>350</td>
<td>195</td>
<td>142</td>
<td>0.458</td>
</tr>
</tbody>
</table>

0.23–0.31 (0.38–0.42) for H$_2$S (H$_3$S) from McMillan-Allen-Dyne formula [51] and 0.31 for H$_3$S from Migdal-Eliashberg equations [55].

As shown in Table II, the $\alpha$ value ranges between 0.458 and 0.470, which are smaller than the BCS value which indicate the correction due to the strong coupling and retardation effects. Moreover, on the basis of only one available experimental data of $T_c$ for LaH$_{10}$ (249 K) and LaD$_{10}$ (180 K) at a pressure of $\sim$150 GPa, the $\alpha$ value can be estimated as 0.46, in good agreement with our estimated average isotope effect coefficient $\overline{\alpha}=0.465$. We note that the present value of $\alpha$ estimated at higher pressures between 250 and 350 GPa agrees well with the previous theoretical value (0.43 at $\sim$160 GPa) obtained using anharmonic phonons [50]. It is thus likely that LaH$_{10}$ exhibits insignificant anharmonic effects for $\alpha$.

It is noteworthy that a recent anisotropic Migdal-Eliashberg theory with including anharmonic effect predicted $T_c$ at pressures lower than 260 GPa in the $F\overline{m}3m$ structure [50]. As shown in Fig. S2(a) of the Supplemental Material [43], the predicted $T_c$ versus pressure results [50] agree well with the experimental data [23] measured between 150 and 210 GPa. Here the theoretical values of $T_c$ decrease by $\sim$21 K between 214 and 264 GPa, close to a slope of $\sim$15 K per 50 GPa between 250 and 350 GPa (see Fig. 5 or Fig. S2(b) in the Supplemental Material [43]) which is obtained using isotropic Migdal-Eliashberg equations with $\mu^\ast=0.2$ and harmonic phonons. It is thus likely that the pressure dependence of $T_c$ at high pressures above 220 GPa shows good agreement between the previous anharmonic [50] and the present harmonic calculations. We note that the present isotope coefficient of 0.465 estimated at higher pressures between 250 and 350 GPa agree well with the previous theoretical value (0.43 at $\sim$160 GPa) obtained using anharmonic phonons [50] as well as the existing experimental data ($\alpha=0.46$) measured only at a pressure of $\sim$150 GPa [23]. This agreement of $\alpha$ between the previous anharmonic [50] and the present harmonic calculations is due to the fact that the two calculations predict similar $T_c$ versus pressure results for LaH$_{10}$ and LaD$_{10}$, as shown in Figs. S2(a) and S2(b) of the Supplemental Material [43]. Our findings not only support a conventional electron-phonon coupling mechanism in the superconductivity of fcc LaH$_{10}$, but also will stimulate further experiments to explore the isotope effect of $T_c$ at higher pressures.

## IV. CONCLUSION

We performed the comprehensive first-principles DFT calculations of the electronic and phonon properties of lanthanum hydride and deuteride at high pressures. We found that fcc LaH$_{10}$ and LaD$_{10}$ phases not only dynamically stabilize in the range of 250–350 GPa, but also have the strong EPC and the high DOS at the Fermi level which are favorable for high-$T_c$ SC. By solving the Eliashberg equations, $T_c$ of LaH$_{10}$ (LaD$_{10}$) decreases almost linearly as 234 (169), 214 (155), 195 (142) K at 250, 300, and 350 GPa, respectively. As a result, the isotope coefficient is estimated to be $\sim$0.465, irrespective of pressure. Therefore, our findings strongly support a conventional electron-phonon coupling mechanism in the observed room-temperature superconductivity of fcc LaH$_{10}$. We believe that these results are of importance for understanding the phenomenon of the superconducting state in fcc LaH$_{10}$, which will be useful for future, more experimental measurements of the isotope effect.

## ACKNOWLEDGMENTS

A.P.D. acknowledges the financial support from the Polish National Science Centre (NCN) under Grant No. 2016/23/D/ST3/02109 and from the Polish Ministry of Science and Higher Education under the scholarship for young outstanding scientists No. 406/STYP/13/2018. J.-H.C. acknowledges the National Research Foundation of Korea (NRF) grant funded by the Korean Government (Grants No. 2019R1A2C1002975, No. 2016K1A4A3914691, and No. 2015M3D1A1070609). Y.L. acknowledges funding from the National Natural Science Foundation of China under Grant No. 11722433, the Six Talent Peaks Project of Jiangsu Province.

[1] H. K. Onnes, Comm. Phys. Lab. Univ. Leiden 122, 124 (1911).

[2] J. Bardeen, L. N. Cooper, and J. R. Schrieffer, Phys. Rev. 106, 162 (1957).

[3] N. W. Ashcroft, Phys. Rev. Lett. 21, 1748 (1968).

[4] J. McMinis, R. C. Clay, D. Lee, and M. A. Morales, Phys. Rev. Lett. 114, 105305 (2015).

[5] J. M. McMahon, M. A. Morales, C. Pierleoni, and D. M. Ceperley, Rev. Mod. Phys. 84, 1607 (2012).

[6] W. A. Bassett, High Press. Res. 29, 163 (2009).

[7] H.-K. Mao, X.-J. Chen, Y. Ding, B. Li, and L. Wang, Rev. Mod. Phys. 90, 015007 (2018).

[8] H. Wang, J. S. Tse, K. Tanaka, T. Iitaka, and Y. Ma, Proc. Natl. Acad. Sci. USA 109, 6463 (2012).

[9] D. Duan, Y. Liu, F. Tian, D. Li, X. Huang, Z. Zhao, H. Yu, B. Liu, W. Tian, and T. Cui, Sci. Rep. 4, 6968 (2014).

[10] X. Feng, J. Zhang, G. Gao, H. Liu, and H. Wang, RSC Adv. 5, 59292 (2015).

[11] F. Peng, Y. Sun, C. J. Pickard, R. J. Needs, Q. Wu, and Y. Ma, Phys. Rev. Lett. 119, 107001 (2017).

[12] H. Liu, I. I. Naumov, R. Hoffmann, N. W. Ashcroft, and R. J. Hemley, Proc. Natl. Acad. Sci. USA 114, 6990 (2017).

[13] E. Zurek and T. Bi, J. Chem. Phys. 150, 050901 (2019).

214501-5

[14] J. A. Flores-Livas, L. Boeri, A. Sanna, G. Profeta, R. Arita, and M. Eremets, *Phys. Rep.* **856**, 1 (2020).

[15] Y. Li, J. Hao, H. Liu, J. S. Tse, Y. Wang, and Y. Ma, *Sci. Rep.* **5**, 9948 (2015).

[16] Y. Li, L. Wang, H. Liu, Y. Zhang, J. Hao, C. J. Pickard, J. R. Nelson, R. J. Needs, W. Li, Y. Huang, I. Errea, M. Calandra, F. Mauri, and Y. Ma, *Phys. Rev. B* **93**, 020103(R) (2016).

[17] Y. Quan, S. S. Ghosh, and W. E. Pickett, *Phys. Rev. B* **100**, 184505 (2019).

[18] H. Liu, I. I. Naumov, Z. M. Geballe, M. Somayazulu, J. S. Tse, and R. J. Hemley, *Phys. Rev. B* **98**, 100102(R) (2018).

[19] Y. Li, J. Hao, H. Liu, Y. Li, and Y. Ma, *J. Chem. Phys.* **140**, 174712 (2014).

[20] A. P. Drozdov, M. I. Eremets, I. A. Troyan, V. Ksenofontov, and S. I. Shylin, *Nature* **525**, 73 (2015).

[21] M. Einaga, M. Sakata, T. Ishikawa, K. Shimizu, M. I. Eremets, A. P. Drozdov, I. A. Troyan, N. Hirao, and Y. Ohishi, *Nat. Phys.* **12**, 835 (2016).

[22] M. Somayazulu, M. Ahart, A. K. Mishra, Z. M. Geballe, M. Baldini, Y. Meng, V. V. Struzhkin, and R. J. Hemley, *Phys. Rev. Lett.* **122**, 027001 (2019).

[23] A. P. Drozdov, P. P. Kong, V. S. Minkov, S. P. Besedin, M. A. Kuzovnikov, S. Mozaffari, L. Balicas, F. F. Balakirev, D. E. Graf, V. B. Prakapenka, E. Greenberg, D. A. Knyazev, M. Tkacz, and M. I. Eremets, *Nature* **569**, 528 (2019).

[24] C. M. Pepin, G. Geneste, A. Dewaele, M. Mezouar, and P. Loubeyre, *Science* **357**, 382 (2017).

[25] X. Li, X. Huang, D. Duan, C. J. Pickard, D. Zhou, H. Xie, Q. Zhuang, Y. Huang, Q. Zhou, B. Liu, and T. Cui, *Nat. Commun.* **10**, 3461 (2019).

[26] I. Troyan, D. Semenok, A. Kvashnin, A. Ivanova, V. Prakapenka, E. Greenberg, A. Gavriliuk, I. Lyubutin, V. Struzhkin, and A. Oganov, arXiv:1908.01534.

[27] Z. M. Geballe, H. Liu, A. K. Mishra, M. Ahart, M. Somayazulu, Y. Meng, M. Baldini, and R. J. Hemley, *Angew. Chem. Int. Ed.* **57**, 688 (2018).

[28] I. A. Kruglov, D. V. Semenok, H. Song, R. Szczesniak, I. A. Wrona, R. Akashi, M. M. Davari Esfahani, D. Duan, T. Cui, A. G. Kvashnin, and A. R. Oganov, *Phys. Rev. B* **101**, 024508 (2020).

[29] L. Liu, C. Wang, S. Yi, K. W. Kim, J. Kim, and J.-H. Cho, *Phys. Rev. B* **99**, 140501(R) (2019).

[30] B. Serin, C. A. Reynolds, and L. B. Nesbitt, *Phys. Rev.* **78**, 813 (1950).

[31] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, *J. Phys. Condens. Matter* **21**, 395502 (2009).

[32] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, N. Colonna, I. Carnimeo, A. D. Corso, S. de Gironcoli, P. Delugas, R. A. D. Jr, A. Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F. Giustino, T. Gorni, J. Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Küçükbenli, M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A. O. de-la Roza, L. Paulatto, S. Poncé, D. Rocca, R. Sabatini, B. Santra, M. Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser, P. Umari, N. Vast, X. Wu, and S. Baroni, *J. Phys. Condens. Matter* **29**, 465901 (2017).

[33] S. R. Billeter, A. Curioni, and W. Andreoni, *Comput. Mater. Sci.* **27**, 437 (2003).

[34] S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, *Rev. Mod. Phys.* **73**, 515 (2001).

[35] G. M. Eliashberg, *J. Exp. Theor. Phys.* **11**, 696 (1960).

[36] F. Marsiglio, M. Schossmann, and J. P. Carbotte, *Phys. Rev. B* **37**, 4965 (1988).

[37] A. P. Durajski, *Sci. Rep.* **6**, 38570 (2016).

[38] D. Szczesniak and T. P. Zemla, *Supercond. Sci. Technol.* **28**, 085018 (2015).

[39] R. Szczesniak, *Acta Phys. Pol. A* **109**, 179 (2006).

[40] A. P. Durajski and R. Szczesniak, *J. Chem. Phys.* **149**, 074101 (2018).

[41] B. Wiendlocha, R. Szczesniak, A. P. Durajski, and M. Muras, *Phys. Rev. B* **94**, 134517 (2016).

[42] J. P. Carbotte, E. J. Nicol, and T. Timusk, *Phys. Rev. B* **100**, 094505 (2019).

[43] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.101.214501 for further plots of calculated phonon spectrum of the fcc ${\rm LaH_{10}}$ phase at 210 GPa and superconducting critical temperatures calculated using Migdal-Eliashberg equations with anharmonic phonons.

[44] C. Wang, S. Yi, and J.-H. Cho, *Phys. Rev. B* **100**, 060502(R) (2019).

[45] T. Jarlborg and A. Bianconi, *Sci. Rep.* **6**, 24816 (2016).

[46] Y. Quan and W. E. Pickett, *Phys. Rev. B* **93**, 104526 (2016).

[47] M. Krzyzosiak, R. Gonczarek, A. Gonczarek, and J. L., *Sci. Rep.* **9**, 2181 (2019).

[48] A. P. Durajski and R. Szczesniak, *Sci. Rep.* **7**, 4473 (2017).

[49] A. P. Durajski and R. Szczesniak, *Physica C* **554**, 38 (2018).

[50] I. Errea, F. Belli, L. Monacelli, A. Sanna, T. Koretsune, T. Tadano, R. Bianco, M. Calandra, R. Arita, F. Mauri, and J. A. Flores-Livas, *Nature* **578**, 66 (2020).

[51] R. Akashi, M. Kawamura, S. Tsuneyuki, Y. Nomura, and R. Arita, *Phys. Rev. B* **91**, 224513 (2015).

[52] I. Errea, M. Calandra, C. J. Pickard, J. Nelson, R. J. Needs, Y. Li, H. Liu, Y. Zhang, Y. Ma, and F. Mauri, *Phys. Rev. Lett.* **114**, 157004 (2015).

[53] R. M. Mendez-Moreno, *Adv. Cond. Matter Phys.* **2019**, 6795250 (2019).

[54] E. F. Talantsev, *Mater. Res. Exp.* **6**, 106002 (2019).

[55] R. Szczesniak and A. Durajski, *Solid State Commun.* **249**, 30 (2017).

---

214501-6