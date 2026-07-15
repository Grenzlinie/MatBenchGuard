# Point defects engineering in graphene/h-BN bilayer:
## A first principle study

Jianmei Yuan $^{a}$, Zhe Wei $^{b}$, Jianxin Zhong $^{b}$, Yanping Huang $^{b}$, Yuliang Mao $^{b,c,*}$

$^{a}$ Hunan Key Laboratory for Computation and Simulation in Science and Engineering, Faculty of Mathematics and Computational Science, Xiangtan University, Hunan 411105, People's Republic of China
$^{b}$ Hunan Key Laboratory for Micro-Nano Energy Materials and Devices, Faculty of Physics and Optoelectronic Engineering, Xiangtan University, Hunan 411105, People's Republic of China
$^{c}$ State Key Laboratory of Silicon Materials, Zhejiang University, Hangzhou 310027, People's Republic of China

---

### ARTICLE INFO

**Article history:**
Received 17 July 2014
Received in revised form
16 September 2014
Accepted 17 September 2014
Available online 28 September 2014

**PACS:**
71.15.Mb
73.20.At
75.75.+a

**Keywords:**
Graphene
h-BN
Hetero-bilayer
Point defect

### ABSTRACT

Point defects engineering in a new type hetero bilayer consisting of graphene and hexagonal boron-nitrogen (h-BN) sheet, including vacancy, substitutional C/B/N doping and the possible combinations of the former two, was theoretically studied using first-principles calculations. The optimized geometry, formation energy, magnetic moment, and electronic property of these systems are discussed. It was found that N vacancy is more likely to form than B vacancy in graphene/h-BN bilayer and their electronic properties exhibit n-type and p-type conductivity, respectively. Divacancy of N and C in hetero bilayer shows high stability and induces direct band gap in up and down spin, respectively. Combined by N substitutional doping in graphene and B vacancy in h-BN layer, this substitution-vacancy combination shows low formation energy and changes the semiconductor property of pristine graphene/h-BN bilayer to metallic. In contrast, the graphene/h-BN bilayer with the combinated defect of C-substitution in B site and C vacancy in graphene shows half-metallic electronic property. The calculated magnetic moments are in reasonable agreement with the available theoretical analysis on atomic charge distribution. This work reveals that the electronic and magnetic properties of graphene/h-BN bilayer can be effectively tuned by above proposed point defects engineering.

© 2014 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Graphene is a promising candidate among two dimensional materials for electronic application due to its unique Dirac electronic property [1]. In single layer graphene or graphene nanoribbons, it was found that vacancy can induce magnetism [2–5], as well as tune its energy gap [6]. Spin-polarized electronic current in graphene could be achieved by substitutional doping with boron and nitrogen atoms [7]. Because of the structural similarity, single layer hexagonal boron nitrogen (h-BN) is an analog to graphene. In h-BN sheet, significant spin polarization can be induced by vacancy defects [8]. However, B–N pair vacancies in h-BN sheet make it polarize by non-spin polarization [9]. Density functional study [10] showed that the electronic properties of a single layer hybrid h-BN and C sheet are related to both geometrical confinement and bonding character at the h-BN/C interface. In graphene and single layer h-BN sheet, point defects such as vacancies or substitutional dopants have significant influence on their electronic and magnetic properties.

Besides single layer atomic crystal, a new type of two-dimensional hetero-bilayer, called graphene/h-BN, was successfully prepared in experiments [11,12]. For this hybrid nanostructure which was combined by graphene and h-BN sheet, a minor energy gap was found because of interplanar interaction [13]. This energy gap is originated from the symmetry breaking of sublattice, which is similar with the case of graphene on h-BN substrate [14,15]. In Dirac nanoelectronics, energy gap opening at K point is particular important for achieving on/off current ratios. Raman experiments [16] and HRTEM imaging [17] proved that graphene/h-BN ultra-thin film posses significant carrier mobility. Moreover, using strain [13] and electric field [18] could effectively tune its band gap. Strain engineering on graphene/h-BN hetero-bilayer was also found interesting for sensor application [19]. The

---

* Corresponding author at: Hunan Key Laboratory for Micro-Nano Energy Materials and Devices, Faculty of Physics and Optoelectronic Engineering, Xiangtan University, Hunan 411105, People's Republic of China. Tel.: +86 73158292195; fax: +86 73158292468.
E-mail address: ylmao@xtu.edu.cn (Y. Mao).

http://dx.doi.org/10.1016/j.apsusc.2014.09.097
0169-4332/© 2014 Elsevier B.V. All rights reserved.

<table>
<caption>Table 1
Summary of results in graphene/h-BN hetero-bilayer with vacancy defects. The bond length in angstrom, the magnetic moment in μB, the electron number N<sub>up</sub> and N<sub>dn</sub> in up and down spin on nearby atoms around vacancies, the spin polarization P(E<sub>f</sub>) and Gibbs formation energy G<sub>f</sub> in eV are indicated. "+" and "−" means the moving of Fermi level upward and downward respect to the Fermi level in pristine graphene/h-BN hetero-bilayer, respectively. M and SC represent for metal and semiconductor properties deduced from band structures.</caption>
<thead>
<tr>
<th>Configurations</th>
<th colspan="2">Bond (Å)</th>
<th colspan="4">Magnetic moment (μB)</th>
<th colspan="3">Atomic charge distribution (e)</th>
<th rowspan="2">P(E<sub>f</sub>) (%)</th>
<th rowspan="2">G<sub>f</sub> (eV)</th>
<th colspan="2">Gap (eV)</th>
</tr>
<tr>
<th>C—C</th>
<th>B—N</th>
<th></th>
<th></th>
<th></th>
<th>Tot</th>
<th>N<sub>up</sub></th>
<th>N<sub>dn</sub></th>
<th>N<sub>up</sub> − N<sub>dn</sub></th>
<th>Majority</th>
<th>Minority</th>
</tr>
</thead>
<tbody>
<tr>
<td>B<sub>15</sub>N<sub>16</sub>/C<sub>32</sub></td>
<td>1.42</td>
<td>1.41</td>
<td>0.28 (N)</td>
<td>0.59 (N)</td>
<td>0.59 (N)</td>
<td>1.79</td>
<td>2.28 (N)</td>
<td>1.68 (N)</td>
<td>0.60 (N)</td>
<td>10</td>
<td>0.146</td>
<td>−0.04 (M)</td>
<td>−0.05 (M)</td>
</tr>
<tr>
<td>B<sub>16</sub>N<sub>16</sub>/C<sub>31</sub></td>
<td>1.43</td>
<td>1.42</td>
<td>0.46 (C)</td>
<td>0.46 (C)</td>
<td>0</td>
<td>1.22</td>
<td>1.43 (C)</td>
<td>1.03 (C)</td>
<td>0.40 (C)</td>
<td>12</td>
<td>0.115</td>
<td>−0.17 (M)</td>
<td>−0.15 (M)</td>
</tr>
<tr>
<td>B<sub>16</sub>N<sub>15</sub>/C<sub>32</sub></td>
<td>1.42</td>
<td>1.43</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0.51</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>72</td>
<td>0.105</td>
<td>+0.13 (M)</td>
<td>+0.16 (M)</td>
</tr>
<tr>
<td rowspan="2">B<sub>15</sub>N<sub>16</sub>/C<sub>31</sub></td>
<td rowspan="2">1.42</td>
<td rowspan="2">1.41</td>
<td>0.28 (C)</td>
<td>0.28 (C)</td>
<td>0.28 (C)</td>
<td>3.03</td>
<td>1.34 (C)</td>
<td>1.10 (C)</td>
<td>0.24 (C)</td>
<td rowspan="2">6</td>
<td rowspan="2">0.265</td>
<td rowspan="2">−0.47 (M)</td>
<td rowspan="2">−0.19 (M)</td>
</tr>
<tr>
<td>0.52 (N)</td>
<td>0.52 (N)</td>
<td>0.52 (N)</td>
<td></td>
<td>2.16 (N)</td>
<td>1.60 (N)</td>
<td>0.56 (N)</td>
</tr>
<tr>
<td>B<sub>16</sub>N<sub>15</sub>/C<sub>31</sub></td>
<td>1.43</td>
<td>1.42</td>
<td>0.77 (C)</td>
<td>0</td>
<td>0</td>
<td>1.00</td>
<td>1.62 (C)</td>
<td>1.00 (C)</td>
<td>0.62 (C)</td>
<td>0</td>
<td>0.207</td>
<td>0.14 (SC)</td>
<td>0.07 (SC)</td>
</tr>
</tbody>
</table>

open question arises such as whether vacancies or substitutional dopants of B, C and N in graphene/h-BN hetero-bilayer have impact on its electronic and magnetic properties? In this paper, we perform first-principles calculations to study the structural, electronic and magnetic properties of graphene/h-BN hetero-bilayer under three kinds of defect engineering: vacancy, anti-site substitution, and the possible combinations of the former two. We found that the electronic and magnetic properties of graphene/h-BN hetero-bilayer can be effectively tuned by the engineering of above mentioned point defects.

## 2. Computational method and model

Our calculations are performed based on density functional theory (DFT) [20] and plane-wave method as implemented in Vienna ab initio software package (VASP) [21]. The exchange correlation potential is treated within the local density approximation (LDA) as implemented by PAW function [22]. The cut-off energy of 450 eV was used and is found sufficient for the convergence in total energy. A vacuum space of 20 Å above the hetero-bilayer is used to eliminate the neighboring interaction between the supercells. A Monkhorst–Pack $13 × 13 × 1$ k-mesh for unit cell and $7 × 7 × 1$ k-mesh for $4 × 4$ supercell in Brillouin zone are employed. Spin polarization calculations are taken into account with a criterion of maximum force on each atom to be smaller than 0.01 eV/Å. Due to the importance of van-der-Waals (VDW) interactions [23–25] between the interlayers, VDW interaction has been accounted in our total energy calculations. Additionally, the dipole moment [26,27] is corrected along the direction perpendicular to the hetero-bilayer.

The stability can be evaluated by Gibbs formation energy $G_{\text{f}}$, which was calculated as the difference in total energy [28]

$$
G_{\text{f}}(\mathrm{X})=E_{\text{tot}}-\chi_{\mathrm{B}} \mu_{\mathrm{B}}-\chi_{\mathrm{C}} \mu_{\mathrm{C}}-\chi_{\mathrm{N}} \mu_{\mathrm{N}} \tag{1}
$$

where $E_{\text{tot}}$ is the average cohesive energy per atom of the optimized graphene/h-BN hetero-bilayer with point defects, $\chi_{\mathrm{i}}$ denotes the molar fraction of atom i (i= B, C, N) in the studied configurations satisfying

$$
\chi_{\mathrm{B}}+\chi_{\mathrm{C}}+\chi_{\mathrm{N}}=1 \tag{2}
$$

and $\mu_{\mathrm{X}}$ is the chemical potential of a single atom X (X=B, C, N). For h-BN monolayer, the chemical potentials of B and N atoms satisfy

$$
\mu_{\mathrm{BN}}=\mu_{\mathrm{B}}+\mu_{\mathrm{N}} \tag{3}
$$

where $\mu_{\mathrm{N}}$ is the energy of a single N atom obtained from a N₂ molecule [29], and $\mu_{\mathrm{C}}$ is the energy of a C atom obtained from pristine bilayer graphene [30]. The spin polarization $P(E_{\text{f}})$ at Fermi level can be expressed as

$$
P(E_{\text{f}})=\frac{D(E_{(\mathrm{f})\uparrow})-D(E_{(\mathrm{f})\downarrow})}{D(E_{(\mathrm{f})\uparrow})+D(E_{(\mathrm{f})\downarrow})} \tag{4}
$$

where $D(E_{(\mathrm{f})\uparrow})$ and $D(E_{(\mathrm{f})\downarrow})$ is the value of DOS in majority and minority spin at the Fermi level [1]. The difference

![](./images/814692441998229504_1.jpg)

Fig. 1. Relaxed configuration of pure graphene/h-BN bilayer, (a) top view and (b) side view. Boron, nitrogen, and carbon atoms are indicated in pink, blue and gray, respectively. In (a), C1, C2, B1, N1, N2 denote the sites where vacancy or substitution may be occur. Graphene layer is schematic indicated by ball-stick model and h-BN layer is depicted by stick model. In (b), the dashed line indicates the $4 × 4$ supercell used in our study. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

Table 2
Summary of results in graphene/h-BN hetero-bilayer with substitutional defects. The parameters and the units are the same with that in Table 1.

<table>
<thead>
<tr>
<th>Configurations</th>
<th colspan="4">Bond (Å)</th>
<th colspan="2">Magnetic moment (μB)</th>
<th colspan="3">Atomic charge distribution (e)</th>
<th rowspan="2">P(Ef) (%)</th>
<th colspan="3">Dopant charge (e)</th>
<th rowspan="2">Gf (eV)</th>
<th colspan="2">Gap (eV)</th>
</tr>
<tr>
<th>C—C</th>
<th>C—B</th>
<th>C—N</th>
<th>B—N</th>
<th></th>
<th>Tot</th>
<th>Nup</th>
<th>Ndn</th>
<th>Nup − Ndn</th>
<th>B</th>
<th>C</th>
<th>N</th>
<th>Majority</th>
<th>Minority</th>
</tr>
</thead>
<tbody>
<tr>
<td>B15CN16/C32</td>
<td>1.42</td>
<td>–</td>
<td>1.36</td>
<td>1.42</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>–</td>
<td>–1.48</td>
<td>–</td>
<td>0.053</td>
<td>+0.22 (M)</td>
<td>+0.22 (M)</td>
</tr>
<tr>
<td>B16N15C/C32</td>
<td>1.43</td>
<td>1.48</td>
<td>–</td>
<td>1.43</td>
<td>0.65 (C)</td>
<td>1.0</td>
<td>1.52 (C)</td>
<td>0.90 (C)</td>
<td>0.62 (C)</td>
<td>85</td>
<td>–</td>
<td>2.03</td>
<td>–</td>
<td>0.075</td>
<td>–0.07 (M)</td>
<td>–0.08 (M)</td>
</tr>
<tr>
<td>B16N16/C31B</td>
<td>1.42</td>
<td>1.49</td>
<td>–</td>
<td>1.43</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>–1.86</td>
<td>–</td>
<td>–</td>
<td>0.011</td>
<td>–0.14 (M)</td>
<td>–0.14 (M)</td>
</tr>
<tr>
<td>B16N16/C31N</td>
<td>1.42</td>
<td>–</td>
<td>1.40</td>
<td>1.43</td>
<td>0</td>
<td>0.22</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>–</td>
<td>–</td>
<td>1.14</td>
<td>0.006</td>
<td>+0.26 (M)</td>
<td>+0.26 (M)</td>
</tr>
<tr>
<td>B15CN16/C31B − TCB</td>
<td>1.42</td>
<td>1.48</td>
<td>1.36</td>
<td>1.43</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>–1.84</td>
<td>–1.50</td>
<td>–</td>
<td>0.051</td>
<td>0.12 (SC)</td>
<td>0.12 (SC)</td>
</tr>
<tr>
<td>B15CN16/C31B − HCB</td>
<td>1.42</td>
<td>1.48</td>
<td>1.35</td>
<td>1.43</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>–1.87</td>
<td>–1.51</td>
<td>–</td>
<td>0.050</td>
<td>0.39 (SC)</td>
<td>0.39 (SC)</td>
</tr>
<tr>
<td>B16N15C/C31N − TCN</td>
<td>1.43</td>
<td>1.46</td>
<td>1.41</td>
<td>1.42</td>
<td>0.32 (C)</td>
<td>0.49</td>
<td>1.47 (C)</td>
<td>1.17 (C)</td>
<td>0.30 (C)</td>
<td>66</td>
<td>–</td>
<td>2.25</td>
<td>1.20</td>
<td>0.080</td>
<td>+0.22 (M)</td>
<td>+0.22 (M)</td>
</tr>
<tr>
<td>B16N15C/C31N − HCN</td>
<td>1.43</td>
<td>1.46</td>
<td>1.41</td>
<td>1.42</td>
<td>–0.32 (C)</td>
<td>–0.49</td>
<td>1.13 (C)</td>
<td>1.42 (C)</td>
<td>–0.29 (C)</td>
<td>75</td>
<td>–</td>
<td>2.26</td>
<td>1.20</td>
<td>0.079</td>
<td>+0.13 (M)</td>
<td>+0.13 (M)</td>
</tr>
</tbody>
</table>

Table 3
Summary of results in combinanted point defects. The parameters and the units are the same with that in Table 1.

<table>
<thead>
<tr>
<th>Configurations</th>
<th colspan="4">Bond (Å)</th>
<th colspan="3">Magnetic moment (μB)</th>
<th></th>
<th colspan="3">Atomic charge distribution (e)</th>
<th>P(Ef) (%)</th>
<th colspan="3">Dopant charge (e)</th>
<th>Gf (eV)</th>
<th colspan="2">Gap (eV)</th>
</tr>
<tr>
<th>C—C</th>
<th>C—B</th>
<th>C—N</th>
<th>B—N</th>
<th></th>
<th></th>
<th></th>
<th>Tot</th>
<th>Nup</th>
<th>Ndn</th>
<th>Nup − Ndn</th>
<th>B</th>
<th>C</th>
<th>N</th>
<th>Majority</th>
<th>Minority</th>
</tr>
</thead>
<tbody>
<tr>
<td>B15N16/C31B</td>
<td>1.43</td>
<td>1.49</td>
<td>0</td>
<td>1.42</td>
<td>0.65 (N)</td>
<td>0.65 (N)</td>
<td>0.65 (N)</td>
<td>2.49</td>
<td>2.18 (N)</td>
<td>1.58 (N)</td>
<td>0.60 (N)</td>
<td>57</td>
<td>–1.89</td>
<td>0</td>
<td>0</td>
<td>0.160</td>
<td>–0.18 (M)</td>
<td>–0.19 (M)</td>
</tr>
<tr>
<td>B15N16/C31N</td>
<td>1.42</td>
<td>–</td>
<td>1.40</td>
<td>1.41</td>
<td>0.53 (N)</td>
<td>0.53 (N)</td>
<td>0.53 (N)</td>
<td>1.76</td>
<td>2.09 (N)</td>
<td>1.60 (N)</td>
<td>0.49 (N)</td>
<td>90</td>
<td>–</td>
<td>–</td>
<td>1.17</td>
<td>0.142</td>
<td>0(M)</td>
<td>0(M)</td>
</tr>
<tr>
<td>B15CN16/C31</td>
<td>1.43</td>
<td>–</td>
<td>1.36</td>
<td>1.45</td>
<td>0.30 (C)</td>
<td>0.30 (C)</td>
<td>0.30 (C)</td>
<td>1.00</td>
<td>1.49 (C)</td>
<td>1.19 (C)</td>
<td>0.30 (C)</td>
<td>100</td>
<td>–</td>
<td>–1.51</td>
<td>–</td>
<td>0.161</td>
<td>0(M)</td>
<td>0.23 (SC)</td>
</tr>
<tr>
<td>B16N15C/C31</td>
<td>1.42</td>
<td>1.50</td>
<td>–</td>
<td>1.43</td>
<td>0.59 (C)</td>
<td>0.59 (C)</td>
<td></td>
<td>1.00</td>
<td>1.48 (C)</td>
<td>1.00 (C)</td>
<td>0.48 (C)</td>
<td>0</td>
<td>–</td>
<td>2.08</td>
<td>–</td>
<td>0.191</td>
<td>0.08 (SC)</td>
<td>0.41 (SC)</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>–0.19 (C)</td>
<td></td>
<td>1.14 (C)</td>
<td>1.32 (C)</td>
<td>–0.18 (C)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/814692441998229504_2.jpg)

Fig. 2. Band structure and corresponding DOS of (a) pure graphene/h-BN hetero-bilayer, i.e. B₁₆N₁₆/C₃₂, (b) B₁₆N₁₅/C₃₂, (c) B₁₅N₁₆/C₃₂, (d) B₁₆N₁₅/C₃₁, (e) B₁₅CN₁₆/C₃₁, and (f) B₁₆N₁₅C/C₃₁ configurations. Projected DOS on B, C, and N atoms are also indicated along with the total DOS. Fermi level is indicated by dotted line.

of electron number between majority and minority spin is defined as

$$
\Delta N = N_{\text{up}} - N_{\text{dn}} \tag{5}
$$

where $N_{\text{up}}$ and $N_{\text{dn}}$ is the number of electrons over all occupied states in up and down spin, respectively [31]. $N_{\text{up}}$ and $N_{\text{dn}}$ can be obtained from the integration of DOS for spin-up and spin-down electrons, respectively. The charge and the magnetic moment around the defects listed in Tables 1–3 are obtained from Bader charge analysis.

For the graphene/h-BN bilayer, our test results predict that AB stacking is energetically preferred, agreeing well with previous reports [32,33]. In pure graphene/h-BN hetero-bilayer, the B–N bond length, C–C bond length and interlayer spacing are $1.42\,\text{Å}$, $1.42\,\text{Å}$, and $3.18\,\text{Å}$, respectively, which is consistent with the results in the literature [34]. Fig. 1 shows the optimized structure of pure graphene/h-BN hetero-bilayer within a $4 \times 4$ supercell. Gibbs formation energy $G_{\text{f}}$ we calculated corresponding to this configuration is $-0.0017\,\text{eV}$, indicating weak VDW interaction between the sublayers. Three types of point defects are considered in our study: vacancy, anti-site substitution and their combinations. We define graphene/h-BN as formula $\text{B}_{16}\text{N}_{16}/\text{C}_{32}$. The "$\text{B}_{16}\text{N}_{16}$" and "$\text{C}_{32}$" denote the h-BN monolayer and graphene, respectively. B1, C1, C2, N1 and N2 indicated in Fig. 1 denote the studied sites of point defects. "B1", "C1" and "N1" are those sites for vacancies or anti-site substitutions. In anti-site substitution, formula $\text{B}_{15}\text{CN}_{16}/\text{C}_{31}\text{B}-\text{T}_{\text{CB}}$ means "B1" and "C1" sites are substituted by C atom and B atom, respectively. Formula $\text{B}_{15}\text{CN}_{16}/\text{C}_{31}\text{B}-\text{H}_{\text{CB}}$ means substitutional positions of C atom and B atom are located at "B1" and "C2" sites, respectively. The rest formulas for other configurations can be deduced by analogy, as listed in Tables 1–3.

![](./images/814692441998229504_3.jpg)

Fig. 3. Partial density of states (PDOS) for B, C and N atoms in (a) $B_{16}N_{15}/C_{32}$, (b) $B_{15}CN_{16}/C_{31}$, and (c) $B_{16}N_{15}C/C_{31}$ configurations. Positive and negative DOS represent for the electron states of spin-up and spin-down.

## 3. Results and discussion

### 3.1. Stability and geometry

For the vacancy point defects, the calculated results are summarized in Table 1. In hetero-bilayer, the Gibbs formation energy of N vacancy in $B_{16}N_{15}/C_{32}$ configuration is 0.105 eV, which is smallest among the studied vacancy point defects. Its stability has some similar with that in single h-BN sheet, because it was reported that N vacancy is much likely to be formed than B vacancy [34]. In $B_{16}N_{15}/C_{32}$ configuration, both sub-layers are found keeping well with the original hexagonal lattice. In $B_{16}N_{15}/C_{32}$ configuration, it is found that strong covalent bonds are formed around B vacancy. Gibbs formation energy of C vacancy in $B_{16}N_{16}C_{31}$ configuration and B vacancy in $B_{15}N_{16}/C_{32}$ configuration are 0.115 eV and 0.146 eV, respectively, which can be compared with that of single vacancy in graphene [35]. Among the Gibbs formation energies of di-vacancies in hetero-bilayers, $B_{16}N_{15}/C_{31}$ configuration has Gibbs formation energy of 0.575 eV, which is lowest in di-vacancy point defects.

For the substitutional point defects, our calculated results are summarized in Table 2. For single atom substitution, the Gibbs formation energy of $B_{16}N/C_{31}N$ configuration is 0.006 eV, which is lowest among the same type substitutional configurations. Due to lower Gibbs formation energy, $B_{15}CN_{16}/C_{32}$ configuration is more favorable to be formed than configuration $B_{16}CN_{15}/C_{32}$, which is similar with the situation in single h-BN sheet [36]. For the anti-site substitutional defect in $B_{15}CN_{16}/C_{31}B-H_{CB}$ configuration, strong covalent bonds are formed around C and B dopants. Among anti-site substitutional defects, this configuration has lowest Gibbs formation energy.

The third type of point defects we studied are the combinations of vacancies and substitutional defects. Their calculated results on energies and optimized configurations are summarized in Table 3. Among this type defected configurations, $B_{15}N_{16}/C_{31}N$ configuration has the lowest Gibbs formation energy of 0.142 eV. In other words, $B_{15}N_{16}/C_{31}N$ configuration is the most favorable to be formed by the defect combination of B vacancy in h-BN layer and N substitution in graphene layer. Though vacancy and substitutional defect exists, this configuration still keeps well the original hexagonal lattice. Interestingly, for $B_{16}N_{15}C/C_{31}$ configuration, there is a concave geometry around the C dopant in h-BN monolayer. Detailed analysis shows that C dopant in h-BN layer is pushed $0.45\,\mathring{A}$ away from the h-BN plane. Correspondingly, the three neighbored B atoms around the C dopant have a height of $0.24\,\mathring{A}$ away from the original h-BN plane.

### 3.2. Electronic structures

The studied spin-resolved band structure, DOS and partial DOS projected on B, C, and N atoms are shown in Fig. 2. In Fig. 2(a), an energy gap of 65 meV in pure graphene/h-BN hetero-bilayer is found, which is in good agreement with previous reports [33,37-39]. As discussed above, $B_{16}N_{15}/C_{32}$ configuration with N

![](./images/814692441998229504_4.jpg)

Fig. 4. Spin density distribution in (a) B₁₅N₁₆/C₃₂, (b) B₁₆N₁₆/C₃₁, (c) B₁₅CN₁₆/C₃₁, and (d) B₁₆N₁₅C/C₃₁ configurations. Here we only show the slices passing through the vacancy layer in studied configurations.

vacancy is most stable among vacancy configurations. As shown in Fig. 2(b), N vacancy in B₁₆N₁₅/C₃₂ configuration leads to the up-shift of the Fermi level when compared with that of pristine graphene/h-BN hetero-bilayer. The band structure induced by N vacancy in B₁₆N₁₅/C₃₂ configuration exhibits n-type conductivity, which is similar with that in single layer h-BN sheet [40]. In contrast, as indicated in Fig. 2(c), B vacancy in B₁₆N₁₅/C₃₂ configuration leads to p-type conductivity due to the down-shift of the Fermi level in band structure. For di-vacancy configuration B₁₆N₁₅/C₃₁, as shown in Fig. 2(d), the band structure exhibits semiconductor character with direct energy gap of 0.143 eV and 0.06 eV in majority and minority spin, respectively. The bands with the energies between −5 and −1 eV are nearly spin degenerated and fully occupied. Thus, they do not contribute to spin polarization. It can be found that spin polarization is mainly originated from the spin unpaired bands with the energies between −1 and 0 eV. Between the same energy level, the DOS and its projection on B, C, and N atoms in majority and minority spin is also spin unpaired.

As the most stable combinated point defect which is composed by vacancy and anti-site substitution, B₁₅N₁₆/C₃₁N configuration behaves metallic character in its band structure (not shown here). In Fig. 2(e), we show the band structure and corresponding DOS of B₁₅CN₁₆/C₃₁ configuration. It is found that $\pi$ and $\pi^{*}$ bands of pristine graphene/h-BN bilayer are changed by the presence of C impurity in h-BN layer and C vacancy in graphene layer. A flat band resulted principally from substitutional C dopant is appear near the Fermi level in the band structure of majority spin, which shows a clear evidence of the interaction between C dopant and the h-BN layer. While in the bands of minority spin, they indicate semiconductor character with a narrow direct band gap of 0.23 eV around the Fermi level. The corresponding DOS in the right panel of Fig. 2(e) displays a peak at the Fermi level in majority spin, while there is no state in minority spin, indicating a full spin polarization. It means that B₁₅CN₁₆/C₃₁ configuration exhibits half-metallic property, which is interested for the potential application in spintronics [41]. As shown in Fig. 2(f), B₁₆N₁₅C/C₃₁ configuration is a semiconductor with direct energy gap of 0.08 eV in majority spin and 0.41 eV in minority spin, respectively. This point defect engineering enlarges the energy gap of pristine graphene/h-BN hetero-bilayer.

### 3.3. Magnetic property

As indicated in Tables 1–3, some studied configurations with point defects engineering show net magnetic moments. As typical examples, the magnetic moments of B₁₅N₁₆/C₃₂, B₁₆N₁₆/C₃₁, B₁₅CN₁₆/C₃₁ and B₁₆N₁₅C/C₃₁ configurations are 1.79 $\mu$B, 1.22 $\mu$B, 1.00 $\mu$B and 1.00 $\mu$B, respectively. To have a better understanding of the magnetism induced by studied point defects in graphene/h-BN bilayer, we show the PDOS of B-s, B-Pₓ, B-Pᵧ, B-P_z, B-P, C-s, C-Pₓ, C-Pᵧ, C-P_z, C-P, N-s, N-Pₓ, N-Pᵧ, N-P_z, and N-P states in Fig. 3. In Fig. 3(a), it can be found that the magnetic moment of B₁₅N₁₆/C₃₂ configuration is predominantly dominated by the N-P_z states due to the large PDOS peak of N-P_z at −0.130 eV in majority spin. In Fig. 3(b), un-symmetric distribution of C-P_z states near the Fermi level in majority and minority spin can be found. It implies that in B₁₅CN₁₆/C₃₁ configuration its magnetic moment is mainly originated from C-P_z states, and the orbitals of B and N atoms have small impact on the magnetic moment. In Fig. 3(c), it can be found from the PDOS of B₁₆N₁₅C/C₃₁ configuration that its magnetic moment is also predominated by C-P_z states near the Fermi level. The PDOS of C-P_z are appeared at 1 eV in majority spin and 0.197 eV in minority spin, respectively.

To gain more insight into the origin of magnetic moment, the spin density (ESD) in some studied magnetic configurations are plotted in Fig. 4. In Fig. 4(a), it can be found that the ESD of B₁₅N₁₆/C₃₂ configuration has a distinct distribution near B vacancy, where large amount of ESD in majority spin is localized around the N atoms. For each N atom closest to B vacancy, two electrons participate in the covalent bonding with nearby B atoms, the remaining three electrons of N atom has to be re-assigned [39]. In Fig. 4(b),

the ESD of $B_{16}N_{16}/C_{31}$ configuration is mainly localized around the two C atoms near the C vacancy. Due to the dangling bonds existing in the local region of defects, single vacancy in graphene/h-BN hetero-bilayer would induce the magnetic coupling between the atoms around the vacancy [31]. In Fig. 4(c), ESD of $B_{15}CN_{16}/C_{31}$ configuration is well described from the spin distribution of individual atoms near the C vacancy. It is clear to see that the ESD in majority spin is localized around the C atoms. However, the ESD of $B_{16}N_{15}C/C_{31}$ configuration as depicted in Fig. 4(d) shows that large amount of ESD in majority spin is localized around the two nearby C atoms around C vacancy.

Quantitative analysis on the distribution of the atomic charge and magnetic moment is performed and the results are listed in Tables 1–3. The charge difference $N_{up}-N_{dn}$ between $N_{up}$ net charge in majority and $N_{dn}$ net charge in minority is consistent with the value of magnetic moments deduced from Bader charge analysis. For instance, in $B_{15}N_{16}/C_{32}$ configuration, the magnetic moments of three N atoms near B vacancy are $0.28\ \mu$B, $0.59\ \mu$B and $0.59\ \mu$B, respectively. From the analysis on atomic charge distribution, the latter two N atoms contribute 0.60 e each as listed in Table 1. From Bader charge analysis, the magnetic moments of three C atoms around C vacancy in $B_{16}N_{16}/C_{31}$ configuration are $0.46\ \mu$B, $0.46\ \mu$B and $0\ \mu$B, respectively. From the integration of majority and minority DOS in this configuration, the former two C atoms has 0.4 e difference each in $N_{up}-N_{dn}$. Moreover, in $B_{15}CN_{16}/C_{31}$ configuration, the magnetic moments of each C atom around C vacancy is $0.30\ \mu$B as shown in Table 3, which is consistent with the value of unpaired electron $N_{up}-N_{dn}$. Interestingly, the magnetic moments of three C atoms around C vacancy in $B_{16}N_{15}C/C_{31}$ configuration are $0.59\ \mu$B, $0.59\ \mu$B and $-0.19\ \mu$B, respectively, exhibiting ferromagnetism. From the analysis on atomic charge distribution as listed in Table 3, the two C atoms have a contributing of 0.48 e each and the other C atom has a contribution of $-0.18$ e. Our analysis on atomic charge difference $N_{up}-N_{dn}$ is accordance with the results of magnetic moments obtained from Bader analysis.

## 4. Summary

In summary, we have performed first-principles calculations to study the structural, electronic and magnetic properties of graphene/h-BN hetero-bilayer with three kinds of point defects engineering: vacancy, B/C/N substitution, and the possible combinations of the former two. The optimized geometry, Gibbs formation energy, magnetic moment, charge transfer and electronic property of these systems are discussed. It was found that N vacancy is more likely to form than B vacancy in graphene/h-BN bilayer and their electronic properties exhibit n-type and p-type conductivity, respectively. Divacancy of nitrogen and carbon in hybrid bilayer shows high stability and induces direct band gap of 0.143 eV and 0.06 eV in up and down spin, respectively. Combined by N substitutional doping in graphene and B vacancy in h-BN layer, the substitution-vacancy combination shows low Gibbs formation energy and changes the semiconductor property of pristine graphene/h-BN bilayer to metallic. In contrast, the graphene/h-BN bilayer with the combinated defect of C-substitution in B site and C vacancy in graphene shows half-metallic electronic property, which has potential application in spintronics. Some studied cases with point defects engineering show net magnetic moments, such as typical examples with magnetic moments in $B_{15}N_{16}/C_{32}$, $B_{16}N_{16}/C_{31}$, $B_{15}CN_{16}/C_{31}$ and $B_{16}N_{15}C/C_{31}$ configurations. In order to give a better understanding on the magnetism induced by studied point defects, PDOS and ESD are explored to show a qualitative analysis. The calculated magnetic moments are in reasonable agreement with the available theoretical analysis on atomic charge distribution. Our study on above point defects engineering in graphene/h-BN hetero bilayer shows a possible way to tune the electronic and magnetic properties of ultra-thin hybrid quantum film.

## Acknowledgments

This work is supported by National Natural Science Foundation of China (nos. 11374251, 11471280 and 11101346), by the Scientific Research Foundation of the Education Bureau of Hunan Province in China (nos. 12K046 and YB2011B029), by Hunan Provincial Natural Science Foundation of China (no. 12JJ9002).

## References

[1] Y.L. Mao, J.M. Yuan, J.X. Zhong, J. Phys.: Condens. Matter 20 (2008) 115209.
[2] D.C. Yu, E.M. Lupton, M.L. Liu, W. Liu, F. Liu, Nano Res. 1 (2008) 56.
[3] D.C. Yu, E.M. Lupton, H.J. Gao, C. Zhang, F. Liu, Nano Res. 1 (2008) 497.
[4] L. Chen, D.C. Yu, F. Liu, Appl. Phys. Lett. 93 (2008) 223106.
[5] W. Liu, Z.F. Wang, Q.W. Shi, J. Yang, F. Liu, Phys. Rev. B 80 (2009) 233405.
[6] B. Huang, F. Liu, J. Wu, B.L. Gu, W.H. Duan, Phys. Rev. B 77 (2008) 153411.
[7] H. Park, A. Wadehra, J.W. Wilkins, A.H. Castro Neto, Phys. Rev. B 87 (2013) 085441.
[8] Z. Wei, J.M. Yuan, S.H. Li, J. Liao, Y.L. Mao, Acta Phys. Sin. 62 (2013) 203101.
[9] S.H. Li, J.M. Yuan, Y.W. Hu, J.X. Zhong, Y.L. Mao, Physica E: Low-dimension. Syst. Nanostruct. 56 (2014) 24.
[10] Z.H. Huang, V.H. Crespi, J.R. Chelikowsky, Phys. Rev. B 88 (2013) 235425.
[11] A. Eckmann, et al., Nat. Phys. 10 (2014) 451.
[12] L.J. Ci, L. Song, C.H. Jin, D. Jariwala, D.X. Wu, Y.J. Li, A. Srivastava, Z.F. Wang, K. Storr, L. Balicas, F. Liu, P.M. Ajayan, Nat. Mater. 9 (2010) 430.
[13] X.L. Zhong, Y.K. Yap, R. Pandey, Phys. Rev. B 83 (2011) 193403.
[14] Y. Sakai, T. Koretsune, S. Saito, Phys. Rev. B 83 (2011) 205434.
[15] G. Giovannetti, P.A. Khomyakov, G. Brocks, P.J. Kelly, J.V.D. Brink, Phys. Rev. B 76 (2007) 073103.
[16] O.M. Nayfeh, A.G. Birdwell, C. Tan, M. Dubey, H. Gullapalli, Z. Liu, A.L.M. Reddy, P.M. Ajayan, Appl. Phys. Lett. 102 (2013) 103115.
[17] K.H. Lee, H.J. Shin, J.Y. Lee, I.Y. Lee, G.H. Kim, J.Y. Choi, S.W. Kim, Nano Lett. 12 (2012) 714.
[18] J. Sławińska, I. Zasada, Z. Klusek, Phys. Rev. B 81 (2010) 155433.
[19] Y. Xu, Z. Guo, H. Chen, Y. Yuan, J.C. Lou, X. Lin, H.Y. Gao, H.S. Chen, B. Yu, Appl. Phys. Lett. 99 (2011) 133109.
[20] G. Kresse, J. Hafner, Phys. Rev. B 47 (1993) 558.
[21] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169.
[22] G. Kresse, J. Joubert, Phys. Rev. B 59 (1999) 1758.
[23] X. Wu, M.C. Vargas, S. Nayak, V. Lotrich, G. Scoles, J. Chem. Phys. 115 (2001) 8748.
[24] S. Grimme, J. Comp. Chem. 27 (2006) 1787.
[25] J. Klimeš, D.R. Bowler, A. Michaelides, Phys. Rev. B 83 (2011) 195131.
[26] G. Makov, M.C. Payne, Phys. Rev. B 51 (1995) 4014.
[27] J. Neugebauer, M. Scheffler, Phys. Rev. B 46 (1992) 16067.
[28] T. Dumitrică, M. Hua, B.I. Yakobson, Phys. Rev. B 70 (2004) 241303.
[29] S.J. Zhao, J.M. Xue, Phys. Rev. B 86 (2012) 165428.
[30] Y. Fujimoto, S. Saito, Phys. Rev. B 84 (2011) 245446.
[31] X.Q. Dai, J.H. Zhao, M.H. Xie, Y.N. Tang, Y.H. Li, B. Zhao, Eur. Phys. J. B 80 (2011) 343.
[32] B. Sachs, T.O. Wehling, M.I. Katsnelson, A.I. Lichtenstein, Phys. Rev. B 84 (2011) 195414.
[33] Y.L. Mao, Z.Q. Xie, J.M. Yuan, S.H. Li, Z. Wei, J.X. Zhong, Physica E: Low-dimension. Syst. Nanostruct. 49 (2013) 111.
[34] M.S. Si, D.S. Xue, Phys. Rev. B 75 (2007) 193409.
[35] F. Banhart, J. Kotakoski, A.V. Krasheninnikov, ACS Nano 5 (2011) 1.
[36] Y. Ding, Y.L. Wang, J. Ni, Appl. Phys. Lett. 98 (2009) 123105.
[37] Y.C. Fan, M.W. Zhao, J.H. Wang, X.J. Zhang, H.Y. Zhang, Appl. Phys. Lett. 98 (2011) 083103.
[38] R. Balu, X.L. Zhong, R. Pandey, S.P. Karna, Appl. Phys. Lett. 100 (2012) 052104.
[39] E.J. Kan, H. Ren, F. Wu, Z.Y. Li, R.F. Lu, C.Y. Xiao, K.M. Deng, J.L. Yang, J. Phys. Chem. C 116 (2012) 3142.
[40] Y.G. Zhou, X.T. Zu, P. Yang, H.Y. Xiao, F. Gao, J. Phys.: Condens. Matter 22 (2010) 465303.
[41] Y. Ding, Y.L. Wang, J. Ni, L. Shi, S.Q. Shi, C.R. Li, W.H. Tang, Nanoscale Res. Lett. 6 (2011) 190.