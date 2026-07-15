![](./images/812518483374899201_1.jpg)

**Materials Chemistry and Physics**

journal homepage: www.elsevier.com/locate/matchemphys

![](./images/812518483374899201_2.jpg)

![](./images/812518483374899201_3.jpg)

# Electronic structure and optical constants of CsPbCl₃: The effect of approaches within ab initio calculations in relation to X-ray spectroscopy experiments

Tuan V. Vu $^{a,b}$, A.A. Lavrentyev $^{c}$, B.V. Gabrelian $^{d}$, Khang D. Pham $^{e}$, O.V. Parasyuk $^{f}$, N. M. Denysyuk $^{g}$, O.Y. Khyzhun $^{g,*}$

$^{a}$ Division of Computational Physics, Institute for Computational Science, Ton Duc Thang University, Ho Chi Minh City, Vietnam
$^{b}$ Faculty of Electrical & Electronics Engineering, Ton Duc Thang University, Ho Chi Minh City, Vietnam
$^{c}$ Department of Electrical Engineering and Electronics, Don State Technical University, 1 Gagarin Square, 344010, Rostov-on-Don, Russian Federation
$^{d}$ Department of Computational Technique and Automated System Software, Don State Technical University, 1 Gagarin Square, 344010, Rostov-on-Don, Russian Federation
$^{e}$ Military Institute of Mechanical Engineering, Ha Noi, Vietnam
$^{f}$ Department of Inorganic and Physical Chemistry, Lesya Ukrainka Eastern European National University, 13 Voli Avenue, 43025, Lutsk, Ukraine
$^{g}$ Frantsevych Institute for Problems of Materials Science, National Academy of Sciences of Ukraine, 3 Krzhyzhanivsky Street, 03142, Kyiv, Ukraine

---

## HIGHLIGHTS

- Total and projected DOS of $CsPbCl_3$ are computed within different approaches.
- Electronic structure of $CsPbCl_3$ crystal is studied experimentally by XPS and XES.
- The mBJ + U + SO calculations fit well data of XPS and XES measurements.
- Main optical constants of $CsPbCl_3$ are clarified by mBJ + U + SO calculations.

---

## ARTICLE INFO

**Keywords:**
Ab initio band-structure calculations
XPS
Electronic structure
Optical properties
Semiconductors

## ABSTRACT

We report on experimental and theoretical studies of the electronic structure and optical properties of cesium lead chloride, $CsPbCl_3$. We employ X-ray photoelectron spectroscopy (XPS) to determine binding energies of core-level electrons of as-grown surface of $CsPbCl_3$ crystal and to measure the energy distribution of electronic states in the valence band region. To achieve the best agreement between the shape and energy positions of peculiarities of the XPS valence-band spectrum and the curve of total density of states, we used various approaches treating exchange-correlation potential. In particular, we have realized that the fair agreement is derived when performing calculations within a density functional theory framework using modified Becke-Johnson potential and treating the Hubbard parameter U and spin-orbit coupling. Using possibilities of this technique, we study in detail curves of partial density of states, energy band dispersion, and principal optical constants of $CsPbCl_3$.

---

## 1. Introduction

In recent years, a substantial increase in studies of group IV metal all-inorganic halide perovskite compounds is observed. These compounds are known to exist as early as the 1950s, starting from pioneering work by Moller on $CsPbX_3$ (X = Cl, Br, I) halides [1]. Since then, great efforts have been made from both scientific and technologic viewpoints to explore their physicochemical properties because the $CsPbX_3$ halides reveal unique optical and electrical properties [2]. The $CsPbX_3$ halides attract significant attention as very promising luminophores offering substantial improvements of optoelectronic materials, in particular diodes for light-emitting applications, lasers, waveguides, and photodetectors [3,4]. The $CsPbX_3$ compounds are prospective materials for application in photovoltaic devices [5] and being nanoparticles they

---

* Corresponding author.
E-mail addresses: vuvantuan@tdtu.edu.vn (T.V. Vu), alavrentyev@dstu.edu.ru (A.A. Lavrentyev), khyzhun@ipms.kiev.ua (O.Y. Khyzhun).

https://doi.org/10.1016/j.matchemphys.2020.124216
Received 1 June 2020; Received in revised form 21 December 2020; Accepted 29 December 2020
Available online 6 January 2021
0254-0584/© 2020 Elsevier B.V. All rights reserved.

reveal strong and tunable emission and are considered to be very promising for substitution of chalcogenide-bearing quantum dots that are most susceptible to photodegradation [6].

Cesium lead chloride, $CsPbCl_3$, a representative member of the above-mentioned $CsPbX_3$ ($X = Cl, Br, I$) halide family, is of special interest, particularly with respect to a number of temperature-induced phase transitions. The crystal structure of $CsPbCl_3$ was a matter of controversy for a long time. Shirotsu and Sawada [7] reported that $CsPbCl_3$ undergoes a cubic to tetragonal phase transition at $47\ ^\circ C$ and below this temperature predict the ternary chloride under discussion reveals superstructure formation. Fujii et al. [8] and Plesko et al. [9] have established that at room temperature $CsPbCl_3$ exists either in monoclinic $(C_{2h}^2 = P2_1/m)$ or in orthorhombic $(D_{2h}^{16} = Pnma)$ structure type. However, in the temperature range close to room temperature, $CsPbCl_3$ undergoes three phase transitions [8,9], and additional phase transition is detected when cooling $CsPbCl_3$ below $-80\ ^\circ C$ [10]. Recent crystal-structure refinement of $CsPbCl_3$ performed by Zhang et al. [11] indicates that this ternary chloride crystallizes in orthorhombic Pbnm structure with unit-cell parameters as follows: $a = 5.860$ Å, $b = 7.9260$ Å, and $c = 11.2451$ Å.

During past several years, numerous extraordinary properties were discovered to exist in $CsPbCl_3$ crystals, in particular when reducing crystal dimensions, doping with other chemical elements or surface passivation. Inorganic perovskite $CsPbCl_3$ is a wide band gap semiconductor revealing a transparency to visible light radiation but sensitivity to UV radiation [12]. Since the band gap increases in semiconductors/insulators as their size decreases, recently the optical band gap of $CsPbCl_3$ is generally adjusted by changing the crystal dimensions to nanometer sizes. Rare-earth co-doped $CsPbCl_3$ nanocrystals are considered very promising materials for application in solar-energy-conversion technologies. Milstein et al. [13] have detected picoseconds quantum cutting generation of photoluminescence quantum yield of $\sim$100% in $Yb^{3+}$ doped $CsPbCl_3$ nanocrystals. Ahmed et al. [14] have reported on enormous photoluminescence detected in nanosize $CsPbCl_3$ through simultaneous dual-surface passivation using trivalent metal ion salt (in fact, $YCl_3$). This technology enhances photoluminescence quantum yield up to 60% without changes in sizes and crystal structure of $CsPbCl_3$ nanocrystals [14]. Lin et al. [15] reported that emission color of Mn-doped $CsPbCl_3$ nanocrystals could be adjusted via full visible spectral range promoting them to be promising for light-emitting application, while dual ion $Bi^{3+}/Mn^{2+}$ $CsPbCl_3$ nanocrystals reveal tunable emission spanning the broad region of correlated color temperature under UV excitation [16]. Striking blue-violet photoluminescence and high luminescence quantum yield up to 36.5% was reported to exist for $La^{3+}/F^-$ ion co-doped $CsPbCl_3$ quantum dots (QDs) making them very prospective materials for anti-counterfeiting [17]. In addition, $CsPbCl_3$ QDs doped with $Ce^{3+}$ ions are promising for luminescent thermometers [18]. It is worth mentioning that ternary $CsPbCl_3$ chloride, as well as its bromine- and iodine-bearing counterparts, possesses narrow emission bandwidth and broad band absorption, large lengths of exciton diffusion, appropriate electron mobility, composition-tailoring emission wavelengths, strong absorption of UV light, good photoresponsibility $(1.89\ A\ W^{-1})$ and a big on/off ratio (till $10^3$), etc. [12,19].

The above intriguing properties of $CsPbCl_3$ have stimulated scientists to explore its electronic structure based on band-structure calculations of densities of states (DOS). This is due to the fact that, the knowledge of chemical bond formation, peculiarities of charge transfer and cohesion energy of chemical bonds plays a substantial role in understanding physical and chemical properties of a solid and predicting possible ways to tailor them to desirable technological demands [20,21]. Zhang el al [11]. have performed band-structure calculations based on density functional theory (DFT) within generalized gradient approximation (GGA) [22] to explore behaviour of the energy band gap, $E_g$, under high pressure and established decreasing $E_g$ value with pressure increasing from ambient conditions till 2.0 GPa. However, with further increasing pressure, the band gap was theoretically found to increase in $CsPbCl_3$ from 2.34 eV till 2.63 eV [11]. Pandey et al. [23] using the same GGA approach for exchange-correlation (XC) potential have explored the influence of manganese dopants on the band structure of the ternary chloride under discussion and found that the conduction band minimum moves downwards by 0.850 eV compared to undoped $CsPbCl_3$. Ilyas and Elias [24] have employed both GGA [22] and local density approximation (LDA) [25] techniques to explore the influence of pressure upon the electronic band structure, elastic, acoustic and thermodynamic properties of $CsPbCl_3$ and their results predict metallic nature of this ternary chloride at pressures above 30 GPa. Taking into account the fact that GGA [22] and LDA [25] approaches in XC potential generally result in far underestimation of $E_g$ values in semiconductors and insulators, Ahmad et al. [26] have employed modified Becke-Johnson potential in the form of Tran and Blaha [27] and found that the $CsPbX_3$ ($X = Cl, Br, I$) halides are semiconductors with energy band gaps changing from 0.79 to 2.54 eV.

However, all the above-mentioned band-structure calculations do not give any comparison of DOS curves of $CsPbCl_3$ with experimental measurements of the energy distribution of the electronic states in the valence band region of this ternary chloride. To fill this lack, in the present work we perform a complex study of the electronic band structure of $CsPbCl_3$ using both theoretical and experimental methods. In particular, using an optical quality $CsPbCl_3$ crystal, with the aim of exploring the nature of the chemical bonding and peculiarities of filling the valence band region by electronic states of the atoms constituting this crystal, we measure the core-level binding energies and the XPS valence-band spectra. Further, we examine different approaches for XC potential, as well as spin-orbit (SO) coupling and Hubbard parameter U effects, to achieve the best correspondence of total DOS curve with the XPS valence-band spectrum of $CsPbCl_3$. Based on the best agreement of the theoretical and experimental data, we calculate the main optical properties of the $CsPbCl_3$ crystal. Furthermore, we explore the effect of middle-energy $Ar^+$ ion-irradiation of the $CsPbCl_3$ crystal surface because such surface treating procedure gives a possibility to evaluate relative stability of the chemical bonds in a solid and middle-energy irradiation is generally used in epitaxial technological processes [28]. Furthermore, the $CsPbCl_3$ compound, to the best of our knowledge, has never been studied with X-ray emission spectroscopy (XES) giving a possibility to probe experimentally the energy distribution of partial DOS in solids.

## 2. Experimental

For the present experimental studies of the XPS spectra, both core-level and representing energy distribution of valence electrons, we deal with the $CsPbCl_3$ crystal grown by Bridgman-Stockbarger method. The calculated weights of binary chlorides ($CsCl$ and $PbCl_2$) were used as initial substances for a batch composition. The main details of the synthesis are similar to that reported earlier for related lead-bearing ternary iodide, $TlPbl_3$ [29]. The structure of the $CsPbCl_3$ single crystal was examined using powder X-ray diffraction (XRD) technique (a digital DRON 4-13 diffractometer, $Cu\ K\alpha$ radiation) and the recorded XRD pattern (not presented here) was found to be consistent with literature data [11]. The XPS measurements were performed with the UHV-Analysis-System produced by SPECS Surface Nano Analysis Company (Germany) for the $CsPbCl_3$ crystal shaped in the form of a parallelepiped with dimensions $7.4 \times 4.3 \times 1.4\ mm^3$. The XPS spectra were excited employing an X-ray $Mg\ K\alpha$ source ($h\nu = 1253.6$ eV) and the spectra were recorded at residual pressure less than $7.4 \cdot 10^{-8}$ Pa in the operation chamber of the UHV-Analysis-System and measured at a constant pass energy of 35 eV. Since XPS is known to be a technique which is rather sensitive to the charging surface effect, we compensated this effect using the adventitious carbon 1s line by its reference to 284.6 eV as recommended for such kind of halides [29,30]. The parameters of an ion source when treating the $CsPbCl_3$ crystal surface with $Ar^+$ ion-irradiation are the same as we used earlier for related ternary halides

![](./images/812518483374899201_4.jpg)

Fig. 1. (a) Crystal structure of CsPbCl₃ (unit cell is outlined), (b) viewing along the z-axis, (c) staking of the PbCl₆ octachedra, coordination surrounding and inter-atomic distances of (d) lead and (e) cesium atoms in the CsPbCl₃ structure.

<table>
<caption>Table 1
Atomic positions in the unit cell of CsPbCl₃ (orthorhombic space group Pbnm, a = 7.8600 Å, b = 7.9260 Å, c = 11.2451 Å [11]) as treated in the present band-structure calculations.</caption>
<thead>
<tr>
<th>Atom</th>
<th>x</th>
<th>y</th>
<th>z</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cs</td>
<td>0.99000</td>
<td>0.97100</td>
<td>0.25000</td>
</tr>
<tr>
<td>Pb</td>
<td>0.00000</td>
<td>0.00000</td>
<td>0.04499</td>
</tr>
<tr>
<td>Cl₁</td>
<td>0.05737</td>
<td>0.52188</td>
<td>0.25000</td>
</tr>
<tr>
<td>Cl₂</td>
<td>0.80840</td>
<td>0.19243</td>
<td>0.02481</td>
</tr>
</tbody>
</table>

![](./images/812518483374899201_5.jpg)

Fig. 2. Survey XPS spectra measured for the CsPbCl₃ crystal: (1) as-synthesized surface, and (2) surface irradiated with 3000 eV Ar⁺ ions.

[29,30]: 3000 eV, duration ~ 5 min, current density ~17 μA cm⁻², total flux of Ar⁺ ions ~5.3·10¹⁶ ions·cm⁻². The XES Cl Kβ₁ band arising due to the transition K → M_II,III was measured employing a Johann-type X-ray spectrometer with the spectrometer energy resolution of about 0.3 eV following the technique [31]. The operation conditions of an X-ray source (Au-anode) were set as following: anode current, Iₐ = 67 mA, accelerating voltage, Uₐ = 38 kV.

### 3. Computing methodology

Fig. 1a presents the crystal structure of CsPbCl₃ that can be viewed as composing of PbCl₆ octahedra stacked well along the c axis (Fig. 1b), while Cs atoms are positioned in the interstitials formed by the PbCl₆ octahedra (Fig. 1c). Within the (ab) plane, the PbCl₆ octahedra contain four Cl atoms with two Pb-Cl distances equal to 2.88 Å, and two other distances are slightly smaller. While for two chlorine atoms along the c axis, the Pb-Cl distances are equal to 2.85 Å (Fig. 1d). Six Cl atoms are in the nearest surrounding of the Cs atoms. The Cs-Cl distances range from 3.40 Å to 3.71 Å (Fig. 1e). Therefore, in the CsPbCl₃ structure, the Cs-Cl distances are much longer as compared to the Pb-Cl distances.

The present DFT calculations of CsPbCl₃ are made within the augmented plane wave + local orbitals (APW-lo) method as implemented in WIEN2k code [32]. Muffin-tin sphere radii were employed as following: 2.50 a.u. (cesium), 2.50 a.u. (lead), and 2.41 a.u. (chlorine). It is worth mentioning that 1 a.u. = 0.529177 Å. The lattice parameters a = 7.8600 Å, b = 7.9260 Å, c = 11.2451 Å and atomic positions (Table 1) were used as reported elsewhere [11]. The $R_{min}^{MT}k_{max}=8$ parameter was employed in the present calculation procedure (note: $R_{min}^{MT}$ is a smallest radius of the muffin-tin sphere, $k_{max}$ is the maximum $k$ vector in the process of plane wave deconvolution), whereas Fourier charge density was extended till $G_{max}=14$ (a.u.)⁻¹. To find the best correspondence of the curve of total DOS to the shape of the XPS valence-band spectrum of the CsPbCl₃ crystal, we treat different XC potentials, in particular GGA in the form of Perdew-Burke-Ernzerhof [22] and modified Becke-Johnson (mBJ) potential in the form of Tran-Blaha (TB-mBJ) [27]. Since we have started using GGA for XC potential in our calculations, further APW-lo calculations are made within GGA + mBJ. However, we shall refer the latter approach to mBJ, for convenience. Furthermore, we involve also the Hubbard correction parameter U as elaborated in Ref. [33] and the spin-orbit (SO) coupling effect (we shall refer this technique to mBJ + U + SO, for clarity). The SO coupling effect was involved in the calculation procedure following the second variational method as reported in Ref. [34]. Integration through the Brillouin zone (BZ) is made adopting the tetrahedron method [35]; for such a goal, a grid consisting of 1000 $k$-points is applied. The calculation process was verified through the convergence value $q=\int |\rho_n - \rho_{n-1}|dr$, where $\rho_{n-1}(r)$ and $\rho_n(r)$ are tentative and following charge density, respectively, and the computation process was interrupted when achieving the case $q \leq 0.0001$ as it is suggested for such kind of ternary halides [36]. When achieving the best agreement of total DOS curve to the shape of the XPS valence-band spectrum of the CsPbCl₃ crystal, such main optical constants as $\alpha(\omega)$ (absorption coefficient), $k(\omega)$ (extinction coefficient), $n(\omega)$ (refractive index), $R(\omega)$ (optical reflectivity) and $L(\omega)$ (electron energy-loss spectrum) were derived employing the well-known relations involving the real $\varepsilon_1(\omega)$ and imaginary $\varepsilon_2(\omega)$ components of the complex dielectric function $\varepsilon(\omega)=\varepsilon_1(\omega)+i\varepsilon_2(\omega)$ as they are reported elsewhere [37,38]. A grid consisting of 3000 $k$-points was applied in the case of calculations of the above-mentioned optical properties. The linear optical properties of CsPbCl₃ were studied using the program OPTIC integrated in WIEN2k code [32]. Direct transitions between the valence band and the conduction band are taken into account in the present calculations of the optical constants as recommended for related ternary halides [30,38].

![](./images/812518483374899201_6.jpg)

Fig. 3. Core-level XPS spectra of (a) Cs 4d, (b) Pb 4f, (c) Cl 2p, (d) Pb 4d, and (e) Cs 3d measured for the CsPbCl₃ crystal: (1) as-synthesized surface, and (2) surface irradiated with 3000 eV Ar⁺ ions.

<table>
<thead>
<tr>
<th colspan="3">Table 2</th>
</tr>
<tr>
<th colspan="3">Binding energies (±0.05 eV) of core level electrons of the CsPbCl₃ crystal.</th>
</tr>
</thead>
<tbody>
<tr>
<td>Core-level</td>
<td>CsPbCl₃/pristine surface</td>
<td>CsPbCl₃/Ar⁺-irradiated surface</td>
</tr>
<tr>
<td>Pb 5d₅/₂</td>
<td>19.30</td>
<td>19.36</td>
</tr>
<tr>
<td>Pb 5d₃/₂</td>
<td>21.94</td>
<td>21.90</td>
</tr>
<tr>
<td>Cs 4d₅/₂</td>
<td>75.11</td>
<td>75.13</td>
</tr>
<tr>
<td>Cs 4d₃/₂</td>
<td>76.85</td>
<td>76.89</td>
</tr>
<tr>
<td>Pb 4f₇/₂</td>
<td>138.12</td>
<td>138.06</td>
</tr>
<tr>
<td>Pb 4f₅/₂</td>
<td>142.98</td>
<td>142.94</td>
</tr>
<tr>
<td>Cl 2p</td>
<td>197.92</td>
<td>197.87</td>
</tr>
<tr>
<td>Cl 2s</td>
<td>268.48</td>
<td>268.55</td>
</tr>
<tr>
<td>Pb 4d₅/₂ᵃ</td>
<td>413.2</td>
<td>413.3</td>
</tr>
<tr>
<td>Pb 4d₃/₂ᵃ</td>
<td>435.6</td>
<td>435.6</td>
</tr>
<tr>
<td>Cs 3d₅/₂</td>
<td>724.03</td>
<td>724.10</td>
</tr>
<tr>
<td>Cs 3d₃/₂</td>
<td>738.01</td>
<td>738.08</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="3">ᵃ Uncertainty of determination: ±0.1 eV.</td>
</tr>
</tfoot>
</table>

## 4. Results and discussion

### 4.1. XPS core-level and valence-band spectra

Survey XPS spectra measured in the present work for as-synthesized and treated with Ar⁺ ions surfaces of the CsPbCl₃ crystal are shown in Fig. 2. All the XPS spectral features, as evidenced from Fig. 2, are well ascribed to the chemical elements constituting the CsPbCl₃ crystal. The exceptions are only the XPS features ascribed to carbon and oxygen. It is well known that the XPS technique is rather sensitive to surface contaminations associated with hydrocarbon adsorbates originating from air. Since prior to the present XPS measurements the surface of the CsPbCl₃ crystal contacted to laboratory air for about a week, we observed carbon(oxygen) 1s levels originated by hydrocarbon- and oxygen-bearing adsorbed species. These species are easily removed from the pristine CsPbCl₃ crystal surface by 5 min treatment with the Ar⁺ ions leading to almost complete elimination of the carbon(oxygen) 1s lines on the survey XPS spectrum. Therefore, by analogy with other Cs- or Pb-bearing ternary halides [30,36,38], the CsPbCl₃ crystal is rather low hygroscopic that may be of importance in the case of practical using such a crystal in optoelectronic devices operating at ambient conditions.

A set of the most informative XPS spectra investigated for core-level electrons of the atoms constituting the CsPbCl₃ crystal is presented in Fig. 3, while Table 2 summarizes the binding energies of those core-level electrons. Following the expected charge balance in CsPbCl₃, one can ascribe the composing atoms to formal valences as following: Cs¹⁺, Pb²⁺, Cl⁻. Comparison of the binding energy values listed in Table 2 with literature data on available XPS studies of cesium- and lead-bearing compounds reported in Refs. [30,38,39] gives us ability to conclude that the charge state of Cs in the CsPbCl₃ crystal is near to +1, while the charge state of Pb is substantially smaller than +2, as expect to occur from the atomic charge balance. This result is reasonably to explain by an essential covalent constituent of Pb-Cl bonds in the CsPbCl₃ crystal. As can be noticed from Fig. 3 and data reported in Table 2, the treatment

![](./images/812518483374899201_7.jpg)

Fig. 4. XPS valence-band spectra measured for the $CsPbCl_3$ crystal: (1) as-synthesized surface, and (2) surface irradiated with $3000$ eV $Ar^+$ ions.

![](./images/812518483374899201_8.jpg)

Fig. 5. Curves of total DOS of $CsPbCl_3$ as derived in the theoretical calculations performed within GGA, mBJ, GGA + U and mBJ + U + SO approaches in comparison with the XPS valence-band spectrum of the $CsPbCl_3$ crystal.

with $3000$ eV $Ar^+$ ions over 5 min does not lead to the formation of new features of the XPS core-level spectra, changes in their maxima positions as well as redistribution of the electronic states within the valence-band region of the $CsPbCl_3$ crystal (Fig. 4). This means that such a surface treatment does not lead to the preferential etching of some chemical elements from topmost surface layers unlike other Cs-bearing ternary halide crystals with the common formula $Cs_2HgX_4$ (X = Cl, Br, I) reveal [30,38,40] in which the same $Ar^+$ ion-treatment induced substantial

![](./images/812518483374899201_9.jpg)

Fig. 6. Band structures of $CsPbCl_3$ calculated using GGA, mBJ, GGA + U, and mBJ + U + SO techniques (Note: the Fermi level is positioned at zero energy).

<table>
<caption>Table 3
Energy band gaps as determined by the present DFT calculations and measured experimentally for $CsPbCl_3$.</caption>
<thead>
<tr>
<th>Methods</th>
<th>$E_g$ – theory</th>
<th>$E_g$ – experiment</th>
</tr>
</thead>
<tbody>
<tr>
<td>GGA</td>
<td>2.547 eV</td>
<td>2.97 eV [11]</td>
</tr>
<tr>
<td>mBJ</td>
<td>3.415 eV</td>
<td>2.85 eV [49]</td>
</tr>
<tr>
<td>GGA + U</td>
<td>2.549 eV</td>
<td></td>
</tr>
<tr>
<td>mBJ + U + SO</td>
<td>2.431 eV</td>
<td></td>
</tr>
</tbody>
</table>

![](./images/812518483374899201_10.jpg)

Fig. 7. Comparison on a common energy scale of curves of total and main projected densities of states as calculated within mBJ + U + SO approach and the XPS valence-band spectrum of the $CsPbCl_3$ crystal.

decreasing (nearly complete elimination in some cases) of the mercury content. Therefore, the present XPS results indicate significant surface stability of the $CsPbCl_3$ crystal. The same peculiarity has been reported to be characteristic of some lead-containing ternary chlorides, in particular $Tl_3PbCl_5$ [41] and $TlPb_2Cl_5$ [42].

![](./images/812518483374899201_11.jpg)

Fig. 8. Curves of projected densities of states of (a) Cs, (b) Pb, and (c) Cl of CsPbCl₃.

### 4.2. Electronic structure as elucidated by DFT calculations and X-ray spectroscopy measurements

Fig. 5 presents the results of calculations of total DOS curves using different techniques, while Fig. 6 presents band dispersion along different directions as defined by high-symmetry points. It is worth noting that the coordinates of the BZ k points, within the confined area of the BZ investigated for band dispersion plotted in Fig. 6, are as follows: $\Gamma$ (0 0 0 0), X (0 0.5 0), M (0.5 0.5 0), Z (0 0 0.5), R (0 0.5 0.5), and A (0.5 0.5 0.5). DFT calculations employing GGA approach for XC potential are generally used for band-structure calculations of semi-conducting/insulating materials like chalcogenides, halides and oxides [43-45]. As can be noticed from Fig. 5, application of different techniques does not influence much the shape of total DOS curves within the valence band region corresponding to the peculiarities labelled A and B of the XPS valence-band spectrum. However, substantial differences are observed in DFT calculations of dipper electronic levels. Fig. 5 presents that the calculations within GGA approach give somewhat underestimated binding energy position for Pb 5d sates. In fact, the sub-band associated with Pb 5d states as calculated by GGA approach is shifted by more than 1 eV toward the Fermi energy in comparison to its correct position in the CsPbCl₃ compound as depicted by the feature E of the XPS valence-band spectrum (Fig. 5). However, in spite of the fact that GGA technique generally reveals far underestimated $E_g$ values for semiconductors/insulators, in our case, it yields the energy band gap value (2.547 eV, Table 3) that is not much underestimated from those determined by the experimental measurements reported elsewhere. The application of mBJ potential causes a shift of the Pb 5d sub-band toward its correct position (Fig. 5); however, it obviously overestimates the $E_g$ value (3.415 eV, Table 3). The use of the Hubbard correction parameter U for Pb 5d electrons to be equal to 0.294 Ry in GGA approach overestimates the energy position of the sub-band associated with Pb 5d sates (Fig. 5) and does not induce changes in the energy band gap value (2.549 eV vs. 2.547 eV, Table 3). It is worth mentioning that, since the U value is very difficult to obtain theoretically, the present value was derived as an adjusting parameter to find the best correspondence of the theoretical total DOS curve to the experimental XPS valence-band spectrum. Our previous band-structure calculations have revealed that the application of the Hubbard parameter U does not influence the energy distribution of the electronic states within valence band and conduction band regions of Tl-based halides [46-48]. The best correspondence of the shapes of the total DOS curve and the XPS valence-band spectrum is detected, however, in the case of the calculations performed within the mBJ + U + SO technique using the same U value as in the case of the GGA + U calculations (Figs. 5 and 7). In such a case, the $E_g$ value (2.431 eV, Table 3) is comparative with those derived within GGA and GGA + U approaches. Fig. 6 presents that all the approaches used in the present calculations allow for concluding that in the CsPbCl₃ compound the valence band maximum and the conduction band minimum are positioned at $\Gamma$ point (center of the BZ). Therefore, the CsPbCl₃ compound is a direct-gap semiconductor.

Detailed curves of partial DOS are shown in Fig. 8. From this figure, it is evident that the main contributors to the band A of the XPS valence-band spectrum of CsPbCl₃ are Cl 3p states revealing the principal contributions to its central part, as well as at its bottom and top. Pb 6s states contribute to the lower part of the band A of the XPS valence-band spectrum of CsPbCl₃, while Pb 6p states bring main input to its top. Electronic states associated with cesium are almost not detected by the present DFT calculations in the band A of the XPS spectrum; however, Cs 5p states contribute substantially in the energy region just below the

![](./images/812518483374899201_12.jpg)

Fig. 9. The XPS valence-band spectrum and the XES Cl Kβ₁ band matched on a common energy scale for the CsPbCl₃ crystal.

<table>
<caption>Table 4 Static values of the real component $\varepsilon_1(\omega)$ of complex dielectric function, the refractive index $n(\omega)$ and the reflectivity coefficient $R(\omega)$ of CsPbCl₃.</caption>
<thead>
<tr>
<th>Component</th>
<th>GGA</th>
<th>mBJ</th>
<th>GGA + U</th>
<th colspan="2">mBJ + U + SO</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th>Without scissons corrections</th>
<th>With scissons corrections</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\varepsilon_1^{xx}(0)$</td>
<td>3.966</td>
<td>3.154</td>
<td>3.928</td>
<td>5.522</td>
<td>5.203</td>
</tr>
<tr>
<td>$\varepsilon_1^{yy}(0)$</td>
<td>3.972</td>
<td>3.158</td>
<td>3.931</td>
<td>5.530</td>
<td>5.210</td>
</tr>
<tr>
<td>$\varepsilon_1^{zz}(0)$</td>
<td>4.065</td>
<td>3.223</td>
<td>4.023</td>
<td>5.688</td>
<td>5.344</td>
</tr>
<tr>
<td>$n^{xx}(0)$</td>
<td>1.992</td>
<td>1.776</td>
<td>1.982</td>
<td>2.350</td>
<td>2.281</td>
</tr>
<tr>
<td>$n^{yy}(0)$</td>
<td>1.993</td>
<td>1.777</td>
<td>1.983</td>
<td>2.352</td>
<td>2.282</td>
</tr>
<tr>
<td>$n^{zz}(0)$</td>
<td>2.016</td>
<td>1.795</td>
<td>2.006</td>
<td>2.385</td>
<td>2.312</td>
</tr>
<tr>
<td>$R^{xx}(0), (\%)$</td>
<td>10.987</td>
<td>7.814</td>
<td>10.844</td>
<td>16.240</td>
<td>15.245</td>
</tr>
<tr>
<td>$R^{yy}(0), (\%)$</td>
<td>11.008</td>
<td>7.830</td>
<td>10.857</td>
<td>16.264</td>
<td>15.265</td>
</tr>
<tr>
<td>$R^{zz}(0), (\%)$</td>
<td>11.352</td>
<td>8.096</td>
<td>11.197</td>
<td>16.740</td>
<td>15.688</td>
</tr>
</tbody>
</table>

band A forming the sub-bands B and C of the XPS spectrum. Cl 3s states form the band D centred at about −14.4 eV and, finally, Pb 5d states give main contributions to the bands E and F of the XPS spectrum of CsPbCl₃. Theoretical separation of the bands E and F is equal to 2.6 eV, as evidenced from mBJ + U + SO calculations, and it is in excellent agreement with the experimental measurements of the separation of Pb 5d₅/₂ and Pb 5d₃/₂ electrons (Table 2). As can be seen from Fig. 8, Pb 6p and Pb 6s states are highly hybridized with Cl 3p states at the bottom and top, respectively, of the band A of the XPS valence-band spectrum of CsPbCl₃ determining its covalent constituent of the chemical bonding. The bottom of the conduction band of CsPbCl₃ is composed by unoccupied Pb 6p states, with minor contributions of unoccupied Cl 3p states, too.

![](./images/812518483374899201_13.jpg)

Fig. 10. Calculated absorption coefficient $\alpha(\omega)$ of CsPbCl₃ (here and further, the mBJ + U + SO technique was used).

![](./images/812518483374899201_14.jpg)

Fig. 11. Calculated (a) real $\varepsilon_1(\omega)$ and (b) imaginary $\varepsilon_2(\omega)$ parts of complex dielectric function of CsPbCl₃.

Concerning the prediction of the present theoretical calculations that the main input of Cl 3p states in CsPbCl₃ should occur in the central portion of the band A of the XPS spectrum, it is confirmed by possibilities of the XES technique. Fig. 9 presents the result of adjusting the XPS valence-band spectrum and the XES Cl Kβ₁ band as measured for the CsPbCl₃ crystal (we follow here the common technique of adjusting XPS and XES spectra described in detail elsewhere [20,41]). It is apparent that the main maximum of XES Cl Kβ₁ band is positioned in the central portion of the band A of the XPS spectrum, and some contributions of Cl 3p states are detected at its bottom and top, being in fair agreement with the predictions of the present mBJ + U + SO calculations reported above. These DFT calculations predict also some contributions of Pb 6p and Pb 6s states at the bottom and top, respectively, of the band A of the XPS valence-band spectrum of CsPbCl₃. However, the present experimental ability does not allow us to verify these theoretical predictions for the CsPbCl₃ crystal.

![](./images/812518483374899201_15.jpg)

Fig. 12. Calculated refractive index $n(\omega)$ of $CsPbCl_3$.

![](./images/812518483374899201_16.jpg)

Fig. 13. Calculated extinction coefficient $k(\omega)$ of $CsPbCl_3$.

![](./images/812518483374899201_17.jpg)

Fig. 14. Calculated electron energy-loss spectrum $L(\omega)$ of $CsPbCl_3$.

![](./images/812518483374899201_18.jpg)

Fig. 15. Calculated optical reflectivity $R(\omega)$ of $CsPbCl_3$.

### 4.3. Main optical constants

It is well-known that calculated optical properties of semiconductors/insulators are very sensitive to the band gap value [48]. Therefore, in many cases, when calculating the optical constants of semiconductors/insulators, their theoretical $E_g$ values are adjusted to the experimentally measured ones using the scissors corrected technique [48]. However, experimental determination of the band gap in $CsPbCl_3$ is a matter of controversy because photoluminescence measurements reveal a series of free exciton peaks in the near optical edge region for this compound. In particular, Sebastian et al. [49] reported that $E_g = 2.85$ eV is characteristic for $CsPbCl_3$, while somewhat bigger band gap value (2.97 eV) was measured for this ternary chloride by Zhang et al. [11]. Therefore, we present here data of calculations of the optical properties of the $CsPbCl_3$ crystal employing mBJ + U + SO technique using the theoretically derived band gap (2.431 eV, Table 3) and scissors adjusted by 0.539 eV to correct this value to its biggest experimentally derived value reported in Ref. [11]. Some parameters for the calculated optical constants employing different approaches are listed in Table 4.

As can be seen from Fig. 10, the calculated absorption spectrum $\alpha(\omega)$ of $CsPbCl_3$ reveals strong absorption in a rather wide range of photon energies. In particular, the maximum of the absorption spectrum of $CsPbCl_3$ is positioned near 17 eV, corresponding to far ultraviolet (FUV), while values above $10^4$ cm$^{-1}$ in $CsPbCl_3$ are detected in the energy range

from about 4 eV till 36 eV that covers the wide region from near ultraviolet till FUV. This fact indicates that the ternary chloride under study is a potential semiconductor for the use in optoelectronics.

Real component $\varepsilon_{1}(\omega)$ of complex dielectric function of $CsPbCl_{3}$ is presented in Fig. 11a, while Fig. 11b presents data of calculations of its imaginary component $\varepsilon_{2}(\omega)$. Static dielectric electronic constants (values of the $\varepsilon_{1}(\omega)$ function at $\omega=0$) are determined to be as following: $\varepsilon_{1}^{xx}(0)=5.552$, $\varepsilon_{1}^{yy}(0)=5.530$, and $\varepsilon_{1}^{zz}(0)=5.688$. The application of scissors correction procedure brings somewhat smaller values of the corresponding static dielectric electronic constants, as it is evident from Table 4. The $\varepsilon_{1}(\omega)$ function of $CsPbCl_{3}$ is characterized by the formation of several maxima (features), namely A (~4 eV), B (7.2 eV), C (~10 eV), D (~12 eV), and E (14.7 eV). Beginning from the feature E, the real component $\varepsilon_{1}(\omega)$ of complex dielectric function decreases to its minimum values at energies around 17 eV and, further, with increasing photon energies, it increases almost monotonously. The imaginary component $\varepsilon_{2}(\omega)$ of dielectric function reveals a fast increase beginning from about 2.5 eV and presents the formation of the pronounced peculiarity A (near 6 eV). In addition to this peculiarity, the $\varepsilon_{2}(\omega)$ function, with increasing energies, features peculiarities B (7.3 eV), C (~10 eV), and D (~12.5 eV), and, finally, it reaches its maximum E positioned near 15 eV followed by a rather fast decrease with increasing photon energies.

The refractive index $n(\omega)$ of $CsPbCl_{3}$ is presented in Fig. 12. Static values of the refractive index of $CsPbCl_{3}$ are found to be following: $n^{xx}(0)=2.350$, $n^{yy}(0)=2.352$, and $n^{zz}(0)=2.385$. Like in the case of the static values of the real component $\varepsilon_{1}(\omega)$ of complex dielectric function, the application of the scissors correction technique is accompanied by decreasing the static magnitudes of the refractive index of $CsPbCl_{3}$ (Table 4). Some similarities of the shapes of the real component $\varepsilon_{1}(\omega)$ of complex dielectric function and the refractive index as well as close energy positions of their fine-structure peculiarities A–E are observed (cf. Figs. 11a and 12).

The extinction coefficient $k(\omega)$ of $CsPbCl_{3}$, revealing its shape to be similar somewhat to that of the imaginary component $\varepsilon_{2}(\omega)$ of dielectric function, is presented in Fig. 13, while the energy-loss spectrum $L(\omega)$ is plotted in Fig. 14. The $L(\omega)$ function reveals a sharp peak located at about 27.5 eV. This value corresponds to plasma frequency in $CsPbCl_{3}$. The reflectivity coefficient $R(\omega)$ of $CsPbCl_{3}$ is presented in Fig. 15. From this figure, one can see that the $CsPbCl_{3}$ compound reveals rather good reflectivity with enhancing photon energy till about 27 eV. Above this energy value, the reflectivity of $CsPbCl_{3}$ diminishes fast. The static values of the reflectivity coefficient of $CsPbCl_{3}$ are following: $R^{xx}(0)=16.240\%$, $R^{yy}(0)=16.264\%$, and $R^{zz}(0)=16.740\%$. The static values of the reflectivity coefficient slightly decrease when calculating with the scissors correction technique. It is worth pointing out that the application of the GGA and GGA + U techniques brings the smaller static values of the real component $\varepsilon_{1}(\omega)$ of complex dielectric function, the refractive index $n(\omega)$ and the reflectivity coefficient $R(\omega)$ of $CsPbCl_{3}$ (Table 4). The smallest static values of the above optical constants are detected when the DFT calculations are made within mBJ approach. In general, the present results of calculations of the main optical constants reported in this section indicate fair good prospective of the application of $CsPbCl_{3}$ crystals in optoelectronic devices.

## 5. Conclusions

We present a complex study of the electronic structure and optical properties of cesium lead chloride, $CsPbCl_{3}$, based on the theoretical and experimental data. We have used various approaches for XC potential in our DFT calculations and revealed that the best agreement is derived in the case of the use of mBJ + U + SO approach. The shape and the energy positions of fine-structure peculiarities of the total DOS curve as calculated within the mBJ + U + SO technique were found to be in excellent agreement with the peculiarities of the XPS valence-band spectrum studied for as-grown surface of the $CsPbCl_{3}$ crystal. The present experimental XPS measurements allow for concluding that the $CsPbCl_{3}$ crystal is rather stable with respect to irradiation by middle-energy $Ar^{+}$ ions. The crystal possesses low hygroscopicity that may be of importance in the case of its handling in practical use in optoelectronic devices operating at ambient conditions. The XPS measurements indicate that the charge state of Cs in the $CsPbCl_{3}$ crystal is near to +1, while the charge state of Pb is substantially smaller than +2, as they are expected to occur from the atomic charge balance. This fact is reasonably to explain by the essential covalent constituent of Pb–Cl bonds in the crystal under consideration. This experimental prediction is supported by data of the present band-structure calculations. The calculations indicate that the $CsPbCl_{3}$ compound is a direct-gap semiconductor because the valence band maximum and the conduction band minimum are positioned at $\Gamma$ point (center of the Brillouin zone). The principal contributors to the main portion of the XPS valence-band spectrum of $CsPbCl_{3}$ are Cl 3p states, Pb 6s states contribute to the lower part of the spectrum, while Pb 6p states bring main input to its top. Cs 5p states contribute near the valence band bottom. The conduction band bottom is composed by unoccupied Pb 6p states, with minor contributions of unoccupied Cl 3p states, too. Concerning predictions of the present theoretical calculations regarding the energy position and the shape of partial Cl 3p DOS curve, they are supported experimentally by adjusting the XPS valence-band spectrum and the X-ray emission $Cl K\beta_{1}$ band measured for the $CsPbCl_{3}$ crystal. The calculated maximum of the absorption coefficient of $CsPbCl_{3}$ is positioned near 17 eV, while values above $10^{4}\ cm^{-1}$ are detected in the energy range from about 4 eV till 36 eV that covers wide ultraviolet region. In general, the present results of calculation of the main optical constants reveal good prospective of the application of the $CsPbCl_{3}$ crystal in optoelectronic devices.

### CRediT authorship contribution statement

Tuan V. Vu: Methodology, Investigation, Funding acquisition. A.A. Lavrentyev: Data curation, Conceptualization, Formal analysis. B.V. Gabrelian: Data curation, Visualization. Khang D. Pham: Investigation, Validation. O.V. Parasuyuk: Methodology, Visualization. N.M. Denysyuk: Investigation, Visualization. O.Y. Khyzhun: Writing - original draft, Writing - review & editing, Supervision.

### Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Acknowledgement

This research is funded by Vietnam National Foundation for Science and Technology Development (NAFOSTED) under grant No. 103.01-2018.334.

### References

[1] C.K. Moller, Nature 182 (1958) 1436.
[2] G. Murtaza, I. Ahmad, Physica B 406 (2011) 3222–3229.
[3] I. Dursum, Y. Zheng, T. Guo, M. De Bastiani, B. Turedi, L. Sinatra, M. Haque, B. Sun, A. Zhumekenov, M. Saidaminov, F.P.G. de Arquer, E. Sargent, T. Wu, Y. Gartstein, O. Bakr, O. Mohammed, A. Malko, ACS Energy Letters 3 (2018) 1492–1498.
[4] P. Ramasamy, D.-H. Lim, B. Kim, S.-H. Lee, M.-S. Lee, J.-S. Lee, Chem. Commun. 52 (2016) 2067–2070.
[5] W. Tress, N. Marinova, T. Moehe, S.M. Zakeeruddin, M.K. Nazeeruddin, M. Gratzel, Energy Environ. Sci. 8 (2015) 995–1004.
[6] R. Ahumada-Lazo, J.A. Alanis, P. Parkinson, D.J. Binks, S.J.O. Hardman, J.T. Griffiths, F.W.R. Rivarova, C.J. Humphrey, C. Ducati, N.J.L.K. Davis, J. Phys. Chem. C 123 (2019) 2651–2657.
[7] S. Shirotsu, S. Sawada, Phys. Lett. A 28 (1969) 762–763.
[8] Y. Fujii, S. Hoshino, Y. Yamada, G. Shirane, Phys. Rev. B 9 (1974) 4549–4559.

[9] S. Plesko, R. Kind, J. Roos, J. Phys. Soc. Jpn. 45 (1978) 553-557.

[10] C. Carabatos-Nedelec, M. Oussaïd, K. Nitsch, J. Raman Spectrosc. 34 (2003), 388-293.

[11] Long Zhang, Lingrui Wang, Kai Wang, Bo Zou, J. Phys. Chem. C 122 (2018)15220-15225.

[12] J. Zhang, Q. Wang, X. Zhang, J. Jiang, Z. Gao, Z. Jin, S. Liu, RSC Adv. 7 (2017)36722-36727.

[13] T.J. Milstein, D.M. Kroupa, D.R. Gamelin, Nano Lett. 18 (2018) 3792-3799.

[14] Ghada H. Ahmed, Jehad K. El-Demellawi, Jun Yin, Jun Pan, D.B. Velusamy, Mohamed, Nejib Hedhili, Erkki Alarousu, Osman M. Bakr, Husam N. Alshareef, Omar F. Mohammed, ACS Energy Letters 3 (2018) 2301-2307.

[15] C.C. Lin, K.Y. Xu, D. Wang, A. Majerink, Sci. Rep. 7 (2017) 45906.

[16] H. Shao, X. Bai, H. Cui, G. Pan, P. Jing, S. Qu, J. Zhu, Y. Zhai, B. Dong, H. Song, Nanoscale 10 (2018) 1023-1029.

[17] Y. Zhai, X. Bai, G. Pan, J. Zhu, H. Shao, B. Dong, L. Xu, X. Song, Nanoscale 11(2019) 2484-2491.

[18] K. Wang, F. You, H. Peng, S. Huang, J. Nanosci. Nanotechnol. 18 (2018)7561-7565.

[19] Qiushui Chen, Jing Wu, Xiangyu Ou, Bolong Huang, Jawaher Almutlaq, Ayan A. Zhumekenov, Xinwei Guan, Sanyang Han, Liangliang Liang, Zhigao Yi, Juan Li, Xiaoji Xie, Yu Wang, Ying Li, Dianyuan Fan, Daniel BL. Teh, H All Angelo, Omar F. Mohammed, Osman M. Bakr, Tom Wu, Marco Bettinelli, Huanghao Yang, Wei Huang, Xiaogang Liu, Nature 561 (2018) 88-93.

[20] A.H. Reshak, O.Y. Khyzhun, I.V. Kityk, A.O. Fedorchuk, H. Kamarudin, S. Auluck, O.V. Parasyuk, Sci. Adv. Mater. 5 (2013) 316-327.

[21] S.F. Solodovnikov, V.V. Atuchin, Z.A. Solodovnikova, O.Y. Khyzhun, M. I. Danylenko, D.P. Pishchur, P.E. Plyusnin, A.M. Pugachev, T.A. Gavrilova, A. P. Yelisseyev, A.H. Reshak, Z.A. Alahmed, N.F. Habubi, Inorg. Chem. 56 (2017)3276-3286.

[22] J.P. Perdew, S. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865-3868.

[23] N. Pandey, A. Kumar, S. Chakrabarti, RSC Adv. 9 (2019) 29556-29565.

[24] B.M. Ilyas, B.H. Elias, Physica B 510 (2017) 60-73.

[25] D.M. Ceperley, B.J. Alder, Phys. Rev. Lett. 45 (1980) 566-569.

[26] M. Ahmad, G. Rehman, L. Ali, M. Shafiq, R. Iqbal, R. Ahmad, T. Khan, S. Jalali- Asadabadi, M. Maqbool, J. Alloys Compd. 705 (2017) 828-839.

[27] F. Tran, P. Blaha, Phys. Rev. Lett. 102 (2009) 226401.

[28] V.V. Atuchin, E.N. Galashov, O.Y. Khyzhun, V.L. Bekenev, L.D. Pokrovsky, Y. A. Borovlev, V.N. Zhdankov, J. Solid State Chem. 236 (2016) 24-31.

[29] O.Y. Khyzhun, P.M. Fochuk, I.V. Kityk, M. Piasecki, S.I. Levkovets, A.O. Fedorchuk, O.V. Parasyuk, Mater. Chem. Phys. 172 (2016) 165-172.

[30] A.A. Lavrentyev, B.V. Gabrelian, V.T. Vu, O.V. Parasyuk, A.O. Fedorchuk, O. Y. Khyzhun, Opt. Mater. 60 (2016) 169-180.

[31] V.L. Bekenev, V.V. Bozhko, O.V. Parasyuk, G.E. Davydyuk, L.V. Bulatetska, A. O. Fedorchuk, I.V. Kityk, O.Y. Khyzhun, J. Electron. Spectrosc. Relat. Phenom. 185(2012) 559-566.

[32] P. Blaha, K. Schwarz, G.K.H. Madsen, D. Kvasnicka, J. Luitz, WIEN2k, an Augmented Plane Wave b Local Orbitals Program for Calculating Crystal Properties, Karlheinz Schwarz, Technical Universitat Wien, Austria, 2001, ISBN 3-9501031-1-2.

[33] P. Novak, F. Boucher, P. Gressier, P. Blaha, K. Schwarz, Phys. Rev. B 63 (2001)235114.

[34] P. Novak, Calculation of spin-orbit coupling. http://www.wien2k.a/reg_user/text books/novak_lecture_on_spinorbit.ps, 1997.

[35] P.E. Blöchl, O. Jepsen, O.K. Andersen, Phys. Rev. B 49 (1994) 16223-16233.

[36] T.V. Vu, A.A. Lavrentyev, B.V. Gabrelian, H.D. Tong, H.L. Luong, O.V. Parasyuk, Y. M. Kogut, O.Y. Khyzhun, Opt. Mater. 86 (2018) 191-197.

[37] C. Ambrosch-Draxl, J.O. Sofo, Comput. Phys. Commun. 175 (2006) 1-14.

[38] A.A. Lavrentyev, B.V. Gabrelian, V.T. Vu, P.N. Shkumat, G.L. Myronchuk, M. Khvyshchun, A.O. Fedorchuk, O.V. Parasyuk, O.Y. Khyzhun, Opt. Mater. 42(2015) 351-360.

[39] O.Y. Khyzhun, V.L. Bekenev, N.M. Denysyuk, L.I. Isaenko, A.P. Yelisseyev, A. A. Goloshumova, A.Y. Tarasova, J. Electron. Mater. 48 (2019) 3059-3068.

[40] A.A. Lavrentyev, B.V. Gabrelian, V.T. Vu, P.N. Shkumat, O.V. Parasyuk, A. O. Fedorchuk, O.Y. Khyzhun, J. Phys. Chem. Solid. 85 (2015) 254-263.

[41] V.L. Bekenev, O.Y. Khyzhun, A.K. Sinelnichenko, V.V. Atuchin, O.V. Parasyuk, O. M. Yurchenko, Y. Bezsmolnyy, A.V. Kityk, J. Szkutnik, S. Catus, J. Phys. Chem. Solid. 72 (2011) 705-713.

[42] O.Y. Khyzhun, V.L. Bekenev, N.M. Denysyuk, O.V. Parasyuk, A.O. Fedorchuk, J. Alloys Compd. 582 (2014) 802-809.

[43] Fatih Ersan, Seymur Cahangirov, Gökhan Gökoğlu, Angel Rubio, Ethem Aktürk, Phys. Rev. B 94 (2016) 155415.

[44] Bakhtatou Ali, Fatih Ersan, Phys. Chem. Chem. Phys. 21 (2019) 3868-3876.

[45] Li Han, Ying Qin, Bohan Shan, Yuxia Shen, Fatih Ersan, Emmanuel Soignard, Can Ataca, Sefaat Tin Tongay, Adv. Mater. 32 (2020) 1907364.

[46] A.A. Lavrentyev, B.V. Gabrelian, V.T. Vu, N.M. Denysyuk, P.N. Shkumat, A. Y. Tarasova, L.I. Isaenko, O.Y. Khyzhun, J. Phys. Chem. Solid. 91 (2016) 25-33.

[47] T.V. Vu, A.A. Lavrentyev, B.V. Gabrelian, D.D. Vo, H.D. Tong, N.M. Denysyuk, L. I. Isaenko, A.Y. Tarasova, O.Y. Khyzhun, RSC Adv. 10 (2020) 11156-11164.

[48] T.V. Vu, A.A. Lavrentyev, B.V. Gabrelian, D.D. Vo, K.D. Pham, N.M. Denysyuk, L. I. Isaenko, A.Y. Tarasova, O.Y. Khyzhun, Opt. Mater. 102 (2020) 109793.

[49] M. Sebastian, J.A. Peters, C.C. Stoumpos, J. Im, S.S. Kostina, Z. Liu, M. G. Kanatzidis, A.J. Freeman, B.W. Wessels, Phys. Rev. B 92 (2015) 235210.