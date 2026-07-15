# The crystal structure of visible light absorbing piezoelectric semiconductor $SrNb_2V_2O_{11}$ revisited: high-resolution X-ray diffraction, vibrational spectroscopy and computational study†

Ievgen V. Odynets, $^{a}$ Sergiy Khainakov, $^{b}$ Santiago Garcia-Granda, $^{b}$ Roman Gumeniuk, $^{cd}$ Matthias Zschornak, $^{c}$ Natalia Soloviova, $^{a}$ Nikolay S. Slobodyanik, $^{a}$ Patricia Horcajada $^{e}$ and Artem A. Babaryk $^{*abe}$

Ferroelectric materials have a long-term track record of applications in electronics due to their spontaneous electric polarization. This property can be coupled with photoabsorption properties, resulting in a bulk photoelectric effect, the new on-the-edge domain for ferroelectric use. In this sense, considering the low bandgap of binary strontium-niobium ortho-vanadate $SrNb_2V_2O_{11}$, which has recently been reported as ferroelectric, we propose here a deep experimental and computational understanding of its structural and physical properties, considered relevant for further applications. Microcrystalline $SrNb_2V_2O_{11}$ was prepared by a conventional solid state route, proposing a synthetic pathway deduced from thermoanalytical observations and high-temperature powder X-ray diffraction. The crystal structure (space group $Cc$, $a = 18.15415(2)$ Å, $b = 5.52811(6)$ Å, $c = 9.52728(1)$ Å, $\beta = 99.8033(8)^\circ$, $Z = 2$), successfully solved using high resolution powder X-ray diffraction, reveals the presence of distorted perovskite-like $[Nb_4V_2O_{12}]$ units when preparing $[Nb_2V_2O_{11}]$ sheets. By application of symmetry adapted mode analysis, the non-centrosymmetry originates from Sr atom displacements and $[Nb_4V_2O_{12}]$ unit "breathing" deformations, which can be explained in terms of the group-subgroup relationship. By ground state analysis of the polytypes across possible C-centered monoclinic cells, only the present experimentally based structural model (space group $Cc$) can be adopted, substituting the so far reported crystallographic data. The semiconducting nature of the phase, with a direct bandgap of 2.3 eV, was determined by optical absorption measurements and confirmed computationally. By coupling Raman spectroscopy and density functional perturbation theory, the dielectric properties $(\varepsilon_{iso} = 55)$ were accurately calculated and the observed optical phonons were fully interpreted. Finally, using the Berry phase formalism, we predicted a value of spontaneous polarization of $16.6\ \mu C\ cm^{-2}$ in the absence of confident existing experimental data.

## Introduction
Ferroelectric materials are solids that exhibit spontaneous electric polarization, and have been exploited on an industrial scale in memory storage media, field effect transistors and ferroelectric random-access memories, among others. $^{1-4}$ Recently, owing to the re-opened use of Fridkin theory of light-to-electricity energy conversion and Berry's understanding of polarization in ferroelectrics, new materials for solar energy conversion, *e.g.*, "photoferroics" (in analogy to multi-ferroics, materials coupling electricity and magnetism with potential use in spintronic technologies), have been proposed. "Classical" materials, predominantly oxide or halide perovskites, have been certified for edge applications, utilizing their capability to interact with both electricity and light. $^{5,6}$ It has been recently shown that niobates, primarily of the perovskite family crystal type, are present amongst the polar oxides exhibiting a bulk photovoltaic effect. For instance, Rappe and co-authors, using accurate theoretical computations, have shown that a substantial narrowing of the band gap in $ANbO_3$-based (A - Li, K) solid solutions can be achieved through doping. $^{7}$ *Bai et al.* have experimentally attained a 1.6 eV band gap for $0.98(K_{1/2}Na_{1/2})NbO_3-0.02$ Ba$(Ni_{1/2}Nb_{1/2})O_{3-\delta}$, retaining as large a piezoelectric coefficient as that for $K_{1/2}Na_{1/2}NbO_3$. $^{8}$ Also, a similar approach has been

---
$^{a}$ Faculty of Chemistry, Taras Shevchenko National University of Kyiv, Volodymyrska 64/13, 01601 Kyiv, Ukraine  
$^{b}$ Department of Physical and Analytical Chemistry, Faculty of Chemistry, University of Oviedo, C/Julian Claveria 8, 33006 Oviedo, Spain  
$^{c}$ Institut für Experimentelle Physik, TU Bergakademie Freiberg, Leipziger Straße 23, 09596 Freiberg, Germany  
$^{d}$ Max-Planck-Institut für Chemische Physik fester Stoffe, Nöthnitzer Str. 40, 01187 Dresden, Germany  
$^{e}$ Advanced Porous Materials Unit, IMDEA Energy, Avda. Ramón de la Sagra, 3, 28935 Móstoles, Madrid, Spain. E-mail: artem.babaryk@imdea.org  
† Electronic supplementary information (ESI) available. See DOI: 10.1039/c9tc00410f

extended to Aurivillius phase type $SrBi_2Nb_2O_9$ by substituting 9 at% of bismuth(III) with nickel, which leads to a 2.25 eV optical band gap at a remnant polarization of $2.5\ \mu\text{C cm}^{-2}.^9$

It is well-known that vanadates are a rich source of non-centrosymmetric structures, often due to the large dipole moment of the vanadate anion, and some of them are also ferroelectrics. So far, only a few examples of binary and ternary vanadates of niobium and tantalum have been reported. Compounds emerging from pseudo-ternary Nb-V-O have demonstrated a broad spectrum of interesting properties. For instance, $NbVO_5$ is known as a negative thermal expansion material. $^{10}$ $VNb_9O_{25-\delta}$ solid solutions are found to be n-type semiconductors, $^{11}$ while one particular representative, $V_{2.38}Nb_{10.7}O_{32.7}$, exhibits efficacy in the catalysis of oxidative dehydrogenation of propane and propene. $^{12}$ The addition of alkali-earth metals to the system alters the essence of phase formation, allowing fixation of perovskite-like phases. Thus, Cranswick *et al.* observed transformation of ordered oxygen vacancy octahedral B-sites into tetrahedral ones when occupied by vanadium for $Ca_3Nb_{2-x}V_xO_8$ substituted at $x=0.025.^{13}$ Also, a six-layer perovskite-related structure, $Ba_6Na_2Nb_2V_2O_{17}$, has demonstrated a moderate relative permittivity of $\varepsilon_r\sim20$-$23.^{14}$ Strontium niobates are attractive objects for study and application as photocatalysts and photovoltaics in the ultraviolet part of the spectrum with band gaps of 3.7-4.1 eV. $^{15,16}$ Generally, ternary stoichiometric phases have been found for the binary $SrNb_2O_6$-$SrV_2O_6$ phase diagram. $^{17}$ Trunov *et al.* have reported a series of isomorphous structures, $M^{II}_2M^V_2O_{11}$ (where $M^{II}=Sr$, Ba, Pb; $M^V=$ Nb, Ta), of common space group $R\overline{3}m.^{18}$ Recently, Paidi *et al.* published results of dielectric and ferroelectric measurements describing $SrNb_2V_2O_{11}$ as a polar material that crystallizes in the $Cm$ space group. $^{19}$

Below, we will show through thorough examination aided by a set of accurate structural and computational studies, that the title material is indeed piezoelectric, but it is not polar. Also, *de novo* corrected space group symmetry from high-resolution/high-intensity synchrotron X-ray powder diffraction validated with the present spectroscopic and computational investigations supports the proposed model and reference dielectric data.

## Experimental
### Preparation of $SrNb_2V_2O_{11}$
A conventional solid-state reaction technique was used to obtain $SrNb_2V_2O_{11}$ in the microcrystalline state. Initial components $SrCO_3$, $Nb_2O_5$ and $NH_4VO_3$ were taken in a molar ratio of $1:1:2$ and wet-milled manually using 2-methyl-propanol as a liquid active medium for 30 min. in an agate mortar. The wet mixture was loaded into a glass dish and dried at $80\ ^{\circ}\text{C}$ overnight. The starting mixture was pressed into pellets ($P=105\ \text{N m}^{-2}$, $\emptyset=20$ mm, $d=2$ mm) and sequentially heated at $600\ ^{\circ}\text{C}$ for 6 hours and then at $700\ ^{\circ}\text{C}$ for 12 hours. At least three re-grindings were required according to an established synthetic protocol.

### Scanning electron microscopy/energy-dispersive X-ray spectroscopy
Scanning electron microscopy (SEM) images were recorded at 20 kV accelerating voltage with a JEOL-6610LV scanning electron microscope equipped with an Oxford X-Max microanalysis system (EDX), which was used to confirm the composition. Gold sputtering of the samples was used prior to the measurements.

### Powder X-ray diffraction studies
The powder X-ray diffraction (PXRD) pattern of the final product was collected at room temperature using a Panalytical X'Pert Pro diffractometer, equipped with a PIXcel one-dimensional hybrid pixel technology position-sensitive device detector and operated with Ni-filtered $CuK_{\alpha}$ radiation ($\lambda=1.54178\ \mathring{\text{A}}$). High-temperature X-ray powder diffraction (HT-PXRD) data were collected using the Anton Paar HTK 1200N chamber in an open air atmosphere by loading 500 mg of the sample in a circular alumina boat and heating it gradually from 25 to $830\ ^{\circ}\text{C}$ at a rate of $10\ ^{\circ}\text{C}\ \text{min}^{-1}$. The reaction mixture was incubated for 0.5 h. upon reaching the selected temperature and 7 consecutive acquisition scans were performed in order to yield statistically meaningful diffraction intensities.

High resolution synchrotron X-ray powder diffraction (SR-PXRD) data were collected using beamline 11-BM at the Advanced Photon Source (APS), Argonne National Laboratory (Lemont, IL, USA) using an average wavelength of $0.41385\ \mathring{\text{A}}$. Discrete detectors covering an angular range from $-6$ to $16^{\circ}\ 2\theta$ were scanned over a $34^{\circ}\ 2\theta$ range, with data points collected every $0.001^{\circ}$ with a scan speed of $0.01^{\circ}\ \text{s}^{-1}$. An amount of 40 mg of the target compound was diluted with 44.4% of X-ray diffractionally checked amorphous silica powder and sealed in a standard 0.4 mm Kapton™ capillary with plasticine.

### Thermogravimetric analysis (TGA)
Investigations of the thermal behavior of the $SrNb_2V_2O_{11}$ reaction batch were performed using a Shimadzu DTG-60H simultaneous thermogravimetry/differential thermal analyzer. The sample and reference ($\alpha\text{-Al}_2\text{O}_3$) were heated up to $1000\ ^{\circ}\text{C}$ in Pt/Rh crucibles under an air atmosphere (flow $100\ \text{ml min}^{-1}$) at a rate of $10\ ^{\circ}\text{C}\ \text{min}^{-1}$.

### Vibrational spectroscopy
Raman scattering signals were collected with a JASCO NRS-5100 instrument, operating at a $100\times$ long working length objective. The excitation line of 532 nm wavelength was applied at a power of 2.5 mW. The Raman spectral resolution was $4\ \text{cm}^{-1}$. Three accumulations were performed for 10 seconds along with 100 subsequent scans, using a CCD detector.

Fourier transformed infrared (FTIR) spectra were typically recorded on powdered samples (*ca.* 2 mg of each probe mixed with a 20-fold excess of IR spectroscopy grade KBr; Merck KGaA, Germany and pressed under 5 kbar pressure into transparent tablets). 40 scans were sequentially measured and averaged with a PerkinElmer 1000 FTIR spectrometer, operating at a spectral resolution of $4\ \text{cm}^{-1}$ at room temperature (see Fig. S1, ESI†).

### Optical spectroscopy
UV-vis diffuse reflectance spectra of the polycrystalline powder samples of the reported materials were obtained using a PerkinElmer Lambda 35 UV/vis scanning spectrophotometer equipped with an integrating sphere in the range of 200-900 nm.

The Kubelka-Munk function, $F(R_\infty) = (R - R_\infty)^2/2R = k/s$, was applied to the data for transformation to the relative absorbance spectrum.

## Computational details
The electronic structures of $SrNb_2V_2O_{11}$ were calculated using density functional theory (DFT) within the plane-wave CASTEP code. $^{20}$ The Perdew-Burke-Ernzerhof (PBESol) functional was used to treat the effects of exchange correlation at the generalized gradient approximation (GGA) level of theory. $^{21}$ Valence-core interaction was described with optimized norm-conserving Vanderbilt pseudopotentials with $[He]2s^22p^4$ for O, $[Ne]3s^23p^63d^34s^2$ for V, $[Ar]3d^{10}4s^24p^65s^2$ for Sr and $[Ar]4s^24p^64d^45s^1$ for Nb core-valence configurations. $^{22,23}$ The experimentally determined (sub-group, $Cc$) and generated (super-group, $Cm$, $C2/c$) structures were transformed to equivalent representation primitive-centered unit cells and fully relaxed. Relaxations of the ionic positions were conducted using $5 \times 5 \times 3$ $k$-point meshes and an energy cutoff of 520 eV. Relaxations were deemed to have converged when the forces on all the ions were less than $0.01$ eV $\mathring{A}^{-1}$. Phonon frequencies were obtained by diagonalization of the dynamical matrices, computed using linear response-density-functional perturbation theory (LR-DFPT, hereafter DFPT for simplicity), using the Gonze formalism. $^{24,25}$ All optical phonons were calculated at the Q(0,0,0) - point, maintaining essentially the same $k$-point mesh but elevating the electron kinetic energy limit to 1100 eV.

## Results
### General synthetic aspects
Thermogravimetric (TG) analysis of the initial blend was used to follow the temperature transformations, corresponding to the mixture's reactivity. A typical DTG/DTA-trace is depicted in Fig. 1 and a short summary of the observed thermal effects is accumulated in Table 1.

In the range of $145-420$ °C, step-wise formation of anhydrous $V_2O_5$ occurs with decomposition of volatile products. Referring to HT-PXRD, the intense $d_{(020)} = 5.89$ $\mathring{A}$ peak of ammonium orthovanadate is visible until 255 °C (Fig. 2). The maximum at 542 °C corresponds to melting of the eutectic mixture of ($\beta\text{-SrV}_2\text{O}_6 + \text{V}_2\text{O}_5$) accompanied by the release of gaseous $\text{CO}_2$. The endo-effect at 658 °C matches the temperature of incongruent melting of $\text{NbVO}_5$. $^{26}$ Furthermore, the excess unreacted $\text{V}_2\text{O}_5$ is fixed with $\text{Nb}_2\text{O}_5$, matching $\alpha\text{-Nb}_9\text{VO}_{25}$, as will be shown below. The TG data agree well with the variable temperature powder X-ray diffraction results, showing slow decay of the diffraction intensities of the parental $\text{Nb}_2\text{O}_5$ up to 650 °C, whereas the monophasic system crystalizes at 660 °C, monitoring the $d_{(202)}/d_{(311)}$ Bragg intensities. The endpoint represents the melting temperature of the final product, normally obtained at lower temperatures as a polycrystalline powder in the form of 5-7 $\mu$m-sized prismatic grains, as estimated from SEM observation (Fig. 1a). In addition, energy dispersive analysis confirms the expected stoichiometry $\text{O/V/Nb/Sr} = 11:2:2:1$.

![](./images/812782549771223042_1.jpg)

Fig. 1 Top left: SEM micrograph of the prepared polycrystalline substance (inset shows a magnified grain) (a). A profile of the TG/DTA examination of a reactive blend (see description in the text for details) (b). A diagram of the Pawley decomposed PXRD ($\lambda$ = 1.5406 $\mathring{A}$) pattern (c). Tauc plot of the processed diffuse reflection spectrum for SNVO (note the color of a bulk powder sample as shown at the inset) (d).

### Structure solution and refinement
The experimental SR-PXRD pattern was unambiguously indexed (SVD $M_{31} = 820.3$) $^{27}$ to a monoclinic system, using fitted positions of the peaks in the region of $2\theta = 2.5-9.5^\circ$. Examination of the systematic absences on $h + k = 2n$ suggested C-type lattice centering. Complete space group assignment was based on further examination of $(h0l)$ and, in particular, $(00l)$ arrays of reflection, for which $h, l = 2n$ and $l = 2n$ absences lead unambiguously to a polar $Cc$ (no. 9) group, showing general consistency with further structure solutions. Whole pattern decomposition was applied to extract the intensity of individual

Table 1 A summary of the observed TG/DTA effects

<table>
<thead>
<tr>
<th>Step</th>
<th>$T_{\text{onset}}$ (°C)</th>
<th>$T_{\text{outset}}$ (°C)</th>
<th>Experimental<br>weight loss (mas.%)</th>
<th>Theoretical<br>weight loss (mas.%)</th>
<th>Process</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>145</td>
<td>203</td>
<td>4.59</td>
<td>8.03</td>
<td>$-2\text{NH}_3$<br>$- \text{H}_2\text{O}$</td>
</tr>
<tr>
<td>2</td>
<td>203</td>
<td>252</td>
<td>2.19</td>
<td rowspan="4">6.79</td>
<td rowspan="4">$- \text{CO}_2$</td>
</tr>
<tr>
<td>3</td>
<td>271</td>
<td>330</td>
<td>1.39</td>
</tr>
<tr>
<td>4</td>
<td>359</td>
<td>418</td>
<td>3.04</td>
</tr>
<tr>
<td>5</td>
<td>495</td>
<td>651</td>
<td>3.81</td>
</tr>
<tr>
<td>6</td>
<td>660</td>
<td>672</td>
<td>—</td>
<td>—</td>
<td>Crystallization</td>
</tr>
<tr>
<td>7</td>
<td>807</td>
<td>830</td>
<td>—</td>
<td>—</td>
<td>Melting</td>
</tr>
</tbody>
</table>

![](./images/812782549771223042_2.jpg)

Fig. 2 Variable temperature PXRD data of the reaction blend.

reflections, according to the Pawley procedure $(R_{p}=6\%, R_{wp}=$ 7.2%). The initial structural model was determined by a charge flipping algorithm $^{28}$ with $R_{I}=30.7\%$ , having correctly placed all found heavy atoms (Sr, Nb, V) and most of the light (O) atoms. Two missing oxygen atoms were revealed from difference Four- ier maps. The final structural model was refined using the Rietveld method $(R_{p}=6.6\%, R_{wp}=7.6\%)$ without any geome trical restraints. A non-fitting low intensity peak of an admix- ture phase with dominant reflection at $d \approx 3.51 \AA$ was attributed to $\alpha-Nb_{9} VO_{25}$ by pattern matching of residuals. By engaging an additional phase into the refinements, its presence was ascertained at about $1.5 wt \%$ . The results of the Rietveld refinements are summarized in Tables 2 and 3 and depicted in Fig. 3.

The validity of the final model was checked using the charge distribution method (CHARDI), $^{29}$ which is the development of the bond-valence sums using the distribution of charge (Q). It is based on the effective coordination number (EcoN) of the cation amongst all the neighboring anions and depends upon

<table><caption>Table 2 Fractional coordinates, isotropic displacement parameters and Q-indices for the refined crystal structure</caption>
<thead>
<tr>
<th>Atom</th>
<th>x/a</th>
<th>y/b</th>
<th>z/c</th>
<th>$U_{iso}[\AA^{2}]$</th>
<th>Q</th>
</tr>
</thead>
<tbody>
<tr>
<td>Nb1</td>
<td>0.42347(37)</td>
<td>0.25051(15)</td>
<td>0.60796(66)</td>
<td>0.6879(54)</td>
<td>4.812</td>
</tr>
<tr>
<td>Nb2</td>
<td>0.31243(37)</td>
<td>0.25033(15)</td>
<td>0.23605(65)</td>
<td>$=U_{iso}(Nb1)$</td>
<td>4.922</td>
</tr>
<tr>
<td>V1</td>
<td>0.02557(38)</td>
<td>0.23534(38)</td>
<td>0.45970(66)</td>
<td>0.551(15)</td>
<td>5.018</td>
</tr>
<tr>
<td>V2</td>
<td>0.71160(38)</td>
<td>0.26242(38)</td>
<td>0.35404(67)</td>
<td>$=U_{iso}(V1)$</td>
<td>5.216</td>
</tr>
<tr>
<td>Sr1</td>
<td>0.11792(37)</td>
<td>0.29700(11)</td>
<td>0.13150(66)</td>
<td>1.318(14)</td>
<td>2.032</td>
</tr>
<tr>
<td>O1</td>
<td>−0.00283</td>
<td>0.04554</td>
<td>0.02040</td>
<td>1.408(27)</td>
<td>−2.010</td>
</tr>
<tr>
<td>O2</td>
<td>0.35442(48)</td>
<td>0.2570(12)</td>
<td>0.42677(91)</td>
<td>$=U_{iso}(O1)$</td>
<td>−2.082</td>
</tr>
<tr>
<td>O3</td>
<td>0.36437(53)</td>
<td>0.0253(11)</td>
<td>0.69120(81)</td>
<td>$=U_{iso}(O1)$</td>
<td>−2.126</td>
</tr>
<tr>
<td>O4</td>
<td>0.11551(49)</td>
<td>0.25691(96)</td>
<td>0.51576(81)</td>
<td>$=U_{iso}(O1)$</td>
<td>−1.900</td>
</tr>
<tr>
<td>O5</td>
<td>0.48693(65)</td>
<td>0.0200(15)</td>
<td>0.0392(11)</td>
<td>$=U_{iso}(O1)$</td>
<td>−1.970</td>
</tr>
<tr>
<td>O6</td>
<td>0.22517(33)</td>
<td>0.03366(88)</td>
<td>0.27542(72)</td>
<td>$=U_{iso}(O1)$</td>
<td>−1.931</td>
</tr>
<tr>
<td>O7</td>
<td>0.38121(52)</td>
<td>0.4663(11)</td>
<td>0.17303(93)</td>
<td>$=U_{iso}(O1)$</td>
<td>−2.096</td>
</tr>
<tr>
<td>O8</td>
<td>0.25330(43)</td>
<td>0.2454(13)</td>
<td>0.02836(91)</td>
<td>$=U_{iso}(O1)$</td>
<td>−1.830</td>
</tr>
<tr>
<td>O9</td>
<td>0.01044(44)</td>
<td>0.2483(13)</td>
<td>0.27445(89)</td>
<td>$=U_{iso}(O1)$</td>
<td>−2.151</td>
</tr>
<tr>
<td>O10</td>
<td>0.24153(60)</td>
<td>0.5273(15)</td>
<td>0.261(1)</td>
<td>$=U_{iso}(O1)$</td>
<td>−1.964</td>
</tr>
<tr>
<td>O11</td>
<td>0.62489(50)</td>
<td>0.23024(99)</td>
<td>0.35765(86)</td>
<td>$=U_{iso}(O1)$</td>
<td>−1.941</td>
</tr>
</tbody>
</table>

<table><caption>Table 3 Principal interatomic distances</caption>
<thead>
<tr>
<th>Bond</th>
<th>Distance (Å)</th>
<th>Bond</th>
<th>Distance (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">$Nb1O_{6}$</td>
<td colspan="2">$V1O_{4}$</td>
</tr>
<tr>
<td>Nb1-O2</td>
<td>1.952(6)</td>
<td>V1-O4</td>
<td>1.629(8)</td>
</tr>
<tr>
<td>Nb1-O3</td>
<td>1.905(7)</td>
<td>V1-O9</td>
<td>1.721(6)</td>
</tr>
<tr>
<td>$Nb1-O5^{b}$</td>
<td>2.065(9)</td>
<td>$V1-O1^{b}$</td>
<td>1.762(2)</td>
</tr>
<tr>
<td>$Nb1-O7^{d}$</td>
<td>1.890(7)</td>
<td>$V1-O5^{j}$</td>
<td>1.748(9)</td>
</tr>
<tr>
<td>$Nb1-O1^{1}$</td>
<td>2.050(2)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$Nb1-O9^{1}$</td>
<td>2.059(6)</td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">$Nb2O_{6}$</td>
<td colspan="2">$V2O_{4}$</td>
</tr>
<tr>
<td>Nb2-O2</td>
<td>1.849(6)</td>
<td>V2-O11</td>
<td>1.593(6)</td>
</tr>
<tr>
<td>Nb2-O6</td>
<td>2.044(6)</td>
<td>$V2-O10^{g}$</td>
<td>1.714(8)</td>
</tr>
<tr>
<td>Nb2-O7</td>
<td>1.900(7)</td>
<td>$V2-O6^{h}$</td>
<td>1.716(6)</td>
</tr>
<tr>
<td>Nb2-O8</td>
<td>2.042(3)</td>
<td>$V2-O8^{1}$</td>
<td>1.753(3)</td>
</tr>
<tr>
<td>Nb2-O10</td>
<td>2.038(9)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$Nb2-O3^{a}$</td>
<td>1.877(7)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Symmetry operations to generate equivalent atoms are: $^{a} x,-y,-1 / 2+z$ ; $^{b} x,-y, 1 / 2+z ;^{d} x, 1-y, 1 / 2+z ;^{g} 1 / 2+x,-1 / 2+y, z ;^{h} 1 / 2+x, 1 / 2+y, z ;$ $^{j}-1 / 2+x, 1 / 2-y, 1 / 2+z ;^{1} 1 / 2+x, 1 / 2-y, 1 / 2+z$ .

![](./images/812782549771223042_3.jpg)

Fig. 3 Rietveld refinement plot of the SR-PXRD pattern $(\lambda=0.41385 \AA)$ .

the geometry of each coordination polyhedron, which is char- acterized through ECoN. The ratio of $Q/q$ was used as a measure of the correctness of the structure (cation ratio) and as the degree of over- or under-bonding (anion ratio).

The asymmetric unit cell holds one formula unit (Table 2). Niobium and vanadium atoms are found in distorted octahedral and tetrahedral oxygen environments (Fig. 4). More precisely, vanadium atoms afford (pseudo)trigonal-pyramidal polygons, following the same trend: the V1-O4 and V2-O11 bond dis- tances are shortened closer to the "V=O", and the rest of the bonds and the bond angles at the pyramid bases vary within narrow limits of 1.72-1.76 $\AA$ and 112.6-113.6 (1.71-1.75 $\AA$ and 110.4-111 in case of V2). Niobium bond lengths are distributed in two groups: Nb-O-Nb linkage is characterized by short $<1.90 \AA$ separations, while the rest of the contacts participate in Nb-O-V bonding with typical values in the range of 1.95-2.00 $\AA$ . $NbO_{6}$ octahedra and $VO_{4}$ tetrahedra are assembled into quasi-two dimensional sheets, at $a/2$ of each other and stacked along the

![](./images/812782549771223042_4.jpg)

Fig. 4 A projection of the $SrNb_2V_2O_{11}$ crystal structure viewed along the $b$-axis (green spheres denote $Sr$ atoms, $NbO_6$ and $VO_4$ polyhedra are depicted in grey and orange colors).

[001] direction. Sr1 occupies a space between the two adjacent sheets, liking them into a framework structure. The nearest sphere of Sr atom enclosure has eight Sr-O contacts spanning over $2.55 < d < 2.90$ Å.

### Distortion mode analysis
For comparison purposes, we used the PSEUDO routine at the Bilbao Crystallographic Server$^{30}$ to find the parental supergroup structure in the $C2/c$ group (no. 15 in IT). Optimized (see DFT calculation section below) strain-unbiased model III was introduced for determining the amplitudes of the distortion modes from the same SR-PXRD experimental dataset as that used for structure solution and refinement. In-depth analysis of the reasons governing the distorted structure, in terms of deviations from idealized geometry, is possible owing to symmetry adapted mode approximation. Thus, the distortion relating a parent structure of the H group with the actual displacively distorted structure of the G group of lower symmetry can be deconvoluted with a set of atomic displacements, which may break some translational symmetry, but keep the metrics of the underlying parent lattice (the secondary eigenmode) and the strain of the parent lattice (the primary eigenmode). In particular, $C2/c$ (ITC #15) can be transformed to the $Cc$ space group (ITC #9) on omission of axial symmetry, so only one distortion mode is needed to describe the structural relationship. The default search criteria were applied to find the displacement mode amplitudes, implying (floating) origin shift for the polar model I structure. Overall, eight $\Gamma_2^-$ and four $\Gamma_1^+$ irreps correspond to the primary and the secondary modes (Table 4), and only the former are the focus of interest hereafter.

By definition, the primary distortion modes do not cause the change of symmetry, but are responsible for a strain and may be weak. The refined amplitude of $\Gamma_1^+$ distortion was found to be only 0.4024 Å, which is in contrast to the magnitude of the $\Gamma_2^-$ mode (1.1929 Å). The interpretation of both is apparent from displacement vector graphs (Fig. 5a). The former appears as superposition of out-of-phase shifts of Sr atoms along the $b$-axis and small rotations of the vanadate group along the local 3-fold axis and is similar for equatorial oxygens at niobium octahedra. The latter distortion mode acts in the $(ac)$ plane, changing the positions of Sr atoms and moving them along the [001] axis synchronously, while polyhedra asynchronously tilt, allowing "breathing" of the perovskite like $[Nb_4V_2O_{12}]$ units (Fig. 5a and b).

<table>
  <thead>
    <tr>
      <th colspan="2">Table 4 Summary of distortion modes</th>
      <th></th>
    </tr>
    <tr>
      <th>Atoms</th>
      <th>Wyckoff position</th>
      <th>Mode irreps</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">$C2/c \rightarrow Cc$ transition</td>
    </tr>
    <tr>
      <td>V1 O6 O3 O5 O1 O4 Nb1</td>
      <td>8f</td>
      <td>$\Gamma_1^+$ (3), $\Gamma_2^-$ (3)</td>
    </tr>
    <tr>
      <td>Sr1</td>
      <td>4e</td>
      <td>$\Gamma_1^+$ (1) $\Gamma_2^-$ (2)</td>
    </tr>
    <tr>
      <td>O2</td>
      <td>4d</td>
      <td>$\Gamma_2^-$ (3)</td>
    </tr>
  </tbody>
</table>

![](./images/812782549771223042_5.jpg)

Fig. 5 Visualization (Vesta program, see ref. 31) of $\Gamma_1^+$ (a, top) and $\Gamma_2^-$ (b, bottom) irreps of symmetry adapted distortion modes, acting on unit cell atoms (viewed normal to the (101) plane). Normalized displacement vectors are drawn in red color.

### Raman spectroscopy analysis
Fig. 6 shows the result of empirical peak deconvolution of the recorded Raman spectrum excited by a green laser. The peaks located over the range of $120$-$425$ $\mathrm{cm^{-1}}$ are similar to those observed for $LiNbO_3$, and correspond to symmetric and asymmetric bending of $NbO_6$ octahedra.$^{32}$ The low intensity doublet at $675$-$705$ $\mathrm{cm^{-1}}$ ought to correspond to different contributions: (i) Nb-O stretching of the shortest bonds have similar distances to those of $LiNbO_3$; and (ii) deformational vibration of $VO_4$ groups.

Two of the most distant and intense peaks (918 and $946$ $\mathrm{cm^{-1}}$) are more typical of orthovanadate groups than niobium oxides. However, one could not exclude their assignment to niobium

![](./images/812782549771223042_6.jpg)

Fig. 6 Representation of the observed (light blue dots) and cumulative deconvolution line (solid red line) of Raman scattering ($\lambda$ = 532.16 nm).

oxides, which also exhibit distinct vibrations in the limits of $800$-$1000\ \text{cm}^{-1}$.$^{33}$

### Density functional theory calculations
Recently, Paidi *et al.* have reported a single crystal diffraction study of $SrNb_2V_2O_{11}$, $^{19}$ proposing the polar $Cm$ space group. This agrees with the ferroelectric properties of the material, but is in contradiction with the current crystallographic model. Experimentally resolved $(hk0)$ series of reflections appear due to twice as large a period and are valid for all $Cc$ space groups. To validate the present structural findings, we calculated the electronic structure of all possible polymorphs of SNVB crystalized in the $Cc$ (model I), $Cm$ (model II) and $C2/c$ (model III) space groups. The later was generated with the aid of the PSEUDO routine of the Bilbao crystallographic server in terms of subgroup-supergroup relationship and represents the hypothetical para-electric state of the material. The calculated key energetic and geometric parameters are listed in Table 5. As can be seen from the normalized total energy per formula unit of each crystal, model I is thermodynamically the most stable polymorph. Moreover, calculations with DFPT on top of the fully relaxed atomic structures yield imaginary vibrational frequencies showing local minima for model II and III (see Tables S1 and S2 for details, ESI†). Finally, the general plot comparing the experimentally observed and calculated diffraction intensities for all three structures obviously supports derived model I, which was the only one retained for further analyses (Fig. 7). Note that we will show later the tight agreement of the optical properties of the established spatial arrangement with available measured data.

<table>
<caption>Table 5 Summary of calculated key parameters of the suggested polytypes</caption>
<thead>
<tr>
<th></th>
<th>Model I</th>
<th>Model II</th>
<th>Model III</th>
</tr>
</thead>
<tbody>
<tr>
<th>Space group</th>
<td>Cc<br>(No. 9 ITC)</td>
<td>Cm<br>(No. 8 ITC)</td>
<td>C2/c<br>(No. 15 ITC)</td>
</tr>
<tr>
<th>$a$, Å</th>
<td>18.0965</td>
<td>9.5259</td>
<td>18.0979</td>
</tr>
<tr>
<th>$b$, Å</th>
<td>5.5370</td>
<td>5.5281</td>
<td>5.5199</td>
</tr>
<tr>
<th>$c$, Å</th>
<td>9.5195</td>
<td>9.5052</td>
<td>9.5972</td>
</tr>
<tr>
<th>$\beta$, deg</th>
<td>99.76</td>
<td>109.78</td>
<td>99.85</td>
</tr>
<tr>
<th>$Z$</th>
<td>4</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<th>Energy p.f.u., meV</th>
<td>0.0</td>
<td>+6.3</td>
<td>+9.6</td>
</tr>
<tr>
<th>$E_g$, eV</th>
<td>2.35 (2.219, 2.01)</td>
<td>2.24</td>
<td>2.29</td>
</tr>
<tr>
<th>Imaginary frequencies</th>
<td>No</td>
<td>Yes (6.86i)</td>
<td>Yes (2.214i)</td>
</tr>
</tbody>
</table>

![](./images/812782549771223042_7.jpg)

Fig. 7 A comparison of the experimental (SR-PXRD, blue line) data with the calculated patterns for DFT models I, II and III within the present work and a reference single crystal study (black, grey, violet and orange lines).

To calculate the local polarization in a unit cell, the following expression was used:$^{34}$

$$
P = \frac{e}{V} \sum_{\text{s}} Z_{\text{s}}^{*} \Delta u_{\text{s}}
$$

where $V$ is the volume of the unit cell, $Z_{\text{s}}^{*}$ is the Born effective charge of ion s and $\Delta u_{\text{s}}$ is the displacement of ion s in this cell (see Table S1, ESI†). The superscript zero refers to the reference structure, which is nonpolar and centrosymmetric.

The calculated electronic density of states for $SrNb_2V_2O_{11}$ is presented in Fig. 8 and 9. The broad valence band in this electronic structure extends from $-7.5$ to $-2$ eV and consists of

![](./images/812782549771223042_8.jpg)

Fig. 8 Calculated electronic density of states of $SrNb_2V_2O_{11}$.

![](./images/812782549771223042_9.jpg)

Fig. 9 Electronic band structure for $SrNb_2V_2O_{11}$. The O 2p bands, corresponding to the VBM and Nb 4d bands forming the CBM (see description in the text), are marked by blue and red dots, respectively.

three separate regions (-7.5 to -7.0 eV, -6.9 to -6.5 eV and -6.4 to -2.0 eV). The two low-lying regions are mostly populated by Nb 4d- and 2p-states of oxygen atoms O2, O3 and O7, which reflect the strongest Nb-O interactions (see Table 3).

Interestingly, there is no contribution of atoms O4 and O11 to the low energy states (from -7.5 to -6.5 eV). This observation is also in agreement with the interatomic distances given in Table 3: there are no Nb-O4 and Nb-O11 contacts. On the other hand, O4 and O11 show the shortest distances with V atoms. Furthermore, the V density of states is mostly located between -5.5 eV and -3 eV, strongly hybridizing with 2p states of the mentioned O-atoms. The valence and conduction bands in the electronic structure of $SrNb_2V_2O_{11}$ are separated by an energy gap of 2.1 eV, confirming the semiconducting nature of the studied compound. This finding is in excellent agreement with the performed optical absorption measurements. The calculated band structure for $SrNb_2V_2O_{11}$ is depicted in Fig. 8. Both the valence band minimum (VBM) (exclusively due to O 2p-bands) and the conduction band maximum (CBM) (exclusively due to Nb 4d-bands) are located at the $\Gamma$-point, which confirms $SrNb_2V_2O_{11}$ as a direct bandgap semiconductor.

## Discussion
The reported compound is a product of the suggested complex interactions, summarized by equations (eqn (1)-(2)):

$$
\begin{align}
\mathrm{SrNb_2O_6 + SrV_2O_6 + 2NbVO_5 = 2SrNb_2V_2O_{11}} & \ (t < 660\ ^\circ\text{C}) \
9\mathrm{SrNb_2O_6 + 9SrV_2O_6 + 2Nb_9VO_5 + 9V_2O_5} & \
= 18\mathrm{SrNb_2V_2O_{11}} & \ (t > 660\ ^\circ\text{C}),
\end{align}
$$

as followed by stepwise analysis of the main TG/DTA observations (see Fig. S3, ESI$\dagger$) and the weak contribution of residual $\mathrm{Nb_9VO_{25}}$ in the final solid. These findings are well supported by the single crystal specimen growth that has been recently described using $\mathrm{SrV_2O_6}$, $\mathrm{SrBr_2}$, $\mathrm{V_2O_5}$ and metallic Nb, eventually leading to an equilibrium polyphasic mixture where $\mathrm{Nb_9VO_{25}}$ was also detected.

According to our HT-XPRD studies, the target compound likely melts peritectically with evolution of liquid $\mathrm{V_2O_5}$ at extreme temperatures and the release of $\mathrm{SrNb_2O_6}$ and $\mathrm{Nb_9VO_{25}}$.

Several structures with general $\mathrm{AB_2C_2X_{11}}$ crystal ANX-formulae: $\mathrm{BaNb_2V_2O_{11}},^{18,19}$ $\mathrm{CaNb_2P_2O_{11}},^{35}$ and $\mathrm{AMo_2Se_2O_{11}},^{36}$ have also been reported to date. For rationalization of the crystal structure, a periodic graph approximation is useful. For the present case, the nodes in the graph correspond to the centers of gravity of polyhedron B = Nb or Mo and C = P, V, or Se nodes as coordination centers of $\mathrm{X=O}$ as ligands. Here, the (3,6)-c double nodal net exhibits a similar topology to $\mathrm{BaNb_2V_2O_{11}}$, indicating that both structures are isotypical. Indeed, $\mathrm{BaNb_2V_2O_{11}}$ crystalizes in the $R\overline{3}m$ group related with the $C2/m$ subgroup. From the other side, analysis of the local symmetry of $\mathrm{NbO_6}$ and $\mathrm{VO_4}$ reveals a distortion from trigonal-pyramidal symmetry, which is common for high symmetry trigonal arrangements. This explains the difficulties in determination of the genuine lattice symmetry$^{19,37}$ and, thus, corrects the symmetry setting.

Plotting of both structures back-transformed in real atom space reveals well-guessed motifs of perovskite type (Fig. 10).

However, the reported structure crystallizes in polar space group $Cc$ (no. 9 in IT), which is not an isomorphic subgroup of the $Pm\overline{3}m$ supergroup, considering an ideal perovskite structure. Thus, a distinct structural type is ascribed for the present complex binary orthovanadate.

As the structure is supposed to be polar, the value of spontaneous polarization is a key parameter for potential applications. Thus, we have used the formalism of DFPT to probe the dielectric properties of the investigated material, thoroughly validated with experimental observations. The highest energy bands are centered at 953 and $960\ \mathrm{cm^{-1}}$ (s, $\mathrm{A'}$) and assigned to asymmetric and symmetric stretching of terminal "vanadyl" bonds, which are usually observed in natural penta- and decavanadates.$^{38}$ The vibrations at $681\ \mathrm{cm^{-1}}$ (m) and $709\ \mathrm{(vs)\ cm^{-1}}$ in the FT-IR spectrum are attributed to $\nu_3$ antisymmetric stretching modes ($\mathrm{A'}$) and $\nu_1$ symmetric stretching modes ($\mathrm{A''}$). $\mathrm{VO_4}$ is found in the region of $780\ \mathrm{cm^{-1}}$ and not $[\mathrm{NbO_6}]$ stretching, as is the case for perovskites.$^{39}$ The deformation of the $[\mathrm{Nb_6V_2O_{12}}]$ cage is accompanied by $\mathrm{Nb-O(-V)}$ transverse vibrations, as observed at 407 and $426\ \mathrm{cm^{-1}}$. Tight agreement of the experimentally observed vibrational modes with the calculated ones on top of the determined and optimized

![](./images/812782549771223042_10.jpg)

Fig. 10 Projection of perovskite-like $[\mathrm{Nb_6V_2O_{12}}]$ units, attributing to $\mathrm{SrNb_2V_2O_{11}}$ (left) and $\mathrm{BaNb_2V_2O_{11}}$ (right) the same topology (atoms constituting internal bonds are emphasized with color: niobium species are filled maroon or shaded light blue, and vanadium species are orange and plum colored bulbs; oxygens are empty spheres).

structural models promises accurate assessment of the dielectric properties of the material. For space group $Cc$ (#9 in ITC), the non-zero components of the dielectric tensor are expressed as:

$$
\varepsilon_{i j}=\left(\begin{array}{ccc}
\varepsilon_{11} & 0 & 0 \\
0 & \varepsilon_{22} & 0 \\
0 & 0 & \varepsilon_{33}
\end{array}\right)
$$

The spatially averaged value $\varepsilon_{\text{iso}}$ is equal to $\varepsilon_{\text{riso}}=(\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{22})/3$. For the present study, $\varepsilon_{\text{riso}}=55$, which is in perfect agreement with the dielectric measurements at a static limit $(\omega=0)$, as already found by Paidi et al. $^{19}$

Based on a combination of the mode crystallographic analysis and DFPT, we tried to calculate the spontaneous polarization $(P_{\text{s}})$, which is the polarization of a ferroelectric material in the absence of any external electrical field. For this, both the experimentally derived and relaxed model I subgroups were analyzed *versus* the model III virtual supergroup structure. Analyzing the contributions, both of the distortion modes $(\Gamma_{1}^{+}, \Gamma_{2}^{-})$ return the value of bulk polarization of $16.6\ \mu\text{C}\ \text{cm}^{-2}$, close to $16.8\pm0.2\ \mu\text{C}\ \text{cm}^{-2}$ from distortion mode analysis. The reported magnitudes of the remnant and spontaneous polarization on the powder specimen equal 0.21 and $0.53\ \mu\text{C}\ \text{cm}^{-2}$. Such discrepancy can be explained by the inaccurate treatment of the reference $P$–$E$ data, very typical for lossy dielectric polarization. $^{40}$ Notwithstanding, the available second-harmonic generation studies suggest that piezoelectric properties are inherent for the as-reported material.

## Conclusions
A rare example of binary orthovanadate $\text{SrNb}_{2}\text{V}_{2}\text{O}_{11}$ has been successfully synthesized as a pure incongruently melting phase at $T<660\ ^{\circ}\text{C}$. Using SR-PXRD, its crystal structure has been unambiguously determined, belonging to the polar space group $Cc$ and correcting all previous recent attempts to establish its spatial organization. The electronic ground state for the title compound, detected over probable $C$-centered polytypes, is consistent with the present experimental structural data. Anionic $[\text{Nb}_{2}\text{V}_{2}\text{O}_{11}]^{2-}$ is unique across an array of $[\text{B}_{2}\text{C}_{2}\text{X}_{11}]^{2-}$ oxygenated isomorphs and has strong similarity to perovskite structures. Following symmetry adapted mode analysis, the structural distortions have been characterized and quantified through the $C2/c$–$Cc$ group-subgroup relationship, invoking the $\Gamma_{2}^{-}$ distortion mode to strongly displace Sr atoms and deform the $[\text{Nb}_{2}\text{V}_{2}\text{O}_{11}]^{2-}$ sublattice in concert. A direct type of bandgap of 2.1 eV has been deduced by electronic structure calculations in the ground state. The interpretation of the optical phonons, measured by Raman spectroscopy, showed separation of the stretching vibrational modes to Nb–O and V–O regions and their overlap in the low energy deformational region of the spectrum. Utilizing the Berry phase formalism, the static limit dielectric constant $(\varepsilon_{\text{r}}=55)$ has been numerically reproduced and a spontaneous polarization value of $P_{\text{s}}=16.6\ \mu\text{C}\ \text{cm}^{-2}$ has been predicted as an alternative to the existing measured value of $0.53\ \mu\text{C}\ \text{cm}^{-2}$.

## Conflicts of interest
There are no conflicts to declare.

## Acknowledgements
Use of the Advanced Photon Source at Argonne National Laboratory was supported by the U. S. Department of Energy, Office of Science, Office of Basic Energy Sciences, under Contract No. DE-AC02-06CH11357. S. K., S. G. and A. B. B. acknowledge the financial support from Spanish Ministerio de Economía y Competitividad (MAT2016-78155-C2-1-R). P. H. and A. A. B. are indebted to the People Programme (Marie Curie Actions) of the European Union's Seventh Framework Programme (FP7/2007-2013) under REA grant agreement no. 291803. This work is partially supported by the ICDD GiA #12-02 "Patterns of inorganic oxides and salts based on oxoanions" and Raphuel (ENE2016-79608-C2-1-R) project.

## References
1 Z. Hu, M. Tian, B. Nysten and A. M. Jonas, *Nat. Mater.*, 2009, **8**, 62.
2 J. F. Scott, *Science*, 2007, **315**, 954.
3 V. Garcia and M. Bibes, *Nature*, 2012, **483**, 279.
4 D. Lee, S. M. Yang, T. H. Kim, B. C. Jeon, Y. S. Kim, J.-G. Yoon, H. N. Lee, S. H. Baek, C. B. Eom and T. W. Noh, *Adv. Mater.*, 2012, **24**, 402.
5 T. Choi, S. Lee, Y. Choi, V. Kiryukhin and S.-W. Cheong, *Science*, 2009, **324**, 63.
6 W. S. Choi, M. F. Chisholm, D. J. Singh, T. Choi, G. E. Jellison Jr. and H. N. Lee, *Nat. Commun.*, 2012, **3**, 689.
7 I. Grinberg, D. Vincent West, M. Torres, G. Gou, D. M. Stein, L. Wu, G. Chen, E. M. Gallo, A. R. Akbashev, P. K. Davies, J. E. Spanier and A. M. Rappe, *Nature*, 2013, **503**, 509.
8 Y. Bai, P. Tofel, J. Palosaari, H. Jantunen and J. Juuti, *Adv. Mater.*, 2017, **29**, 29.
9 M. Wu, X. Lou, T. Li, J. Li, S. Wang, W. Li, B. Peng and G. Gou, *J. Alloys Compd.*, 2017, **15**, 1093.
10 T. G. Amos and A. W. Sleight, *J. Solid State Chem.*, 2001, **160**, 230.
11 C. Bergner, V. Vashook, S. Leoni and H. Langbein, *J. Solid State Chem.*, 2009, **182**, 2053.
12 C. Börrnert, J. Zosel, A. Polte, R. Wenzel, U. Guth and H. Langbein, *Mater. Res. Bull.*, 2011, **46**, 1955.
13 L. M. D. Cranswick, W. G. Mumme, I. E. Grey, R. S. Roth and P. Bordet, *J. Solid State Chem.*, 2003, **172**, 178.
14 X. Kuang, J. B. Claridge, T. Price, D. M. Iddles and M. J. Rosseinsky, *Inorg. Chem.*, 2008, **47**, 8444.
15 Y. Miseki, H. Kato and A. Kudo, *Energy Environ. Sci.*, 2009, **2**, 306.
16 X. Xu, C. Randorn, P. Efstathiou and J. T. S. Irvine, *Nat. Mater.*, 2012, **11**, 595.
17 S. V. Alchangyan and I. P. Kislyakov, *Izv. Vyssh. Uchebn. Zaved., Khim. Khim. Tekhnol.*, 1975, **18**, 696.
18 V. K. Trunov, E. V. Murashova, Y. V. Oboznenko, Y. A. Velikodnyi and L. N. Kinzhibaio, *Russ. J. Inorg. Chem.*, 1985, **30**, 269.

19 A. K. Paidi, P. W. Jaschin, K. B. R. Varma and K. Vidyasagar, *Inorg. Chem.*, 2017, **56**, 12631.

20 S. J. Clark, M. D. Segall, C. J. Pickard, P. J. Hasnip, M. J. Probert, K. Refson and M. C. Payne, *Z. Kristallogr.*, 2005, **220**, 567.

21 J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou and K. Burke, *Phys. Rev. Lett.*, 2008, **100**, 136406.

22 D. R. Hamman, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2013, **88**, 085117.

23 D. R. Hamman, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2017, **95**, 239906.

24 X. Gonze, *Phys. Rev. A: At., Mol., Opt. Phys.*, 1995, **52**, 1086.

25 X. Gonze, *Phys. Rev. A: At., Mol., Opt. Phys.*, 1995, **52**, 1096.

26 J. Wang, J. Deng, R. Yu, J. Chen and X. Xing, *Dalton Trans.*, 2011, **40**, 3394.

27 A. A. Coelho, *J. Appl. Crystallogr.*, 2003, **36**, 86–95.

28 G. Oszlányi and A. Süto, *Acta Crystallogr., Sect. A: Found. Adv.*, 2004, **60**, 134.

29 M. Neslpolo, G. Ferraris and H. Ohashi, *Acta Crystallogr., Sect. B: Struct. Sci.*, 1999, **55**, 902.

30 C. Capillas, E. S. Tasci, G. de la Flor, D. Orobengoa, J. M. Perez-Mato and M. I. Aroyo, *Z. Kristallogr.*, 2011, **226**, 186.

31 K. Momma and F. Izumi, *J. Appl. Crystallogr.*, 2011, **44**, 1272.

32 Y. Repelin, E. Husson, F. Bennani and C. Proust, *J. Phys. Chem. Solids*, 1999, **60**, 819.

33 J.-M. Jehng and I. E. Wachs, *Chem. Mater.*, 1991, **3**, 100.

34 N. A. Spaldin, *J. Solid State Chem.*, 2012, **195**, 2.

35 D. L. Serra and S.-J. Hwu, *J. Solid State Chem.*, 1992, **98**, 174.

36 S.-J. Oh, D. W. Lee and K. M. Ok, *Inorg. Chem.*, 2012, **51**, 5393.

37 R. Spanchenko and E. Antipov, Joint Committee of Powder Diffraction Standards, 2000, Card Entry #52-1582.

38 R. L. Frost, K. L. Erickson, M. L. Weier and O. Carmody, *Spectrochim. Acta, Part A*, 2005, **61**, 829.

39 R. L. Frost, D. A. Henry, M. L. Weier and W. Martens, *J. Raman Spectrosc.*, 2006, **37**, 722.

40 J. F. Scott, *J. Phys.: Condens. Matter*, 2008, **20**, 021001.