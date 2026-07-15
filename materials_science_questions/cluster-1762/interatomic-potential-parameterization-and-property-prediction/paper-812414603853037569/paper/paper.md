![](./images/812414603853037569_1.jpg)

Journal of Nuclear Materials 212-215 (1994) 148-153

![](./images/812414603853037569_2.jpg)

# Molecular dynamics calculations of defect energetics in $\beta$-SiC *

Hanchen Huang, Nasr Ghoniem

Mechanical, Aerospace and Nuclear Engineering Department, University of California, Los Angeles, CA 90024-1597, USA

## Abstract

The molecular dynamics (MD) method is used to calculate defect energetics in $\beta$-silicon carbide. Many-body interaction effects in this covalent material are accounted for by using a hybrid of two-body and three-body potentials. Pearson's potential is modified to accurately fit the sublimation energy of $\beta$-SiC, and interatomic potentials among silicon, carbon, and helium atoms are also developed. A microcrystal is constructed to represent the computational cell, and external forces are applied to its boundaries so that it behaves as a part of an infinite medium. The potential energy for the unperturbed computational cell is first calculated. The cell is then set at a chosen defect configuration and relaxed, and the potential energy of the relaxed cell is computed. The difference between the potential energies of the unperturbed cell and that of the defect-containing cell is used to calculate the formation energies of point defects and defect clusters in SiC. Binding energies, and migration energies of point defects are then deduced. Preexponential factors of point defect diffusion coefficients are derived from the calculated potential energy profile. Activation energies and preexponential factors of thermal diffusion through the vacancy mechanism are compared to corresponding experimental data.

## 1. Introduction

Defect energetics in covalent materials have not yet been studied by the molecular dynamics (MD) simulation technique. Several approximate calculations were performed for vacancy formation energies [1-6] in germanium, diamond, silicon, and silicon carbide. These studies can be classified into two categories. The first one [1-3] employed a Morse-type potential and made several approximations about the relaxation of atoms neighboring a vacancy. One shortcoming of this approach is that it does not fully relax the defected lattice. The second approach [4-6], however, considered the electronic structure of a defected lattice and omitted lattice relaxation. Since a defected lattice does relax, this approach should not be able to give reasonable results. Surprisingly, results of both approaches are in good agreement with experimental data.

In the present numerical simulations, an empirically calibrated potential function given by Pearson et al. [8] is modified to accurately fit experimental sublimation energy of $\beta$-SiC. Many-body effects are taken into account by employing a phenomenological three-body potential. Interatomic potential functions among silicon, carbon, and helium atoms are also developed. Using the constructed potential functions, we study defect energetics in $\beta$-SiC by the molecular dynamics simulation technique. When an atom is put on a crystal's surface, certain amount of energy will be recovered. This effect is taken into account according to Olander's scheme [23].

Nuclear reactor components are affected by neutron irradiation. Changes of their macroscopic properties are determined not only by point defect production rate but also by defect evolution processes. In order to understand defect evolution processes, defect energetics have to be studied first. Generally, there are several possible defect cluster configurations. One factor which determines the defect configuration is its formation energy. Study of defect binding energies can also help us to determine the importance of backward reactions with respect to forward reactions. These results are

* Work supported by the Office of Fusion Energy, US DOE under grant DE-FG03-91ER54115.

0022-3115/94/$07.00 © 1994 Elsevier Science B.V. All rights reserved
SSDI 0022-3115(94)00124-7

critical to defect clustering processes to be studied later.

## 2. MD simulation

The molecular dynamics simulation method is well established. Calibrating interatomic potential functions and constructing a representative computational cell are generally the two most important considerations when the MD simulation technique is applied to a variety of problems.

### 2.1. Interatomic potentials in silicon carbide

Two-body potentials have been widely used for metals (e.g., Ref. [9]). When one considers a covalent material (e.g., SiC), directional dependent interactions become important. A many-body potential appropriate for this purpose has been developed by Born and Oppenheimer [7], and is given in the form

$$
\begin{aligned}
\Phi_{i}(& \boldsymbol{r}_{1}, \boldsymbol{r}_{2}, \cdots, \boldsymbol{r}_{n}) \\
& =\frac{1}{2!} \sum_{j \neq i} V^{(2)}(\boldsymbol{r}_{i j})+\frac{1}{3!} \sum_{k \neq} \sum_{j \neq i} V^{(3)}(\boldsymbol{r}_{i j}, \boldsymbol{r}_{i k}, \boldsymbol{r}_{j k}) \\
& +\cdots+\frac{1}{n!} \sum_{q \neq} \cdots \sum_{m \neq} \cdots \sum_{j \neq i} V^{(n)} \\
& \times(\boldsymbol{r}_{i j}, \cdots, \boldsymbol{r}_{i q}, \cdots, \boldsymbol{r}_{m q}).
\end{aligned}
$$

To make this many-body potential usable in practice, Pearson et al. [8] truncated the expansion up to the three-body level. For SiC, they combined the Lennard-Jones two-body potential [9] and Axilrod-Teller three-body potential [10] in the form

$$
V^{(2)}\left(\boldsymbol{r}_{i j}\right)=\frac{\varepsilon}{m-n}\left[n\left(\frac{R_{0}}{r_{i j}}\right)^{m}-m\left(\frac{R_{0}}{r_{i j}}\right)^{n}\right],
$$

$$
V^{(3)}\left(\boldsymbol{r}_{i j}, \boldsymbol{r}_{i k}, \boldsymbol{r}_{j k}\right)=Z\left[\frac{1+3 \cos \theta_{i j} \cos \theta_{i k} \cos \theta_{j k}}{\left(r_{i j} r_{i k} r_{j k}\right)^{3}}\right],
$$

where the energy parameters $(\varepsilon, Z)$ and the two-body structure parameters $(m, n, R_{0})$ were adjusted to fit experimental data for bulk solid and atomic clusters (sublimation energies and bond length). A set of potential parameters is given by Pearson et al. [8]. Unfortunately, the calculated Si-C sublimation energy (15.409 eV) with their parameters is at discrepancy with corresponding experimental data (12.865 eV) for $\beta$-SiC. Since defect formation energies are generally on the order of several eV, higher accuracy of the potential function is required. To improve this fit and keep other constants unchanged, we modify the $Z$ parameter for the Si-C-C system. The Si-Si-C and Si-C-C systems are symmetrical with respect to silicon and carbon atoms. Assuming that contribution of a carbon atom to three-body interaction is underestimated, we multiply $Z_{\text{Si-C-C}}$ by a factor $f$ and $Z_{\text{Si-Si-C}}$ by $f/2$. The factor $f$ is adjusted to fit the experimental sublimation energy of $\beta$-SiC. With this simple procedure, we derive the following potential function parameters:
$(m, n)$ value: (12, 6);
$\varepsilon$ value (eV): (Si-Si) = 2.817, (Si-C) = 3.895, (C-C) = 5.437;
$R_{0}$ value (Å): (Si-Si) = 2.2951, (Si-C) = 1.7400, (C-C) = 1.4806;
$Z$ value (eV Å⁹): (Si-Si-Si) = 3484.0, (Si-Si-C) = 796.8, (Si-C-C) = 597.5, (C-C-C) = 167.3.

### 2.2. Interatomic potentials among He, C, and Si atoms

The interaction between closed shell atoms is dominated by a Van der Waals mechanism. Using a perturbation method, Slater et al. [11] calculated interatomic potential function between two helium atoms $(V_{\text{He-He}})$. Their calculated result of polarizability is close to that measured experimentally, and their potential function can be written as

$$
V_{\text{He-He}}=\left(0.91 / r^{6}\right) \mathrm{eV}.
$$

The Van der Waals potential is proportional to the polarizability of participating atoms [21]. Polarizability data for silicon or carbon atom is not available while that for noble gas atoms is available. Since a carbon atom has fewer electrons than a neon atom, it should have a smaller polarizability. On the other hand, a carbon atom has an open electronic structure while a neon atom has a closed shell configuration. A carbon atom should therefore have larger polarizability than a neon atom. As a first order approximation, the polarizability of a carbon atom $(\alpha_{C})$ is taken as equal to that of a neon atom $(\alpha_{\text{Ne}})$. Likewise, the polarizability of a silicon atom $(\alpha_{\text{Si}})$ is taken as equal to that of an argon atom $(\alpha_{\text{Ar}})$.

According to Slater et al. [11], the polarizability of a helium atom $(\alpha_{\text{He}})$, a neon atom $(\alpha_{\text{Ne}})$, and an argon atom $(\alpha_{\text{Ar}})$ are $0.205 \times 10^{-24}, 0.39 \times 10^{-24}$ and $1.65 \times$ $10^{-24} \mathrm{~cm}^{3}$, respectively. The Van der Waals potential between helium and carbon atoms $(V_{\text{He-C}})$ can then be derived from the helium-helium Van der Waals potential and is written as

$$
V_{\text{He-C}}=\left(\alpha_{\mathrm{C}} / \alpha_{\mathrm{He}}\right) V_{\text{He-He}}.
$$

A similar expression holds for the helium-silicon Van der Waals potential $(V_{\text{He-Si}})$. The two-body potential for Si-He or C-He system can be written in the same form as for Si-C system. The equilibrium distance is approximated as the sum of the atomic radii of interacting atoms. When bonds are formed, the atomic

radii of helium, carbon, and silicon atoms are 0.93, 0.77 and 1.11 Å, respectively [12].

Since the three-body Van der Waals potential is also proportional to the polarizability of each participating atom [22], the potential function parameter for Si-Si-He system can be derived from that of silicon and carbon systems, and is written as

$$
Z_{\mathrm{Si}-\mathrm{Si}-\mathrm{He}}=\sqrt{\frac{\alpha_{\mathrm{He}}}{\alpha_{\mathrm{Si}}} Z_{\mathrm{Si}-\mathrm{Si}-\mathrm{Si}} \frac{\alpha_{\mathrm{He}}}{\alpha_{\mathrm{C}}} Z_{\mathrm{Si}-\mathrm{Si}-\mathrm{C}}} \cdot \tag{6}
$$

Similar expressions hold for $Z_{\mathrm{C}-\mathrm{C}-\mathrm{He}}$ and $Z_{\mathrm{Si}-\mathrm{C}-\mathrm{He}}$.
In these expressions, differences in covalent and Van der Waals interactions are not included. A three-body system containing a helium atom is less directionally dependent than that containing silicon and carbon atoms alone. In other words, participation of helium atoms reduces the covalent nature of the three-body system. We found that a reduction of $Z$ by a factor of 2 will give reasonable results (i.e., helium stabilizes a silicon vacancy and has positive interstitial formation energy). The two-body and three-body potential parameters involving a helium atom are summarized as
$(m, n)$ value: (12, 6);
$\varepsilon$ value (eV): (Si-He) = 0.0677, (C-He) = 0.2193;
$R_0$ value (Å): (Si-He) = 2.04, (C-He) = 1.70;
$Z$ value (eV Å$^9$): (Si-Si-He) = 78.3, (Si-C-He) = 32.4, (C-C-He) = 14.9.

### 2.3. Construction of a computational cell

A computational cell consists of inner atoms and boundary atoms. The thickness of boundary layer atoms is larger than the effective range of interactions in the crystal. The boundary consists of a hybrid of fixed and flexible atoms. Due to the cutoff of interatomic interactions, a net force on an atom in a perfect crystal is not zero. External forces are applied to lattice atoms to balance these net forces. A vacancy is created by moving an inner lattice atom to the crystal's surface. A vacancy cluster is created by moving several neighboring atoms to the crystal's surfaces. These atoms are located far away from each other on the surfaces, so that mutual interactions do not take place. An antisite defect is formed by replacing a silicon (or carbon) atom by a carbon (or silicon) atom. A cavity consisting of a vacancy and a helium atom is formed by (1) creating a vacancy, and (2) filling the vacancy by a helium atom. When an extra atom is added to the lattice, an interstitial is formed. Two tetrahedral interstitial configurations are the most favorable, one is that surrounded by four carbon lattice atoms $(T_{\mathrm{C}})$ and the other is that surrounded by four silicon lattice atoms $(T_{\mathrm{Si}})$.

A computer code for solving these coupled equations was developed at UCLA [13]. The standard

![](./images/812414603853037569_3.jpg)

Fig. 1. Relaxation field of lattice atoms around a silicon vacancy, located at center of the cell. Length of the lines corresponds to displacement magnitude of atom relaxation.

Leap-frog numerical method was used in solving the set of coupled differential equations. In the simulation process, a velocity component is quenched to zero whenever it is in the opposite direction to the corresponding acceleration component.

### 2.4. Defect energetics

The potential energy of the computational cell is calculated before any defect is introduced. The computational cell is then set at a defected configuration and the increased potential energy is calculated. Relaxation of the defected lattice results in an energy decrease. The net increase of the potential energy from a perfect configuration to a relaxed defected configuration is the formation energy of the defect. Clustering of two defects usually results in decrease of their total potential energy. This decrease is binding energy of the two defects. The relaxation of lattice atoms surrounding a silicon single vacancy is shown in Fig. 1, where it is clearly shown that the four nearest neighbors of the vacancy undergo the largest displacement from their equilibrium positions. The magnitude of this relaxation decreases rapidly with distance away from the vacancy. Relaxation of nearest neighbors to a silicon vacancy and that of those to a carbon vacancy are compared in Fig. 2. It is observed that the four nearest neighbors of a vacancy tend to form bonds. When a silicon vacancy is created, the four nearest neighbors relax significantly. On the other hand, the nearest neighbors of a carbon vacancy do not relax as much, because of the geometrical asymmetry of silicon and carbon atoms.

When a defect migrates, it must cross a potential barrier. Formation energies of the defect at an equilibrium position $(E^{\mathrm{eq}})$ and a saddle point position $(E^{\mathrm{sad}})$ can be calculated in the same way as for defect formation energies. The migration energy of a defect can then be deduced as the difference of $E^{\mathrm{sad}}$ and $E^{\mathrm{eq}}$.

![](./images/812414603853037569_4.jpg)

Each carbon atom surrounding a silicon vacancy displaces 4.3% of bond length

![](./images/812414603853037569_5.jpg)

Each silicon atom surrounding a carbon vacancy displaces 0.1% of bond length

Fig. 2. Relaxation of the nearest neighbors: (a, top) around a silicon vacancy, (b, bottom) around a carbon vacancy. The larger spheres are silicon atoms and the smaller ones are carbon atoms.

It is found that $T_C$ is energetically the most favorable interstitial position. The most favorable path of interstitial migration is $T_C \Rightarrow T_{Si} \Rightarrow (\text{another } T_C)$. The most favorable path for a silicon vacancy $(V_{Si})$ is $V_{Si} \Rightarrow T_{Si} \Rightarrow (\text{nearest silicon lattice})$. Similarly, a carbon vacancy migrates through a $T_C$. If we assume that the potential profile along the migration path, $E(x)$, can be approximated by a parabola, the Debye frequency $(\nu)$ and diffusion coefficient $(D)$ of the defect can be calculated as [23]

$$
\nu = \frac{1}{2\pi} \left[ \frac{1}{m} \left( \frac{\mathrm{d}^2 E}{\mathrm{d} x^2} \right)_{x=x_{\mathrm{eq}}} \right]^{1/2}, \tag{7}
$$

$$
D = \frac{1}{6} \lambda^2 \delta \nu \ \mathrm{e}^{-E^{\mathrm{mig}} / kT}, \tag{8}
$$

where $\lambda = (\sqrt{2}/2)a_0$ is jump distance and $\delta = 12$ is number of the nearest identical neighbors for the jumping atom or defect. $a_0$ is the lattice constant.

For SiC, thermal diffusion data has been documented by Ghoshtagore et al. [14], Hong et al. [15,16] and Hon et al. [17,18]. A vacancy diffusion mechanism is strongly suggested by the experimental data [14-18]. It is found that acceptor dopants always occupy Si-sites [19,20]. Hong et al. [15,16] found that n-doping increases Si diffusivity and decreases C diffusivity. These results imply that Si atom diffuses through Si vacancies while C atom diffuses through C vacancies. Based on these experimental evidences, we can take the measured activation energy as the sum of vacancy formation energy and vacancy migration energy. The preexponential factors for self-diffusion will therefore correspond to those of vacancy diffusion coefficients.

### 3. Results and conclusions

The calculated defect energetics data for point defects are summarized in Table 1 and those for extended defects are summarized in Table 2. From the calculated results, several salient conclusions can be made:

(1) A silicon atom can be spontaneously replaced by a carbon atom from the energy point of view. This

<table>
<caption>Table 1 Energetics of points defects in SiC</caption>
<thead>
<tr>
<th>Species</th>
<th colspan="3">Calculated</th>
<th colspan="2">Experimental</th>
</tr>
<tr>
<th></th>
<th>Formation<br>$E^\text{f}$ (eV)</th>
<th>Migration<br>$E^\text{m}$ (eV)</th>
<th>Diffusion<br>$D_0$ ($\text{cm}^2/\text{s}$)</th>
<th>$E^\text{f} + E^\text{m}$<br>(eV)</th>
<th>Diffusion<br>$D_0$ ($\text{cm}^2/\text{s}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Si interstitial ($T_C$)</td>
<td>6.48</td>
<td>6.04</td>
<td>$1.09 \times 10^{-2}$</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>Si interstitial ($T_{Si}$)</td>
<td>13.80</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>C interstitial ($T_C$)</td>
<td>6.00</td>
<td>1.47</td>
<td>$1.31 \times 10^{-2}$</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>C interstitial ($T_{Si}$)</td>
<td>6.43</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>He interstitial ($T_C$)</td>
<td>0.70</td>
<td>0.68</td>
<td>$1.38 \times 10^{-2}$</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>He interstitial ($T_{Si}$)</td>
<td>1.07</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>Si vacancy</td>
<td>3.25</td>
<td>7.39</td>
<td>$1.10 \times 10^{-2}$</td>
<td>9.5</td>
<td>$8.4 \times 10^7$</td>
</tr>
<tr>
<td>C vacancy</td>
<td>2.63</td>
<td>6.10</td>
<td>$1.51 \times 10^{-2}$</td>
<td>8.7</td>
<td>$2.6 \times 10^8$</td>
</tr>
<tr>
<td>Antisite Si replaces C</td>
<td>3.66</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>Antisite C replaces Si</td>
<td>$-3.33$</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<table><thead><tr><th rowspan="2">Species</th><th colspan="2">Calculated</th><th rowspan="2">Configuration</th></tr><tr><th>Formation $E^{\mathrm{f}}$ (eV)</th><th>Binding of last defect (eV)</th></tr></thead><tbody><tr><td>He + vacancy (He replaces Si)</td><td>3.06</td><td>-- 0.79</td><td>A helium atom fills a Si vacancy</td></tr><tr><td>He + vacancy (He replaces C)</td><td>3.29</td><td>-- 0.04</td><td>A helium atom fills a C vacancy</td></tr><tr><td>Divacancy SiC</td><td>5.01</td><td>-- 0.53(Si/C)</td><td>Two vacancies occupy nearest lattice points</td></tr><tr><td>Trivacancy SiSiC</td><td>8.44</td><td>-- 0.16(Si)</td><td>Two Si vacancies enclose one C vacancy</td></tr><tr><td>Trivacancy SiCC</td><td>7.79</td><td>-- 0.19(C)</td><td>Two C vacancies enclose one Si vacancy</td></tr><tr><td>Diinterstitial SiSi</td><td>10.79</td><td>-- 2.17(Si)</td><td>Two atoms occupy two nearest interstices</td></tr><tr><td>Diinterstitial SiC</td><td>10.33</td><td>-- 2.15(Si/C)</td><td>Two atoms occupy two nearest interstices</td></tr><tr><td>Diinterstitial CC</td><td>9.73</td><td>-- 2.27(C)</td><td>Two atoms occupy two nearest interstices</td></tr><tr><td>Triinterstitial SiSiSi [110]</td><td>15.19</td><td>-- 2.08(Si)</td><td>Three atoms form a line along [110]</td></tr><tr><td>Triinterstitial SiSiC [110]</td><td>14.31</td><td>-- 2.48(C)</td><td>Three atoms form a line along [110]</td></tr><tr><td></td><td></td><td>-- 2.50(Si)</td><td></td></tr><tr><td>Triinterstitial SiCC [110]</td><td>14.78</td><td>-- 1.55(C)</td><td>Three atoms form a line along [110]</td></tr><tr><td></td><td></td><td>-- 1.43(Si)</td><td></td></tr><tr><td>Triinterstitial CCC [110]</td><td>14.12</td><td>-- 1.61(C)</td><td>Three atoms form a line along [110]</td></tr><tr><td>Triinterstitial SiSiSi {100}</td><td>14.91</td><td>-- 2.36(Si)</td><td>Three atoms form a {100} plane</td></tr><tr><td>Triinterstitial SiSiC {100}</td><td>15.04</td><td>-- 1.75(C)</td><td>Three atoms form a {100} plane</td></tr><tr><td></td><td></td><td>-- 1.77(Si)</td><td></td></tr><tr><td>Triinterstitial SiCC {100}</td><td>13.44</td><td>-- 2.69(C)</td><td>Three atoms form a {100} plane</td></tr><tr><td></td><td></td><td>-- 2.57(Si)</td><td></td></tr><tr><td>Triinterstitial CCC {100}</td><td>13.26</td><td>-- 2.47(C)</td><td>Three atoms form a {100} plane</td></tr><tr><td>Triinterstitial SiSiSi {111}</td><td>17.56</td><td>+ 0.29(Si)</td><td>Three atoms form a {111} plane</td></tr><tr><td>Triinterstitial SiSiC {111}</td><td>14.45</td><td>-- 2.34(C)</td><td>Three atoms form a {111} plane</td></tr><tr><td></td><td></td><td>-- 2.36(Si)</td><td></td></tr><tr><td>Triinterstitial SiCC {111}</td><td>15.90</td><td>-- 0.43(C)</td><td>Three atoms form a {111} plane</td></tr><tr><td></td><td></td><td>-- 0.49(Si)</td><td></td></tr><tr><td>Triinterstitial CCC {111}</td><td>15.88</td><td>+ 0.15(C)</td><td>Three atoms form a {111} plane</td></tr></tbody></table>

means that more carbon atoms may be present in nonstoichiometric cases.

(2) Atoms surrounding a silicon vacancy undergo substantial relaxation while those surrounding a carbon vacancy do not relax as much. This is due to the size asymmetry of silicon and carbon atoms.

(3) The sum of calculated formation energy and migration energy of a vacancy agrees quite well with the corresponding experimental data on self-diffusion in SiC, indicating the validity of the modified Pearson potential.

(4) Helium-filled silicon vacancies are energetically more stable as compared to unoccupied ones. The effect of helium in stabilizing vacancies is therefore important.

(5) Defects tend to cluster. A divacancy is always composed of one silicon vacancy and one carbon vacancy because the nearest neighbors are always of different types.

(6) The calculated preexponential factors of vacancies are not in good agreement with experimental data. This may be accounted for by the complexity of experimental conditions. In reality, many diffusion mechanisms may operate at the same time.

## Acknowledgement

Special thanks are directed to Mr. A. El-Azab for passing on the MD subroutines, and Mr. Ed Aguilar for his assistance in typing the manuscript.

## References

[1] R. Swalin, J. Phys. Chem. Solids 18 (1960) 290.
[2] A. Scholz, Phys. Status Solidi 3 (1063) 43.
[3] A. Scholz and A. Seeger, Phys. Status Solidi 3 (1963) 1480.
[4] C. Hwang and L. Watt, Phys. Rev. 171 (1965) 958.
[5] K. Bennemann, Phys. Rev. A 137 (1965) 1497.
[6] J. Bernholc, S. Kajhara, C. Wang and A. Antonelli, Mater. Sci. Eng. B 11 (1992) 265.
[7] J. Lennard-Jones, Interatomic Forces, Special Publica-

tion No. VIII, Indian Association for the Cultivation of
Science, Calcutta, India (1939).

[8] E. Pearson, T. Takai, T. Halicioglu and W. Tiller, J.
Cryst. Growth 70 (1984) 33.

[9] G. Maitland et al., Intermolecular Forces, Oxford (1981)
Appendix 1.

[10] B. Axilrod and E. Teller, J. Chem. Phys. 54 (1971) 2129.

[11] J. Slater and J. Kirwood, Phys. Rev. 37 (1931) 690.

[12] Table of Periodic Properties of the Elements, Sargent-
Welch Scientific Company, USA (1992).

[13] P. Chou and N. Ghoniem, Phys. Rev. B 43 (1991) 2490.

[14] R. Ghoshtagore and R. Coble, Phys. Rev. 143 (1966) 623.

[15] J. Hong and R. Davis, J. Am. Ceram. Soc. 63 (1980) 546.

[16] J. Hong, R. Davis and D. Newbury, J. Mater. Sci. 16
(1981) 2485.

[17] M. Hon and R. Davis, J. Mater. Sci. 14 (1979) 2411.

[18] M. Hon and R. Davis, J. Mater. Sci. 15 (1980) 2073.

[19] W. Choyke and L. Patrick, Phys. Rev. B 2 (1970) 4959.

[20] Y. Vodakov and E. Mokhov, Silicon Carbide-1973, eds.
R. Marshall, J. Faust Jr. and C. Ryan (University of
Southern California Press, 1974) p. 508.

[21] D. Adams, Inorganic Solids/An Introduction to Con-
cepts in Solid-State Structural Chemistry (Wiley, London,
1974).

[22] B. Axilrod and E. Teller, J. Chem. Phys. 11 (1943) 299.

[23] D. Olander, Fundamental Aspects of Nuclear Reactor
Fuel Elements, Technical Information Center, Energy
Research and Development Administration (1976) chap.
2.