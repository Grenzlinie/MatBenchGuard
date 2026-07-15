GEOPHYSICAL RESEARCH LETTERS, VOL. 31, L11603, doi:10.1029/2004GL019839, 2004

# Ab-initio high-pressure alloying of iron and potassium: Implications for the Earth's core

Kanani K. M. Lee¹
Department of Earth and Planetary Science, University of California, Berkeley, California, USA

Gerd Steinle-Neumann
Bayerisches Geoinstitut, Universität Bayreuth, Bayreuth, Germany

Raymond Jeanloz
Department of Earth and Planetary Science, University of California, Berkeley, California, USA

Received 27 February 2004; revised 13 April 2004; accepted 29 April 2004; published 3 June 2004.

[1] *Ab-initio* quantum mechanical calculations show that several percent potassium (K) can be alloyed into iron (Fe) at high pressure, suggesting that K may have been incorporated into the Earth's iron-rich core. We find that substitutional incorporation of K into the high-pressure polymorph of Fe, hexagonal close packed (hcp) $\varepsilon$-Fe, is energetically favored over the separate elements. The incorporation of potassium causes iron to expand with increasing K concentration, in agreement with high-pressure experiments. This alloying process is of potential importance to understanding the thermal state and history of Earth's deep interior, as radioactive decay of $^{40}$K (half-life $\sim$1.25 billion years) in the core could be an important source of energy for the geodynamo and mantle dynamics. **INDEX TERMS:** 3919 Mineral Physics: Equations of state; 3924 Mineral Physics: High-pressure behavior; 8124 Tectonophysics: Earth's interior—composition and state (1212); 8130 Tectonophysics: Heat generation and transport. **Citation:** Lee, K. K. M., G. Steinle-Neumann, and R. Jeanloz (2004), *Ab-initio* high-pressure alloying of iron and potassium: Implications for the Earth's core, *Geophys. Res. Lett.*, 31, L11603, doi:10.1029/2004GL019839.

## 1. Introduction

[2] The possible presence of potassium in the Earth's core is an old debate stemming from discrepant values of K/U (potassium/uranium) ratios as measured in chondrites and terrestrial rocks [Wasserburg et al., 1964]. Two popular theories on the fate of the "missing" K include loss to space during accretion [McDonough and Sun, 1995] or seques- tering into the accreting core [e.g., Goettel, 1976].

[3] Recent core energetics models [Buffett, 2002; Labrosse et al., 2001; Nimmo et al., 2004] and experimental results [Gessmann and Wood, 2002; Lee and Jeanloz, 2003; Murthy et al., 2003] have brought about renewed interest in the possibility of radioactivity being an important source of energy in the Earth's core. These models, which estimate the power necessary for the Earth's dynamo, are compatible with a K concentration of order 100 ppm in the Earth's core. Partitioning experiments of potassium between an iron-rich melt and surrounding silicate have documented the presence of 100–1000 ppm K in the iron-rich melt [Gessmann and Wood, 2002; Ito et al., 1993; Murthy et al., 2003].

[4] Most recently, *Lee and Jeanloz* [2003] compressed pure metals K and Fe in a diamond-anvil cell, melted the sample, and temperature quenched this melt. For samples compressed above $\sim$26 GPa, a systematic expansion was measured in the $\varepsilon$-Fe unit-cell volume due to the incorporation of K into Fe. These experimental results in particular raise two questions: What is the mechanism of K incorporation, and how much K can hcp $\varepsilon$-Fe accommo- date? Experiments can provide estimates of how much K gets incorporated through electron probe microanalysis (EPMA) of recovered samples [Gessmann and Wood, 2002; Ito et al., 1993; Murthy et al., 2003] or based on volume expansion [Lee and Jeanloz, 2003]. However, such experiments can not definitively pin down the incorporation mechanism, whereas calculations can. To further explore the possibility of potassium being present in the Earth's core, we apply first-principles quantum mechanical calculations to model the incorporation of K into the unit cell of $\varepsilon$-Fe at high pressures. Our objective is to understand the incorporation mechanism of K into $\varepsilon$-Fe, the effect of pressure on the chemical bonding in K-Fe alloys, and the influence of K alloying on the lattice parameter expansion in $\varepsilon$-Fe as observed experimentally [Lee and Jeanloz, 2003]. Potassium, an alkali metal at ambient conditions, has been shown to undergo an electronic transition under pressure, with the outer (valence) electrons changing from 4s to 3d character; it thus becomes a transition metal-like element that is more likely to form a solid solution with transition metal Fe [Bukowinski, 1976; Parker et al., 1996].

[5] First-principles density functional theory (DFT) pro- vides a complement to high-pressure experiments, and offers a powerful means of predicting the stability and properties of solids independent of experimental data and without invok- ing free parameters (see Methods). Recently, computational mineral physics has helped to advance the understanding of physical properties of material at high pressure that may be difficult to measure in the laboratory. Iron has been one material at the focus of computational mineral physics due to the complex interplay of electronic, magnetic, and structural properties [Bagno et al., 1989; Steinle-Neumann et al., 1999; Vocadlo et al., 1997]. The high-pressure $\varepsilon$-Fe polymorph is of central importance in geophysics, as the solid inner core is

---
¹Now at Division of Geological and Planetary Sciences, California Institute of Technology, Pasadena, California, USA.

Copyright 2004 by the American Geophysical Union.
0094-8276/04/2004GL019839

L11603
1 of 4

<table><caption>Table 1. Equation of State Parameters for Fe and $\text{Fe}_{x}\text{K}_{(1-x)}$ Alloys$^{\text{a}}$</caption>
<thead>
<tr>
<th>
</th>
<th>
Supercell Size
</th>
<th>
$V_{0}$ ($\text{\AA}^{3}$)
</th>
<th>
$\% \partial V_{0}$
</th>
<th>
$\text{K}_{0}$ (GPa)
</th>
<th>
$\text{K}_{0}^{\prime}$
</th>
<th>
K Concentration (in wt% ppm)
</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7">
$\varepsilon$-$Fe$
</td>
</tr>
<tr>
<td>
Fe, this study
</td>
<td>
</td>
<td>
10.32
</td>
<td>
-
</td>
<td>
285
</td>
<td>
4.4
</td>
<td>
-
</td>
</tr>
<tr>
<td>
Fe, theory [Steinle-Neumann et al., 1999]
</td>
<td>
</td>
<td>
9.80
</td>
<td>
-
</td>
<td>
292
</td>
<td>
4.4
</td>
<td>
-
</td>
</tr>
<tr>
<td>
Fe, theory [Vocadlo et al., 1997]
</td>
<td>
</td>
<td>
10.4
</td>
<td>
-
</td>
<td>
290
</td>
<td>
4.0$^{\text{b}}$
</td>
<td>
-
</td>
</tr>
<tr>
<td>
Fe, experiment [Jephcoat et al., 1986]
</td>
<td>
</td>
<td>
11.17
</td>
<td>
-
</td>
<td>
193 (9)
</td>
<td>
4.29 (0.36)
</td>
<td>
-
</td>
</tr>
<tr>
<td>
Fe, experiment [Mao et al., 1990]
</td>
<td>
</td>
<td>
11.17
</td>
<td>
-
</td>
<td>
165 (4)
</td>
<td>
5.33 (0.09)
</td>
<td>
-
</td>
</tr>
<tr>
<td colspan="7">
$\text{Fe}_{x}\text{K}_{(1-x)}$Alloys
</td>
</tr>
<tr>
<td>
$\text{Fe}_{0.97}\text{K}_{0.03}$, this study
</td>
<td>
32
</td>
<td>
10.67
</td>
<td>
3.4
</td>
<td>
246
</td>
<td>
4.5
</td>
<td>
22100
</td>
</tr>
<tr>
<td>
$\text{Fe}_{0.98}\text{K}_{0.02}$, this study
</td>
<td>
48
</td>
<td>
10.54
</td>
<td>
2.1
</td>
<td>
255
</td>
<td>
4.5
</td>
<td>
14700
</td>
</tr>
<tr>
<td>
$\text{Fe}_{0.99}\text{K}_{0.01}$, this study
</td>
<td>
96
</td>
<td>
10.41
</td>
<td>
0.9
</td>
<td>
267
</td>
<td>
4.5
</td>
<td>
7300
</td>
</tr>
<tr>
<td>
$\text{Fe}_{x}\text{K}_{(1-x)}$, experiment [Lee and Jeanloz, 2003]
</td>
<td>
</td>
<td>
11.41$^{\text{c}}$ (0.23)
</td>
<td>
2.1$^{\text{c}}$
</td>
<td>
196 (11)
</td>
<td>
4.0$^{\text{b}}$
</td>
<td>
$\sim$7000
</td>
</tr>
</tbody>
</table>

$^{\text{a}}$Uncertainties are given in parentheses.
$^{\text{b}}$$\text{K}_{0}^{\prime}$ values are fixed to 4.
$^{\text{c}}$Values assumed given the average volume deviation measured at high pressure.

thought to be composed primarily of this phase [Hemley and Mao, 2001]. Physical properties of $\varepsilon$-iron have been investigated by computational methods both at static (i.e., athermal conditions) and at high temperatures for comparison with laboratory experiments at room and high temperature, and to gain deeper insight into properties of the Earth’s core. Here we are primarily concerned with the energetics and equation of state of Fe and Fe-K alloys, and will compare room-temperature experiments with computational results under static conditions.

## 2. Methods
### 2.1. Computational Methods

[6] We use the Vienna ab-initio simulation package (VASP) [Kresse and Furthmuller, 1996; Kresse and Hafner, 1993], a DFT-based method, to evaluate the ground-state energetics of hcp Fe-K alloy supercells. Within VASP we perform calculations with the projector augmented wave (PAW) method [Kresse and Joubert, 1999], using the generalized gradient approximation (GGA) [Perdew et al., 1992] for the exchange and correlation potential. DFT-GGA based computations have been successful in describing ground-state properties of iron [Bagno et al., 1989; Steinle-Neumann et al., 1999; Vocadlo et al., 1997] and other transition metals [Korling and Haglund, 1992; Steinle-Neumann et al., 1999] both at ambient and high pressure. As high compressions are achieved in our study, resulting in the hybridization of low-lying electronic states such as the 3p bands in iron, we chose potentials that treat the 3p, 3d and 4s states of iron and the 3s, 3p and 4s states for potassium as valence electrons.

### 2.2. Incorporation Mechanisms and Supercell Setup

[7] There are two incorporation mechanisms of elements into a metallic hcp structure: i) substitution and ii) two possibilities of interstitial occupation, tetrahedrally and octahedrally [Smallman et al., 1988]. We use supercells to study substitution and interstitial behavior: one potassium atom is substituted on an hcp lattice site with 32, 48 or 96 Fe atoms (essentially $\text{Fe}_{0.97}\text{K}_{0.03}$, $\text{Fe}_{0.98}\text{K}_{0.02}$, and $\text{Fe}_{0.99}\text{K}_{0.01}$) over a wide compression range, and incorporated interstitially on the tetrahedral and octahedral sites for the 96 atom supercell at two volumes, corresponding to ambient pressure and a compression of $\text{V/V}_{0} = 0.7$.

[8] The supercells are based on an orthorhombic description of the hcp cell (space group Pmma with four atoms per cell, atoms at Wyckoff positions $2f$ and $2e$ with $z = 1/3$ and 1/6, respectively) with cell edges of relative lengths of $\sqrt{3}$, 1, and 1.6 (the c/a ratio in the hcp cell). The supercells consist of $2 \times 2 \times 2$ (32 atoms), $2 \times 3 \times 2$ (48 atoms), and $2 \times 4 \times 3$ (96 atoms) orthorhombic cells, and we use 6, 4, and 1 special k-points, respectively. Forces on the atoms occur in response to the incorporation of potassium. The atoms are relaxed self-consistently into their instantaneous ground-state position with a quasi-Newtonian algorithm. The non-hydrostatic stress exerted on the lattice is small, and we do not have to relax the cell parameters or shape. This justifies our choice of setting the free structural parameter, the axial ratio in the hcp cell, to $\text{c/a} = 1.6$ constant: close to the equilibrium value for pure iron, determined from experiment and computations [Jephcoat et al., 1986; Steinle-Neumann et al., 1999]. It is also an indication that the supercells chosen are sufficiently big, such that K - K interactions do not play an important role.

[9] For a comparison of the incorporation mechanisms we find that substitution is energetically favored at both volumes, with the energy difference increasing with compression. We hence focus on the substitutional incorporation mechanism in the supercells discussed above. The resulting energy-volume relations have been fit with a third-order finite-strain expression [Birch, 1952], from which equation of state parameters are obtained (Table 1). We use the volume deviations given by the equations of state of these hcp potassium-iron alloys from the pure hcp $\varepsilon$-iron equation of state to constrain the potassium content in the experiments (see Table 1, Figure 1).

### 2.3. Pure Element Calculations

[10] To compare the energetics of alloying and to test the PAW potentials, we also perform computations on pure iron in the hcp phase and on potassium. We tested hcp Fe, obtaining good agreement with previous results [Vocadlo et al., 1997] (Table 1). For K we perform computations on the ambient-pressure K I structure (bcc), and the two high-pressure phases K II (fcc) and K III (tet). We reproduce the experimentally determined equations of state for K I and K II [Liu, 1986] (also in agreement with theoretical results [Katsnelson et al., 2000]), but are unable to obtain good agreement for the high-pressure polymorph K III. The previously determined tetragonal structure of K III [Winzenick et al., 1994] is currently under debate [Schwarz et al., 1999]. This reconsideration is supported by our calculations, which

do not predict a reasonable equation of state for the tetragonal KIII structure. For this reason, we use the KII structure of potassium in our consideration of energetics in the K-Fe system rather than the KIII structure [Schwarz et al., 1999] (Figure 1). This is a reasonable approximation because the equations of state of the different potassium phases are similar despite their different structures [Winzenick et al., 1994].

## 3. Results

[11] Our results on hcp Fe-K alloy supercells support experimental indications that potassium can alloy with iron at high pressure by substitution of K into the Fe unit cell and result in a lattice expansion [Lee and Jeanloz, 2003]. We see a systematic, non-linear, increase of volume with increasing potassium concentration (Figure 1a), as well as softer equations of state (Table 1), compatible with experimental results [Lee and Jeanloz, 2003]. Our calculations predict that $\sim$2 (or more) atomic$\%$ ($\sim$15,000 ppm by weight) potassium at 0 K causes the experimentally observed volume expansion (Figure 1a). This value is near to that estimated by assuming simple Vegard-like behavior [Vegard, 1921] ($\sim$1 atomic$\%$ K in Fe for the volume expansion measured experimentally).

![](./images/812347177819963393_1.jpg)

Figure 1. (a) Percent volume difference, 100* (V(FeₓK₍₁₋ₓ₎) − V(Fe))/V(Fe), vs. pressure. Curves are labeled for the different K concentrations: Fe₀.₉₉K₀.₀₁ (Fe₉₅K₁, solid), Fe₀.₉₈K₀.₀₂ (Fe₄₈K₁, dotted), Fe₀.₉₇K₀.₀₃ (Fe₃₂K₁, dashed). Filled (empty) circles show experimental data for unalloyed (alloyed) FeₓK₍₁₋ₓ₎ [Lee and Jeanloz, 2003]. Bold vertical shaded area centered at 26 ($\pm$3) GPa indicates empirical alloying pressure [Lee and Jeanloz, 2003]. (b) Gibbs free energy difference (at static conditions) for the reaction: xFe + (1 − x)K $\iff$ FeₓK₍₁₋ₓ₎ as a function of pressure where pure K is in the K II structure (see Methods). The stability range for each side of the reaction is separated by the horizontal dashed line at $\Delta$G = 0 eV/atom: a positive (negative) $\Delta$G value indicates pure elements Fe and K are less (more) stable unalloyed rather than alloyed as FeₓK₍₁₋ₓ₎. Temperature and entropy effects will push each curve up, making the FeₓK₍₁₋ₓ₎ alloy more stable.

![](./images/812347177819963393_2.jpg)

Figure 2. Nearest-neighbor distance around K vs. lattice constant for Fe₃₁K₁ (Fe₀.₉₇K₀.₀₃) supercell shown with the dashed curve. The dotted line is the 1:1 relation. At the smallest lattice constant spacing (corresponding to the highest pressure investigated, $\sim$485 GPa), the nearest neighbor distance around the K is approximately the same as the lattice spacing.

[12] aWe also compare the Gibbs free energy difference at static conditions for the equilibrium reaction: xFe + $(1-x)$K $\iff$ FeₓK₍₁₋ₓ₎. We find that with increasing pressures the supercell alloy FeₓK₍₁₋ₓ₎ becomes more favorable (Figure 1b). If we assume that each side of the reaction has similar vibrational entropy, with the only difference being the entropy of mixing for the alloy, the alloy is even more favored (i.e., stability will be achieved at lower pressures) at high temperatures [Smallman et al., 1988]. For example, at 2000 K the entropy of mixing for the Fe₀.₉₉K₀.₀₁ alloy is expected to contribute $\sim$0.01 eV/atom to the free energy, thereby moving the stability pressure of the Fe₀.₉₉K₀.₀₁ alloy from 35 down to 21 GPa. This is in good agreement with the experimental measurements, that show alloying behavior at pressures and temperatures greater than 26 ($\pm$3) GPa and 2500 K [Lee and Jeanloz, 2003]. However, we remind the reader that the Gibbs free energy difference is small relative to uncertainties in our theoretical modeling (e.g., using K II rather than K III equation of state and energetics).

[13] Atoms in the supercell are relaxed self-consistently to accommodate the K atom. We find that K compresses rapidly, and that its compressive behavior is independent of the supercell size hence K concentration (with the range investigated). Thus, when we compare nearest-neighbor distances around K with the lattice spacing of the alloy, the K site is not much bigger than that of Fe at high compressions (Figure 2 and see auxiliary material¹). This is due to the fact

---
¹Auxiliary material is available at ftp://ftp.agu.org/apend/gl/2004GL019839.

that K is much more compressible than Fe, especially when the change in bonding character (electronic transition) is taken into account.

[14] Our results confirm earlier quantum mechanical calculations on the alkali $\rightarrow$ transition metal behavior of K at high pressure [Bukowinski, 1976]. A more recent molecular orbital calculation suggests otherwise [Sherman, 1990], but the $\text{KFe}_{14}$ cluster examined in that study corresponds to a greater potassium concentration than is the case for our study (7% versus up to 3%) or for what is cosmochemically expected.

## 4. Discussion and Conclusions

[15] Recent core energetics calculations suggest that some radioactivity may have been required in order to produce the Earth's early magnetic field [Buffett, 2002; Labrosse et al., 2001; Nimmo et al., 2004]. Pure metal (K, Fe) experiments and calculations provide an upper limit to the potassium concentration in the Earth's core; even so, the possibility of radioactivity in the core cannot be ignored. This amount of radioactivity is more than two orders of magnitude greater than is necessary to satisfy geodynamo energy requirements [Buffett, 2002]. The pressures and temperatures may not have been favorable to alloy potassium with iron until the Earth's accretion was nearly finished, yet core differentiation likely began before accretion was complete thereby leaving the earliest core potassium free. Therefore, although we find a high amount of K alloying with Fe at pressures above $\sim$35 GPa (at 0 K or $\sim$21 GPa at 2000 K) (Figure 1, Table 1), much of the core could have already formed before the conditions were favorable for Fe-K alloying. If the Earth's core contains the cosmochemi- cally-based estimates of 1200 ppm K [Gessmann and Wood, 2002], $\sim$20% of the Earth's power budget or 8 TW of power would be currently produced and $\sim$100 TW 4.5 billion years ago. Additionally, if uranium and thorium are also present in the core, radioactive heating may indeed provide a significant fraction of the power necessary for the geodynamo and mantle dynamics.

[16] Acknowledgments. K. K. M. L. would like to thank Bayerisches Geoinstitut for the opportunity to conduct these calculations. This work was supported in part by the National Science Foundation, the Bayerisches Geoinstitut visitors program and a Sigma Xi travel grant.

## References

Bagno, P., O. Jepsen, and O. Gunnarsson (1989), Ground-state properties of third-row elements with nonlocal density functionals, Phys. Rev. B, 40, 1997-2000.

Birch, F. (1952), Elasticity and constitution of the Earth's interior, J. Geo- phys. Res., 57, 227-286.

Buffett, B. A. (2002), Estimates of heat flow in the deep mantle based on the power requirements for the geodynamo, Geophys. Res. Lett., 29(12), 1566, doi:10.1029/2001GL014649.

Bukowinski, M. S. T. (1976), The effect of pressure on the physics and chemistry of potassium, Geophys. Res. Lett., 3, 491-503.

Gessmann, C. K., and B. J. Wood (2002), Potassium in the Earth's core?, Earth Planet. Sci. Lett., 200, 63-78.

Goettel, K. A. (1976), Models for the origin and composition of the Earth, and the hypothesis of potassium in the Earth's core, Geophys. Surv., 2, 369-397.

Hemley, R. J., and H.-K. Mao (2001), In situ studies of iron under pressure: New windows on the Earth's core, Int. Geol. Rev., 43(1), 1-30.

Ito, E., K. Morooka, and O. Ujike (1993), Dissolution of K in molten iron at high pressure and temperature, Geophys. Res. Lett., 20, 1651-1654.

Jephcoat, A. P., H.-K. Mao, and P. M. Bell (1986), Static compression of iron to 78 GPa with rare gas solids as pressure-transmitting media, J. Geophys. Res., 91, 4677-4684.

Katsnelson, M. I., G. V. Sinko, N. A. Smirnov, A. V. Trefilov, and K. Y. Khromov (2000), Structure, elastic moduli, and thermodynamics of so- dium and potassium at ultrahigh pressures, Phys. Rev. B, 61, 14,420-14,424.

Korling, M., and J. Haglund (1992), Cohesive and electronic properties of transition metals: The generalized gradient approximation, Phys. Rev. B, 45, 13,293-13,297.

Kresse, G., and J. Furthmuller (1996), Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B, 54, 11,169-11,186.

Kresse, G., and J. Hafner (1993), Ab initio molecular dynamics for liquid metals, Phys. Rev. B, 47, 558-561.

Kresse, G., and D. Joubert (1999), From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B, 59, 1758-1775.

Labrosse, S., J.-P. Poirier, and J.-L. Le Mouel (2001), The age of the inner core, Earth Planet. Sci. Lett., 190, 111-123.

Lee, K. K. M., and R. Jeanloz (2003), High-pressure alloying of potassium and iron: Radioactivity in the Earth's core?, Geophys. Res. Lett., 30(23), 2212, doi:10.1029/2003GL018515.

Liu, L. G. (1986), Compression and polymorphism of potassium to 400 kbar, Phys. Chem. Solids, 47(11), 1067-1072.

Mao, H.-K., Y. Wu, L. C. Chen et al. (1990), Static compression of iron to 300 GPa and $\text{Fe}_{0.8}\text{Ni}_{0.2}$ alloy to 260 GPa: Implications for the composi- tion of the core, J. Geophys. Res., 95, 21,737-21,742.

McDonough, W. F., and S.-S. Sun (1995), The composition of the Earth, Chem. Geol., 120, 223-253.

Murthy, V. R., W. van Westrenen, and Y. Fei (2003), Radioactive heat sources in planetary cores: Experimental evidence for potassium, Nature, 423, 163-165.

Nimmo, F., G. D. Price, J. Brodholt, and D. Gubbins (2004), The influence of potassium on core and geodynamo evolution, Geophys. J. Int., 156(2), 363-376.

Parker, L. J., T. A. Atou, and J. V. Badding (1996), Transition element-like chemistry for potassium under pressure, Science, 273, 95-97.

Perdew, J. P., J. A. Chevary, S. H. Vosko et al. (1992), Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approxima- tion for exchange and correlation, Phys. Rev. B, 46, 6671-6687.

Schwarz, U., A. Grzenick, K. Syassen et al. (1999), Rubidium IV: A high pressure phase with complex crystal structure, Phys. Rev. Lett., 83(20), 4085-4088.

Sherman, D. M. (1990), Chemical bonding and the incorporation of potas- sium into the Earth's core, Geophys. Res. Lett., 17, 693-696.

Smallman, R. E., W. Hume-Rothery, and C. W. Haworth (1988), The Structure of Metals and Alloys, Inst. of Metals, London.

Steinle-Neumann, G., L. Stixrude, and R. E. Cohen (1999), First-principles elastic constants for the hcp transition metals Fe, Co, and Re at high pressure, Phys. Rev. B, 60, 791-799.

Vegard, L. (1921), The constitution of mixed crystals and the space occu- pied by atoms, Z. Phys., 5(17), 17-26.

Vocadlo, L., G. A. de Wijs, G. Kresse et al. (1997), First Principles calcula- tions on crystalline and liquid iron at Earth's core conditions, Faraday Discuss., 106, 205-217.

Wasserburg, G. J., G. J. F. MacDonald, F. Hoyle, and W. A. Fowler (1964), Relative contributions of uranium, thorium, and potassium to heat production in the Earth, Science, 143, 465-467.

Winzenick, M., V. Vijayakumar, and W. B. Holzapfel (1994), High-pressure x-ray diffraction on potassium and rubidium up to 50 GPa, Phys. Rev. B, 50, 12,381-12,385.

R. Jeanloz, Department of Earth and Planetary Science, University of California, Berkeley, CA 94720, USA.

K. K. M. Lee, Division of Geological and Planetary Sciences, California Institute of Technology, 1200 East California Boulevard MC 170-25, Pasadena, CA 91125, USA. (kanani@gps.caltech.edu)

G. Steinle-Neumann, Bayerisches Geoinstitut, Universität Bayreuth, Bayreuth D-95440, Germany.

4 of 4