First-principles study on the lattice dynamics and thermodynamic properties of $Cu_2GeSe_3$

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2015 EPL 109 47004

(http://iopscience.iop.org/0295-5075/109/4/47004)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.100.58.76
This content was downloaded on 06/03/2015 at 22:24

Please note that terms and conditions apply.

First-principles study on the lattice dynamics and thermodynamic properties of $Cu_2GeSe_3$

HEZHU SHAO, XIAOJIAN TAN, TIANQI HU, GUO-QIANG LIU(a), JUN JIANG and HAOCHUAN JIANG

Ningbo Institute of Materials Technology and Engineering, Chinese Academy of Science - Ningbo 315201, China

received 5 December 2014; accepted in final form 7 February 2015
published online 27 February 2015

PACS 71.20.-b - Electron density of states and band structure of crystalline solids
PACS 63.20.D- - Phonon states and bands, normal modes, and phonon dispersion
PACS 65.40.-b - Thermal properties of crystalline solids

Abstract - The lattice dynamics and thermodynamic properties of $Cu_2GeSe_3$ are investigated by first-principles calculations. The obtained phonon frequencies agree well with the measurements of Raman scattering. The thermodynamic properties are calculated within quasi-harmonic approximation, and the measured lattice thermal conductivity is well reproduced. The calculated Grüneisen parameter is found to be much smaller than previous prediction, indicating that the bonding anharmonicity is insufficient to explain the low thermal conductivity in $Cu_2GeSe_3$. Our study shows that the thermodynamic properties of $Cu_2GeSe_3$ are inherently related to its weak covalent Cu-Se bonding.

Copyright © EPLA, 2015

Introduction. - Thermoelectric (TE) materials have many potential applications in power generation and heat pumping since they can realise direct energy conversion between heat and electricity [1]. TE performance is determined by a dimensionless figure of merit, $ZT = S^2\sigma T/\kappa$, where $S$, $\sigma$, $\kappa$, and $T$ are the Seebeck coefficient, electrical conductivity, thermal conductivity, and absolute temperature, respectively. This expression indicates that high TE performance could be achieved in the materials, which have large Seebeck coefficient, high electrical conductivity, and low thermal conductivity. Recently, ternary and multinary Cu-based diamond-like chalcogenides have attracted considerable interests in TE applications because of their unexpected low thermal conductivities [2-7].

Cu-based diamond-like chalcogenides include $Cu_2B^{IV}X_3$, $CuB^{II}X_2$, and $Cu_2B^{II}B^{IV}X_4$, where $B^{II} = Zn$ or Cd, $B^{III} = Al$, Ga, or In, $B^{IV} = Ge$ or Sn, and $X = S$, Se, or Te. In-doped $Cu_2SnSe_3$ has been reported to be an effective TE material with $ZT = 1.14$ and $\kappa = 0.9\ \mathrm{Wm^{-1}K^{-1}}$ at 850 K [3]. Ge- and Ga-doped $Cu_2GeSe_3$ exhibit low $\kappa$ of 1.0 and $0.67\ \mathrm{Wm^{-1}K^{-1}}$ at 750 K, respectively [4,5]. Quaternary $Cu_{2.1}Zn_{0.9}SnSe_4$ exhibits $\kappa = 1.3\ \mathrm{Wm^{-1}K^{-1}}$ at 860 K [6], and $Cu_{2.1}Cd_{0.9}SnSe_4$ $\kappa = 0.49\ \mathrm{Wm^{-1}K^{-1}}$ at 700 K [7]. $Cu_2GeSe_3$, Ge and ZnSe have similar crystal structures and average atomic masses, but they have much higher thermal conductivities: $58\ \mathrm{Wm^{-1}K^{-1}}$ for Ge and $18\ \mathrm{Wm^{-1}K^{-1}}$ for ZnSe at room temperature [8,9].

The electronic structures of Cu-based diamond-like compounds have been well understood. Xi et al. have investigated the electrical transport properties of $Cu_2SnX_3$ ($X = S$, Se) based on first-principles calculations [10]. It is found that the upper valence bands of $Cu_2SnX_3$ ($X = S$, Se) consist of the $Cu$-$d$ and $Se(S)$-$p$ orbitals, and thus the carrier concentration could be tuned by Sn-site doping without severe damage of the hole transport networks [10]. Such electronic structures are believed to be beneficial to the TE performance. Other Cu-based diamond-like compounds, such as $CuGaSe_2$, $CuGaS_2$, and $Cu_2ZnSnS_4$ etc., have similar electronic structures to $Cu_2SnX_3$ [11-13].

Recently, Cho et al. synthesized Ge- and Ga-doped $Cu_2GeSe_3$ and investigated their thermodynamic properties [4,5]. They obtained a fairly large Grüneisen parameter, $\gamma = 1.7$, by fitting the measured heat capacity and thermal expansion coefficient. Grüneisen parameter measures the magnitude of bonding anharmonicity. It is known that PbTe have very strong anharmonic phonon scattering, whereas its Grüneisen parameter is only 1.45 at room temperature [14-16]. The low thermal conductivity of $Cu_2GeSe_3$ was therefore ascribed to its high anharmonicity [5]. It is noticeable that previous studies have revealed that Grüneisen parameter in diamond-like structures is usually smaller than that

(a)E-mail: liugq@nimte.ac.cn (corresponding author)

47004-p1

![](./images/814652614011518977_1.jpg)

Fig. 1: (Colour on-line) Crystal structure of Cu₂GeSe₃ in orthorhombic cell.

in rock-salt systems [17,18]. Nevertheless, the proposed high bonding anharmonicity in Cu₂GeSe₃ have not been confirmed by other experimental measurements or theoretical calculations.

Here we report a theoretical investigation of lattice dynamics and thermodynamic properties for Cu₂GeSe₃ based on first-principles calculations. The phonon frequencies by Raman scattering and thermal conductivity are well reproduced in our calculations. This paper is organized as follows. In the second section, we present the computational methods and parameters used in the calculations. The third section presents the results and discusses for the phonon spectra and thermodynamic properties of Cu₂GeSe₃. The conclusion is given in the fourth section.

Methodology. – The calculations are based on the density functional theory (DFT) method within the generalized gradient approximation (GGA) using the Perdew, Burke, and Ernzerhof (PBE) functional [19], as implemented in the Vienna Ab initio Simulation Package (VASP), which employs the plane-wave basis [20,21]. The supercell approach with the finite displacement method implemented in the Phonopy package is used to calculate phonon dispersions [22,23]. The plane-wave energy cutoff is set to 500.00 eV, and the electronic energy convergence is $10^{-8}$ eV. In structure relaxations, the force convergence for ionic is set to $10^{-3}$ eV/A. In phonon calculations, a supercell containing 72 atoms is employed, and a $\Gamma$-centered $5 \times 5 \times 5$ Monkhorst-Pack $k$-point mesh is used to sample the irreducible Brillouin zone.

Results and discussion. –

Crystal and electronic structures. Cu₂GeSe₃ has orthorhombic structure with space group of Imm2 [24]. The diamond-like structure of Cu₂GeSe₃ can be obtained by (cation mutation of zinc blende binary II-VI analogs (e.g., ZnSe)). As shown in fig. 1, there are two types of anion-centered tetrahedra in the Cu₂GeSe₃ structure. The $2a$-site Se atoms are surrounded by two Cu and two Ge atoms, and the $4c$-site Se atoms bond with three Cu and one Ge atoms. Cu and Ge atoms occupy $4c$ and $2b$ positions, respectively. As shown in table 1, the relaxed structure is in good accordance with the experimental data [25].

The electronic structures of Cu₂GeSe₃ are calculated by DFT method. The total and atom projected density of states (DOS) for Cu₂GeSe₃ are presented in fig. 2. The calculated DOS indicates a metallic ground state for Cu₂GeSe₃. This is inconsistent with optical absorption measurements, which measured a band gap around 0.8 eV [26,27]. A similar discrepancy between DFT calculations and experimental measurements has been found in other Cu-based diamond-like compounds [10–13], such as CuGaSe₂, CuGaS₂, and Cu₂ZnSnS₄ etc. It is well known that the DFT method usually underestimates the band gap of semiconductors. Xi et al. have applied the

<table>
<caption>Table 1: Calculated structure parameters in the orthorhombic cell with space group Imm2. Experimental data [25] for comparison are given in parentheses.</caption>
<tr>
<td>Lattice</td>
<td></td>
<td>$a = 11.889$</td>
<td>$b = 4.052$</td>
<td>$c = 5.596$</td>
</tr>
<tr>
<td>parameter</td>
<td></td>
<td>($a = 11.854$</td>
<td>$b = 3.954$</td>
<td>$c = 5.489$)</td>
</tr>
<tr>
<td>Atom</td>
<td>Wyckoff</td>
<td>$x$</td>
<td>$y$</td>
<td>$z$</td>
</tr>
<tr>
<td>Cu</td>
<td>$4c$</td>
<td>0.168</td>
<td>0</td>
<td>0.262</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(0.1709</td>
<td>0</td>
<td>0.244)</td>
</tr>
<tr>
<td>Ge</td>
<td>$2b$</td>
<td>0</td>
<td>0.5</td>
<td>0.734</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(0</td>
<td>0.5</td>
<td>0.762)</td>
</tr>
<tr>
<td>Se₁</td>
<td>$2a$</td>
<td>0</td>
<td>0</td>
<td>0.009</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(0</td>
<td>0</td>
<td>0)</td>
</tr>
<tr>
<td>Se₂</td>
<td>$4c$</td>
<td>0.329</td>
<td>0</td>
<td>$-0.003$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(0.3341</td>
<td>0</td>
<td>0.006)</td>
</tr>
</table>

![](./images/814652614011518977_2.jpg)

Fig. 2: (Colour on-line) Total and atom projected DOS for Cu₂GeSe₃.

![](./images/814652614011518977_3.jpg)

Fig. 3: (Colour on-line) Electronic charge density of Cu₂GeSe₃ in the [010] plane.

hybrid functional (HSE) [28,29] calculations to Cu₂SnX₃ (X = S, Se), and reproduced the experimental band gaps [10]. Although DFT calculations failed to open a gap, they give similar band characteristics for Cu₂SnX₃ (X = S, Se) as the HSE calculations did [10].

As shown in fig. 2, the total DOS from -10 to 4 eV is mainly composed of Cu-d, Se-p, Ge-s and Ge-p states. The valence band close to the Fermi level is mainly made up of Cu-d and Se-p states, and the conduction band is mainly from Ge-s and Se-p states. Therefore the hole doping at Ge-site can be used to tune the carrier con- centration without severe damage of the hole transport networks. As mentioned, such electronic structure is ben- eficial to the p-type TE applications [10]. Figure 2 shows that the Cu-d state is separated into two parts: The main part is located from -2.8 to 0 eV and a small part is from -6 to -3.4 eV. Comparing with the Se-p DOS, we may realize that the separation of Cu-d state is due to the co- valent bonding between Cu-d and Se-p orbitals. The Cu-d DOS from -2.8 to 0 eV is corresponding to the p-d anti- bonding state, while the Cu-d DOS from -6 to -3.4 eV is corresponding to the p-d bonding state. The overlap between Cu-d and Se-p state is rather slight, indicating a weak covalent p-d bonding.

Figure 3 presents the electronic charge density in the [010] plane containing a whole Cu₂GeSe₃ molecule. The highest charge density is found to be on the Cu ions, con- sistently with the projected DOS shown in fig. 2. The in- teratomic charge density indicates the strength of covalent bonding. As may be seen from fig. 3, the covalent bond- ing between Cu and Se is rather weak, whereas the Se-Ge bonding is a little bit stronger. Usually, high thermal con- ductivity in semiconductor is related to strong covalent bonding, such as in diamond and silicon. We will shows that the weak covalent Cu-Se bonding is important to the understanding of the low lattice thermal conductivity in Cu₂GeSe₃.

Phonon spectra. The phonon spectra of Cu₂GeSe₃ are calculated using the supercell approach with the fi- nite displacement method. Figure 4 presents the phonon DOS and phonon spectra along several high symme- try lines in the Brillouin zone. The primitive cell of Cu₂GeSe₃ contains six atoms, and there are 18 phonon branches presented in the phonon spectra. As shown in the phonon DOS, the low-frequency branches up to 100 cm⁻¹ are mainly from Cu and Se vibrations, whereas the high-frequency branches above 220 cm⁻¹ are mainly from Ge and Se₂ vibrations. Usually, the lattice ther- mal conductivity is mainly contributed by low-frequency acoustic phonon branches. Therefore the Cu-Se bonding is crucial to the heat transport of Cu₂GeSe₃.

![](./images/814652614011518977_4.jpg)

Fig. 4: (Colour on-line) Phonon spectra (top) and phonon DOS (bottom) of Cu₂GeSe₃.

<table>
<caption>Table 2: Theoretically determined Raman frequencies (cm⁻¹) and their symmetry assignments of the experimental results [25].</caption>
<thead>
<tr>
<th colspan="2">Raman scattering</th>
<th colspan="2">Calculations</th>
</tr>
<tr>
<th>Frequency</th>
<th>Symmetry</th>
<th>Frequency</th>
<th>Symmetry</th>
</tr>
</thead>
<tbody>
<tr>
<td>135</td>
<td>A₁ or B₁</td>
<td>136.4</td>
<td>B₁</td>
</tr>
<tr>
<td></td>
<td></td>
<td>138.2</td>
<td>A₁</td>
</tr>
<tr>
<td>189</td>
<td>A₂</td>
<td>191.4</td>
<td>B₂</td>
</tr>
<tr>
<td>212</td>
<td>B₂</td>
<td>193.0</td>
<td>A₂</td>
</tr>
<tr>
<td>235</td>
<td>A₁ or B₁</td>
<td>235.5</td>
<td>A₁</td>
</tr>
<tr>
<td>254</td>
<td>A₁ or B₁</td>
<td>252.2</td>
<td>B₁</td>
</tr>
</tbody>
</table>

The Raman spectra and vibrational modes of Cu₂GeSe₃ have been reported by Marcano <i>et al.</i> [25] We list the calculated Raman frequencies and their symmetries in table 2. The calculated phonon frequencies are in good accordance with the experimental data. The discrepancy between the calculated and the measured frequencies is less than 3%, except for the B₂ mode. The calculated frequency for the B₂ mode is 11 cm⁻¹ lower than the ex- perimental value. In our calculations, the B₂ mode has lower frequency than the A₂ mode, but the experiment results is reversed. The difference between calculational and experimental results for B₂ mode may be from the LO-TO splitting. Since our DFT calculation predicts a metallic ground state for Cu₂GeSe₃, the LO-TO splitting is not considered in the phonon calculation.

![](./images/814652614011518977_5.jpg)

Fig. 5: (Colour on-line) Schematic phonon vibrations with different frequencies listed in table 2.

At the $\Gamma$-point, the phonon branches can be classified according to crystal point group. The orthorhombic $\mathrm{Cu}_{2} \mathrm{GeSe}_{3}$ has point group $C_{2 v}$. The 18 zone-center vibrational modes can be classified as $6 A_{1}+2 A_{2}+6 B_{1}+4 B_{2}$, in which $1 A_{1}+1 B_{1}+1 B_{2}$ are acoustic modes [24]. The optical modes are all Raman active [25]. In Raman scattering measurements, several vibrational modes cannot be determined. At $135 \mathrm{~cm}^{-1}$, the experimental symmetry was assigned as $A_{1}$ or $B_{1}$. Our calculations actually find two branches around $135 \mathrm{~cm}^{-1}$ : an $A_{1}$ mode at $138.2 \mathrm{~cm}^{-1}$ and a $B_{1}$ mode at $136.4 \mathrm{~cm}^{-1}$. The symmetries of the 235 and $252 \mathrm{~cm}^{-1}$ branches were not determined in experiment either. Our calculations indicate $A_{1}$ mode for $235 \mathrm{~cm}^{-1}$ and $B_{1}$ modes $252 \mathrm{~cm}^{-1}$.

In fig. 5, we present the schematic vibrations for the phonon modes listed in table 2. $A_{1}$ and $B_{1}$ modes vibrate in the $x-z$ plane, and $A_{2}$ and $B_{2}$ modes vibrate along the $y$-direction. Among the four vibrational modes, the $A_{2}$ is infrared inactive, the other three modes are infrared active. As shown in fig. 5, there is no dipole moment in $A_{2}$ vibration, since the two $\mathrm{Cu}$ ions vibrate along opposite directions, as well as the two Se ions. In the $B_{2}$ mode, the vibration of $\mathrm{Cu}$ ions is anti-parallel to the vibration of $\mathrm{Se}$ ions, and their vibrations form a dipole moment. In the vibrations of 235 and $253 \mathrm{~cm}^{-1}$, Ge ions have the greatest amplitudes, and $\mathrm{Cu}$ ions almost remain at rest, consistently with the phonon DOS shown in fig. 4.

Thermodynamic properties. The Grüneisen parameter describes the relationship between the thermal expansion of a crystal and its vibrational properties. If a system has no anharmonic vibrations, its Grüneisen parameter is zero and thermal expansion would not occur. Conversely, the larger Grüneisen parameter indicates the stronger anharmonic vibrations. Grüneisen parameter, $\gamma$, can be calculated using the formula

$$
\gamma=\frac{3 \beta B V_{m}}{C_{v}}, \tag{1}
$$

where $\beta$ is the linear thermal expansion coefficient, $B$ is the bulk modulus, $V_{m}$ is the the molar volume, and $C_{v}$ is the isometric heat capacity.

<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    Calculation
   </th>
   <th>
    Experiments
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    $C_{v}$
   </th>
   <td>
    0.328
   </td>
   <td>
    0.34
   </td>
  </tr>
  <tr>
   <th>
    $E$
   </th>
   <td>
    90.7
   </td>
   <td>
    91
   </td>
  </tr>
  <tr>
   <th>
    $\beta$
   </th>
   <td>
    13.2
   </td>
   <td>
    8.4
   </td>
  </tr>
 </tbody>
</table>

Table 3: Comparison between calculated and measured isometric heat capacity $C_{v}$ ($\mathrm{Jg}^{-1}\mathrm{K}^{-1}$), Young’s modulus $E$ (GPa), and linear thermal expansion coefficient $\beta$ ($10^{-6}$/K) for $\mathrm{Cu}_{2}\mathrm{GeSe}_{3}$ at 300 K.

![](./images/814652614011518977_6.jpg)

Fig. 6: (Colour on-line) Calculated Grüneisen parameters with respect to temperatures for $\mathrm{Cu}_{2}\mathrm{GeSe}_{3}$.

Table 3 presents the comparison of calculated and measured isometric heat capacity, Young’s modulus, and linear thermal expansion coefficient at 300 K. The isometric heat capacity can be calculated as

$$
C_{v}=\sum_{n, \mathbf{q}} k_{B}\left(\frac{\hbar \omega_{n}(\mathbf{q})}{k_{B} T}\right)^{2} \frac{e^{\hbar \omega_{n}(\mathbf{q}) / k_{B} T}}{\left(e^{\hbar \omega_{n}(\mathbf{q}) / k_{B} T}-1\right)^{2}}, \tag{2}
$$

where $\hbar$ is Planck constant, $k_{B}$ is Boltzmann constant, $T$ is the temperature, and $\omega_{n}(\mathbf{q})$ is the phonon frequency of the $n$-th branch with wave vector $\mathbf{q}$. The calculated $C_{v}$ is $0.328\mathrm{Jg}^{-1}\mathrm{K}^{-1}$ at 300 K, which is well consistent with the experimental result of $0.34\mathrm{Jg}^{-1}\mathrm{K}^{-1}$ at room temperature.

The bulk modulus and linear thermal expansion coefficient at various temperatures are calculated within the quasi-harmonic approximation (QHA), in which the phonons are treated as harmonic but volume dependent [23]. The obtained bulk modulus $B$ is 54.0 GPa at 300 K. The experimental Young’s modulus for $\mathrm{Cu}_{2}\mathrm{GeSe}_{3}$ is $E = 91$ GPa [2]. Using the relation $E = B(3(1 - 2\nu))$, where $\nu$ is Poisson’s ration, we obtained Young’s modulus $E = 90.6$ GPa, which agrees well with the measured value. The calculated linear thermal expansion coefficient $\beta$ at room temperature is $13.2 \times 10^{-6}$/K, which is greater than the experimental value of $8.4 \times 10^{-6}$/K [30]. Using eq. (1), the Grüneisen parameter $\gamma$ with respect to temperature is calculated, as shown in fig. 6. At room temperature, the calculated Grüneisen parameter $\gamma$ for $\mathrm{Cu}_{2}\mathrm{GeSe}_{3}$ is 1.2, which is much smaller than the previous report of 1.7 by Cho et al. [5]. Note that the calculated linear thermal expansion coefficient is lager than the experimental value, and therefore our calculation may overestimate the Grüneisen parameter, but not underestimate it.

47004-p4

First-principles study on the lattice dynamics and thermodynamic properties of Cu₂GeSe₃

Grüneisen parameter can also be calculated by averaging the mode Grüneisen parameter $\gamma_n(\mathbf{q})$,

$$
\gamma_{\text{ave}}^{\text{mode}} = \frac{1}{C_v} \sum_{n,\mathbf{q}} \gamma_n(\mathbf{q}) C_{v,n}(\mathbf{q}), \tag{3}
$$

where $\gamma_n(\mathbf{q})$ is the mode Grüneisen parameter, $C_{v,n}(\mathbf{q})$ is the mode heat capacity. The mode Grüneisen parameter is defined as the phonon frequency shift with respect to the volume

$$
\gamma_n(\mathbf{q}) = -\frac{V_0}{\omega_n(\mathbf{q})} \frac{\partial \omega_n(\mathbf{q})}{\partial V}, \tag{4}
$$

where $\omega_n(\mathbf{q})$ is the phonon frequency of the $n$-th branch with wave vector $\mathbf{q}$, $V_0$ is the equilibrium volume at 0 K. Figure 6 presents the calculated $\gamma_{\text{ave}}^{\text{mode}}$, which is consistent with the Grüneisen parameter calculated using eq. (1).

The mode Grüneisen parameter as functions of wave vectors and frequencies are plotted in fig. 7. Under $100\ \text{cm}^{-1}$, Cu₂GeSe₃ exhibits many negative mode Grüneisen parameters, which indicate that the corresponding phonon frequencies will increase when volume is increased. At low temperature, since only the low-frequency phonons are excited, the averaged Grüneisen parameters could be negative, as shown in fig. 6. Such negative Grüneisen parameter is common in diamond-like semiconductors, such as Si, Ge and ZnSe [31,32]. Cho *et al.* presumed that Cu₂GeSe₃ has similar bonding anharmonicity to PbTe [5]. Previous calculations have shown that the mode Grüneisen parameters of PbTe are all positive throughout the Brillouin zone, and the mode Grüneisen parameters are very high at the $\Gamma$-point, up to 15 [33]. However, the largest mode Grüneisen parameters of Cu₂GeSe₃, as shown in fig. 7, is less than 3. These properties show that the bonding anharmonicity in Cu₂GeSe₃ is very different from PbTe.

According to Slack's expression [16,18,34], the lattice thermal conductivity at high temperatures can be given as

$$
\kappa_L = A \frac{\overline{M} \theta_D^3 \delta}{\gamma^2 n^{2/3} T}, \tag{5}
$$

where $\overline{M}$ is the average atomic mass, $\theta_D$ is the Debye temperature, $\delta^3$ is the volume per atom, $n$ is the number of atoms in the primitive cell, $\gamma$ is Grüneisen parameter, and $A$ is a physical constant $\approx 3.1 \times 10^{-6}$ when the units of $\kappa_L$, $\overline{M}$, and $\delta$ are taken as $\text{Wm}^{-1}\text{K}^{-1}$, amu, and angstroms, respectively. The experimental Debye temperature is 168 K [2]. Finally, the obtained lattice thermal conductivity at room temperature is $2.0\ \text{Wm}^{-1}\text{K}^{-1}$, which is slightly less than the experimental value of $2.4\ \text{Wm}^{-1}\text{K}^{-1}$ [2].

Cho *et al.* ascribed the low thermal conductivity of Cu₂GeSe₃ to high bonding anharmonicity, based on their estimated Grüneisen parameter of 1.7 [5]. Our calculated Grüneisen parameter for Cu₂GeSe₃ is only 1.2, which is less than that of 1.45 in PbTe. This result is consistent with previous knowledge that Grüneisen parameter in diamond-like structures is usually smaller than that in rock-salt systems. The calculated lattice thermal conductivity is in good agreement with experimental results. Our calculations show that the bonding anharmonicity in Cu₂GeSe₃ is insufficient to explain the low thermal conductivity. We note that the polycrystalline sample used in the measurements of Cho *et al.* has lower relative densities, about 95%. This might be the reason that they obtained a lower bulk modulus and a higher thermal expansion coefficient than the earlier experiments [2,5,30].

![](./images/814652614011518977_7.jpg)

Fig. 7: (Colour on-line) Calculated mode Grüneisen parameter with respect to wave vectors (a) and frequencies (b) for Cu₂GeSe₃.

Compared with the elemental semiconductor Ge, Cu₂GeSe₃ has similar crystal structure, average mass, and isometric heat capacity, but much lower thermal conductivity. The experimental thermal conductivity and Debye temperature for Ge are $58\ \text{Wm}^{-1}\text{K}^{-1}$ and 363 K [35], compared with $2.4\ \text{Wm}^{-1}\text{K}^{-1}$ and 168 K for Cu₂GeSe₃. Equation (5) indicates that the lattice thermal conductivity is proportional to the third power of the Debye temperature. Therefore the low thermal conductivity of Cu₂GeSe₃ is related to its low Debye temperature. The Debye temperature reflects the magnitude of sound velocity. According to the discussions in the above section, the low-frequency vibrations in Cu₂GeSe₃ is determined by its weak covalent Cu-Se bonding. Therefore, the weak covalent Cu-Se bonding leads to a low Debye temperature, and then results in a low lattice thermal conductivity.

Conclusion. – In summary, we have employed first-principles calculations to investigate the lattice dynamics and thermodynamic properties of Cu₂GeSe₃. The obtained phonon frequencies and lattice thermal conductivity agree well with experimental measurements. Our calculations show that Cu₂GeSe₃ has a moderate Grüneisen parameter, indicating that the bond anharmonicity is insufficient to explain the low lattice thermal

47004-p5

conductivity. We conclude that the low thermal conductivity in $Cu_2GeSe_3$ is due to its low Debye temperature, which originates in the weak covalent Cu-Se bonding.

* * *

This work was supported by the National Natural Science Foundation of China (Grant Nos. 11234012, 11404348 and 11404350), China Postdoctoral Science Foundation (Grant No. 2014M561796), Zhejiang Province Preferential Postdoctoral Funded Project (Grant No. BSH1402080), Ningbo Municipal Natural Science Foundation (Grant No. 2014A610008), and Ningbo Science and Technology Innovation Team (Grant No. 2014B82004).

REFERENCES

[1] Rowe D. M. (Editor), *CRC Handbook of Thermoelectrics* (CRC Press, Boca Raton, Fla.) 1995.

[2] Berger L. I. and Prochukhan V. D., *Ternary Diamond-like Semiconductors* (Consultants Bureau, New York) 1969.

[3] Shi X., Xi L., Fan J., Zhang W. and Chen L., *Chem. Mater.*, **22** (2010) 6029.

[4] Cho J. Y., Shi X., Salvador J. R., Yang J. and Wang H., *J. Appl. Phys.*, **108** (2010) 073713.

[5] Cho J. Y., Shi X., Salvador J. R., Meisner G. P., Yang J., Wang H., Wereszczak A. A., Zhou X. and Uher C., *Phys. Rev. B*, **84** (2011) 085207.

[6] Liu M., Huang F., Chen L. and Chen I. W., *Appl. Phys. Lett.*, **94** (2009) 202103.

[7] Liu M., Chen I. W., Huang F. and Chen L., *Adv. Mater.*, **21** (2009) 3808.

[8] Bakhchieva S. R., Kekelidze N. P. and Kekua M. G., *Phys. Status Solidi (a)*, **83** (1984) 139.

[9] Balasubramanian A. K., Sankar N., Ramakrishnan S. K. and Ramachandran K., *Cryst. Res. Technol.*, **39** (2004) 558.

[10] Xi L., Zhang Y. B., Shi X. Y., Yang J., Shi X., Chen L. D., Zhang W., Yang J. and Singh D. J., *Phys. Rev. B*, **86** (2012) 155201.

[11] Alonso M. I., Wakita K., Pascual J., Garriga M. and Yamamoto N., *Phys. Rev. B*, **63** (2001) 075203.

[12] Paier J., Asahi R., Nagoya A. and Kresse G., *Phys. Rev. B*, **79** (2009) 115126.

[13] Zhang Y., Yuan X., Sun X., Shih B. C., Zhang P. and Zhang W., *Phys. Rev. B*, **84** (2011) 075127.

[14] Božin E. S., Malliakas C. D., Souvatzis P., Proffen T., Spaldin N. A., Kanatzidis M. G. and Billinge S. J. L., *Science*, **330** (2010) 1660.

[15] Delaire O., Ma J., Marty K., May A. F., McGuire M. A., Du M. H., Singh D. J., Podlesnyak A., Ehlers G., Lumsden M. D. and Sales B. C., *Nat. Mater.*, **10** (2011) 614.

[16] Ehrenreich F. S. H. and Turnbull D. (Editors), *The Thermal Conductivity of Nonmetallic Crystals Solid State Physics*, Vol. **34** (Academic Press) 1979, pp. 1–71.

[17] Slack G. A. and Huseby I. C., *J. Appl. Phys.*, **53** (1982) 6817.

[18] Morelli D. T. and Heremans J. P., *Appl. Phys. Lett.*, **81** (2002) 5126.

[19] Perdew J. P., Burke K. and Ernzerhof M., *Phys. Rev. Lett.*, **77** (1996) 3865.

[20] Kresse G. and Hafner J., *Phys. Rev. B*, **47** (1993) 558.

[21] Kresse G. and Furthmüller J., *Phys. Rev. B*, **54** (1996) 11169.

[22] Parlinski K., Li Z. Q. and Kawazoe Y., *Phys. Rev. Lett.*, **78** (1997) 4063.

[23] Togo A., Oba F. and Tanaka I., *Phys. Rev. B*, **78** (2008) 134106.

[24] Parthé E. and Garín J., *Monatsh. Chem.*, **102** (1971) 1197.

[25] Marcano G., Rincón C., Marín G., Delgado G. E., Mora A. J., Herrera-Pérez J. L., Mendoza-Alvarez J. G. and Rodríguez P., *Solid State Commun.*, **146** (2008) 65.

[26] Marcano G. and Nieves L., *J. Appl. Phys.*, **87** (2000) 1284.

[27] Sarkar B. K., Verma A. S. and Deviprasad P. S., *Phys. B: Condens. Matter*, **406** (2011) 2847.

[28] Heyd J., Scuseria G. E. and Ernzerhof M., *J. Chem. Phys.*, **118** (2003) 8207.

[29] Paier J., Marsman M., Hummer K., Kresse G., Gerber I. C. and Ángyán J. G., *J. Chem. Phys.*, **124** (2006) 154709.

[30] Berger L. I. and Balanevskaya A. E., *Fiz. Tverd. Tela (Leningrad)*, **6** (1964) 1311.

[31] Biernacki S. and Scheffler M., *Phys. Rev. Lett.*, **63** (1989) 290.

[32] Debernardi A. and Cardona M., *Phys. Rev. B*, **54** (1996) 11305.

[33] Zhang Y., Ke X., Chen C., Yang J. and Kent P. R. C., *Phys. Rev. B*, **80** (2009) 024304.

[34] Slack G. A., *J. Phys. Chem. Solids*, **34** (1973) 321.

[35] Keesom P. H. and Seidel G., *Phys. Rev.*, **113** (1959) 33.

47004-p6