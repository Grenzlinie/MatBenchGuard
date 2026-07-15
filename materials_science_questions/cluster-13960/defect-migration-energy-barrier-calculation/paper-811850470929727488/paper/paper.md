# Computer simulation of intrinsic defects in $\text{YAlO}_3$ single crystal

Jianyu Chen $^{a,b}$, Guangjun Zhao $^{a,*}$, Dunhua Cao $^{a,b}$, Qin Dong $^{a,b}$, Yutong Ding $^{a,b}$, Shengming Zhou $^{a}$

$^{a}$ Key Laboratory of High Power Laser Materials, Shanghai Institute of Optical and Fine Mechanics, Chinese Academy of Sciences, No. 390, Qinghe Road, Jia Ding District, Shanghai 201800, PR China
$^{b}$ Graduate School of the Chinese Academy of Sciences, Beijing 100039, PR China

---

## ARTICLE INFO

**Article history:**
Received 30 August 2008
Received in revised form
6 May 2009
Accepted 15 May 2009

**PACS:**
61.72.Bb
61.72.Hh
61.72.Ji
61.82.Ms

**Keywords:**
$\text{YAlO}_3$ crystal
Intrinsic defects
Redox reaction
Activation energy

---

## ABSTRACT

Computer simulation techniques were used to investigate intrinsic defects in $\text{YAlO}_3$ single crystal. A set of short-range potential parameters were derived using a relaxed fitting procedure incorporating with the known crystal properties. These parameters were then applied within the framework of the shell model. The simulation results reveal that oxygen Frenkel disorder and the antisite defect of Al ion substituting the Y ion dominate the intrinsic defects in $\text{YAlO}_3$. An analysis of redox reactions corroborate that the oxidation is most likely to occur via forming interstitial oxygen, while the oxidation via filling oxygen vacancies and reduction reaction may predominate at high temperature. The activation energy of oxygen vacancy migration on conduction was also studied.

© 2009 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Yttrium orthoaluminate single crystal, $\text{YAlO}_3$ (YAP), with a perovskite-like orthorhombic structure ($a=5.330\,\text{Å}$, $b=7.375\,\text{Å}$, $c=5.180\,\text{Å}$; space group Pnma-$D_{2\text{h}}^{16}$) [1] is a host material exhibiting high thermal conductivity and hardness [2]. YAP single crystals doped with rare-earth and transition metal ions are prospective materials for laser engineering, scintillators, holographic recording, data storage and substrate materials for thin films of high temperature superconductors [3–12]. As laser crystals, Nd, Tm, Ho, etc. rare-earth ions doped YAP crystals have the advantages of the line polarized laser output and high laser efficiency compared with the same rare-earth ions doped well-known YAG host [5–7]; Ce:YAP single crystal characterized by high light yield and very short decay time is an excellent scintillator which can be employed in various gamma ray and light particle detections [8,9]; Mn doped YAP crystal was shown to be a promising material for use in holographic recording and optical data storage [10–12].

Defects appearing in crystals during crystal growth process (nonstoichiometric, unintentional impurities, growth atmosphere, etc.) and under different external stimuli (irradiation, thermal treatment, etc.) have great influence on the crystal properties, e.g., the color center absorption bands are the "footprint" of defects. As for YAP host matrix, although the nature of color centers which degrades the crystal radiation hardness and the light output in "pure" and doped YAP has been undertaken for several decades [13–18], some basic properties on defects are still debated.

YAP crystals as-grown in inert atmosphere are generally clear and easily colored by irradiation at wavelengths $\leq$280 nm [13]. The coloration which could be reduced by annealing is ascribed to a very broad band with a peak at about 450 nm. Schirmer et al. suggest it to be caused by optical absorption of bound small polarons [14], whereas Li et al. proposed that the color change of YAP after thermal treatment is ascribed to oxygen vacancies and electron trap $\text{O}^-$ centers produced in crystal growth process due to the charge compensation [15]. Antisite defects that Al and Y ions are interchanged are proposed to be associated with the trap states seen in thermoluminescence that degrade the scintillator performance of YAP [16]. Besides the deviation of crystal composition from stoichiometry [17], another possible reason for the color center formation in as-grown YAP crystals is the impurities ($\text{Na}^+$, $\text{K}^+$, $\text{Li}^+$, $\text{Ca}^{2+}$, $\text{Mg}^{2+}$, $\text{Fe}^{3+}$, $\text{Cr}^{4+}$, etc.). So it is suggested that except for single points defects (cation and anion

---

* Corresponding author.
E-mail addresses: zhaoguangjun@163.net, giep2008@163.com, maomaochen2008@yahoo.com.cn (G. Zhao).

0921-4526/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.physb.2009.05.028

vacancies, antisite defects), more complex defect clusters (defect pairs) are formed in crystals. Irradiation and anneal treatments can change the charge state of point defects and impurities in crystal [18].

However, color center models aforementioned are not gen- erally accepted owning to the shortage of direct experimental evidences. Therefore, the resolution to clarify the intrinsic point defects mechanisms in YAP crystal is rather important, which can offer useful references to refine the crystal growth techniques and to improve the performances of rare-earth or transition metal ions doped YAP crystals for laser, scintillation and date-recording applications.

Atomistic computer simulation method is based on standard static lattice energy minimization techniques which has been extensively employed many ternary oxides [19-21]. Very recently, Kuklja [22] has investigated the defects in YAG and YAP crystals using completely the same group of potential parameters. However, it is not reasonable to use the same potential parameters to simulation because the structure and properties of YAG and YAP are totally different. It is necessary to use more reliable potential parameters based on the experimental data and to give more elaborate intrinsic defects simulation in YAP.

## 2. Methods of simulation

The lattice simulations are performed using the freeware General Utility Lattice Program (GULP) [23] based upon the Mott-Littleton methodology for accurate modeling of perfect and defect lattices. The program GULP [23-25] optimizes the structure with respect to the asymmetric unit fractional coordinates and cell strains, using analytical symmetry-adapted first and second derivatives within a Newton-Raphson procedure starting from the exact Hessian matrix.

An important feature of these calculations is the modeling of defects. The simplification of the Mott-Littleton method is to divide the crystal lattice that surrounds the defect into three regions known as 1, 2a, and 2b [23,26,27] as is shown in Fig. 1. In the inner region 1, all the interactions are treated at an atomistic level and the ions are explicitly allowed to relax in response to the defect, while the remainder of the crystal, where the defect forces are relatively weak, is treated by more approximate quasi- continuum methods. In this way, local relaxation is effectively modeled and the crystal is not considered simply as a rigid lattice through which ion species diffuse. In this study, the inner defect region is set as $8.5\mathring{A}$, which is found to be adequate for the convergence of the energies in simulation.

![](./images/811850470929727488_1.jpg)

Fig. 1. Mott-Littleton method deals with the lattice relaxation around a defect.

Calculations on both the perfect and defect lattices are formulated within the framework of the Born-like model [28]. The potential describing the interactions between two ions is expressed as a function of the distance $r$:

$$
U_{ij}=\frac{Z_{i}Z_{j}e^{2}}{r}+A\exp\left(\frac{-r}{\rho}\right)-\frac{C}{r^{6}}
$$

where the first term is the long-range Coulombic and the others are the short-range in terms of the two-body Buckingham form. $Z_{i}$ is the formal charge of atom $i$. $A$, $\rho$, and $C$ are the adjustable parameters.

Because charged defects will polarize other ions in lattice, ionic polarizability $(\alpha)$ is also incorporated into the potential model. A shell model treatment of such effects [29] is described in terms of a shell with charge Y connected with an isotropic harmonic spring of force constant $k$ to a massive core of charge $Z-Y$, namely

$$
\alpha=\frac{Y^{2}}{k}
$$

A crucial test of any theoretical study on solid-state materials is the accurate simulation of the crystal structure. The unit cell of YAP crystal structure is shown in Fig. 2. The orthorhombic cell contains four formula units with two nonequivalent oxygen sites. The coordinates of the ions in the YAP unit cell are distorted from the positions of an ideal perovskite, and a monoclinic pseudo-cells representation is equally valid [30]. The short-range interaction parameters of YAP for the pairs such as oxygen-oxygen, oxygen-aluminum, and oxygen-yttrium are transferred directly from the libraries in GULP package. All the potential parameters are treated as variables in a "relax fitting" procedure [24] at normal condition (i.e. 300K and 1atm). The final resulted potential and shell model parameters are given in Table 1, which will be used in the following simulation.

![](./images/811850470929727488_2.jpg)

Fig. 2. Unite cell of YAP crystal structure.

<table><caption>Table 1 Empirically derived potential parameters used in YAP.</caption>
<tbody>
<tr>
<td colspan="4">(a) Short-range potential parameters</td>
</tr>
<tr>
<td>Interactions</td>
<td>A (eV)</td>
<td>$\rho$ (Å)</td>
<td>$C$ (eV Å⁶)</td>
</tr>
<tr>
<td>O²⁻–O²⁻</td>
<td>7763.013</td>
<td>0.277819</td>
<td>0.00000</td>
</tr>
<tr>
<td>O²⁻–Al³⁺</td>
<td>11590.781</td>
<td>0.203647</td>
<td>2.93523</td>
</tr>
<tr>
<td>O²⁻–Y³⁺</td>
<td>10510.057</td>
<td>0.250406</td>
<td>0.00000</td>
</tr>
<tr>
<td colspan="4">(b) Shell-parameters¹</td>
</tr>
<tr>
<td>Species</td>
<td>Y (e)</td>
<td colspan="2">$k$ (eV Å⁻²)</td>
</tr>
<tr>
<td>O²⁻</td>
<td>−2.815</td>
<td colspan="2">40.01</td>
</tr>
<tr>
<td>Al³⁺</td>
<td>2.980</td>
<td colspan="2">889.11</td>
</tr>
<tr>
<td>Y³⁺</td>
<td>3.151</td>
<td colspan="2">27077.90</td>
</tr>
<tr>
<td colspan="4">¹ Y and $k$ refer to the shell charge and harmonic force constant, respectively.</td>
</tr>
</tbody>
</table>

<table><caption>Table 2 Calculated and experimental parameters of perfect crystal of YAP.</caption>
<tbody>
<tr>
<td>Properties</td>
<td>Calculated</td>
<td>Experimental [1,31,32]</td>
</tr>
<tr>
<td>Lattice energy (eV/formula)</td>
<td>−155.92</td>
<td></td>
</tr>
<tr>
<td>Unit cell parameters (Å)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>a</td>
<td>5.3390</td>
<td>5.33</td>
</tr>
<tr>
<td>b</td>
<td>7.3727</td>
<td>7.375</td>
</tr>
<tr>
<td>c</td>
<td>5.1746</td>
<td>5.18</td>
</tr>
<tr>
<td>Interatomic distances (Å)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Y–Y</td>
<td>3.640</td>
<td>3.642</td>
</tr>
<tr>
<td>Al–Al</td>
<td>3.686</td>
<td>3.687</td>
</tr>
<tr>
<td>YAl₈-hexahedron</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Y–Al</td>
<td>3.145</td>
<td>3.184</td>
</tr>
<tr>
<td></td>
<td>3.234</td>
<td>3.236</td>
</tr>
<tr>
<td></td>
<td>3.023</td>
<td>3.015</td>
</tr>
<tr>
<td></td>
<td>3.471</td>
<td>3.475</td>
</tr>
<tr>
<td>AlO₆-octahedron</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Al–Oᵢ</td>
<td>1.899</td>
<td>1.901</td>
</tr>
<tr>
<td>Al–Oᵢᵢ</td>
<td>1.910</td>
<td>1.911</td>
</tr>
<tr>
<td></td>
<td>1.929</td>
<td>1.921</td>
</tr>
<tr>
<td>Y–O₁₂-polyhedron</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Y–Oᵢ</td>
<td>2.326</td>
<td>2.306</td>
</tr>
<tr>
<td></td>
<td>3.097</td>
<td>3.119</td>
</tr>
<tr>
<td></td>
<td>2.232</td>
<td>2.237</td>
</tr>
<tr>
<td></td>
<td>3.002</td>
<td>3.010</td>
</tr>
<tr>
<td>Y–Oᵢᵢ</td>
<td>2.495</td>
<td>2.480</td>
</tr>
<tr>
<td></td>
<td>3.268</td>
<td>3.262</td>
</tr>
<tr>
<td></td>
<td>2.266</td>
<td>2.283</td>
</tr>
<tr>
<td></td>
<td>2.567</td>
<td>2.570</td>
</tr>
<tr>
<td>Static dielectric constant ($\varepsilon_0$)</td>
<td>15.96</td>
<td>16.00</td>
</tr>
<tr>
<td>High-frequency dielectric contant ($\varepsilon_\infty$)</td>
<td>3.82</td>
<td>3.83</td>
</tr>
<tr>
<td>Density (g/cm³)</td>
<td>5.345</td>
<td>5.35</td>
</tr>
</tbody>
</table>

The comparison of the calculated parameters with experimental values is listed in Table 2. Satisfying agreement between the calculated results and the experimental ones can be found, which could be a good basis for further calculations.

## 3. Simulated results and discussions

### 3.1. Intrinsic defects

Energy calculations of intrinsic defects were performed on the isolated point defects (namely the vacancy and interstitial defects). In order to confirm the optimal position of interstitial oxygen in the crystal, decades of positions where the interstitial oxygen exist possibly are simulated in Fig. 2 and we take the position having lowest energy as the formation energy of interstitial oxygen. The most basic intrinsic defects are Frenkel and Schottky disorders and antisite defects in YAP crystals.

<table><caption>Table 3 Calculated energies of intrinsic defects in YAP.</caption>
<tbody>
<tr>
<td colspan="4">(a) Isolated point defects</td>
</tr>
<tr>
<td>Defect</td>
<td>Energy (eV)</td>
<td>Defect</td>
<td>Energy (eV)</td>
</tr>
<tr>
<td>$V_{\ddot{O}}$</td>
<td>18.87</td>
<td>$O'_{I}$</td>
<td>−44.34</td>
</tr>
<tr>
<td>$V'''_{Al}$</td>
<td>65.84</td>
<td>$Al_{I}^{\cdot\cdot}$</td>
<td>−53.67</td>
</tr>
<tr>
<td>$V'''_{Y}$</td>
<td>52.01</td>
<td>$Y_{I}^{\cdot\cdot}$</td>
<td>−31.42</td>
</tr>
<tr>
<td>$Y_{Al}$</td>
<td>16.71</td>
<td>$Al_{Y}$</td>
<td>−9.34</td>
</tr>
<tr>
<td colspan="4">(b) Frenkel and Schottky disorder</td>
</tr>
<tr>
<td>Frenkel-type</td>
<td>Energy (eV/defect)</td>
<td>Schottky-type</td>
<td>Energy (eV/defect)</td>
</tr>
<tr>
<td>Oxygen</td>
<td>−12.74</td>
<td>YAlO₃</td>
<td>3.71</td>
</tr>
<tr>
<td>Yttrium</td>
<td>10.30</td>
<td>Al₂O₃</td>
<td>3.54</td>
</tr>
<tr>
<td>Aluminum</td>
<td>6.09</td>
<td>Y₂O₃</td>
<td>3.81</td>
</tr>
</tbody>
</table>

Frenkel disorder formation involves the displacement of lattice ions to well separated interstitial sites. The values of "energy per defect" are the sum of the energies of the component defects divided by the number of defects; Schottky disorder describes processes in which vacancies are generated in stoichiometric proportions in the bulk of the crystal and the displaced ions constitute new components at the crystal surface. Isolated defects are assumed do not interact with each other. Using the isolated defect energies given in Table 3(a) we obtained the following energies of the aforementioned two types of disorders denoted by

$$
'YAlO_{3}' \rightarrow O'_{I} + V_{\ddot{O}} \tag{3.1}
$$

$$
'YAlO_{3}' \rightarrow Y_{I}^{\cdot\cdot} + V'''_{Y} \tag{3.2}
$$

$$
'YAlO_{3}' \rightarrow Al_{I}^{\cdot\cdot} + V'''_{Al} \tag{3.3}
$$

$$
'YAlO_{3}' \rightarrow V'''_{Y} + V'''_{Al} + 3V_{O^{\cdot\cdot}} + YAlO_{3} \tag{3.4}
$$

$$
'YAlO_{3}' \rightarrow 2V'''_{Y} + 3V_{O^{\cdot\cdot}} + Y_{2}O_{3} \tag{3.5}
$$

$$
'YAlO_{3}' \rightarrow 2V'''_{Al} + 3V_{O^{\cdot\cdot}} + Al_{2}O_{3} \tag{3.6}
$$

In order to work out the energies of reaction (3.5) and reaction (3.6), lattice energies ($E_{Y_{2}O_{3}}=-142.95$ eV and $E_{Al_{2}O_{3}}=-169.22$ eV) are needed which are calculated consistently using the parameters given in Table 1. The calculated formation energies per defect are presented in Table 3(b).

It can be noted from Table 3(b) that the oxygen Frenkel disorder has the lowest energy (−12.74 eV) which means it is the most possible defect existed in YAP. It is well known that oxygen components are the most active and can be moveable in oxides [33]. The color change of the YAP after annealing has been validated relating with the lattice oxygen exchange between the lattice oxygen and the oxygen gas at proper temperature [34]. The corresponding oxygen vacancy can also trap electron and to form F and F⁺ centers [15]. So the changes of the charge state of Frenkel disorder incorporated with other defects may responsible for the photochromic under anneal or irradiation treatment. The formation energies of yttrium and aluminum Frenkel disorders are considerably high so that the possibilities of their existence are very low. It may relate with the perovskite-like orthorhombic structure of YAP that Al ion locates at the center of practically regular AlO₆ octahedron and the Y ion locates at the center of YO₁₂ polyhedron. The positions of them are relatively stable and difficult to move and form vacancy.

With respect to the Schottky-type disorder formation from Eqs. (3.4)–(3.6), it can be seen that the discrepancy of the energies of the three Schottky defects in YAP is not evident and their

energies are higher than that of the oxygen Frenkel disorder. So high concentration of Schottky disorders are not expected at normal temperature. However, we expect that such defects would be formed largely at high temperature or as compensators for dopants which will be discussed in another paper.

Next, we consider two antisite disorders which are isolated Y on Al site ($Y_{Al}$) and isolated Al on Y site ($Al_Y$) in the cation sublattice. Their formation energies are 16.71 and $-9.34$ eV, respectively. So the antisite defect $Al_Y$ is more preferable existence than $Y_{Al}$ and is the most possible defect existed in YAP besides the oxygen Frenkel disorder. It can be interpreted by the fact that the ion radii of $Al^{3+}$ ($0.53\mathring{A}$) is a much smaller than that of $Y^{3+}$ ($1.02\mathring{A}$) in YAP, the smaller $Al^{3+}$ ion is easier to replace the bigger $Y^{3+}$ ion.

### 3.2. Redox reaction

It is important to consider the reaction of defects in response to the variation of oxygen partial pressure because the YAP crystals are often annealed in air or $H_2$ atmosphere to improve the crystal properties [34,35]. There are three relevant reactions: addition of oxygen (oxidation) by vacancy filling and hole formation [Eq. (3.7)]; oxidation by oxygen interstitial and hole formation [Eq. (3.8)]; loss of oxygen (reduction) with formation of oxygen vacancies and compensation with electrons [Eq. (3.9)]

$$
{}^{\text{'}} \text{YAlO}_{3}^{\prime}+\frac{1}{2} \mathrm{O}_{2}+V_{\mathrm{O}}^{\cdot} \rightarrow \mathrm{O}_{\mathrm{O}}^{\times}+2 \dot{h} \tag{3.7}
$$

$$
{}^{\text{'}} \text{YAlO}_{3}^{\prime}+\frac{1}{2} \mathrm{O}_{2} \rightarrow \mathrm{O}_{\mathrm{i}}^{\prime \prime}+2 \dot{h} \tag{3.8}
$$

$$
{}^{\text{'}} \text{YAlO}_{3}^{\prime} \rightarrow V_{\mathrm{O}}^{\cdot}+2 e^{\prime}+\frac{1}{2} \mathrm{O}_{2} \tag{3.9}
$$

In order to calculate the reaction energies of these equations, one should acquire the defect energies of the electronic defects (namely the hole and electron) first. To simplify the treatments, our approach regarding electronic defects follows from the method that has been successfully modeled in $\mathrm{PbWO}_{4}$ [19], $\mathrm{KTaO}_{3}$ [20], and $\mathrm{Ba}_{2}\ln_{2}\mathrm{O}_{5}$ [36] compounds. According to the *ab initio* calculation [37], the valence band of YAP consists mainly of the O 2p states while the conduction band of the Y 4d states. Therefore, we have modeled the hole ($\dot{h}$) as $\mathrm{O}^{-}$ species, whereas electron ($e'$) as $\mathrm{Y}^{2+}$ species.

When calculating electronic defect energy, only the large contribution due to the change in the Coloumbic interaction was taken into account. That is, the short-range interactions of $\mathrm{O}^{-}$ ion on $\mathrm{O}^{2-}$ lattice and $\mathrm{Y}^{2+}$ on $\mathrm{Y}^{3+}$ lattice that represent the species were taken to be the same as for the $\mathrm{O}^{2-}$ and $\mathrm{Y}^{3+}$ ion, respectively. Furthermore, interionic energy terms, such as the electron affinity of the $\mathrm{O}^{2-}$ ion ($EA_1=1.47$ eV, $EA_2=-8.75$ eV) [38], the oxygen molecule dissociation energy ($D_e=5.16$ eV) [19], and the ionization potential terms of Y atom [$IP_2=12.24$ eV, $IP_3=20.52$ eV] should also be taken into account. The specific values are listed in Table 4(a).

The resulting energies of redox reaction are listed in Table 4(b). Examination of these results shows that: (a) the oxidation reaction is mostly to occur via forming interstitial oxygen, whereas the oxidation via filling oxygen vacancies seems unlikely. (b) A comparison of the energies of oxidation and reduction indicates that the former reaction is more favorable. The high energy values suggest that the oxidation via filling oxygen vacancies and the reduction reaction can only predominate at high temperature. These results are in accord with the practical condition and the results of anneal experiments [15,17,34,35].

If the law of mass action was applied to the reaction (3.7) and (3.9), we can obtain the following relations, respectively

$$
\left(\frac{\partial \ln [\dot{h}]}{\partial \ln P_{\mathrm{O}_{2}}}\right)_{a \mathrm{YAlO}_{3}}=+\frac{1}{4} \tag{3.10}
$$

$$
\left(\frac{\partial \ln \left[e^{\prime}\right]}{\partial \ln P_{\mathrm{O}_{2}}}\right)_{a \mathrm{YAlO}_{3}}=-\frac{1}{4} \tag{3.11}
$$

Consequently, it is suggested that at low-oxygen pressures, the electronic conduction of YAP will be $n$ type, whereas at high-oxygen pressures the electronic conduction will be $p$ type. These conclusions are consistent with other oxides [19,39].

Note that from the calculated electron and hole energies we can also estimate the band gap of YAP. The dispersion between our calculated value for band gap (7.43 eV) and the experimental value (about 7.9 eV) [40] is small. This discrepancy due in part to the inadequacy in the (small polaron) treatment of hole and electron states; moreover, even if the strongly localized models are valid, the omission of ligand field splitting terms would cause some errors.

### 3.3. Oxygen vacancy migration

It has been well established that oxygen vacancy is mobile defect in oxide crystals [33,41-43]. However, the knowledge with respect to the nature of migration mechanism or pathway in YAP is vacant. Simulation methods can enhance our understanding of this problem by evaluating the activation energy of mobile oxygen ion.

For YAP, we estimated the activation energies by calculation the defect energies along the migration path between adjacent oxygen sites of $\mathrm{AlO}_{6}$ octahedron. In this way, activation energies for these different migration pathways were estimated by placing single oxygen ion in "transition" state, as if frozen in the act of jumping from one site to another [36]. The transition state was assumed to be the saddle-point of the energy surface between the initial and final sites of the migration ion. It is recognized that there are 12 pathways for oxygen vacancy migration, as shown in Fig. 3. The derived activation energies are reported in Table 5.

The results in Table 5 show that the oxygen vacancies along different pathways have different energy barriers which may be

<table>
<caption>Table 4 Energies of electronic defects and redox reactions of YAP.</caption>
<tbody>
<tr>
<td colspan="3">(a) Formation energies and electronic defect energies of isolated defects</td>
</tr>
<tr>
<td>Hole/electron states</td>
<td>Formation energie (eV)</td>
<td>Electronic defect energies (eV)</td>
</tr>
<tr>
<td>$\mathrm{O}^{-}(\dot{h})$</td>
<td>17.80</td>
<td>9.05</td>
</tr>
<tr>
<td>$\mathrm{Y}^{2+}(e')$</td>
<td>26.33</td>
<td>5.81</td>
</tr>
<tr>
<td colspan="4">(b) Reaction energies of redox reaction</td>
</tr>
<tr>
<td>Oxidation</td>
<td>Energy (eV)</td>
<td>Reduction</td>
<td>Energy (eV)</td>
</tr>
<tr>
<td>Eq. (3.7)</td>
<td>9.09</td>
<td>Eq. (3.9)</td>
<td>20.63</td>
</tr>
<tr>
<td>Eq. (3.8)</td>
<td>–16.38</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/811850470929727488_3.jpg)

Fig. 3. Schematic of the possible migration paths for oxygen vacancy along the AlO₆ octahedron edge.

<table>
<caption>Table 5<br>Oxygen migration activation energies in YAP.</caption>
<thead>
<tr>
<th>Jump path</th>
<th>ΔE (eV)</th>
<th>Jump path</th>
<th>ΔE (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1→2, 2→6</td>
<td>0.99</td>
<td>1→3, 3→6</td>
<td>0.52</td>
</tr>
<tr>
<td>1→4, 4→6</td>
<td>0.30</td>
<td>1→5, 5→6</td>
<td>0.15</td>
</tr>
<tr>
<td>2→3</td>
<td>0.31</td>
<td>3→4</td>
<td>0.69</td>
</tr>
<tr>
<td>4→5</td>
<td>0.29</td>
<td>5→2</td>
<td>0.69</td>
</tr>
</tbody>
</table>

originated from the distorted perovskite structure of YAP. The energy barriers (0.15–0.99 eV) are not high (<1.5 eV) and may have much contribution to conductivity. Furthermore, these different energies along different pathways imply the anisotropic conductivity of YAP.

### 4. Conclusions
The present atomistic computer simulation was employed to investigate the perovskite-like structure YAP crystal. An interionic potential model has been constructed according to the observed experimental parameters of YAP. Valuable results including the intrinsic defects, the redox behavior, as well as the transport properties of oxygen vacancy migration have been obtained. The following conclusions have emerged from our discussions.

(1) The predominant intrinsic defect is oxygen Frenkel disorder in YAP crystal.
(2) The antisite defect of Al on Y site (Alᵧ) is more preferable existence than Y on Al site (Yₐₗ). The antisite defect Alᵧ is the most possible defects existed in YAP crystal besides the oxygen Frenkel disorder.
(3) Based on the redox reactions, the oxidation is most likely to occur via forming interstitial oxygen; while the oxidation via filling oxygen vacancies and reduction only predominate at high temperature.
(4) Oxygen vacancy migration was responsible for ionic conduction in YAP crystal and the oxygen vacancy migration along different pathways has different energy barriers which caused by the anisotropic of YAP crystal.

### Acknowledgment
This work was financially supported by the National Science Foundation of China (Grant no. 60607015).

### References
[1] R. Diehl, G. Brandt, Mater. Res. Bull. 10 (1975) 85.
[2] J. Kvapil, J. Kubelka, R. Autrata, Cryst. Res. Technol. 18 (1983) 127.
[3] D.M. Bercha, K.Z. Rushchanskii, M. Sznajder, A. Matkovskii, P. Potera, Phys. Rev. B 66 (2002) 195203.
[4] P. Potera, L. Grigorjeva, A. Matkovskii, D. Millers, T. Lukasiewicz, Z. Galazka, T. Wojciechowski, Radiation Meas. 38 (2004) 371.
[5] C.K. Duan, P.A. Tanner, V.N. Makhov, M. Kirm, Phys. Rev. B 75 (2007) 195130.
[6] S. Yiou, F. Balembois, P. Georges, A. Brun, Appl. Opt. 40 (2001) 3019.
[7] N. Garnier, R. Moncorge, H. Manaa, E. Descroix, P. Laporte, Y. Guyot, J. Appl. Phys. 79 (1996) 4323.
[8] S. Baccaro, K. Blazek, F. de Notaristefani, P. Maly, J.A. Marser, R. Pani, R. Pellegrini, A. Soluri, Nucl. Instrum. Methods Phys. Res. A 361 (1995) 209.
[9] M. Kapusta, J. Pawelke, M. Moszynski, Nucl. Instrum. Methods Phys. Res. A 404 (1998) 413.
[10] G.B. Loutts, M. Warren, L. Taylor, R.R. Rakhimov, H.R. Ries, G. Miller, M.A. Noginov, M. Curley, N. Noginova, N. Kukhtarev, H.J. Caulfield, P. Venkates- warlu, Phys. Rev. B 57 (1998) 3706.
[11] M.A. Noginov, G.B. Loutts, J. Opt. Soc. Amer. B 16 (1999) 3.
[12] M.A. Noginov, G.B. Loutts, M. Warren, J. Opt. Soc. Amer. B 16 (1999) 475.
[13] M.J. Weber, M. Bass, K. Andringa, R.R. Monchamp, E. Comperchio, Appl. Phys. Lett. 15 (1969) 342.
[14] O.F. Schirmer, K.W. Blazey, W. Berlinger, R. Diehl, Phys. Rev. B 11 (1975) 4201.
[15] T. Li, G.J. Zhao, X.M. He, J. Xu, S.K. Pan, J. Synthetic Crystals 31 (2002) 456.
[16] D.J. Singh, Phys. Rev. B 76 (2007) 214115.
[17] J. Kvapil, B. Perner, B. Manek, K. Blazek, Z. Hendrich, Cryst. Res. Technol. 20 (1985) 473.
[18] D. Sugak, A. Matkovskii, D. Savitskii, A. Durygin, A. Suchocki, Y. Zhydachevskii, I. Solskii, I. Stefaniuk, F. Wallrafen, Phys. Stat. Sol. (a) 184 (2001) 239.
[19] Q.S. Lin, X.Q. Feng, Z.Y. Man, Phys. Rev. B 63 (2001) 134105.
[20] M. Exner, H. Donnerberg, C.R.A. Catlow, O.F. Schirmer, Phys. Rev. B 52 (1995) 3930.
[21] G.V. Lewis, C.R.A. Catlow, J. Phys. Chem. Solids 47 (1986) 89.
[22] M.M. Kuklja, J. Phys. Condens. Matter 12 (2000) 2953.
[23] N.F. Mott, M.J. Littleton, Trans. Faraday Soc. 34 (1938) 485.
[24] J.D. Gale, General Utility Lattice Program, Imperial College, London, 1996.
[25] J.D. Gale, Philos. Mag. B 73 (1996) 3.
[26] C.R.A. Catlow, J. Chem. Soc. Faraday Trans. 2 85 (1989) 335.
[27] A.B. Lidiard, J. Chem. Soc. Faraday Trans. 2 85 (1989) 341.
[28] M. Born, Atomtheorie des Festen Zustandes, Teubner, Leipzig, Berlin, 1923.
[29] B.J. Dick, A.W. Overhauser, Phys. Rev. 112 (1958) 90.
[30] S. Geller, E.A. Wood, Acta Crystallogr. 9 (1956) 563.
[31] X. Gonze, C. Lee, Phys. Rev. B 55 (1997) 10355.
[32] H. Asano, S. Kubo, O. Michikami, M. Satoh, T. Konaka, Japan. J. Appl. Phys. 29 (1990) L1452.
[33] Z.J. Qu, C.Y. Yu, W.Z. Li, Y.X. Chen, Acta Phys. Chimica Sinica 10 (1994) 796.
[34] X.H. Zeng, G.J. Zhao, J. Xu, X.M. He, J. Appl. Phys. 95 (2004) 749.
[35] H. Bernhardt, Phys. Stat. Sol. (a) 21 (1974) 95.
[36] C.A.J. Fisher, M.S. Islam, R.J. Brook, J. Solid State Chem. 128 (1997) 137.
[37] W.Y. Ching, Y.N. Xu, Phys. Rev. B 59 (1999) 12815.
[38] M.S. Islam, M. Leslie, S.M. Tomlinson, C.R.A. Catlow, J. Phys. C 21 (1988) L109.
[39] Z.X. Shao, Q.R. Zhang, T.Y. Liu, J.Y. Chen, Nucl. Instrum. Methods Phys. Res. B 266 (2008) 797.
[40] Y.V. Zorenko, A.S. Voloshinovskii, I.V. Konstankevych, Opt. Spectroscopy 96 (2004) 532.
[41] W. Van Loo, J. Solid State Chem. 14 (1975) 359.
[42] J.A. Groenink, H. Binsma, J. Solid State Chem. 29 (1979) 227.
[43] M.S. Islam, L.J. Winch, Phys. Rev. B 52 (1995) 10510.