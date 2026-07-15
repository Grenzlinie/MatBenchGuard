# Study on electronic properties of $\alpha$-, $\beta$- and $\gamma$-AlH₃ – The theoretical approach

M. Savić *, J. Radaković, K. Batalović

Institute of Nuclear Sciences Vinča, P.O. Box 522, University of Belgrade, 11000 Belgrade, Serbia

---

## A R T I C L E I N F O

**Article history:**
Received 21 November 2016
Received in revised form 6 March 2017
Accepted 22 March 2017

**Keywords:**
Hydrogen storage
AlH₃
Electronic properties
Band gap
Charge analysis

---

## A B S T R A C T

AlH₃ polymorphs ($\alpha$-, $\beta$-, $\gamma$-) are highly promising materials for hydrogen storage and hydride electronics applications. Given the recent developments in the synthesis and hydrogen desorption approaches, here presented detailed comparison study of three AlH₃ polymorphs ($\alpha$-, $\beta$-, $\gamma$-) is aimed to explain and potentially guide the improvements in applicability of these materials. We use electronic structure calculations based on the density functional theory (DFT) to address stability and bonding in $\alpha$-, $\beta$- and $\gamma$-AlH₃. For better understanding of stability of various polymorphs, formation enthalpy of $\alpha'$-AlH₃ is also addressed. Electronic properties (electronic density distribution, density of states, band structure and Bader's charge) are calculated using both generalized gradient approximation (GGA) of Perdew-Burke-Ernzerhof (PBE) for exchange-correlation, as well as additional Tran-Blaha modified Becke-Johnson functional (TBmBJ) for exchange. Study shows interesting correlation of electronic structure and bond strength, not observed in previously reported studies of alanes, and presents results obtained using TBmBJ method applied on $\beta$- and $\gamma$-alanes. Band gaps, calculated using TBmBJ, are increased up to 96% as compared to the GGA-PBE values. Due to the lack of experimental data, strong conclusion on the applicability of TBmBJ for alanes cannot be made, although good agreement to G₀W₀ value and overestimation of GW value is seen in case of $\alpha$-AlH₃. Band structure calculations lead to conclusions on electron mobility and other types of application beside hydrogen storage, while based on Bader's theory we compare bonding in all investigated polymorphs.

© 2017 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Hydrogen has been studied as an attractive energy carrier for many years. The major disadvantage for the broad use of hydrogen energy is its storage, and storing hydrogen in suitable materials have shown to be an interesting option. Materials used for this purpose must be safe, recyclable, cheap, and have the ability to release hydrogen, which depends on their stability. This is the greatest focus of experimental research nowadays and the major problem to be overcome. Gravimetric target for on board hydrogen storage materials set by U.S. DOE (Department of Energy) went from 6 wt% hydrogen in 2010 to 9 wt% hydrogen in 2015 [1].

One promising material, which meets these preconditions, is AlH₃ (alane) with volumetric density of 0.148 kg H₂/l [2] and high hydrogen content of 10.1 wt% [3]. So far scientists have confirmed the existence of seven alane polymorphs $\alpha$-, $\alpha'$-, $\beta$-, $\gamma$-, $\delta$-, $\varepsilon$-, $\zeta$-. According to many studies, all AlH₃ polymorphs are metastable at ambient conditions, however using different synthesizing techniques it is possible to obtain the polymorph of interest. First synthesis of AlH₃ ether solvated form [4] and AlH₃ adduct (C₆H₁₂N₂-AlH₃) [5] were reported over half century ago. Since then, organo-metallic synthesis of six AlH₃ polymorphs was reported [3]. Studies [6,7] report in detail organo-metallic synthesis of $\alpha$-, $\beta$- and $\gamma$-AlH₃. Recently, mechanochemical synthesis showed many advantages over the chemical synthesis: it is greener (solvent free) and cheaper than the standard methods [8], giving the possibility to avoid environmental problems and to accelerate and simplify synthesizing process. Several AlH₃ polymorphs ($\alpha$-, $\alpha'$-, $\beta$-, and $\gamma$-) were synthesized during cryomilling of LiAlH₄ and AlCl₃ at low temperature [9]. Mechanochemical synthesis of $\alpha$-AlH₃ [10] and $\alpha$- and $\alpha'$-AlD₃ [11], and $\gamma$-AlH₃ [12,13] under ambient conditions is reported. Synthesis of $\beta$-polymorph using mechanochemical method at ambient conditions is not noticed reviewing the literature.

Besides applications in hydrogen economy alanes are also very interesting due to their electronic structure, and could potentially find application in electronic devices, i.e. hydride electronics [14]. Karazhanov et al. [14,15] reported interesting properties of some AlH₃ phases, and classified alanes as wide band gap

---

* Corresponding author.
E-mail address: msavic@vinca.bg.ac.rs (M. Savić).

http://dx.doi.org/10.1016/j.commatsci.2017.03.034
0927-0256/© 2017 Elsevier B.V. All rights reserved.

semiconductors, translucent to electromagnetic waves in VIS/UV range, having well dispersive bottommost CB (conduction band) and/or topmost VB (valence band) therefore allowing electronic conductivity. Recently, activation of $\alpha$-AlH$_3$ using UV irradiation was demonstrated [16], showing how optical properties can be exploited to improve hydrogen storage properties.

In this work, we use theoretical approach to investigate crystal structure, stability and electronic features of $\alpha$-, $\beta$- and $\gamma$-AlH$_3$, three most commonly synthesized alane polymorphs. The choice to investigate electronic properties is due to the fact that information regarding optical properties of $\beta$- and $\gamma$-AlH$_3$ is obtained so far using LDA and GGA exchange-correlation potentials, leading to well-known deficiency of DFT approach for semiconductors. Therefore, we hope to address systematically electronic properties of the studied polymorphs in order to explain and potentially enhance their performances for various applications, including hydrogen storage and electronic devices.

## 2. Computational details and methodology

Electronic structure calculations are performed based on DFT [17] using FP LAPW + lo (full potential linearized augmented plane waves + local orbital) method (implemented in wien2k [18] program package). For comparison, identical parameters for investigated polymorphs are used for $R_{\text{MT}}K_{\text{max}}$ (i.e. the size and the completeness of sets of basis function), and number of k-points (i.e. the quality of Brillouin zone sampling). Parameters are set as follows: $R_{\text{MT}}$ (Al) = 1.75 bohr, $R_{\text{MT}}$ (H) = 0.95 bohr, $R_{\text{MT}}K_{\text{max}}$ is set to 9.20 for aluminum and 5.00 for polymorphs, while the magnitude of the largest vector G in the Fourier expansion is set to $20\ \text{bohr}^{-1}$. The k-points sampling is performed using $14 \times 14 \times 14$ grid for Al, $\alpha$- and $\beta$-polymorphs, and $11 \times 8 \times 10$ grid is used for $\gamma$-polymorph. Energy to separate core and valence states is $-6.0$ Ry, treating $3s^2\ 3p^1$ Al states and $1s^1$ H states as valence. As a charge convergence criterion, the charge difference between two iterations in self-consistent field cycles is chosen 0.00005e. The relaxation of crystal structures, according to the lattice symmetry, is performed by minimizing the forces that affect atoms until they became less than $1\ \text{m Ry bohr}^{-1}$. Exchange-correlation (XC) interactions are treated within general gradient approximation of Perdew-Burke-Ernzerhof (GGA-PBE) [19] during the structure optimization. In order to accurately address band structure, and given that energy of CB minimum is dependent on the exchange and correlation terms of the potential, additional calculations are done after structure optimization. Modified version of the Becke-Johnson potential is used (TBmBJ – uses local density approximation and modified Becke-Johnson density functional (LDA-mBJ)) for exchange [20], that adds a small amount of non-local Hartree-Fock (HF) exchange to the semi local density functional. Bader's [21] quantum theory of atoms in molecules (AIM) is used to investigate the character of bonds.

## 3. Results and discussion

### 3.1. AlH$_3$ polymorphs – crystal structures and stability

Fig. 1 shows crystal structures of Al and AlH$_3$ polymorphs. $\alpha$- and $\beta$-AlH$_3$ have hexagonal and cubic unit cell respectively, while $\gamma$-AlH$_3$ has orthorhombic unit cell with two nonequivalent Al atoms and four nonequivalent H atoms. Fig. 1(d) and (e) show two hydrogen atoms, labeled as H-2 and four atoms labeled as H-4 that surround Al-1 atom, and atoms H-1, H-2, two H-3 and two H-4 surround Al-2 atom.

Comparing to Al which crystallizes in the fcc structure (space group Fm-3 m, calculated lattice parameter $a = 4.0395\ \text{Å}$ (4.0460 [22])), Al atoms in investigated polymorphs form a distorted face-centered structure (tilted in different angle for each polymorph). 6 H atoms octahedrally coordinate each Al atom. Calculated lattice parameters and atomic positions of AlH$_3$ polymorphs are given in Table 1, while Table 2 gives interatomic distances of H-H, Al-H, and Al-Al.

In addition to $\alpha$-, $\beta$-, and $\gamma$-AlH$_3$, in Table 1 we also report relaxed structure of $\alpha'$-polymorph; it was calculated in order to complement investigation of thermodynamics of the studied alanes. Optimized structural parameters for all phases are in good agreement with experimental and previously reported theoretical results, with discrepancies less than 2%, which is in range of GGA-DFT precision. Possible reasons for small deviations are using different theoretical approach (e.g. high-pressure study [27]) experimental conditions [28]. The volume of formula unit is the greatest for $\beta$-AlH$_3$ while $\alpha$-AlH$_3$ has the smallest unit cell volume. Large volume related to $\beta$-AlH$_3$ formula unit is due to the large distance between neighboring octahedra (3.9 Å, Fig. 1c). This could imply structural changes under different conditions (high pressure, temperature), as also noticed by Vajeeston et al. [31].

Calculated Al-H distances (Table 2) within all structures vary in range from 1.70 Å to 1.76 Å. It is noticed that Al-H distances in $\beta$-AlH$_3$ octahedra are 1.725 Å (exp. value of 1.712 Å [28]), which is close to interatomic distances between Al and H in $\alpha$-AlH$_3$ octahedra, 1.717 Å (experimental value 1.715 Å [25]). Interatomic distance between two H atoms in $\beta$-AlH$_3$ is the shortest among investigated polymorphs, in accordance with report of Brinks et al. [28]. Crystal structure and calculated interatomic distances are in agreement with previously reported results [24-26,31].

AlH$_3$ polymorphs are metastable and do not decompose at ambient conditions due to the existence of Al$_2$O$_3$ layer [32]. However, at elevated temperatures they decompose according to reaction (1) exhibiting low decomposition enthalpy.

$$
\mathrm{AlH}_{3} \rightarrow \mathrm{Al}+3 / 2 \mathrm{H}_{2} \tag{1}
$$

Reaction (1) is not easily reversible due to the entropy term [33], pointing out that Al does not absorb hydrogen under moderate temperature and pressure, and that high hydrogen gas pressure is needed ($P > 2.5$ GPa) [34]. However, enthalpy term is important because it reflects the stability of the Al-H bond. AlH$_3$ shows low enthalpy of formation as compared to other non-reversible hydrogen storage materials. For $\alpha$-AlH$_3$, experiments show that decomposition is a single step process [35], while for $\beta$-AlH$_3$ [36] it is reported that during decomposition phase transition to $\alpha'$-AlH$_3$, is followed by transformation to more stable $\alpha$-AlH$_3$ occurs before decomposition to Al and H$_2$. Also, $\gamma$-AlH$_3$ transforms to $\alpha$-AlH$_3$ during decomposition [35]. For $\beta$- to $\alpha$- transition, measured enthalpies are $-1.0\ \text{kJ/mol}\ \text{H}_2$ [37] and $-2.99\ \text{kJ/mol}$ [31], while for $\gamma$- to $\alpha$-measured values are $-1.9\ \text{kJ/mol}\ \text{H}_2$ [38] and $-1.14\ \text{kJ/mol}$ [31]. For $\alpha'$- to $\alpha$-AlH$_3$ transition, reported energy difference is $-1.1\ \text{kJ/mol}\ \text{H}_2$ [36] and $-0.4\ \text{kJ/mol}$ [31]. However, some experiments show that $\beta$-AlH$_3$ can decompose directly if suitable conditions are applied (i.e. lower temperature [6] or faster heating [36]); similar holds for $\gamma$-polymorph [39].

Pressure also lead to phase transitions among various alane polymorphs. $\gamma$-AlH$_3$ transforms into the $\alpha$-AlH$_3$ in the pressure range 1-2 GPa, at medium temperatures [40]. Study of Drozd et al. [41] reported that $\beta$-AlH$_3$ is stable below 6 GPa, while with further pressure increase, it transforms to $\alpha$-AlH$_3$.

To compare stability of three polymorphs we calculated enthalpy of formation, reaction (2). Enthalpy change in reaction (1) can be approximated by the change in electronic energy calculated from first principles [42,43] between product and reactants of the reaction. Energy of hydrogen molecule is obtained in [44] using the same exchange correlation (XC) functional.

![](./images/811037301474852865_1.jpg)

Fig. 1. Crystal structures of Al and AlH₃ polymorphs: (a) Al, (b) α-AlH₃, (c) β-AlH₃, (d) γ-AlH₃ unit cell, Al-1 atom is in the center of the octahedra, (e) γ-AlH₃ unit cell, Al-2 atom is in the center of the octahedra.

<table>
<caption>Table 1<br>Structural parameters of investigated polymorphs.</caption>
<thead>
<tr>
<th>Space group of AlH₃ polymorphs</th>
<th>a (Å)</th>
<th>b (Å)</th>
<th>c (Å)</th>
<th>V (Å³/f.u.)</th>
<th>Calculated atomic positions</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">α<br>167<br>R-3C</td>
<td>4.464</td>
<td rowspan="5">b = a</td>
<td>11.725</td>
<td>33.72</td>
<td rowspan="5">Al (0, 0, 0)<br>H (0.6205, 0, 0.25)</td>
</tr>
<tr>
<td>4.451[23]</td>
<td>11.818 (23)</td>
<td>33.80 [23]</td>
</tr>
<tr>
<td>4.492 [24]</td>
<td>11.821 (24)</td>
<td>33.50 [24]</td>
</tr>
<tr>
<td>4.449 [25]</td>
<td>11.804 (25)</td>
<td>33.72 [25]</td>
</tr>
<tr>
<td>4.450 [26]</td>
<td>11.82 (26)</td>
<td>33.78 [26]</td>
</tr>
<tr>
<td rowspan="3">β<br>227<br>Fd-3m</td>
<td>9.092</td>
<td rowspan="3">b = a</td>
<td rowspan="3">c = a</td>
<td>46.97</td>
<td rowspan="3">Al (0.5, 0, 0)<br>H (0.431, 0.125, 0.125)</td>
</tr>
<tr>
<td>9.049 [27]</td>
<td>46.31 [27]</td>
</tr>
<tr>
<td>9.004 [28]</td>
<td>45.62 [27]</td>
</tr>
<tr>
<td rowspan="4">γ<br>58<br>Pnmm</td>
<td>5.452</td>
<td>7.445</td>
<td>5.822</td>
<td>39.39</td>
<td rowspan="4">Al-1 (0, 0, 0.5)<br>Al-2(0.7885, 0.0851,0)<br>H-1(0, 0.5, 0.5)<br>H-2(0.672, 0.2992, 0)<br>H-3(0.098, 0.1385, 0)<br>H-4(0.7985, 0.0818, 0.2974)</td>
</tr>
<tr>
<td>5.381 [26]</td>
<td>7.356 [26]</td>
<td>5.775 [26]</td>
<td>38.09 [26]</td>
</tr>
<tr>
<td>5.367 [29]</td>
<td>7.336 [29]</td>
<td>5.756 [29]</td>
<td>37.77 [29]</td>
</tr>
<tr>
<td>5.34 [30]</td>
<td>7.40 [30]</td>
<td>5.79 [30]</td>
<td>38.78 [30]</td>
</tr>
<tr>
<td rowspan="4">α'<br>63<br>Cmcm</td>
<td>6.598</td>
<td>11.153</td>
<td>6.623</td>
<td>40.61</td>
<td rowspan="4">Al-1 (0, 0.5, 0)<br>Al-2 (0.25, 0.25, 0)<br>H-1 (0, 0.2136, 0.448)<br>H-2 (0.3104, 0.1024, 0.0503)<br>H-3 (0, 0.4563, 0.25)<br>H-4 (0.2934, 0.2859, 0.25)</td>
</tr>
<tr>
<td>6.563 [31]</td>
<td>11.228 [31]</td>
<td>6.654 [31]</td>
<td>40.86 [31]</td>
</tr>
<tr>
<td>6.508 [27]</td>
<td>11.112 [27]</td>
<td>6.583 [27]</td>
<td>39.67 [27]</td>
</tr>
<tr>
<td>6.470 [11]</td>
<td>11.117 [11]</td>
<td>6.562 [11]</td>
<td>39.33 [11]</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2<br>Interatomic distances of the nearest neighbors in AlH₃ polymorphs.</caption>
<thead>
<tr>
<th colspan="2">Interatomic distances (Å)</th>
<th></th>
<th></th>
</tr>
<tr>
<th>AlH₃ polymorph</th>
<th>H-H</th>
<th>H-Al</th>
<th>Al-Al</th>
</tr>
</thead>
<tbody>
<tr>
<td>α</td>
<td>2.4112</td>
<td>1.7174</td>
<td>3.3244</td>
</tr>
<tr>
<td>β</td>
<td>2.3844</td>
<td>1.7254</td>
<td>3.2145</td>
</tr>
<tr>
<td>γ</td>
<td>H-1-H-4 2.4170</td>
<td>Al-1-H-4 1.7230</td>
<td>Al-1-Al-2 3.195</td>
</tr>
<tr>
<td></td>
<td>H-1-H-3 2.4221</td>
<td>Al-1-H-2 1.7648</td>
<td>Al-2-Al-2 2.631</td>
</tr>
<tr>
<td></td>
<td>H-1-H-4 2.4530</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>H-2-H-4 2.4172</td>
<td>Al-2-H-1 1.6957</td>
<td></td>
</tr>
<tr>
<td></td>
<td>H-2-H-3 2.6126</td>
<td>Al-2-H-2 1.7159</td>
<td></td>
</tr>
<tr>
<td></td>
<td>H-3-H-4 2.4172</td>
<td>Al-2-H-4 1.7326</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Al-2-H-3 1.7336</td>
<td></td>
</tr>
</tbody>
</table>

$$
\Delta H_{f}=E_{(AlH_{3})}-E_{(Al)}-3/2E_{(H_{2})} \tag{2}
$$

Calculated total electronic energies for Al, H₂, AlH₃ polymorphs and formation enthalpies are given in Table 3. In addition to the three studied polymorphs, we also included calculated formation enthalpy for α'-AlH₃, since it was identified as middle step in decomposition of β-AlH₃. Previously reported experimental and theoretical results are also listed.

Calculated formation enthalpies are in good agreement with experimental results for γ- and α-AlH₃, and predict stability order β-, α'-, α-, γ-AlH₃ in agreement with previous DFT reports [31,45]. However, higher calculated formation enthalpies of the β-AlH₃, and

<table>
<caption>Table 3<br>Total electronic energies of Al, H₂ and AlH₃ polymorphs and calculated formation enthalpies of AlH₃ polymorphs; formation enthalpies reported in literature are given for comparison; in cases where literature values for enthalpies of dehydrogenation (decomposition) are reported, we show them with opposite sign in the table for comparison.</caption>
<thead>
<tr>
<th>Products<br>and<br>reactants</th>
<th>Calculated<br>(DFT) total<br>electronic<br>energies (Ry)</th>
<th>Calculated<br>formation enthalpy<br>of AlH₃ polymorphs<br>(kJ/mol H₂)</th>
<th>Experimentally<br>measured values for<br>formation enthalpy of<br>AlH₃ polymorphs<br>(kJ/mol H₂)</th>
</tr>
</thead>
<tbody>
<tr>
<td>α-AlH₃</td>
<td>−489.1444</td>
<td>−7.6<br>−5.99 [31]<br>−8.23 [45]<br>−10.8 [30]</td>
<td>−7.9 [6]<br>−6.00 [37]<br>−6.6 [46,36]<br>−7.6 [47]</td>
</tr>
<tr>
<td>β-AlH₃</td>
<td>−489.1476</td>
<td>−10.4<br>−8.98 [31]<br>−10.09 [45]</td>
<td>−6.4 [6]<br>−6.3 [36]</td>
</tr>
<tr>
<td>γ-AlH₃</td>
<td>−489.1441</td>
<td>−7.3<br>−10.8 [30]<br>−7.13[31]</td>
<td>−5.6 [6]<br>−7.1 [26],<br>−6.6 [36]<br>−1.00 [37]</td>
</tr>
<tr>
<td>α'-AlH₃</td>
<td>−489.1463</td>
<td>−9.2<br>−7.54 [31]<br>−9.01[45]</td>
<td>/</td>
</tr>
<tr>
<td>Al</td>
<td>−485.6445</td>
<td></td>
<td></td>
</tr>
<tr>
<td>H₂</td>
<td>−2.3275 [44]</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

$\alpha'-AlH_3$ than the one of $\alpha-AlH_3$, contradicts the experiments. Namely, our calculations, as well as all other reported DFT works [24,45] predict the greatest stability of $\beta-AlH_3$, while experimen- tally $\alpha-AlH_3$ is identified as the most stable, as discussed above. Few reasons might be the cause of this discrepancy. The calcula- tions are done for ideal crystal structures at temperature of 0 K, while experiments relate to room temperature or higher; as also discussed by Ke et al. [45] it is possible that at 0 K $\beta$-polymorph is the most stable one. Final argument to the greater stability of $\alpha-AlH_3$ would be to show that upon temperature drop, it do not transform to $\beta-AlH_3$, as pointed by Ojwang et al. [34]. However, it is also noted that small difference between determined forma- tion energies might be hardly resolved by DFT; all here studied polymorphs show practically the same formation enthalpies when taking into account precision of DFT approach [43].

The discrepancy between the polymorph stability trend in DFT calculations and experimental findings is reported in many DFT studies [24,48,45,34]. Only by adjusting reactive force filed in

![](./images/811037301474852865_2.jpg)

Fig. 2. (a) Total and angular momentum projected density of Al states, (b) density of states for $AlH_3$ polymorphs obtained using TBmBJ method.

![](./images/811037301474852865_3.jpg)

Fig. 3. 2D plots of charge distribution (in $e/\AA^3$) in valence and conduction zone of $\beta-AlH_3$ obtained using GGA-PBE and TBmBJ potential, calculated for the same energy range. Figures (a), (c) are obtained using GGA-PBE, while (b) and (d) are obtained using TBmBJ: (a), (b) VZ of the plane that shows bond between Al and H; (c), (d) CZ of the plane in which the bond is between Al and H;

PAW calculation, experimental trend is reproduced [34]. Interest- ingly, comparing to those results, we find agreement to the relative stability of $\beta$- and $\gamma$-polymorphs; namely, we calculate $\beta$-AlH₃ to be $3.1\ \text{kJ/mol}\ \text{H}_2$ more stable than $\gamma$-AlH₃, in excellent agreement with the value obtained in the study of Ojwang et al. (3.2 kJ/- mol $\text{H}_2$) [34]. It is important to highlight that our comparison of stability of various polymorphs is based on the calculated energies of formation where zero point energy (ZPE) contribution is dis- carded. However, this issue was addressed in the work of Vajeeston et al. [49], and even if the reported ZPEs for $\alpha$-, $\beta$- and $\gamma$-AlH₃ (0.661, 0.664 and 0.655 eV/f.u, respectively) are considered, $\beta$- AlH₃ is still the most stable polymorph. Further, study of Ojwang et al. [34] pointed out that use of pseudopotentials might be the cause of disagreement with experiment; however, in here pre- sented full-potential all-electron study $\beta$-AlH₃ is determined as the most stable polymorph at 0 K, as in other DFT reports (Table 3).

As pointed out, calculated energies of formation of various alane polymorphs differ by up to $3\ \text{kJ/mol}\ \text{H}_2$; given such small energy differences, multiple alanes can be expected to form simultane- ously in experimentally prepared samples, and this is usually the case [48]. However, while predicted as the most stable by DFT, $\beta$- polymorph is not synthesized often, while $\alpha$-, $\alpha'$- and even $\gamma$- are more likely to form [35]. Additional reasons other than the ones related to precision of DFT calculations might explain this discrep- ancy; firstly, DFT calculations refer to ideal crystal at 0 K, while most synthesis are done at room temperature or higher; this could lead to different stability order [35]. Two recently published stud- ies described wet technique of synthesis [6,7], which is used for preparation of $\beta$-alane; both studies agree that prepared sample experiences a structural transition to $\alpha$-AlH₃ before achieving steady structure, when heated for longer time. Additionally, during cryomilling synthesis of $\alpha'$-AlH₃ (also found to be more stable than $\alpha$-AlH₃ in our DFT calculations) it is not observed that it undergoes transition to $\alpha$-AlH₃, implying it has higher stability than $\alpha$-AlH₃ at low temperatures [48]. Secondly, different structures and volumes of formula units seen in the studied polymorphs imply that other factors other than thermodynamics can play important role in the real systems, i.e. during synthesis, as opposed to ideally order systems used in calculations. $\beta$-AlH₃ has peculiar cubic structure with wide channels and the highest volume per unit cell among all studied polymorphs (see Table 1); on the other hand, as sug- gested by Vajeeston et al., due to the compact atomic arrangement and less pore sizes, $\alpha$-AlH₃ becomes very stable compared to the other polymorphs [31].

We further discuss the stability of the studied polymorphs based on their electronic structure in next section.

### 3.2. Electronic structure

In Fig. 2 are presented density of states (DOS) diagrams for Al and all studied polymorphs, as well as angular momentum pro- jected DOS for Al. Aluminum, being a metal, shows continuum of electronic states at energies above Fermi energy. On the other hand, aluminum hydride polymorphs exhibit non-metal nature and different band gap width.

It is known that (semi)local exchange-correlation functionals lead to KS band gaps, which underestimate experimental band gaps of solids, by 30–100% [50]. To overcome the deficiency of GGA-PBE for determination of excited state properties of alanes we used modified version of the Becke-Johnson exchange potential plus LDA-correlation (TBmBJ) [20]. TBmBJ potential is also semi local potential, but it mimics the behavior of orbital-dependent potentials, at computational cost of standard DFT calculation [20]. It was found suitable for various classes of semiconductors, including also semiconducting hydrides [51]. The applicability of TBmBJ relies on the fact that the overlap between the occupied and unoccupied orbitals around the band gap is usually small and thus an orbital-independent potential could catch the essen- tials of orbital-dependent potentials [20]. To illustrate this, for the case of here studied alanes, in Fig. 3 we depict calculated 2D charge density plot for valence and conduction zone of $\beta$-AlH₃, using both GGA and TBmBJ.

Fig. 3(a)-(d) represents charge density 2D plots of valence (VZ) and conduction zone (CZ) of $\beta$-AlH₃ obtained using GGA-PBE and TBmBJ potential. Charge density distributions are showing similar shape in both cases, and reflect decrease in VB width seen in TBmBJ case (VZ narrowed for 1.47 eV). While charge around hydrogen dominates top of the valence band, Al s electrons dominate bottom of the conduction band (this is also seen at Fig. 5, and holds for all studied polymorphs); consequently, different spatial distribution of charge in VB and CB enable TBmBJ potential to mimic orbital- dependent potentials in this case. In area where the charge density is high, the TB-mBJ exchange potential will be positive causing CZ shifting to higher energies, leading to wider band gaps comparing to gaps obtained with GGA-PBE method.

![](./images/811037301474852865_4.jpg)

Fig. 4. Band structure using TBmBJ method for (a) $\alpha$-AlH₃, (b) $\beta$-AlH₃ and (c) $\gamma$-AlH₃.

Table 4 presents calculated band gap energies; for comparison, results reported in the literature, obtained with different levels of approximations are also listed.

Use of the TBmBJ leads to the significant increase of calculated BG in all polymorphs as compared to GGA-PBE value (e.g. 96% for β-AlH₃). Extensive list of band gap values obtained with different approximations is available from literature for α-AlH₃, enabling the discussion, while for β- and γ-AlH₃, literature provides results obtained using GGA-PBE. Our results obtained using GGA approximation are in excellent agreement with other reports (Table 4). TBmBJ band gap calculated for α-AlH₃ shows good agreement with all-electron non-self-consistent G₀W₀ results reported [54], as well as excellent agreement with Singh's TBmBJ value obtained for the experimental lattice parameters of α-AlH₃ [51]; agreement with the experimental value is discussed in the next paragraph. We considered here also the suggestion of that optimization procedure can lead to large deviation in calculated BG values [58], and calculated TBmBJ BG for LDA relaxed structure. We concluded that relaxation of the hydride structure do not play important role in the final BG value obtained, as they leads to small variations in the BG value (up to 0.3%).

Best to our knowledge, there are no literature references for experimental values or GW values for β-, γ- or α'-polymorph. As experimental band gap of α-polymorph Gabis et al. [16] adopted GW value of 3.54 eV [54], and in the work they further focus on photoluminescence investigation to find significant absorption for 4.88 eV mercury line. Therefore, additional experimental investigation might also be needed to address BG of α-AlH₃, as well as to consider temperature effects. Namely, experimental BG measured at room temperature should be extrapolated to 0 K for comparison to DFT values, due to the general trend of gap narrowing with temperature [59]. Having all this in mind, we compare here calculated TBmBJ BG to the value 3.54 eV adopted in experimental work of Gabis et al. [16], and we see that estimation of the band gaps for the α-polymorph is improved in comparison to GGA BG, but also significant overestimation of the experimental value is seen. However, earlier investigation of ionic hydrides [51] (LiH, MgH₂) showed much better agreement between TBmBJ and experimental band gap. Therefore, we would like to stress out that additional experimental results are needed in order to prove efficiency of TBmBJ for alanes, and also in order to, if proven necessary, further improve prediction for hydrides by optimizing semi empirical parameters in TBmBJ potential.

Further, we compare three studied hydrides.

In Fig. 4, band structure diagrams of studied polymorphs are presented. If orbital overlapping increases (e.g. if interatomic distance is decreasing), bonding interactions are stabilized and antibonding interactions are destabilized. This indicates well dispersive bands. The small overlapping leads to less dispersive bands what indicates that electrons are localized.

From calculated band structure (Fig. 4), and based on the work of Karazhanov et al. [14] we consider all studied polymorphs are wide band gap semiconductors. It is possible to classify studied hydrides according to their main band gap characteristics [60]: band gap width (wide or narrow), localization (direct or indirect), and type (s, p, d). The conduction zone, compared to cases before TBmBJ introduction, is shifted to higher energies. Bands at the top of VB (Fig. 4) originate from H-s and Al-p states (Fig. 5) with dominant contribution of H-s states in all polymorphs, what enables classification of studied alanes as s-type hydrides, according to [60]. Direct band gap is seen in case of α-AlH₃ (Fig. 3(a)). According to [61], the greater the overlap between the electrons of the neighboring atoms, the greater band gap is going to be. β-AlH₃ has the widest band gap (6.04 eV) and shows less dispersive bands comparing to α-polymorph. Well dispersive bands in CB and, somewhat less, in VB found for α-AlH₃ imply possibility for good conductivity. Comparing band dispersion in β- and γ-AlH₃, we see that localized states and consequently weak electron mobility, is slightly more expressed in case of γ-AlH₃.

![](./images/811037301474852865_5.jpg)

Fig. 5. Site and angular momentum projected density of states: (a) α-AlH₃, (b) β-AlH₃, and (c) γ-AlH₃.

Band structure analysis of α-AlH₃ leads [14] to conclusion that electrons from the conduction zone contribute to electrical conductivity and it was expected that it has high mobility of electrons when it was doped with shallow donors, indicating the ability for n/p-electrical conductivity. Based on these indications, hydrides could also be used as buffer layers, solar cells or LED.

Applied TBmBJ method has confirmed previously reported characteristics of band structure for α-polymorph, and showed good agreement with results obtained using G₀W₀. For other two alanes, it shows significant increase in band gap width comparing to results obtained using LDA/GGA, and outlines the importance in

<table>
<caption>Table 4 Calculated band gaps and band gaps reported in literature.</caption>
<thead>
<tr>
<th>Polymorph</th>
<th>GGA-PBE</th>
<th>Other (semi) local approximations</th>
<th>TBmBJ</th>
<th>G₀W₀</th>
<th>Other theoretical methods</th>
</tr>
</thead>
<tbody>
<tr>
<td>α</td>
<td>2.37
2.34 [24]
2.53 [31]
2.45 [52]
2.27 [51]
2.104 [53]</td>
<td>GGA-PW 2.14 [14]
GGA 2.18 [54]
LDA 1.79 [54]</td>
<td>4.38
4.31 [51]</td>
<td>4.31 [54]</td>
<td>sX 3.35 [55]
GW<sub>core</sub> 3.54 [54]
HSE06 3.38 [56]</td>
</tr>
<tr>
<td>β</td>
<td>3.08
3.22 [24]
2.44 [27]
3.85 [31]</td>
<td></td>
<td>6.04</td>
<td></td>
<td></td>
</tr>
<tr>
<td>γ</td>
<td>3.20
2.80 [14]
3.24 [24]
4.41 [31]</td>
<td></td>
<td>5.44</td>
<td></td>
<td></td>
</tr>
<tr>
<td>α′</td>
<td>2.81
2.82 [27]</td>
<td>LDA 2.1 [57]</td>
<td>5.25</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<caption>Table 5 The number of electrons in valence zone (obtained by integrating DOS curves).</caption>
<thead>
<tr>
<th>DOS\ alane</th>
<th>α</th>
<th>β</th>
<th>γ</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tot Al</td>
<td>0.4444</td>
<td>0.4124</td>
<td>Al-1: 0.4204
Al-2: 0.4400</td>
</tr>
<tr>
<td>Al-s</td>
<td>0.1864</td>
<td>0.1709</td>
<td>Al-1: 0.1801
Al-2: 0.1978</td>
</tr>
<tr>
<td>Al-p</td>
<td>0.1986</td>
<td>0.1836</td>
<td>Al-1: 0.1852
Al-2: 0.1978</td>
</tr>
<tr>
<td>Tot H</td>
<td>0.5273</td>
<td>0.5553</td>
<td>H-1: 0.5491
H-2: 0.5346
H-3: 0.5193
H-4: 0.5336</td>
</tr>
<tr>
<td>H-s</td>
<td>0.5242</td>
<td>0.5521</td>
<td>H-1: 0.5470
H-2: 0.5326
H-3: 0.5143
H-4: 0.5304</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 6 Bader's charge (difference between the charge of neutral atom and the charge in the (atomic) basin of given atoms) for studied AlH₃ polymorphs.</caption>
<thead>
<tr>
<th>AlH₃ polymorph</th>
<th>Bader charge (GGA-PBE) (e)</th>
<th>Bader charge (TBmBJ) (e)</th>
</tr>
</thead>
<tbody>
<tr>
<td>α</td>
<td>Al (2.34 ± 0.01)
H (−0.78 ± 0.01)</td>
<td>Al (2.59 ± 0.01)
H (−0.86 ± 0.01)</td>
</tr>
<tr>
<td>β</td>
<td>Al (2.34 ± 0.01)
H (−0.78 ± 0.01)</td>
<td>Al (2.64 ± 0.01)
H (−0.88 ± 0.01)</td>
</tr>
<tr>
<td>γ</td>
<td>Al-1(2.32 ± 0.01)
Al-2(2.34 ± 0.01)
H-1 (−0.78 ± 0.01)
H-2 (−0.77 ± 0.01)
H-3 (−0.78 ± 0.01)
H-4 (−0.77 ± 0.01)</td>
<td>Al-1(2.60 ± 0.01)
Al-2(2.61 ± 0.01)
H-1 (−0.87 ± 0.01)
H-2 (−0.87 ± 0.01)
H-3 (−0.87 ± 0.01)
H-4 (−0.87 ± 0.01)</td>
</tr>
</tbody>
</table>

using different exchange potentials for real band gap estimation instead of standard (GGA-PBE).

Fig. 5 depicts DOS diagrams for α-, β- and γ-polymorphs.

All studied polymorphs show dominant contribution of Al-s states at lower energies while Al-p states are dominant in the range of higher energies (top of VB). It is seen that contribution of H s-states spans the whole energy range, i.e. we see its interaction with both s- and p-Al states. Comparing studied polymorphs, the increase in overlap is noticed when interatomic distance between atoms in lattice is smaller. In case of α-AlH₃, overlap of Al-p and H-s is evident. Dominant contribution at energies close to Fermi energy comes from p-states. β-polymorph, comparing to α-, shows more narrow valence zone (7.3 eV). Al s-states dominate the bottom of CB; also contribution of Al-p is significant. DOS diagram for γ-AlH₃ shows more complex picture due to the existence of two nonequivalent Al atoms and four nonequivalent H atoms. Top of VB is dominated by H-s, while bottom of CB is (same as in case of β-AlH₃) mainly from Al-s and, in small part, Al-p states.

According to calculated interatomic distances between Al and H atoms in crystal cells of polymorphs, we discuss bond strength. Bond strength depends on bond length, and we can expect that the stronger the bond is between Al and H, the smaller interatomic distance is between them. Comparing the interatomic distance between H and Al atoms (Table 2) and DOS diagram (Fig. 5c); we see that the further the peak of H s-state from the Fermi energy, the shorter the bond is; this would imply the weaker bond (in agreement with [62]) and could imply the order of desorption from γ-alane. This is seen based on the peak (maximum) positions of H s-states: s-H-3, s-H-4, s-H-2 and s-H-1. Importantly, s-H-3 peak is the nearest to the top of VB.

To further discus hydride stability, density of states curves were integrated to obtain the number of electrons in VB. Obtained values are given in Table 5; orbital dependent DOS curves represent electronic states distribution within RMT sphere (without states in interstitial area).

The highest number of H-s electrons is noticed in case of β-polymorph. The number of electrons decrease in γ-polymorph and the lowest number of electrons (H-s) is seen for α-AlH₃.

Based on everything discussed, we conclude that for the studied alanes, the highest stability of β-polymorph (see Table 3) is reflected in higher amount of electrons on hydrogen atom.

### 3.3. Charge transfer based on QTAIM

Additional investigation of bonding in studied polymorphs is performed based on Bader's [21] quantum theory of atoms in molecules (AIM). Based on the electron density ($\rho$) and Laplacian of the electron density ($\nabla^2\rho$) in bcp, classification of the bond is possible [63]. Table 6 shows values for calculated Bader's charges (GGA-PBE and TBmBJ). Values of Laplacian of the electron density, electron density and distances between bond critical point (bcp) and Al and bcp and H atoms for investigated alanes are given in Table 7.

According to values of Laplacian and electron density in bcp between Al and H atoms it is concluded that studied polymorphs show predominantly ionic bond character (Laplacian is positive and electron density relatively small - the larger Laplacian value and the smaller the electron density value, the more ionic bond

<table><thead><tr><th>AlH3polymorph</th><th>∇2ρ (e/Å5)</th><th>ρ (e/Å3)</th><th>bcp distance from Al (r1) (Å)</th><th>bcp distance from H (r2) (Å)</th></tr></thead><tbody><tr><td>α</td><td>0.1303</td><td>0.05438</td><td>0.8511</td><td>0.8667</td></tr><tr><td>β</td><td>0.1248</td><td>0.05387</td><td>0.8540</td><td>0.8719</td></tr><tr><td></td><td>0.2293</td><td>0.04814</td><td>0.8222</td><td>0.9040</td></tr><tr><td>γ</td><td>0.1269</td><td>0.05477</td><td>0.8511 (Al-1)</td><td>0.8718 (H-4)</td></tr><tr><td></td><td>0.1027</td><td>0.04843</td><td>0.8698</td><td>0.8949 (H-2)</td></tr><tr><td></td><td>0.1328</td><td>0.05559</td><td>0.8485 (Al-2)</td><td>0.8472 (H-1)</td></tr><tr><td></td><td>0.1194</td><td>0.05506</td><td>0.8527</td><td>0.8633 (H-2)</td></tr><tr><td></td><td>0.1238</td><td>0.05292</td><td>0.8557</td><td>0.8773 (H-4)</td></tr><tr><td></td><td>0.1426</td><td>0.05792</td><td>0.8445</td><td>0.8921 (H-3)</td></tr><tr><td></td><td>0.1307</td><td>0.05289</td><td>0.8558</td><td>0.9251 (H-3)</td></tr></tbody></table>

[63]). Charge transfer from Al to H is in accordance with electronegativity of the atoms. Great difference in electronegativity of Al and H (Al 1.61 and H 2.20) leads to redistribution of electrons in alane, reflected as mixing of Al-p and H-s states. According to the number of electrons obtained after DOS curve integration, it is noticed that mixing of states is the strongest in the case of β-AlH3indicating stronger bond than in the case of other two polymorphs. This conclusion agrees with [64], which states that electrons are during redistribution assigned usually to low lying states in the band, and in that way bond strength raises. Based on Bader's charge results (Table 6), obtained after the introduction of TBmBJ functional, slight increase in all atomic charges is observed. The greatest change is noticed in case of β-polymorph from 2.34 e (GGA-PBE) to 2.64 e (TBmBJ).

Conclusion of ionic bond character is in agreement with previous conclusions [45] saying that bond character is closer to ionic than to covalent. Ionic character is confirmed in Al-H bond on the basis of first principles study for different alanes [27]. Trend of calculated Bader charge is in agreement with study [65]; for comparison of calculated values also knowledge of used RMT values is needed. Electron density and Laplacian of electron density show slight difference to the values reported in [66]; the reason for discrepancy could be in the use of different methodology, which uses second order Moller-Plesset perturbation method.

From our results reported in Table 7, we can conclude that investigated polymorphs in general exhibit similar values of topological parameters. Laplacian of electron density shows the highest value for β-polymorph. Bcp is also found further away in this case.

## 4. Conclusion

We presented extensive DFT investigation on three alane polymorphs: α-, β- and γ-AlH3, in order to explain particularities of these most commonly synthesized phases, and potentially enable improvement of their features for hydrogen storage and hydrogen electronics applications. Study is focused on detail examination of electronic structure of investigated alanes. Discrepancies between theoretical and experimentally reported results regarding the structural properties are less than 2% what is in range of GGA-DFT precision. From obtained interatomic distances it is concluded that the shortest bond is found between H-1 and Al-2 in γ-AlH3. Obtained results for formation enthalpy are in agreement with other theoretical results obtained by DFT (−7.6 kJ/mol H2, −10.4 kJ/mol H2, −7.3 kJ/mol H2for α-, β- and γ-AlH3, respectively). Based on three main band structure features, it is concluded that investigated polymorphs are s-type, wide band gap semiconductors with direct band gap found in α-polymorph. Calculated band gap for α-AlH3(4.38 eV) obtained using TBmBJ functional is comparable with reported results, while for β- and γ-AlH3we obtained BG values: 6.04 eV, 5.44 eV respectively. TBmBJ improves estimation of the band gap of α-AlH3, showing agreement with G0W0value but overestimating reported GW value. Additional experimental results are needed in order to check performance of TBmBJ for other polymorphs. From band structure diagrams analysis imply different nature of the studied polymorphs, in terms of different level of band dispersion originating from localized or delocalized electrons. Higher delocalization of electrons in α-polymorph (comparing to other two polymorphs) imply possibility for good electron conductivity (n, p or both). Strong interaction between Al-p and H-s states enables forming more dispersive bands in β- comparing to γ-polymorph, and wider band gap. Beside high gravimetric capacity for hydrogen storage, AlH3polymorphs can be used for different applications related to electron mobility. Based on bond strength discussion for studied alanes, we concluded that stronger bond is reflected in higher amount of electrons on hydrogen atom that is obtained after DOS curves integration. Bader's charge analysis proved mainly ionic character of interactions between Al and H. β-AlH3shows the greatest change in Bader's charge after introduction of TBmBJ method, giving values of 2.64 e for Al and −0.88 for H atom.

## Acknowledgments

This work is done as a part of bilateral cooperation Serbia-Portugal 451-03-01765/2014-09/03, and under grant of Ministry of Science and Technological Development of Republic of Serbia, Project 171001. Authors thank Prof. Carmen Rangel for cooperation in this work.

## References

[1] Executive summaries for the Hydrogen storage materials centers of excellence chemical hydrogen storage CoE, hydrogen sorption CoE, and metal Hydride CoE period of Performance: 2005-2010, Fuel cell technologies program office of energy efficiency and renewable energy U.S. Department of Energy <https://www1.eere.energy.gov/hydrogenandfuelcells/pdfs/executive_summaries_h2_storage_coes.pdf> (August 2011).

[2] J. Reilly, J.J. Graetz, W.-M. Zhou, J. Johnson, J. Wegrzyn, Alkali metal hydride doping of α-AlH3for enhanced H2desorption kinetics, J. Alloy Compd. 421 (2006) 185-189.

[3] F.M. Brower, N.E. Matzek, P.F. Reigler, H.W. Rinn, C.B. Roberts, D.L. Schmidt, J.A. Snover, K. Terada, Preparation and properties of aluminum hydride, J. Am. Chem. Soc. 98 (1976) 2450-2453.

[4] A.E. Finholt, A.C. Bond, H.I. Schlesinger, Lithium aluminum hydride, aluminum hydride and lithium gallium hydride and some of their applications in organic and inorganic chemistry, J. Am. Chem. Soc. 69 (1947) 1199-1203.

[5] E.C. Ashby, The direct synthesis of amine alanes, J. Am. Chem. Soc. 86 (1964) 1882-1883.

[6] J. Liu, B. Xu, X. Wang, Preparation and thermal properties of aluminum hydride polymorphs, Vacuum 99 (2014) 127-134.

[7] J. Graetz, J.J. Reilly, Decomposition kinetics of the AlH3polymorphs, J. Phys. Chem. B 109 (2005) 22181-22185.

[8] D.K. Lee, S.Y. Lee, B.I. Park, S. Yu, Y. Hwang, S.H. Cho, J.S. Lee, C. Park, Highly crystalline Fe2GeS4nanocrystals: green synthesis and their structural and optical characterization, J. Mater. Chem. A 3 (2015) 2265-2270.

[9] M. Paskevicius, D.A. Sheppard, C.E. Buckley, Characterisation of mechanochemically synthesised alane (AlH3) nanoparticles, J. Alloy. Compd. 487 (2009) 370-376.

[10] S. Gupta, M. Pruski, V.K. Pecharsky, T. Kobayashi, I.Z. Hlova, J.F. Goldston, Solvent-free mechanochemical synthesis of alane, $AlH_3$: effect of pressure on the reaction pathway, Green Chem. 16 (2014) 4378-4788.

[11] H.W. Brinks, A. Istad-Lem, B.C. Hauback, Mechanochemical synthesis and crystal structure of $\alpha'-AlD_3$ and $\alpha -AlD_3$, J. Phys. Chem. B 110 (2006) 25833-25837.

[12] C.W. Duan, L.X. Hu, Y. Sun, H.P. Zhou, H. Yu, Reaction kinetics for the solid state synthesis of the $AlH_3/MgCl_2$ nano-composite by mechanical milling, Phys. Chem. Chem. Phys. 17 (2015) 22152-22159.

[13] L.X. Hu, C.W. Duan, D. Xue, Solid state synthesis of nano-sized $AlH_3$ and its dehydriding behavior, Green Chem. 17 (2015) 3466-3474.

[14] S.Zh. Karazhanov, P. Ravindran, P. Vajeeston, A.G. Ulyashin, Hydride electronics, Phys. Status Solidi (a) 204 (10) (2007) 3538-3544.

[15] S.Z. Karazhanov, A.G. Ulyashin, P. Ravindran, P. Vajeeston, Semiconducting hydrides, EPL 82 (2008) 17006-17010.

[16] I.E. Gabis, A.P. Baraban, V.G. Kuznetsov, D.I. Elets, M.A. Dobrotvorskii, A.P. Voyt, A mechanism of ultraviolet activation of the $\alpha-AlH_3$ decomposition, Int. J. Hydrogen Energy 39 (28) (2014) 15844-15850.

[17] P. Hohenberg, W. Kohn, Inhomogeneous electron gas, Phys. Rev. 136 (3B)(1964) B864-B871.

[18] P. Blaha, K. Schwarz, G.K.H. Madsen, D. Kvasnicka, J. Luitz, WIEN2k, An Augmented Plane Wave + Local Orbitals Program for Calculating Crystal Properties, Karlheinz Schwarz, Techn. Universitat Wien, Austria, Wien, 2001, ISBN 3-9051031-1-2.

[19] J.P. Perdew, K. Burke, M. Enzerhof, Generalized gradient approximation made simple, PRL 77 (1996) 3865-3868.

[20] F. Tran, P. Blaha, Accurate band gaps of semiconductors and insulators with a semilocal exchange-correlation potential, Phys. Rev. Lett. 102 (2009) 226401-226404.

[21] R.F.W. Bader, A bond path: a universal indicator of bonded interactions, J. Phys. Chem. A 102 (1998) 7314-7323.

[22] W.P. Davey, Precision measurements of the lattice constants of twelve common metals, Phys. Rev. 25 (1925) 753-761.

[23] K. Ikeda, H. Ohshita, N. Kaneko, J. Zhang, M. Yonemura, T. Otomo, K. Suzuya, H. Yukawa, M. Morinaga, H.-W. Li, S. Semboshi, S. Orimo, Structural and hydrogen desorption properties of aluminum hydride, Mater. Trans. 52 (2011) 598-601.

[24] P. Vajeeston, P. Ravindran, H. Fjellvåg, Novel high pressure phases of $\beta-AlH_3$: a density-functional study, Chem. Mater. 20 (2008) 5997-6002.

[25] W. Turley, H.W. Rinn, The crystal structure of aluminum hydride, Inorg. Chem.8(1)(1968)18-22.

[26] V.A. Yartys, R.V. Denys, J.P. Maehlen, C. Frommen, M. Fichtner, B.M. Bulychev, H. Emerich, Double-bridge bonding of aluminium and hydrogen in the crystal structure of $\gamma-AlH_3$, Inorg. Chem. 46 (1) (2007) 1051-1055.

[27] W. Feng, S. Cui, M. Feng, First-principles study of structural stabilities of $AlH_3$ under high pressure, J. Phys. Chem. Solids 75 (2014) 803-807.

[28] H.W. Brinks, C.M. Jensen, J. Graetz, J.J. Reilly, B.C. Hauback, Synthesis and crystal structure of $\beta-AlD_3$, J. Alloy. Compd. 433 (2007) 180-183.

[29] B.C. Hauback, H.W. Brinks, C. Brown, C.M. Jensen, J. Graetz, J.J. Reilly, The crystal structure of $\gamma-AlD_3$, J. Alloy. Compd. 441 (2007) 364-367.

[30] Y. Wang, J.-A. Yan, M.Y. Chou, Electronic and vibrational properties of $\gamma-AlH_3$, Phys. Rev. B 77 (2008) 014101-014108.

[31] P. Vajeeston, P. Ravindran, H. Fjellvag, Stability enhancement by particle size reduction in $AlH_3$, J. Alloy. Compd. 509S (2011) 662-666.

[32] G. Sandrock, J. Reilly, J. Graetz, W.-M. Zhou, J. Johnson, J. Wegrzyn, Accelerated thermal decomposition of $AlH_3$ for hydrogen-fueled vehicles, Appl. Phys. A 80(2005)687-690.

[33] A. Züttel, P. Wenger, S. Rentsch, P. Sudan, P. Mauron, C. Emmenegger, $LiBH_4$ a new hydrogen storage material, J. Power Sources 118 (2003) 1-7.

[34] J.G.O. Ojwang, R.A. van Santen, G.J. Kramer, A.C.T. van Duin, W.A. Goddard III, Parametrization of a reactive force field for aluminum hydride, J. Chem. Phys.131(2009)044501-144513.

[35] J. Graetz, J.J. Reilly, V.A. Yartys, J.P. Maehlen, B.M. Bulychev, V.E. Antonov, B.P. Tarasov, I.E. Gabis, Aluminum hydride as a hydrogen and energy storage material: past, present and future, J. Alloy. Compd. 509S (2011) 517-528.

[36] J. Graetz, J.J. Reilly, Thermodynamics of the $\alpha$, $\beta$ and $\gamma$ polymorphs of $AlH_3$, J. Alloy. Compd. 424 (2006) 262-265.

[37] S. Orimo, Y. Nakamori, T. Kato, C. Brown, C.M. Jensen, Intrinsic and mechanically modified thermal stabilities of $\alpha$-, $\beta$- and $\gamma$-aluminum trihydrides $AlH_3$, Appl. Phys. A - Mater. 83 (1) (2006) 5-8.

[38] J. Graetz, Metastable metal hydrides for hydrogen storage, ISRN Mater. Sci.,2012,2012,ID863025.

[39] V.A. Yartys, J.P. Maehlen, R.V. Denys, M. Fichtner, Ch. Frommenc, B.M. Bulychev, P. Pattison, H. Emerich, Y.E. Filinchuk, D. Chernyshov, Thermal decomposition of $AlH_3$ studied by in situ synchrotron X-ray diffraction and thermal desorption spectroscopy, J. Alloy. Compd. 446-447 (2007) 280-289.

[40] S.K. Konovalov, B.M. Bulychev, The P, T-state diagram and solid phase synthesis of aluminum hydride, Inorg. Chem. 34 (1995) 172-175.

[41] V. Drozd, S. Garimella, S. Saxena, J. Chen, T. Palasyuk, High-pressure Raman and X-ray diffraction study of $\beta$- and $\gamma$-polymorphs of aluminum hydride, J. Phys. Chem. C 116 (5) (2012) 3808-3816.

[42] S.V. Alapati, J.K. Johnson, D.S. Sholl, Using first principles calculations to identify new destabilized metal hydride reactions for reversible hydrogen storage, Phys. Chem. Chem. Phys. 9 (2007) 1438-1452.

[43] K. Batalovic, J. Radakovic, V. Koteski, M. Savic, Density functional theory guide to structure and thermodynamics of metal hydrides - Case study of (Ti, Zr, Hf) Ni intermetallic compounds, Int. J. Hydrogen Energy 40 (38) (2015) 13029-13038.

[44] K.D. Ćirić, V.J. Koteski, D.L.j. Stojić, J.S. Radakovic, V.N. Ivanovski, HfNi and its hydrides - First principles calculations, Int. J. Hydrogen Energy 35 (2010) 3572-3577.

[45] X. Ke, A. Kuwabara, I. Tanaka, Cubic and orthorhombic structures of aluminum hydride $AlH_3$ predicted by a first-principles study, Phys. Rev. B 71 (2005) 184107-184113.

[46] J. Graetz, J.J. Reilly, J.G. Kulleck, R.C. Bowman, Kinetics and thermodynamics of the aluminum hydride polymorphs, J. Alloy. Compd. 446-447 (2007) 271-275.

[47] G.C. Sinke, L.C. Walker, F.L. Oetting, D.R. Stull, Thermodynamic properties of aluminum hydride, J. Chem. Phys. 47 (8) (1967) 2759-2761.

[48] S. Sartori, S.M. Opalka, O.M. Løvvik, M.N. Guzik, X. Tang, B.C. Hauback, Experimental studies of $\alpha-AlD_3$ and $\alpha'-AlD_3$ versus first-principles modelling of the alane isomorphs, J. Mater. Chem. 18 (2008) 2361-2370.

[49] P. Vajeeston, P. Ravindran, H. Fjellvag, Phonon, IR, and Raman spectra, NMR parameters, and elastic constant calculations for $AlH_3$ polymorphs, J. Phys. Chem. A 115 (2011) 10708-10719.

[50] C.S. Wang, W.E. Pickett, Density-functional theory of excitation spectra of semiconductors: Application to Si, Phys. Rev. Lett. 51 (7) (1983) 597-600.

[51] D.J. Singh, Electronic structure calculations with the Tran-Blaha modified Becke-Johnson density functional, Phys. Rev. B 82 (2010) 205102-205111.

[52] C.J. Pickard, R.J. Needs, Metallization of aluminum hydride at high pressures: a first-principles study, Phys. Rev. B 76 (2007) 144114-144118.

[53] Y.-L. Lu, H. Zhao, First-principles studies on the structural stability of $\alpha-AlH_3$ under pressure, Model. Simul. Mater. Sci. Eng. 20 (2012) 085004-085010.

[54] M.J. van Setten, V.A. Popa, G.A. de Wijs, G. Brocks, Electronic structure and optical properties of lightweight metal hydrides, Phys. Rev. B 75 (2007) 035204-035216.

[55] M.C. Gibson, S.J. Clark, S. Brand, R.A. Abram, Screened exchange calculations of semiconductor band structures, Flagstaff, Arizona: AIP Conf. Proc. 772 (2005)1125-1126.

[56] L. Ismer, A. Janotti, C.G. Van de Walle, Stability and mobility of native point defects in $AlH_3$, J. Alloy. Compd. 509 (Suppl 2) (2011) S658-S661.

[57] K. Tatsumi, S. Muto, K. Ikeda, S.-I. Orimo, Chemical bonding of $AlH_3$ hydride by Al-$L_{2,3}$ electron energy-loss spectra and first-principles calculations, Materials5(4)(2012)566-574.

[58] J.A. Camargo-Martinez, R. Baquero, Performance of the modified Becke- Johnson potential for semiconductors, Phys. Rev. B 86 (2012) 195106-195113.

[59] K.P. O'Donnell, X. Chen, Temperature dependence of semiconductor band gaps, Appl. Phys. Lett. 58 (1991) 2924-2926.

[60] S.Zh. Karazhanov, U. Sheripov, A.G. Ulyashin, Classification of hydrides according to features of band structure, Philos. Mag. 89 (13) (2009) 1111-1120.

[61] R. Hoffmann, Solids and Surfaces: A Chemist's View on Bonding in Extended Structures, VCH Publishers Inc., New York, 1988 (ISBN 0-89573-709-4 US).

[62] X. Ke, G.J. Kramer, O.M. Løvvik, The influence of electronic structure on hydrogen absorption in palladium alloys, J. Phys. - Condens. Mat. 16 (2004) 6267-6277.

[63] F.C. Hill, G.V. Gibbs, M.B. Boisen Jr, Critical point properties of electron density distributions for oxide molecules containing first and second row cations, Phys. Chem. Min. 24 (1997) 582-596.

[64] R. Asokamani, P. Ravindran, Correlation between electronic structure, mechanical properties and phase stability in intermetallic compounds, Bull. Mater. Sci. 20 (4) (1997) 613-622.

[65] P. Sirsch, F.N. Che, J.T. Titah, G.S. McGrady, Hydride-hydride bonding interactions in the hydrogen storage materials $AlH_3$, $MgH_2$, and $NaAlH_4$, Chem. Eur. J. 18 (2012) 9476-9480.

[66] S.A. Kulkarni, A.K. Srivastava, Dihydrogen bonding in main group elements: a case study of complexes of $LiH$, $BH_3$, and $AlH_3$ with third-row hydrides, J. Phys. Chem. A 103 (1999) 2836-2842.