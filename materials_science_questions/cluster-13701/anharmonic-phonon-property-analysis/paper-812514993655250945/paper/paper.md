# First-principles study of the atomic volume of hydrogen in palladium

Samaneh Sadat Setayandehⁱⁱ, Tim Gouldⁱⁱ, Aminollah Vaezᵇ, Keith McLennanⁱⁱ, Nicolas Armanetᶜ, Evan Grayⁱⁱ,∗

ⁱⁱ Queensland Micro and Nanotechnology Centre, Griffith University, Nathan 4111, Brisbane, Australia
ᵇ Faculty of Physics, University of Isfahan, Isfahan, Iran
ᶜ International Institute for Hydrogen Materials Research (i2-HMR), Bourgoin Jallieu, France

---

## ARTICLE INFO

**Article history:**
Received 29 September 2020
Received in revised form 23 December 2020
Accepted 9 January 2021
Available online 12 January 2021

**Keywords:**
Palladium hydride
Band structure
Density of states
Atomic volume
Mixed interstitial occupancy

---

## ABSTRACT

The partial atomic volume of hydrogen, $v_H$, is a fundamentally important thermodynamic parameter of interstitial metal hydrides in which dissociated H occupies interstices in the metal lattice. Such an important property should be able to be reliably calculated by a suitable theory or model in order to explain and understand its origin. In practice, $v_H$ is typically obtained by means of *ab initio* calculations founded on density functional theory (DFT), where the equilibrium lattice constant at zero temperature is found by minimising the Born-Oppenheimer energy. While the absolute lattice constants calculated in this way depend quite strongly on the DFT scheme employed, the present work showed that $v_H$ is rather robust against differing calculational approaches, thus making a meaningful comparison of theory and experiment possible. Comparing $v_H$ for PdₙH (0 < n < 8) calculated with DFT and obtained from *in-situ* neutron diffraction measurements revealed a significant discrepancy when octahedral-only interstitial occupancy was assumed. Calculations for PdH with mixed octahedral and tetrahedral occupancy gave a value for $v_H$ in agreement with experiment assuming that PdH contains 15–20% tetrahedral H.

© 2021 Elsevier B.V. All rights reserved.

---

## 1. Introduction

During the past two decades there has been improving convergence between computational techniques applied to calculating physical properties of materials and experiments to measure those properties. Superconductivity in polyhydrides is an outstanding example of this convergence [1]. Computational techniques have also been applied systematically to predicting the hydrogen storage properties of numerous hypothetical materials [2], although few have been synthesised to confirm the calculations.

Computational techniques, especially those founded on density functional theory (DFT), have been applied to the archetypal interstitial metal-hydrogen system Pd-H₂ since the 1970s [3–14]. While there is very good agreement between the many modern calculations of electron band structure, suggesting that they are as accurate as possible given the approximations involved (typically the local density approximation (LDA) [15] and the generalised gradient approximation (GGA) [16] applied within the Born-Oppenheimer approximation), there is poorer agreement among calculations of the phonon bands, especially the optical bands, even among those employing ostensibly the same DFT scheme [17]. The agreement between calculations and experiment is generally very poor for the optical bands, particularly in relation to the existence of a phonon band gap [18]. Anharmonicity of the potential in the octahedral (*oct*) interstitial site occupied by H is implicated, but the most recent attempts to account for it do not yet provide quantitative agreement with experimental results for the phonon dispersion [19,20].

One of the most fundamental properties of an interstitial metal hydride is the partial atomic volume of hydrogen, $v_H$, *i.e.* the increase in the volume of the crystal per H atom incorporated (in Å³/H). This volume increase is readily predicted by first-principles calculations to find the equilibrium lattice constant(s) at 0 K through minimising the total energy in the Born-Oppenheimer approximation and thus excluding phonon energy. Experimentally, $v_H$ may be found from length measurements such as dilation and, especially, lattice constants extracted from x-ray diffraction (XRD) or neutron (ND) profiles. These aspects were reviewed by Peisl [21] (see §§ 3.3.1 and 3.3.2) and Manchester et al. [22] (see p. 73). Interestingly, $v_H$ has been found from experiments to be surprisingly constant over a range of metallic hosts [21] (see §§ 3.4.4 and 3.4.5). Fukai [23] (see § 4.2) further examined the dependence of $v_H$ on the host metal and found differences between lanthanides and *d*-band metals. For *d*-band hosts, $v_H$ is larger for tetrahedral sites (2.9(3) Å³/H) than for octahedral sites (2.2(3) Å³/H). Fukai explains these differences as

---

∗ Corresponding author.
E-mail address: e.gray@griffith.edu.au (E. Gray).

https://doi.org/10.1016/j.jallcom.2021.158713
0925-8388/© 2021 Elsevier B.V. All rights reserved.

![](./images/812514993655250945_1.jpg)

Fig. 1. Conventional FCC unit cell showing (a) oct and (b) tet interstitial sites. In PdH(tet) half the tet sites are occupied.

having electronic origins. Significantly for this study, $v_{\mathrm{H}}$ is rather independent of temperature [22] (see p. 73), at least for normal temperatures far below the Fermi temperature, suggesting that the hydrogen-induced expansion is indeed of electronic origin, with little dependence on phonons. This is confirmed experimentally by the small isotopic dependence of the measured lattice constant between $\mathrm{PdH}_{x}$ and $\mathrm{PdD}_{x}$ with $x$ approaching one [24-26]. A stringent comparison between theory and experiment is thus possible without explicit phonon calculations, but to the authors' knowledge has not been made for the $\mathrm{Pd}-\mathrm{H}_{2}$ system, except in part in the study of FeH by Antonov et al. (see Table SII in [27]).

Such a comparison is pertinent to the long-standing controversy concerning a downward trend in the measured rate of increase of the volume of a FCC $\mathrm{PdH}_{x}$ unit cell relative to $\operatorname{Pd}\left(\Delta V_{\text {cell }}=x \cdot v_{\mathrm{H}}\right)$ with added $\mathrm{H}$, corresponding to $v_{\mathrm{H}} \approx 2.88 \AA^{3} / \mathrm{H}$ below about $x=0.75$ and decreasing to a much lower value above this concentration, as reported by Baranowski et al. [28], based on XRD measurements. Such experiments are very difficult, requiring kilobar hydrogen pressures along with a means of measuring the $\mathrm{H}$ concentration accurately. Based on neutron diffraction measurements on $\mathrm{Ni}_{0.8} \mathrm{Fe}_{0.2} \mathrm{H} / \mathrm{D}_{x}$, in which a similar phenomenon was observed with XRD, Antonov et al. [29] concluded that this change of slope in the $\Delta V_{\text {cell }}$ vs $x$ plot arises from higher $\mathrm{H}$ concentration at the surface (sampled by XRD) than in the bulk of the samples (sampled by ND) with intermediate values of $x$ resulting from strong decrease in the $\mathrm{H}$ or D diffusion rate caused by supercritical fluctuations at the temperature where the samples were prepared. In a new XRD study of the $\mathrm{Pd}-\mathrm{H}_{2}$ system, Antonov et al. [30] re-examined the reported change of slope at $x=0.75$ employing samples hydrogenated above the critical temperature. They found that $\Delta V_{\text {cell }}$ due to $\mathrm{H}$ uptake by Pd (and its FCC alloy with Au) could be described by Vegard's law for the full range $0 \leq x \leq 1.0$ with a slope of $2.51 \AA^{3} / \mathrm{H}$, exhibiting no downward trend at high $x$ values. It was concluded that the change of slope is likely an artefact of the interaction of x-rays with just the sample surface, caused by passage through the two-phase region of the $T-x$ phase diagram.

A further controversy associated with this most-studied of all metal-hydrogen systems is the persistence of suggestions that under some circumstances there is partial occupancy of the tetrahedral (tet) interstitial site in addition to the octahedral (oct) site for $x<1$: see e.g. pp. 184-185 in Ref. [31], p. 603 in Ref. [32] and refs. [33-35]. Tetrahedral occupancy has also been proposed in the deuterides of Pd-Au alloys [36]. It is worth noting that early experiments and later calculations aimed at deciding the interstitial occupancy of hydrogen in stoichiometric PdH/D only tested the $100 \%$ oct and $100 \%$ tet occupancy alternatives, without considering the possibility of mixed occupancy [18], with the exception of the recent work of Antonov et al. [27]. Given a binary choice, the evidence supporting $100 \% \mathrm{PdH}$ (oct) over $100 \% \mathrm{PdH}($ tet) is very strong. Zero-temperature DFT calculations, reviewed by Setayandeh et al. in Ref. [18] and tested systematically in ref. [17], routinely show that the total (Born-Oppenheimer) energy of the electron-nucleus system is slightly higher for the oct alternative, but the inclusion of zero-point energy reverses the stability order [37]. Lattice constants predicted for the $100 \%$ tet alternative by DFT are clearly larger than any found by experiment [17,18]. Neutron diffraction experiments, reviewed in Ref. [33], established that the choice between oct-only and tet-only D occupancy in $\mathrm{PdD}_{x}(0<x<1)$ formed at room temperature was clearly in favour of the oct alternative.

In this paper, these two controversies are further examined by means of DFT calculations. DFT is applied first to calculating the electronic properties of $\mathrm{PdH}_{x}$ with fractional oct occupancy and of PdH with mixed oct and tet occupancy. Then $\Delta V_{\text {cell }}$ in $\mathrm{PdH}_{x}$ is calculated as a function of $x$. Finally, the volume of $\mathrm{PdH}_{1}$ relative to $\mathrm{PdH}_{0}$ is calculated for mixed $\mathrm{H}$ occupancy of oct and tet sites. The results are compared to those from published in-situ neutron diffraction experiments on $\mathrm{PdD}_{x}$ with independent confirmation of the D concentration.

### 2. Structures investigated

Fig. 1 illustrates the oct and tet interstitial sites in the conventional face-centred cubic (FCC) unit cell.

The primitive cell cannot accommodate variations in the number of placement of $\mathrm{H}$ atoms. To overcome this limitation, supercells consisting of eight primitive FCC unit cells $(2 \times 2 \times 2)$ were employed to deal with the lowered symmetry of the atomic arrangement caused by $\mathrm{H} / \mathrm{Pd}$ ratios $<1$ and mixed oct and tet occupancy.

Calculations of atomic volume used cells with functional unit $\mathrm{Pd}_{8} \mathrm{H}_{0}, \mathrm{Pd}_{8} \mathrm{H}_{1}, \mathrm{Pd}_{8} \mathrm{H}_{2}, \mathrm{Pd}_{8} \mathrm{H}_{3}, \mathrm{Pd}_{8} \mathrm{H}_{4}, \mathrm{Pd}_{8} \mathrm{H}_{5}, \mathrm{Pd}_{8} \mathrm{H}_{6}, \mathrm{Pd}_{8} \mathrm{H}_{7}$ and $\mathrm{Pd}_{8} \mathrm{H}_{8}$. In all cases, only the oct sites were occupied with $\mathrm{H}$.

Calculations were also performed for $\mathrm{PdH}(100 \%$ tet) (six configurations), $\mathrm{PdH}(75 \%$ tet $+25 \%$ oct) (twelve configurations), $\mathrm{PdH}(50 \%$ tet $+50 \%$ oct) (six configurations) and $\mathrm{PdH}(25 \%$ tet $+75 \%$ oct) (six configurations). Fig. 2 shows one possible configuration of each supercell, together with the only possible configurations of $\mathrm{PdH}(100 \%$ oct) and Pd in the same supercell. The configurations considered in this study represent a subset of a stochastically-obtained (and most likely comprehensive) set of geometries with the given ratio of oct and tet sites in a $2 \times 2 \times 2$ supercell, which was found by evaluating 1000 random cells and selecting only those that were distinct in energy (i.e. that were not related to each other by symmetries) using a representative energy model. The O(10) distinct cells thus found

![](./images/812514993655250945_2.jpg)
![](./images/812514993655250945_3.jpg)
![](./images/812514993655250945_4.jpg)
![](./images/812514993655250945_5.jpg)
![](./images/812514993655250945_6.jpg)
![](./images/812514993655250945_7.jpg)

Fig. 2. Supercell representations of the structures of the lowest-energy configuration of (a) PdH(tet); (b) PdH(75% tet + 25% oct); (c) PdH(50% tet + 50% oct); d) PdH(25% tet + 75% oct); and the only possible configuration of (e) PdH(oct) and (f) Pd. Each supercell consists of 8 rhombohedral primitive unit cells of the FCC lattice. Red/dark H: oct; pink/light H: tet.

were then evaluated at the DFT level, and ranked according to energy. The geometries for which detailed calculations were performed were selected to have energies within 50 meV = 580 K of the lowest possible energy (regardless of density functional approximation) meaning that they might be accessible at room temperature.

Fig. 3 shows relative energies,

$$
\Delta E_{\text{lattice}} = E_{\text{config}} - f_{\text{tet}} E(tet) - f_{\text{oct}} E(oct) \tag{1}
$$

of "lattice" formation of different configurations. Here $f_{tet}/E(tet)$ and $f_{oct}/$ $E(oct)$ are the fractions/energies of 100% tet and oct PdH. All energies are calculated using the DFT method described in the next section. These numbers do not account for lattice effects and do not consider barrier energies, so are provided for descriptive purposes only.

## 3. Computational methods

Ab initio calculations were performed using the Quantum Espresso package [38]. As noted where the results are presented, the exchange-correlation functional was considered within the LDA [15], GGA PBE [16] or PBESol [39,40] approximations. Ion cores were described by projector-augmented wave (PAW) methods [41] or ultrasoft pseudopotentials (USPP) [42]. The Monkhorst-Pack mesh was used to sample the Brillouin zone. All structures were optimised by relaxing their lattice vectors and internal coordinates. Following a series of convergence tests, an energy cut-off of 60 Ry and a $k$ grid of $12×12×12$ points were adopted. Fig. 4 shows a sample convergence for the value of energy cut-off for PdH(50% tet).

Band-structure calculations were performed at high-symmetry $k$ points selected for each primitive unit cell with the SeeK-path tool [43,44].

In order to select the most probable configuration of each supercell with mixed oct and tet occupancy, enthalpies of formation were calculated for six, twelve, six and six possible configurations respectively of PdH(100% tet), PdH(75% tet + 25% oct), PdH(50% tet + 50% oct) and PdH(25% tet + 75% oct) and the most stable was used for the calculations of band structure.

![](./images/812514993655250945_8.jpg)

Fig. 3. Relative energy of possible configurations with mixed oct and tet H occupancy in a 2×2×2 superlattice. (a) 100% tet; (b) 75% tet; (c) 50% tet; (d) 25% tet.

![](./images/812514993655250945_9.jpg)

Fig. 4. Convergence of total energy with increasing the value of energy cut-off for PdH (50% tet)with the PBE/PAW scheme, relative to the last value (cut-off=120 Ry). An energy cut-off of 60 Ry was selected for all subsequent calculations.

Enthalpies of formation per Pd atom were calculated at zero temperature as

$$
\Delta H_{f}(x)=E\left(\mathrm{PdH}_{x}\right)-E(\mathrm{Pd})-\frac{x}{2} E\left(\mathrm{H}_{2}\right)
\tag{2}
$$

where $E(\mathrm{PdH}_{x})$ and $E(\mathrm{Pd})$ are the total Born-Oppenheimer energies of the corresponding Pd + H configuration and an isolated palladium atom respectively. It was assumed that$E(\mathrm{H}_{2}) \simeq E^{0}(\mathrm{H}_{2})$, the total energy of an isolated $\mathrm{H}_{2}$ molecule. In Eq. (2), $x$ is the hydrogen-to-metal ratio defined by $x=m / n$ for the reaction

$$
n \mathrm{Pd}+\frac{m}{2} \mathrm{H}_{2} \rightleftharpoons n \mathrm{PdH}_{x}
\tag{3}
$$

### 4. Formation enthalpy and lattice constant

Table 1 shows the variation of the calculated formation enthalpy and lattice constant with mixed interstitial occupancy for the

<table><caption>Table 1
Calculated enthalpy of formation (per Pd atom) and lattice constant of Pd and PdH with mixed oct and tet interstitial occupancy. All calculations employed the 2×2×2 supercell. For comparison, experimental lattice constants are 4.09 Å and 4.0953 Å for PdH at 77 K [24] and 85 K [30] respectively, and 3.881 Å at 0 K for Pd [46].</caption>
<thead>
<tr>
<th>Schemes</th>
<th>Property</th>
<th>Pd</th>
<th colspan="5">PdH tet fraction</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>100%</th>
<th>75%</th>
<th>50%</th>
<th>25%</th>
<th>0%</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">LDA/PAW</td>
<td>$\Delta H_{f}$(eV)</td>
<td>–</td>
<td>–0.55</td>
<td>–0.39</td>
<td>–0.13</td>
<td>–0.48</td>
<td>–0.52</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>3.947</td>
<td>4.242</td>
<td>4.252</td>
<td>4.310</td>
<td>4.182</td>
<td>4.134</td>
</tr>
<tr>
<td rowspan="2">PBE/PAW</td>
<td>$\Delta H_{f}$(eV)</td>
<td>–</td>
<td>–0.24</td>
<td>–0.11</td>
<td>–0.04</td>
<td>–0.15</td>
<td>–0.17</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>3.873</td>
<td>4.180</td>
<td>4.168</td>
<td>4.152</td>
<td>4.116</td>
<td>4.064</td>
</tr>
<tr>
<td rowspan="2">PBESol/PAW</td>
<td>$\Delta H_{f}$(eV)</td>
<td>–</td>
<td>–0.42</td>
<td>–0.29</td>
<td>–0.09</td>
<td>–0.35</td>
<td>–0.39</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>3.837</td>
<td>4.124</td>
<td>4.133</td>
<td>4.102</td>
<td>4.067</td>
<td>4.036</td>
</tr>
<tr>
<td rowspan="2">LDA/USPP</td>
<td>$\Delta H_{f}$(eV)</td>
<td>–</td>
<td>–0.56</td>
<td>–0.41</td>
<td>–0.14</td>
<td>–0.49</td>
<td>–0.55</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>3.939</td>
<td>4.241</td>
<td>4.226</td>
<td>4.210</td>
<td>4.182</td>
<td>4.124</td>
</tr>
<tr>
<td rowspan="2">PBE/USPP</td>
<td>$\Delta H_{f}$(eV)</td>
<td>–</td>
<td>–0.38</td>
<td>–0.24</td>
<td>–0.07</td>
<td>–0.27</td>
<td>–0.30</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>3.874</td>
<td>4.180</td>
<td>4.162</td>
<td>4.152</td>
<td>4.112</td>
<td>4.066</td>
</tr>
<tr>
<td rowspan="2">PBESol/USPP</td>
<td>$\Delta H_{f}$(eV)</td>
<td>–</td>
<td>–0.42</td>
<td>–0.31</td>
<td>–0.10</td>
<td>–0.36</td>
<td>–0.41</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/812514993655250945_10.jpg)

Fig. 5. DoS per atom of (a) six possible configurations of PdH(100% tet), (b) twelve possible configurations of PdH(75% tet), (c) six possible configurations of PdH(50% tet) and (d) six possible configurations of PdH(25% tet), all computed for a 2 × 2 × 2 supercell of the primitive FCC cell. Numbers on the graphs correspond to the configuration number in Fig. 3.

lowest-energy configurations shown in Fig. 3. The enthalpy calculations reproduce the well-known reversal of the order of stability of PdH(oct) compared to PdH(tet) owing to the exclusion of zero-point energy [37]. In a DFT study performed without lattice relaxation, McLennan [45] found that the minimum-energy configuration occurred with one tet and 7 oct interstitials in Pd₈H₈. The present results obtained after lattice relaxation suggest that the stability difference between PdH(100% oct) and PdH(25% tet + 75% oct) is very small. Both the lattice constant and magnitude of the formation enthalpy vary between DFT schemes in the order LDA < PBESol < PBE, with the effect of the (pseudo)potential being relatively small.

## 5. Band structure and density of states

Fig. 5 shows the effect of differing H configurations (six, twelve, six and six configurations respectively of PdH(100% tet), PdH(75% tet + 25% oct), PdH(50% tet + 50% oct) and PdH(25% tet + 75% oct)) on the density of states (DoS). The differences between configurations are not drastic and all exhibit similar behaviour around the Fermi energy. Therefore it is unlikely that experiments measuring the band structure can offer insights into the nature of H occupancy.

Fig. 6 shows the band structure and DoS calculated for the minimum-energy configuration of each of the studied combinations of oct and tet occupancy. Apart from consequences of lowered symmetry, the effects of mixed oct and tet occupancy are relatively minor. The most significant features of PdHₓ, viz. bonding states below the conduction band and metallic character, are retained in all cases.

The projected density of states for each structure was also calculated, as shown in Fig. 7. The relative contributions differ little between configurations, with the exception that partial tet occupancy suppresses the contribution of Pd 5s above $E_F$.

## 6. Partial atomic volume of H

The key to the comparison presented here between first-principles calculations and experiment is the reliance on a relative measure – the increase in unit cell volume ($\Delta V_{cell}$) caused by H uptake – rather than calculated and measured lattice constants. On the theory side, the variation of calculated lattice constant for the same structure according to the adopted DFT scheme [17] is found to be greatly reduced. On the experiment side, it may be recalled that the measured $\Delta V_{cell}$ (and the corresponding $v_H$) appears to be nearly independent of temperature [22] (see p. 73), so that a comparison of notionally zero-temperature volumes becomes possible and the problem of estimating the thermal expansion between zero and the measurement temperature is avoided.

Real PdHₓ is a mixture two phases for 0.01 < x < 0.61 approximately at room temperature [47], becoming single-phase above the critical point ($T_{crit}$ = 563 ± 1 K for Pd-H₂ and $T_{crit}$ = 556 ± 1 K for Pd-D₂ [48]), with a complex phase structure developing below about 75 K for x > 0.6 [18,22]. Comparisons with experiment therefore require structural data obtained at elevated temperatures to ensure that the sample is single-phase.

![](./images/812514993655250945_11.jpg)
![](./images/812514993655250945_12.jpg)
![](./images/812514993655250945_13.jpg)
![](./images/812514993655250945_14.jpg)
![](./images/812514993655250945_15.jpg)
![](./images/812514993655250945_16.jpg)

Fig. 6. Band structure and DoS of the minimum-energy configuration of (a) PdH(100% tet), (b) PdH(75% tet), (c) PdH(50% tet) and (d) PdH(25% tet), compared to (e) PdH(100% oct) and (f) Pd, all computed for a 2×2×2 supercell of the primitive FCC cell.

### 6.1. Octahedral-only occupancy
Lattice constants were calculated at zero temperature for $Pd_8H_0$, $Pd_8H_1$, $Pd_8H_2$, $Pd_8H_3$, $Pd_8H_4$, $Pd_8H_5$, $Pd_8H_6$, $Pd_8H_7$ and $Pd_8H_8$, all with oct-only occupation of the H sites.

Fig. 8 compares the increase in the conventional FCC unit cell volume, containing 4 Pd atoms, obtained by DFT (PBESol; oct-only occupation) with that calculated from experimental lattice constants obtained at $T > T_{crit}$ by neutron diffraction with bulk samples. The DFT prediction does not follow Vegard's Law. The total calculated volume increase at H/Pd=1 is equivalent to $v_H$ =2.26 $\mathring{A}^3$/H, in excellent agreement with $\Delta V_{cell}$ values obtained from the lattice constants calculated by McLennan et al. [33], equivalent to $v_H$ =2.22 $\mathring{A}^3$/H, and consistent with what is commonly found for d-band metals: $v_H$ =2.2 ± 0.3 $\mathring{A}^3$/H for oct occupancy according to Fukai (p. 107 in Ref. [23]). In contrast, the average experimental expansion rate from neutron diffraction is $v_H$ = 2.69 ± 0.05 $\mathring{A}^3$/D. The disagreement between DFT and experiment at high H/Pd values is significant compared to the spread in the experimental results. Noting that the lattice constant of PdD is slightly higher than that of PdH [24-26] owing to the smaller vibration amplitude of D in the anharmonic real potential, the discrepancy between the ND experiments on $PdD_x$ and the DFT values is actually underestimated by about 0.5% in volume.

The agreement between the extrapolations of the two ND datasets from around 300 °C and the point obtained at 25 °C is excellent. The latter sample was also prepared at 25 °C, therefore passing through the two-phase region, which suggests that ND measurements are indeed more reliable because the entire sample is illuminated and the effect of any difference in hydrogen concentration at the surface is minimised.

The reliability of the DFT results is of key importance. Fig. 9 collates published results where lattice constants for both PdH(oct)

![](./images/812514993655250945_17.jpg)

Fig. 7. Partial DoS (pDoS) of the minimum-energy configuration of (a) PdH(100% tet), (b) PdH(75% tet), (c) PdH(50% tet) and (d) PdH(25% tet), compared to (e) PdH(100% oct) and (f) Pd, all computed for a 2×2×2 supercell of the primitive FCC cell.

and Pd were available. Some of the scatter in the volume data is contributed by lattice constants sometimes being quoted to only three significant figures. The early results of Methfessel and Kübler (1982) [50] were excluded because the calculated $v_H$ value of $3.03\ Å^3$/H is at odds with all the other data. The results of Ostanin et al. [51] (PBE/PAW) were excluded because they did not report lattice constants. Their value for the relative expansion of the oct unit cell was approximately 13.5%, compared to an average 15.2% for the results shown in Fig. 9. While the often observed trend, that lattice constants calculated within the GGA are larger than those from the LDA, is apparent, there is no such trend in the calculated volume differences, confirming the effectiveness of the representation used in decreasing the dependence on absolute lattice constants and the details of the DFT calculations.

To the authors' knowledge this is the most reliable comparison between ab initio predictions and experiment related to the partial hydrogen atomic volume to have been published. The ND results were obtained with in-situ loading of deuterium into the sample and independent measurement of the D uptake by the Sieverts (manometric) technique using carefully calibrated apparatus. The disagreement between the ND results ($v_H = 2.69 \pm 0.05\ Å^3$/D) and the latest XRD results ($v_H = 2.51 \pm 0.03\ Å^3$/H) [30] is unexplained. In-situ neutron diffraction has two significant advantages over x-rays in the present situation: first, the neutron beam illuminates the entire

![](./images/812514993655250945_18.jpg)

Fig. 8. Volume increase per conventional FCC unit cell owing to hydrogen uptake, comparing values calculated from equilibrium DFT-derived lattice constants at zero temperature with those obtained from neutron diffraction (ND) measurements on PdDx at the stated temperatures. [*] indicates this study. The error bar on the DFT average value corresponds to one standard deviation (see Fig. 9. and associated text). The long-dash line corresponds to the trend line and the diamonds to the experimental values (from x-ray diffraction) for Pd in Fig. 1 of Baranowski et al. [28], where the point at x = 0.69 comes from Ref. [49].

![](./images/812514993655250945_19.jpg)

Fig. 9. Comparison of DFT predictions of the lattice constants of Pd (open circles) and PdH(oct) (filled circles), with the corresponding partial atomic volume of H, $v_H$ (filled squares). [*] indicates this work. See the text in relation to the data from ref. [20]. The dashed line is the average of the DFT-derived values of $v_H$ (2.251 $\mathring{A}^3$/H). The thickness of the grey bar represents the spread of the values of $v_H$ obtained from neutron diffraction, extrapolated to H/Pd = 1. The span of the volume axis is equivalent to that of the lattice-constant axis, so that a direct comparison of the scatter in the data can be made [52-56].

sample volume, so that surface effects [30] contribute little to the measured diffraction peaks; second, the sample is much larger in the neutron case, so that an accurate measurement of the D uptake can be made in situ [57]. Both experimental results are significantly higher than the average DFT prediction ($v_H = 2.25 \pm 0.08 \mathring{A}^3$/H), and all are significantly smaller than the trend value of $2.88 \mathring{A}^3$/H for Pd and Pd-alloy hydrides below about x = 0.75 reported by Baranowski et al. [28].

On the DFT side, while the results are essentially independent of the DFT scheme employed, the calculations do suffer from the unknown inaccuracy in the equilibrium lattice constant of $PdH_x$ introduced by not accounting for anharmonic phonons (harmonic phonons would have less effect). Belov et al. [20] included anharmonic phonons in their LDA/PAW calculations for $Pd_{32}H$ and PdH. Linearly extrapolating $\Delta V_{cell}$ calculated from their values for the lattice constants to the interval $PdH_0$-$PdH_1$ yields $v_H = 2.284 \mathring{A}^3$, very close to the average value from calculations ignoring phonons. Errea et al. [19] also accounted for anharmonicity, and calculated lattice constants for PdH and PdD that agree quite well with x-ray diffraction measurements [24], but did not provide a calculated value for bare Pd with which to calculate $\Delta V_{cell}$.

### 6.2. Mixed octahedral and tetrahedral occupancy

Fig. 10 shows the values for $\Delta V_{cell}$ obtained for mixed oct and tet occupancy in PdH, based on the lattice constants in Table 1. In order for the calculated expansion to agree with that extrapolated from the neutron diffraction results 15-20% tet occupancy would be required.

The possibility of partial oct occupancy in $PdH_1$ finds echoes in the recent literature on $PdD_x$ for x < 1.0, having been observed in neutron diffraction measurements on nanocrystals loaded at $T < T_{crit}$, where about 31% of the tet sites were occupied [35,58]. Simultaneous occupancy of oct and tet sites has also been reported for bulk Pd-Au-D alloys loaded at $T > T_{crit}$ ($Pd_{75}Au_{25}$; 35-50% tet occupancy), and at $T < T_{crit}$ ($Pd_{90}Au_{10}$, $Pd_{80}Au_{20}$; 5-30% tet occupancy) [36,59]. Partial filling of the tet sites in $PdH_1$ and $PdD_1$ was recently predicted by the ZPE-corrected ab-initio DFT calculations of Antonov et al. [27], supporting the Boltzmann mechanism of tet occupancy proposed in refs [33,34] for bulk samples loaded at $T > T_{crit}$.

### 7. Summary and conclusions

A comparison was made between the partial atomic volume, $v_H$, of hydrogen in palladium as calculated from first principles and measured by in-situ neutron diffraction. Basing the comparison on a relative measure, the increase in unit cell volume relative to bare Pd ($\Delta V_{cell}$), rather than absolute lattice constants, made it robust: it was found that the DFT-derived value for $\Delta V_{cell}$ for 100% oct occupancy was quite insensitive to the details of the DFT scheme employed. Although the calculations were made without phonons, inclusion of anharmonic phonons [20] made no significant difference. In contrast to the many DFT-based reports of lattice constants, the DFT-derived values of $v_H$ for PdH(oct) were quite well clustered around $2.25 \pm 0.08 \mathring{A}^3$/H, and that for PdH(tet) was $3.71 \mathring{A}^3$/H.

Lattice-constant measurements from earlier in-situ neutron diffraction studies of $PdD_x$ that included values for bare Pd indicated $v_H = 2.69 \pm 0.05 \mathring{A}^3$/D. The significance of these studies is that the

![](./images/812514993655250945_20.jpg)

Fig. 10. Volume increase per conventional FCC unit cell owing to hydrogen uptake (PBE/PAW) as a function of the fraction of tet occupancy in PdH. The solid line represents the spread of the values of $\Delta V_{cell}$ obtained from neutron diffraction, extrapolated to H/Pd = 1.

entire sample was illuminated with neutrons, in contrast to the x-ray case, and the sample was large enough (grams) to permit an accurate independent measurement of the deuterium uptake in situ by the Sieverts method. Taking into account the most recent and compre- hensive XRD study [30], which found $v_{H}=2.51 \pm 0.03 \AA^{3} / H$ for PdH, the experimental value is converged reasonably well at $2.6 \pm 0.1 \AA^{3} / H, D$.

The present study does not support a definite conclusion about the slope change in the graph of $\Delta V_{cell }$ versus H/Pd reported by Baranowski et al. [28] around $x=0.75$: while the DFT and experi mental results disagree strongly in the $x$ range centred on 0.75, at around $x=1$ they are in good agreement.

Given the reproducibility of both the DFT calculations and neu- tron diffraction experiments, the significant disagreement betweenthem cannot be resolved easily, even if the slope change for $x>0.75$ is real. The fact that the most recent x-ray diffraction study [30] found that $PdH_{x}$ obeyed Vegard's Law suggests strongly that theslope change is an artefact. If so, two alternatives offer themselves: either the DFT calculations are wrong for unknown reasons, or, based on calculations of $\Delta V_{cell }$ with mixed oct and tet occupancy, a small proportion (15-20%) of tet occupancy occurs in stoichiometric PdH. Given the indications from GPA measurements of the lattice constant that $x$ saturates at 1 (at $1.9 GPa$ in Ref. [26], at $2.0 \pm 0.5 GPa$ in ref.[60], both at room temperature), the simplest interpretation is that PdH, has the oct structure. If so, the problem becomes one of un-derstanding why LDA- and GGA-level DFT is so wrong, which if truewould suggest that most of the published DFT studies on $PdH_{x}$  should be set aside. This question cannot be resolved on the basis of currently available knowledge about the $Pd-H_{2}$ system. The most direct route to a resolution is an in-situ neutron diffraction experi- ment on bulk $PdD_{x}$ to confirm the D occupancy, with simultaneous and independent measurement of the $D$ uptake by the sample, at a temperature low enough that the $D_{2}$ pressure required to approach x=1 is low enough for Sieverts-type measurements to be reliable. Such an experiment would be challenging, but without it our un- derstanding of the atomic volume of $H$ in Pd will remain in doubt. In parallel, it would be interesting to trial a higher level of DFT ap- proximation, such as meta-GGA, to see if a value for $v_{H}$ closer to experiment is obtained.

## CRediT authorship contribution statement

S.S.S. performed the DFT calculations. All authors contributed to the manuscript, which was edited by E.M.G.

## Declaration of Competing Interest

The authors declare that they have no known competing fi- nancial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

S.S.S. acknowledges receipt of Griffith University postgraduate research awards (GUPRS and GUIPRS).

We thank the authors of ref. [30] for permission to quote their unpublished results.

N.A. thanks Pole Empire, RSA for financial support, and Sci-Hub, LibGen for providing reprints.

## References

[1] J.A. Flores-Livas, L. Boeri, A. Sanna, G. Profeta, R. Arita, M. Eremets, A perspective on conventional high-temperature superconductors at high pressure: methods and materials, Phys. Rep. 856 (2020) 1-78.
[2] S.V. Alapati, J.K. Johnson, D.S. Sholl, Identification of destabilized metal hydridesfor hydrogen storage using first principles calculations, J. Phys. Chem. B 110 (17)(2006) 8769-8776.
[3] F.M. Mueller, A.J. Freeman, J.O. Dimmock, A.M. Furdyna, Electronic structure of palladium, Phys. Rev. B 1 (12) (1970) 4617-4635.
[4] A.C. Switendick, Metal hydrides-structure and band structure, Int. J. Quantum Chem. 5 (1971) 459-470.
[5] P.B. Johnson, R.W. Christy, Opticant constants of transition metals: Ti, V, Cr, Mn, Fe, Co, Ni, and Pd, Phys. Rev. B 9 (12) (1974) 5056-5070.
[6] M. Gupta, A.J. Freeman, Electronic structure and proton spin-lattice relaxation in PdH, Phys. Rev. B 17 (1978) 3029-3039.
[7] C.D. Gelatt, H. Ehrenreich, J.A. Weiss, Transition-metal hydrides: electronic structure and the heats of formation, Phys. Rev. B 17 (4) (1978) 1940-1957.
[8] E. Matsushita, Electron theory of inverse isotope effect in superconducting PdHX system, Solid State Commun. (1981) 419-421.
[9] J.W. Davenport, Linear augmented-Slater-type-orbital method for electronic- structure calculations, Phys. Rev. B 29 (6) (1984) 2896-2904.
[10] B.K. Sharma, A. Gupta, H. Singh, S. Perkki, A. Kshirsagar, D.G. Kanhere, Compton profile of palladium, Phys. Rev. B 37 (12) (1988) 6821-6826.
[11] H. Hemmes, A. Driessen, R. Griessen, M. Gupta, Isotope effects and pressure dependence of the Tc of superconducting stoichiometric PdH and PdD synthe-sized and measured in a diamond anvil cell, Phys. Rev. B: Condens. Matter 39 (7)(1989) 4110-4118.
[12] B.M. Klein, R.E. Cohen, Anharmonicity and the inverse isotope effect in the palladium-hydrogen system, Phys. Rev. B 45 (21) (1992) 12405-12414.
[13] L.E. Isaeva, D.I. Bazhanov, E.I. Isaev, S.V. Eremeev, S.E. Kulkova, I.A. Abrikosov, Dynamic stability of palladium hydride: an ab initio study, Int. J. Hydrog. Energy36 (1)(2011) 1254-1258 1254-125.
[14] A. Houari, S.F. Matar, V. Eyert, Electronic structure and crystal phase stability of palladium hydrides, J. Appl. Phys. 116 (17) (2014) 173706.
[15] J.P. Perdew, A. Zunger, Self-interaction correction to density-functional approx- imations for many-electron systems, Phys. Rev. B 23 (10) (1981) 5048-5079.
[16] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (18) (1996) 3865-3868.
[17] S.S. Setayandeh, T. Gould, A. Vaez, E. Gray, Effect of pseudopotential choice on the calculated electron and phonon band structures of palladium hydride and its vacancy defect phases, 46 (1) (2021) 943-954.
[18] S.S. Setayandeh, C.J. Webb, E.M. Gray, Electron and phonon band structures ofpalladium and palladium hydride: a review, Prog. Solid State Chem. 60 (2020)100285.
[19] I. Errea, M. Calandra, F. Mauri, First-principles theory of anharmonicity and the inverse isotope effect in superconducting palladium-hydride compounds, Phys. Rev. Lett. 111 (17) (2013) 177002.
[20] M.P. Belov, A.B. Szydykova, Y.K. Vekilov, I.A. Abrikosov, Hydrogen in palladium:anharmonicity of lattice dynamics from first principles, Phys. Solid State 57 (2)(2015) 260-265.
[21] H. Peisl, Lattice Strains due to Hydrogen in Metals, in Hydrogen in Metals I: Basic Properties, (1978), pp. 53-74.
[22] F.D. Manchester, A. San-Martin, J.M. Pitre, The H-Pd (hydrogen-palladium) System, J. Phase Equilib. 15 (1) (1994) 62-83.
[23] Y. Fukai, The metal hydrogen system, Springer Series in Materials Science, 2nd ed., Springer-Verlag, Berlin Heidelberg, 2005.
[24] J.E. Schirber, B. Morosin, Lattice constants of $\beta$ - PdHx and $\beta$ -PdDx with x near1.0, Phys. Rev. B 12 (1) (1975) 117-118.
[25] K. Brownsberger, M. Ahart, M. Somayazulu, C. Park, S.A. Gramsch, R.J. Hemley, X-ray diffraction, lattice structure, and equation of state of PdHx and PdDx to megar bar pressures, J. Phys. Chem. C 121 (49) (2017) 27327-27331.
[26] B. Guigue, G. Geneste, B. Leridon, P. Loubeyre, An x-ray study of palladium hy-drides up to 100 GPa: synthesis and isotopic effects, J. Appl. Phys. 127 (7) (2020)075901.
[27] V.E. Antonov, V.M. Gurev, V.I. Kulakov, M.A. Kuzovnikov, I.A. Sholin, V.Y. Zuykova, Solubility of deuterium and hydrogen in fcc iron at high pressures and tem- peratures, Phys. Rev. Mater. 3 (11) (2019) 113604.
[28] B. Baranowski, S. Majchrzak, T.B. Flanagan, The volume increase of fcc metals and alloys due to interstitial hydrogen over a wide range of hydrogen contents, J. Phys. F: Metal Phys. 1 (3) (1971) 258-261.
[29] V.E. Antonov, M. Baier, B. Dorner, V.K. Fedotov, G. Grosse, A.I. Kolesnikov, E.G. Ponyatovsky, G. Schneider, F.E. Wagner, High-pressure hydrides of iron and its alloys, J. Phys.: Condens. Matter 14 (25) (2002) 6427-6445.
[30] V.E. Antonov, N. Armanet, B.M. Bulychev, V.K. Fedotov, V.I. Kulakov, M.A. Kuzovnikov, I.A. Sholin, V.Y. Zuykova. In preparation 2020.
[31] B. Baranowski, Metal-hydrogen systems at high hydrogen pressures, Hydrogen in Metals II, Springer, 1978, pp. 157-200.
[32] E. Ponyatovskii, V.E. Antonov, I. Belash, Properties of high pressure phases in metal-hydrogen systems, Sov. Phys. Uspekhi 25 (8) (1982) 596-619.
[33] K.G. McLennan, E.M. Gray, J.F. Dobson, Deuterium occupation of tetrahedral sites in palladium, Phys. Rev. B 78 (1) (2008) 014104.
[34] M.P. Pitt, E.M. Gray, Tetrahedral occupancy in the Pd-D system observed by in situ neutron powder diffraction, Europhys. Lett. 64 (3) (2003) 344-350.
[35] H. Akiba, M. Kofu, H. Kobayashi, H. Kitagawa, K. Ikeda, T. Otomo, O. Yamamuro, Nanometer-size effect on hydrogen sites in palladium lattice, J. Am. Chem. Soc.138 (32)(2016) 10238-10243.
[36] D.E. Nanu, M.G. Tucker, W.G. Haije, J.F. Vente, A.J. Bottger, Atom configurations in Pd-Au and Pd-Au-D alloys: a neutron total scattering and reverse Monte Carlo study, Acta Mater. 58 (16) (2010) 5502-5510.
[37] R. Caputo, A.L.I. Alavi, Where do the $H$ atoms reside in PdH x systems? Mol. Phys101(11)(2003)1781-1787.
[38] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris,

G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, S. Braccia, S. Scandolo, G. Sclauzero, A.P. Seitsonen, A. Smogunov, P. Umari, R.M. Wentzcovitch, QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials, J. Phys.: Condens. Matter 21 (39) (2009) 395502.

[39] J.P. Perdew, A. Ruzsinszky, G.I. Csonka, O.A. Vydrov, G.E. Scuseria, L.A. Constantin, X. Zhou, K. Burke, Restoring the density-gradient expansion for exchange in solids and surfaces, Phys. Rev. Lett. 100 (13) (2008) 136406-1-4.

[40] A.E. Mattsson, R. Armiento, T.R. Mattsson, Comment on restoring the density-gradient expansion for exchange in solids and surfaces, Phys. Rev. Lett. 101 (23) (2008) 239701-1.

[41] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (24) (1994) 17953-17979.

[42] D. Vanderbilt, Soft self-consistent pseudopotentials in a generalized eigenvalue formalism, Phys. Rev. B 41 (11) (1990) 7892-7895.

[43] Y. Hinuma, G. Pizzi, Y. Kumagai, F. Oba, I. Tanaka, Band structure diagram paths based on crystallography, Comput. Mater. Sci. 128 (2017) 140-184.

[44] A. Togo, I. Tanaka. Spglib: A Software Library for Crystal Symmetry Search. arXiv:1808.01590v1 [cond-mat.mtrl-sci], 2018.

[45] K.G. McLennan, Structural Studies of the Palladium-Hydrogen System, PhD Thesis, Griffith University, 2005.

[46] J.W. Arblaster, Crystallographic properties of palladium, Platin. Met. Rev. 56 (9) (2012) 181-189.

[47] H. Frieske, E. Wicke, Magnetic susceptibility and equilibrium diagram of PdHn, Berichte der Bunsenges. Phys. Chem. 77 (1) (1973) 48-52.

[48] E. Wicke, J. Blaurock, New experiments on and interpretations of hysteresis effects of Pd-D2 and Pd-H2, J. Less Common Met. 130 (1987) 351-363.

[49] A. Maeland, T.B. Flanagan, Lattice constants and thermodynamic parameters of the hydrogen-platinum-palladium and deuterium-platinum-palladium systems, J. Phys. Chem. 68 (6) (1964) 1419-1426.

[50] M. Methfessel, J. Kubler, Bond Analysis of Heats of Formation: Application to Some Group VIII and IB Hydrides. 1982.

[51] S. Ostanin, V. Borisov, D.V. Fedorov, E.I. Salamatov, A. Ernst, I. Mertig, Role of tetrahedrally coordinated dopants in palladium hydrides on their super-conductivity and inverse isotope effect, J. Phys.: Condens. Matter 31 (7) (2019) 075703.

[52] X. Yang, H. Li, R. Ahuja, T. Kang, W. Luo, Formation and electronic properties of palladium hydrides and palladium-rhodium dihydride alloys under pressure, Sci. Rep. 7 (1) (2017) 3520.

[53] C. Elsässer, M. Fähnle, K.M. Ho, C.T. Chan, Ab initio pseudopotential calculations of total energies and forces for hydrogen in palladium, Phys. B: Condens. Matter 172 (1) (1991) 217-224.

[54] D. Tománek, Z. Sun, S.G. Louie, Ab initio calculation of chemisorption systems: H on Pd (001) and Pd (110), Phys. Rev. B 43 (6) (1991) 4699-4713.

[55] N. Fukumuro, Y. Fukai, H. Sugimoto, Y. Ishii, H. Saitoh, S. Yae, Superstoichiometric hydride PdH ≤ 2 formed by electrochemical synthesis: Dissolution as molecular H₂ proposed, J. Alloy. Compd. 825 (2020) 153830.

[56] D. Long, M. Li, D. Meng, Y. He, I.T. Yoon, R. Ahuja, W. Luo, Accounting for the thermo-stability of PdHₓ (x= 1-3) by density functional theory, Int. J. Hydrog. Energy 43 (39) (2018) 18372-18381.

[57] E.M. Gray, C.J. Webb, In-situ diffraction techniques for studying hydrogen storage materials under high hydrogen pressure, Int. J. Hydrog. Energy 37 (13) (2012) 10182-10195.

[58] M. Kofu, O. Yamamuro, Dynamics of atomic hydrogen in palladium probed by neutron spectroscopy, J. Phys. Soc. Jpn. 89 (5) (2020) 051002.

[59] D.E. Nanu, W.J. Legerstee, S.W.H. Eijt, W.G. Haije, J.F. Vente, M.G. Tucker, A.J. Böttger, Insights into the relation between crystal structure and deuterium desorption characteristics of Pd-Au-D alloys, Acta Mater. 56 (20) (2008) 6132-6140.

[60] Z.M. Geballe, M. Somayazulu, N. Armanet, A.K. Mishra, M. Ahart, High Pressure Synthesis and Thermodynamic Stability of PdH1 ± ε to 8 GPa, In Press, 2021.