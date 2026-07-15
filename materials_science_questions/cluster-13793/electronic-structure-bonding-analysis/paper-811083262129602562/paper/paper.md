# First-principles study of Zr-N crystalline phases: phase stability, electronic and mechanical properties†

Shuyin Yu,*\(^{ab}\) Qingfeng Zeng,\(^{ab}\) Artem R. Oganov,\(^{bcde}\) Gilles Frapper,\(^f\) Bowen Huang,\(^f\) Haiyang Niu\(^c\) and Litong Zhang\(^a\)

Using a variable-composition *ab initio* evolutionary algorithm, we investigate stability of various Zr-N compounds. Besides the known ZrN and Zr₃N₄, new candidate structures with Zr : N ratios of 2 : 1, 4 : 3, 6 : 5, 8 : 7, 15 : 16, 7 : 8 and 4 : 5 are found to be ground-state configurations, while Zr₃N₂ has a very slightly higher energy. Besides Zr₂N, the newly discovered ZrₓNᵧ compounds adopt rocksalt structures with ordered nitrogen or zirconium vacancies. The electronic and mechanical properties of the zirconium nitrides are further studied in order to understand their composition-structure-property relationships. Our results show that bulk and shear moduli monotonically increase with decreasing vacancy content. The mechanical enhancement can be attributed to the occurrence of more Zr-N covalent bonds and weakening of the ductile Zr-Zr metallic bonds. These simulations could provide additional insight into the vacancy-ordered rocksalt phases that are not readily apparent from experiments.

## 1 Introduction
Group IVB transition metal (TM = Ti, Zr and Hf) nitrides have been widely used in cutting tools and as wear-resistant coatings, because of their excellent properties such as high hardness and strength, high melting points, excellent thermal conductivity, and good chemical stability.\(^{1-4}\) Formally, their mononitrides adopt the rocksalt structure, but may show significant variation in composition, both towards cation and anion enrichment.\(^1\) Such nonstoichiometry widely exists in group IV/V transition metal oxides, nitrides and carbides, due to the formation of structural vacancies.\(^5\) The concentration of vacancies can be up to 50 at%. Their microstructures are usually controlled by the co-precipitation of nonstoichiometric phases, and the mechanical behavior is dependent on the vacancy concentration.

Unlike carbides, not only nonmetal vacancies exist, but structure can also tolerate metal atom vacancies since metal atom oxidation state can reach +4.\(^6\) Experimental investigations of nonstoichiometric TM nitrides (TM = Ti, Zr, Hf, V, Nb and Ta) have been conducted intensely for more than thirty years.\(^{7-10}\) About twenty ordered carbides and nitrides have been found.\(^1\) However, it has not yet been possible to construct a single phase diagram of TM-C or TM-N systems at low temperatures (most of the available phase diagrams have been constructed above 1300–1500 K). In this paper, we explore stable compounds in the Zr-N system at ambient pressure and finite temperatures. To date, there is no comprehensive and inclusive computational investigation of phase stability in the Zr-N system.

Zirconium nitrides represent a rich family of phases where the stability and microstructures are still not completely understood. According to the phase diagram provided by Gribaudo *et al.*,\(^{11}\) ZrN and Zr₃N₄ can be stable at ambient conditions. In 2003, c-Zr₃N₄ with a Th₃P₄ structure was synthesized by Zerr *et al.* using diamond-anvil cell experiments at 16 GPa and 2500 K.\(^{12}\) This compound was expected to exhibit a very high Vickers hardness around 30 GPa, similar to that of γ-Si₃N₄. However, Kroll showed that hardness is just slightly harder than 14 GPa.\(^{13}\) Besides c-Zr₃N₄, an orthorhombic *Pnma* modification of Zr₃N₄ has been proposed.\(^{14}\) First-principles calculations show that o-Zr₃N₄ is energetically more stable than c-Zr₃N₄.\(^{15}\) However, both structures are metastable considering decomposition into ZrN and N₂.\(^{13}\) Besides, two nitrogen-rich phases ZrNₓ (1.06 < x < 1.23) with NaCl-type structures have been claimed by Juza *et al.* in 1964.\(^{16}\) However, precise stoichiometries and crystal structures are not known for their synthesized samples.

---

\(^{a}\)Science and Technology on Thermostructural Composite Materials Laboratory, Northwestern Polytechnical University, Xi'an, Shaanxi 710072, China. E-mail: yushuyin2014@gmail.com
\(^{b}\)International Center for Materials Discovery, Northwestern Polytechnical University, Xi'an, Shaanxi 710072, China
\(^{c}\)Department of Geosciences, Center for Materials by Design, Institute for Advanced Computational Science, State University of New York, Stony Brook, NY 11794-2100, USA
\(^{d}\)Skolkovo Institute of Science and Technology, 3 Nobel Street, Skolkovo 143025, Russia
\(^{e}\)Moscow Institute of Physics and Technology, Dolgoprudny, Moscow Region 141700, Russia
\(^{f}\)IC2MP UMR 7285, Université de Poitiers, CNRS, 4, rue Michel Brunet, TSA 51106, 86073 Poitiers Cedex 9, France

† Electronic supplementary information (ESI) available. See DOI: 10.1039/c6ra27233a

Here, we apply recently developed evolutionary algorithm USPEX to extensively explore the crystal structures and stoi- chiometries in the Zr-N system at ambient conditions, and then their phase stability at finite temperatures are evaluated. Furthermore, the electronic and mechanical properties of stable ZrₓNᵧ compounds are studied using density functional theory. Our work should provide guidance for experimental groups aiming to synthesize these new technologically useful materials.

## 2 Computational details

Searches for low-energy crystalline Zr-N structures were per- formed using evolutionary algorithm (EA) methodology imple- mented in the USPEX code¹⁷⁻¹⁹ in its variable-composition mode.²⁰ The energies and structural optimizations (including lattice shape, volume and atomic positions) were calculated by VASP package based on density-functional theory.²¹ The first generation contained 80 randomly produced candidate struc- tures, which were produced under the following constraints: (1) all possible stoichiometries were allowed, (2) the maximum number of atoms is 30 in the primitive cell. In the subsequent generations, each generation contained 60 structures, which were produced by applying heredity (50%), atom transmutation (20%), lattice mutation (15%) operators, while some structures were still randomly (15%). These are typical parameters for USPEX calculations, with which efficiency is known to be very high. Besides, we also performed a fixed-composition search for Zr₁₅N₁₆ which has 31 atoms in its primitive cell.

First-principles electronic structure calculations were carried out within the generalized gradient approximation (GGA) in the Perdew-Burke-Ernzerhof form.²² The interactions between ions and electrons were described by the projector-augmented-wave method²³ with a cutoff energy of 600 eV. Uniform Γ-centered k- points meshes with a resolution of $2\pi \times 0.03$ Å⁻¹ and Meth- fessel-Paxton electronic smearing²⁴ were adopted for the inte- gration in the Brillouin zone. These settings ensure convergence of the total energies to within 1 meV per atom. Structure relaxation proceeded until all forces on atoms were less than 1 meV Å⁻¹ and the total stress tensor was within 0.01 GPa of the target value.

Theoretical phonon spectra were calculated with the super- cell method using the PHONOPY package.²⁵ Hellmann-Feyn- man forces exerted on all atoms in supercells ($2 \times 2 \times 2$ of the unit cell) were calculated by finite atomic displacements of each symmetrically nonequivalent atom. Phonon dispersion rela- tions were then obtained by the diagonalization of the dynam- ical matrix. We used the quasiharmonic approximation to calculate the free energy of zirconium nitrides at finite temperatures. Free energy of a crystal was obtained as a sum of the static total energy, vibrational energy and configurational energy. Computational details are described in ESI.†

## 3 Results and discussion

### 3.1 Phase stability of the Zr-N system at finite temperatures

Thermodynamic stability of zirconium nitrides in the temper- ature range of 0-2000 K was quantified by constructing the thermodynamic convex hull, which is defined as the Gibbs free energy of formation of the most stable phases at each composition:

$$
\Delta G(\mathrm{Zr}_{x}\mathrm{N}_{y}) = [G(\mathrm{Zr}_{x}\mathrm{N}_{y}) - xG(\mathrm{Zr}) - yG(\mathrm{N})]/(x + y) \tag{1}
$$

Any phase located on the convex hull is considered to be thermodynamically stable (at $T = 0$ K, $G = H$) and at least in principle synthesizable.²⁶ In the case of zirconium nitrides, a series of stable compounds at various Zr:N ratios, *i.e.* $2:1$, $4:3, 6:5, 8:7, 1:1, 15:16, 7:8, 4:5$ have been discovered by our evolutionary searches at 0 K, shown in Fig. 1. The rocksalt ZrN with space group (SG) $Fm\overline{3}m$ was found to have the lowest enthalpy of formation. Besides ZrN, substoichiometric Zr₂N (SG: $P4_{2}/mnm$), Zr₄N₃ (SG: $C2/m$), Zr₆N₅ (SG: $C2/m$) and Zr₈N₇ (SG: $C2/m$) have also been found to be thermodynamically stable. For the missing composition Zr₃N₂, the lowest-energy structure is *Immm* with the enthalpy of formation lying very close to the convex hull at only 0.005 eV per atom, *i.e.* Zr₃N₂ is a metastable phase at 0 K.

Additionally, Juza *et al.* in 1964 have discovered two nitrogen- rich phases ZrNₓ ($1.06 < x < 1.23$) with rocksalt structures.¹⁶ The synthesized sample had a dark blue color and turned into metallic ZrN upon heating. Unfortunately, detailed stoichiom- etries and crystallographic information were not determined. Subsequent studies even questioned the existence of these two compounds.¹¹ From our evolutionary searches, we found these two compounds could be Zr₁₅N₁₆ ($x = 1.07$, SG: $P\overline{1}$) and Zr₄N₅ ($x = 1.25$, SG: $C2/m$). Their structures are composed of edge- sharing ZrN₆ and $\square$N₆ ($\square$ means Zr vacancy) octahedra, similar to the rocksalt ZrN structure. To the best of our knowledge, such nitrogen-rich nitrides have never been re- ported in other TM-N systems. For Zr₃N₄, the most stable structure has the orthorhombic *Pnma* symmetry,²⁷ which is

![](./images/811083262129602562_1.jpg)

Fig. 1 Convex hulls of the Zr-N system in the temperature range of 0-2000 K at ambient pressure. The solid squares represent stable structures, while open ones denote metastable structures. The solid $P6_{3}/mmc$ phase of Zr, $\alpha$-N₂ ($T = 0$ K) and N₂ gas ($T \geq 300$ K) were adopted as reference states.

energetically more favorable than the $Th_3P_4$-type structure by $\sim$0.019 eV per atom at 0 GPa and 0 K. We found it is thermo-dynamic metastable considering decomposition into ZrN and $N_2$ at ambient conditions. First-principles calculation shows that $o$-$Zr_3N_4$ will transform into $c$-$Zr_3N_4$ at $\sim$2 GPa (Fig. S2$\dagger$).

We have carefully calculated the temperature contribution to the phase stability of the new discovered zirconium nitrides from 0 K to 2000 K within the quasiharmonic approximation, as shown in Fig. 1. Note that for each stoichiometry, the space group/structure found at 0 K is kept for higher temperatures. The free energies of formation increase with increasing temperatures for all phases but at different rates, yielding a convex hull which changes with temperature. Our results show that $Zr_2N$, $Zr_8N_7$, ZrN and $Zr_{15}N_{16}$ will not lose their stability in the whole studied temperature range. The unstable $Zr_3N_2$ at 0 K will become stable at temperatures higher than $\sim$900 K, while for $Zr_4N_3$, $Zr_6N_5$, $Zr_7N_8$ and $Zr_4N_5$, the temperature contributions have negative effect on their structural stability. For example, the formation enthalpy of reaction $2Zr_4N_5$ (s) $\rightarrow$ $8ZrN$ (s) + $N_2$ (g) will become negative above 300 K, which means $Zr_4N_5$ should decompose into ZrN and $N_2$ gas at roughly room temperature if associated kinetic barrier allows this process, perfectly consistent with the results of Juza et al.¹⁶

Crystal structures of the representative zirconium-rich $Zr_6N_5$ and nitrogen-rich $Zr_4N_5$ are schematically shown in Fig. 2, while other structures and their corresponding phonon dispersion curves are shown in Fig. S3 and S4.$\dagger$ No imaginary phonon frequencies are found, indicating their dynamical stability. The detailed crystallographic data, enthalpies and zero-point energies are listed in Table S1.$\dagger$ From Table S1,$\dagger$ we can find the computed lattice parameters for ZrN and $Zr_3N_4$ are in good agreement with those obtained from other theoretical and experimental investigations, which confirms the accuracy of our calculations. From the structural point of view, ZrN has the ideal cubic rocksalt structure, while $Zr_{n+1}N_n$ ($n=2,3,5,7$) and $Zr_mN_{m+1}$ ($m=4,7,15$) are versions of the rocksalt structure with ordered nitrogen or zirconium vacancies ($Zr_2N$ has rutile-type structure).

![](./images/811083262129602562_2.jpg)

Fig. 2 Crystal structures of the representative (a) $Zr_6N_5$ and (b) $Zr_4N_5$ compounds.

In the structures of Zr-rich phases, the metal atoms form hexagonal close-packed (hcp) sublattices with N atoms filled in the octahedral voids, thus each N atom is coordinated by six Zr atoms, forming $NZr_6$ octahedra. However, the concentration of filled octahedral voids in various $Zr_{n+1}N_n$ structures is different. Two thirds of them are filled in $Zr_3N_2$; while seven eighths in $Zr_8N_7$. Similar nitrogen vacancy-ordered structures were also reported earlier to be stable for transition metal carbides $M_{n+1}C_n$ ($M=$ Hf and $n=2,5;^{28}M=$ Zr and $n=1,2,3,6;^{29}M=$ Ti and $n=1,2,5$ (ref. 30)) and nitrides $M_{n+1}N_n$ ($M=$ Ti and $n=1$, $2,3,5$ (ref. 31)). For N-rich phases, one eighth of the metal atoms are replaced with vacancies in $Zr_7N_8$, while one fifth in $Zr_4N_5$.

The formation of such N-rich phases could be attributed to the enhanced stability of the +4 oxidation state of Zr and Hf compared to Ti due to the relativistic effects,³² leading to the coexistence of +3 in MN and +4 in $M_3N_4$, while in the Ti-N system, TiN has the highest nitrogen content under normal conditions. In the structures of $Zr_3N_4$, the hcp metal framework of the rocksalt structure is significantly distorted. For $o$-$Zr_3N_4$, there are three nonequivalent types of Zr atoms, one of them is octahedrally coordinated to six N atoms, one resides at the center of a trigonal prism, and the last one is located inside of a heavily distorted octahedron (Fig. S3$\dagger$). Thus, the second and third nonequivalent Zr atoms are sevenfold coordinated, while in $c$-$Zr_3N_4$, each Zr atom is coordinated to eight N atoms.

### 3.2 Electronic properties and chemical bonding
We calculated the electronic properties (density of states, DOS, see Fig. 3) of zirconium nitrides at ambient conditions in order to study their chemical bonding. Let us start first with $Zr_3N_4$ and then discuss the effect of zirconium or nitrogen vacancies on the electronic properties of rocksalt based-structures. In DOS of

![](./images/811083262129602562_3.jpg)

Fig. 3 The calculated electronic density of states of (a) $o$-$Zr_3N_4$, (b) ZrN and (c) $Zr_2N$. (d) Crystal orbital Hamilton population (-COHP) curves of $Zr_2N$.

o-Zr₃N₄ displayed in Fig. 3a, three main regions may be described with three kinds of molecular orbital overlaps: nonbonding, bonding and antibonding.³³ Firstly, a rather sharp peak at roughly −13 eV appears and it is mainly of N(2s) character although with some Zr(4d) character. This sharp peak reflects the localized character of the nonbonding N(2s)-based levels; secondly, from −6 eV to 4 eV, a very broad structure with two well-defined main peaks originates from mixing of Zr(4d) and N(2p) orbitals. The lower peak corresponds to the bonding states, and the antibonding counterparts appear just above the Fermi level. These bonding and antibonding peaks exhibit a clear mixing of metal 4d and nitrogen 2p states, although the latter has a stronger Zr(4d) character. In o-Zr₃N₄, the gap separates bonding and antibonding states, thus Zr₃N₄ is a semiconductor and possesses a remarkable stability. Its calculated band gap (0.68 eV) is consistent with previous theoretical results.⁶,¹³ These findings are understandable if one considers the following Zintl picture: Zr is in a formal oxidation state of +4 (Zr⁴⁺, d⁰), and N³⁻ follows the octet rule.

For the well-known stoichiometric rocksalt ZrₓNᵧ, we will first briefly discuss their electronic properties, then analyze the electronic perturbation due to the creation of nitrogen or zirconium vacancies – empty octahedral sites in the fcc network – leading to symmetry-broken Zrₙ₊₁Nₙ and ZrₘNₘ₊₁ structures. Similarly to o-Zr₃N₄, DOS of ZrₓNᵧ phases can be decomposed into three well-separated energy regions as shown in Fig. 3 and S5,† but here no gap separates the valence and conducting bands: (1) a deep lowest valence band, s_N; (2) hybridized Zr(4d)/N(2p) band, d_MPN; (3) a partially filled higher-energy Zr(4d) band, d_M. The s_N band is dominated by the 2s orbitals of the nitrogen atoms and is nonbonding. The next group of valence bands, d_MPN, results from strong hybridization of the 4d states of zirconium atoms with 2p states of nitrogen atoms. Also, one may see that for ZrₓNᵧ, the bottom of the d_M band, dominated by 4d orbitals of zirconium atoms, responsible for metallicity.

When nitrogen vacancies are created in substoichiometric Zrₙ₊₁Nₙ ($n = 1, 2, 3, 5$ and 7), notice that obviously the formal oxidation state of Zr decreases as the number of nitrogen vacancies increases, going from Zr³⁺ d¹ in ZrN to Zr¹.⁵⁺ d².⁵ in Zr₂N. Therefore, one may expect the occupation of the Zr 4d levels in substoichiometric Zrₙ₊₁Nₙ compounds. This is what happens: Zr–Zr bonding and nonbonding (slightly antibonding) Zr–N levels appear just below the Fermi level, mainly metal 4d in character (see Fig. 3d and S6†). In Zrₙ₊₁Nₙ, Zr atoms are no longer all in the MN₆ octahedral environment; some of them are in MN₅ square pyramidal configurations. Therefore, one may expect the stabilization of antibonding Zr–N levels when going from formally octahedral ZrN₆ to square pyramidal ZrN₅ environment due to the lack of a Zr(4d)–N(2p) antibonding component. The occupation of these Zr–N nonbonding levels may explain the mechanical properties of these substoichiometric Zrₙ₊₁Nₙ compounds.

Fig. 3c displays the total and projected DOS of Zr₂N, but also the projected d states of a hypothetical ZrN structure within the Zr₂N structure (all N vacancies are filled in the so-called perfect structure). One can see that nitrogen vacancies give rise to additional states just below the Fermi level compared to its corresponding perfect structure, which originates from the Zr–Zr bonds passing through a nitrogen vacancy site. Such "vacancy states" usually lead to a drastic increase in the density of states at the Fermi level (0.076 in ZrN; 0.090 in Zr₆N₅; 0.112 in Zr₂N, states per eV per electron). The increasing density of the d state at the Fermi level can be interpreted as an increase in the Zr(4d_σ)–Zr(4d_σ) bonding or metallic bonds between the zirconium atoms.

### 3.3 Mechanical properties
We further studied mechanical properties of the Zr–N compounds. The calculated elastic constants are shown in Table 1. All structures satisfy the Born–Huang stability criteria,⁴⁰ confirming their mechanical stability. From the calculated elastic constants, we can find ZrN holds the largest $C_{11}$, $C_{22}$ and $C_{33}$ values among the ZrₓNᵧ compounds, which indicate the very high compressibility along the axis directions. o-Zr₃N₄ has the smallest $C_{11}$ and $C_{44}$ values. The bulk modulus $B$, shear modulus $G$, Young's modulus $E$ and Poisson's ratio $\nu$ were further obtained using the Voigt–Reuss–Hill averaging,⁴¹ shown in Table 1. The calculated B values of zirconium nitrides are

<table>
<caption>Table 1 The calculated bulk modulus $B$, shear modulus $G$, Young's modulus $E$, Poisson's ratio $\nu$, $B/G$ ratio, anisotropy index $A^{\mathrm{U}}$, Šimůnek's hardness $H_{\mathrm{S}}$ and Chen's hardness $H_{\mathrm{C}}$ of ZrₓNᵧ compounds at 0 GPa ($B$, $G$, $E$ and $H$, GPa)</caption>
<thead>
<tr>
<th>Phase</th>
<th>$C_{1}$</th>
<th>$C_{12}$</th>
<th>$C_{13}$</th>
<th>$C_{15}$</th>
<th>$C_{22}$</th>
<th>$C_{23}$</th>
<th>$C_{25}$</th>
<th>$C_{33}$</th>
<th>$C_{35}$</th>
<th>$C_{44}$</th>
<th>$C_{46}$</th>
<th>$C_{55}$</th>
<th>$C_{66}$</th>
<th>$B$</th>
<th>$G$</th>
<th>$E$</th>
<th>$\nu$</th>
<th>$B/G$</th>
<th>$A^{\mathrm{U}}$</th>
<th>$H_{\mathrm{S}}$</th>
<th>$H_{\mathrm{C}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zr₂N</td>
<td>305</td>
<td>142</td>
<td>108</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>362</td>
<td></td>
<td>119</td>
<td></td>
<td>114</td>
<td>187</td>
<td>109</td>
<td>274</td>
<td>0.256</td>
<td>1.721</td>
<td>0.116</td>
<td>14.8</td>
<td>13.5</td>
</tr>
<tr>
<td>Zr₃N₂</td>
<td>293</td>
<td>132</td>
<td>130</td>
<td></td>
<td>325</td>
<td>93</td>
<td></td>
<td>384</td>
<td></td>
<td>112</td>
<td></td>
<td>96</td>
<td>84</td>
<td>190</td>
<td>100</td>
<td>255</td>
<td>0.276</td>
<td>1.896</td>
<td>0.170</td>
<td>15.5</td>
<td>11.0</td>
</tr>
<tr>
<td>Zr₄N₃</td>
<td>336</td>
<td>147</td>
<td>140</td>
<td>8</td>
<td>349</td>
<td>127</td>
<td>2</td>
<td>371</td>
<td>13</td>
<td>127</td>
<td>−10</td>
<td>95</td>
<td>109</td>
<td>209</td>
<td>108</td>
<td>277</td>
<td>0.280</td>
<td>1.931</td>
<td>0.091</td>
<td>15.2</td>
<td>11.3</td>
</tr>
<tr>
<td>Zr₆N₅</td>
<td>376</td>
<td>135</td>
<td>159</td>
<td>−25</td>
<td>384</td>
<td>153</td>
<td>29</td>
<td>364</td>
<td>2</td>
<td>118</td>
<td>25</td>
<td>134</td>
<td>145</td>
<td>224</td>
<td>122</td>
<td>309</td>
<td>0.270</td>
<td>1.845</td>
<td>0.233</td>
<td>15.3</td>
<td>13.2</td>
</tr>
<tr>
<td>Zr₈N₇</td>
<td>394</td>
<td>137</td>
<td>171</td>
<td>−28</td>
<td>396</td>
<td>162</td>
<td>31</td>
<td>385</td>
<td>2</td>
<td>131</td>
<td>35</td>
<td>154</td>
<td>147</td>
<td>235</td>
<td>129</td>
<td>328</td>
<td>0.267</td>
<td>1.815</td>
<td>0.301</td>
<td>13.3</td>
<td>14.1</td>
</tr>
<tr>
<td>ZrNᵃ</td>
<td>556</td>
<td>123</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>113</td>
<td></td>
<td></td>
<td></td>
<td>267</td>
<td>147</td>
<td>372</td>
<td>0.268</td>
<td>1.818</td>
<td>0.534</td>
<td>15.6</td>
<td>15.4</td>
</tr>
<tr>
<td>Zr₁₅N₁₆</td>
<td>437</td>
<td>153</td>
<td>155</td>
<td>−16</td>
<td>467</td>
<td>117</td>
<td>1</td>
<td>468</td>
<td>20</td>
<td>154</td>
<td>−13</td>
<td>130</td>
<td>161</td>
<td>247</td>
<td>148</td>
<td>369</td>
<td>0.251</td>
<td>1.673</td>
<td>0.323</td>
<td>15.5</td>
<td>17.3</td>
</tr>
<tr>
<td>Zr₇N₈</td>
<td>422</td>
<td>132</td>
<td>146</td>
<td>30</td>
<td>421</td>
<td>157</td>
<td>−30</td>
<td>396</td>
<td>2</td>
<td>150</td>
<td>28</td>
<td>166</td>
<td>160</td>
<td>234</td>
<td>146</td>
<td>362</td>
<td>0.242</td>
<td>1.605</td>
<td>0.199</td>
<td>15.5</td>
<td>18.2</td>
</tr>
<tr>
<td>Zr₄N₅</td>
<td>338</td>
<td>120</td>
<td>159</td>
<td>−11</td>
<td>425</td>
<td>116</td>
<td>−9</td>
<td>378</td>
<td>21</td>
<td>139</td>
<td>−12</td>
<td>106</td>
<td>118</td>
<td>215</td>
<td>120</td>
<td>303</td>
<td>0.264</td>
<td>1.789</td>
<td>0.211</td>
<td>15.0</td>
<td>13.7</td>
</tr>
<tr>
<td>o-Zr₃N₄ᵇ</td>
<td>209</td>
<td>159</td>
<td>164</td>
<td></td>
<td>469</td>
<td>167</td>
<td></td>
<td>422</td>
<td></td>
<td>95</td>
<td></td>
<td>63</td>
<td>130</td>
<td>214</td>
<td>91</td>
<td>239</td>
<td>0.314</td>
<td>2.359</td>
<td>1.043</td>
<td>12.4</td>
<td>7.3</td>
</tr>
<tr>
<td>c-Zr₃N₄ᶜ</td>
<td>423</td>
<td>146</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>133</td>
<td></td>
<td></td>
<td></td>
<td>238</td>
<td>135</td>
<td>341</td>
<td>0.261</td>
<td>1.761</td>
<td>0.002</td>
<td>11.0</td>
<td>15.2</td>
</tr>
<tr>
<td colspan="22">$^{a}B=249,^{34}G=157,^{35}H_{\nu}=16.^{36}$ $^{b}B=203,^{37}238,^{38}H_{\nu}=12.4.^{37}$ $^{c}B=224,^{37}H_{\nu}=11.7,^{39}11.4.^{37}$</td>
</tr>
</tbody>
</table>

![](./images/811083262129602562_4.jpg)

Fig. 4 Calculated bulk and shear moduli of the rocksalt structures as a function of vacancy concentration; also rutile-like $Zr_2N$ is shown (its structure can also be represented as a close-packed metal sublattice with 1/2 octahedral voids occupied by nitrogen atoms).

comparable with many other transition metal carbides, nitrides and borides, such as $Fe_3C$ (224 GPa (ref. 42)), TiN (294 GPa (ref. 31)) and $TiB_2$ (213 GPa (ref. 43)), but much lower than diamond (437 GPa (ref. 44)). Among these $Zr_xN_y$ compounds, ZrN has the largest bulk and shear moduli, although $Zr_7N_8$ has a practically identical shear modulus (see Table 1).

The effect of vacancy concentration on bulk and shear moduli of the rocksalt $Zr_xN_y$ structures is shown in Fig. 4. It can be seen that bulk and shear moduli monotonically decrease with increasing vacancy concentration. When N vacancies increase in a rocksalt structures, the number of Zr-N bonds obviously decreases. Moreover, the computed Zr-N separations are increasing when N vacancies increase, *i.e.* from 2.24 to 2.27 Å in $Zr_8N_7$ and $Zr_2N$, reflecting the weakening of the Zr-N bonding. Therefore, one may understand our findings, *i.e.* the loss of $B$ and $G$ is mainly attributed to the disappearance of some strong covalent Zr-N bonds.

For brittle materials, $B/G$ ratio is smaller than 1.75 (ref. 45) (for example, for diamond $B/G = 0.8$). From Table 1, we can find that $B/G$ values decreases in the following sequence: o-$Zr_3N_4$ > $Zr_4N_3$ > $Zr_3N_2$ > $Zr_6N_5$ > ZrN > $Zr_8N_7$ > $Zr_4N_5$ > c-$Zr_3N_4$ > $Zr_2N$ > $Zr_{15}N_{16}$ > $Zr_7N_8$. $B/G$ values of $Zr_2N$ (1.721), $Zr_{15}N_{16}$ (1.673) and $Zr_7N_8$ (1.605) are smaller than 1.75, which indicate that these are brittle or borderline materials. For the other compounds, $B/G$ values are larger than 1.75, which suggest that they are ductile materials. For ZrN, $B/G$ value is slightly larger than 1.75, making a good compromise between hardness and ductility, which is mainly due to a peculiar interplay between metallicity and covalency. Besides, we can find that $B/G$ values of Zr-rich phases are larger than N-rich ones except $Zr_2N$ and o-$Zr_3N_4$. Obviously, the higher metal content, the more ductile the material. Surprisingly, semiconducting o-$Zr_3N_4$ has the largest $B/G$ value (2.359) due to the low $C_{11}$ and $C_{44}$, and o-$Zr_3N_4$ also possesses remarkable elastic anisotropy. Here, we used the Ranganathan and Ostoja-Starzewski method⁴⁶ to estimate anisotropy:

$$
A^{\mathrm{U}}=5 \frac{G^{\mathrm{V}}}{G^{\mathrm{R}}}+\frac{B^{\mathrm{V}}}{B^{\mathrm{R}}}-6 \tag{2}
$$

where $G^{\mathrm{V}}$, $B^{\mathrm{V}}$, $G^{\mathrm{R}}$ and $B^{\mathrm{R}}$ are the shear and bulk moduli estimated using the Voigt and Reuss methods, respectively.

The calculated anisotropy parameters $A^{\mathrm{U}}$ of $Zr_xN_y$ phases are listed in Table 1. Elastic anisotropy decreases in the following sequence: o-$Zr_3N_4$ > ZrN > $Zr_{15}N_{16}$ > $Zr_8N_7$ > $Zr_6N_5$ > $Zr_4N_5$ > $Zr_7N_8$ > $Zr_3N_2$ > $Zr_2N$ > $Zr_4N_3$ > c-$Zr_3N_4$.

![](./images/811083262129602562_5.jpg)

Fig. 5 Directional dependence of Young's moduli (in GPa) of the $Zr_xN_y$ compounds.

Fig. 5 shows the directional dependence of Young's moduli for the selected $Zr_xN_y$ compounds (see eqn (8) in ESI†). For an isotropic system, one would see a spherical shape. The degree of elastic anisotropy can be directly reflected from the degree of deviation in shape from a sphere. From Fig. 5, we can find that Young's modulus is more anisotropic in o-$Zr_3N_4$, while $Zr_4N_3$ and $Zr_2N$ show more isotropic features. The anisotropy of o-$Zr_3N_4$ is due to low $C_{11}$ and high $C_{22}$, $C_{33}$ values, resulting in a flat shape of Young's modulus.

The Vickers hardness of zirconium nitrides was estimated by using Chen's model,⁴⁷ as follows:

$$
H_{C}=2(\kappa^{2} G)^{0.585}-3 \tag{3}
$$

where $\kappa$ is the Pugh ratio:⁴⁵ $\kappa = G/B$. The computed hardness values are given in Table 1. The estimated hardness of ZrN is 15.4 GPa, which is consistent with the experimental value of 16 GPa of Lévy *et al.*³⁶ Among these $Zr_xN_y$ compounds, $Zr_7N_8$ has the highest hardness of 18.2 GPa. Given that Chen's model is based solely on the computed elastic constants, here we also used the Šimůnek method to estimate their hardness, which is mainly based on bond density and bond strength.⁴⁸ The corresponding expression is given as follows:

$$
H_{\mathrm{S}}=\frac{C}{\Omega} n\left[\prod_{i, j=1}^{n} b_{i j} s_{i j}\right]^{1 / n} \mathrm{e}^{-\sigma f_{\mathrm{e}}} \tag{4}
$$

where $s_{ij}$ is the bond strength between atom $i$ and $j$, $b_{ij}$ is the bond number, $\Omega$ is the volume of the cell. The semi-empirical constants $C$ and $\sigma$ equal to 1450 and 2.8, respectively. The calculated hardness values are also given in Table 1. For the substoichiometric phases, the estimated hardness values are around 15 GPa. For $Zr_3N_4$, we found hardness values of 12.4 and 11.0 GPa for o-$Zr_3N_4$ and c-$Zr_3N_4$, respectively, which is consistent with previous theoretical calculations.³⁷,³⁹ The reported Vickers hardness of c-$Zr_3N_4$ film is 36 GPa,¹⁴,⁴⁹ making it nearly a superhard film material. It is possible that hardness could be much higher in a thin film compared to a bulk crystal.³⁷ Certainly, more extensive hardness experiments for the $Zr_xN_y$ structures should be performed.

## 4 Conclusions

By using the variable-composition *ab initio* evolutionary algorithm USPEX, we explored stable and metastable compounds in the Zr–N system at ambient pressure. Our calculations revealed that ZrN, Zr₂N, Zr₄N₃, Zr₆N₅, Zr₈N₇, Zr₁₅N₁₆, Zr₇N₈ and Zr₄N₅ are thermodynamically stable compounds at low temperatures, while Zr₃N₂ is marginally metastable and could be stable at high temperatures. Particularly, we found the two controversial compounds discovered by Juza *et al.* could be Zr₁₅N₁₆ and Zr₄N₅. The newly discovered compounds have defective rocksalt structures with ordered nitrogen or zirconium vacancies. The calculated elastic constants of zirconium nitrides are in good agreement with available experimental values. Our results show that bulk and shear moduli monotonically increase with decreasing vacancy content. This can be attributed to the occurrence of more Zr–N covalent bonds and weakening of the ductile Zr–Zr metallic bonds. Besides, we found hardness of bulk Zr₃N₄ is below ~15 GPa.

## Acknowledgements

We thank the National Natural Science Foundation of China (No. 51372203 and 51332004), the Foreign Talents Introduction and Academic Exchange Program (No. B08040), the GDRI RFCCT CNRS (DNM-evol program) and the Hubert Curien Partnerships PHC XU GUANGQI 2015 (No. 34455PE) part of the French Ministry of Foreign Affairs, the Région Poitou-Charentes (France) for a PhD fellowship, and the Government of the Russian Federation (No. 14.A12.31.0003) for financial support. We also acknowledge the High Performance Computing Center of NWPU (China), and TGCC/Curie GENCI (France) under project no. 2016087539 for allocation of computing time on their machines. We would like to thank an anonymous referee to point out Zr₁₅N₁₆ as a potential candidate.

## References

1 H. O. Pierson, *Handbook of refractory carbides and nitrides: properties, characteristics, processing and applications*, Noyes Publication, New York, 1996, pp. 163–180.

2 H. Holleck, *J. Vac. Sci. Technol.*, A, 1986, **4**, 2661–2669.

3 K. Inumaru, T. Ohara, K. Tanaka and S. Yamanaka, *Appl. Surf. Sci.*, 2004, **235**, 460–464.

4 D. J. Kim, Y. R. Cho, M. J. Lee, J. M. Hong, Y. K. Kim and K. H. Lee, *Surf. Coat. Technol.*, 1999, **116**, 906–910.

5 A. I. Gusev and A. A. Rempel, *Phys. Status Solidi A*, 1997, **163**, 273–304.

6 D. I. Bazhanov, A. A. Knizhnik, A. A. Safonov, A. A. Bagaturyants, M. W. Stoker and A. A. Korkin, *J. Appl. Phys.*, 2005, **97**, 044108.

7 R. Niewa and F. J. DiSalvo, *Chem. Mater.*, 1998, **10**, 2733–2752.

8 A. Kafizas, C. J. Carmalt and I. P. Parkin, *Coord. Chem. Rev.*, 2013, **257**, 207–2119.

9 A. Salamat, A. L. Hector, P. Kroll and P. F. McMillan, *Coord. Chem. Rev.*, 2013, **257**, 2063–2072.

10 S. V. Didziulis and K. D. Butcher, *Coord. Chem. Rev.*, 2013, **257**, 93–109.

11 L. Gribaudo, D. Arias and J. Abriata, *J. Phase Equilib.*, 1994, **15**, 441–449.

12 A. Zerr, G. Miehe and R. Riedel, *Nat. Mater.*, 2003, **2**, 185–189.

13 P. Kroll, *Phys. Rev. Lett.*, 2003, **90**, 125501.

14 M. Chhowalla and H. E. Unalan, *Nat. Mater.*, 2005, **4**, 317–322.

15 W. H. Baur and M. Lerch, *Z. Anorg. Allg. Chem.*, 1996, **622**, 1729–1730.

16 R. Juza, A. Gabel, H. Rabenau and W. Klose, *Z. Anorg. Allg. Chem.*, 1964, **329**, 136–145.

17 A. R. Oganov and C. W. Glass, *J. Chem. Phys.*, 2006, **124**, 244704.

18 A. R. Oganov, A. O. Lyakhov, M. Valle, C. Gatti and Y. Ma, *Rev. Mineral. Geochem.*, 2010, **71**, 271–298.

19 A. R. Oganov, A. O. Lyakhov and M. Valle, *Acc. Chem. Res.*, 2011, **44**, 227–237.

20 A. O. Lyakhov, A. R. Oganov, H. T. Stokes and Q. Zhu, *Comput. Phys. Commun.*, 2012, **184**, 1172–1182.

21 G. Kresse and J. Furthmller, *Phys. Rev. B: Condens. Matter*, 1996, **54**, 11169–11186.

22 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865.

23 P. E. Blöchl, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1994, **50**, 17953.

24 M. Methfessel and A. T. Paxton, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1989, **40**, 3616–3621.

25 A. Togo, F. Oba and I. Tanaka, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2008, **78**, 134106.

26 H. Tang, A. Van der Ven and B. L. Trout, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2004, **70**, 045420.

27 M. Lerch, E. Füglein and J. Wrba, *Z. Anorg. Allg. Chem.*, 1996, **622**, 367–372.

28 Q. F. Zeng, J. H. Peng, A. R. Oganov, Q. Zhu, C. W. Xie, X. D. Zhang, D. Dong, L. T. Zhang and L. F. Cheng, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2013, **88**, 4269–4275.

29 X. X. Yu, C. R. Weinberger and G. B. Thompson, *Comput. Mater. Sci.*, 2016, **112**, 318–326.

30 C. Jiang and W. S. Jiang, *Phys. Status Solidi B*, 2014, **251**, 533–536.

31 S. Y. Yu, Q. F. Zeng, A. R. Oganov, G. Frapper and L. T. Zhang, *Phys. Chem. Chem. Phys.*, 2014, **17**, 11763–11769.

32 J. E. Huheey, *Inorganic chemistry: principles of structure and reactivity*, Harpar & Row, 1993, vol. 156, pp. 907–914.

33 R. Hoffmann, *Solids and surfaces: a chemist's view of bonding in extended structures*, Wiley-VCH, New York, 1988, pp. 18–21.

34 Z. Q. Chen, J. Wang and C. M. Li, *J. Alloys Compd.*, 2013, **575**, 137–144.

35 C. Sarioglu, *Surf. Coat. Technol.*, 2006, **201**, 707–717.

36 F. Lévy, P. Hones, P. Schmid, R. Sanjinés, M. Diserens and C. Wiemer, *Surf. Coat. Technol.*, 1999, **120**, 284–290.

37 F. M. Gao, *Chin. Phys. Lett.*, 2011, **28**, 076102.

38 W. Y. Ching, Y. N. Xu and L. Z. Ouyang, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2002, **66**, 126–130.

39 F. M. Gao, R. Xu and K. Liu, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2005, **71**, 2103.

40 F. Mouhat and F. X. Coudert, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2014, **90**, 224104.

41 W. Zhou, L. J. Liu, B. L. Li, P. Wu and Q. G. Song, *Comput. Mater. Sci.*, 2009, **46**, 921–931.

42 C. Jiang, S. G. Srinivasan, A. Caro and S. A. Maloy, *J. Appl. Phys.*, 2007, **103**, 3654–3660.

43 V. Milman and M. Warren, *J. Phys.: Condens. Matter*, 2001, **13**, 5585.

44 Y. C. Liang, W. L. Guo and Z. Fang, *Acta Phys. Sin.*, 2007, **56**, 4847–4855.

45 S. F. Pugh, *Philos. Mag.*, 1954, **45**, 823–843.

46 S. I. Ranganathan and M. Ostoja-Starzewski, *Phys. Rev. Lett.*, 2008, **101**, 055504.

47 X. Q. Chen, H. Y. Niu, D. Z. Li and Y. Y. Li, *Intermetallics*, 2011, **19**, 1275–1281.

48 A. Šimúnek, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2007, **75**, 172108.

49 A. Zerr, G. Miehe and R. Riedel, *Nat. Mater.*, 2003, **2**, 185–189.