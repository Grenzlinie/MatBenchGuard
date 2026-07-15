![](./images/812120499885703169_1.jpg)

Available online at www.sciencedirect.com
![](./images/812120499885703169_2.jpg)
Physica B 373 (2006) 328-333
![](./images/812120499885703169_3.jpg)

# Band structure and UV optical spectra of TGS crystals in the range of 4-10 eV

B. Andriyevsky$^{a, *}$, N. Esser$^{b}$, A. Patryn$^{a}$, C. Cobet$^{b}$, W. Ciepluch-Trojanek$^{a}$, M. Romanyuk$^{c}$

$^{a}$ Department of Electronics and Computer Sciences, Koszalin University of Technology, 2 Śniadeckich Street, PL-75-453 Koszalin, West Pomeranian, Poland
$^{b}$ ISAS-Institute for Analytical Sciences Department Berlin, Albert-Einstein-Street 9, D-12489 Berlin, Germany
$^{c}$ The Ivan Franko National University of L'viv, Kyrylo-and-Mefodii Street 8, UA-79005 L'viv, Ukraine

Received 3 December 2005; received in revised form 7 December 2005; accepted 8 December 2005

## Abstract

Theoretical and experimental studies of the band energy structure and optical spectra for triglycine sulphate crystal (TGS), $(NH_{2}CH_{2}COOH)_{3}\cdot H_{2}SO_{4}$, in the ferroelectric phase have been performed for the first time. First principal DFT calculations of the band structure, density of states and dielectric functions spectra $\varepsilon'(E)$ and $\varepsilon''(E)$ of TGS crystal have been done using the computer package Cambridge Serial Total Energy Package (CASTEP) code. Experimental spectral dispersions of the complex reflection ratio $\rho(E)$ have been measured using the synchrotron radiation at BESSY synchrotron source in the spectral range of 4-10 eV and the pseudo-dielectric functions $\langle\varepsilon\rangle=\langle\varepsilon'\rangle+\mathrm{i}\langle\varepsilon''\rangle$ were evaluated. Experimental data and theoretically calculated dielectric functions have demonstrated a good agreement. The band energy dispersion of valence and conducting bands have been analyzed and were used to identify the dielectric functions peculiarities.

© 2005 Elsevier B.V. All rights reserved.

PACS: 71.20.-b; 71.25.Tn; 78.20.-e

Keywords: Band structure of crystalline semiconductors and insulators; Optical properties

## 1. Introduction

Triglycine sulphate crystal (TGS), $(NH_{2}CH_{2}COOH)_{3}\cdot H_{2}SO_{4}$, is ferroelectric below 322 K belonging to the monoclinic space group $P2_{1}$, and above the transition temperature it becomes paraelectric with the center symmetry monoclinic space group $P2_{1}/m$ [1-4]. There are two formula units in the crystal unit cell of TGS. The structure of this crystal is a complicated arrangement of quasi-molecular glycine complexes, sulphate anions, and hydrogen bonds O–H…–O and N–H…–O (Fig. 1). Different kinds of chemical bonds are characteristic for the crystal: strong covalent-and-ion bonds in the ions $NH_{3}^{+}CH_{2}COO^{-}$, $NH_{3}^{+}CH_{2}COOH$, and $SO_{4}^{2-}$, and more weaker ion and hydrogen bonds between these quasi-molecular complexes. Parameters of TGS crystal unit cell in ferroelectric phase are the following: $a=9.419\mathring{A}$, $b=12.647\mathring{A}$, $c=5.727\mathring{A}$, $\beta=110.32^{\circ}$ [4]. Two formula units are in the crystal unit cell of TGS in both phases. The spontaneous polarization vector $P_{s}$ of TGS crystal is parallel to the two-fold axis of symmetry (b-axis in Fig. 1) and is due to the position of the polar group $NH^{3+}$ of glycine-I molecule. The total spontaneous polarization of TGS crystal at room temperature 293 K is relatively great, $2.8\times10^{-2}\mathrm{C/m^{2}}$, so this peculiarity together with great corresponding pyroelectric coefficient of TGS caused its wide application as a detectors of electromagnetic radiation [5-7]. Because of low symmetry of TGS crystal (monoclinic), the corresponding optical indicatrix is characterized by three different refractive indices half-axes $n_{\mathrm{p}}$, $n_{\mathrm{m}}$, $n_{\mathrm{g}}$ [8] and therefore an essential anisotropy of the optical functions in the UV fundamental absorption range $E>5.1\mathrm{eV}$ is expected. The study of the anisotropy of optical functions for the TGS crystals in this spectral range can be particularly useful for the investigation of relations

*Corresponding author. Tel.: +48 943478690; fax: +48 943433479.
E-mail address: bandri@tu.koszalin.pl (B. Andriyevsky).

0921-4526/$ - see front matter © 2005 Elsevier B.V. All rights reserved.
doi:10.1016/j.physb.2005.12.245

![](./images/812120499885703169_4.jpg)

Fig. 1. Spatial view of TGS crystal unit cell (horizontal unit cell axis is the b-axis).

between the peculiarities of electron structure and the ferroelectric state formation.

Physical properties of TGS crystals were widely studied experimentally and theoretically during the past 50 years. First measurements of partially polarized reflectance spectra of TGS crystals for light polarizations $E \parallel X$ and $E \parallel Y$ in the range of 4-22 eV were done using the Lyman discharge light source [9].

Nevertheless theoretical first-principal calculations of the total energy, band structure and related physical properties have not yet been carried out. This was probably caused by computation difficulties connected with the great number of atoms in the crystal unit cell $N_{\mathrm{c}}$ of TGS $(N_{\mathrm{c}}=74)$ and its low symmetry.

It is known from previous studies of TGS crystal, that for the wavelength $\lambda=300 \mathrm{~nm}(E=4.133 \mathrm{eV})$ and temperature 293 K the principal refractive indices are: $n_{X}=1.6371, n_{Z}=1.6055, n_{Y}=1.5190$ [10]. The following relations between the principal directions of the optical indicatrix $g, m, p$, and crystallographic directions take place: $n_{X} \| a \sin \beta, n_{Y} \| b, n_{Z} \| c$.

The aim of the present study was a theoretical first principal calculation of the electron band structure and optical spectra of TGS crystal, as well as the measurement of its polarized optical properties in the range of 4-10 eV using the synchrotron radiation.

## 2. Method of theoretical calculations

Calculations of the band energy dispersion $E(\boldsymbol{k})$, density of electron states (DOS), and dielectric functions $\varepsilon^{\prime}(E)$ and $\varepsilon^{\prime \prime}(E)$ of the TGS crystal have been performed using the Cambridge Serial Total Energy Package (CASTEP) code [11]. The CASTEP is a first principle density function theory (DFT) code, involving no fitting parameters, based on an explicit quantum treatment of the electrons in a model system which means solving Schrodinger's equation to find the electronic ground state. The calculations were performed within a framework of generalized gradient approximation (GGA) (Perdew-Wang 1991) for the exchange and correlation effects [12]. The ultra-soft model pseudopotentials were used [13]. These pseudopotentials require a quite low energy cutoff and guarantee good transferability, that is, the same potential correctly reproduces the valence electron scattering by the ionic core in different chemical environments. Calculations were performed using the plane-wave basis set with the kinetic energy cutoff for plane waves 340 eV, that corresponds to the energy convergence criterion of self consistency of $0.2 \times 10^{-5} \mathrm{eV} /$ atom. The optimization of crystal structure has been performed with the characteristic tolerances for total energy, $0.2 \times 10^{-4} \mathrm{eV} /$ atom, and RMS stress tensor, $0.1 \mathrm{GPa}$, before the calculations of band structure. Each energy state of the crystal was calculated at 23 k-points of the Brillouin zone.

## 3. Experimental

Measurements of the dielectric functions $\varepsilon^{\prime}(E)$ and $\varepsilon^{\prime \prime}(E)$ of TGS crystals have been done by spectroscopic ellipsometry (SE) method using the synchrotron-ellipsometer [14] attached to the 3m-NIM-1 off-Rowland circle normal incidence monochromator of the Berlin electron storage ring (BESSY II). The magnitude of monochromator exit slit used in experiments gave possibility to resolve spectral positions difference of approximately 0.02 eV in the range of $7.3 \mathrm{eV}$. $\mathrm{MgF}_{2}$ Rochon prisms were used as a polarizer and rotating analyzer attaining $99.998 \%$ degree of polarization. The complex reflectance ratio $\rho$ of TGS samples was measured with incidence angle of about $68^{\circ}$, from 4.0 to 9.9 eV and converted to the pseudodielectric function $\hat{\varepsilon}=\varepsilon^{\prime}+\mathrm{i} \varepsilon^{\prime \prime}$ via the two-phase (substrate ambient) model [15].

Measurements were done for two types of sample's: (1) the samples with a cleaved surface perpendicularly to the Y-direction of TGS crystal, and (2) the samples with mechanically polished surfaces perpendicularly to the Yand Z-direction. The final polishing of TGS samples was done with the paste of characteristic dimension $1-3 \mu \mathrm{m}$ of diamond grains in the air just before the inserting of samples into the vacuum chamber.

## 4. Results and discussion

Most of the energy states of TGS crystal are flat or of low band energy dispersion in $E(\boldsymbol{k})$ (Fig. 2). The degree of this dispersion for the $i$ th state can be presented by the inverse density of states effective mass, $1 / m_{i}^{*}$, measured on certain $k$-length:

$$
\frac{1}{m_{i}^{*}}=\frac{1}{\hbar^{2} k}\left|\frac{\mathrm{d} E_{i}}{\mathrm{~d} k}\right|. \tag{1}
$$

The minimum effective mass for the valence states is equal to about $m^{*}=0.64 m_{\mathrm{e}}$ and is observed near the energy $E=-7.5 \mathrm{eV}$ for the division $\Gamma-Y$ of the Brillouin zone (BZ) (Fig. 3). For the top of the valence band, the smallest effective mass is equal to $m^{*}=9.3 m_{\mathrm{e}}$ for the BZ

![](./images/812120499885703169_5.jpg)

Fig. 2. Band energy dispersion $E(k)$ for TGS crystal. The dashed directed line corresponds to the optical band gap.

direction $\Gamma-Z$. For the states of conducting band of TGS crystal, the dispersion of $E(\boldsymbol{k})$ is generally greater. Minimum effective mass for the states of conducting band is equal to $m^{*}=0.31 m_{\mathrm{e}}$ and is observed near the energy $E=6.16 \mathrm{eV}$ for the BZ direction $\Gamma-Y$, too. One of the peculiarities of the TGS band structure is a flatness of the bottom states of the conducting band in $\boldsymbol{k}$-space. The energy band gap of the TGS crystal is indirect and corresponds to optical transitions between $\Gamma$ and D points of the BZ (Figs. 2 and 3). The magnitude of this value $E_{\mathrm{gi}}=4.65 \mathrm{eV}$ is close to the experimental one $E_{\mathrm{gi}}^{(\mathrm{e})}=$ $4.97 \mathrm{eV}$ obtained from the optical absorption study [16].

Similar flatness of the band energy dispersion $E(k)$ is characteristic for typical borate crystals [17,18] where the borate complexes play role similar to the $\mathrm{SO}_{4}$ groups in the investigated crystals. This may be considered as a principal feature of the crystals possessing strong oxide clusters with the high degree of covalence chemical bonds. In the case of the TGS these clusters are substantially delocalized in the space.

On the basis of the band energy ground state calculation a Mulliken population analysis of TGS crystal has been done. The corresponding parameters of the atomic and overlap populations of the constituent atoms and bonds

![](./images/812120499885703169_6.jpg)

Fig. 3. Brillouin zone of TGS crystal in the ferroelectric phase.

<table>
<caption>Table 1 Atomic populations of the constituent atoms of TGS crystal</caption>
<thead>
<tr>
<th>Species</th>
<th>s-orbitals</th>
<th>p-orbitals</th>
<th>Total</th>
<th>Charge ($e$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>S</td>
<td>1.28</td>
<td>2.71</td>
<td>3.99</td>
<td>2.01</td>
</tr>
<tr>
<td>O</td>
<td>1.80–1.89</td>
<td>4.70–4.99</td>
<td>6.50–6.88</td>
<td>−0.50 to −0.88</td>
</tr>
<tr>
<td>N</td>
<td>1.65–1.66</td>
<td>4.00</td>
<td>5.65–5.66</td>
<td>−0.65 to −0.66</td>
</tr>
<tr>
<td>C</td>
<td>1.01–1.36</td>
<td>2.46–3.16</td>
<td>3.47–4.52</td>
<td>−0.53 to 0.52</td>
</tr>
<tr>
<td>H</td>
<td>0.52–0.69</td>
<td>0.0</td>
<td>0.52–0.69</td>
<td>0.48 to 0.31</td>
</tr>
</tbody>
</table>

are presented in Tables 1 and 2. Oxygen atoms of the $\mathrm{SO}_{4}$ groups are characterized by greater charges (−0.84 to −0.88) and smaller bond populations (0.54–0.59) than in the glycine groups, (−0.51 to −0.56) and (0.77–1.13), respectively. Two carbon atoms of the glycine groups have different charges: positive charge for that bonding with oxygen atoms, and negative one for that bonding with hydrogen atoms. The crystal possesses the hydrogen bonds O–H…O of different lengths (1.04–2.94 Å) and populations (0.50–0.01).

The results on DOS for the crystal studied are presented in Figs. 4 and 5. The upper part of the valence band (−3.0–0.5 eV) is mainly (95%) of $p$-character. In the

<table>
<caption>Table 2 Lengths and overlap populations of the typical atomic bonding bonds in TGS crystal</caption>
<thead>
<tr>
<th>Bond</th>
<th>Length (Å)</th>
<th>Population</th>
</tr>
</thead>
<tbody>
<tr>
<td>N–H</td>
<td>1.033–1.060</td>
<td>0.70–0.64</td>
</tr>
<tr>
<td>O–H</td>
<td>1.04–2.94</td>
<td>0.50–0.01</td>
</tr>
<tr>
<td>C–H</td>
<td>1.09–1.10</td>
<td>0.85–0.82</td>
</tr>
<tr>
<td>C–O</td>
<td>1.23–1.30</td>
<td>1.13–0.77</td>
</tr>
<tr>
<td>C–N</td>
<td>1.466–1.471</td>
<td>0.49–0.47</td>
</tr>
<tr>
<td>S–O</td>
<td>1.48–1.49</td>
<td>0.59–0.54</td>
</tr>
<tr>
<td>C–C</td>
<td>1.50–1.51</td>
<td>0.68–0.67</td>
</tr>
<tr>
<td>H–H</td>
<td>2.96–2.98</td>
<td>0.04</td>
</tr>
</tbody>
</table>

![](./images/812120499885703169_7.jpg)

Fig. 4. Densities of electron states (total, s and p) of TGS crystal at ferroelectric phase.

![](./images/812120499885703169_8.jpg)

Fig. 5. Densities of electron $p$-states (total, $\text{SO}_4$, and glycine) of TGS crystal at ferroelectric phase. In the insertion, densities of electron states (total, s and p) for atoms O, C, H, S, and N of the crystal.

valence band energy range $-10.0$ to $-3.0\,\text{eV}$, the part of $p$-states is equal to about $70\%$, whereas the part of $p$-states is about $20\%$ in the range $-23.0$ to $-11.0\,\text{eV}$ (Fig. 4).

The lower part of the conducting band (4.0–6.0 eV) is also mainly originated from p-character ($80\%$). An analysis of DOS in Fig. 5 reveals that both glycine and $\text{SO}_4$ groups give contributions to the density of p-states in the upper part of the valence band ($-3.0$–0.5 eV), whereas the lower part of the conducting band (4.0–6.0 eV) is formed predominantly ($98\%$) by the states of three glycine groups. Additional analysis has revealed that the DOS energy dependencies in this region for three different glycine groups are separated, that testifies the antibonding character of the corresponding electron states.

Analysis of the DOS by chemical elements has revealed that the predominant part of DOS in the range of $-3.0$ to $0.5\,\text{eV}$ ($92\%$) is formed by the 2p-states of oxygen (Fig. 5). In particular, the highest valence energy states at $E=-0.2\,\text{eV}$ are formed by the oxygen of $\text{SO}_4$-groups and glycine II group without “short hydrogen” near oxygen. The lower part of the conducting band (4.0–6.0 eV) is formed by carbon ($53\%$), oxygen ($30\%$), and hydrogen ($16\%$). The part of the hydrogen electron states in the range of $6.0$–11.0 eV is the greatest and is equal to about $45\%$. One of the clear peculiarities of the DOS of conducting band is also its mixed character related to the character (s-, and p-type) and origin (chemical elements) of electron states.

The pseudo-dielectric functions $\varepsilon'(E)$ and $\varepsilon''(E)$ of TGS crystal experimentally obtained for different geometries of the relative orientation “light—sample” are presented in Figs. 6 and 7. The dielectric functions $\varepsilon''(E)$ were calculated using the CASTEP code and experimentally measured using a synchrotron radiation's light reflection. The corresponding data are presented in Fig. 8. The experimental dependencies $\varepsilon''(E)$ are characterized by a clear spectral band in the range of $6.6$–8.2 eV and an increase in the range of $9.0$–10.0 eV (Figs. 6 and 7). The spectra of $\varepsilon''(E)$ depend significantly on the cut orientation of the sample surface. The most pronounced peak of $\varepsilon''(E)$ is observed at the photon energy $E=7.3\,\text{eV}$ for geometry 1, whereas this band is absent for geometry 3 (Fig. 6). The magnitudes of $\varepsilon'(E)$ at $E=4\,\text{eV}$ (Fig. 6) agree satisfactorily

![](./images/812120499885703169_9.jpg)

Fig. 6. Optical spectra of real $\varepsilon'(E)$ and imaginary $\varepsilon''(E)$ parts of pseudo dielectric permittivity of TGS crystals for different characteristic geometries and state of reflecting surface: Geom. 1—$Y$-cut cleaved, $E\parallel X$ mainly; Geom. 2—$Y$-cut cleaved, $E\parallel Z$ mainly; Geom. 3—$Z$-cut polished, $E\parallel Y$ mainly; Geom. 4—$Z$-cut polished, $E\parallel X$ mainly.

![](./images/812120499885703169_10.jpg)

Fig. 7. Optical spectra of real $\varepsilon'(E)$ and imaginary $\varepsilon''(E)$ parts of pseudo dielectric permittivity of TGS crystals for the characteristic geometry 2 (Y-cut cleaved, $\mathbf{E}||\mathbf{Z}$ mainly) and two kinds of the reflecting surface.

![](./images/812120499885703169_11.jpg)

Fig. 8. Theoretical spectra of the imaginary part $\varepsilon''(E)$ of dielectric permittivity of TGS crystals for the cartesian directions $\mathbf{X}$, $\mathbf{Y}$, $\mathbf{Z}$ and scissor factor 0.9 eV, and experimental spectrum of pseudo dielectric permittivity $\varepsilon''(E)$ for the characteristic geometry 1 (Y-cut cleaved, $\mathbf{E}||\mathbf{X}$ mainly).

with the square of the refractive indices of TGS crystals [10] mentioned in the Introduction.

The dielectric functions $\varepsilon'(E)$ and $\varepsilon''(E)$ of the TGS crystals obtained from the cleaved and polished surfaces of the same orientation are very close (Fig. 7). This means that the roughness degree of the polished surface does not substantially influence the dielectric functions of the crystal in the spectral range studied.

Comparative analysis of the experimental and theoretical dependencies of $\varepsilon''(E)$ of TGS crystal permits to state that the best fit of the theoretical dependencies $\varepsilon''(E)$ to the corresponding experimental ones takes place when a scissor factor of 0.9 eV is used (Fig. 8). The use of scissor factor is usually necessary to fit the DFT-based results of dielectric functions calculations to the corresponding experimental data. Taking this into account, one can state that the strong spectral band of $\varepsilon''(E)$ with maximum at $E=7.3$ eV corresponds to direct optical transitions at the $\Gamma$-, $Y$-, $B$, and $E$-points between the highest valence band ($-1.07$ to $-0.25$ eV), and the conducting band (5.4-6.5 eV) (Fig. 2). These transitions are associated with the valence p-states of oxygen and, predominantly, with the conducting states of hydrogen and carbon (Fig. 5). When these valence p-states of oxygen are flat and therefore are of localized type, the corresponding conducting states of hydrogen and carbon are rather of the band character (Fig. 2). High anisotropy of the functions $\varepsilon''(E)$ in the spectral region of $E=7.3$ eV and peculiarities of the placement of the crystal's fragments in the unit cell give possibility to suggest that the mentioned valence p-states of oxygen are associated with $\text{SO}_4$ groups, whereas the conducting states of hydrogen and carbon belong mainly to the glycine I.

Similar analysis of the experimental and theoretical dielectric functions $\varepsilon''(E)$, band dispersion $E(\boldsymbol{k})$, and densities of states for the TGS crystal give possibility to assign the experimental maxima of $\varepsilon''(E)$ at 8.35 and 9.55 eV to the transitions between the oxygen valence p-states, probably partially delocalized, and lower lying delocalized states of the conducting band ($E>6.0$ eV).

Small maxima of the theoretical functions of $\varepsilon''(E)$ in the range of 5.4-7.0 eV (Fig. 8), corresponding to the low-probable direct transitions (indirect transitions) between the top of valence band and the conducting states of the range 4.4-5.4 eV (Fig. 2), are also seen on the experimental dielectric function $\varepsilon''(E)$. Taking into account (a) the flat energy dispersions $E(k)$ of these states (Fig. 2) and (b) the corresponding peculiarities of densities of electron states for different atoms, one can state that these optical transitions are of localized type and take place between the p-states of oxygen atoms of separate glycine groups.

### 5. Conclusions

On the basis of the performed investigations one can conclude that for the first time the band structure, density of electron states, and optical dielectric functions were calculated for TGS crystal in the spectral energy range covering $-23$-$18$ eV.

The dispersions of energy bands $E(\boldsymbol{k})$ of TGS crystals are mainly flat with great effective masses $m^{*} \geqslant 10m_\text{e}$, however smaller magnitudes of the effective mass ($m^{*} \approx 0.5m_\text{e}$) take place on certain division of the Brillouin zone. Energy band gap of TGS crystal is confirmed to be indirect and corresponds to the optical transition between $\Gamma$ and $D$ points of the Brillouin zone.

Mulliken population analysis of the crystal reveals the hydrogen bonds O-H...O of different lengths (1.04-2.94 Å) and populations (0.50-0.01).

The upper part of the valence band ($-3.0$-$0.5$ eV) is mainly (95%) of of 2pO-origin. The electron states of the lower part of the conducting band (4.0-6.0 eV) are also mainly of the p-states (80%) originated from three glycine groups having antibonding character.

The theoretical dielectric functions $\varepsilon''(E)$ of TGS crystal agree satisfactorily with corresponding experimental dependencies obtained in the spectral range of 4.0-10.0 eV.

Strong spectral band of $\varepsilon''(E)$ with maximum at $E=7.3\,\text{eV}$ corresponds to the direct optical transitions in the $\Gamma$-, $Y$-, $B$, and $E$-points of BZ between the upper valence band at $-1.07$ to $-0.25\,\text{eV}$ and the conducting band at $5.4$–$6.5\,\text{eV}$.

Long-wavelength fundamental optical absorption of TGS crystal ($E\approx5.0\,\text{eV}$) can be assign to the indirect transitions of localized type realizing between the $p$-states of oxygen atoms of separate glycine groups.

## Acknowledgment

The authors are thankful for Professor Zbigniew Czapla from Wroclaw University, who kindly presented TGS crystals for investigations.

## References

[1] S. Hoshino, I. Okaya, R. Pepinsky, Phys. Rev. 115 (1959) 323.
[2] K. Iton, T. Mitsui, Ferroelectrics 5 (1973) 235.
[3] M.I. Kay, R. Kleinberg, Ferroelectrics 5 (1973) 45.
[4] S.R. Fletcher, E.T. Keve, A.C. Skapski, Ferroelectrics 14 (1976) 775.

[5] M.E. Lines, A.M. Glass, Principles and Application of Ferroelectrics and Related Materials, Clarendon Press, Oxford, 1977.
[6] H.V. Alexandru, C. Berbecaru, F. Stanculescu, L. Pintilie, I. Matei, M. Lisca, Sens. Actuat. A 113 (2004) 387.
[7] D. Barosova, S. Panos, Sens. Actuat. A 110 (2004) 350.
[8] B. Andriyevsky, O. Myshchyshyn, M. Romanyuk, Phys. Stat. Sol. B 203 (1997) 549.
[9] N.A. Romanyuk, B.V. Andriyevsky, I.S. Zheludev, Ferroelectrics 21 (1978) 333.
[10] N.A. Romanyuk, A.M. Kostetsky, B.V. Andriyevsky, Phys. Sol. State 19 (1977) 3095.
[11] V. Milman, B. Winkler, J.A. White, C.J. Pickard, M.C. Payne, E.V. Akhmatskaya, R.H. Nobes, Int. J. Quant. Chem. 77 (2000) 895.
[12] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, C. Fiolhais, Phys. Rev. B 46 (1992) 6671.
[13] D. Vanderbilt, Phys. Rev. B 41 (1990) 7892.
[14] T. Wethkamp, K. Wilmers, N. Esser, W. Richter, O. Ambacher, H. Angerer, G. Jungk, R.L. Johnson, M. Cardona, Thin Solid Films 313–314 (1998) 745.
[15] R.M.A. Azzam, N.B. Bashara, Ellipsometry and Polarized Light: North-Holland Personal Library, Amsterdam, 1987 (paperback edition).
[16] A. Abu El-Fadl, Physica B 269 (1999) 60.
[17] I.V. Kityk, A. Mefleh, Physica B 262 (1999) 170.
[18] P. Smok, I.V. Kityk, J. Berdowski, Physica B 328 (2003) 163.