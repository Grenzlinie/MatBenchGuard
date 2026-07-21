# DFT study on the sulfurization mechanism during the desulfurization of $H_2S$ on the ZnO desulfurizer

Lixia Ling $^{a,b}$, Riguang Zhang $^{c}$, Peide Han $^{b}$, Baojun Wang $^{c,*}$

$^{a}$ Research Institute of Special Chemicals, Taiyuan University of Technology, Taiyuan 030024, Shanxi, PR China
$^{b}$ College of Materials Science and Engineering, Taiyuan University of Technology, Taiyuan 030024, Shanxi, PR China
$^{c}$ Key Laboratory of Coal Science and Technology (Taiyuan University of Technology), Ministry of Education and Shanxi Province, Taiyuan 030024, Shanxi, PR China

---

## ARTICLE INFO

**Article history:**
Received 16 April 2012
Received in revised form 1 August 2012
Accepted 1 August 2012
Available online 9 September 2012

**Keywords:**
Sulfurization mechanism
$H_2S$
ZnO surface
Density functional theory

---

## ABSTRACT

The sulfurization mechanism of $H_2S$ on the $ZnO(10\overline{1}0)$ surface during the desulfurization of coal gas was investigated by using periodic density functional theory (DFT) calculations. The adsorption of $H_2S$, SH, atomic S, and atomic H, as well as the coadsorption of SH and an H atom, and the coadsorption of S and two H atoms, were initially examined to identify energetically favorable intermediates. Potential energy profiles for three paths of $H_2S-ZnO(10\overline{1}0)$ interactions producing $H_2$ and $H_2O$ were obtained, respectively. Our results show that $H_2S$ is preferred to dissociatively adsorb on the $ZnO(10\overline{1}0)$ surface, followed by dehydrogenation process to form sulfur species. Molecular-level calculations demonstrate that $H_2O$ formation via the $H_2S-ZnO$ interaction is the most probable reaction pathway both kinetically and thermodynamically. ZnO has double functions during the desulfurization of $H_2S$. One is as a catalyst to accelerate the dissociation of $H_2S$, while the other is as the reactant participating in the reaction of $H_2S$ with ZnO to form $H_2O$.

© 2012 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Sulfur compounds including $H_2S$ need to be reduced to low levels in natural gas, chemical synthesis gas and coal-derived fuel gas due to their negative effects on environment and chemical processing [1,2]. Metal oxides as candidate desulfurization sorbents have been investigated as desulfurizers for the removal of $H_2S$ [3-7]. Of the various oxides available, ZnO is known as a highly efficient desulfurizer [8-11]. A fundamental understanding of the interaction of $H_2S$ with ZnO is important by reason that ZnO can reduce the concentration of $H_2S$ to a few parts per million [12-14].

Sulfurization is the first process in desulfurization, which determines the desulfurization efficiency. Adsorption is the precondition of sulfurization. Experimental results show that $H_2S$ adsorption progresses via the chemical reaction of sulfide formation. In this system, a reaction takes place between the gas-phase reactant and the solid surface [15,16]: $H_2S+ZnO\rightarrow H_2O+ZnS$. A more detailed study shows that ZnO is able to dissociate $H_2S$ at very low temperatures [17]. Adsorption of molecules on this oxide at approximately 100 K produces only Zn-bonded HS species, which decompose into S atoms at temperatures between 300 and 400 K. The reaction between $H_2S$ and ZnO at elevated temperatures of 400 K to 500 K produces $H_2O$ and ZnS: $H_2S_{(gas)}+ZnO_{(solid)}\rightarrow H_2O_{(gas)}+ZnS_{(solid)}$ [18,19]. Furthermore, the apparent kinetics of $H_2S$ removal by ZnO has been investigated via thermogravimetric analysis [20], and an activation energy of $19.32\ \mathrm{kJ{\cdot}mol^{-1}}$ has been obtained. An activation energy of $30.31\ \mathrm{kJ{\cdot}mol^{-1}}$ for the reaction between $H_2S$ and ZnO was obtained by Westmoreland et al. [21]. To date, experimental data on the sulfurization process, including each elementary step, are insufficient. Therefore, theoretical calculations will be helpful in elucidating the mechanism of this process. With the development of quantum chemistry, the density functional theory (DFT) method has already been extensively used to provide qualitative and quantitative insights into the structure of active surfaces, as well as into the surface reactions [22-24]. Rodriguez et al. [12] studied the adsorption and dissociation of $H_2S$ on the ZnO(0001) surface using first-principles density-functional calculations (DFT-GGA) and a periodic supercell, which showed that the strong bonding of $H_2S$ and its S-containing dissociated species (HS and S) on the ZnO(0001) surface facilitate the dissociation. Casarin et al. [25] studied $H_2S$ adsorption on the $ZnO(10\overline{1}0)$ surface by using a local DFT coupled with the molecular-cluster approach, including molecular and dissociative adsorptions. They found that the dissociative chemisorption of $H_2S$ on the relaxed $ZnO(10\overline{1}0)$ is highly favored. Desulfurizer is a special material, which has double roles during the desulfurization of $H_2S$. One is that desulfurizers have catalytic capacity to dissociate $H_2S$. The other is that desulfurizers participate in the desulfurization reaction as a reactant. However, only the adsorption processes of $H_2S$ on ZnO surfaces have been studied, the detailed interaction between $H_2S$ and the ZnO surface remains unclear, and the formation

---

* Corresponding author at: No. 79 Yingze West Street, Taiyuan 030024, PR China.
Tel.: +86 351 6018239; fax: +86 351 6041237.
E-mail address: wangbaojun@tyut.edu.cn (B. Wang).

0378-3820/$ - see front matter © 2012 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.fuproc.2012.08.001

mechanism of the probable products is unknown. More importantly, the two roles of ZnO in the desulfurization process have not yet been elucidated.

In this study, the ZnO(10$\overline{1}$0) surface is chosen as the study surface because it is electrostatically stable and is shown to be the main surface of ZnO [26]. The adsorption of H₂S and dissociated species on the ZnO(10$\overline{1}$0) surface, as well as the coadsorption of different dissociated species are discussed. The first-principles DFT and self-consistent periodic calculation are applied to systematically investigate the adsorption energies and adsorption geometries systematically. Meanwhile, the interaction of H₂S with the ZnO(10$\overline{1}$0) surface is discussed to obtain the sulfurization mechanism of ZnO, which is important to illustrate the desulfurization process of ZnO. The two roles of ZnO during the dusulfurization of H₂S are further analyzed in detailed.

## 2. Computational modes and methods

### 2.1. Calculation methods

We have performed periodic density functional calculations using the Dmol³ program [27,28]. The PW91 gradient-corrected GGA functional of Perdew and Wang [29,30] was employed, which can give much better dissociation energies [31] and adsorption energies [32]. It is now widely used in molecular calculations. The double-numeric quality basis set with polarization functions (DNP) was used. The size of the DNP basis set was comparable to that of Gaussian 6-31 G **. The inner electrons of Zn atoms were kept frozen and replaced by an effective core potential (ECP), and other atoms in this study were treated with an all-electron basis set. Brillouin-zone integrations were performed using a 4×2×1 Monkhorst-Pack grid [33]. A Fermi smearing of 0.005 hartree and a real-space cutoff of 4.4 Å were used to improve the computational performance. Spin polarization was considered in all calculations. The tolerances of energy, force, and displacement convergence were 2×10⁻⁵ hartree, 4×10⁻³ hartree/Å, and 5×10⁻³ Å, respectively. All calculations were performed on an HP Proliant DL 380 G5 server system.

### 2.2. Surface models

The ZnO(10$\overline{1}$0) surface was modeled using a 6-layer slab and a p(2×2) supercell. The slab was periodically repeated in the x-y directions with a 1 nm vacuum region between the slabs in the z-direction. The optimized ZnO(10$\overline{1}$0) surface is shown in Fig. 1. The O and Zn atoms on the first layer are labeled, and hexagonal channels are composed of atoms in the first and second layers. In all calculations, the bottom two layers of the slab were kept fixed at their bulk-like position, whereas the remaining atoms in the top four layers, as well as the adsorbed molecules or atoms, were allowed to relax. Considering that the effect of layers on the surface and the electronic coupling between adjacent slabs, an 8-layer slab model and a larger model p(3×2) supercell were used in calculating the adsorption energy of H₂S on the ZnO(10$\overline{1}$0) surface. Our results show that the energy differences were only 1.29 and 3.12 kJ·mol⁻¹, corresponding to the 6-layer slab with p(2×2) supercell, respectively.

![](./images/813282798398865410_1.jpg)

Fig. 1. ZnO(10$\overline{1}$0) surface optimized by the GGA-PW91 functional.

The adsorption energies, $E_{\text{ads}}$, are calculated as follows:

$$
E_{\text{ads}} = E_{\text{tot}}(\text{ads}) + E_{\text{tot}}(\text{slab}) - E_{\text{tot}}(\text{ads/slab}) \tag{1}
$$

where $E_{\text{tot}}(\text{ads})$ is the total energy of the free adsorbate in the gas phase, $E_{\text{tot}}(\text{slab})$ is the total energy of the bare slab, and $E_{\text{tot}}(\text{ads/slab})$ is the total energy of the slab with adsorbate in its equilibrium geometry. By this definition, a positive $E_{\text{ads}}$ value corresponds to an exothermic adsorption. Furthermore, the more positive the $E_{\text{ads}}$ is, the stronger the adsorption is.

Transition state (TS) search was performed at the same theoretical level with the complete linear synchronous transit/quadratic synchronous transit (LST/QST) method [34]. In this method, the LST maximization was performed, followed by an energy minimization in the directions that conjugate to the reaction pathway to obtain an approximated TS. The approximated TS was used to perform QST maximization, followed by another conjugated gradient minimization. The cycle was repeated until a stationary point was located. TS confirmation is performed on every transition state structure to confirm that they lead to the desired reactants and products using the nudged elastic band (NEB) method.

The reaction energy ($\Delta E$) and the activation energy ($E_{\text{a}}$) are defined as follows:

$$
\Delta E = E_{(\text{P})} - E_{(\text{R})} \tag{2}
$$

$$
E_{\text{a}} = E_{(\text{TS})} - E_{(\text{R})} \tag{3}
$$

where $E_{(\text{P})}$ is the energy of the product in each reaction, $E_{(\text{R})}$ is the energy of the reactant in each reaction, and $E_{(\text{TS})}$ is the energy of the transition state in each elementary reaction.

## 3. Results and discussion

### 3.1. Calculations of H₂S molecule and ZnO

The accuracy of the computational method used in this study has been tested by describing the properties of H₂S molecule in gas phase and the lattice constants of bulk ZnO. The bond length and bond angle of molecular H₂S calculated by our approach are 0.1354 nm and 91.34°, which are in good agreement with the experimental values of 0.1336 nm and 92.12° [35], respectively. The calculated values for the lattice parameters of bulk ZnO are $a = b = 0.3306$ nm and $c = 0.5326$ nm in comparison with the experimental value of $a = b = 0.3249$ nm and $c = 0.5205$ nm [36]. The largest deviations in the calculated values from the experimental ones are only 1.75% and 2.32%, respectively. The calculated lattice constants are also in good agreement with other similar GGA results [37]. The calculated ZnO bond length is 0.2036 nm in bulk, which shortens by 0.0148 nm to become 0.1888 nm in the surface. The surface Zn atom relaxes inward, whereas the O atom expands, resulting in a buckling of the surface layer and tilting angle ($\theta$) is 9.899°, which is consistent with previously reported GGA-PW91 results [38], as well as the experimental results of Duke et al. [39]. They concluded from their best low-energy electron diffraction analysis that the top-layer Zn ion is displaced downward by $\Delta d(\text{Zn}) = -0.045 \pm 0.01$ nm and likewise the top-layer oxygen by $\Delta d(\text{O}) = -0.005 \pm 0.01$ nm, leading to a $12^{\circ} \pm 5^{\circ}$ tilt of the Zn-O dimer. Above results obtained in these tests make us confident in pursuing the next step of our investigations.

### 3.2. Adsorption of single species on the ZnO(10$\overline{1}$0) surface

The adsorbed structures of single species involved in the desulfurization of H₂S are shown in Fig. 2, and the main bond lengths and the adsorption energies are listed in Table 1.

![](./images/813282798398865410_2.jpg)

Fig. 2. The geometric structures of $H_2S$, SH, S and H on the $ZnO(10\overline{1}0)$ surface optimized by the GGA-PW91 functional.

### 3.2.1. $H_2S$ adsorption
When $H_2S$ is placed on the top of Zn1 with S atom, two H atoms face O3 and O4 in the initial structure, the optimized structure is $H_2S(a)$ (in Fig. 2). We can see that the $H_2S$ molecule is dissociatively adsorbed on the $ZnO(10\overline{1}0)$ surface, consistent with the experimental observations [17]. The adsorption energy is $131.58\ \text{kJ·mol}^{-1}$, and the $S-H1$ bond is elongated to 0.2211 nm corresponding to 0.1354 nm of $H_2S$ in gas phase. The other adsorption structure is molecular, $H_2S(b)$, in which two H atoms are toward O1 and O2. The adsorption energy is $51.00\ \text{kJ·mol}^{-1}$, which is lower than that of $H_2S(a)$. The dissociative adsorption of $H_2S$ is thus clearly favorable. Casarin et al. [25] have also studied $H_2S$ adsorption on the $ZnO(10\overline{1}0)$ surface with the cluster model. They found that $H_2S$ is preferred to dissociatively adsorb on the $ZnO(10\overline{1}0)$ surface. The experimental studies by Galtayries et al. [5] show the same results about the dissociative adsorption of $H_2S$ on the $Cu_2O(111)$ surface using X-ray photoelectron spectroscopy (XPS) and ion scattering spectroscopies (ISS). However, both the molecular and dissociative interactions are investigated during $H_2S$ adsorption by Casarin et al. [40]. Only the molecular adsorption of $H_2S$ on the perfect $Cu_2O(111)$ surface is obtained in our recently study [41], and the dissociative adsorption of $H_2S$ occurs predominantly on the oxygen-vacancy surface. $H_2O$ is similar in structure to $H_2S$, but has a different adsorption state. The results show that a $H_2O$ is fully molecularly adsorbed on the $ZnO(10\overline{1}0)$ surface with $p(2\times2)$ supercell, however partial dissociation may be possible at elevated temperatures or coverage of $H_2O$ molecules [42-44].

### 3.2.2. SH adsorption
Initially, two stable configurations [SH(a) and SH(b)] of SH adsorption on the $ZnO(10\overline{1}0)$ surface are obtained. In SH(a), the S atom is bonded to two Zn atoms of surface in the adjacent hexagonal channels via the bridge bond mode, while the H atom lies toward the direction of O3 and O4. The two $S-Zn$ bonds are 0.2441 and 0.2439 nm, respectively, and the adsorption energy is $142.21\ \text{kJ·mol}^{-1}$. SH(b) is similar to the SH(a), with nearly similar $S-Zn$ bond lengths and adsorption energies. The only difference between the two structures is that the H atom in

<table>
<caption>Table 1
The properties of single species adsorbed on the ZnO(10$\overline{1}$0) surface with different adsorption modes calculated from the GGA-PW91 functional.</caption>
<thead>
<tr>
<th>
</th>
<th>
r(S$-$Zn1)
</th>
<th>
r(S$-$H1)
</th>
<th>
r(S$-$H2)
</th>
<th>
r(S$-$Zn2)
</th>
<th>
r(S$-$O3)
</th>
<th>
r(S$-$O1)
</th>
<th>
r(H$-$O)
</th>
<th>
$E_{\text{ads}}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
H₂S(a)
</td>
<td>
0.2323
</td>
<td>
0.2211
</td>
<td>
0.1356
</td>
<td>
0.4397
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
131.58
</td>
</tr>
<tr>
<td>
H₂S(b)
</td>
<td>
0.2557
</td>
<td>
0.1368
</td>
<td>
0.1354
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
51.00
</td>
</tr>
<tr>
<td>
SH(a)
</td>
<td>
0.2441
</td>
<td>
0.1358
</td>
<td>
</td>
<td>
0.2439
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
142.21
</td>
</tr>
<tr>
<td>
SH(b)
</td>
<td>
0.2443
</td>
<td>
0.1358
</td>
<td>
</td>
<td>
0.2439
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
140.14
</td>
</tr>
<tr>
<td>
SH(c)
</td>
<td>
0.2299
</td>
<td>
0.1376
</td>
</td>
<td>
0.4258
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
121.74
</td>
</tr>
<tr>
<td>
S(a)
</td>
<td>
0.2374
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
0.1825
</td>
<td>
</td>
<td>
</td>
<td>
198.86
</td>
</tr>
<tr>
<td>
S(b)
</td>
<td>
0.2353
</td>
<td>
</td>
<td>
</td>
<td>
0.2348
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
123.16
</td>
</tr>
<tr>
<td>
S(c)
</td>
<td>
0.2253
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
0.1748
</td>
<td>
</td>
<td>
211.82
</td>
</tr>
<tr>
<td>
H(a)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
0.0975
</td>
<td>
265.14
</td>
</tr>
<tr>
<td>
H(b)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
75.81
</td>
</tr>
</tbody>
</table>

Note: the unit of bond length is nm, and the unit of $E_{\text{ads}}$ is kJ·mol⁻¹.

SH(b) is toward the direction of O1 and O2. The adsorption mode of the S bonded to two adjacent Zn atoms via the bridge bond is similar to the adsorption of SH on other metal surfaces [45,46]. However, this finding is not consistent with the result of Casarin et al. [25], who found that the S of SH was bonded to one Zn atom via a single bond. Therefore, the SH(c) was also investigated in this study. The calculated adsorption energy is 121.74 kJ·mol⁻¹, which is 20.47 and 18.40 kJ·mol⁻¹ lower than those of SH(a) and SH(b), respectively. It can be concluded that SH(a) and SH(b) are the stable adsorption configurations of SH on the ZnO(10$\overline{1}$0) surface.

### 3.2.3. S adsorption
The S atom adsorption on the ZnO(10$\overline{1}$0) surface for three modes (see Fig. 2) has also been investigated. S(a) is the S atom bridging Zn1 and O3 in a hexagonal channel, and the bond lengths of S$-$Zn1 and S$-$O3 are 0.2374 and 0.1825 nm, respectively. S(b) is the S atom bonded to two adjacent Zn atoms of the surface via the bridge bond mode, the two S$-$Zn bonds are 0.2353 and 0.2348 nm in length, respectively. S(c) is the S atom bridging Zn1 and O1 in a Zn-O bond, the bond lengths of S$-$Zn1 and S$-$O1 are 0.2253 and 0.1748 nm, respectively.

From the calculated adsorption energies listed in Table 1, the strengths of atomic S adsorption over the three types of adsorption sites are ranked in the following order: S(c)$>$S(a)$>$S(b). It is clear that the S atom bridging a Zn$-$O bond is the most stable configuration for single S atom adsorption.

### 3.2.4. H adsorption
Regarding H adsorption, we optimized two configurations on the O- and Zn-top sites [H(a) and H(b)]. The H atom preferentially adsorbs on the O-top site with an adsorption energy of 265.14 kJ·mol⁻¹ and H$-$O distance of 0.0975 nm. For H adsorption on the Zn-top site, the adsorption energy is only 75.81 kJ·mol⁻¹, which is less stable than that of H(a) by 189.33 kJ·mol⁻¹. Thus the O-top site in metal oxides is found to be the stable site for H adsorption, which is in agreement with other theoretical result [47], and also in accordance with H atom adsorption on other metal oxide surfaces [24,48].

### 3.3. Coadsorption of dissociated species on the ZnO(10$\overline{1}$0) surface
In order to investigate the desulfurization process of H₂S on the ZnO(10$\overline{1}$0) surface, it is necessary to investigate the coadsorption of dissociated species of H₂S, namely, the coadsorption of SH and H, as well as the coadsorption of S, H and H, respectively. The main bond lengths and coadsorption energies are listed in Table 2.

#### 3.3.1. SH and H coadsorption
As above mentioned, two stable adsorption structures of SH on the ZnO(10$\overline{1}$0) surface are obtained. Based on these two configurations, two coadsorption configurations of SH and H on the ZnO(10$\overline{1}$0) surface were investigated, see SH$+$H(a) and SH$+$H(b) in Fig. 3. It can be seen that H atom is located at the O-top site on the ZnO(10$\overline{1}$0) surface, and SH is bonded to two Zn atoms of surface in the adjacent hexagonal channels via the S atom. This behavior is similar to that observed for the stable adsorption mode of single species. SH$+$H(a) is the H of SH lies toward the direction of the adsorbed H atom, whereas SH$+$H(b) lies toward the opposite direction. There is only a difference of 4.60 kJ·mol⁻¹ in coadsorption energy.

#### 3.3.2. S, H and H coadsorption
As shown in Fig. 3, the most stable coadsorption structure is that two H atoms are on the two O atoms of surface in two adjacent hexagonal channels, and the S atom adsorbs on two Zn atoms in the adjacent hexagonal channels via the bridge bond mode, while this adsorption mode of single S atom is the most unstable. S$+$2 H(a) is especially noted, the original structure is S atom bridging Zn and O based on S(a), and two H atoms placed on the O-top sites. After optimization, the S atom adsorbs on two adjacent Zn atoms with bridge bond mode. S$+$2 H(a) and S$+$2 H(b) have similar structure, the difference is that S and two H atoms coadsorb on two adjacent Zn$-$O bonds in S$+$2 H(a), while in S$+$2 H(b), the coadsorbed S and H atoms are placed on two adjacent hexagonal channels. The difference of coadsorption energy is 49.62 kJ·mol⁻¹. S$+$2 H(c) is the optimized structure of the most stable adsorption of single S atom S(c) combining with two H atoms, the coadsroption energy is 656.19 kJ·mol⁻¹, which is the most unstable in the three coadsorption configurations.

<table>
<caption>Table 2
The properties of dissociated species coadsorbed on the ZnO(10$\overline{1}$0) surface with different adsorption modes calculated from the GGA-PW91 functional.</caption>
<thead>
<tr>
<th>
</th>
<th>
r(S$-$Zn1)
</th>
<th>
r(S$-$H2)
</th>
<th>
r(S$-$Zn2)
</th>
<th>
r(S$-$O1)
</th>
<th>
r(H1$-$O3)
</th>
<th>
r(H2$-$O4)
</th>
<th>
$E_{\text{ads}}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
SH$+$H(a)
</td>
<td>
0.2467
</td>
<td>
0.1358
</td>
<td>
0.2455
</td>
<td>
</td>
<td>
0.0974
</td>
<td>
</td>
<td>
507.34
</td>
</tr>
<tr>
<td>
SH$+$H(b)
</td>
<td>
0.2453
</td>
<td>
0.1355
</td>
<td>
0.2456
</td>
<td>
</td>
<td>
0.0975
</td>
<td>
0.2737
</td>
<td>
511.94
</td>
</tr>
<tr>
<td>
S$+$2 H(a)
</td>
<td>
0.2307
</td>
<td>
</td>
<td>
0.2310
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
901.17
</td>
</tr>
<tr>
<td>
S$+$2 H(b)
</td>
<td>
0.2393
</td>
<td>
0.2381
</td>
<td>
0.2393
</td>
<td>
</td>
<td>
0.0999
</td>
<td>
0.0999
</td>
<td>
851.55
</td>
</tr>
<tr>
<td>
S$+$2 H(c)
</td>
<td>
0.2244
</td>
<td>
</td>
<td>
</td>
<td>
0.1808
</td>
<td>
0.0978
</td>
<td>
0.0977
</td>
<td>
656.19
</td>
</tr>
</tbody>
</table>

Note: the unit of bond length is nm, and the unit of $E_{\text{ads}}$ is kJ·mol⁻¹

![](./images/813282798398865410_3.jpg)

Fig. 3. The coadsorption structures of dissociated species of $H_2S$ on the $ZnO(10\overline{1}0)$ surface optimized by the GGA-PW91 functional.

![](./images/813282798398865410_4.jpg)

Fig. 4. The structures of transition states and products obtained by the GGA-PW91 functional.

<table><thead><tr><td colspan="9"><b>Table 3 The bond length of transition states and products adsorbed on the ZnO(1010) surface calculated from the GGA-PW91 functional. (nm).</b></td></tr><tr><td></td><td><b>r(S−Zn1)</b></td><td><b>r(S−H1)</b></td><td><b>r(S−H2)</b></td><td><b>r(S−Zn2)</b></td><td><b>r(H1−O3)</b></td><td><b>r(H2−O4)</b></td><td><b>r(S−O1)</b></td><td><b>r(H1−H2)</b></td></tr></thead><tbody><tr><td><b>TS1</b></td><td><b>0.2327</b></td><td><b>0.2875</b></td><td><b>0.1342</b></td><td><b>0.3335</b></td><td><b>0.0993</b></td><td><b>0.3009</b></td><td></td><td></td></tr><tr><td><b>TS2</b></td><td><b>0.2653</b></td><td><b>0.2569</b></td><td><b>0.1642</b></td><td><b>0.2416</b></td><td><b>0.0993</b></td><td><b>0.1397</b></td><td></td><td></td></tr><tr><td><b>TS3</b></td><td><b>0.2418</b></td><td></td><td><b>0.2308</b></td><td><b>0.2400</b></td><td><b>0.2109</b></td><td></td><td></td><td><b>0.0763</b></td></tr><tr><td><b>P1</b></td><td><b>0.2351</b></td><td></td><td></td><td><b>0.2349</b></td><td><b>0.3025</b></td><td><b>0.3296</b></td><td></td><td><b>0.0751</b></td></tr><tr><td><b>TS4</b></td><td><b>0.2168</b></td><td></td><td></td><td><b>0.3708</b></td><td><b>0.0972</b></td><td><b>0.0971</b></td><td><b>0.2318</b></td><td></td></tr><tr><td><b>TS5</b></td><td><b>0.2255</b></td><td></td><td></td><td></td><td><b>0.2089</b></td><td><b>0.0995</b></td><td><b>0.1790</b></td><td><b>0.1799</b></td></tr><tr><td><b>P2</b></td><td><b>0.2252</b></td><td></td><td></td><td></td><td><b>0.3780</b></td><td><b>0.2658</b></td><td><b>0.1749</b></td><td><b>0.0753</b></td></tr><tr><td><b>TS6</b></td><td><b>0.2238</b></td><td></td><td></td><td></td><td><b>0.1249</b></td><td><b>0.0976</b></td><td><b>0.1782</b></td><td><b>0.1917</b></td></tr><tr><td><b>P3</b></td><td><b>0.2306</b></td><td></td><td></td><td></td><td><b>0.5147</b></td><td><b>0.1009</b></td><td><b>0.1743</b></td><td><b>0.1567</b></td></tr></tbody></table>

### 3.4. Reaction mechanism of $H_{2}S-ZnO(10\overline{1}0)$ interactions

To characterize the probable reaction pathways of $H_{2}S$ on the ZnO(1010) surface, we applied energetically the most stable adsorption configuration $H_{2}S(a)$ as the reactant. According to the reaction process, the coadsorption configuration SH + H(a), the coadsorption configuration S + 2 H(b) and S + 2 H(c) are selected as intermediates. Fig. 4 shows the optimized structures of the transition states and products, their partial bond lengths are listed in Table 3. Fig. 5 shows the potential energy profiles for the interaction of $H_{2}S$ with the ZnO(1010) surface. The relative energy of each configuration to the reactant is also listed, and the reaction energies $(\Delta E)$ and activation energy $(E_{a})$ of each elementary reaction can be obtained according to Eqs. (2) and (3). In Path 1, $H_{2}S$ is dissociatively adsorbed on the ZnO(1010) surface without a tight transition state. This is the first dehydrogenation process. However, $H_{2}S$ is weakly molecularly bound to the $CeO_{2}(111)$ surface with a binding energy of $14.65~kJ\cdot mol^{-1}$, then a little energy barrier of $7.95~kJ\cdot mol^{-1}$ is needed for the first dehydrogenation by the DFT calculation [24]. On the $Cu_{2}O(111)$ surface, an energy barrier of $52.40~kJ\cdot mol^{-1}$ is needed to overcome [41]. The bond dissociation energy of $H-SH$ is about $381.40~kJ\cdot mol^{-1}$ [49] in gas, indicating that ZnO has the catalytic effect on the dissociation of $H_{2}S$. It is the first role of ZnO during the desulfurization of $H_{2}S$. S atom bonds to Zn with single bond, which is unstable according to the above calculation of SH adsorption. The S atom in SH changes the adsorption mode via TS1 leading to SH + H(a) with a small activation energy of $35.66~kJ\cdot mol^{-1}$. In this configuration, the S atom bridges two Zn atoms in two adjacent hexagonal channels. The SH species is an important reactive intermediate, which has also been investigated by FT-IR in the interaction of $H_{2}S$ with $\alpha-Fe_{2}O_{3}$ [50]. This step of SH changing the adsorption mode is endothermic by $6.13~kJ\cdot mol^{-1}$. The bond length of $S-Zn1$ elongates from 0.2323 nm in dissociative $H_{2}S$ molecule via 0.2327 nm in TS1 to 0.2467 nm in SH + H(a), while the $S-Zn2$ bond shortens from 0.4397 nm in $H_{2}S(a)$ via 0.3335 nm in TS1 to 0.2455 nm in SH + H(a). Then the second dehydrogenation step takes place from SH + H(a) to S + 2 H(b). H2 transfers from S to O4 by overcoming a reaction energy barrier of $51.47~kJ\cdot mol^{-1}$ at TS2, producing S + 2 H(b) with a reaction energy of $20.75~kJ\cdot mol^{-1}$ compared to SH + H(a). The energy barriers of $35.17~kJ\cdot mol^{-1}$ and $82.70~kJ\cdot mol^{-1}$ are needed for the second dehydrogenation of $H_{2}S$ on the $CeO_{2}(111)$ surface [24] and $Cu_{2}O(111)$ surface [42], respectively. At the transition state TS2, the breaking $S-H$ and forming $O-H$ bonds in TS2 are 0.1642 and 0.1397 nm, respectively. Finally, S + 2 H(b) can undergo an $H_{2}$ forming process giving P1. However, the TS confirmation calculation shows that an intermediate similar to SH + H(a) existed in this step, which suggests that an $H_{2}$ molecule can be directly formed by SH + H(a). The formation of P1 via TS3 from SH + H(a) is investigated, and an activation energy of $318.99~kJ\cdot mol^{-1}$ is needed, which suggests that this pathway is less favorable. In P1, the distances between H1 and O3, and between H2 and O4 are 0.3025 and 0.3296 nm, which show that the interaction between the formed $H_{2}$ and the ZnO surface is negligible; The S atom is adsorbed on two Zn atoms in the adjacent hexagonal channels via the bridge bond mode, which is the most unstable structure of single S adsorption. Thus, other pathways are investigated, and the results are discussed in the subsequent paragraphs.

Path 2 has steps which are different from Path1. $H_{2}S(a)$ undergoes dehydrogenation steps to S + 2 H(b) via the intermediate SH + H(a). Starting from S + 2 H(b), the S atom changes the adsorption mode from bridging two adjacent Zn atoms to bonding to a $Zn-O$ bond via the bridge bond mode, leading to S + 2 H(c) via TS4 with a reaction barrier of $219.97~kJ\cdot mol^{-1}$, which is $99.02~kJ\cdot mol^{-1}$ lower than that of the $SH + H(a)\to P1$ step. The breaking $S-Zn2$ and forming $S-O1$ bonds are 0.3708 nm and 0.2318 nm in TS4, respectively. S + 2 H(c) is converted

![](./images/813282798398865410_5.jpg)

Fig. 5. Potential energy profiles for the interaction of $H_{2}S$ and ZnO(1010) surface. The energies are relative to that of the adsorption structure of $H_{2}S$, calculated from the GGA-PW91 functional.

![](./images/813282798398865410_6.jpg)

Fig. 6. Potential energy profiles for the $H_{2}O$-forming pathway. The energies are relative to that of the adsorption structure of $H_{2}S$, calculated from GGA-PW91, GGA-BLYP and LDA-PWC functionals. The black line, red line and blue line denote the calculated results at the GGA-PW91, the GGA-BLYP and the LDA-PWC levels, respectively.

to P2 leading to final products $H_{2}$ and $S$ adsorbing on the $ZnO(10\overline{1}0)$ surface via a transition state TS5 involving the bonds H1-O3 and H2 -O4 cleavage. TS5 is predicated to be $199.45~kJ\cdot mol^{-1}$ higher in energy than $S+2H(c)$, which is $119.54~kJ\cdot mol^{-1}$ lower than that of the $SH+H(a)\to P1$ step.

In Path 3, all of the steps are identical to those in Path 2 except for the last step. $H_{2}$ is eliminated from $S+2H(c)$ in Path 2, whereas in Path 3, two HO surface species in $S+2H(c)$ can undergo H-migration via TS6 with a small reaction barrier of $97.55~kJ\cdot mol^{-1}$, leading to the formation of a $H_{2}O$-containing P3 product via an exothermic process of $55.77~kJ\cdot mol^{-1}$. $H_{2}O$ is also investigated as the final product in the interaction of $H_{2}S$ with other metal oxides, such as $Fe_{2}O_{3}$ [48], CoO [51], $Cu_{2}O$ [5]. In this step, the distance between H1-O3 increases from 0.0978 nm in $S+2H(c)$ via 0.1249 nm in TS6 to 0.5147 nm in P3. Due to the formation of an $H_{2}O$ species, an oxygen vacancy is generated in the surface. The oxygen vacancies on the $WO_{3}$ surface during the interaction of $H_{2}S$ and $WO_{3}$ have also been investigated via XPS, as well as via ultra-high vacuum (UHV) and ultraviolet photoelectron spectroscopy (UPS) [52,53]. During the formation of $H_{2}O$, ZnO acts as a reactant participating in the reaction of $H_{2}S$ with ZnO, which is the second role of ZnO during the desulfurization of $H_{2}S$.

From Fig. 5, we can see that the total reaction energy of the $H_{2}O$-forming path is $166.47~kJ\cdot mol^{-1}$, which is the lowest among all three paths. This result shows that the $H_{2}O$-forming path is the most thermodynamically favorable. From the kinetic point of view, the activation energy of the step $(SH+H(a)\to P1)$ is $318.99~kJ\cdot mol^{-1}$, which is the highest in Path 1. Therefore, this step is the rate determining step in Path 1. While in Path 2 and 3, the same rate determining step $(S+2H(b)\to S+2H(c))$ is overcome, the activation energy is $219.97~kJ\cdot mol^{-1}$, which is $99.02~kJ\cdot mol^{-1}$ less than that of Path 1. In addition, a high energy of $421.69~kJ\cdot mol^{-1}$ is needed in TS5 for Path 2. So the $H_{2}O$-forming process is the most favorable reaction pathway for the $H_{2}S-ZnO$ interaction both kinetically and thermodynamically. The results are similar to those obtained from the interaction of $H_{2}S$ with the $CeO_{2}(111)$ surface, which shows that the $H_{2}O$-forming pathway is also energetically more favorable than the $H_{2}$-forming pathway [24].

### 3.5. Comparison of different functionals

To investigate the influence of different functionals on the study results, the adsorption energy of $H_{2}S$ on the $ZnO(10\overline{1}0)$ surface and the potential energies in the $H_{2}O$-forming pathway have been calculated using the GGA-PW91, GGA-BLYP (generalized gradient approximation with the Becke-Lee-Yang-Parr), and LDA-PWC (local spin density approximation with the Perdew-Wang correlational) functionals.

The adsorption energies of $H_{2}S$ on the $ZnO(10\overline{1}0)$ surface are 131.58, 108.34 and $171.62~kJ\cdot mol^{-1}$ at the GGA-PW91, GGA-BLYP, and LDA-PWC functional levels, respectively. It can be seen that the energy difference between the GGA-PW91 and GGA-BLYP functionals is little, whereas the LDA-PWC adsorption energy is 40.04 and $63.28~kJ\cdot mol^{-1}$ higher than those of GGA-PW91 and GGA-BLYP, respectively. Obviously, the LDA approximation often overestimates the adsorption energy [54].

As the energetically favorable path, the $H_{2}O$-forming pathway during the interaction of $H_{2}S$ and $ZnO(10\overline{1}0)$ surface has been selected to determine the influence of different functionals. Every equilibrium structure has been optimized, and the transition states are searched at the GGA-BLYP and LDA-PWC levels, which can be seen in the supplemental materials. A comparison of the potential energies at the three functional levels is shown in Fig. 6. We can see that the three functionals have little influence on the bond lengths of all structures. The different functionals yield nearly similar results for the relative reaction energy. The rate determining step for all functionals is $S+2H(b)\to S+2H(c)$, and the activation energies at the GGA-PW91, GGA-BLYP and LDA-PWC levels are 219.97, 192.56 and $227.48~kJ\cdot mol^{-1}$, respectively.

In summary, the different functionals have influence on the adsorption energy. In particular, LDA approximation often overestimates the adsorption energy. However, the effects of these functionals on the relative reaction energy are negligible.

## 4. Conclusions

Using the DFT method, a periodic slab model study has been carried out to investigate the adsorption of three types of sulfur-containing species ($H_{2}S$, SH and atomic S) and atomic H, as well as the coadsorption of SH and H, and of S and two H. The interaction of $H_{2}S$ with $ZnO(10\overline{1}0)$ was also investigated. The results show that the dissociative adsorption of $H_{2}S$ molecule on the $ZnO(10\overline{1}0)$ surface is preferred, which is in agreement with experimental observations [17]. The most stable configuration for SH adsorption on the $ZnO(10\overline{1}0)$ surface is that the S atom is bonded to two adjacent Zn atoms of the surface via the bridge bond mode. The S atom bridging a Zn-O bond is the most stable configuration for single S atom adsorption. The H atom is preferentially adsorbed on the O-top site on the $ZnO(10\overline{1}0)$ surface.

In the coadsorption structure of SH and H, the adsorption sites are the same as the sites of SH and H adsorption separately. In the coadsorption

structure of S and 2H, the most stable structure is that the S atom is adsorbed on two adjacent Zn atoms via the bridge bond mode, and two H atoms are located on the O-top sites. However, this adsorption mode of single S atom is the most unstable.

Finally, the potential energy profiles for the $\mathrm{H}_{2} \mathrm{S}-\mathrm{ZnO}(10 \overline{1} 0)$ interactions have been obtained. The surface adsorbates formed through the dehydrogenation processes can further eliminate $\mathrm{H}_{2}$, or react with oxygen anions to form $\mathrm{H}_{2} \mathrm{O}$. According to our calculations, the $\mathrm{H}_{2} \mathrm{O}$-forming via $\mathrm{H}_{2} \mathrm{S}-\mathrm{ZnO}$ interaction is the most probable reaction route both kinetically and thermodynamically. The same conclusions can be obtained when different functional levels are used.

ZnO has double roles during the desulfurization of $\mathrm{H}_{2} \mathrm{S}$, one is as a catalyst to accelerate the dissociation of $\mathrm{H}_{2} \mathrm{S}$, and the other is as the reactant participating in the reaction of $\mathrm{H}_{2} \mathrm{S}$ with $\mathrm{ZnO}$ leading to the formation of $\mathrm{H}_{2} \mathrm{O}$. It is the first reason that the desulfurizer is different from the catalyst. The second reason is that an oxygen vacancy is generated in the surface during the formation of $\mathrm{H}_{2} \mathrm{O}$, and $\mathrm{S}$ of $\mathrm{H}_{2} \mathrm{S}$ can be deposited on the surface leading to the loss of sulfurization activity of $\mathrm{ZnO}$, but which can be regenerated in oxidational atmosphere to prolong the lifetime of $\mathrm{ZnO}$.

In addition, sulfurization and regeneration are two important processes for the desulfurization, both of which determine the desulfurization efficiency and lifetime of $\mathrm{ZnO}$. The regeneration mechanisms of the sulfurized and oxygen-deficient $\mathrm{ZnO}(10 \overline{1} 0)$ surfaces in the presence of $\mathrm{O}_{2}$ will be investigated in subsequent studies.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant No. 20976115), the National Younger Natural Science Foundation of China (Grant Nos. 21103120, 20906066), the Doctoral Fund of Ministry of Education (Grant No. 20091402110013) and the Younger Foundation of Shanxi Province (No. 2009021015).

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx.doi.org/10.1016/j.fuproc.2012.08.001.

## References

[1] S. Cheah, D.L. Carpenter, K.A. Magrini-Bair, Review of mid- to high-temperature sulfur sorbents for desulfurization of biomass- and coal-derived syngas, Energy and Fuels 23 (2009) 5291-5307.

[2] W.F. Elseviers, H. Verelst, Transition metal oxides for hot gas desulphurization, Fuel 78 (1999) 601-612.

[3] M.S. Najjar, D.Y. Jung, High temperature desulfurization of synthesis gas with iron compounds, Fuel Processing Technology 44 (1995) 173-180.

[4] R.B. Slimane, J. Abbasian, Utilization of metal oxide-containing waster materials for hot coal gas desulfurization, Fuel Processing Technology 70 (2001) 97-113.

[5] A. Galtayries, J.-P. Bonnelle, XPS and ISS studies on the interaction of $\mathrm{H}_{2} \mathrm{S}$ with polycrystalline $\mathrm{Cu}, \mathrm{Cu}_{2} \mathrm{O}$ and $\mathrm{CuO}$ surfaces, Surface and Interface Analysis 23 (1995) 171-179.

[6] R. Agnihotri, S.S. Chauk, S.K. Mahuli, L.-S. Fan, Mechanism of CaO reaction with $\mathrm{H}_{2} \mathrm{S}$: diffusion through CaS product layer, Chemical Engineering Science 54 (1999) 3443-3453.

[7] J.A. Rodriguez, T. Jirsak, M. Pérez, S. Chaturvedi, M. Kuhn, L. González, A. Maiti, Studies on the behavior of mixed-metal oxides and desulfurization: reaction of $\mathrm{H}_{2} \mathrm{S}$ and $\mathrm{SO}_{2}$ with $\mathrm{Cr}_{2} \mathrm{O}_{3}(0001), \mathrm{MgO}(100)$, and $\mathrm{Cr}_{x} \mathrm{Mg}_{1-x} \mathrm{O}(100)$, Journal of the American Chemical Society 122 (2000) 12362-12370.

[8] M. Xue, R. Chitrakar, K. Sakane, K. Ooi, Screening of adsorbents for removal of $\mathrm{H}_{2} \mathrm{S}$ at room temperature, Green Chemistry 5 (2003) 529-534.

[9] I.I. Novochinskii, C.S. Song, X.L. Ma, X.S. Liu, L. Shore, J. Lampert, R.J. Farrauto, Low-temperature $\mathrm{H}_{2} \mathrm{S}$ removal from steam-containing gas mixtures with $\mathrm{ZnO}$ for fuel cell application. 1. ZnO particles and extrudates, Energy and Fuels 18 (2004) 576-583.

[10] H.Y. Yang, R. Sothen, D.R. Cahela, B.J. Tatchuk, Breakthrough characteristics of reformate desulfurization using ZnO sorbents for logistic fuel cell power systems, Industrial and Engineering Chemistry Research 47 (2008) 10064-10070.

[11] R.P. Gupta, B.S. Turk, J.W. Portzer, D.C. Cicero, Desulfurization of syngas in a transport reactor, Environmental Progress 20 (2001) 187-195.

[12] J.A. Rodriguez, A. Maiti, Adsorption and decomposition of $\mathrm{H}_{2} \mathrm{S}$ on $\mathrm{MgO}(100)$, $\mathrm{NiMgO}(100)$, and $\mathrm{ZnO}(0001)$ surfaces: A first-principles density functional study, The Journal of Physical Chemistry. B 104 (2000) 3630-3638.

[13] J.B. Gibson III, D.P. Harrison, The reaction between hydrogen sulfide and spherical pellets of zinc oxide, Industrial & Engineering Chemistry Process Design and Development 19 (1980) 231-237.

[14] Y.X. Li, H.X. Guo, C.H. Li, S.B. Zhang, A study on the apparent kinetics of $\mathrm{H}_{2} \mathrm{S}$ removal using a ZnO-MnO desulfurizer, Industrial and Engineering Chemistry Research 36 (1997) 3982-3987.

[15] I. Rosso, C. Galletti, M. Bizzi, G. Saracco, V. Specchia, Zinc oxide sorbents for the removal of hydrogen sulfide from syngas, Industrial and Engineering Chemistry Research 42 (2003) 1688-1697.

[16] P. Courty, A. Deschamps, S. Franckowiak, A. Sugier, Process for purifying a gas containing hydrogen sulfide and contact masses usable therefor, US patent no. 4088736 (1978).

[17] J. Lin, J.A. May, S.V. Didziulis, E.I. Solomon, Variable-energy photoelectron spectroscopic studies of $\mathrm{H}_{2} \mathrm{S}$ chemisorption on $\mathrm{Cu}_{2} \mathrm{O}$ and $\mathrm{ZnO}$ single-crystal surfaces: $\mathrm{HS}^{-}$bonding to copper(I) and zinc(II) sites related to catalytic poisoning, Journal of the American Chemical Society 114 (1992) 4718-4727.

[18] J. Evans, J.M. Corker, C.E. Hayter, R.J. Oldman, B.P. Williams, In situ sulfur K-edge X-ray absorption spectroscopy of the reaction of zinc oxide with hydrogen sulfide, Chemical Communications 12 (1996) 1431-1432.

[19] S.S. Tamhankar, M. Bajajewlcz, G.R. Gavalas, P.K. Sharma, M. Flytzani-Stephanopoulos, Mixed-oxide sorbents for high-temperature removal of hydrogen sulfide, Industrial & Engineering Chemistry Process Design and Development 25 (1986) 429-437.

[20] H.L. Fan, Y.X. Li, C.H. Li, H.X. Guo, K.C. Xie, The apparent kinetics of $\mathrm{H}_{2} \mathrm{S}$ removal by zinc oxide in the presence of hydrogen, Fuel 81 (2002) 91-96.

[21] P.R. Westmoreland, D.P. Harrison, Evaluation of candidate solids for high-temperature desulfurization of low-Btu gases, Environmental Science and Technology 10 (1976) 659-661.

[22] M.Y. Sun, A.E. Nelson, J. Adjaye, Adsorption and dissociation of $\mathrm{H}_{2}$ and $\mathrm{H}_{2} \mathrm{S}$ on $\mathrm{MoS}_{2}$ and NiMoS catalysts, Catalysis Today 105 (2005) 36-43.

[23] J.A. Rodriguez, S. Chaturvedi, M. Kuhn, J. Hrbek, Reaction of $\mathrm{H}_{2} \mathrm{S}$ and $\mathrm{S}_{2}$ with Metal/Oxides surfaces: Band-gap size and chemical reactivity, The Journal of Physical Chemistry. B 102 (1998) 5511-5519.

[24] H.-T. Chen, Y.M. Choi, M.L. Liu, M.C. Lin, A first-principles analysis for sulfur tolerance of $\mathrm{CeO}_{2}$ in solid oxide fuel cells, Journal of Physical Chemistry C 111 (2007) 11117-11122.

[25] M. Casarin, C. Maccato, A. Vittadini, An LCAO-LDF study of the chemisorption of $\mathrm{H} 2 \mathrm{O}$ and $\mathrm{H} 2 \mathrm{S}$ on $\mathrm{ZnO}(0001)$ and $\mathrm{ZnO}(10 \overline{1} 0)$, Surface Science 377-379 (1997) 587-591.

[26] A. Wander, N.M. Harrison, An ab initio study of $\mathrm{ZnO}(10 \overline{1} 0)$, Surface Science 457 (2000) L342-L346.

[27] B. Delley, Form molecules to solids with the Dmol $^{3}$ approach, Journal of Chemical Physics 113 (2000) 7756-7764.

[28] B. Delley, An all-electron numerical method for solving the local density functional for polyatomic molecules, Journal of Chemical Physics 92 (1990) 508-517.

[29] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Physical Review Letters 77 (1996) 3865-3868.

[30] J.P. Perdew, K. Burke, Y. Wang, Generalized gradient approximation for the exchange-correlation hole of a many-electron system, Physical Review B 54 (1996) 16533-16539.

[31] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Atom, molecules, solids, and surfaces: applications of the generalized gradient approximation for exchange and correlation, Physical Review B 46 (1992) 6671-6687.

[32] P. Hu, D.A. King, S. Crampin, M.H. Lee, M.C. Payne, Gradient corrections in density functional theory calculations for surfaces: CO on Pd(110), Chemical Physics Letters 230 (1994) 501-506.

[33] R.G. Zhang, H.Y. Liu, H.Y. Zheng, L.X. Ling, Z. Li, B.J. Wang, Adsorption and dissociation of $\mathrm{O}_{2}$ on the $\mathrm{Cu}_{2} \mathrm{O}(111)$ surface: Thermochemistry reaction barrier, Applied Surface Science 257 (2011) 4787-4794.

[34] T.A. Halgren, W.N. Lipscomb, The synchronous-transit method for determining reaction pathways and locating molecular transition states, Chemical Physics Letters 49 (1977) 225-232.

[35] D.R. Lide, in: Handbook of Chemistry and Physics, CRC Press, Boca Raton, 2001-2002, pp. 9-21, 82nd.

[36] H. Sawada, R. Wang, A.W. Sleight, An electron density residual study of zinc oxide, Journal of Solid State Chemistry 122 (1996) 148-150.

[37] M.J.S. Spencer, K.W.J. Wong, I. Yarovsky, Density functional theory modelling of $\mathrm{ZnO}(10 \overline{1} 0)$ and $\mathrm{ZnO}(2110)$ surfaces: structure, properties and adsorption of N2O, Materials Chemistry and Physics 119 (2010) 505-514.

[38] B. Meyer, D. Marx, Density-functional study of the structure and stability of ZnO surfaces, Physical Review B 67 (2003) 035403-1-11.

[39] C.B. Duke, R.J. Meyer, A. Paton, P. Mark, Calculation of low-energy-electron-diffraction intensities from $\mathrm{ZnO}(10 \overline{1} 0)$. II. Influence of calculational procedure, model potential, and second-layer structural distortions, Physical Review B 18 (1978) 4225-4240.

[40] M. Casarin, C. Maccato, N. Vigato, A. Vittadini, A theoretical study of the $\mathrm{H}_{2} \mathrm{O}$ and $\mathrm{H}_{2} \mathrm{S}$ chemisorption on $\mathrm{Cu}_{2} \mathrm{O}(111)$, Applied Surface Science 142 (1999) 164-168.

[41] R.G. Zhang, H.Y. Liu, J.R. Li, L.X. Ling, B.J. Wang, A mechanistic study of $\mathrm{H}_{2} \mathrm{S}$ adsorption and dissociation on $\mathrm{Cu}_{2} \mathrm{O}(111)$ surfaces: thermochemistry, reaction barrier, Applied Surface Science 258 (2012) 9932-9943.

[42] B. Meyer, H. Rabaa, D. Marx, Water adsorption on $\mathrm{ZnO}(10 \overline{1} 0)$: from single molecules to partially dissociated monolayers, Physical Chemistry Chemical Physics 8 (2006) 1513-1520.

[43] A. Calzolari, A. Catellani, Water adsorption on nonpolar $\mathrm{ZnO}(10 \overline{1} 0)$ surface: a microscopic understanding, Journal of Physical Chemistry C 113 (2009) 2896-2902.

[44] Y.F. Yan, M.M. Al-Jassim, Structure and energetics of water adsorbed on the ZnO(10$\overline{1}$0) sueface, Physical Review B 72 (2005) 235406.

[45] M.P. Hyman, B.T. Loveless, J.W. Medlin, A density functional theory study of H₂S decomposition on the (111) surfaces of model Pd-alloys, Surface Science 601 (2007) 5382-5393.

[46] D.R. Alfonso, First-principles studies of H₂S adsorption and dissociation on metal surfaces, Surface Science 602 (2008) 2758-2768.

[47] P. Zapol, J.B. Jaffe, A.C. Hess, Ab initio study of hydrogen adsorption on the ZnO(10 $\overline{1}$0) surface, Surface Science 422 (1999) 1-7.

[48] X.R. Ren, L.P. Chang, F. Li, K.C. Xie, Study of intrinsic sulfidation behavior of Fe₂O₃ for high temperature H₂S removal, Fuel 89 (2010) 883-887.

[49] Y.R. Luo, in: Handbook of Bond Dissociation Energy, Science Press, Beijing, 2005, p. 263.

[50] A. Davydov, K.T. Chuang, A.R. Sanger, Mechanism of H₂S oxidation by ferric oxide and hydroxide surfaces, The Journal of Physical Chemistry. B 102 (1998) 4745-4752.

[51] E. Auschitzky, A.B. Boffa, J.M. White, T. Sahin, Adsorption of H₂O and H₂S on thin films of cobalt oxide supported on alumina, Journal of Catalysis 125 (1990) 325-334.

[52] B. Frühberger, M. Grunze, D.J. Dwyer, Surface chemistry of H₂S-sensitive tungsten oxide films, Sensors and Actuators B 31 (1996) 167-174.

[53] D.J. Dwyer, Surface chemistry of gas sensors: H₂S on WO₃ films, Sensors and Actuators B 5 (1991) 155-159.

[54] Y.J. Xu, J.Q. Li, Y.F. Zhang, W.K. Chen, CO adsorption on MgO(001) surface with oxygen vacancy and its low-coordinated surface sites: embedded cluster model density functional study employing charge self-consistent technique, Surface Science 525 (2003) 13-23.