ORIGINAL PAPER

# Semiconducting character analysis of ${\text{RhY}}_{2}{\text{O}}_{4}$ oxide spinel via GGA, GGA + mBJ, and GGA + U approximations

F Ak¹, E G Özdemir²* and H A R Aliabad³

¹Darende Bekir Ilıcak Vocational School, Opticianry Program, Malatya Turgut Özal University, 44700 Malatya, Türkiye
²Department of Physics, Faculty of Science, Gazi University, Teknikokullar, 06560 Ankara, Türkiye
³Department of Physics, Hakim Sabzevari University, Sabzevar, Iran

Received: 23 September 2024 / Accepted: 01 May 2025 / Published online: 9 June 2025

**Abstract:** The semiconducting character of ${\text{RhY}}_{2}{\text{O}}_{4}$ oxide spinel was investigated using first-principles approximations. As a result of the optimization curve, ${\text{RhY}}_{2}{\text{O}}_{4}$ was obtained as a ferromagnet with an equilibrium lattice parameter of 9.46 Å with the help of the GGA approximation. When U = 1, 2, 3, and 4 eV were used, the lattice parameters were obtained as 9.49 Å, 9.52 Å, 9.55 Å, and 9.58 Å, respectively. The GGA approximation yielded the band gap values with the lowest semiconductor character, measuring 0.352 eV for the majority electron spin and 0.134 eV for the minority electron spin. Both direct and indirect band gaps were observed in the majority and minority electron spins. Elastic calculations confirmed the elastic stability of ${\text{RhY}}_{2}{\text{O}}_{4}$. Furthermore, the Debye temperature was determined to be 480.942 K at 0 GPa pressure. Poisson’s and B/G ratios were obtained at this pressure as 0.278 and 1.92, respectively. According to these results, ${\text{RhY}}_{2}{\text{O}}_{4}$ spinel is ductile. However, with increasing pressure, brittleness properties begin at about 10 GPa. ${\text{RhY}}_{2}{\text{O}}_{4}$ has a total magnetic moment of 6.000 $\mu_{\text{B}}$/f.u. ${\text{RhY}}_{2}{\text{O}}_{4}$ is a promising candidate for semiconductor applications, characterized by advantageous elastic, magnetic, and electronic properties.

**Keywords:** Coulomb interactions; Pressure-dependent; Semiconducting; GGA + U; Ferromagnetic

## Introduction

For decades, extensive research has been conducted on spinel oxides’ structural, magnetic, and electronic properties containing 3d transition-metal (TM) ions. It is well-established that these properties are significantly influenced by both the oxidation state and the arrangement of TM ions within the tetrahedral (A) and octahedral (B) sites of the spinel lattice [1]. Transition-metal-oxide (TMO) spinels have attracted significant interest because of the complex interaction among charge, spin, and orbital properties, leading to fascinating characteristics. Extensive research has focused on normal spinels, characterized by the general formula ${\text{AB}}_{2}{\text{O}}_{4}$, where ${\text{AO}}_{4}$ tetrahedral units are linked with ${\text{BO}}_{6}$ octahedral units. These materials frequently experience shifts from cubic to tetragonal symmetries, along with orbital and magnetic ordering phenomena at low temperatures [2].

Materials possessing spinel structures attract considerable attention due to their varied physical characteristics. This attention is primarily driven by the existence of two separate crystallographic sublattices, specifically tetrahedral (A) and octahedral (B), which are suitable for accommodating metal ions [3]. The crystal structure of ${\text{AB}}_{2}{\text{O}}_{4}$ crystals, known as the spinel structure, was first elucidated in 1915 by Bragg and Nishikawa. The arrangement of oxygen ions in this structure follows a face-centered cubic pattern, where metal ions occupy half of the octahedral positions and one-eighth of the tetrahedral spaces within the anion sublattice [4]. The characteristics of spinel materials can vary due to their crystal structure and chemical composition differences. Spinels exist in two distinct structural configurations: normal spinel and inverse spinel. A normal spinel’s crystal structure adheres to a typical arrangement represented as ${\text{A}}^{2 + }{\text{B}}_{2}^{3 + }{\text{O}}_{4}$, wherein bivalent ${\text{A}}^{2 + }$ and trivalent ${\text{B}}^{3 + }$ cations are arranged in tetrahedral and octahedral coordination, respectively. On the other hand, an inverse spinel exhibits a different configuration where A-site ions and half of the B-site ions

*Corresponding author, E-mail: evrengorkemozdemir@gazi.edu.tr

© 2025 The Author(s)

exchange positions. Inverse spinels are described by the chemical formula $\mathrm{B}^{3+}(\mathrm{A}^{2+}\mathrm{B}^{3+})\mathrm{O}_{4}$, where bivalent $\mathrm{A}^{2+}$ ions and half of the trivalent B ions occupy octahedral sites. On the contrary, the residual trivalent B ions are within tetrahedral sites [5, 6].

Under varying experimental conditions, oxides with a close-packed structure corresponding to the $\mathrm{AB}_{2}\mathrm{O}_{4}$ formula have demonstrated polymorphism, displaying different crystalline forms [7]. We utilize the unit cell structure for $\mathrm{AB}_{2}\mathrm{O}_{4}$ spinels, classified under the $Fd\overline{3}m$ space group [8]. The crystallographic arrangement of $\mathrm{RhY}_{2}\mathrm{O}_{4}$ is cubic and falls under the $Fd\overline{3}m$ space group, designated as No. 227 in the International Tables. In this structure, Rh, Y, and O atoms are at Wyckoff positions 8a, 16d, and 32e, respectively [9].

Derived from the characteristics of the component ions within their chemical composition, these oxide materials have the potential to manifest a wide array of physical properties. This encompasses electrical transport behaviors, extending from semiconducting traits to transitions between insulating and metallic states and demonstrating superconducting responses. Furthermore, they may display various magnetic features, including paramagnetism, superparamagnetism, antiferromagnetism, ferrimagnetism, and ferromagnetism, and even exhibit magnetoelectric behavior [10, 11]. Moreover, the category of spinel compounds constitutes an extensive and important group of versatile materials, playing a crucial role in various advanced domains such as energy and optoelectronics. These applications span a wide spectrum, including but not limited to batteries, fuel cells, photonics, catalysis, spintronics, and thermoelectric devices [12]. Extensive research has been conducted on spinel materials' structural properties and electronic structure, employing the conventional density functional theory (DFT) framework [13].

Semiconductors composed of transition metal oxides with a spinel structure are recognized for their low mobility characteristics. Their electrical conduction is typically attributed to charge transfer between octahedral cations through a hopping mechanism [14, 15]. Diluted magnetic semiconductors (DMSs) are currently under extensive investigation, primarily due to their potential applications in spintronics [16]. Semiconductor compounds featuring a spinel structure present a potential and cost-efficient option for robust detection systems due to their outstanding chemical and thermal stability during operation. When subjected to particular gaseous surroundings, these sensors rely on modified electric resistivity from chemical interactions between the metal-oxide surface and gas molecules. The selectivity and sensitivity of solid-state sensors are significantly influenced by the composition and morphology of the sample [17]. Additionally, phase field studies of $\mathrm{MgRh}_{2}\mathrm{O}_{4}$ spinel, which is one of the spinels containing Rh and O atoms, were experimentally investigated by Jacob et al. in 2012 [18]. The results obtained with the spinel phase electron microprobe in different phases and oxygen partial pressures showed that pure $\mathrm{MgRh}_{2}\mathrm{O}_{4}$ does not exist at high temperatures. While the structural and superconductivity studies of Te-doped $\mathrm{CuRh}_{2}\mathrm{Se}_{4}$ spinel containing Rh atom were investigated by Li et al. in 2024 [19], the structural properties of $\mathrm{MRh}_{2}\mathrm{O}_{4}$ (M = Mg, Mn, Cd) spinel alloys were investigated by Akbar et al. in 2024 [20]. According to the experimental results, it was obtained that $\mathrm{CuRh}_{2}\mathrm{Se}_{4-\mathrm{x}}\mathrm{Te}_{\mathrm{x}}\ (0\leq\mathrm{x}\leq0.28)$ doping crystallizes in the $Fd\overline{3}m$ (227) space group. The Debye temperatures of $\mathrm{CuRh}_{2}\mathrm{Se}_{4}$, $\mathrm{CuRh}_{2}\mathrm{Se}_{3.9}\mathrm{Te}_{0.1}$, and $\mathrm{CuRh}_{2}\mathrm{Se}_{2.72}\mathrm{Te}_{0.28}$ doped spinels were obtained as 202 K, 175 K, and 194 K, respectively. They confirmed that $\mathrm{CuRh}_{2}\mathrm{Se}_{4}$, $\mathrm{CuRh}_{2-}\mathrm{Se}_{3.9}\mathrm{Te}_{0.1}$, and $\mathrm{CuRh}_{2}\mathrm{Se}_{2.72}\mathrm{Te}_{0.28}$ spinels exhibit super-conducting characteristics by obtaining their critical temperatures as 3.4 K, 3.11 K, and 2.5 K, respectively. $\mathrm{MRh}_{2}\mathrm{O}_{4}$ (M = Mg, Mn, Cd) oxide spinels are stable materials according to their mechanical properties. $\mathrm{CdRh}_{2}\mathrm{O}_{4}$ spinel is ductile, while $\mathrm{MnRh}_{2}\mathrm{O}_{4}$ spinel is brittle. $\mathrm{MgRh}_{2}\mathrm{O}_{4}$ spinel has values at the limit of ductility/brittleness. $\mathrm{MnRh}_{2}\mathrm{O}_{4}$ spinel has the highest Debye temperature, with a Debye temperature of 634.4 K. While MnRh2O4 spinel was obtained as a ferrimagnetic semiconductor with a total magnetic moment of $10.00\ \mu_{\mathrm{B}}/\mathrm{f.u.}$, $\mathrm{MgRh}_{2}\mathrm{O}_{4}$ and $\mathrm{CdRh}_{2}\mathrm{O}_{4}$ spinels were obtained as non-magnetic semiconductors. As can be seen, spinel materials have been investigated experimentally and theoretically many times. The fact that semiconductor material groups similar to the structure of $\mathrm{RhY}_{2}\mathrm{O}_{4}$ oxide spinel, which is examined in this study, have been studied experimentally and theoretically in the literature has further increased our motivation. $\mathrm{RhY}_{2}\mathrm{O}_{4}$ spinel is a substance suitable for application in spintronic devices, given its electronic, magnetic, and elastic attributes. The band gaps in the up and down spins indicate that $\mathrm{RhY}_{2}\mathrm{O}_{4}$ oxide spinel is a semiconductor material. Its elastic properties show that $\mathrm{RhY}_{2}\mathrm{O}_{4}$ oxide spinel is mechanically stable. Its total magnetic moment has been obtained as $6.000\ \mu_{\mathrm{B}}$, and its magnetic character is remarkable.

## Calculation method

First, the initial state conditions of $\mathrm{RhY}_{2}\mathrm{O}_{4}$ oxide spinel were determined. The cubic $\mathrm{RhY}_{2}\mathrm{O}_{4}$ oxide spinel is formed in the $Fd\overline{3}m$ symmetry group. Rh, Y, and O atoms are placed in 0.125, 0.125, 0.125; 0.50, 0.50, 0.50; and 0.25, 0.25, 0.25 atomic positions, respectively. In Fig. 1,

![](./images/1138969294827159552_1.jpg)

Fig. 1 The created atomic structure of $RhY_2O_4$ oxide spinel

$RhY_2O_4$ semiconductor was formed using atomic positions and chosen symmetry.

The created oxide spinel's first-principles calculations were determined by the WIEN2k program developed by Blaha et al. [21-23]. The calculations of $RhY_2O_4$ oxide spinel were performed using GGA-PBE [24], GGA + mBJ, and GGA + U [25-27] approximations. Elastic cal- culations were made with the IRElast software developed by Jamal et al. [28]. All these calculations were made in the $10 \times 10 \times 10$ Brillouin region. While performing the initial calculations of the FM phases of $RhY_2O_4$ oxide spinel, spin orientations of atoms were polarized both up and down. As a result of this polarization, both total and partial net magnetic values emerged. Spin polarization orientations were not performed in the NM calculations. The energy cut-off values were chosen as $-6$ Ry. The radii of Muffin- Tin spheres surrounding Rh, Y, and O atoms were deter- mined as 2.15 a.u., 2.32 a.u., and 1.61 a.u., respectively. When using the GGA + mBJ approximation, the ground state values of $RhY_2O_4$ oxide spinel were determined by the GGA approximation, while mBJ coding was performed in the SCF calculations. Coulomb interactions were also performed by selecting $U=1,2,3$, and $4$ eV values in the GGA approximations.

## Results and discussion

$RhY_2O_4$ oxide spinel is characterized by $Fd\overline{3}m$ symmetry group, 227-space number, and atomic coordinates. Subse- quently, ferromagnetic (FM) and non-magnetic (NM) energy curves were generated using the GGA approxima- tion, and these curves are presented in Fig. 2a. The volume and energy values were fitted using Murnaghan's equation of states [29], yielding the initial state values detailed in Table 1. As depicted in Fig. 2, the FM phase exhibits greater magnetic stability than the NM phase. Figure 2b contrasts the optimization curves obtained through the GGA approximation with those obtained using the GGA + U approximations. According to Fig. 2b, the GGA approximation demonstrates higher energetic stability than the applied U-Coulomb interactions.

As illustrated in Fig. 2b, while the phase obtained is more stable with the utilization of the GGA approximation, the volume of $RhY_2O_4$ oxide spinel experiences an increase with the applied Coulomb interactions. In pro- portion to the volume value, increases are also observed in the equilibrium lattice parameters. Here, the lattice con- stant for the FM phase is calculated as $9.46$ Å. All initial state values obtained in Fig. 2 are given in Table 1.

Here, a (Å) is the equilibrium lattice parameter obtained for each initial state, B (GPa) is the bulk modulus sym- bolizing the resistance against volume change, $B'$ is the first derivative of the bulk modulus as a function of pres- sure, $V_0$-(atomic unit)$^3$ and $E_0$ (Ry) are the volume and energy values obtained at the equilibrium state. As seen in Table 1, an increase was observed in the lattice parameters as the applied U-Coulomb value increased. Conversely, decreases occurred in bulk modules. This is an expected result. As the volume increases, a decrease in the volume change is shown in response to the pressure. Furthermore, since the Coulomb repulsion will increase as the U-Cou- lomb potential value increases in the GGA + U approxi- mation, the expected result is that the energy values will decrease in stable equilibrium situations. For the Mn-Y-O spinel, the equilibrium lattice constant was determined to be $9.34$ Å in the ferromagnetic (FM) phase, with the cal- culated bulk modulus being 134.234 GPa [30]. When the4d transition metal Rh is used instead of the 3d transition metal Mn, the lattice constant increases, while the bulk modulus values are almost the same (134.119 GPa). Therefore, it can be interpreted that the resistances of oxide

Fig. 2 The plotted (a) FM and NM, (b) GGA and GGA + U optimization curves of $\text{RhY}_2\text{O}_4$ oxide spine

![](./images/1138969294827159552_2.jpg)

spinels obtained with Mn and Rh transition metals against volume change are almost equal.

In Fig. 3, band structures illustrating the electronic properties of the $\text{RhY}_2\text{O}_4$ oxide spinel under different approximations are presented. The horizontal dotted lines within the band structures indicate Fermi energy levels. To observe electronic interactions around Fermi energy levels, the energy values of the band structures are confined to the range of $-4$ eV to $+4$ eV. In each applied approximation depicted in Fig. 3, discernible band gaps are evident around the Fermi energy levels for both majority and minority electrons. It is shown that the bottom of the conduction bands is approximated as parabolic with a semiconductor nature.

The majority state electrons exhibit direct band gaps at their $\Gamma$-points. As for the minority state electrons, the valence band maximum (VBM) electrons are located at the $\Gamma$-point, whereas the electrons at the conduction band minimum (CBM) are at the L-point. Therefore, minority state electrons of $\text{RhY}_2\text{O}_4$ oxide spinel have indirect band gaps. The VBM values of the majority electrons in each approximation are exactly at the Fermi energy level. The VBM, CBM, and band gap values of the band structures shown in Fig. 3 are given in Table 2. As seen in Table 2, the VBM values of the majority (up) electrons are at 0 eV. The CBM values form the band gaps of the majority electrons. The VBM values of the minority state electrons, on the other hand, vary with the applied approximation.

First, it is striking that the VBM values are below the Fermi energy levels, so these values are negative. In the GGA and GGA + mBJ approximations, while the VBM values were $-0.047$ eV, the VBM values increased numerically with increasing U values. The increment in U values resulted in the displacement of valence band values away from the Fermi energy levels. However, these energy divergences are more striking in the conduction band. The CBM was 0.087 eV using the GGA approximation, while it was 1.911 eV using the GGA + mBJ. The CBM values were 0.491 eV, 0.899 eV, 1.303 eV, and 1.693 eV for U = 1, 2, 3, and 4 eV values in the GGA + U approximation, respectively. Therefore, the semiconductor feature of $\text{RhY}_2\text{O}_4$ was seen in all approximations.

Under the GGA approximation, the semiconductor band gap value for the majority electron states was 0.352 eV, and for the minority electron states, it was 0.134 eV. In Mn–Y–O spinel [30], utilizing the GGA approximation yielded a semiconductor band gap of 0.539 eV for majority electron states and 3.422 eV for minority electron states. These values were significantly larger compared to $\text{RhY}_2\text{O}_4$ oxide spinel. Therefore, using the 4d transition metal Rh resulted in observable reductions in the band structures of the oxide spinel.

The acquired band gaps are presented in Fig. 4, demonstrating their dependence on the changing lattice parameters. The changing lattice parameter values here are the lattice parameter values corresponding to the volume values obtained to obtain the lowest energy value while performing the optimization of $\text{RhY}_2\text{O}_4$ oxide spinel. These volume values correspond to the changes of $-5\%$, $-4\%$, $-3\%$, $-2\%$, $-1\%$, $0\%$, $1\%$, $2\%$, $3\%$, $4\%$, and $5\%$ of the equilibrium points of 9.46 Å for GGA approximation, and 9.49 Å, 9.52 Å, 9.55 Å and 9.58 Å for GGA + U approximations, respectively. When the lattice parameter increases, the semiconductor band gaps also increase. In Mn–Y–O spinel [30], as the lattice parameter increases, the band gaps in the majority electron states increase, while in the minority electron states, they decrease. When only the GGA approximation was used, band gaps were not observed in $\text{RhY}_2\text{O}_4$ oxide spinel at 9.30 Å and 9.33 Å lattice parameters, and the spinel showed metallic character in that range.

To examine the electron densities of states within the band structures, Figs. 5, 6, and 7 present the total and partial densities of states obtained for the different approximations of $\text{RhY}_2\text{O}_4$.

When the GGA approximation is used, almost 100% symmetry is seen in up and down spin electrons in the range of $-5$ eV to $-2$ eV and 2 eV to $+6$ eV. Electrons may be paired in these regions. Vertical dotted lines represent the sharp divergent peaks around the Fermi energy levels. In the negative energy regions closest to the Fermi

<table>
<caption>Table 1 The obtained initial state values of RhY₂O₄ for different approximations</caption>
<thead>
<tr>
<th>Spinel</th>
<th>Phases</th>
<th>a (Å)</th>
<th>B (GPa)</th>
<th>B`</th>
<th>V₀ (a.u.)³</th>
<th>E₀ (Ry)</th>
</tr>
</thead>
<tbody>
<tr>
<td>RhY₂O₄</td>
<td>FM</td>
<td>9.46</td>
<td>134.119</td>
<td>4.37</td>
<td>1427.13</td>
<td>− 47,431.966</td>
</tr>
<tr>
<td></td>
<td>NM</td>
<td>9.41</td>
<td>135.731</td>
<td>4.57</td>
<td>1403.87</td>
<td>− 47,431.888</td>
</tr>
<tr>
<td></td>
<td>U = 1 eV</td>
<td>9.49</td>
<td>131.805</td>
<td>4.67</td>
<td>1440.69</td>
<td>− 47,431.786</td>
</tr>
<tr>
<td></td>
<td>U = 2 eV</td>
<td>9.52</td>
<td>130.341</td>
<td>4.42</td>
<td>1454.31</td>
<td>− 47,431.616</td>
</tr>
<tr>
<td></td>
<td>U = 3 eV</td>
<td>9.55</td>
<td>128.272</td>
<td>4.47</td>
<td>1467.63</td>
<td>− 47,431.453</td>
</tr>
<tr>
<td></td>
<td>U = 4 eV</td>
<td>9.58</td>
<td>127.272</td>
<td>4.15</td>
<td>1480.85</td>
<td>− 47,431.298</td>
</tr>
</tbody>
</table>

![](./images/1138969294827159552_3.jpg)

Fig. 3 The calculated majority and minority state electron band structures of RhY₂O₄ for different approximations

energy level, electron pairings in the up and down spins are quite strong. However, in the lower spins, sharp electron density peaks in the energy region closest to the Fermi energy level are striking. It is possible to say that this peak is far away from the Fermi energy level when the GGA + mBJ approximation is used. The band gap of 1.911 eV in Table 2 directly represents this peak.

Figure 6 shows that the sharply paired electrons in the range of − 6 eV to − 2 eV come from the p orbitals of O atoms. The main contributions from the transition metal Y are in the positive energy region. The electron densities at the Fermi energy level originate from the d orbitals of the transition metal Rh. In Fig. 6, when the GGA + mBJ approximation is used, the splitting from the Fermi energy level in the conduction band (positive energy region) is

<table>
<caption>Table 2 The calculated VBM, CBM, and band gap of RhY₂O₄ for majority and minority state electrons</caption>
<thead>
<tr>
<th>Spinel</th>
<th>Approximation</th>
<th>VBMᵐᵃʲᵒʳⁱᵗʸ (eV)</th>
<th>CBMᵐᵃʲᵒʳⁱᵗʸ (eV)</th>
<th>Gapᵐᵃʲᵒʳⁱᵗʸ (eV)</th>
<th>VBMᵐⁱⁿᵒʳⁱᵗʸ (eV)</th>
<th>CBMᵐⁱⁿᵒʳⁱᵗʸ (eV)</th>
<th>Gapᵐⁱⁿᵒʳⁱᵗʸ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>RhY₂O₄</td>
<td>GGA</td>
<td>0</td>
<td>0.352</td>
<td><b>0.352</b></td>
<td>− 0.047</td>
<td>0.087</td>
<td><b>0.134</b></td>
</tr>
<tr>
<td></td>
<td>GGA + mBJ</td>
<td>0</td>
<td>1.673</td>
<td><b>1.673</b></td>
<td>− 0.047</td>
<td>1.911</td>
<td><b>1.958</b></td>
</tr>
<tr>
<td></td>
<td>U = 1 eV</td>
<td>0</td>
<td>0.600</td>
<td><b>0.600</b></td>
<td>− 0.055</td>
<td>0.491</td>
<td><b>0.546</b></td>
</tr>
<tr>
<td></td>
<td>U = 2 eV</td>
<td>0</td>
<td>0.845</td>
<td><b>0.845</b></td>
<td>− 0.079</td>
<td>0.899</td>
<td><b>0.978</b></td>
</tr>
<tr>
<td></td>
<td>U = 3 eV</td>
<td>0</td>
<td>1.078</td>
<td><b>1.078</b></td>
<td>− 0.116</td>
<td>1.303</td>
<td><b>1.419</b></td>
</tr>
<tr>
<td></td>
<td>U = 4 eV</td>
<td>0</td>
<td>1.292</td>
<td><b>1.292</b></td>
<td>− 0.156</td>
<td>1.693</td>
<td><b>1.849</b></td>
</tr>
</tbody>
</table>

![](./images/1138969294827159552_4.jpg)

Fig. 4 The band gaps of RhY₂O₄ oxide spinel are calculated for (a) majority and (b) minority electrons as a function of lattice parameters

![](./images/1138969294827159552_5.jpg)

Fig. 5 The plotted TDOS of RhY₂O₄ for different approximations

apparent. The GGA + mBJ approximation further increased the orbital splitting of the band structures obtained by the GGA approximation. The energy values of these splits increased compared to the GGA approximation. As illustrated in Fig. 7, alterations in electron densities are evident when U-Coulomb interactions are applied to Rh, Y, and O atoms. The differences were not observed in the interactions of atoms in the valence band (negative energy region). The Coulomb repulsive interactions applied to RhY₂O₄ oxide spinel have almost no effect on the electron states at energy densities close to the Fermi energy level in the valence band. There is no change in the densities and energy levels of the Rh, Y, and O atoms. However, this situation is precisely the opposite in the conduction band. As the Coulomb repulsive interaction amounts increase, the repulsive interactions on the majority electron carriers of the Rh, Y, and O atoms increase. As the U-potential values increase, the energy splits in the d-orbitals of the Rh and Y atoms increase, while the same situation occurs in the p-orbital of the O atom. The absence of any changes in the

Fig. 6 The plotted PDOS of
$\text{RhY}_2\text{O}_4$ for GGA and
GGA + mBJ approximations

![](./images/1138969294827159552_6.jpg)

![](./images/1138969294827159552_7.jpg)

Fig. 7 The obtained PDOS of $\text{RhY}_2\text{O}_4$ oxide spinel for GGA + U approximation

electron density interactions at the valence band maximum
values and the increase in the energy split values in the
conduction band have increased the semiconductor band
gaps due to the Coulomb repulsive interactions. Therefore,
the rise in semiconductor band gap values, as indicated in
Table 2 with increasing U values, supports these
observations.

The structural stability of $\text{RhY}_2\text{O}_4$ oxide spinel was
determined by Born's stability conditions for cubic struc-
tures [31].

$$
\begin{aligned}
& C_{11}>0, C_{44}>0, C_{11}-C_{12}>0, C_{11} \\
& +2 C_{12}>0, C_{12}<B<C_{11}
\end{aligned} \tag{1}
$$

If the obtained elastic constants $\text{C}_{ij}$ and the bulk

modulus of the structure for which the elastic calculations are performed meet the conditions given above, it is said that the structure is elastically stable. If the structure is elastically stable, it is possible to obtain other parameters that will determine the brittleness and ductility of the structure using the elastic constants $C_{ij}$ obtained. Bulk modulus (B), shear modulus (G), Young's modulus (E), Cauchy's pressure ($C''$), and Poisson's ratios (v) can be obtained from these parameters using the formulas given below [32-34].

$$
B=\frac{1}{3}\left(C_{11}+2 C_{12}\right) \tag{2}
$$

$$
G=\frac{1}{5}\left(C_{11}-C_{12}+3 C_{44}\right) \tag{3}
$$

$$
E=\frac{9 B G}{3 B+G} \tag{4}
$$

$$
C^{\prime \prime}=C_{12}-C_{44} \tag{5}
$$

$$
v=\frac{3 B-2 G}{2(3 B+G)} \tag{6}
$$

All the elastic parameters obtained for $RhY_2O_4$ oxide spinel are given in Table 3 for 0-50 GPa. However, the pressure-dependent elastic properties of $RhY_2O_4$ spinel were investigated. The pressure range is set between 0 and 50 GPa.

$C_{11}$, $C_{12}$, and $C_{44}$ values in Table 3 satisfy Born's stability conditions given in Eq. 1. Also, the bulk modulus value obtained using elastic constants and Eq. 2 is in the $C_{11}$ and $C_{12}$ values range. Therefore, it can be said that $RhY_2O_4$ is structurally stable during the production phase. The changes of $C_{ij}$ constants and values of bulk, shear, and Young's modulus with varying pressure are given in Fig. 8. $C_{11}$ and $C_{44}$ values increase with increasing pressure, while $C_{12}$ values decrease. B, G, and E-values increase with increasing pressure. Meanwhile, the bulk modulus value obtained with the help of elastic constants is 133.750 GPa, while the bulk modulus value obtained with the ground state values and given in Table 1 is 134.119 GPa. The fact that both results are almost the same shows that the initial and elastic calculations are compatible.

Critical values of B/G, $C_{12}$-$C_{44}$, and v-values are used to determine the brittleness or ductility of structures. If a material's v and B/G-values are greater than 0.26 and 1.75, respectively, the material is ductile. Otherwise, it is brittle [35-38]. If the $C_{12}$-$C_{44}$ is positive, the material is ductile. The B/G, v, and $C_{12}$-$C_{44}$ values of $RhY_2O_4$ were obtained as 1.92, 0.278, and 15.485 GPa, respectively. According to these results, $RhY_2O_4$ oxide spinel is ductile at 0 GPa pressure. Figure 9 shows the changes in ductility of $RhY_2O_4$ oxide spinel with pressure.

As can be seen, the $C_{12}$-$C_{44}$, B/G, and v-values decrease with increasing pressure. $RhY_2O_4$ was obtained as ductile. However, as the applied external pressure increases, the ductility of the $RhY_2O_4$ spinel is lost, and the spinel turns into a brittle structure. The brittle structure began to be observed after a pressure of about 10 GPa. When the pressure of 250 GPa is applied, the v of Mn-Y-O oxide spinel becomes zero. Mn-Y-O oxide spinel [30] also met Born's elastic stability conditions. At 0 GPa pressure, the B/G and v-values were 1.459 and 0.221, respectively. Therefore, at 0 GPa pressure, Mn-Y-O is obtained as brittle, while $RhY_2O_4$ is ductile.

As a final step in the elastic calculations, the Debye temperatures of $RhY_2O_4$ were obtained as a function of pressure. Equation 7 was used to obtain Debye temperatures.

$$
\Theta_{D}=\frac{h}{k_{B}}\left(\frac{4 \pi}{9}\right)^{\frac{1}{3}} \rho^{\frac{1}{3}}\left(\frac{1}{v_{l}^{3}}+\frac{2}{v_{s}^{3}}\right)^{\frac{-1}{3}} \tag{7}
$$

Here, the values of transverse elastic wave velocity (TEWV), the longitudinal elastic wave velocity (LEWV), and the average wave velocity (AWV) were given in Table 4 for 0-50 GPa.

The variations of TEW, LEW, and AW velocities and the Debye temperatures with pressure are given in Fig. 10. It was observed that the velocities increased as the pressure increased. Considering this increase in Eq. 7, the Debye temperature is also expected to increase. The Debye

Table 3 The calculated elastic constants and B, G, B/G, E, $C_{12}$-$C_{44}$ ($C''$) and v-values of $RhY_2O_4$

<table>
<thead>
  <tr>
    <th>Spinel</th>
    <th>Pressure (GPa)</th>
    <th>$C_{11}$ (GPa)</th>
    <th>$C_{12}$ (GPa)</th>
    <th>$C_{44}$ (GPa)</th>
    <th>B (GPa)</th>
    <th>G (GPa)</th>
    <th>B/G</th>
    <th>E (GPa)</th>
    <th>$C''$ (GPa)</th>
    <th>v</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$RhY_2O_4$</td>
    <td>0</td>
    <td>206.306</td>
    <td>97.473</td>
    <td>81.988</td>
    <td>133.750</td>
    <td>69.564</td>
    <td>1.92</td>
    <td>177.857</td>
    <td>15.485</td>
    <td>0.278</td>
  </tr>
  <tr>
    <td></td>
    <td>10</td>
    <td>222.973</td>
    <td>94.139</td>
    <td>91.988</td>
    <td>137.083</td>
    <td>79.749</td>
    <td>1.71</td>
    <td>200.387</td>
    <td>2.152</td>
    <td>0.256</td>
  </tr>
  <tr>
    <td></td>
    <td>20</td>
    <td>239.639</td>
    <td>90.806</td>
    <td>101.988</td>
    <td>140.417</td>
    <td>89.891</td>
    <td>1.56</td>
    <td>222.247</td>
    <td>− 11.182</td>
    <td>0.236</td>
  </tr>
  <tr>
    <td></td>
    <td>30</td>
    <td>256.306</td>
    <td>87.473</td>
    <td>111.988</td>
    <td>143.750</td>
    <td>100.002</td>
    <td>1.44</td>
    <td>243.533</td>
    <td>− 24.515</td>
    <td>0.217</td>
  </tr>
  <tr>
    <td></td>
    <td>40</td>
    <td>272.973</td>
    <td>84.139</td>
    <td>121.988</td>
    <td>147.083</td>
    <td>110.093</td>
    <td>1.34</td>
    <td>264.328</td>
    <td>− 37.848</td>
    <td>0.200</td>
  </tr>
  <tr>
    <td></td>
    <td>50</td>
    <td>289.639</td>
    <td>80.806</td>
    <td>131.988</td>
    <td>150.417</td>
    <td>120.168</td>
    <td>1.25</td>
    <td>284.690</td>
    <td>− 51.182</td>
    <td>0.184</td>
  </tr>
</tbody>
</table>

![](./images/1138969294827159552_8.jpg)

![](./images/1138969294827159552_9.jpg)

Fig. 9 The calculated pressure-dependent $C''$, B/G, and $v$ values of
$\text{RhY}_2\text{O}_4$

temperature of Mn–Y–O spinel [30] was calculated as
485 K, while it was calculated in $\text{RhY}_2\text{O}_4$ spinel as
480.942 K at 0 GPa. It increased proportionally with the
increase in temperature. The Debye temperature was
determined to be 625.423 K under a pressure of 50 GPa.

The total and partial magnetic moments of $\text{RhY}_2\text{O}_4$
were obtained as $6.000\ \mu_\text{B}$/f.u., $1.959\ \mu_\text{B}$, $0.058\ \mu_\text{B}$, and
$0.106\ \mu_\text{B}$ for Rh, Y, and O, respectively. The main con-
tribution comes from the Rh atom. This is an expected
result. When we examine the partial electron densities in
Figs. 6 and 7, the atom with the least coupling in the up and
down spins is the Rh atom. High couplings in the majority
and minority state electrons of the Y and O atoms
prevented the Y and O atoms from forming a net magnetic
moment. While the total magnetic moment of Mn–Y–O
spinel [30] was obtained as $10.00\ \mu_\text{B}$/cell, the most con-
tribution came from the 3d transition metal Mn. This value
is $4.106\ \mu_\text{B}$. Compared to the 4d transition metal Rh, it can
be said that the magnetic property is more in the Mn atom.

## Conclusion

The semiconductor character of $\text{RhY}_2\text{O}_4$ oxide spinel was
investigated. $\text{RhY}_2\text{O}_4$ was obtained as an FM. The lattice
parameter was determined to be $9.46\ \mathring{\text{A}}$ under the GGA
approximation, and these values experienced an increase
with the applied Coulomb interactions. The lowest band
gap values of the spinel were obtained with the GGA
approximation as 0.352 eV and 0.134 eV for the majority
and minority electron spins, respectively. It was observed
that the semiconductor characters increased considerably in
the GGA + mBJ and GGA + U. Direct band gaps at their
$\Gamma$-points are observed in all approximations for majority
state electrons. In minority state electrons, VBM is at the
$\Gamma$-points while CBM electrons are at the L-points. Minority
state electrons have indirect band gaps. $\text{RhY}_2\text{O}_4$ spinel
meets the conditions of Born’s stability and is, therefore,
elastically stable. The Debye temperature at 0 GPa pressure
was calculated as 480.942 K. At this pressure, Poisson’s
and B/G ratios were obtained as 0.278 and 1.92, respec-
tively. According to these results, $\text{RhY}_2\text{O}_4$ spinel is ductile.
However, with increasing pressure, brittle properties begin
at about 10 GPa. $\text{RhY}_2\text{O}_4$ spinel had a total magnetic
moment of $6.000\ \mu_\text{B}$/f.u. This is a very high and practical
value compared to most results. The most significant

<table>
<caption>Table 4 The calculated pressure-dependent velocities and the Debye temperatures of RhY₂O₄</caption>
<thead>
<tr>
<th>Spinel</th>
<th>Pressure (GPa)</th>
<th>TEWV (m/s)</th>
<th>LEWV (m/s)</th>
<th>AWV (m/s)</th>
<th>Θ (K)</th>
</tr>
</thead>
<tbody>
<tr>
<td>RhY₂O₄</td>
<td>0</td>
<td>3584.71</td>
<td>6468.41</td>
<td>3993.26</td>
<td>480.942</td>
</tr>
<tr>
<td></td>
<td>10</td>
<td>3838.17</td>
<td>6705.56</td>
<td>4264.29</td>
<td>513.584</td>
</tr>
<tr>
<td></td>
<td>20</td>
<td>4074.92</td>
<td>6933.86</td>
<td>4516.73</td>
<td>543.988</td>
</tr>
<tr>
<td></td>
<td>30</td>
<td>4297.99</td>
<td>7154.33</td>
<td>4754.04</td>
<td>572.570</td>
</tr>
<tr>
<td></td>
<td>40</td>
<td>4509.63</td>
<td>7367.87</td>
<td>4978.81</td>
<td>599.641</td>
</tr>
<tr>
<td></td>
<td>50</td>
<td>4711.46</td>
<td>7575.14</td>
<td>5192.88</td>
<td>625.423</td>
</tr>
</tbody>
</table>

Fig. 10 The obtained pressure-
dependent TEWV, LEWV,
AWV, and the Debye
temperatures of RhY₂O₄
![](./images/1138969294827159552_10.jpg)

contribution came from the Rh transition metal. Given its elastic, electronic, and magnetic properties, $RhY_2O_4$ oxide spinel has been identified as a promising material for semiconductor technologies.

Author contributions Fermin Ak: data curation, investigation, writing—reviewing, and editing. Evren Görkem Özdemir: conceptu-alization, investigation, methodology, software, and writing—original draft preparation. Hossein A. Rahnamaye Aliabad: data curation, investigation, writing—reviewing, and editing.

Funding Open access funding provided by the Scientific and Tech-nological Research Council of Türkiye (TÜBİTAK). The authors declare that no funds, grants, or other support were received during the preparation of this manuscript.

Data availability All data is available in the article.

Declarations

Conflict of interest The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

1. K J Kim and J W Heo Journal of the Korean Physical Society 60 1376 (2012).
2. S Sarkar and T Saha-Dasgupta Physical Review B 84 235112 (2011).
3. E Agostinelli, C Battistoni, D Fiorani, G Mattogno and M Nogues Journal of Physics and Chemistry of Solids 50 269 (1989).
4. R W Grimes, A B Anderson and A H Heuer Journal of the American Chemistry Society 111 1 (1989).
5. V S Zhandun and A V Nemtsev Materials Chemistry and Physics 259 124065 (2021).
6. V S Zhandun Journal of Magnetism and Magnetic Materials 533 168015 (2021).
7. J Choisnet, M Hervieu, B Raveau and P Tarte Journal of Solid State Chemistry 45 280 (1982).
8. J M Recio, R Franco, A M Pendas, M A Blanco and L Pueyo Physical Review B 63 184101 (2001).
9. R J Wiglusz, T Grzyb, S Lis and W Strek Journal of Nanoscience and Nanotechnology 9 5803 (2009).
10. J A Grisales Cerón, D A Landínez Téllez and J Roa Rojas Journal of Electronic Materials 51 822 (2022).
11. M A Rafiq, A Javed, M N Rasul, M Nadeem, F Iqbal and A Hussain Materials Chemistry and Physics 257 123794 (2021).
12. E Chikoidze et al. Crystal Growth&Design 20 2535 (2020).

13. H Dixit, N Tandon, S Cottenier, R Saniz, D Lamoen, B Partoens, V Van Speybroeck and M Waroquier *New Journal of Physics* **13** 063002 (2011).

14. M Suzuki *Journal of Physics and Chemistry of Solids* **41** 1253 (1980).

15. S Dubey, J A Abraham, K Dubey, V Sahu, A Modi, G Pagare and N K Gaur *Physica B: Condensed Matter* **672** 415452 (2024).

16. T Maitra and R Valenti *Journal of Physics: Condensed Matter* **17** 7417 (2005).

17. C Doroftei, O S Prelipceanu, A Carlescu, L Leontie and M Prelipceanu $14^{th}$ *International Conference on Development and Application Systems*, Suceava, Romania, May 24–26 (2018)

18. K T Jacob, D Prusty and G M Kale *Journal of Alloys and Compounds* **513** 365 (2012).

19. K Li, L Zeng, L Li, R Chen, P Yu, K Wang, C Zhang, Z Xiang and H Luo *Journal of Alloys and Compounds* **995** 174756 (2024).

20. M S Akbar, A Hussain, A Javed, M A Rafiq and M N Rasul *Journal of Magnetism and Magnetic Materials* **589** 171605 (2024).

21. P Blaha, K Schwarz, G K H Madsen, D Hvasnicka, J Luitz and K Schwarz Techn. Univ. Wien, Austria, ISBN 3-9501031-1-2 (2001)

22. F Tran and P Blaha *Physical Review Letters* **102** 226401 (2009).

23. P Blaha, K Schwarz, F Tran, R Laskowski, G K H Madsen and L D Marks *The Journal of Chemical Physics* **152** 074101 (2020).

24. J P Perdew, K Burke and M Ernzerhof *Physical Review Letters* **77** 3865 (1996).

25. L J Bennett and G Jones *Physical Chemistry Chemical Physics* **16** 21032 (2014).

26. S A Dar, V Srivastava, U K Sakalle, A Rashid and G Pagare *Material Research Express* **5** 026106 (2018).

27. E G Özdemir *Journal of Superconductivity and Novel Magnetism* **35** 3745 (2022).

28. M Jamal, S J Asadabadi, I Ahmad and H A R Aliabad *Computational Materials Science* **95** 592 (2014).

29. F D Murnaghan *Proceedings of the National Academy of Sciences, United States of America* **30** 9 (1944).

30. E G Özdemir and S Doğruer *European Physical Journal Plus* **138** 23 (2023).

31. M Born and K Huang *Dynamical Theory of Crystal Lattices*, vol 420 (Oxford: Clarendon) (1954)

32. T S Dağ, A Gencer, Y Ciftci and G Surucu *Journal of Magnetism and Magnetic Materials* **560** 169620 (2020).

33. H Wang, Y Zhan and M Pang *Computational Materials Science* **54** 16 (2012).

34. E G Özdemir and Z Merdan *Journal of Magnetism and Magnetic Materials* **514** 167198 (2020).

35. Y O Ciftci, C Coban, M Evecen and İK Durukan *Materials Chemistry and Physics* **291** 126695 (2022).

36. V Ashwin and M M S Sirajuddeen *Physica B: Condensed Matter* **654** 414521 (2022).

37. Q Fan, S R Zhang, H J Hou and J H Yang *Vacuum* **208** 111648 (2023).

38. M Zanib, G M Mustafa, M W Iqbal, B Younas, A Mahmood and M Iqbal *Materials Science in Semiconductor Processing* **169** 107890 (2024).

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.