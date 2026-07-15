PAPER

View Article Online
View Journal | View Issue

![](./images/812507272553955329_1.jpg)

Cite this: Phys. Chem. Chem. Phys.,
2021, 23, 5340

# First-principles investigation of oxygen interaction with hydrogen/helium/vacancy irradiation defects in $Ti_{3}AlC_{2}^{\dagger}$

Zhaocang Meng, $^{abc}$ Canglong Wang, $^{*acd}$ Jitao Liu, $^{ac}$ Yinlong Wang, $^{e}$ Xiaolu Zhu, $^{f}$ Lei Yang*acd and Liang Huang$^{b}$

First-principles calculations have been performed to investigate the interaction between solute impurity O and H/He/vacancy irradiation defects in $Ti_{3}AlC_{2}$. The formation energy and occupation of O atoms within different defects as well as the trapping progress of O/H clusters are discussed. It is found that the O atom preferentially occupies the hexahedral interstitial site $(I_{hex}-1)$ in bulk $Ti_{3}AlC_{2}$, whereas it prefers to occupy the neighbouring tetrahedral interstitial site $(I_{tetr}-2)$ within pre-exisiting Al monovacancy $(V_{Al})$, Al divacancy $(2V_{Al-Al})$ and the $2V_{Al-C}$ divacancy composed of Al and C vacancies. The appearance of C vacancy could greatly reduce the oxygen formation energy and make an O atom more inclined to occupy the center of C vacancy. Vacancy could capture more O atoms than H/He atoms, where $V_{Al}$ and $2V_{Al-Al}$ could hold up to fifteen and eighteen O atoms, respectively. Meanwhile, the O could also promote the formation of Al vacancy. On the other hand, O atoms tend to occupy the interstitial sites near the Al atomic layer and have attraction to Al atoms, which is likely to enable the O atoms to combine with the Al atoms to form a $Al_{2}O_{3}$ protective layer, thus effectively inhibiting further oxidation inside the $Ti_{3}AlC_{2}$. In addition, the H-O exhibits repulsion interaction, but strong attraction occurs in the He-O interaction. Therefore, the O atom has an inhibitory effect on the formation of the H cluster, while it could bind more He atoms to form a large number of He bubbles. Besides, the O impurity greatly reduces the trapping ability of vacancy to H atoms, and O and He have a synergistic interaction for inhibiting the aggregation of H clusters. The present results are expected to provide a new insight into the behaviour of $Ti_{3}AlC_{2}$ under irradiation and oxidation conditions so that structural materials could be better designed.

Received 14th December 2020,
Accepted 4th February 2021

DOI: 10.1039/d0cp06462a

rsc.li/pccp

## 1 Introduction

As a clean and virtually unlimited energy source, fusion energy is widely regarded as the ultimate solution to the problem of resource depletion in the future, which has driven humans to make considerable efforts to conduct relevant technical and feasibility studies. The International Thermonuclear Experimental Reactor (ITER) $^{1,2}$ project is already being carried out through international cooperation and is aimed at realizing the extended burn of deuterium-tritium (D-T) plasma in a fusion reactor. One of the biggest challenges is that the structural materials will inevitably be exposed to the extremely high-energy neutrons, high temperature, high fluxes of H isotope ions and He particles, $^{3}$ which could result in the degradation of the mechanical and physical properties of the materials. $^{4-6}$ Therefore, structural materials must possess superior thermal mechanical properties, oxidation resistance and irradiation resistance to withstand the extreme fusion environment for a long time.

First of all, a great number of intrinsic defects and H/He transmutation atoms will be generated continuously under the irradiation of neutrons and high fluxes of ions, $^{7}$ leading to the formation of H/He bubbles, and embrittlement and swelling of the materials. $^{8,9}$ In addition, the O atoms are typical solute impurities. The oxidation behaviour of a structural material will greatly limit its high temperature application. Due to the long-term coexistence of irradiation and high-temperature oxidation of structural materials in extreme environments, it is inevitable that irradiation defects and soluble impurity O will interact jointly to affect the performance of the materials. There is a strong

$^{a}$ Institute of Modern Physics, Chinese Academy of Sciences, Lanzhou 730000, China. E-mail: cwang@impcas.ac.cn, lyang@impcas.ac.cn
$^{b}$ School of Physical Science and Technology, Lanzhou University, Lanzhou 730000, China
$^{c}$ School of Nuclear Science and Technology, University of Chinese Academy of Sciences, Beijing 100049, China
$^{d}$ Advanced Energy Science and Technology Guangdong Laboratory, Huizhou 516000, China
$^{e}$ College of Nuclear Science and Technology, Lanzhou University, Lanzhou 730000, China
$^{f}$ School of Electrical Engineering, Longdong University, Qingyang 745000, China
$\dagger$ Electronic supplementary information (ESI) available: (I) Local DOS for vacancy nearest-neighbor Al atom and interstitial O atom within different vacancy complexes. See DOI: 10.1039/d0cp06462a

interaction between O atoms and vacancies, which leads to the formation of stable vacancy-O complexes, thus influencing the evolution of microstructure in structural materials. $^{10-12}$ Recent thermal desorption spectroscopy (TDS) experiments by Nita $^{13}$ demonstrated the effects of impurity O on the behaviour of He-vacancy clusters in vanadium by He implantation, and the major desorption peaks were identified as $He_n$-vacancy-O clusters. In addition, Zhang *et al.* $^{14,15}$ also investigated the He interactions with vacancy-O clusters in vanadium by first-principles studies; the results show that the presence of O impurity reduces vacancy trapping ability for more He impurities.

In the past few decades, tremendous efforts have been devoted to understand the influence of long-term elevated temperature and high dose of irradiation on the evolution of microstructure and find materials suitable for the fusion reactors. $^{16-19}$ Among possible candidates, MAX phases are considered as the most promising candidates for high-temperature structure materials and protective coatings in future nuclear reactors. The MAX phases are a family of nano-laminated materials with the general formula $M_{n+1}AX_n$ $(n = 1, 2, 3),^{20}$ where M is an early transition metal, A is an element usually belonging to group IIIA or IVA, and X is C or N. The MAX phases have the highly anisotropic hexagonal crystal structure, in which M and X atoms form the octahedral edge sharing building blocks interleaved by layers of A atoms. This unique structure enables the MAX phases to exhibit an outstanding combination of metallic and ceramic properties, such as low density, high strength and modulus, high melting point, tolerance to damage, and resistance to thermal shock. $^{21-24}$ Meanwhile, extensive efforts have been devoted to the study on the oxidation resistance properties of MAX phases, $^{25,26}$ which exhibit a relatively good oxidation resistance over a wide range of environmental conditions. The oxidation behaviour of MAX materials obeys a cubic law, and the oxide film formed on the surface of MAX provides a good protective barrier against further oxidation, which has a crucial influence on the high-temperature performance of MAX phases. Furthermore, as a typical member of the family of MAX phase materials, the excellent performance of $Ti_3AlC_2$ has aroused tremendous attention in recent years. In particular, several studies $^{27-30}$ have been conducted to study the behaviour of $Ti_3AlC_2$ upon exposure to high temperature radiation; the results suggest that $Ti_3AlC_2$ exhibits excellent tolerance to irradiation damage under neutron/ion irradiation. Wang *et al.* $^{31}$ reported that $Ti_3AlC_2$ is superior to generate lattice disorder rather than amorphization under high doses of irradiation. The thermal stability of bulk $Ti_3AlC_2$ at high temperature in a hydrogen atmosphere was investigated $^{32}$ using scanning electron microscope and X-ray diffraction techniques, and it was found that $Ti_3AlC_2$ had a good hydrogen resistance at temperatures below $1300\ ^\circ\text{C}$, while the dissociation of $Ti_3AlC_2$ was accelerated by the introduction of hydrogen at higher temperatures. It has been reported $^{33}$ that He implantation only disorders the Al layers under the irradiation of $200\ \text{keV}\ \text{He}^+$ up to a fluence of $2 \times 10^{17}\ \text{cm}^{-2}$ at $500\ ^\circ\text{C}$, and $Ti_3AlC_2$ can suppress the formation of large He bubbles at temperatures below $500\ ^\circ\text{C}$. In addition, the irradiation induced damage of $Ti_3AlC_2$ can realize self-healing at about $800\ ^\circ\text{C}.^{34,35}$

Despite the above mentioned efforts, until now the fundamental physical mechanism of the interaction between solute impurity O and H/He/vacancy irradiation defects in $Ti_3AlC_2$ has not yet been clearly understood. In the present work, we use first-principles calculations to investigate the occupation of O atoms within different defects in $Ti_3AlC_2$. The interaction between O and H/He impurity is analyzed using binding energies and equilibrium distances. Furthermore, the effect of impurity O on the trapping ability of vacancy to H atoms as well as the stability of the V-O-$n$H and V-2O-$n$H complexes are investigated. Meanwhile, the effects of O atom concentration on vacancy and H/He impurity are also discussed using the formation energy of corresponding defect. Ultimately, the stable configurations of different complexes are displayed to better understand the microstructure evolution of $Ti_3AlC_2$ under extreme conditions.

## 2 Computational methodology

All first-principles calculations have been performed using density functional theory (DFT) and the pseudopotential plane-wave method implemented using the VASP codes. $^{36,37}$ The projector-augmented wave (PAW) potentials for the ion-electron interaction and the generalized gradient approximation (GGA) with a PBE functional $^{38}$ for the exchange-correlation interaction are adopted. The $3 \times 3 \times 1$ supercells composed of 108 atoms are used for all defect calculations. The plane wave cutoff energy is set to 480 eV and the k-point of Brillouin zone sampling is performed using the Monkhorst-pack scheme with $5 \times 5 \times 2$, which has been proven to be sufficient in the convergence test. During geometry optimization, both lattice parameters and coordinates of atoms are fully relaxed to ensure adequate calculation accuracy, where the energy change on each atom is less than $1 \times 10^{-6}$ eV and the force on each atom is less than $0.01\ \text{eV}\ \mathring{\text{A}}^{-1}$.

To determine the stable configuration of the defect in $Ti_3AlC_2$, the formation energy of defect is calculated, which is defined as follows:

$$
E_{\mathrm{f}}[\mathrm{X}]=E_{\mathrm{tot}}[\mathrm{X}]-E(\mathrm{ref})-\sum_{i} n_{i} \mu_{i} \tag{1}
$$

where $E_{\mathrm{tot}}[\mathrm{X}]$ is the total energy containing defect X in the supercell, and $E(\text{ref})$ represents the total energy of a perfect crystal. The integer $n_i$ indicates the number of atoms i that have been added to ($n_i > 0$) or removed from ($n_i < 0$) the supercell, and the $\mu_i$ denotes the corresponding chemical potential of the element. For the O and H atoms, $\mu_{\mathrm{O}}=E(\mathrm{O}_{2})/2$ and $\mu_{\mathrm{H}}=E(\mathrm{H}_{2})/2$, where $E(\mathrm{O}_{2})/2$ and $E(\mathrm{H}_{2})/2$ are half of the energy of gas-phase $\mathrm{O}_{2}$ and $\mathrm{H}_{2}$ molecules in vacuum, which are $-4.928$ and $-3.385$ eV, respectively. $\mu_{\text{He}}$ is the energy of an isolated He atom in vacuum, which is $-0.00019$ eV per atom. The chemical potentials of pure phases are variable and strongly dependent on partial pressure and temperature. Here, we have considered the chemical potential under poor conditions to describe the vacancy formation energy, which satisfies the following formula:

$$
\mu_{\mathrm{Al}}^{\text{poor}}=E_{\mathrm{Ti}_{3} \mathrm{AlC}_{2}}-3 \mu_{\mathrm{Ti}}-2 \mu_{\mathrm{C}} \tag{2}
$$

where $E_{\mathrm{Ti}_{3} \mathrm{AlC}_{2}}$ is the total energy of the $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$ primitive cell, and $\mu_{\mathrm{Ti}}, \mu_{\mathrm{Al}}$, and $\mu_{\mathrm{C}}$ correspond to the chemical potential of Ti, Al, and C under rich conditions; they are defined by the chemical potentials of bulk hcp Ti $(-7.761$ eV per atom), fcc Al $(-3.728$ eV per atom), and graphite $(-9.267$ eV per atom), respectively.

In order to analyze the interaction between different defects, the binding energy between defect A and B is defined as:

$$
E_{\text {bind }}[\mathrm{A}, \mathrm{B}]=E_{\mathrm{f}}[\mathrm{A}, \mathrm{B}]-\left[E_{\mathrm{f}}(\mathrm{A})+E_{\mathrm{f}}(\mathrm{B})\right] \tag{3}
$$

where $E_{\mathrm{f}}(\mathrm{A}, \mathrm{B})$ is the formation energy of the cluster composed of defect A and B, and $E_{\mathrm{f}}(\mathrm{A})$ and $E_{\mathrm{f}}(\mathrm{B})$ are the formation energies of defect A and B, respectively. By this definition, a negative binding energy denotes an attractive interaction, while a positive one denotes a repulsive interaction.

## 3 Results and discussions

$\mathrm{Ti}_{3} \mathrm{AlC}_{2}$ has a hexagonal crystal structure with a space group of $P 63 / \mathrm{mmc}$. The optimized unit cell structure is demonstrated in Fig. 1, in which blue spheres, pink spheres, and gray spheres denote Ti atoms, Al atoms, and C atoms, respectively. Al and C atoms occupy Wyckoff positions of $2 \mathrm{~b}(0,0,1 / 4)$ and $4 \mathrm{f}(1 / 3,2 / 3$, $\left.Z_{\mathrm{C}}\right)$, respectively. Two types of non-equivalent Ti atoms (Ti1 and Ti2) are located in Wyckoff positions of $2 \mathrm{a}(0,0,0)$ and $4 \mathrm{f}(1 / 3,2 /$ $\left.3, Z_{\mathrm{Ti} 2}\right)$, respectively. The optimized lattice constants are shown in Table 1, together with the experimental and other firstprinciples results for comparison. As we could see, the current results are in good agreement with theoretical and experimental data, which ensure the reliability of our present firstprinciples calculations.

![](./images/812507272553955329_2.jpg)

Fig. 1 Schematic of the crystal structure and different stable interstitial configurations in $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$. The frames using green lines are employed to represent different interstitial sites.

<table>
<caption>Table 1 Comparison of our calculated lattice constants (in $\mathring{A}$) with experimental results and previous first-principles calculations of $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$</caption>
<thead>
<tr>
<th>Ref.</th>
<th>$a$</th>
<th>$c$</th>
<th>$c/a$</th>
</tr>
</thead>
<tbody>
<tr>
<td>This work</td>
<td>3.082</td>
<td>18.637</td>
<td>6.047</td>
</tr>
<tr>
<td>Experimental³⁹</td>
<td>3.075</td>
<td>18.587</td>
<td>6.042</td>
</tr>
<tr>
<td>VASP(PBE)⁴⁰</td>
<td>3.082</td>
<td>18.652</td>
<td>6.052</td>
</tr>
<tr>
<td>CASTEP(PBE)⁴¹</td>
<td>3.081</td>
<td>18.645</td>
<td>6.052</td>
</tr>
<tr>
<td>CASTEP(PW91)⁴²</td>
<td>3.072</td>
<td>18.732</td>
<td>6.098</td>
</tr>
</tbody>
</table>

### 3.1 Preferential individual O site in bulk $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$

Since the structural materials of the reactor need to be exposed to high temperature conditions for a long time, the safety and sustainability of the reactor is of great significance to study the stability of the structural materials at high temperatures. First of all, with respect to the high-temperature behaviour of $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$, oxidation is inevitable and involves sufficient complexity in the evolution of the microstructure. As soluble impurities, oxygen atoms are abundant at the interstitial sites of $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$. There are several possible stable configurations with high symmetry for the interstitial $\mathrm{O}$ atoms in $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$. In order to determine the most stable site for individual $\mathrm{O}$ atom in bulk $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$, five typical interstitial positions are considered here, as shown in Fig. 1. The hexahedral interstitial site $\mathrm{I}_{\text {hex}-1}$ is surrounded by three $\mathrm{Al}$ atoms and two Ti2 atoms, the tetrahedral interstitial site $\mathrm{I}_{\text {tetr}-2}$ is surrounded by three Ti2 atoms and one $\mathrm{Al}$ atom, the hexahedral interstitial site $\mathrm{I}_{\text {hex}-3}$ is surrounded by three $\mathrm{Al}$ atoms and two $\mathrm{C}$ atoms, the octahedral interstitial site $\mathrm{I}_{\text {oct}-4}$ consists of three Ti2 atoms and three $\mathrm{Al}$ atoms, and the tetrahedral interstitial site $\mathrm{I}_{\text {tetr}-5}$ is composed of four $\mathrm{C}$ atoms. Based on the above mentioned possible stable interstitial positions, the formation energies of $\mathrm{O}$ atoms at different interstitial sites are calculated using eqn (1) and the results are shown in Table 2.

It can be clearly seen from Table 2 that the oxygen insertion energy in the Ti-Al layer is negative everywhere, indicating that impurity $\mathrm{O}$ atom tends to occupy the interstitial sites near the $\mathrm{Al}$ atomic layer. Meanwhile, the oxygen insertion energy varies greatly with different interstitial sites. The ordering of oxygen insertion energy is $E_{\mathrm{f}}\left(\mathrm{I}_{\text {hex}-1}\right)<E_{\mathrm{f}}\left(\mathrm{I}_{\text {tetr}-2}\right)<E_{\mathrm{f}}\left(\mathrm{I}_{\text {oct}-4}\right)<E_{\mathrm{f}}\left(\mathrm{I}_{\text {hex}-3}\right)<$ $E_{\mathrm{f}}\left(\mathrm{I}_{\text {tetr}-5}\right)$. Of all the interstitial positions, the $\mathrm{O}$ atom is most likely to occupy the $\mathrm{I}_{\text {hex}-1}$ site and has the lowest formation energy of $-3.67$ eV. In $\mathrm{I}_{\text {hex}-1}$ configuration, the $\mathrm{O}$ atom moves into the $\mathrm{Al}$ layer and occupies the center of the triangle which is formed by three $\mathrm{Al}$ atoms, and the distance between the $\mathrm{Al}$ and $\mathrm{O}$ atoms is about $1.96 \mathring{A}$. In $\mathrm{Al}_{2} \mathrm{O}_{3}$, the $\mathrm{Al}-\mathrm{O}$ bond length is $1.97 \mathring{A}$, which is approximately equal to the bond length of $\mathrm{Al}-\mathrm{O}$ in $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$. This result suggests that the $\mathrm{Al}$ layer is more likely to combine with

<table>
<caption>Table 2 Formation energy $E_{\mathrm{f}}$ (in eV per atom) of the O/H/He atom at different interstitial sites in $\mathrm{Ti}_{3} \mathrm{AlC}_{2}$</caption>
<thead>
<tr>
<th>Atomic layer</th>
<th colspan="5">Ti-Al layer</th>
<th>Ti-C layer</th>
</tr>
<tr>
<th>Interstitial position</th>
<th>$\mathrm{I}_{\text{hex}-1}$</th>
<th>$\mathrm{I}_{\text{tetr}-2}$</th>
<th>$\mathrm{I}_{\text{hex}-3}$</th>
<th>$\mathrm{I}_{\text{oct}-4}$</th>
<th>$\mathrm{I}_{\text{tetr}-5}$</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>O formation energy(this work)</td>
<td>−3.67</td>
<td>−3.48</td>
<td>−2.03</td>
<td>−2.59</td>
<td>1.62</td>
<td></td>
</tr>
<tr>
<td>H formation energy⁴³</td>
<td>−0.11</td>
<td>−0.25</td>
<td>−0.07</td>
<td>−0.06</td>
<td>0.90</td>
<td></td>
</tr>
<tr>
<td>He formation energy⁴⁴</td>
<td>2.48</td>
<td>3.28</td>
<td>—</td>
<td>2.95</td>
<td>4.99</td>
<td></td>
</tr>
</tbody>
</table>

O atoms and form the $Al_2O_3$ protective layer, which could prevent further oxidation inside the material. Meanwhile, the $Al_2O_3$ protective layer could well fill the cracks on the material surface, so as to realize the healing of cracks. This oxidation induced self-healing mechanism is attractive as the MAX phase is protected and self-healing is achieved without the addition of a secondary material or chemical reagent. In the literature, it has been reported $^{45,46}$ that the oxide scale composed of multiple crystalline phases is formed on the exterior surface with increase in temperature, which could profoundly affect the mechanical properties of MAX phases, producing a significant increase in strength and loss of ductility. Thus, oxygen incorporation within the MAX phase material may be beneficial not only for tuning its properties, but would also allow for shorter diffusion paths when self-healing is required. Our calculation results explain this phenomenon well. In addition, the formation energies of H and He at different interstitial sites in bulk $Ti_3AlC_2$ have been calculated, and the results show that the H atom tends to occupy the $I_{tetr}$-2 site and the He atom tends to occupy the $I_{hex}$-1 site. Compared with impurity H/He atoms at different interstitial sites, the O atom always has a much lower formation energy, suggesting that O impurity has higher solubility than H/He in $Ti_3AlC_2$, which supports the existence of the O atom as the predominant impurity in $Ti_3AlC_2$. At the same time, it is not difficult to find that O, H and He atoms usually occupy the open Ti-Al layer, indicating that Al atoms have a strong attraction to different impurities and could bind the impurity atoms to gather in the Al layer. Therefore, the Al atomic layer is still the most vulnerable to being destroyed by the impurity atoms in the $Ti_3AlC_2$ structure.

### 3.2 The occupation of O atom within different vacancy clusters in $Ti_3AlC_2$

In order to explore the interaction between O and vacancy, we firstly calculated the formation energy of impurity O atom in the center of different mono-vacancies, and the results are shown in Table 3. It is obvious that the O atom is unstable at the center of the Ti2 vacancy and will deviate from the Ti2 vacancy center and move to the adjacent $I_{hex}$-1 site. When an O atom occupies the center of the Ti1 vacancy, it has the highest formation energy of 3.74 eV. Instead, the O atom has negative formation energy in the center of the C and Al vacancies. Moreover, the formation energy of the O atom in the center of the C vacancy is much lower than that of other vacancies, which implies that the O atom is more likely to occupy the center of the C vacancy. Our result is in good agreement with recent experimental observations, $^{47}$ which show that the characteristic nano-laminated structure of the MAX phase is retained upon oxygen incorporation, with strong indications of O substituting for C. Further evidence of O substituting for C has since been presented based on electron-energy-loss spectroscopy and WIEN2K calculations, $^{48}$ and a new MAX-phase-related material, in part based on oxygen, is hence suggested. Therefore, quaternary MAX phases provide future possibilities for designing multifunctional materials where the control of chemical order, or disorder, as well as inherent stoichiometry is necessary.

<table>
<caption>Table 3 Formation energies $E_f$ (in eV per atom) of an O atom at the center of different mono-vacancies in $Ti_3AlC_2$</caption>
<thead>
<tr>
<th>Vacancy</th>
<th>$V_{Al}$</th>
<th>$V_C$</th>
<th>$V_{Ti1}$</th>
<th>$V_{Ti2}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>O formation energy</td>
<td>−2.44</td>
<td>−6.17</td>
<td>3.74</td>
<td>Unstable</td>
</tr>
</tbody>
</table>

Next, since previous first-principles calculations $^{43}$ have suggested that Al monovacancy $(V_{Al})$, Al divacancy $(2V_{Al-Al})$ and the $2V_{Al-C}$ divacancy composed of Al and C vacancies are the most easily formed ones in all vacancy complexes, we investigated the occupation and formation energy of an individual O atom within the above three types of vacancies, and the results are shown in Table 4.

<table>
<caption>Table 4 Formation energies $E_f$ (in eV per atom) of an O atom within different vacancy complexes in $Ti_3AlC_2$</caption>
<thead>
<tr>
<th>Interstitial position</th>
<th>$I_{hex}$-1</th>
<th>$I_{tetr}$-2</th>
<th>$I_{hex}$-3</th>
<th>$I_{oct}$-4</th>
<th>Sub</th>
</tr>
</thead>
<tbody>
<tr>
<td>$V_{Al}$</td>
<td>−4.04</td>
<td>−4.15</td>
<td>−2.80</td>
<td>−3.30</td>
<td>−2.44</td>
</tr>
<tr>
<td>$2V_{Al-Al}$</td>
<td>−4.09</td>
<td>−4.29</td>
<td>Unstable</td>
<td>Unstable</td>
<td>Unstable</td>
</tr>
<tr>
<td>$2V_{Al-C}$</td>
<td>−4.07</td>
<td>−4.42</td>
<td>Unstable</td>
<td>−4.29</td>
<td>Unstable (Al)
<br>−6.05 (C)</td>
</tr>
</tbody>
</table>

It can be seen that an O atom always tends to occupy the neighbouring $I_{tetr}$-2 site within different vacancy complexes, which is significantly different from the O occupation in bulk $Ti_3AlC_2$. In the case of $V_{Al}$, the order of oxygen formation energy is $E_f(I_{tetr}-2) < E_f(I_{hex}-1) < E_f(I_{oct}-4) < E_f(I_{hex}-3) < E_f(Sub)$, and the formation energy of O atom varies greatly with different interstitial sites. The O atom has the highest formation energy when it occupies the center of the Al vacancy, which suggests that the O atom preferentially occupies the neighboring interstitial sites of the vacancy rather than the Al vacancy center. In the case of $2V_{Al-Al}$, the O atom is unstable at $I_{hex}$-3 and $I_{oct}$-4 sites and shifts from the initial sites toward the adjacent $I_{hex}$-1 position, respectively. Similarly, the O atom also preferentially deviates from the Al vacancy center to the nearby $I_{hex}$-1 site. These results indicate that the O atom has a strong tendency to migrate towards the $I_{hex}$-1 site, which may be mainly due to its low migration energy. In the case of $2V_{Al-C}$, the $I_{hex}$-3 configuration is also unstable, where the O atom will move to the adjacent $I_{oct}$-4 position after relaxation. Meanwhile, the O atom preferentially moves from the Al vacancy center toward the adjacent $I_{tetr}$-2 site. In contrast, the O atom is most likely to occupy the center of C vacancy with the lowest formation energy of −6.05 eV. The order of oxygen formation energy is $E_f(sub-C) < E_f(I_{tetr}-2) < E_f(I_{oct}-4) < E_f(I_{hex}-1)$. It is the occurrence of vacancy that makes the occupation of interstitial O atom change significantly. The optimal interstitial site of O atom changes from the $I_{hex}$-1 site in bulk $Ti_3AlC_2$ to the $I_{tetr}$-2 site near the vacancy. As the number of vacancies increases, the probability of instability occurring on oxygen atom at interstitial sites increases gradually, where the O atom has a stronger tendency to migrate to the adjacent $I_{hex}$-1 and $I_{tetr}$-2 positions, so $nV-O_{hex}$-1 and $nV-O_{tetr}$-2 are the predominant complexes in all vacancy–O clusters. Besides, oxygen formation energies within these vacancies are all much smaller than that of single O in bulk $Ti_3AlC_2$, and the oxygen formation energy decreases gradually

with an increase in the number of vacancies. This is mainly because vacancy could provide more space for the accumulation of O clusters, which also well explains the trapping effect of the vacancy on O atoms. All of these results show that the O atom preferentially occupies the neighboring interstitial sites of Al vacancy rather than the vacancy center. On the contrary, the appearance of C vacancy has a pronounced influence on the O atom, which greatly reduces the formation energy of the O atom in $Ti_{3}AlC_{2}$ and particularly makes the O atom stable in the center of the C vacancy compared with other vacancy centers and interstitial sites. However, the C vacancy defect has a relatively higher formation energy, which is why the C vacancy is not dominant in $Ti_{3}AlC_{2}$. Therefore, only a few C vacancies will be preempted by the implanted O atoms, and the remaining large number of O atoms are still mainly distributed in the interstitial sites around the Al vacancy. In addition, these results also suggest that a tunable method for producing nanoscale oxides is possible, the growth of which could be controlled by the generation and migration of intrinsic defects, as well as appropriate chemical environment change. Therefore, a deeper knowledge of interaction between impurity O atom and point defects in MAX phases is technologically crucial for the production of desirable nanoscale materials by tuning the ambient environment.

In order to explain the behaviour of O preferentially occupying the neighbouring $I_{tetr}$-2 interstitial sites of the vacancy and the C vacancy center, we computed and analyzed the local densities of states (LDOS) on O and its nearest-neighbor Al atom. For $V_{Al}$ and $2V_{Al-Al}$, the p-projected DOS of O at the Fermi energy level for $I_{tetr}$-2 O is slightly lower than that for O in the $V_{Al}$ center and $I_{hex}$-1 O, respectively. Meanwhile, the deformation of the p-projected DOSs of Al for the O in the center of Al vacancy and neighbouring interstitial sites are clearly observed compared with that in the pure material with vacancy, and the deformation of p-projected DOSs of the Al atom for $I_{tetr}$-2 O is smaller than that for O at other sites, as shown in Fig. S1(a and b) (ESI†). This finding further indicates less O-Al interactions at the $I_{tetr}$-2 site. For $2V_{Al-C}$, the p-projected DOS of O at the Fermi energy level for O in the center of the C vacancy is much lower than that for $I_{hex}$-1 O, while the insertion of O causes distortion of the p-projected DOSs of the neighboring Al atom, and the LDOS of Al for the O in the center of the C vacancy deforms less than that for the $I_{hex}$-1 O, as shown in Fig. S1(c) (ESI†). In addition, it is also reported⁵⁰ that oxygen substituting carbon is most beneficial for MAX phases where it adds the stability of phases due to a charge redistribution of Ti 3d states that gives rise to an increased Ti 3d-Al 2p hybridization. All these analyses reveal that the $I_{tetr}$-2 site for O atoms is more stable than the Al vacancy center and other interstitial sites. But the presence of the C vacancy makes the O atom more inclined to occupy the center of the C vacancy rather than the neighbouring interstitial sites, in agreement with the calculated formation energies.

### 3.3 O trapping progress within different vacancies in Ti3AlC₂
Since vacancies have a strong interaction with O impurities in $Ti_{3}AlC_{2}$, which could bind a certain number of O atoms and form stable vacancy-O complexes, it is necessary to study the trapping capacity of different vacancies for O atoms. Here, we calculated the trapping energy of O atoms within the typical $V_{Al}$ and $2V_{Al-Al}$ vacancy clusters. Firstly, we placed the O atoms into the space of the vacancy one by one and relaxed the entire system, and obtained the most stable configuration for every trapped O atom by comparing the formation energy of O atoms at different interstitial sites. Next, we calculated the trapping energy of the $n$-th O atom migrating to the vacancy, so as to determine the number of O atoms that different vacancies could accommodate. The trapping energy is defined as:

$$
E^{\text{trap}}(n\text{th}) = E(n\text{O,V}) - E[(n-1)\text{O,V}] - E(\text{O}_{\text{hex1}}) + E(\text{ref})
\tag{4}
$$

where $E(n\text{O,V})$ is the energy of $Ti_{3}AlC_{2}$ with $n$O atoms and vacancy, and $E(\text{O}_{\text{hex1}})$ is the energy of the system with one O atom in the most stable $I_{hex}$-1 interstitial site. A negative trapping energy represents an exothermic process when the O atom moves from the remote $I_{hex}$-1 site to the trapped vacancy space. The trapping energy as a function of the number of O atoms within $V_{Al}$ and $2V_{Al-Al}$ is illustrated in Fig. 2.

It can be seen that the change in trapping energy presents a small periodic oscillation as the number of O atoms increases. The trapping of the first O atom within $V_{Al}$ requires the trapping energy of $-0.48$ eV, while the trapping energy for the fifteenth O atom is $-0.24$ eV. When more O atoms are implanted, the O trapping energy becomes positive, indicating that the sixteenth O atom is energetically favorable to occupy the remote $I_{hex}$-1 interstitial site rather than the trapped vacancy space. Therefore fifteen O atoms could be trapped by $V_{Al}$. Meanwhile, the process of O atoms being captured by $2V_{Al-Al}$ divacancy is exothermic until the number of O atoms reaches nineteen, suggesting that eighteen O atoms could be trapped by $2V_{Al-Al}$. This result further confirms that vacancy defects caused by irradiation could capture a large number of O atoms, which aggravates the oxidation of $Ti_{3}AlC_{2}$. In the literature,⁴³,⁴⁹ $V_{Al}$ could capture four H atoms, and $2V_{Al-Al}$ could capture seven H

![](./images/812507272553955329_3.jpg)

Fig. 2 Trapping energy for O atom as a function of the number of O atoms trapped by $V_{Al}$ and $2V_{Al-Al}$ in $Ti_{3}AlC_{2}$.

atoms; so, Al vacancy has stronger interaction with soluble impurity O and could hold more O atoms. Compared with Al mono-vacancy, there is a significant drop in the magnitude of oxygen trapping energy within the Al divacancy, but the number of O atoms captured by $2V_{Al-Al}$ does not increase significantly. This is mainly because the formation of Al vacancies causes Al atoms to diffuse out from their original position, and these Al atoms combine easily with O impurities to form a protective $Al_2O_3$ layer on the surface of $Ti_3AlC_2$, which effectively inhibits the further permeation of O atoms into the material, thus effectively inhibiting further oxidation. This also explains the periodic oscillation of O trapping energy within Al vacancy. Therefore, the oxygen capture mechanism involves both the attraction of vacancy and the inhibition of oxide film, which make the trapping process of O atoms sufficiently complex and significantly different from that of the H/He atoms. Ultimately, when O atoms exceed a critical number, the two types of interactions tend to be in equilibrium so that the number of O atoms in $Ti_3AlC_2$ is saturated. In addition, it has been reported that $^{50}$ the increase in O concentration has a significant impact on the increase of elastic modulus and the change of electronic properties. Therefore, it is possible to adjust the concentration of O atoms diffused into the material by changing the type and amount of vacancy in $Ti_3AlC_2$, so as to achieve the effect of tuning the material properties. Our calculation results provide a new insight and solution for tuning the material properties.

At the same time, we investigated the stable configurations of $nO-V_{Al}$ and $nO-2V_{Al-Al}$ complexes, which are illustrated in Fig. 3 and 4, respectively. In Fig. 3, for the $2O-V_{Al}$ complex, two O atoms prefer to occupy the equivalent $I_{tetr}-2$ sites residing on both sides of the Al vacancy, forming a symmetrical dumbbell structure. The distance between these two O atoms is about 2.47 Å, which is much larger than that in a $O_2$ molecule (1.23 Å). Meanwhile, the trapping energy for the second O atom is $-0.60$ eV, which is lower than that of the first O or the third O atom within $V_{Al}$. This implies that $2O-V_{Al}$ is the predominant complex in $Ti_3AlC_2$. For the $9O-V_{Al}$ complex, all O atoms tend to stay at the surrounding $I_{tetr}-2$ sites. However, it is clear that the O atoms are not evenly distributed around the Al vacancy, which usually distribute on one side of the vacancy. This causes the significant shift of the adjacent Al atoms on one side of the vacancy, which is consistent with the observed disorder in the Al layer in a previous experiment. $^{51}$ Meanwhile, the ninth O atom has a relatively high trapping energy of $-0.06$ eV. In the configuration of $15O-V_{Al}$, the Al vacancy is uniformly surrounded by trapped O atoms. These O atoms are regularly divided into two layers, which are interspersed between the Al-Ti atomic layers. Besides, Al atoms around the vacancy are shifted to different degrees, and the uniform distribution of O atoms makes the orientation of surrounding Al atoms towards the vacancy, forming a regular circle around the vacancy.

In Fig. 4, for the $2O-2V_{Al-Al}$ complex, the occupation of O atoms is consistent with that of O within $2O-V_{Al}$, and the trapping energy for the second O atom is $-0.74$ eV. In the $12O-2V_{Al-Al}$ configuration, two Al vacancies are uniformly surrounded by the trapped O atoms with a strong symmetry. Meanwhile, the $2V_{Al-Al}$ divacancy has the lowest trapping energy of $-0.98$ eV for the twelfth O atom, so the $12O-2V_{Al-Al}$ complex is probably the most predominant among all $nO-mV$ complexes. For the $17O-2V_{Al-Al}$ complex, the continuously trapped O atoms reside on the vicinity of two Al vacancies and all tend to occupy the equivalent $I_{tetr}-2$ sites. The vicinity of $2V_{Al-Al}$ is so crowded that there is not enough space to hold more O atoms; therefore, the number of O atoms captured by $2V_{Al-Al}$ reaches saturation. It is found that the O trapping energy is closely related to the regular distribution of O atoms. These complex clusters with symmetrical structure tend to have lower trapping energy, which are usually the predominant complexes in $Ti_3AlC_2$. In these configurations, the distance between any

![](./images/812507272553955329_4.jpg)

Fig. 3 Atomic configurations for different numbers of O atoms trapped in the $V_{Al}$ monovacancy. Blue spheres, pink spheres, and red spheres denote Ti atoms, Al atoms and O atoms, respectively. The black squares denote Al vacancies.

![](./images/812507272553955329_5.jpg)

Fig. 4 Atomic configurations for different numbers of O atoms trapped in the $2V_{Al-Al}$ divacancy. Blue spheres, pink spheres, and red spheres denote Ti atoms, Al atoms and O atoms, respectively. The black squares denote Al vacancies.

two O atoms is larger than that in an $O_2$ molecule, which indicates that the $O_2$ molecule cannot be formed in these complexes.

### 3.4 Interaction between O and H/He impurity
The structural materials of the reactor are not only exposed to high-temperature oxidation, but also inevitably withstand long-term irradiation. A large number of soluble impurity O atoms will embed in the material; meanwhile, impurity atoms (H/He) can be continuously produced from $(n,p)$ and $(n,\alpha)$ transmutation reactions in the nuclear reactor. Therefore, the interaction between O and H/He atoms in $Ti_3AlC_2$ is studied here to explore the effects of irradiation defects and oxidation on the microstructure. As shown in previous studies that H atom tends to occupy the $I_{tetr}$-2 site, and He atom tends to occupy the $I_{hex}$-1 site in bulk $Ti_3AlC_2$, we firstly place the H/He atom into the corresponding optimal interstitial site, respectively, and then add an O atom around the primary H/He atom, so as to study the formation energies of O at different interstitial sites around a single H/He atom in bulk $Ti_3AlC_2$. To analyze the defect-defect interactions, the binding energy is calculated using eqn (3) and the results are shown in Table 5.

It is noted that the formation energies of all interstitial O atoms are negative, which indicates that the insertion of O atom around primary H/He is thermally favorable. The O atom around H still tends to occupy the $I_{hex}$-1 site with a formation energy of $-3.71$ eV. In addition, the formation energies of different interstitial O atoms around H are close to that of O in the perfect cell. On the contrary, the O atom around He tends to occupy the $I_{tetr}$-2 site with the lowest formation energy of $-4.13$ eV. Meanwhile, the formation energies of different interstitial O atoms around He are greatly reduced compared with that of O in a perfect cell. This indicates that the impurity He atom could have a greater influence on the O implantation. From the perspective of the interaction between defects, only the interaction between $Hex_3$-O and H exhibits weak attraction, other interstitial O and H are all mutually repulsive, and the greatest repulsive interaction exists between $Tetr_2$-O and H. On the contrary, strong attraction is exhibited between all interstitial O and He, and $Hex_3$-O has the greatest attraction interaction with He. It is obvious that H-O and He-O have completely different interaction mechanisms. Impurity He atoms have a greater influence on O implantation and could reduce the formation energy of O, which is mainly attributed to the strong attraction between He and O.

Next, we study the binding of O to multiple H/He atoms and the stability of O-$n$H and O-$n$He clusters. When a single O atom is placed at the optimal interstitial site, the possibility of interstitial H/He atom clustering in $Ti_3AlC_2$ is determined by placing the H/He atoms one by one at different interstitial sites, the interstitial H/He atoms close to the primary O atom are investigated to find the lowest-energy site. To determine the number of H/He atoms that a primary O atom could accomodate, we calculate the total trapping energy of H/He atoms migrating to the primary O atom, which is defined as

$$
E^{\text{trap}}(X_n) = E(n\text{H/He,O}) - E(\text{O}) - n[E(\text{H/He}_{\text{int}}) - E(\text{ref})]
\tag{5}
$$

where $E(n\text{H/He,O})$ is the energy of $Ti_3AlC_2$ with $n$H/$n$He atoms and a single O atom, and $E(\text{O})$ and $E(\text{H/He}_{\text{int}})$ are the energies of system with one O or H/He atom in the corresponding most stable interstitial site, respectively. By this definition, a negative trapping energy represents an attractive interaction. The calculated total trapping energy is displayed in Fig. 5. Overall, the total trapping energies for O-$n$H complexes are much larger than those of O-$n$He complexes, indicating that the primary O atom has a stronger trapping ability to He impurity atoms. For O-$n$H clusters, all total trapping energies are positive except for the O-1H cluster, which confirms that there are strong repulsive interactions between O and multiple H atoms. When the first H atom is close to primary O, it remains in the nearby $I_{tetr}$-2 site with a negative trapping energy of $-0.04$ eV, which is probably the most stable configuration in all O-$n$H clusters. For O-2H and O-3H clusters, the total trapping energies of two configurations are small positive values of 0.09 eV and 0.14 eV, respectively. As more H atoms are implanted into the space around O, the total trapping energy begins to increase dramatically, indicating that the capturing for more H atoms is energetically unfavorable and the O-$n$H clusters are less thermally stable than the O-1H clusters in $Ti_3AlC_2$. Recent experimental studies$^{52}$ have reported that O can be regarded as the trapping sites in metal, which makes a large amount of H isotope ions aggregate and further form H blisters. Obviously, the trapping mechanism of O to H atoms in $Ti_3AlC_2$ is different

<table>
<caption>Table 5 Formation energies of O at different interstitial sites around a single H/He atom and binding energies between O and H/He in bulk $Ti_3AlC_2$</caption>
<thead>
<tr>
<th colspan="2">Configurations</th>
<th>$Hex_1$-O</th>
<th>$Tetr_2$-O</th>
<th>$Hex_3$-O</th>
<th>$Oct_4$-O</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Pre-H</td>
<td>Formation energy</td>
<td>−3.71</td>
<td>−2.75</td>
<td>−2.51</td>
<td>−2.47</td>
</tr>
<tr>
<td>Binding energy</td>
<td>0.21</td>
<td>0.98</td>
<td>−0.22</td>
<td>0.37</td>
</tr>
<tr>
<td rowspan="2">Pre-He</td>
<td>Formation energy</td>
<td>−3.35</td>
<td>−4.13</td>
<td>Unstable</td>
<td>−2.99</td>
</tr>
<tr>
<td>Binding energy</td>
<td>−2.05</td>
<td>−3.03</td>
<td>−3.33</td>
<td>−2.77</td>
</tr>
</tbody>
</table>

![](./images/812507272553955329_6.jpg)

Fig. 5 The total trapping energy for the H/He atom as a function of the number of H/He atoms trapped by primary O atom in $Ti_3AlC_2$.

from that in metals. On the other hand, all total trapping energies of O-$n$He clusters are negative, indicating that the interaction between $n$He and O atoms is a strong attraction. For n from 1 to 8, the O-$n$He clusters tend to be more stable because the total trapping energy drops dramatically from $-0.46$ to $-3.77$ eV. All of these imply that the process of capturing of He atoms by primary O atoms is exothermic, and the O atom could bind a large number of He atoms to form stable O-$n$He clusters. Therefore, O atoms could cause more serious He embrittlement in Ti₃AlC₂, making the performance of the material more sensitive to the implantation of He impurity.

### 3.5 The trapping behaviour of H atoms within vacancy-O and vacancy-2O complexes
A large number of H atoms are widely implanted in Ti₃AlC₂ under irradiation, so H atoms easily encounter the monovacancy-O (V-O)/divacancy-O (2V-O) defect and form V-O-$H_n$/2V-O-$H_n$ complexes. To explore the effect of impurity O on the trapping ability of vacancy to H atoms as well as the stability of the V-O-$H_n$ and 2V-O-$H_n$ complexes, we put H atoms into different interstitial sites within vacancy-O defect one by one. Then the system was relaxed to find the most stable configuration for every H atom. To determine the number of H atoms that different complexes could accommodate, we calculated the trapping energy of n-th H atom migrating to the complexes. The calculated trapping energies of V-O-$H_n$/2V-O-$H_n$ complexes and that of alone vacancy defects for comparison are displayed in Fig. 6(a). In general, all of the trapping energies increase monotonously as the number of H atoms increases, but the variation trend of H trapping energy within different complexes is obviously different. For the V-O complex, the trapping energy for the first H atom is $-0.71$ eV. When the second H atom is added into the space of the V-O complex, the trapping energy immediately becomes positive, indicating that this capture process is energetically unfavorable. Therefore only one H atom could be trapped by the V-O complex, which is far less than H atoms captured by the Al monovacancy. For the 2V-O complex, capturing the first H atom requires the lowest trapping energy of $-0.71$ eV, while the trapping energy for the fourth H atom increases to $-0.03$ eV. When more H atoms are implanted, the H trapping energy begins to become positive, indicating that the fifth H atom is energetically favorable to occupy the Iₜₑₜᵣ-2 interstitial site far away from the complex, rather than being captured by the 2V-O complex. Therefore, the 2V-O complex could hold up to four H atoms. Compared with the simple Al divacancy, which could capture seven H atoms, the addition of O impurity greatly reduces the trapping ability of the divacancy to H atoms. All these results suggest that vacancy could be used as the trapping center to capture the surrounding H atoms, and the number of trapped H atoms increases significantly with increase in the number of vacancies. On the other hand, the O impurity could effectively inhibit the binding of vacancy to more H atoms, making it difficult for H atoms to form clusters in Ti₃AlC₂, which significantly reduces the growth and swelling of H bubbles.

Since Al divacancy could attract multiple O atoms, we further explored the interaction of H atoms with the 2V-2O complex and the stability of the 2V-2O-$H_n$ clusters. Previous calculations have investigated the most stable configuration of the 2V-2O complex, in which the two O atoms are located at the equivalent Iₜₑₜᵣ-2 sites on the top and down sides of one Al vacancy, respectively. Next, H atoms are continuously placed into the most stable interstitial site around the 2V-2O complex one by one. The calculated trapping energy is displayed in Fig. 6(b). Due to the insertion of the second O atom, the H trapping energy of the 2V-2O complex significantly increases compared to that of the 2V-O complex. Obviously, the number of O atoms around the vacancy has a certain influence on the trapping process of H atoms. For the 2V-2O complex, the increasing trend of the trapping energy with the number of H atoms is very obvious, in which the trapping energy for the first H atom is $-0.45$ eV, while the trapping energy for the third H is increased to $-0.02$ eV. When the fourth H atom is added into the space of the 2V-2O complex, the trapping energy becomes positive, suggesting that the 2V-2O complex could only hold up to three H atoms. All of these results imply that impurity O strongly affects the stability and dissociation of the vacancy-$H_n$ complexes. The results are in good agreement with the previous

![](./images/812507272553955329_7.jpg)

Fig. 6 Trapping energy of H atom as a function of the number of H atoms trapped by vacancy-O complexes (a) and vacancy-2O complexes (b) in Ti₃AlC₂.

experiment, $^{53}$ which investigated the thermal stability of bulk $Ti_{3}AlC_{2}$ at high temperatures (700-1000 °C) in hydrogen atmosphere (low oxygen pressure) using scanning electron microscope and X-ray diffraction techniques, and it was found that the reacted samples were intact and cracks were not formed on the surface; meanwhile, hydrides were not detected in the experiments. We speculate that the thermal stability of $Ti_{3}AlC_{2}$ at high temperatures in hydrogen may be attributed to the formation of oxides on the surface of specimens, which will have a strong rejection effect on the implantation of H.

We have previously investigated the trapping behaviour of H within the $2V_{Al-Al}-He$ complex in $Ti_{3}AlC_{2},^{43}$ which mentioned that the $2V_{Al-Al}-He$ complex could capture up to four H atoms. By comparison the H trapping energy of $2V_{Al-Al}-O$ and $2V_{Al-Al}-He$, we found that O and He could effectively inhibit the trapping behaviour of vacancy on H atoms, and the inhibition effects of these two types of impurity atoms on the H aggregation are approximately equal. Furthermore, in order to understand the effect of O and He co-existence on the trapping behaviour of vacancy on H atoms, here, all defects are taken into account to explore the trapping energy of H atoms within the more complex 2V-O-He cluster. The calculated trapping energy as a function of the number of H atoms within the 2V-O-He complex is also illustrated in Fig. 6b. It can be seen that the H trapping energy increases sharply with the increase in H atomic number, and the binding strength of vacancy to H atoms is significantly reduced, so that the $2V_{Al-Al}-O-He$ complex could only hold up to two H atoms. This result implies that the He-O synergistic interaction greatly reduces the trapping capacity of vacancy to H atoms, which could suppress further aggregation of H atoms and block hydrogen embrittlement and volume swelling.

![](./images/812507272553955329_8.jpg)

Fig. 7 Stable configurations and charge-density differences for different complexes. Blue spheres, pink spheres, gray spheres, orange spheres, black spheres and green spheres denote Ti atoms, Al atoms, C atoms, O atoms, He atoms and H atoms, respectively. Blue and yellow curved isosurfaces stand for the charge density of about -0.01 e $\AA^{-3}$ and 0.01 e $\AA^{-3}$, respectively.

The stable configurations and charge-density differences for multiple H atoms trapped within different defects are displayed in Fig. 7. The charge-density difference (isosurface value) was obtained by subtracting the charge densities of the system with impurities from the charge densities of reference system without impurities. At first, there is a uniform and large isosurface of charge density surrounding the $V_{Al}$ and $2V_{Al-Al}$ vacancies in the absence of any impurity atoms. As more and more impurity atoms are inserted into the vacancy space, it is obvious that the surface of optimal charge density shrinks sharply so that there are no available optimal-density sites to contain excess H atoms. For the V-O-H complex, O and H atoms occupy the equivalent $I_{tetr}$-2 sites on the top and down sides of Al vacancy, respectively. Meanwhile, charge-density differences show strong bonding between vacancy and surrounding O/H atoms, and vacancy-O cluster exhibits a stronger interaction than vacancy-H in $Ti_{3}AlC_{2}$. In the configuration of the 2V-O-4H complex, the two Al vacancies are in the nearest neighbor position, where the charge density surfaces of the two Al vacancies do not overlap, indicating that the interaction between the vacancies is very weak. The O atom tends to occupy the $I_{tetr}$-2 site above one Al vacancy, and four trapped H atoms are distributed unevenly around the 2V-O cluster, resulting in obvious shifts of adjacent Al atoms. There is no chemical bonding between the adjacent O and H atoms from the perspective of charge-density differences. For the 2V-2O-3H complex, two O atoms occupy the equivalent $I_{tetr}$-2 sites on the top and down sides of one Al vacancy, and the distance between them is 2.51 $\mathring{A}$, which is much larger than the distance between the O atoms in the $O_{2}$ molecule. The charge density differences show that two O atoms together form an symmetric dumbbell-like structure with the Al vacancy, suggesting that the vacancy interacts strongly with multiple O atoms and could form stable vacancy-O clusters. In addition, the preferential interstitial sites of H atoms remain unchanged in the presence of the second O atom, where all H atoms still tend to occupy the equivalent $I_{tetr}$-2 sites around the complex. The insertion of the second O atom only changes the trapping energy of H atom, making it easier for H atoms to escape from the binding of the vacancy-O cluster. This is mainly because O atoms take up most of the vacancy space, so that there are less available optimal-density sites to accommodate more H atoms. In the configuration of the 2V-O-He-2H complex, the distribution of all impurity atoms is very regular. The O and He atoms are located at the equivalent $I_{tetr}$-2 sites on the top and down sides of one Al vacancy, Meanwhile, the two captured H atoms occupy the top and down sides of another Al vacancy. In addition, O and He atoms together form an asymmetric dumbbell-like structure with the Al vacancy, the overlap of the charge density surfaces between them suggests that there is a strong attraction between vacancy and O/He atoms; they also could form a stable vacancy-O-He cluster. In all of these configurations, the charge density surfaces of any two H atoms do not overlap, and the distances between them are all larger than that in a $H_{2}$ molecule, which indicates that the $H_{2}$ molecule cannot be formed in these structures.

### 3.6 The effects of O atom concentration on the irradiation defects
The O atoms as typical solute impurities have strong interaction with vacancies/H/He in $Ti_{3}AlC_{2}$, and could form stable complexes

![](./images/812507272553955329_9.jpg)

Fig. 8 The defect formation energy for Al vacancy and H/He atom nearest to a primary Al vacancy as a function of the number of O atoms in $Ti_3AlC_2$.

affecting the evolution of the microstructure. In order to investigate the effects of O atom concentration on irradiation defects and material properties, we calculated the formation energy of irradiation defects with different O atom numbers. As mentioned above, an Al vacancy could be readily formed in $Ti_3AlC_2$. Therefore, we firstly introduce an Al vacancy in $Ti_3AlC_2$. Next, we let the vacancy capture different numbers of O atoms. Finally, the defect formation energies of the secondary vacancy and H/He impurity are calculated for the Al, H, and He atoms nearest to the primary Al vacancy, respectively. The defect formation energies for Al vacancy and H/He atom as a function of the number of O atoms within the primary Al vacancy are shown in Fig. 8.

It can be seen that the formation energies of the second Al vacancy are significantly influenced by the O impurity content. When the primary Al vacancy contain no O atom, the secondary Al vacancy formation energy is approximately −1.77 eV. With increase in the number of O atoms, the vacancy formation energy rapidly decreases. When fifteen O atoms are located in the space around the primary Al vacancy, the second vacancy formation energy has been reduced to −3.34 eV, indicating that O atoms could promote the formation of Al vacancy, which could be well explained by the strong attraction of O impurity to Al atoms. The implanted O atoms cause Al atoms in $Ti_3AlC_2$ to break away from their original constraint and migrate towards the O atoms, thus forming a dense $Al_2O_3$ layer on the surface of $Ti_3AlC_2$. Meanwhile, a large number of vacancies are formed in the original position of Al atom due to the migration of Al. For He impurity, the defect formation energy is always positive and fluctuates greatly with the number of O atoms. When no O atom is captured by the primary Al vacancy, the He formation energy is approximately 0.70 eV. With increase in the number of captured O atoms, the formation energy changes periodically, and three peaks are formed at 2O-V, 8O-V and 13O-V complexes, with the formation energies of 1.63 eV, 2.53 eV and 2.35 eV, respectively. Eventually, when fifteen O atoms fill the space around the Al vacancy, the He formation energy has been reduced to 0.40 eV. This suggests that O atoms could promote the formation of He, but the effect is not significant. And the He formation energy is periodic with respect to the number of O atoms. In contrast, the formation energy of H impurity increases with increase in the number of O atoms, from −0.79 eV without any O atoms to −0.44 eV with fifteen O atoms. This is mainly due to the strong repulsive interaction between O and H. Therefore, the O atom concentration has a completely different effect mechanism for the formation of vacancy, H, and He irradiation defects, where O could promote the formation of vacancy and have a periodic influence on He formation energy; however, it has an inhibitory effect on the formation of H clusters.

## 4 Summary and conclusions

The synergistic interaction between irradiation defects and oxygen impurities in the microstructure of $Ti_3AlC_2$ is studied using first-principles calculations. The trapping progress and occupation of O atoms within different defects are discussed. On the other hand, the effect of O impurities on H/He clusters is investigated, and the stable configurations of vacancy-$m$O-$n$H complexes are displayed to better understand the evolution of the microstructure. The predominant results are described below. (1) An individual O atom prefers to occupy the $I_{hex}$-1 interstitial site, and these O atoms are more likely to combine with Al atoms to form the $Al_2O_3$ protective layer, which could effectively inhibit the further implantation of impurity atoms. Compared with impurity H/He atoms at different interstitial sites, the O atom has a lower formation energy, which indicates that O atoms will be present in $Ti_3AlC_2$ as the predominant impurity. (2) The occurrence of vacancy greatly changes the occupation and formation energy of the O atom; the O atom always tends to occupy the $I_{tetr}$-2 site around the vacancies, and the formation energies of the O atom within these vacancies are all much smaller than that of individual O in bulk $Ti_3AlC_2$. Moreover, the appearance of C vacancy could significantly reduce the formation energy of O atoms and make O atoms more inclined to occupy the center of the C vacancy. (3) The trapping process of the O atom is sufficiently complex and significantly different from that of H/He atoms, which involves both the attraction of vacancy and the inhibition of oxide film, so that the trapping energy presents a small periodic oscillation. In addition, the vacancy has a stronger interaction with soluble impurity O and could capture more O atoms compared with H/He atoms, where $V_{Al}$ and $2V_{Al-Al}$ could hold up to fifteen and eighteen O atoms, respectively. (4) The interaction between H–O is mainly repulsion, while He–O exhibits strong attraction. Thus, the O atom has an inhibitory effect on the formation of an H cluster, while it could bind more He atoms to form a large number of He bubbles. (5) The insertion of O impurity greatly reduces the trapping ability of vacancy to H atoms, where the V–O, 2V–O and 2V–2O complexes could only hold up to one, four and three H atoms, respectively. In addition, O and He have a synergistic interaction for inhibiting the aggregation of H clusters, where the 2V–O–He complex could only capture two H atoms. (6) The O atom concentration has a completely different effect mechanism for various irradiation

defects, where O could promote the formation of vacancy and have a periodic influence on He formation energy, but it has an inhibitory effect on the formation of H cluster.

The present results will contribute to better understanding of the evolution of microstructure and performance differences of $Ti_3AlC_2$ under irradiation and oxidation conditions. Oxygen incorporation within the MAX phase material may be beneficial not only for tuning properties, but would also allow for the formation of a protective layer on the surface of the material when self-healing is required. This oxidation induced self-healing mechanism is attractive as the MAX phase is protected and self-healing is achieved without the addition of a secondary material or chemical reagent. In addition, we also provide future possibilities for designing multifunctional quaternary MAX phases by controlling the generation and migration of intrinsic defects.

## Conflicts of interest
There are no conflicts to declare.

## Acknowledgements
This work was supported by the National Key Research and Development Program of China (Grant No. 2016YFB0200504), the National Natural Science Foundation of China (Grant No. 11905272), the Strategic Priority Research Program of Chinese Academy of Sciences (Grant No. XDA21010202), the Doctoral Research Foundation of Longdong University (Grant No. XYBY202016), and the Guangdong Laboratory of Advanced Energy Science and Technology.

## References
1 J. Roth, E. Tsitrone, A. Loarte, Th Loarer, G. Counsell, R. Neu, V. Philipps and S. Brezinsek, *J. Nucl. Mater.*, 2009, **390-391**, 1-9.

2 G. Janeschitz, *J. Nucl. Mater.*, 2001, **290-293**, 1-11.

3 J. B. Condon and T. Schober, *J. Nucl. Mater.*, 1993, **207**, 1-24.

4 I. I. Arkhipov, S. L. Kanashenko, V. M. Sharapov, R. Kh Zalavutdinov and A. E. Gorodetsky, *J. Nucl. Mater.*, 2007, **363-365**, 1168-1172.

5 D. S. Gelles and H. L. Heinisch, *J. Nucl. Mater.*, 1992, **191**, 194-198.

6 V. Chakin, R. Rolli, A. Moeslang, P. Vladimirov, P. Kurinskiy, S. van Til, A. J. Magielsen and M. Zmitko, *Fusion Eng. Des.*, 2013, **88**, 2309-2313.

7 L. Hu, Y. G. Li, C. G. Zhang and Z. Zeng, *RSC Adv.*, 2015, **5**, 65750-65756.

8 Y. G. Zhang, Y. W. You, D. D. Li, Y. C. Xu, C. S. Liu, B. C. Pan and Z. G. Wang, *Phys. Chem. Chem. Phys.*, 2015, **17**, 12292.

9 A. Herklotz, S. F. Rus, S. Kc, V. R. Cooper, A. Huon, E. J. Guo and T. Z. Ward, *Appl. Phys. Lett.*, 2017, **5**, 066106.

10 H. M. Chung, B. A. Loomis and D. L. Smith, *J. Nucl. Mater.*, 1996, **239**, 139.

11 M. Hatakeyama, T. Muroga, S. Tamura and I. Yamagata, *J. Nucl. Mater.*, 2011, **417**, 303.

12 T. Muroga, in *Comprehensive Nuclear Materials*, ed. R. J. M. Konings, Elsevier, Oxford, 2012, p. 391.

13 N. Nita, K. Miyawaki and H. Matsui, *J. Nucl. Mater.*, 2007, **367-370(Part A)**, 505-510.

14 P. B. Zhang, T. T. Zou, W. B. Liu, Y. Yin and J. J. Zhao, *J. Nucl. Mater.*, 2018, **505**, 119.

15 P. B. Zhang, J. H. Ding, D. Sun, Y. C. Yang, S. S. Huang and J. J. Zhao, *Compos. Mater.*, 2019, **160**, 180.

16 Y. Yu, Q. F. Han, Z. Y. Zhou, Y. M. Ma, S. Jia and Y. L. Liu, *J. Nucl. Mater.*, 2015, **466**, 194-200.

17 X. L. Zhu, C. L. Wang, Z. C. Meng, Y. L. Wang, H. Q. Deng, W. S. Duan and L. Yang, *J. Nucl. Mater.*, 2019, **525**, 7-13.

18 L. Sun, S. Jin, H. B. Zhou, Y. Zhang and G. H. Lu, *Compos. Mater. Sci.*, 2015, **102**, 243.

19 A. Alkhamees, H. B. Zhou, Y. L. Liu, S. Jin, Y. Zhang and G. H. Lu, *J. Nucl. Mater.*, 2013, **437**, 6-10.

20 M. W. Barsoum, *Prog. Solid State Chem.*, 2000, **28**, 201-281.

21 Q. D. Xiao and Z. L. Lv, *Adv. Appl. Ceram.*, 2012, **111**, 202-207.

22 A. G. Zhou, C. A. Wang and Y. Huang, *Mater. Sci. Eng., A*, 2003, **352**, 333-339.

23 X. H. Wang and Y. C. Zhou, *Acta Mater.*, 2002, **50**, 3141-3149.

24 X. H. Wang and Y. C. Zhou, *J. Mater. Chem.*, 2002, **12**, 455-460.

25 B. Cui, R. Sa, D. D. Jayaseelan, F. Inam, M. J. Reece and W. E. Lee, *Acta Mater.*, 2012, **60**, 1079-1092.

26 M. Baben, L. Shang, J. Emmerlich and J. M. Schneider, *Acta Mater.*, 2012, **60**, 4810-4818.

27 X. M. Liu, M. Le Flem, J. L. Bechade and I. Monnet, *J. Nucl. Mater.*, 2010, **401**, 149-153.

28 J. C. Nappe, I. Monnet, P. Grosseau, F. Audubert, B. Guilhot, M. Benabdesselam, L. Thome and M. Beauvy, *J. Nucl. Mater.*, 2011, **409**, 53-61.

29 J. R. Xiao, T. F. Yang, C. X. Wang, J. M. Xue and Y. G. Wang, *J. Am. Ceram. Soc.*, 2015, **98**, 1323-1331.

30 J. M. Wang, B. Liu, J. Y. Wang and Y. C. Zhou, *Phys. Chem. Chem. Phys.*, 2015, **17**, 8927-8934.

31 C. Wang, T. Yang, S. Kong, J. Xiao, J. Xue, Q. Wang, C. Hu, Q. Huang and Y. Wang, *J. Nucl. Mater.*, 2013, **440(1-3)**, 606.

32 C. Chen, H. B. Zhang, S. M. Peng, X. G. Long and J. G. Zhu, *Chin. J. Mater. Res.*, 2014, **28**, 858-864.

33 M. K. Patel, D. J. Tallman, J. A. Valdez, J. Aguiar, O. Anderoglu, M. Tang, J. Griggs, E. G. Fu, Y. Q. Wang and M. W. Barsoum, *Acta Mater.*, 2014, **77**, 1-4.

34 M. Bugnet, V. Mauchamp, P. Eklund, M. Jaouen and T. Cabioch, *Acta Mater.*, 2014, **61**, 7348.

35 Q. Qi, G. J. Cheng, L. Q. Shi, D. J. O'Connor, B. V. King and E. H. Kisi, *Acta Mater.*, 2014, **66**, 317.

36 G. Kresse and J. Hafner, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1993, **47(1)**, 558.

37 G. Kresse and J. Furthmüler, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1996, **54(16)**, 11169.

38 P. E. Blöhl, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1994, **50(24)**, 17953.

39 M. A. Pietzka and J. C. Schuster, *J. Phase Equilib.*, 1994, **15**, 392.

40 Y. G. Xu, X. J. Bai, X. H. Zha, Q. Huang, J. He, K. Luo, Y. H. Zhou, T. C. Germann, J. S. Francisco and S. Y. Du, *J. Chem. Phys.*, 2015, **143**, 114707.

41 S. T. Yang, N. W. Hu, X. Q. Gou, C. L. Wang, X. L. Zhu, W. S. Duan and L. Yang, *RSC Adv.*, 2016, **6**, 59875.

42 Y. C. Zhou, X. H. Wang, Z. M. Sun and S. Q. Chen, *J. Mater. Chem.*, 2001, **11**, 2335.

43 Z. C. Meng, C. L. Wang, J. T. Liu, Y. L. Wang, X. L. Zhu, L. Yang and L. Huang, *Phys. Chem. Chem. Phys.*, 2020, **22**, 18040-18049.

44 J. R. Xiao, C. X. Wang, T. F. Yang, S. Y. Kong, J. M. Xue and Y. G. Wang, *Nucl. Instrum. Methods Phys. Res., Sect. B*, 2013, **304**, 27.

45 M. Bugnet, T. Cabioch, V. Mauchamp, Ph. Guerin, M. Marteau and M. Jaouen, *J. Mater. Sci.*, 2010, **45**, 5547-5552.

46 T. Liao, J. Y. Wang and Y. C. Zhou, *Scr. Mater.*, 2008, **59**, 854-857.

47 J. Rosen, P. O. A. Persson, M. Ionescu, A. Kondyurin, D. R. McKenzie and M. M. M. Bilek, *Appl. Phys. Lett.*, 2008, **92**, 064102.

48 P. O. A. Persson, J. Rosen, D. R. Mckenzie and M. M. M. Bilek, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2009, **80**, 092102.

49 J. J. Liu, C. L. Wang, X. L. Zhu, J. T. Liu, X. M. Zhang, X. Q. Gou, W. S. Duan and L. Yang, *Phys. Chem. Chem. Phys.*, 2018, **10**, 1039.

50 M. Dahlqvist, B. Alling, I. A. Abrikosov and J. Rosen, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2010, **81**, 024111.

51 M. W. Barsoum, T. El-Raghy, L. Farber, M. Amer, R. Christini and A. Adams, *J. Electrochem. Soc.*, 1999, **146**, 3919-3923.

52 K. O. E. Henriksson, K. Nordlund, A. Krasheninnikov and J. Keinonen, *Appl. Phys. Lett.*, 2005, **87**, 163113.

53 C. Chen, H. B. Zhang, S. M. Peng, L. J. Zhao and J. G. Zhu, *J. Inorg. Mater.*, 2014, **29**, 864-868.

---

This journal is © the Owner Societies 2021

*Phys. Chem. Chem. Phys.*, 2021, **23**, 5340-5351 | **5351**