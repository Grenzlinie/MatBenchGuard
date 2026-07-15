# Insight into methanol synthesis from $CO_2$ hydrogenation on $Cu(1\ 1\ 1)$: Complex reaction network and the effects of $H_2O$

Ya-Fan Zhao $^{a,b}$, Yong Yang $^{b}$, Charles Mims $^{c}$, Charles H.F. Peden $^{b}$, Jun Li $^{a,b}$, Donghai Mei $^{b,*}$

$^{a}$ Department of Chemistry and Laboratory of Organic Optoelectronics and Molecular Engineering of the Ministry of Education, Tsinghua University, Beijing 100084, China
$^{b}$ Institute for Interfacial Catalysis, Pacific Northwest National Laboratory, Richland, WA 99352, USA
$^{c}$ Department of Chemical Engineering and Applied Chemistry, University of Toronto, Ontario, Canada M5S 3E5

---

## ARTICLE INFO

**Article history:**
Received 24 January 2011
Revised 7 April 2011
Accepted 19 April 2011
Available online 31 May 2011

**Keywords:**
Methanol synthesis
Carbon dioxide
$Cu(1\ 1\ 1)$
Density functional theory
Reaction mechanism

---

## ABSTRACT

Methanol synthesis from $CO_2$ hydrogenation on supported Cu catalysts is of considerable importance in the chemical and energy industries. Although extensive experimental and theoretical efforts have been carried out in the past decades, the most fundamental questions such as the reaction mechanisms and the key reaction intermediates are still in debate. In the present work, a comprehensive reaction network for $CO_2$ hydrogenation to methanol on $Cu(1\ 1\ 1)$ is studied using periodic density functional theory calculations. All of the elementary reaction steps in the reaction network are identified in an unbiased way with the dimer method. Our calculation results show that methanol synthesis from direct hydrogenation of formate on $Cu(1\ 1\ 1)$ is not feasible due to the high activation barriers for some of the elementary steps. Instead, we find that $CO_2$ hydrogenation to hydrocarboxyl (*trans*-COOH) is kinetically more favorable than formate in the presence of $H_2O$ via a unique hydrogen transfer mechanism. The *trans*-COOH is then converted into hydroxymethylidyne (COH) via dihydroxycarbene (COHOH) intermediates, followed by three consecutive hydrogenation steps to form hydroxymethylene (HCOH), hydroxymethyl ($H_2COH$), and methanol. This is consistent with recent experimental observations [1], which indicate that direct hydrogenation of formate will not produce methanol under dry hydrogen conditions. Thus, both experiment and computational modeling clearly demonstrate the important role of trace amounts of water in methanol synthesis from $CO_2$ hydrogenation on Cu catalysts. The proposed methanol synthesis route on $Cu(1\ 1\ 1)$ not only provides new insights into methanol synthesis chemistry, but also demonstrates again that spectroscopically observed surface species are often not critical reaction intermediates but rather spectator species.

© 2011 Elsevier Inc. All rights reserved.

---

## 1. Introduction

While methanol synthesis is one of the most important industrial catalytic reactions for its significance in energy production and conversion, carbon dioxide conversion and utilization are of great environmental importance. Methanol is commercially produced from syngas ($CO_2/CO/H_2/H_2O$) using $Cu/ZnO/Al_2O_3$ catalysts and has been widely used in methanol fuel cells, as hydrogen energy carriers, and as the feedstock for the production of many other chemicals such as acetic acid and methyl tert-butyl ether [2,3]. On the other hand, for efforts to mitigate global climate change through effective $CO_2$ capture and utilization, catalytic conversion of $CO_2$ into methanol has attracted considerable interest in the past decades [2,4,5]. Extensive experimental and theoretical investigations of $CO_2$ hydrogenation over oxide-supported Cu-based catalysts have been carried out [1,6–24]. The reaction mechanism and the key reaction intermediates, however, are still not clearly understood [2]. As such, fundamental understanding and theoretical insights into the chemical process of $CO_2$ hydrogenation on metallic Cu surfaces remain crucial to improve the synthesis of methanol using Cu-based catalysts.

$CO_2$ hydrogenation to methanol is an exothermic reaction and, thus, is favored by operation at low temperatures (473–523 K) [7,25]

$$\mathrm{CO_2 + 3H_2 \rightarrow CH_3OH + H_2O} \quad \Delta H_{298} = -49.5\ \mathrm{kJ/mol} \tag{1}$$

The reverse water-gas shift (RWGS) reaction may also occur as a side reaction

$$\mathrm{CO_2 + H_2 \rightarrow CO + H_2O} \quad \Delta H_{298} = +41.2\ \mathrm{kJ/mol} \tag{2}$$

It is generally accepted that metallic Cu is the active phase for methanol synthesis via $CO_2$ hydrogenation [1,8,17,20,24,26]. Previous experimental studies of $CO_2$ hydrogenation on the low-index single crystalline Cu surfaces suggested that methanol was formed by the consecutive hydrogenation of formate (HCOO)

---

* Corresponding author.
E-mail address: Donghai.Mei@pnl.gov (D. Mei).

0021-9517/$ - see front matter © 2011 Elsevier Inc. All rights reserved.
doi:10.1016/j.jcat.2011.04.012

[8,10,17,18,20,24,26,27]. This conclusion was primarily based on the experimental observation that HCOO was the most abundant surface intermediate during CO₂ hydrogenation. In the proposed formate reaction route, CO₂ reacts with surface atomic H forming HCOO via either an Eley-Rideal (ER) or Langmuir-Hinshelwood (LH) mechanism. HCOO is then hydrogenated to dioxymethylene (H₂COO), followed by further hydrogenation to methoxy (H₃CO), and the final product, methanol (H₃COH). The hydrogenation of HCOO to H₃CO was commonly assumed to be the rate-limiting step in methanol synthesis [6]. Chorkendorff and coworkers, however, found that the hydrogenation of HCOO on Cu(1 0 0) most likely leads to formaldehyde (H₂CO) and/or formic acid (HCOOH) instead of methanol [20]. Very recently, Yang et al. thoroughly studied HCOO hydrogenation on Cu catalysts using a simultaneous mass spectroscopy and infrared spectroscopy techniques [1]. They concluded that direct hydrogenation of bidentate HCOO on metallic Cu catalysts does not produce methanol. Interestingly, they found that significant amounts of methanol are formed if the Cu catalyst is pretreated by NO₂ or O₂. The authors suggested that surface oxygen or water-derived species may play a critical role in methanol synthesis on Cu, although the underlying mechanism was not defined [1].

Except for the formate reaction mechanism, methanol formation via hydrogenation of formyl (HCO) on Cu-based catalysts has also been proposed [19]. Liu and coworkers investigated these two reaction mechanisms for CO₂ hydrogenation to methanol on oxide-supported Cu clusters and on Cu(1 1 1) surfaces using density functional theory (DFT) calculations [23]. These authors found that the hydrogenation of HCOO to H₂COO, and the dissociation of H₂COO into H₂CO on Cu(1 1 1) are kinetically inhibited by high barriers of ~1.60 eV. Therefore, methanol synthesis from CO₂ hydrogenation on the perfect Cu(1 1 1) surface is hindered if the reaction follows the assumed formate route [23]. On the other hand, the formyl route is also unlikely due to the instability of HCO species on the Cu(1 1 1) surface. Liu and coworkers' results indicate that the formed HCO from CO hydrogenation will quickly decompose back to CO and atomic H on Cu(1 1 1) without any barrier.

Previously, Gao and Au studied methanol synthesis from CO₂ and H₂ over YBa₂Cu₃O₇ catalysts [12]. They suggested that the adsorbed CO₂ reacts via stepwise hydrogenation to hydrocarboxyl (COOH), dihydrocarbene (HCOH), HCOOH, and HCOHOH. The possible intermediates COOH, HCOH, HCOHOH, and H₂COHOH then transform to HCOO, H₂COO, HCO, and H₂CO groups, respectively. The crucial steps for methanol formation in this hydrocarboxyl-like mechanism might be the hydrogenation of HCO and H₂CO. Herein, we have performed comprehensive theoretical investigations on the hydrocarboxyl mechanism as a third alternative reaction route for CO₂ hydrogenation to methanol on Cu(1 1 1).

Understanding complex heterogeneous reactions on catalytic surfaces requires detailed knowledge of how reaction intermediates interact with the surface, and how the bond-breaking and bond-making processes occur at the active site(s). The entire surface reaction network (mechanisms) generally comprises a great number of elementary steps involving adsorption, reaction, desorption, and diffusion steps of reaction intermediates. Typically, because of the lack of information on the mechanism, all of the reaction intermediates and possible reaction steps in a reaction network are pre-assumed based on experimental observations and/or chemical intuition. On the basis of such assumed elementary steps, a locally optimized initial and final state of each elementary reaction path is then determined before identifying the transition state along this pre-determined pathway. Finally, a plausible and favorable reaction route may be obtained by comparing the calculated activation barrier for each elementary step. In such a modeling process, the reaction mechanisms are not "truly" explored but are, again, pre-assumed and then justified. On the other hand, different reaction paths might exist for each elementary step, but might have not been considered. In the present work, we combine periodic DFT calculations with the dimer method [28] to explore the entire reaction network of CO₂ hydrogenation on Cu(1 1 1), which is displayed in Fig. 1. The complete potential energy surface of CO₂ hydrogenation is thus mapped out in an unbiased way. We have demonstrated this computational methodology in our previous work on methanol decomposition on the Cu(1 1 0) [29] and Cu(1 0 0) [30] surfaces. In the present work, an unexpected reaction step is identified, which eventually inspires us to propose a feasible reaction route for methanol synthesis from CO₂ hydrogenation that is now more consistent with recent experimental observations [1].

## 2. Computational details

Periodic plane-wave DFT calculations combined with minimum mode-following saddle point searches were carried out to explore all possible reaction and diffusion pathways during methanol synthesis from CO₂ hydrogenation on the Cu(1 1 1) surface. Ion-electron interactions were represented by ultrasoft pseudopotentials within the framework of the projector-augmented wave (PAW) method, and the generalized gradient approximation (GGA) with the Perdew-Wang 91 functional was used in the calculations. The geometry of all stationary points were found with the conjugate-gradient algorithm and considered converged when the force on each ion dropped below 0.02 eV/Å. The Cu(1 1 1)-3 × 3 surface was modeled with a supercell containing a slab of three atomic layers. Cu(1 1 1)-4 × 4 surface was used for investigating the effect of H₂O. Periodic images of the slab were separated by a 12-Å vacuum gap. The bottom two layers were held frozen at equilibrium bulk positions; all other atoms were fully relaxed in our optimizations. Several surface sizes, numbers of atomic layers, and k-point sampling meshes were tested. A 2 × 2 × 1 Monkhorst-Pack k-point mesh and a (2 × 3) surface size were found to result in convergence of the relative energies to within 0.05 eV. All calculations were performed using the Vienna ab initio simulation package (VASP) [31,32]. The effects of the zero point energy correction (ZPEC) on the calculated energetics were also investigated in this work.

The binding energies of adsorbates on the Cu(1 1 1) surface, $E_b$, were calculated as:

$$
E_{\mathrm{b}}=E_{\text {adsorbate}+\mathrm{Cu}(111)}-\left(E_{\text {adsorbate }}+E_{\mathrm{Cu}(111)}\right) \tag{3}
$$

where $E_{\text{adsorbate+Cu(111)}}$ is the total energy of the adsorbate interacting with the Cu(1 1 1) slab; $E_{\text{Cu(111)}}$ is the energy of bare Cu(1 1 1) slab; and $E_{\text{adsorbate}}$ is the energy of the adsorbate in vacuum.

In the present study, various reaction and diffusion pathways during CO₂ hydrogenation to methanol on the Cu(1 1 1) surface are explored using the minimum mode following dimer method [28]. Without prior knowledge of the possible final states, only the initial states, i.e., the stable configurations of adsorbate(s) are required for each possible elementary reaction step. At first, the stable configuration of the reactant molecule(s) on the surface is determined with a standard DFT energy minimization. This configuration is then used as the initial state. The dimer searches are initiated by displacing the atoms of the reactant molecule(s) by a Gaussian distributed random distance of 0.05 Å. From the initial configuration, a dimer is created by making two equal and opposite small finite-difference displacements in the coordinates of the reactant molecule. A nearby saddle point is then found iteratively, by alternatively taking rotation and translation steps. In the rotation step, the lowest curvature direction is found by minimizing

![](./images/811655950476771329_1.jpg)

Fig. 1. Reaction mechanism network of methanol synthesis on Cu(1 1 1).

the energy of the dimer with respect to its orientation. In the trans- lation step, the force at the center of the dimer is inverted along the dimer orientation, so that it points up the potential along the low- est curvature mode and down in all other directions. Both rotation and translation steps are implemented with a conjugate gradient optimizer. The identified saddle point (transition state) is further confirmed by a vibrational frequency calculation, in which only one imaginary frequency is obtained at the saddle point. After each saddle point is found, the dimer images are relaxed to the neigh- boring local minima. In a successful search, one of the images will minimize to the initial state and the other will be in a new (and perhaps unexpected) final state. In this work, the dimer separation was set at 0.01 Å and the tolerance for convergence to the transi- tion state is such that the force on each atom is less than 0.01 eV/Å. The reaction energy of each path is calculated as the to- tal energy difference between the final state and the initial state. The forward and reverse activation barriers of each reaction (diffu- sion) path are defined as the total energy differences between the initial state and the saddle point, and between the final state and the saddle point, respectively.

## 3. Results

### 3.1. Reaction intermediates

All of the structural parameters and binding energies of reaction intermediates involved in various reaction routes are summarized in Table 1. The optimized adsorption structures of reaction inter- mediates in the most favorable configurations on Cu(1 1 1) are gi- ven in the supporting information (Fig. S1).

Both atomic H and O prefer to bind at 3-fold hollow sites on Cu(1 1 1), with calculated binding energies of –3.40 and –6.45 eV, respectively. Hydroxyl (OH) species also bind at the hol- low sites, with a binding energy of –3.62 eV. $H_2O$ adsorbs weakly at atop sites via a Cu–O bond of 2.28 Å, with a calculated binding energy of –0.19 eV, consistent with previous DFT calculations [33–34]. CO binds at hollow sites on Cu(1 1 1) through the C atom with a binding energy of –0.99 eV. $CO_2$ very weakly (–0.06 eV) physisorbs at hollow sites, also consistent with a previous study [33].

Formyl (HCO) prefers to bind at hollow sites with a binding en- ergy of –1.63 eV, which is in good agreement with the previous DFT results of –1.41 eV [35], and –1.32 eV [36]. In the most stable configuration as illustrated in Figure S1g, the Cu–C and Cu–O bond lengths of the adsorbed HCO are 2.10 and 2.07 Å, respectively. Hydroxymethylidyne (COH) also binds at hollow sites via a Cu–C bond, with an optimized Cu–C bond length of ~1.93 Å and a bind- ing energy of –3.19 eV.

Hydrocarboxyl (COOH) has been found to be the key reaction intermediate in the water-gas shift (WGS) reaction on Cu(1 1 1) [33]. COOH adsorbs at the Cu(1 1 1) surface in two distinguishable configurations, i.e., *trans*-COOH and *cis*-COOH, depending upon the direction of the hydroxyl group. The *trans*-COOH species prefers to adsorb at bridge sites (Fig. S1i), while the *cis*-COOH species binds at hollow sites (Fig. S1j). The calculated binding energies of *trans*- COOH and *cis*-COOH are very close, –1.89 and –2.08 eV, respec- tively. Gokhale et al. found both *trans*-COOH and *cis*-COOH adsorb at the atop site only through the C atom binding, with binding energies of –1.88 and –1.68 eV [33], respectively. Our calculated binding energies for *trans*-COOH and *cis*-COOH at atop sites are –1.92 and –1.67 eV, respectively, which are consistent with the

<table><thead><tr><th>Species</th><th>Site</th><th>$\boldsymbol{E_b}$ (eV)</th><th>$\boldsymbol{E_b^{ZPEC}}$ (eV)</th><th>Cu–Å (Å)</th><th colspan="3">Bond length (Å) and angle (∘) of adsorbed species</th></tr></thead><tbody><tr><td>H</td><td>3-Fold hollow</td><td>−3.58</td><td>−3.40</td><td>d(Cu–H)</td><td>1.75</td><td></td><td></td></tr><tr><td>O</td><td>3-Fold hollow</td><td>−6.55</td><td>−6.45</td><td>d(Cu–O)</td><td>1.89</td><td></td><td></td></tr><tr><td>OH</td><td>3-Fold hollow</td><td>−3.75</td><td>−3.62</td><td>d(Cu–O)</td><td>2.02</td><td>d(O–H)</td><td>0.99</td></tr><tr><td>H₂O</td><td>Atop</td><td>−0.20</td><td>−0.19</td><td>d(Cu–O)</td><td>2.28</td><td>d(O–H)</td><td>1.00</td><td>∠HOH</td><td>106.0</td></tr><tr><td>CO</td><td>3-Fold hollow</td><td>−1.06</td><td>−0.99</td><td>d(Cu–C)</td><td>2.01</td><td>d(C–O)</td><td>1.23</td></tr><tr><td>CO₂</td><td>3-Fold hollow</td><td>−0.05</td><td>−0.06</td><td>d(Cu–O)</td><td>1.98</td><td>d(C–O_up)</td><td>1.24</td><td>∠OCO</td><td>127.6</td></tr><tr><td rowspan="4">HCO</td><td rowspan="4">3-Fold hollow</td><td rowspan="4">−1.73</td><td rowspan="4">−1.63</td><td>d(Cu–C)</td><td>2.1</td><td>d(C–O_down)</td><td>1.36</td></tr><tr><td>d(Cu–O)</td><td>2.1</td><td>d(H–C)</td><td>1.11</td><td>∠HCO</td><td>114.3</td></tr><tr><td>d(Cu–C)</td><td>2.03</td><td>d(C–O)</td><td>1.31</td><td>∠CuOC</td><td>100.8</td></tr><tr><td></td><td></td><td></td><td></td><td>∠CuCCu</td><td>75.7</td></tr><tr><td>COH</td><td>3-Fold hollow</td><td>−3.36</td><td>−3.19</td><td>d(Cu–C)</td><td>1.92</td><td>d(H–O)</td><td>1.00</td><td>∠HOC</td><td>112.4</td></tr><tr><td>trans-COOH</td><td>Bridge</td><td>−1.96</td><td>−1.89</td><td>d(Cu–O)</td><td>2.09</td><td>d(H–O)</td><td>1.00</td><td>∠HOC</td><td>108.6</td></tr><tr><td></td><td></td><td></td><td></td><td>d(Cu–C)</td><td>1.96</td><td>d(O–C)</td><td>1.37</td><td>∠OCO</td><td>114.7</td></tr><tr><td rowspan="3">cis-COOH</td><td rowspan="3">3-Fold hollow</td><td rowspan="3">−2.14</td><td rowspan="3">−2.08</td><td></td><td></td><td>d(C–O)</td><td>1.29</td></tr><tr><td>d(Cu–O)</td><td>2.14</td><td>d(H–O)</td><td>1.00</td><td>∠HOC</td><td>108.0</td></tr><tr><td>d(Cu–C)</td><td>2.1</td><td>d(O–C)</td><td>1.38</td><td>∠O C O</td><td>117.0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>d(C–O)</td><td>1.30</td><td>∠CuOC</td><td>96.0</td></tr><tr><td>HCOO-mono</td><td>3-Fold hollow</td><td>−2.63</td><td>−2.52</td><td>d(Cu–O)</td><td>2.08</td><td>d(H–C)</td><td>1.11</td><td>∠HCO</td><td>123.5</td></tr><tr><td rowspan="3">HCOO-bi</td><td rowspan="3">Bridge</td><td rowspan="3">−3.00</td><td rowspan="3">−2.86</td><td></td><td>2.14</td><td>d(C–O_up)</td><td>1.25</td><td>∠OCO_up</td><td>123.7</td></tr><tr><td>d(Cu–O)</td><td>2.11</td><td>d(C–O_down)</td><td>1.37</td><td>∠HCO_down</td><td>112.8</td></tr><tr><td></td><td>2.02</td><td>d(H–C)</td><td>1.11</td><td>∠HCO</td><td>116.8</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>d(C–O)</td><td>2.30</td><td>∠OCO</td><td>126.6</td></tr><tr><td>t,t-C(OH)₂</td><td>Atop</td><td>−1.19</td><td>−1.15</td><td>d(Cu–C)</td><td>1.96</td><td>d(H–O)</td><td>1.01</td><td>∠HOC</td><td>107.3</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>d(O–C)</td><td>1.34</td><td>∠OCO</td><td>107.7</td></tr><tr><td>t,c-C(OH)₂</td><td>Atop</td><td>−1.05</td><td>−1.00</td><td>d(Cu–C)</td><td>1.95</td><td>d(O–H_down)</td><td>1.02</td><td>∠HOC</td><td>107.8</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>d(O–C)</td><td>1.35</td><td>∠OCO</td><td>109.6</td></tr><tr><td>c,c-C(OH)₂</td><td>Atop</td><td>−0.81</td><td>−0.75</td><td>d(Cu–C)</td><td>2.05</td><td>d(H–O)</td><td>1.00</td><td>∠HOC</td><td>110.9</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>d(O–C)</td><td>1.39</td><td>∠OCO</td><td>110.7</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>d(C–Cu)</td><td>2.05</td><td>∠CuCO</td><td>117.9</td></tr><tr><td rowspan="4">CHOH</td><td rowspan="4">Atop</td><td rowspan="4">−1.97</td><td rowspan="4">−1.87</td><td>d(Cu–C)</td><td>1.87</td><td>d(O–C)</td><td>1.37</td></tr><tr><td></td><td></td><td>d(H–O)</td><td>1.00</td><td>∠HOC</td><td>112.5</td></tr><tr><td></td><td></td><td>d(O–C)</td><td>1.37</td><td>∠OCH</td><td>111.3</td></tr><tr><td></td><td></td><td>d(C–H)</td><td>1.11</td><td>∠OCCu</td><td>125.8</td></tr><tr><td rowspan="3">H₂CO</td><td rowspan="3">Atop</td><td rowspan="3">−0.12</td><td rowspan="3">−0.10</td><td></td><td></td><td>d(C–Cu)</td><td>1.87</td><td>∠OCCu</td><td>120.3</td></tr><tr><td>d(Cu–O)</td><td>2.52</td><td>d(C–H)</td><td>1.11</td><td>∠HCH</td><td>118.6</td></tr><tr><td></td><td></td><td>d(O–C)</td><td>1.26</td><td>∠HCO</td><td>121.2</td></tr><tr><td rowspan="2">H₃CO</td><td rowspan="2">3-Fold hollow</td><td rowspan="2">−2.95</td><td rowspan="2">−2.79</td><td>d(Cu–O)</td><td>2.04</td><td>d(C–O)</td><td>1.46</td><td>∠CuCO</td><td>123.8</td></tr><tr><td></td><td></td><td>d(C–H)</td><td>1.10</td><td>∠COCu</td><td>129.3</td></tr><tr><td rowspan="3">CH₂OH</td><td rowspan="3">Atop</td><td rowspan="3">−1.34</td><td rowspan="3">−1.25</td><td></td><td></td><td></td><td></td><td>∠CuOCu</td><td>83.4</td></tr><tr><td>d(Cu–C)</td><td>2.07</td><td>d(C–H)</td><td>1.10</td><td>∠COH</td><td>109.1</td></tr><tr><td></td><td></td><td>d(C–O)</td><td>1.43</td><td>∠HCO</td><td>106.6</td></tr><tr><td rowspan="3">CH₃OH</td><td rowspan="3">Atop</td><td rowspan="3">−0.22</td><td rowspan="3">−0.19</td><td></td><td></td><td>d(O–H)</td><td>1.00</td><td>∠CuCO</td><td>106.8</td></tr><tr><td>d(Cu–O)</td><td>2.35</td><td>d(C–O)</td><td>1.46</td><td>∠COH</td><td>110.7</td></tr><tr><td></td><td></td><td>d(C–H)</td><td>1.10</td><td>∠CuOH</td><td>104.6</td></tr><tr><td rowspan="4">HCOOH</td><td rowspan="4">Atop</td><td rowspan="4">−0.24</td><td rowspan="4">−0.23</td><td></td><td></td><td>d(O–H)</td><td>1.00</td></tr><tr><td>d(Cu–O)</td><td>2.27</td><td>d(H–O)</td><td>1.02</td><td>∠HOC</td><td>110.1</td></tr><tr><td></td><td></td><td>d(O–C)</td><td>1.35</td><td>∠OCO</td><td>126.2</td></tr><tr><td></td><td></td><td>d(C–H)</td><td>1.10</td><td>∠HCOₐ</td><td>122.4</td></tr><tr><td rowspan="3">H₂COO</td><td rowspan="3">3-Fold hollow</td><td rowspan="3">−3.76</td><td rowspan="3">−3.67</td><td></td><td></td><td>d(C–Oₐ)</td><td>1.26</td><td>∠CuOₐC</td><td>131.0</td></tr><tr><td>d(Cu–O)</td><td>1.99</td><td>d(H–C)</td><td>1.11</td><td>∠HCH</td><td>111.3</td></tr><tr><td></td><td></td><td>d(C–O)</td><td>1.44</td><td>∠OCO</td><td>111.8</td></tr><tr><td rowspan="3">H₂COOH</td><td rowspan="3">3-Fold hollow</td><td rowspan="3">−2.61</td><td rowspan="3">−2.45</td><td rowspan="3">d(Cu–O)</td><td>2.03</td><td>d(H–O)</td><td>1.00</td><td>∠HOC</td><td>109.0</td></tr><tr><td>2.05</td><td>d(O–C)</td><td>1.42</td><td>∠OCO</td><td>111.7</td></tr><tr><td>2.06</td><td>d(C–H)</td><td>1.11</td><td>∠HCH</td><td>111.2</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>d(C–Oₐ)</td><td>1.45</td><td></td><td></td></tr></tbody></table>

previous results [33]. However, both of these atop geometries are not the most stable adsorption configurations.

Two configurations of adsorbed formate (HCOO), i.e., monodentate and bidentate, are identified. We find that the bidentate HCOO (bi-HCOO) structure is 0.44 eV more stable than the monodentate HCOO (mono-HCOO) (Fig. S1k) on clean Cu(1 1 1) surfaces. The optimized Cu–O bond lengths of bi-HCOO are the same (2.02 Å) and consistent with the experimental values of $1.92\pm0.04$ Å [37]. The calculated binding energy of the bi-HCOO at the bridge site is −2.86 eV, which agrees well with the DFT value of −2.92 eV [35], but slightly higher than the reported value of −2.77 eV obtained by Gokhale et al. [33]. The mono-HCOO species adsorbs at the hollow site on the Cu(1 1 1) surface via three Cu–O bonds.

Our calculated binding energy of the mono-HCOO is −2.52 eV, which is also slightly higher than a previously reported value of −2.32 eV [33].

Dihydroxycarbene (COHOH) had been proposed as one of the reaction intermediates in methanol synthesis from CO₂ hydrogenation over a YBa₂Cu₃O₇ catalyst [12]. COHOH can be directly generated by extrusion of CO₂ from $\alpha$-keto carboxylic acid [38]. COHOH has three possible isomeric structures (t,t-COHOH, t,c-COHOH and c,c-COHOH), as shown in Figure S1(m-o). Schreiner and Reisenauer have clearly identified t,t-COHOH and t,c-COHOH by infrared spectroscopy and high-level ab initio coupled cluster theory calculations [39]. In this work, we find that all three isomeric COHOH species bind at the atop site on Cu(1 1 1) through the C atom.

The Cu–C bond lengths for adsorbed t,t-COHOH, t,c-COHOH and c,c-COHOH are almost the same (1.96, 1.95 and 1.94 Å, see Table 1). Our calculation results indicate that the symmetric H-down t,t-COHOH structure (−1.15 eV) is more stable than the other two adsorption structures (−1.00 eV for the t,c-COHOH and −0.75 eV for the c,c-COHOH). We note that Ferrin and Mavrikakis also reported a COHOH binding energy of +0.44 eV (referenced to the total gas-phase energy of CO₂ and H₂) on Cu(1 1 1) [40]. Unfortunately, we cannot compare our results with theirs, since the authors did not report adsorption structures for COHOH on Cu(1 1 1).

Hydroxymethylene (HCOH) has been theoretically studied as a possible reaction intermediate in methanol decomposition on Pt(1 1 1) [41] and methanol electrooxidation on transition metal surfaces [40]. HCOH is formed by the hydrogenation of HCO or COH. HCOH adsorbs at the atop site on Cu(1 1 1) through the C atom (Fig. S1p), with a calculated Cu–C bond length of 1.87 Å. The binding energy of the adsorbed HCOH is −1.87 eV, which agrees well with the previous DFT result of −1.77 eV for HCOH adsorbed at bridge sites [40]. Previous theoretical calculations have indicated that the adsorption of H₂CO on Cu(1 1 1) is very weak [35,36,40,42,43]. Our calculated binding energy of H₂CO is −0.10 eV, which is consistent with those previous results. Further hydrogenation of HCOH or H₂CO leads to the formation of hydroxymethyl (H₂COH). On Cu(1 1 1), H₂COH binds at the atop site through the C atom with an adsorption energy of −1.25 eV. This is in good agreement with the previous DFT result of −1.11 eV [35]. The Cu–C bond length of the adsorbed H₂COH is 2.07 Å.

Besides HCOO, methoxy (H₃CO) is another experimentally observed surface species during methanol decomposition on Cu(1 1 1) [44,45] and methanol synthesis on oxide-supported Cu-based catalysts [6,9,46]. The geometrical structure and adsorption energy of H₃CO on Cu(1 1 1) has been studied by DFT calculations [35,42,43]. H₃CO prefers to adsorb at the hollow site through the O atom with a Cu–O bond length of 2.04 Å (Fig. S1r). The binding energy of H₃CO is −2.79 eV, which is higher than the most recent DFT result of −2.45 eV [35].

Formic acid (HCOOH) binds at the atop site on Cu(1 1 1) with a single Cu–O bond. As shown in Figure S1u, in its most stable configuration, the hydroxyl H atom in the adsorbed HCOOH points downwardly, towards the Cu surface, while an adsorption structure with the hydroxyl H atom pointing upward (not shown) is slightly weaker. The binding energy of the most stable adsorbed HCOOH is −0.23 eV, in good agreement with a prior result of −0.24 eV [35].

H₂COO was identified as a reaction intermediate during H₂CO oxidation on Cu(1 1 0) using X-ray photoelectron spectroscopy (XPS) and temperature-programmed desorption (TPD) [47]. However, H₂COO species could not be confirmed in high-resolution electron energy loss spectroscopy (HREELS) measurements [48]. Even though experimental evidence for the existence of H₂COO is weak and H₂COO was only proposed in the studies of Cu(1 1 0) surfaces, H₂COO, as the product of direct HCOO hydrogenation, has been widely assumed to be an intermediate in methanol synthesis on Cu-based catalysts via the formate reaction mechanism [17,18,23,49]. Consistent with the previous DFT studies of H₂COO adsorption on Cu(1 1 1) [23,35,40], we find that H₂COO prefers to bind at the Cu(1 1 1) surface with both O atoms of H₂COO bonded at two bridge sites shown in Fig. S1v. The optimized four Cu–O bond lengths are about 2.01 Å. Our calculated binding energy of H₂COO in this configuration is −3.67 eV.

Like H₂COO, hydroxymethoxy (H₂COOH) has been proposed as a possible hydrogenated intermediate of H₂COO before its conversion to H₂CO in the formate reaction mechanism [23]. H₂COOH has also been investigated in the studies of methanol steam reforming and electrooxidation on Cu(1 1 1) using DFT calculations [35,40]. As shown in Fig. S1w, H₂COOH adsorbs at the hollow site via one O atom bridge-bonded with two Cu atoms, and another hydroxyl O atom bound at a third Cu atom. Our calculated binding energy of H₂COOH in this configuration is −2.45 eV, which is larger than the previously reported values of −2.19 eV [35] and −1.90 eV [40], although similar adsorption structures of H₂COOH were identified in all three studies.

As the final desired product of CO₂ hydrogenation, methanol (H₃COH) interacts with Cu(1 1 1) very weakly via the Cu–O bond. Our calculated binding energy of H₃COH is −0.19 eV, in good agreement with previous DFT calculations [23,35,40].

### 3.2. Elementary reaction steps in various methanol synthesis routes

To elucidate feasible reaction mechanisms for CO₂ hydrogenation to methanol, all of the elementary steps in various reaction routes shown in Fig. 1 are investigated using the dimer method [28]. The calculated reaction energies, activation barriers, free energies, and rate constants at 500 K for the elementary steps are summarized in Table 2. The transition states for all elementary steps are given in the supporting information (Figs. S2–S4).

#### 3.2.1. Hydrogen adsorption: $H_2(g) \rightarrow H+H$

Hydrogen dissociatively adsorbs on the Cu(1 1 1) surface, forming two atomic H sitting at a pair of the neighboring fcc and hcp sites. Our result shows that hydrogen adsorption on Cu(1 1 1) is exothermic with a reaction energy of −0.32 eV. The calculated activation barrier is 0.55 eV, which is in excellent agreement with the experimentally measured barrier of 0.55 eV [50] and DFT result of 0.54 eV [33].

### 3.2.2. Formate reaction route
#### 3.2.2.1. HCOO formation: $CO_2(g)+H \rightarrow mono-HCOO \rightarrow bi-HCOO$
Inasmuch as the adsorption of CO₂ on Cu(1 1 1) is very weak, the hydrogenation of CO₂ is most likely activated by gas-phase CO₂ directly reacting with atomic surface H via an ER mechanism. The formed mono-HCOO binds at the atop site on Cu(1 1 1) with the single Cu–O bond. At the transition state (Fig. S2a), the forming C–H bond length is 1.61 Å. The calculated activation barrier for $CO_2(g)+H \rightarrow mono-HCOO$ is 0.62 eV and the reaction energy is −0.10 eV, indicating this step is energetically favorable. Our calculation is in good agreement with the experimentally measured HCOO formation barriers of $0.57 \pm 0.06$ eV by XPS [51] and $0.59 \pm 0.05$ eV by infrared reflection absorption spectroscopy (IRAS) [52]. Consistent with the previous findings [33], the formed mono-HCOO surface species is not stable and quickly converts to the more stable bi-HCOO structure on Cu(1 1 1). This configuration transformation is exothermic (−0.31 eV) and nearly spontaneous (0.02 eV).

#### 3.2.2.2. HCOO decomposition: $bi-HCOO \rightarrow HCO+O$ and $mono-HCOO \rightarrow CO(g)+OH$
By breaking one of the C–O bonds of bi-HCOO, the bi-HCOO can be deoxygenated into HCO and an atomic O atom. At the transition state (Fig. S2c), one of the O atoms of bi-HCOO moves from the atop site to the hollow site and breaks the C–O bond. At the same time, the C atom of bi-HCOO replaces the moving O atom and binds at the original atop Cu site. The forming HCO species binds at a bridge site on Cu(1 1 1) with Cu–C and Cu–O bond lengths of 2.01 and 2.08 Å, respectively. At the final state, HCO moves from the bridge site to the more stable hollow site. The bi-HCOO → HCO + O path is found to be highly endothermic with a reaction energy of +1.55 eV. The calculated activation barrier is 1.73 eV, indicating the direct deoxygenation of bi-HCOO into HCO via the C–O bond scission is unlikely. A possible concurrent HCOO decomposition pathway, via mono-HCOO decomposi-

<table>
<caption>Table 2<br>DFT Calculated activation barriers ($E_a$), reaction energies ($\Delta H$), Gibbs free energies ($\Delta G$), and rate constants (@ 500 K) ($k_{forward}$ and $k_{reverse}$) for elementary reaction steps.</caption>
<thead>
<tr>
<th>Elementary step</th>
<th>$E_a$ (eV)</th>
<th>$\Delta E$ (eV)</th>
<th>$E_a^{ZPEC}$ (eV)</th>
<th>$\Delta E^{ZPEC}$ (eV)</th>
<th>$\Delta G$ (eV)</th>
<th>$k_{forward}$ ($s^{-1}$)</th>
<th>$k_{reverse}$ ($s^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$H_2(g) \leftrightarrow H + H$</td>
<td>0.60</td>
<td>−0.39</td>
<td>0.55</td>
<td>−0.32</td>
<td>−0.28</td>
<td>2.34E+06</td>
<td>2.02E+05</td>
</tr>
<tr>
<td>$CO_2(g) + H \leftrightarrow mono-HCOO$</td>
<td>0.67</td>
<td>−0.21</td>
<td>0.62</td>
<td>−0.10</td>
<td>−0.06</td>
<td>2.73E+06</td>
<td>1.62E+06</td>
</tr>
<tr>
<td>$mono-HCOO \leftrightarrow bi-HCOO$</td>
<td>0.03</td>
<td>−0.33</td>
<td>0.02</td>
<td>−0.31</td>
<td>−0.31</td>
<td>6.31E+12</td>
<td>1.06E+10</td>
</tr>
<tr>
<td>$bi-HCOO \leftrightarrow HCO + O$</td>
<td>1.80</td>
<td>1.63</td>
<td>1.73</td>
<td>1.55</td>
<td>1.55</td>
<td>1.90E−05</td>
<td>1.33E+11</td>
</tr>
<tr>
<td>$mono-HCOO \leftrightarrow CO(g) + OH$</td>
<td>2.36</td>
<td>0.91</td>
<td>2.21</td>
<td>0.84</td>
<td>0.80</td>
<td>1.73E−09</td>
<td>7.62E−02</td>
</tr>
<tr>
<td>$bi-HCOO + H \leftrightarrow H_2COO$</td>
<td>1.24</td>
<td>0.29</td>
<td>1.20</td>
<td>0.43</td>
<td>0.43</td>
<td>1.86E+01</td>
<td>1.65E+06</td>
</tr>
<tr>
<td>$bi-HCOO + H \leftrightarrow HCOOH$</td>
<td>0.81</td>
<td>0.20</td>
<td>0.70</td>
<td>0.29</td>
<td>0.29</td>
<td>9.47E+06</td>
<td>5.96E+08</td>
</tr>
<tr>
<td>$H_2COO + H \leftrightarrow H_2COOH$</td>
<td>0.82</td>
<td>−0.34</td>
<td>0.71</td>
<td>−0.23</td>
<td>−0.23</td>
<td>6.01E+06</td>
<td>2.51E+03</td>
</tr>
<tr>
<td>$HCOOH + H \leftrightarrow H_2COOH$</td>
<td>0.90</td>
<td>−0.18</td>
<td>0.86</td>
<td>−0.02</td>
<td>−0.02</td>
<td>3.81E+04</td>
<td>5.40E+04</td>
</tr>
<tr>
<td>$HCO + H \leftrightarrow H_2CO$</td>
<td>0.46</td>
<td>−0.45</td>
<td>0.43</td>
<td>−0.32</td>
<td>−0.32</td>
<td>1.32E+09</td>
<td>1.01E+06</td>
</tr>
<tr>
<td>$HCO + H \leftrightarrow H_2CO(g)$</td>
<td>0.63</td>
<td>−0.22</td>
<td>0.57</td>
<td>−0.16</td>
<td>−0.20</td>
<td>2.03E+08</td>
<td>2.11E+04</td>
</tr>
<tr>
<td>$H_2COO \leftrightarrow H_2CO(g) + O$</td>
<td>1.03</td>
<td>0.96</td>
<td>0.92</td>
<td>0.84</td>
<td>0.84</td>
<td>1.28E+05</td>
<td>5.07E+11</td>
</tr>
<tr>
<td>$H_2COOH \leftrightarrow H_2CO + OH$</td>
<td>1.36</td>
<td>0.52</td>
<td>1.17</td>
<td>0.41</td>
<td>0.41</td>
<td>1.49E+03</td>
<td>2.93E+06</td>
</tr>
<tr>
<td>$HCOH \leftrightarrow H_2CO$</td>
<td>1.75</td>
<td>−0.43</td>
<td>1.56</td>
<td>−0.45</td>
<td>−0.45</td>
<td>5.25E−03</td>
<td>1.89E−07</td>
</tr>
<tr>
<td>$H_2CO + H \leftrightarrow CH_3O$</td>
<td>0.13</td>
<td>−1.41</td>
<td>0.14</td>
<td>−1.20</td>
<td>−1.20</td>
<td>2.03E+10</td>
<td>1.03E+00</td>
</tr>
<tr>
<td>$H_3CO + H \leftrightarrow H_3COH(g)$</td>
<td>1.01</td>
<td>0.05</td>
<td>0.90</td>
<td>0.14</td>
<td>0.10</td>
<td>1.68E+05</td>
<td>1.48E+05</td>
</tr>
<tr>
<td>$CO_2(g) + H \leftrightarrow trans-COOH$</td>
<td>1.27</td>
<td>0.18</td>
<td>1.16</td>
<td>0.32</td>
<td>0.36</td>
<td>6.69E+00</td>
<td>2.33E+05</td>
</tr>
<tr>
<td>$CO_2 + H \leftrightarrow trans-COOH$</td>
<td>0.91</td>
<td>−0.24</td>
<td>0.81</td>
<td>−0.10</td>
<td>−0.10</td>
<td>4.39E+05</td>
<td>2.88E+04</td>
</tr>
<tr>
<td>$trans-COOH \leftrightarrow cis-COOH$</td>
<td>0.53</td>
<td>0.03</td>
<td>0.47</td>
<td>0.05</td>
<td>0.05</td>
<td>1.11E+09</td>
<td>7.59E+09</td>
</tr>
<tr>
<td>$trans-COOH + H \leftrightarrow t,t-COHOH$</td>
<td>0.43</td>
<td>−0.11</td>
<td>0.37</td>
<td>0.03</td>
<td>0.03</td>
<td>6.20E+09</td>
<td>5.29E+09</td>
</tr>
<tr>
<td>$t,t-COHOH \leftrightarrow t,c-COHOH$</td>
<td>0.64</td>
<td>0.11</td>
<td>0.58</td>
<td>0.10</td>
<td>0.10</td>
<td>6.76E+07</td>
<td>6.85E+08</td>
</tr>
<tr>
<td>$t,c-COHOH \leftrightarrow c,c-COHOH$</td>
<td>0.73</td>
<td>0.53</td>
<td>0.68</td>
<td>0.50</td>
<td>0.50</td>
<td>3.33E+06</td>
<td>2.79E+11</td>
</tr>
<tr>
<td>$trans-COOH \leftrightarrow COH + O$</td>
<td>2.13</td>
<td>0.28</td>
<td>2.14</td>
<td>0.36</td>
<td>0.36</td>
<td>1.75E−09</td>
<td>1.03E−05</td>
</tr>
<tr>
<td>$c,c-COHOH \leftrightarrow COH + OH$</td>
<td>0.59</td>
<td>−0.19</td>
<td>0.55</td>
<td>−0.19</td>
<td>−0.19</td>
<td>3.02E+07</td>
<td>2.01E+06</td>
</tr>
<tr>
<td>$HCO \leftrightarrow CO + H$</td>
<td>0.26</td>
<td>−0.66</td>
<td>0.15</td>
<td>−0.73</td>
<td>−0.73</td>
<td>7.71E+11</td>
<td>4.96E+04</td>
</tr>
<tr>
<td>$COH \leftrightarrow CO + H$</td>
<td>1.02</td>
<td>−0.93</td>
<td>0.83</td>
<td>−1.04</td>
<td>−1.04</td>
<td>1.05E+05</td>
<td>4.36E−06</td>
</tr>
<tr>
<td>$cis-COOH \leftrightarrow CO + OH$</td>
<td>0.18</td>
<td>−0.56</td>
<td>0.12</td>
<td>−0.61</td>
<td>−0.61</td>
<td>1.19E+12</td>
<td>7.58E+05</td>
</tr>
<tr>
<td>$HCO + H \leftrightarrow cis-HCOH$</td>
<td>1.15</td>
<td>0.23</td>
<td>1.06</td>
<td>0.35</td>
<td>0.35</td>
<td>5.75E+02</td>
<td>1.43E+06</td>
</tr>
<tr>
<td>$COH + H \leftrightarrow cis-HCOH$</td>
<td>0.48</td>
<td>−0.14</td>
<td>0.44</td>
<td>−0.05</td>
<td>−0.05</td>
<td>1.08E+09</td>
<td>1.22E+08</td>
</tr>
<tr>
<td>$cis-HCOH + H \leftrightarrow H_2COH$</td>
<td>0.14</td>
<td>−0.84</td>
<td>0.10</td>
<td>−0.75</td>
<td>−0.75</td>
<td>3.31E+12</td>
<td>1.75E+04</td>
</tr>
<tr>
<td>$trans-HCOH + H \leftrightarrow H_2COH$</td>
<td>0.12</td>
<td>−0.77</td>
<td>0.08</td>
<td>−0.66</td>
<td>−0.66</td>
<td>4.24E+12</td>
<td>2.91E+05</td>
</tr>
<tr>
<td>$H_2CO(g)+H \leftrightarrow H_2COH$</td>
<td>0.70</td>
<td>−0.13</td>
<td>0.66</td>
<td>0.05</td>
<td>0.10</td>
<td>3.69E+05</td>
<td>1.50E+07</td>
</tr>
<tr>
<td>$H_2COH + H \leftrightarrow H_3COH(g)$</td>
<td>0.66</td>
<td>−0.90</td>
<td>0.62</td>
<td>−0.78</td>
<td>−0.83</td>
<td>3.26E+07</td>
<td>3.27E−03</td>
</tr>
<tr>
<td>$t,c-COHOH \leftrightarrow COH + OH$</td>
<td>1.09</td>
<td>0.31</td>
<td>1.01</td>
<td>0.27</td>
<td>0.27</td>
<td>6.99E+02</td>
<td>1.05E+06</td>
</tr>
<tr>
<td>$O + H \leftrightarrow OH$</td>
<td>0.87</td>
<td>−0.69</td>
<td>0.77</td>
<td>−0.60</td>
<td>−0.60</td>
<td>1.68E+06</td>
<td>5.95E−01</td>
</tr>
<tr>
<td>$OH + H \leftrightarrow H_2O$</td>
<td>1.12</td>
<td>0.17</td>
<td>0.99</td>
<td>0.23</td>
<td>0.23</td>
<td>2.71E+04</td>
<td>1.24E+04</td>
</tr>
<tr>
<td>$OH + H \leftrightarrow H_2O$</td>
<td>1.39</td>
<td>0.04</td>
<td>1.28</td>
<td>0.09</td>
<td>0.09</td>
<td>5.90E+01</td>
<td>1.98E+12</td>
</tr>
<tr>
<td>$OH + OH \leftrightarrow H_2O + O$</td>
<td>0.35</td>
<td>0.13</td>
<td>0.27</td>
<td>0.17</td>
<td>0.17</td>
<td>3.10E+10</td>
<td>3.43E+07</td>
</tr>
</tbody>
</table>

tion into CO and OH (Fig. S2d), was identified in our previous work [53]. However, also in this case, the process was found to be kinetically unlikely due to an extremely high barrier (2.21 eV).

3.2.2.3. HCOO hydrogenation: $bi-HCOO + H \rightarrow H_2COO$ and $bi-HCOO + H \rightarrow HCOOH$. Hydrogenation of the bi-HCOO can lead to two possible products: $H_2COO$ and $HCOOH$. An $H_2COO$ intermediate has been experimentally observed in the transformation of $H_2CO$ to HCOO on Cu(1 1 0) [47], and in methanol decomposition on $Cu/SiO_2$ and $Cu/ZnO/Al_2O_3$ catalysts using TPRS and NMR techniques [54,55]. Burch et al. proposed that the hydrogenation of HCOO to $H_2COO$ was the rate-determining step in methanol synthesis on Cu surfaces [56]. However, Sexton et al. argued that the existence of $H_2COO$ on the Cu(1 1 0) surface during the oxidation of methanol and $H_2CO$ is questionable [48]. Our calculations show that HCOO hydrogenation to $H_2COO$ is endothermic, with a reaction energy of +0.43 eV and activation barrier of 1.20 eV. As shown in Fig. S2e, the distance for the forming C–H bond at the transition state is 1.56 Å. A higher activation barrier of 1.60 eV and endothermicity of +0.70 eV for HCOO hydrogenation to $H_2COO$ were also recently reported by Liu and coworkers [23] using the synchronous transit method within Dmol³ software.

The bi-HCOO can also react with surface atomic H to form HCOOH. The calculated activation barrier for this hydrogenation pathway is 0.70 eV, and the reaction energy is +0.29 eV. Our result is close to a recently reported DFT result of 0.99 eV for the barrier and +0.44 eV for the reaction energy [35]. Compared with the $H_2COO$ formation, HCOO hydrogenation to HCOOH is energetically and kinetically more favorable. Since HCOOH adsorbs weakly on Cu(1 1 1), the formed HCOOH most likely desorbs from the surface or dissociates back to HCOO with a low barrier of 0.31 eV.

3.2.2.4. $H_2COOH$ formation: $H_2COO + H \rightarrow H_2COOH$ and $HCOOH + H \rightarrow H_2COOH$. Once $H_2COO$ or HCOOH are produced, they can be further hydrogenated to $H_2COOH$. The $H_2COO + H \rightarrow H_2COOH$ reaction step is exothermic (−0.23 eV). Our calculated activation barrier for this O–H bond-making step is 0.71 eV. The second possible pathway for $H_2COOH$ formation is via HCOOH hydrogenation. We find that this second pathway is only slightly exothermic (−0.02 eV) with a barrier of 0.86 eV. Gu and Li also studied these two hydrogenation pathways using DFT calculations [35] and found a slightly higher barrier of 0.95 eV for $H_2COO + H \rightarrow H_2COOH$. At the transition state, the forming O–H bond distance is 1.63 Å, which is close to another reported value of 1.60 Å [35].

3.2.2.5. $H_2CO$ formation: $HCO + H \rightarrow H_2CO$, $H_2COO \rightarrow H_2CO(g) + O$ and $H_2COOH \rightarrow H_2CO + OH$. $H_2CO$ can be formed on the Cu(1 1 1) surface by three different pathways. First, $H_2CO$ can be generated from HCO hydrogenation. The adsorbed HCO at the hollow site reacts with neighboring atomic H forming $H_2CO$. Due to the relatively weak adsorption of $H_2CO$ on Cu(1 1 1), two pathways for $HCO + H \rightarrow H_2CO$ are identified in our simulations, leading to either a weakly bonded $H_2CO$ at hollow sites or directly to gas-phase $H_2CO$. The second pathway is different from the first one because $H_2CO$ can be generated from

different transition states are found. For $HCO + H \to H_2CO$, only the atomic H moves toward the adsorbed HCO that is binding at the original hollow site. The distance for the forming C–H bond is 1.72 Å at the transition state (Fig. S2i). The calculated activation barrier for this first pathway is 0.43 eV with a reaction energy of $-0.32$ eV. For the concerted $HCO + H \to H_2CO(g)$ elementary step, besides the neighboring atomic H moving to the bridge site, the adsorbed HCO also shifts from the original hollow site to the atop site by breaking a Cu–O bond (Fig. S2j). The distance for the forming C–H bond is 1.62 Å at the transition state. Although the calculated reaction energies ($-0.32$ and $-0.16$ eV) indicate both reaction pathways are exothermic, the first reaction pathway is kinetically more favorable with a lower (by 0.14 eV) barrier. We note that the reverse barriers along both reaction pathways, i.e., $H_2CO$ dissociation into $HCO + H$ either from the gas phase or the surface reaction are very close (0.92 and 0.85 eV), further confirming the weak interaction of $H_2CO$ on $Cu(1\ 1\ 1)$.

The second pathway for $H_2CO$ formation is via the C–O scission of $H_2COO$. The formed $H_2CO$ is released into the gas phase in the final state. At the transition state (Fig. S2k), the broken C–O bond distance is 2.17 Å. This second $H_2CO$ formation path is found to be highly endothermic ($+0.84$ eV). The calculated activation barrier of 0.92 eV is equal to the reaction energy, indicating that the reverse process of gas-phase $H_2CO$ reacting with surface O atoms to form $H_2COO$ is spontaneous.

$H_2COOH$ might also decompose into $H_2CO$ and $OH$ on $Cu(1\ 1\ 1)$. To initiate this reaction, bridge-bonded $H_2COOH$ first tilts toward the surface. At the transition state (Fig. S2l), the C–O bond is already broken (3.36 Å), forming $H_2CO$ and $OH$ with both species binding at atop sites through their O atoms (Fig. S2k). Our calculations show that the $H_2COOH \to H_2CO + OH$ path is endothermic ($+0.41$ eV) with a high barrier of 1.18 eV. A similar pathway, $H_2COO + H \to H_2CO + OH$, was investigated by Liu and coworkers [23]. They found that the activation barrier was even higher (1.60 eV), although the reaction was found to be slightly exothermic ($-0.14$ eV).

Finally, an intermolecular H transfer process that converts $HCOH$ to $H_2CO$ is found in the present work. The reaction energy for the intramolecular H transfer is $-0.45$ eV. However, the activation barrier is extremely high (1.56 eV), indicating that the intramolecular H transfer ($HCOH \to H_2CO$) process on $Cu(1\ 1\ 1)$ is highly unlikely.

#### 3.2.2.6. Formation of methoxy: $H_2CO + H \to H_3CO$.
The $H_2CO + H \to H_3CO$ step on $Cu(1\ 1\ 1)$ has been investigated using DFT calculations extensively. We note, however, that somewhat different reaction barriers and reaction energies were reported [23,35]. For example, Liu and coworkers found that this hydrogenation step was exothermic ($-1.16$ eV) with an activation barrier of 0.69 eV [23], while Greeley and Mavrikakis reported a reaction energy of $-0.97$ eV and an activation barrier of 0.45 eV [43]. In previous DFT study by Gu and Li, the reaction barrier and energy were found to be 0.35 and $-0.92$ eV, respectively [35]. In this work, we find that the hydrogenation of $H_2CO$ to $H_3CO$ is highly exothermic ($-1.20$ eV) with a low barrier of 0.14 eV. At the transition state, the forming C–H bond distance is 1.76 Å (Fig. S2n). Again, these kinetic and energetic differences are most likely attributed to the weak $H_2CO$ binding in the initial states of the reaction pathway that result in different co-adsorbed $H_2CO + H$ configurations in these initial states.

#### 3.2.2.7. Formation of methanol: $H_3CO + H \to H_3COH$.
The final step in the formate route is the hydrogenation of $H_3CO$ to $H_3COH$. At the transition state (Fig. S2o), the distance for the forming O–H bond in $H_3COH$ is 1.45 Å. Our calculation shows that this final hydrogenation step is almost thermoneutral ($+0.14$ eV). The calculated activation barrier is 0.90 eV, which is comparable with previously reported values of 1.15 eV [23] and 1.16 eV [35].

### 3.2.3. Hydrocarboxyl (COOH) reaction route

#### 3.2.3.1. COOH Formation: $CO_2(g) + H \to trans$-COOH and $CO_2 + H \to trans$-COOH.
The formation of COOH from $CO_2$ hydrogenation is via either an ER or LH mechanism. The formed COOH, which is in the trans-configuration, adsorbs at a bridge site with both Cu–C and the Cu–O bonds. Our calculation results show that the ER path ($CO_2(g) + H \to trans$-COOH) is endothermic ($+0.32$ eV), while the LH path ($CO_2 + H \to trans$-COOH) is exothermic ($-0.10$ eV). The activation barrier for the LH path is 0.35 eV lower than the value of 1.16 eV obtained for the ER mechanism, although the distances of the forming O–H bond at the transition states for both pathways are nearly the same (1.52 and 1.49 Å). The differences can be attributed to the energy needed for the activation of gas-phase $CO_2$. Our calculated barrier for the ER path is slightly lower than the previous result of 1.38 eV [33].

#### 3.2.3.2. Configurational transformation of COOH: $trans$-COOH $\to$ cis-COOH.
Adsorbed COOH can exist in two isomeric configurations, trans- and cis-COOH, as described earlier in Section 3.1. The hydroxyl H atom in the trans-COOH points toward the surface, while in cis-COOH, it points upward away from the surface. We find that the stabilities of both configurations on $Cu(1\ 1\ 1)$ are nearly the same (0.05 eV). Consistent with the previous DFT calculations [33], the calculated barrier for the trans-COOH to cis-COOH interconversion (Fig. S3c) is 0.47 eV.

#### 3.2.3.3. Dihydrocarbene formation and configurational transformation: $trans$-COOH $+ H \to t,t$-COHOH $\to t,c$-COHOH $\to c,c$-COHOH.
Hydrogenation of the trans-COOH forms the t,t-COHOH isomer of adsorbed dihydrocarbene. The $trans$-COOH $+ H \to t,t$-COHOH pathway is slightly exothermic ($-0.10$ eV) with an activation barrier of 0.43 eV. At the transition state (Fig. S3d), the forming O–H bond length is 1.45 Å. Of all three isomeric COHOH species, the t,t-COHOH with both hydroxyl H atoms pointing toward the surface is found to be most stable. The interconversion pathways of the three isomers of adsorbed COHOH are examined using the dimer method. The calculated barriers of $t,t$-COHOH $\to t,c$-COHOH and $t,c$-COHOH $\to c,c$-COHOH are 0.58 and 0.68 eV, respectively.

#### 3.2.3.4. COH formation: $c,c$-COHOH $\to COH + OH$, $t,c$-COHOH $\to COH + OH$.
COH is feasibly formed by the decomposition of c, c-COHOH. The additional H atom on the O (second OH group in the c,c-COHOH) significantly weakens the C–O bond in trans-COOH. The calculated barrier for the $c,c$-COHOH $\to COH + OH$ pathway is only 0.55 eV. At the transition state (Fig. S3h), the distance for the breaking C–O bond in the c,c-COHOH is elongated to 1.92 Å from the original C–O bond length of 1.39 Å. Furthermore, we find that this reaction pathway is slightly exothermic ($-0.14$ eV). We also find another reaction path for COH formation through decomposition of the t,c-COHOH (Fig. S3r). Before the t,c-COHOH is transformed to the c,c-COHOH, it can dissociated to COH and OH with a barrier of 1.01 eV and the reaction is endothermic by 0.27 eV.

#### 3.2.3.5. CO formation: $COH \to CO + H$, $HCO \to CO + H$, $cis$-COOH $\to CO + OH$.
Dehydrogenations of HCO and COH produce CO and atomic H on $Cu(1\ 1\ 1)$. Consistent with previous results [57], HCO dissociation into $CO + H$ is energetically favorable ($-0.73$ eV) with a barrier of 0.15 eV. The adsorbed HCO at the hollow site tilts toward the surface. At the transition state (Fig. S3i), the C–H bond elongates to 1.29 Å and the leaving H atom is already bonded with the surface Cu atom. In the final state, the formed CO and H co-adsorb at neighboring hollow sites. Compared with the facile C–H bond breaking in HCO, the O–H bond scission of COH leading to

CO and H is relatively more difficult. Although the O-H bond scission path is highly exothermic (-1.04 eV), the activation barrier is 0.83 eV. At the transition state (Fig. S3j), the breaking O-H bond distance is 1.37 Å. The third CO formation pathway is through the decomposition of cis-COOH. The cis-COOH adsorbed at the atop site on Cu(1 1 1) can readily decompose into CO sitting at an atop site and OH at a neighboring hollow site. The calculated barrier is only 0.12 eV, which is slightly lower than the barrier of 0.35 eV obtained by Gokhale et al. [33].

3.2.3.6. HCOH formation: $COH + H \rightarrow HCOH$ and $HCO + H \rightarrow HCOH$. Further hydrogenations of COH and HCO species lead to the formation of HCOH via C-H and O-H bond-making processes, respectively. Our calculation results show that the $COH + H \rightarrow H-COH$ path is exothermic (-0.05 eV), while the $HCO + H \rightarrow HCOH$ reaction is endothermic (+0.35 eV). The former pathway is also kinetically more favorable than the latter, with a lower barrier of 0.44 eV compared with a barrier of 1.06 eV for the $HCO + H \rightarrow H-COH$ reaction.

3.2.3.7. $H_2COH$ formation: $HCOH + H \rightarrow H_2COH$ and $H_2CO(g) + H \rightarrow H_2COH$. Two reaction pathways are identified for $H_2COH$ formation. $H_2COH$ can be produced via HCOH hydrogenation in an LH mechanism, or by the hydrogenation of $H_2CO$ in an ER mechanism. Bridged HCOH species react with atomic H to form $H_2COH$ sitting at a bridge site. At the transition state (Fig. S3o), the forming C-H bond length is 1.72 Å. Hydrogenation of HCOH to $H_2COH$ is found to be exothermic (-0.75 eV) with a very low barrier of 0.10 eV. For the $H_2CO(g) + H \rightarrow H_2COH$ pathway, gas-phase $H_2CO$ directly reacts with surface H to form $H_2COH$ adsorbed at atop sites on Cu(1 1 1). Although this second pathway is still exothermic (-0.05 eV), the activation barrier (0.66 eV) is higher than the first pathway.

3.2.3.8. Methanol formation from $H_2COH$: $H_2COH + H \rightarrow H_3COH$. $H_2COH$ hydrogenation to methanol on Cu(1 1 1) is highly exothermic with a reaction energy of -0.78 eV. At the transition state (Fig. S3q), the distance of the forming C-H bond is 1.87 Å. The calculated barrier is 0.62 eV, which is in good agreement with a previously reported barrier of 0.54 eV [35]. Compared with methanol formation from $H_3CO$ hydrogenation with a high barrier of 0.90 eV, the $H_2COH + H \rightarrow H_3COH$ pathway is significantly more favorable.

### 3.3. Water formation

#### 3.3.1. $O + H \rightarrow OH$
OH formation via the recombination of atomic H and O is exothermic (-0.60 eV), with a calculated barrier of 0.76 eV. At the initial state, the atomic O and H sit at adjacent hollow sites, approximately 2.80 Å apart. At the transition state (Fig. S4a), the atomic H moves to the bridge site, resulting in a shortening of the distance between the O and H atoms to 1.56 Å. The formed OH adsorbs at hollow sites in an uptight configuration via a Cu-O bond. Our results for this process are again consistent with the previous DFT calculations [33,34].

#### 3.3.2. $OH + H \rightarrow H_2O$
The formed OH further reacts with another atomic H to generate weakly bonded $H_2O$ sitting at an atop site. In good agreement with the results of Phatak et al. [34], $H_2O$ formation from $OH + H$ is slightly endothermic (+0.23 eV) and the barrier for $H_2O$ formation on Cu(1 1 1) is 0.99 eV. At the transition state, the distance for the forming O-H bond is 1.43 Å (Fig. S4b). We also find a second and similar pathway for the $OH + H \rightarrow H_2O$ reaction. The calculated reaction energy (+0.09 eV) suggests this alternative $H_2O$ formation path is thermoneutral. The calculated activation barrier is 1.28 eV, which is in excellent agreement with the result by Gokhale et al. [33]. We note that the initial states are different for these two $H_2O$ formation pathways, although the final states are the same. In the first pathway, the atomic H and the OH co-adsorb at neighboring fcc and hcp hollow sites sharing a common surface Cu atom. In the second pathway, both the atomic H and the OH group co-adsorb at neighboring fcc sites. These results demonstrate the advantage of the dimer method for reaction pathway studies over the traditional NEB method. In the NEB method, pre-determined initial and final states may overlook the "real" possible minimum reaction path for the same elementary step.

To find out the effects of different functionals such as PBE on the reaction energetics, we re-calculated the $H_2O$ formation on Cu(1 1 1) using PBE functional. The calculated activation barrier for $H_2O$ formation is 1.37 eV, which is close to the barrier of 1.28 eV with PW91 functional in the alternative $H_2O$ path. The calculated reaction energy is +0.18 eV with PBE functional, which is also consistent with 0.09 eV with PW91 functional.

#### 3.3.3. $OH + OH \rightarrow H_2O + O$
$H_2O$ can also be produced by the recombination of two surface OH groups. Our result indicates that this disproportionation reaction is endothermic (+0.17 eV). The calculated barrier is 0.27 eV, which is slightly higher than a previously reported value of 0.23 eV [33]. At the transition state, the distance for the forming O-H bond is 1.35 Å (Fig. S4c).

### 3.4. Reaction paths in the presence of water or hydroxyl

Because water is a reaction product of methanol synthesis, we have investigated the effects of co-adsorbed water or hydroxyl groups on the calculated reaction kinetics and energetics for a number of the mechanistic processes described in Sections 3.2 and 3.3. The results are summarized in Table 3.

#### 3.4.1. $CO_2 + H_2O \rightarrow trans-COOH + OH$
Trans-COOH can be produced by reaction of $CO_2$ and $H_2O$ on the Cu(1 1 1) surface. This reaction is endothermic by +0.29 eV, and the calculated reaction barrier is 0.38 eV. In the initial state, the distance between the O atom in $CO_2$ and the H atom in $H_2O$ is 1.46 Å. At the transition state, the OH bond length is 1.06 Å. However, since the reverse barrier for the reaction is as low as 0.08 eV, it is expected that the formed trans-COOH would quickly dissociate back to $CO_2$ and $H_2O$. Our result is consistent with previous work [33].

#### 3.4.2. $CO_2 + H_b + HOH_a \rightarrow trans-COOH_a + HOH_b$
A unique LH reaction pathway for $CO_2$ hydrogenation to the trans-COOH on Cu(1 1 1) has been identified in this work (Section 3.2.3.1). In the initial state, weakly bonded $CO_2$ at bridge sites co-adsorbs with atomic H. Addition of an $H_2O$ molecule positioned right above the atomic H, allows for interactions between $H_2O$ and the surface H atoms sitting at hollow sites via hydrogen bonding. The attractive interaction due to hydrogen bonding between the $H_2O$ and these H atoms is estimated to be ~0.2 eV. The distance between the surface H atom and the O atom in $CO_2$ is 3.42 Å, which is 1.0 Å longer than the distance between the surface H atom and the O atom in $H_2O$. As shown in Fig. 2, the surface H moves upward forming a new O-H bond with $H_2O$ at the transition state. Simultaneously, one of O-H bonds in $H_2O$ is breaking as this latter H atom moves toward the O atom in the adsorbed $CO_2$. Compared with the initial distance of 1.81 Å, the distance between the moving H atom in $H_2O$ and the O atom in $CO_2$ is shortened to 1.46 Å. Thus, unlike the $CO_2 + H \rightarrow trans-COOH$ pathway in the absence of $H_2O$ discussed earlier, in the presence of $H_2O$, the hydrogenation of $CO_2$ to the trans-COOH is via a hydrogen transfer mechanism. The

<table><caption>Table 3 DFT Calculated activation barriers ($E_a$), reaction energies ($\Delta H$), Gibbs free energies ($\Delta G$), and rate constants (@500 K) ($k_{forward}$ and $k_{reverse}$) for several hydrogenation steps in the presence of $\text{H}_2\text{O}$ or $\text{OH}$.</caption>
<thead>
<tr>
<th>Elementary step</th>
<th>$E_a$ (eV)</th>
<th>$\Delta E$ (eV)</th>
<th>$E_a^{ZPEC}$ (eV)</th>
<th>$\Delta E^{ZPEC}$ (eV)</th>
<th>$\Delta G$ (eV)</th>
<th>$k_{forward}$ ($\text{s}^{-1}$)</th>
<th>$k_{reverse}$ ($\text{s}^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{CO}_2 + \text{H}_2\text{O} \leftrightarrow \text{COOH} + \text{OH}$</td>
<td>0.38</td>
<td>0.30</td>
<td>0.38</td>
<td>0.30</td>
<td>0.30</td>
<td>1.25E+09</td>
<td>2.81E+12</td>
</tr>
<tr>
<td>$\text{CO}_2 + \text{H}_b + \text{HOH}_a \leftrightarrow trans\text{-COOH}_a + \text{HOH}_b$</td>
<td>0.26</td>
<td>−0.51</td>
<td>0.17</td>
<td>−0.38</td>
<td>−0.34</td>
<td>8.51E+10</td>
<td>3.43E+07</td>
</tr>
<tr>
<td>$\text{CO}_2 + \text{H}_b + \text{HOH}_a \leftrightarrow trans\text{-COOH}_a + \text{HOH}_b$</td>
<td>0.86</td>
<td>0.04</td>
<td>0.77</td>
<td>0.16</td>
<td>0.16</td>
<td>4.59E+05</td>
<td>9.53E+03</td>
</tr>
<tr>
<td>$\text{CO}_2 + \text{H} + \text{H}_2\text{O} \leftrightarrow bi\text{-HCOO} + \text{H}_2\text{O}$</td>
<td>0.55</td>
<td>−0.72</td>
<td>0.49</td>
<td>−0.58</td>
<td>−0.58</td>
<td>2.31E+08</td>
<td>2.27E+07</td>
</tr>
<tr>
<td>$\text{HCOO(bi)} + \text{OH} \leftrightarrow \text{H}_2\text{COO} + \text{O}$</td>
<td>1.93</td>
<td>1.20</td>
<td>1.81</td>
<td>1.23</td>
<td>1.23</td>
<td>1.68E−06</td>
<td>1.04E+11</td>
</tr>
<tr>
<td>$mono\text{-HCOO} + \text{H}_2\text{O} \leftrightarrow bi\text{-HCOO} + \text{H}_2\text{O}$</td>
<td>0.30</td>
<td>−0.18</td>
<td>0.24</td>
<td>−0.16</td>
<td>−0.16</td>
<td>1.73E+12</td>
<td>6.96E+08</td>
</tr>
<tr>
<td>$mono\text{-HCOO} + \text{OH} \leftrightarrow bi\text{-HCOO} + \text{OH}$</td>
<td>0.29</td>
<td>−0.23</td>
<td>0.29</td>
<td>−0.19</td>
<td>−0.19</td>
<td>1.28E+11</td>
<td>1.09E+08</td>
</tr>
<tr>
<td>$bi\text{-HCOO} + \text{H}_2\text{O} \leftrightarrow \text{HCO} + \text{OH} + \text{OH}$</td>
<td>1.87</td>
<td>1.45</td>
<td>1.78</td>
<td>1.34</td>
<td>1.34</td>
<td>3.83E−06</td>
<td>2.81E+12</td>
</tr>
</tbody>
</table>

![](./images/811655950476771329_2.jpg)

Fig. 2. $trans$-COOH formation via hydrogen transfer mechanism.

calculated activation barrier for the $trans$-COOH formation is only 0.17 eV, which is dramatically lower than the barrier of 1.16 eV in the absence of $\text{H}_2\text{O}$. The reaction energy for this hydrogen transfer pathway is $-0.52$ eV, suggesting that this step is both kinetically and thermodynamically favorable. Note that the reaction energy without $\text{H}_2\text{O}$ is +0.18 eV for gas-phase $\text{CO}_2$ or $-0.24$ eV for weakly adsorbed $\text{CO}_2$.

We also identified a second hydrogen transfer transition state with adsorbed $\text{H}_2\text{O}$ on the surface in the initial state. At the transition state, the surface H atom moves toward the O atom of adsorbed $\text{H}_2\text{O}$ on the surface. The distance between the surface H and the O atom is shortened from $3.49\ \text{Å}$ to $1.51\ \text{Å}$. While the H atom of $\text{H}_2\text{O}$ moves to the O atom of adsorbed $\text{CO}_2$. The OH bond length is extended from $1.07\ \text{Å}$ to $1.41\ \text{Å}$. The calculated reaction barrier for the second hydrogen transfer path is 0.77 eV with the reaction energy of 0.16 eV. Since the reverse barriers for both hydrogen transfer reaction paths are the same, we concluded that the difference of the forward barriers (0.25 vs 0.77 eV) is mainly due to the energy difference between two initial states. The calculated interaction energy between co-adsorbed $\text{CO}_2$ and $\text{H}_2\text{O}$ is 0.5 eV, which is consistent with the previous result [33].

### 3.4.3. $\text{CO}_2(g) + \text{H} + \text{H}_2\text{O} \rightarrow bi\text{-HCOO} + \text{H}_2\text{O}$

The effect of co-adsorbed $\text{H}_2\text{O}$ on HCOO formation from $\text{CO}_2(g) + \text{H}$ is also investigated. In this case, a similar hydrogen transfer reaction pathway for HCOO formation is not identified using the dimer method. Instead, we find that the effect of co-adsorbed $\text{H}_2\text{O}$ at an atop site has quite small effects on the reaction kinetics and energetics. The calculated barrier is 0.48 eV, which is only slightly lower than the barrier of 0.57 eV in the absence of $\text{H}_2\text{O}$.

### 3.4.4. $bi\text{-HCOO} + \text{OH} \rightarrow \text{H}_2\text{COO} + \text{H}$

In the presence of the co-adsorbed OH, the disproportionation reaction of $bi\text{-HCOO} + \text{OH} \rightarrow \text{H}_2\text{COO} + \text{H}$ is highly endothermic (+1.23 eV). The calculated barrier is 1.81 eV, which is much higher than the barrier for HCOO hydrogenation without OH.

### 3.4.5. $mono\text{-HCOO} + \text{H}_2\text{O} \rightarrow bi\text{-HCOO} + \text{H}_2\text{O}$ and $mono\text{-HCOO} + \text{OH} \rightarrow bi\text{-HCOO} + \text{OH}$

Without co-adsorbed $\text{H}_2\text{O}$ or OH, the conversion of $mono$-HCOO to $bi$-HCOO is nearly spontaneous (0.02 eV). However, the barrier for this conversion increases to $\sim$0.28 eV when an OH group or $\text{H}_2\text{O}$ molecule is in the vicinity of the reactive site. Although $bi$-HCOO is still more stable than $mono$-HCOO, the existence of OH and/or $\text{H}_2\text{O}$ increases the relative stability of the $mono$-HCOO species on the $\text{Cu(1 1 1)}$ surface.

### 3.4.6. $bi\text{-HCOO} + \text{H}_2\text{O} \rightarrow \text{HCO} + \text{OH} + \text{OH}$

We have also studied the C–O bond scission in $bi$-HCOO with the assistance of neighboring $\text{H}_2\text{O}$ to form HCO and two OH groups. This reaction is highly endothermic (+1.34 eV) with an extremely higher barrier (1.78 eV), indicating that this disproportionation reaction is not practical.

## 4. Discussion

We have investigated the reaction network of methanol synthesis from $CO_2$ hydrogenation on $Cu(1\ 1\ 1)$, including 46 elementary steps and 18 reaction intermediates. As shown in Fig. 1, the formate and hydrocarboxyl routes are considered as the two most probably elementary step mechanisms in the reaction network. A mixed reaction route via a formyl species is also evaluated in the present work. On the basis of our extensive DFT calculations, the potential energy surfaces of $CO_2$ hydrogenation to methanol via the formate and hydrocarboxyl mechanisms are directly compared in Fig. 3. For all the elementary steps in the two routes, only the most favorable path with the lowest activation barrier for each elementary step is considered.

### 4.1. The formate route

Methanol synthesis from $CO_2$ hydrogenation via formate hydrogenation has been widely assumed as the reaction mechanism on Cu-based catalysts [17,18,20,23,24,49]. After dissociative adsorption of $H_2$, $CO_2$ directly interacts with the surface H to form HCOO via an ER mechanism. HCOO is then hydrogenated to $H_2COO$, which can be deoxygenated to $H_2CO$ via the $H_2COOH$ intermediate. Further hydrogenation of $H_2CO$ leads to $H_3CO$ and $H_3COH$. This formate reaction mechanism was first proposed for methanol synthesis on the $Cu(1\ 0\ 0)$ surface [17-18]. On the basis of the formate mechanism, Askgaard et al. suggested that the hydrogenation of $H_2COO$ to $H_3CO$ ($H_2COO + H \rightarrow H_3CO + O$) is the rate-limiting step in their kinetic modeling, although, as discussed earlier, the evidence for the existence of $H_2COO$ was very elusive [49]. These authors suspected that undetectable $H_2COO$ and $H_3CO$ intermediates on the metallic Cu surface during methanol synthesis were due to very low surface coverages. However, they also suggested that the rate-limiting step might be the $H_3CO$ hydrogenation to methanol as compared with the experimental data on the industrial catalysts with the dominating $Cu(1\ 1\ 1)$ surface exposed. This uncertainty is further complicated by the experimental observation that hydrogenation of HCOO most likely leads to $H_2CO$ and HCOOH formation instead of methanol on $Cu(1\ 0\ 0)$ [20].

Many previous experiments unambiguously observe large concentrations of HCOO species on clean Cu surfaces upon exposure to $CO_2$ and $H_2$ mixtures, as well as at typical methanol synthesis reaction conditions [1,21,22,51,52,58]. The first step from $CO_2$ hydrogenation on $Cu(1\ 1\ 1)$ is to form HCOO, with a formation barrier (0.62 eV) that is much lower than the barrier (1.16 eV) for COOH formation. As shown in Fig. 3, two elementary steps with high activation barriers are found as possible rate-limiting steps in the following hydrogenation steps from HCOO to $H_3COH$. The first possible rate-limiting step is the hydrogenation of HCOO to $H_2COO$. This step has been studied in detail in our previous work [53]. The calculated HCOO hydrogenation rate is about 5-6 times slower than the HCOO decomposition to $CO_2$ in the temperature range of 353-403 K. More importantly, the dehydrogenation rate of $H_2COO$ to HCOO is about $2 \times 10^6$-$10^7$ times greater than the HCOO hydrogenation rate [53]. Although our results show that the formed $H_2COO$ strongly binds on the $Cu(1\ 1\ 1)$ surface, the stability of $H_2COO$ is low (the lifetime on the surface is short). Once $H_2COO$ is formed, it will be easily dehydrogenated back to HCOO before further hydrogenation to $H_2COOH$. The HCOO hydrogenation on $Cu(1\ 1\ 1)$ was recently studied by Liu and coworkers [23]. An even higher activation barrier (1.60 eV) for HCOO hydrogenation than found here was reported. Besides hydrogenation to $H_2COO$, bi-HCOO can also be hydrogenated into HCOOH with a barrier of 0.70 eV. Obviously, HCOOH formation is more favorable than $H_2COO$ formation. The formed HCOOH either desorbs from the surface due to relatively weak binding or dissociates back into the bi-HCOO and atomic H with a barrier of 0.31 eV. In fact, the side product, HCOOH, from $CO_2$ hydrogenation on $Cu(1\ 0\ 0)$ was

![](./images/811655950476771329_3.jpg)

Fig. 3. Potential energy surfaces for CO2 hydrogenation to methanol on $Cu(1\ 1\ 1)$ via the formate and hydrocarboxyl mechanisms.

only assumed and no direct experimental evidence was reported [20], although the reverse reaction, HCOOH decomposition to HCOO, on Cu has been experimentally studied [1,51,58].

Our calculations show that the decomposition of $\text{H}_2\text{COOH}$ to $\text{H}_2\text{CO}$ and $\text{OH}$ is even more difficult than the HCOO hydrogenation. This second possible rate-limiting step is endothermic with the highest barrier of 1.16 eV in the formate route. Liu and coworkers [23] calculated an activation barrier of 1.60 eV for the $\text{H}_2\text{COO} + \text{H} \rightarrow \text{H}_2\text{CO} + \text{OH}$ step on $\text{Cu(1 1 1)}$. They suggested that the slow kinetics of methanol synthesis on $\text{Cu(1 1 1)}$ were due to the high barriers of both HCOO and $\text{H}_2\text{COO}$ hydrogenations. Most importantly, we note that the formed $\text{H}_2\text{CO}$ most likely desorbs from the surface rather than being further hydrogenated to $\text{H}_3\text{CO}$. Our calculations indicate that $\text{H}_2\text{CO}$ very weakly adsorbs on $\text{Cu(1 1 1)}$, consistent with previous theoretical studies [23,36,43]. However, no large amounts of $\text{H}_2\text{CO}$ as a side product of methanol synthesis over Cu catalysts have been experimentally detected [1,17,18,20–23]. Although it has been argued that supported Cu nanoparticles with coordinatively unsaturated Cu sites provide for stronger interaction with $\text{H}_2\text{CO}$ [23], it is clear that there should be detectable $\text{H}_2\text{CO}$ formation during $\text{CO}_2$ hydrogenation on Cu if the formate mechanism is followed.

Based on the earlier discussion, we conclude that the formate route for $\text{CO}_2$ hydrogenation to methanol on $\text{Cu(1 1 1)}$ is not feasible at typical operating low temperature conditions. This confirms recent experimental observations that the direct hydrogenation of formate on metallic Cu catalysts under dry $\text{H}_2$ condition does not produce any methanol [1]. Thus, an alternative reaction route leading to methanol formation on Cu catalysts must be operative. Interestingly, formate is also identified as the "dead end" for $\text{CO}_2$ hydrogenation on $\text{Ni(1 1 0)}$ by a combined experimental and theoretical study [59].

### 4.2. The hydrocarboxyl route
Although a hydrocarboxyl species has been recently identified as a key intermediate in the WGS reaction on $\text{Cu(1 1 1)}$ [33], the formation of $\text{COOH}$ from $\text{CO}_2$ hydrogenation is difficult. Because $\text{CO}_2$ binding at the $\text{Cu(1 1 1)}$ surface is very weak, gas phase $\text{CO}_2$ directly interacts with surface atomic H to form *trans*-COOH via an ER mechanism. Compared with the parallel HCOO formation, the COOH formation barrier (1.17 eV) is quite high. This is almost certainly why abundant HCOO, not the COOH species, are always observed in the experiments [1,21,22]. After its formation, the COOH has to first be deoxygenated to COH. The resulting COH will then be converted to $\text{H}_3\text{COH}$ by three consecutive hydrogenation steps. Our calculation results show that all three hydrogenation steps from COH to $\text{H}_3\text{COH}$ are energetically downhill processes. The highest barrier for these three hydrogenation steps is only 0.66 eV. This suggests that both COOH and COH formation are the key steps in the hydrocarboxyl mechanism for methanol production.

We find that *trans*-COOH can be hydrogenated to a COHOH species, which then decomposes into COH and OH on $\text{Cu(1 1 1)}$. As shown in Fig. 3, the barriers for the *trans*-$\text{COOH} + \text{H} \rightarrow \text{t,t-COHOH} \rightarrow \text{t,c-COHOH} \rightarrow \text{COH} + \text{OH}$ are 0.37, 0.58, 1.01 eV, respectively. Actually, another low barrier path has been calculated by using the dimer method. The t,c-COHOH may convert to the c,c-COHOH, which dissociates into COH and OH with a much lower barrier of 0.55 eV. These results suggest that the formation of the COH species via COHOH is feasible as long as the *trans*-COOH can be efficiently formed by $\text{CO}_2$ hydrogenation. We also note that COHOH was proposed as an intermediate in the conversion of COH to COOH for the direct methanol electrooxidation mechanism on transition metal surfaces [40]. It is clear that the hydrocarboxyl route for $\text{CO}_2$ hydrogenation to methanol on $\text{Cu(1 1 1)}$ is energetically more plausible over the formate route if the *trans*-COOH could be formed. The calculated barriers of all involved elementary steps in the hydrocarboxyl route are lower than 1.0 eV.

### 4.3. $\text{H}_2\text{O}$ effects
Yang et al. studied the reactivity of HCOO overlayers on supported and unsupported Cu catalysts under $\text{H}_2$ pressure [1]. While no methanol was generated for the clean Cu catalysts, they found that significant amounts of methanol were produced when the Cu catalysts were pretreated by $\text{O}_2$ or $\text{N}_2\text{O}$, although formate decomposition to $\text{CO}_2$ and $\text{H}_2$ was still the dominant pathway [1]. In a high-pressure $\text{H}_2$ environment, it is reasonable to suggest that OH groups or $\text{H}_2\text{O}$ molecules can be formed on the $\text{O}_2$- or $\text{N}_2\text{O}$-pretreated Cu surfaces. This experimental observation motivated us to investigate the role of $\text{H}_2\text{O}$ in methanol synthesis on the $\text{Cu(1 1 1)}$ surface.

Firstly, we find that co-adsorbed $\text{H}_2\text{O}$ has negligible effects on HCOO formation from $\text{CO}_2$ hydrogenation, although it does affect the relative stability of the adsorbed HCOO. In the absence of $\text{H}_2\text{O}$, mono-HCOO converts to bi-HCOO spontaneously without a barrier. Thus, as experiments demonstrate, the Cu surface can become completely covered by the bi-HCOO species. However, the conversion barrier from a mono-HCOO to bi-HCOO increases to 0.24 eV in the presence of $\text{H}_2\text{O}$, even though our calculation results show that bi-HCOO is still very slightly more stable (0.1 eV) than mono-HCOO. This is also perhaps consistent with experimental observations that a bi-HCOO formate surface overlayer changes to mono-HCOO for $\text{O}_2$- or $\text{N}_2\text{O}$-pretreated Cu surfaces [1]. On the basis of our calculation results, we also find that the existing presence of $\text{H}_2\text{O}$ on the $\text{Cu(1 1 1)}$ surface actually plays an inhibiting role in the further hydrogenation or decomposition processes from HCOO to methanol in the formate mechanism.

On the other hand, we find that the presence of $\text{H}_2\text{O}$ markedly promotes a key step of COOH formation in the hydrocarboxyl mechanism. Notably, a unique hydrogen transfer process for *trans*-COOH formation, shown in Fig. 2, is identified using the dimer method. In this hydrogen transfer mechanism, weakly bonded $\text{CO}_2$ is hydrogenated by one of the H atoms in $\text{H}_2\text{O}$ as surface H begins to strongly interact with the $\text{H}_2\text{O}$ molecule. Thus, this water-mediated pathway facilitates the formation of the *trans*-COOH, which is the bottleneck step in the hydrocarboxyl mechanism. The barrier for *trans*-COOH formation is only 0.17 eV, and the reaction is exothermic, in part, because the presence of $\text{H}_2\text{O}$ greatly enhances the stability of *trans*-COOH by co-adsorption. The promotion effect of $\text{H}_2\text{O}$ was also found in our previous study of CO oxidation on gold nanoclusters [60].

### 4.4. The reverse water–gas shift and methanol synthesis from CO hydrogenation
The reverse water–gas shift (RWGS) reaction has been considered to be the major side reaction during $\text{CO}_2$ hydrogenation to methanol [7,24,26]. Here, we briefly discuss the RWGS shift reaction on $\text{Cu(1 1 1)}$ based on our calculations of various elementary steps of the methanol synthesis reaction. On the clean $\text{Cu(1 1 1)}$ surface (i.e., in the absence of significant amounts of co-adsorbed O, OH or $\text{H}_2\text{O}$), bi-HCOO will be the most abundant surface species formed by $\text{CO}_2$ hydrogenation as discussed earlier, because the formation of *trans*-COOH is kinetically inhibited by a relatively high barrier. Our previous DFT study indicated that CO formation from the HCOO decomposition is impossible due to an extremely high barrier (2.80 eV) [53]. Considering that direct dissociation of $\text{CO}_2$ to CO on $\text{Cu(1 1 1)}$ is also not likely, we conclude that the RWGS might not occur on the clean $\text{Cu(1 1 1)}$ surface. Note, however, one cannot exclude the possibility of the RWGS reaction on clean $\text{Cu(1 1 0)}$ and $\text{Cu(1 0 0)}$ surfaces, which is beyond the scope of

our present work. However, RWGS reaction can potentially occur on Cu(1 1 1) surfaces with pre-adsorbed oxygen atoms, which can then be hydrogenated to OH and $H_2O$ by surface H atoms. As discussed in Section 4.2, instead of the HCOO species, trans-COOH is expected to be generated via a water-mediated hydrogen transfer mechanism. Our calculations show that cis-COOH, which is formed from trans-COOH with a barrier of 0.47 eV, could dissociate into CO and OH with a barrier of 0.12 eV. This is consistent with previous findings that the WGS reaction on Cu(1 1 1) is most likely via a COOH species [33]. Our calculations show that methanol synthesis from CO hydrogenation may also follow the COOH route. CO reacts with OH forming cis-COOH on Cu(1 1 1) surface and has a barrier of 0.73 eV. Then cis-COOH could easily transfer to trans-COOH with a barrier of 0.42 eV.

Hydrogenation of CO can lead to either HCO or COH species. Our calculated barrier for the $CO + H \rightarrow COH$ step is 1.87 eV, indicating this reaction step is very unlikely. On the other hand, the barrier for the $CO + H \rightarrow HCO$ step is only 0.88 eV. Consistent with the previous DFT results [23], the formed HCO is unstable and readily dissociates back to CO and atomic H with a very low barrier of 0.15 eV. Further hydrogenation of HCO could lead to the formation of HCOH or $H_2CO$. Our results show that the formation of $H_2CO$ is much more favorable than HCOH formation from HCO hydrogenation, although the formed $H_2CO$ most likely desorbs from the surface. However, as noted before, previous methanol synthesis studies did not observe $H_2CO$ as a product. As a result, we believe that methanol formation on Cu(1 1 1) is probably not through an HCO intermediate.

## 5. Conclusions

Extensive density functional theory calculations were performed to map out the entire reaction network of $CO_2$ hydrogenation to methanol on the Cu(1 1 1) surface. Our results can rationalize previous experimental results; it is shown that direct formate hydrogenation does not lead to methanol due to the high hydrogenation barriers of HCOO and $H_2COO$. Formate, formaldehyde, and methoxy are unlikely to be reaction intermediates for methanol synthesis. In addition, we find that an alternative hydrocarboxyl mechanism, while possible, is also difficult because of a high barrier for the initial step, $H + CO_2 \rightarrow trans$-COOH. However, we demonstrate a crucial role of $H_2O$ in the methanol synthesis on Cu(1 1 1), particularly for the enhancement of the hydrocarboxyl mechanism. Since small amounts of oxygen species on Cu(1 1 1), mimicking Cu catalysts pretreated with the oxidants, $O_2$ or $N_2O$ in the experimental studies, can generate adsorbed $H_2O$ in $H_2$ environments, we have identified a feasible reaction route for methanol production from $CO_2$ hydrogenation, i.e., $CO_2 + 6H+(H_2O) \rightarrow trans$-COOH $+ 5H \rightarrow t,t$-COHOL $+ 4H \rightarrow t,c$-COHOL $+ 4H \rightarrow c,c$-COHOL $+ 4H \rightarrow COH + OH + 4H \rightarrow HCOH + 3H + OH \rightarrow H_2$-COH $+ 2H + OH \rightarrow H_3COH + H + OH \rightarrow H_3COH + H_2O$. The rate-limiting step in this hydrocarboxyl route is the decomposition of COH to COH and OH with the highest barrier of 0.68 eV, a value that is much lower than the two hydrogenation barriers of 1.20 and 1.17 eV in the formate mechanism. Most importantly, trans-COOH formation via a unique hydrogen transfer process is kinetically more favorable than the HCOO formation in the presence of $H_2O$. Finally, on the basis of the calculation results, we suggest that both reverse water-gas shift reaction and methanol synthesis from dry $CO_2 + H_2$ mixtures on the clean Cu(1 1 1) surface (i.e., without co-adsorbed O) at low temperatures are unlikely because the dominant HCOO surface species is a mechanistic "dead end".

## Acknowledgments

This work was supported by a Laboratory Directed Research and Development (LDRD) project at the Pacific Northwest National Laboratory (PNNL). The computations were performed using the Molecular Science Computing Facility in the William R. Wiley Environmental Molecular Sciences Laboratory (EMSL), which is a US Department of Energy national scientific user facility located at PNNL in Richland, Washington. Computing time was made available through a Computational Grand Challenge (gc34000) and user facility project under EMSL-30209 as well as the National Energy Research Scientific Computing Center (NERSC). J. Li and Y.-F. Zhao were also financially supported by the National Natural Science Foundation of China (Nos. 20933003 and 91026003) and the National Basic Research Program of China (No. 2011CB932400). Y.-F. Zhao acknowledges the fellowship from PNNL.

## Appendix A. Supplementary material

Supplementary data associated with this article can be found, in the online version, at doi:10.1016/j.jcat.2011.04.012.

## References

[1] Y. Yang, C.A. Mims, R.S. Disselkamp, J.H. Kwak, C.H.F. Peden, C.T. Campbell, J. Phys. Chem. C 114 (2010) 17205.

[2] X.M. Liu, G.Q. Lu, Z.F. Yan, J. Beltramini, Ind. Eng. Chem. Res. 42 (2003) 6518.

[3] D.R. Palo, R.A. Dagle, J.D. Holladay, Chem. Rev. 107 (2007) 3992.

[4] J. Ma, N.N. Sun, X.L. Zhang, N. Zhao, F.K. Mao, W. Wei, Y.H. Sun, Catal. Today 148 (2009) 221.

[5] C.S. Song, Catal. Today 115 (2006) 2.

[6] M. Bowker, R.A. Hadden, H. Houghton, J.N.K. Hyland, K.C. Waugh, J. Catal. 109 (1988) 263.

[7] G.C. Chinchen, P.J. Denny, J.R. Jennings, M.S. Spencer, K.C. Waugh, Appl. Catal. 36 (1988) 1.

[8] I. Chorkendorff, P.A. Taylor, P.B. Rasmussen, J. Vac. Sci. Technol. A 10 (1992) 2277.

[9] I.A. Fisher, A.T. Bell, J. Catal. 184 (1999) 357.

[10] T. Fujitani, I. Nakamura, T. Uchijima, J. Nakamura, Surf. Sci. 383 (1997) 285.

[11] T. Fujitani, I. Nakamura, S. Ueno, T. Uchijima, J. Nakamura, Appl. Surf. Sci. 121 (1997) 583.

[12] L.Z. Gao, C.T. Au, J. Catal. 189 (2000) 1.

[13] K. Klier, V. Chatikavanij, R.G. Herman, G.W. Simmons, J. Catal. 74 (1982) 343.

[14] M. Maack, H. Friis-Jensen, S. Sckerl, J.H. Larsen, I. Chorkendorff, Top. Catal. 22 (2003) 151.

[15] I. Nakamura, T. Fujitani, T. Uchijima, J. Nakamura, J. Vac. Sci. Technol. A 14 (1996) 1464.

[16] J. Nakamura, I. Nakamura, T. Uchijima, Y. Kanai, T. Watanabe, M. Saito, T. Fujitani, Catal. Lett. 31 (1995) 325.

[17] P.B. Rasmussen, P.M. Holmlblad, T. Askgaard, C.V. Ovesen, P. Stoltze, J.K. Norskov, I. Chorkendorff, Catal. Lett. 26 (1994) 373.

[18] P.B. Rasmussen, M. Kazuta, I. Chorkendorff, Surf. Sci. 318 (1994) 267.

[19] Q.L. Tang, Q.J. Hong, Z.P. Liu, J. Catal. 263 (2009) 114.

[20] P.A. Taylor, P.B. Rasmussen, I. Chorkendorff, J. Chem. Soc. - Faraday Trans. 91 (1995) 1267.

[21] Y. Yang, C.A. Mims, R.S. Disselkamp, D. Mei, J.H. Kwak, J. Szanyi, C.H.F. Peden, C.T. Campbell, Catal. Lett. 125 (2008) 201.

[22] Y. Yang, C.A. Mims, R.S. Disselkamp, C.H.F. Peden, C.T. Campbell, Top. Catal. 52 (2009) 1440.

[23] Y.X. Yang, J. Evans, J.A. Rodriguez, M.G. White, P. Liu, Phys. Chem. Chem. Phys. 12 (2010) 9909.

[24] J. Yoshihara, C.T. Campbell, J. Catal. 161 (1996) 776.

[25] K.C. Waugh, Catal. Today 15 (1992) 51.

[26] J. Yoshihara, S.C. Parker, A. Schafer, C.T. Campbell, Catal. Lett. 31 (1995) 313.

[27] J. Szanyi, D.W. Goodman, Catal. Lett. 10 (1991) 383.

[28] G. Henkelman, H. Jonsson, J. Chem. Phys. 111 (1999) 7010.

[29] D.H. Mei, L.J. Xu, G. Henkelman, J. Phys. Chem. C 113 (2009) 4522.

[30] L.J. Xu, D.H. Mei, G. Henkelman, J. Chem. Phys. 131 (2009).

[31] G. Kresse, J. Furthmuller, Phys. Rev. B 54 (1996) 11169.

[32] G. Kresse, J. Furthmuller, Comput. Mater. Sci. 6 (1996) 15.

[33] A.A. Gokhale, J.A. Dumesic, M. Mavrikakis, J. Am. Chem. Soc. 130 (2008) 1402.

[34] A.A. Phatak, W.N. Delgass, F.H. Ribeiro, W.F. Schneider, J. Phys. Chem. C 113 (2009) 7269.

[35] X.K. Gu, W.X. Li, J. Phys. Chem. C 114 (2010) 21539.

[36] K.H. Lim, Z.X. Chen, K.M. Neyman, N. Rosch, J. Phys. Chem. B 110 (2006) 14890.

[37] A. Sotiropoulos, P.K. Milligan, B.C.C.owie, M. Kadodwala, Surf. Sci. 444 (2000) 52.

[38] P.R. Schreiner, H.P. Reisenauer, F.C. Pickard, A.C. Simmonett, W.D. Allen, E. Matyus, A.G. Csaszar, Nature 453 (2008) 906.

[39] P.R. Schreiner, H.P. Reisenauer, Angew. Chem. Int. Edit. 47 (2008) 7071.

[40] P. Ferrin, M. Mavrikakis, J. Am. Chem. Soc. 131 (2009) 14381.

[41] J. Greeley, M. Mavrikakis, J. Am. Chem. Soc. 126 (2004) 3910.

[42] Z.X. Chen, K.M. Neyman, K.H. Lim, N. Rosch, Langmuir 20 (2004) 8068.

[43] J. Greeley, M. Mavrikakis, J. Catal. 208 (2002) 291.

[44] P. Hofmann, K.M. Schindler, S. Bao, V. Fritzsche, D.E. Ricken, A.M. Bradshaw, D.P. Woodruff, Surf. Sci. 304 (1994) 74.

[45] S.M. Johnston, A. Mulligan, V. Dhanak, M. Kadodwala, Surf. Sci. 530 (2003) 111.

[46] D.B. Clarke, A.T. Bell, J. Catal. 154 (1995) 314.

[47] I.E. Wachs, R.J. Madix, Surf. Sci. 84 (1979) 375.

[48] B.A. Sexton, A.E. Hughes, N.R. Avery, Surf. Sci. 155 (1985) 366.

[49] T.S. Askgaard, J.K. Norskov, C.V. Ovesen, P. Stoltze, J. Catal. 156 (1995) 229.

[50] J. Stromquist, L. Bengtsson, M. Persson, B. Hammer, Surf. Sci. 397 (1998) 382.

[51] H. Nishimura, T. Yatsu, T. Fujitani, T. Uchijima, J. Nakamura, J. Mol. Catal. A 155 (2000) 3.

[52] I. Nakamura, H. Nakano, T. Fujitani, T. Uchijima, J. Nakamura, J. Vac. Sci. Technol. A 17 (1999) 1592.

[53] D.H. Mei, L. Xu, G. Henkelman, J. Catal. 258 (2008) 44.

[54] D.B. Clarke, D.K. Lee, M.J. Sandoval, A.T. Bell, J. Catal. 150 (1994) 81.

[55] N.D. Lazo, D.K. Murray, M.L. Kieke, J.F. Haw, J. Am. Chem. Soc. 114 (1992) 8552.

[56] R. Burch, S.E. Golunski, M.S. Spencer, Catal. Lett. 5 (1990) 55.

[57] L.C. Grabow, M. Mavrikakis, ACS Catal. 1 (2011) 365.

[58] H. Nakano, I. Nakamura, T. Fujitani, J. Nakamura, J. Phys. Chem. B 105 (2001) 1355.

[59] E. Vesselli, M. Rizzi, L. De Rogatis, X.L. Ding, A. Baraldi, G. Comelli, L. Savio, L. Vattuone, M. Rocca, P. Fornasiero, A. Baldereschi, M. Peressi, J. Phys. Chem. Lett. 1 (2010) 402.

[60] C.R. Chang, Y.G. Wang, J. Li, Nono Res. 1 (2011) 131.