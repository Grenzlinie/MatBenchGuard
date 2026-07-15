Accepted Manuscript

![](./images/812838135741284354_1.jpg)

Title: Reaction mechanisms and kinetics of the β-elimination
processes of compounds $CHF_2CH_2SiF_nMe_{3nulln}$ ($n=0$null3):
DFT and CBS-QB3 methods using
Rice-Ramsperger-Kassel-Marcus and transition state theories

Authors: Zahra Safaei, Abolfazl Shiroudi, Rahman Padash,
Mika Sillanpää, Ehsan Zahedi

<table>
  <tr>
    <td>PII:</td>
    <td>S0022-1139(18)30364-6</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.jfluchem.2018.10.009</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>FLUOR 9234</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>FLUOR</td>
  </tr>
  <tr>
    <td>Received date:</td>
    <td>16-9-2018</td>
  </tr>
  <tr>
    <td>Revised date:</td>
    <td>12-10-2018</td>
  </tr>
  <tr>
    <td>Accepted date:</td>
    <td>13-10-2018</td>
  </tr>
</table>

Please cite this article as: Safaei Z, Shiroudi A, Padash R, Sillanpää M, Zahedi
E, Reaction mechanisms and kinetics of the β-elimination processes of compounds
$CHF_2CH_2SiF_nMe_{3horbarn}$ ($n=0$horbar;3): DFT and CBS-QB3 methods using Rice-
Ramsperger-Kassel-Marcus and transition state theories, *Journal of Fluorine Chemistry*
(2018), https://doi.org/10.1016/j.jfluchem.2018.10.009

This is a PDF file of an unedited manuscript that has been accepted for publication.
As a service to our customers we are providing this early version of the manuscript.
The manuscript will undergo copyediting, typesetting, and review of the resulting proof
before it is published in its final form. Please note that during the production process
errors may be discovered which could affect the content, and all legal disclaimers that
apply to the journal pertain.

# Reaction mechanisms and kinetics of the β-elimination processes of compounds $CHF_2CH_2SiF_nMe_{3-n} (n=0-3)$: DFT and CBS-QB3 methods using Rice-Ramsperger-Kassel-Marcus and transition state theories

Zahra Safaei $^{a}$, Abolfazl Shiroudi $^{b,*}$, Rahman Padash $^{c}$, Mika Sillanpää $^{a}$, and Ehsan Zahedi $^{d}$

$^{a}$ Department of Green Chemistry, School of Engineering Science, Lappeenranta University of Technology, Sammonkatu 12, FI-50130 Mikkeli, Finland

$^{b}$ Young Researchers and Elite Club, East Tehran Branch, Islamic Azad University, Tehran, Iran

$^{c}$ Department of Chemistry, Yasouj University, Yasouj, Iran

$^{d}$ Chemistry Department, Shahrood Branch, Islamic Azad University, Shahrood, Iran

## Graphical abstract

![](./images/812838135741284354_2.jpg)

## Research Highlights

- β-elimination processes of 2,2-difluoroethylsilane and derivatives are studied theoretically
- Activation and reaction energies are computed by means of DFT and CBS-Qb3 methods
- Kinetic rate constants are obtained by means of transition state and RRKM theories
- TST approximation breaks down at pressures $P <10^{-4}$ bar for the most effective reaction

## Abstract

The gas-phase β-elimination kinetics of 2,2-difluoroethyltrifluorosilane (1), 2,2-difluoroethylmethyldifluorosilane (2), 2,2-difluoroethyldimethylfluorosilane (3), and 2,2-difluoroethyltrimethylsilane (4) have been investigated computationally using M06-2x exchange-correlation functional as well as the benchmark CBS-QB3 quantum chemical approach. The obtained energy profile has been enhanced with kinetic calculations using

---
* Corresponding author: E-mail: abolfazl.shiroudi@uhasselt.be (A. Shiroudi)

statistical Rice-Ramsperger-Kassel-Marcus (RRKM) theory and transition state theory (TST). The calculated results are in good agreement with the available experimental data which obtained by the CBS-QB3 approach. The comparison between all our calculations and experiments indicates that a thermodynamically-controlled reaction that gives more stable products derived from the compound 2 species will be the vinyl fluoride and methyltrifluorosilane species, whereas the elimination of compound 1 into the vinyl fluoride and silicon tetrafluoride species is favorable process from kinetic point of view.

In proportion to rather larger barrier heights, pressures where $P > 10^{-4}$ bar are insufficient to ensure a saturation of the calculated rate constant compared with the RRKM unimolecular rate kinetics (in high-pressure limit) .

Natural bond orbital analysis revealed that in accordance with an increase of barrier height from compounds 1 to 4, the HOMO-LUMO energy-gaps decreases. Furthermore, the obtained order of barrier heights could be explained by the number of electron-withdrawing fluorine atoms attached to the silicon atom. The occupancies of $\sigma_{C1-F3}$ bonding orbital for the studied compounds are as follows: 1>2>3>4 and those of $\sigma^{*}_{C1-F3}$ antibonding orbital increase in the opposite order (4>3>2>1) by NBO analysis. This fact explains a comparatively easier elimination of the $\sigma_{C1-F3}$ bond in compound 1 compared to the other compounds. The calculated data reveal that the polarization of the $C_1-F_3$ bond in the sense $C_1^{\delta+}-F_3^{\delta-}$ is the determining factor in the elimination reaction of the studied compounds.

**Keywords:** Elimination processes, 2,2-Difluoroethylsilane, Rate constants, Unimolecular reaction, Reaction mechanisms, NBO.

### 1. Introduction

The pyrolysis of fluoroalkylsilicon compounds $[\overset{\gamma}{\text{C}}-\overset{\beta}{\text{C}}-\overset{\alpha}{\text{C}}-\text{Si}]$ depends on the fluorine position relative to the silicon atom ($\alpha$-, $\beta$- or $\gamma$-position) [1]. The presence of a fluorine atom on both $\alpha$- and $\beta$-carbon relative to a silicon atom confirms the two individual mechanisms proposed for the $\alpha$-[2,3], and $\beta$-[1,4-6]-substituted compounds, both of which processes yield olefins. It is well-proven fluorine atom at the $\beta$-position of organosilicon compounds can decompose through unimolecular gas reaction and proceed *via* a four-center cyclic transition state (see Scheme 1) [7-11].

$$
\mathrm{CX-CH_2-Si} \longrightarrow \begin{array}{c}
\mathrm{C=CH_2} \\
\mathrm{\boxed{X-Si}}
\end{array} \longrightarrow \mathrm{C=CH_2 + XSi}
$$

Scheme 1

Further understanding factors that influence the studied reactions can be achieved by the study of the effects of different substituents on the silicon atom as well as in the side-chain silicon substituents. Kinetic rate constants reported by Haszeldine *et al.* [5,6] for the thermal decomposition of compound $\boldsymbol{1}$ into vinyl fluoride and silicon tetrafluoride have been followed by the study of decompositions of compound $\boldsymbol{2}$ in the gas phase. The decompositions are first-order and unaffected by the surface, the volume ratio of the reaction vessel or the addition of olefins at fairly low temperatures.

Haszeldine *et al.* studied the $\beta$-fluorine elimination of compounds $\mathrm{CHF_2CH_2SiF_nMe_{3-n}}$ ($n$=0–3) when $n$=2,3 and the obtained results show that the kinetics decreased when the fluorine atom was replaced by a methyl group on the silicon atom. They have shown that the energy barrier for the production of vinyl fluoride from 2,2-difluoroethyltrifluorosilane (compound $\boldsymbol{1}$) *via* the $\beta$-elimination process decomposes easily when heated, and that the replacement of a fluorine by a methyl group (electron-supplying) attached to the silicon atom is expected to reduce kinetics [8] (Scheme 2).

![](./images/812838135741284354_3.jpg)

Scheme 2

The study on the mechanism of the gas-phase $\beta$-elimination of 2,2-difluoroethylmethyldifluorosilane (2) into methyltrifluorosilane ($\text{MeSiF}_3$) and vinyl fluoride ($\text{CH}_2=\text{CHF}$) at an initial pressure of 20–186 mmHg and temperature ranges 182–246 °C is of the first-order rate constants and is also homogeneous [6]. The kinetics of 2,2-difluoroethylsilane and derivatives in a static system shows that the decomposition prevails yields vinyl fluoride and that the overall reaction is homogenous, first-order, and proceeds through a four-center transition-state structure.

![](./images/812838135741284354_4.jpg)

Scheme 3

An Arrhenius plot of the available experimental kinetics of the compounds $\textbf{1–2}$ over

the temperature range 151 to 246 °C is depicted in Figure 1. The kinetics of the thermal decomposition reactions 1–2 reveals positive temperature dependencies equivalent to energy barriers of (32.72±0.53) [5] and (32.54±0.36) kcal mol⁻¹, respectively [6]. The least-square fit to the Arrhenius expression of the experimental rate coefficient yields accordingly as follows [5,6]

$$
\log k_{1}\left(\mathrm{~s}^{-1}\right)=(12.27 \pm 0.27)-\frac{\left(32720 \pm 530 \mathrm{cal} \mathrm{mol}^{-1}\right)}{4.576 T} ;\left[P=10-180 \mathrm{mmHg} ; T=151-221{ }^{\circ} \mathrm{C}\right] \quad(1)
$$

$$
\log k_{2}\left(\mathrm{~s}^{-1}\right)=(11.32 \pm 0.16)-\frac{\left(32540 \pm 360 \mathrm{cal} \mathrm{mol}^{-1}\right)}{4.576 T} ;\left[P=20-186 \mathrm{mmHg} ; T=182-246{ }^{\circ} \mathrm{C}\right] \quad(2)
$$

Despite the fact that the kinetics of β-elimination of 2,2-difluoroethylsilane and its derivatives have been investigated in the gas phase, the molecular mechanism of pressure and the kinetics of the studied processes are unknown. The objective of this work is to provide rich insight into the β-elimination reactions shown in Scheme 2.

We shall first use at the M06-2x/aug-cc-pVTZ theoretical level [12,13], and then compare the calculated reaction energies as well as energy barriers with the high-level composite CBS-QB3 results. Furthermore, kinetics will be measured using transition state theory [14–20] at the high-pressure limit, and its fall-off behavior will be studied by means of statistical the Rice-Ramsperger-Kassel-Marcus (RRKM) theory [21–23] at lower pressures for unraveling the detailed mechanism by Haszeldine *et al.* [5,6] at available experimental over a temperature range from 151 to 246 °C. Finally, we will attempt to get a further insight into the studied pathways by means of exploring results calculated using bond orders, natural bond orbital (NBO) occupancies [24,25], and donor-acceptor interaction energies.

![](./images/812838135741284354_5.jpg)

Fig. 1. Arrhenius plot for kinetic rate constant of compounds 1 and 2.
Legend: (○) Haszeldine et al. [5]; (▲) Haszeldine et al. [6].

## 2. Computational details

All of the quantum chemistry calculations are performed with the Gaussian 09 suite of programs [26]. The geometrical structures of all the reactants, transition states and products were optimized at the M06-2x/aug-cc-pVTZ level of theory. The M06-2x energies are not accurate enough, so the electronic energies were further optimized at the CBS-QB3 level of theory that spin-unrestricted wave functions are used in order to eliminate the need for empirical corrections that are incorporated in standard CBS-QB3 to compensate for spin contamination [27].

The energies of the all studied stationary points were re-evaluated by means of the CBS-QB3 model. It includes low level calculations on large basis sets, medium basis sets for second-order Møller-Plesset (MP2) calculation, and small basis sets for the high level correlation corrections [28–30].

The five-step CBS-QB3 series of calculations start with a geometry optimization at the B3LYP/6-311G(2d,d,p) level of theory, followed by a frequency calculation to obtain zero-point vibrational energies, thermal corrections, and entropic information [31]. The CBS-QB3 model chemistry is reliable, offers small improvements in the mean absolute and root-mean-square errors, and suffers little penalty in speed [32]. The CBS-QB3 method

amounts to an extrapolation of energies to the CCSD(T) level in conjunction with a complete basis set. Based on the idea that the truncation of the basis set is an important source of error in molecular electronic structure calculations, the CBS-QB3 method was developed [33–36]. It is a benchmark approach to calibrating the accuracy of DFT methods [37].

Structures with the lowest energies were optimized with the geometry optimization method using an energy-represented direct inversion in the iterative subspace (GEDIIS) algorithm, which was subsequently used for searching the transition state geometries of the decomposition pathways at the M06-2x/aug-cc-pVTZ level [38,39]. Intrinsic reaction coordinate (IRC) analysis was performed in both the forward and reverse directions at the CBS-QB3 level of theory using the Hessian-based predictor corrector (HPC) integrator algorithm to check the energy profiles connecting the identified transition structure to the associated energy minima [40–42].

Unimolecular reaction kinetics of compounds 1–4 were estimated in the high-pressure limit with the KiSThelP program [43] according to the transition state theory (TST). With this approach, kinetic studies on the decomposition reactions are given by [44,45]:

$$
k_{\mathrm{TST}}(T)=\kappa(T) \times \frac{\sigma k_{\mathrm{B}} T}{h} \times \frac{Q_{T S}^{\dagger}}{Q_{\mathrm{R}}} \times \exp \left(-E^{\dagger} / k_{\mathrm{B}} T\right) \tag{3}
$$

where $h$ and $k_{\mathrm{B}}$ are the Planck's and Boltzmann's constants, $\sigma$ denotes the reaction path degeneracy, $T$ is the absolute temperature, $\kappa(T)$ represent the Wigner's tunneling factor [46], and $E^{\dagger}$ is defined as the difference in activation energy between zero-point vibrational frequencies between reactant and transition state. In the above equation, $Q^{\dagger}$ and $Q_{\mathrm{R}}$ represent total partition functions per unit volume of the transition state and reactant, respectively. Wigner tunneling correction is expressed as

$$
\kappa_{\text {Wigner }}(T)=1+\frac{1}{24}\left(\frac{h \operatorname{Im}\left(v_{i}\right)}{k_{B} T}\right)^{2} \tag{4}
$$

where $\operatorname{Im}(v_{i})$ denotes the imaginary frequency in the transition state. Because of the simplicity of TST, the upper limit of the kinetics is given, enabling the provision of reliable high-pressure limiting rate constants [23,47]. In proportion to the experiments [5,6], rate constants are calculated at a P=1 bar and over the temperature range 151–246 °C by means of TST.

The atmospheric pressures are measured to be enough in order to reliably calculate kinetics rate constant by means of transition state theory. The fall-off behavior of

canonical kinetic rate constants $k(T)$ from the TST limit ($P$$\to\infty$) towards the low-pressure limit ($P$$\to0$) was also calculated using the RRKM theory [21–23]. The microcanonical kinetics $k(E)$ are evaluated according to unimolecular RRKM theory [21]:

$$
k(E)=\frac{\sigma N^{\dagger}(E)}{h \rho(E)}
\tag{5}
$$

$\rho(E)$ is the density of states of the reactants and $N^{\dagger}(E)$ is the total number of states at the transition state [48]. The $k(T)$ is defined by [49]

$$
k(T)=\frac{1}{Q(T)} \int k(E) N(E) \exp (-\beta E) d E
\tag{6}
$$

where $Q(T)$ denote the internal partition functions for the reactants.

All RRKM and TST kinetics are calculated using the KiSThelP package [43].
Collisional stabilization rate constants were calculated using the Lennard-Jones (LJ) collision rate theory [50]. The strong collision approximation is used assuming that every collision deactivates with $\omega$=$\beta_{c}Z_{LJ}$[M] being the effective collision frequency where [M] denotes the total gas concentration, $\beta_{c}$ is the collisional efficiency, and $Z_{LJ}$ represents the LJ collision frequency which are calculated using the LJ parameters for reactants $\textbf{1–4}$ [51] and argon as diluent gas [52] are given in Table 1.

<table>
<caption>Table 1: Potential parameters of Lennard-Jones</caption>
<thead>
<tr>
<th rowspan="2">Species</th>
<th colspan="2">LJ potential parameters</th>
</tr>
<tr>
<th>$\sigma$($\mathring{\text{A}}$)</th>
<th>$\varepsilon/k_{\text{B}}$(K)</th>
</tr>
</thead>
<tbody>
<tr>
<td>2,2-Difluoroethyltrifluorosilane (1)</td>
<td>4.8</td>
<td>288.3</td>
</tr>
<tr>
<td>2,2-Difluoroethylmethyldifluorosilane (2)</td>
<td>4.8</td>
<td>312.4</td>
</tr>
<tr>
<td>2,2-Difluoroethyldimethylfluorosilane (3)</td>
<td>4.8</td>
<td>337.0</td>
</tr>
<tr>
<td>2,2-Difluoroethyltrimethylsilane (4)</td>
<td>4.8</td>
<td>361.9</td>
</tr>
<tr>
<td>Ar (Diluent gas)</td>
<td>3.465</td>
<td>113.5</td>
</tr>
</tbody>
</table>

## 3. Results and discussion

### 3.1. Energetic and thermodynamic parameters

The reaction energies ($\Delta H$ and $\Delta G$) as well as activation energies ($\Delta G^{\dagger}$ and $\Delta H^{\dagger}$) at standard temperature and pressure ($T = 298$ K, $P$ =1 atm) for the decomposition of 2,2-difluoroethyltrifluorosilane (1), 2,2-difluoroethylmethyldifluorosilane (2), 2,2-difluoroethyldimethylfluorosilane (3), and 2,2-difluoroethyltrimethylsilane (4) are

presented in Tables 2 and 3. In line with experiments [5,6], the CBS-QB3 results indicate that the $\beta$-elimination of compounds $\textbf{1-4}$ is an exothermic process ($\Delta H \approx -12.66, -17.05$, $-15.95$ and $-13.78$ kcal mol$^{-1}$, respectively). At ambient temperature and pressure, all studied reactions are exoergic and spontaneous ($\Delta G < 0$). Upon inspecting the energy profiles are shown in Table 2, it appears that the formation of methyltrifluorosilane (MeSiF$_3$) is thermodynamically most favored pathway since the process $\textbf{2}$ is strongly exothermic ($\Delta H \approx -17.05$ kcal mol$^{-1}$) and exoergic ($\Delta G \approx -28.73$ kcal mol$^{-1}$).

Thermal decomposition of the studied compounds corresponds to the homolytic, four-center, and concerted process in the gas phase. A replacement of a fluorine attached to the silicon atom by the methyl group is expected to decrease the barrier height, and thus, reaction kinetics will be increased [53,54].

![](./images/812838135741284354_6.jpg)

Fig. 2. Potential energy profile of the unimolecular decomposition processes $\textbf{1-4}$.

It is worth mentioning that the activation barrier ($\Delta E_{0K}^{\dagger}$) for reaction $\textbf{1}$ is lower by nearly 5.07-9.76 kcal mol$^{-1}$ than the activation energy for reaction $\textbf{4}$, which is consistent

with the replacement of the 3 methyl groups attached to silicon by fluorine atoms. When $\Delta G^{\dagger}$ related to the studied reactions are measured, you can find similar observations: in spite of slightly unfavorable entropy effects, Gibb's free energy for the 2,2- difluoroethyltrifluorosilane (1) species (~34.36 kcal mol⁻¹) is less than those for pathways 2–4 (38.96, 41.64, and 43.48 kcal mol⁻¹, respectively). The difference between the activation energy $\Delta E^{\dagger}$, and activation entropy $\Delta S^{\dagger}$ for the studied pathways indicates that from a chemical-kinetic viewpoint, is the most favorable reaction channel is β-elimination of compound 1 into the vinyl fluoride and silicon tetrafluoride species (as products P1), while from a thermodynamic viewpoint, the most favorable process is the formation of CH₂=CHF and MeSiF₃ species (as products P2). Energy profile for the β-elimination processes 1–4 is depicted in Figure 2.

Indeed, the increase in the kinetics of the β-elimination process is calculated not only by the energy barrier but also by the activation entropy ($\Delta S^{\dagger}$), which is required to reach the transition state structure [8,55]. The β-elimination of compound 1 is considered to be a unimolecular reaction. The pre-exponential factor A for this process is larger than that found for a unimolecular reaction in which the transition state is the ring of four heavy atoms [log A=12.27 vs. log A=9–11.5 sec⁻¹) [56]. Hence, the activation entropy is less negative than the normal value for processes of this type ($\Delta S^{\dagger} = -5.4$ vs. –9 to –20 cal. mol⁻¹ deg⁻¹). The pre-exponential factor A is higher than usual when the rotational entropy on the formation of the transition state structure is less than normal. However, the experimental A factor for the β-elimination of compound 2 is nearly 8 times smaller than compound 1, and is more consistent with the values generally obtained for molecular decompositions in which the TS structure is a ring of four heavy atoms [57–59].

The Berny algorithm was used to locate the transition states. TST calculations for the β-elimination processes 1–4 were performed in conjunction with the IRC path at the B3LYP/6-311G(2d,d,p) level which energy profiles along the IRC for the pathways 1–4 are presented in Figures S1a–S1d in the Supplementary material. We used a step size of 0.1 amu¹/²-Bohr and 60 steps were run in the both forward and reverse directions along the reaction path. IRC calculations revealed that the transition state connects the reactant and corresponding products, so the CBS-QB3 results should be reasonably reliable, and the rate constants calculation will be based on the CBS-QB3 energies, M06-2x geometries and vibrational frequencies unless otherwise specified.

Table 2. Reaction energy parameters (energies, enthalpies and Gibb's free energies) (in kcal mol⁻¹) of the pathways 1-4.

<table>
  <thead>
    <tr>
      <th rowspan="2">Reaction</th>
      <th>Parameter</th>
      <th colspan="3">M06-2x/aug-cc-pVTZ</th>
      <th colspan="3">CBS-QB3</th>
    </tr>
    <tr>
      <th></th>
      <th>$\Delta E_{0\text{K}}$</th>
      <th>$\Delta H^{\bullet}_{298\text{K}}$</th>
      <th>$\Delta G^{\bullet}_{298\text{K}}$</th>
      <th>$\Delta E_{0\text{K}}$</th>
      <th>$\Delta H^{\bullet}_{298\text{K}}$</th>
      <th>$\Delta G^{\bullet}_{298\text{K}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2,2-Difluoroethyltrifluorosilane $\rightarrow$ CH₂=CHF + SiF₄</td>
      <td></td>
      <td>−10.433</td>
      <td>−10.051</td>
      <td>−19.964</td>
      <td>−13.023</td>
      <td>−12.659</td>
      <td>−22.275</td>
    </tr>
    <tr>
      <td>2,2-Difluoroethylmethyldifluorosilane $\rightarrow$ CH₂=CHF + MeSiF₃</td>
      <td></td>
      <td>−15.511</td>
      <td>−15.093</td>
      <td>−26.723</td>
      <td>−17.476</td>
      <td>−17.047</td>
      <td>−28.726</td>
    </tr>
    <tr>
      <td>2,2-Difluoroethyldimethylfluorosilane $\rightarrow$ CH₂=CHF + Me₂SiF₂</td>
      <td></td>
      <td>−14.342</td>
      <td>−13.886</td>
      <td>−25.809</td>
      <td>−16.485</td>
      <td>−15.954</td>
      <td>−28.105</td>
    </tr>
    <tr>
      <td>2,2-Difluoroethyltrimethylsilane $\rightarrow$ CH₂=CHF + Me₃SiF</td>
      <td></td>
      <td>−12.871</td>
      <td>−12.215</td>
      <td>−24.227</td>
      <td>−14.342</td>
      <td>−13.782</td>
      <td>−24.898</td>
    </tr>
  </tbody>
</table>

Table 3. Activation energy parameters (in kcal mol⁻¹) and activation entropies (in cal mol⁻¹ K⁻¹) of the pathways 1-4 ($P=1$ atm)

<table>
  <thead>
    <tr>
      <th rowspan="2">Reaction</th>
      <th>Method</th>
      <th colspan="3">M06-2x/aug-cc-pVTZ</th>
      <th colspan="4">CBS-QB3</th>
      <th>Experiment ($\Delta E_{0\text{K}}^{\dagger}$)</th>
    </tr>
    <tr>
      <th></th>
      <th>$\Delta E_{0\text{K}}^{\dagger}$</th>
      <th>$\Delta H^{\bullet}_{298\text{K}}^{\dagger}$</th>
      <th>$\Delta G^{\bullet}_{298\text{K}}^{\dagger}$</th>
      <th>$\Delta E_{0\text{K}}^{\dagger}$</th>
      <th>$\Delta H^{\bullet}_{298\text{K}}^{\dagger}$</th>
      <th>$\Delta G^{\bullet}_{298\text{K}}^{\dagger}$</th>
      <th>$\Delta S^{\bullet}_{298\text{K}}^{\dagger}$</th>
      <th>(kcal mol⁻¹)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2,2-Difluoroethyltrifluorosilane $\rightarrow$ TS1</td>
      <td></td>
      <td>30.897</td>
      <td>30.521</td>
      <td>32.085</td>
      <td>33.051</td>
      <td>32.771</td>
      <td>34.357</td>
      <td>−5.317</td>
      <td>$(32.72\pm0.53)^{a}$</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>$(-5.4)^{a}$</td>
      <td></td>
    </tr>
    <tr>
      <td>2,2-Difluoroethylmethyldifluorosilane $\rightarrow$ TS2</td>
      <td></td>
      <td>36.055</td>
      <td>35.641</td>
      <td>37.144</td>
      <td>38.117</td>
      <td>37.861</td>
      <td>38.957</td>
      <td>−3.676</td>
      <td>$(32.54\pm0.36)^{b}$</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>$(-9.7)^{b}$</td>
      <td></td>
    </tr>
    <tr>
      <td>2,2-Difluoroethyldimethylfluorosilane $\rightarrow$ TS3</td>
      <td></td>
      <td>39.429</td>
      <td>39.078</td>
      <td>40.105</td>
      <td>41.317</td>
      <td>41.202</td>
      <td>41.639</td>
      <td>−1.469</td>
      <td></td>
    </tr>
    <tr>
      <td>2,2-Difluoroethyltrimethylsilane $\rightarrow$ TS4</td>
      <td></td>
      <td>42.628</td>
      <td>42.454</td>
      <td>42.952</td>
      <td>42.808</td>
      <td>42.756</td>
      <td>43.476</td>
      <td>−2.423</td>
      <td></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="10">- Experimental values: a) Ref [5]; b) Ref [6].</td>
    </tr>
  </tfoot>
</table>

### 3.2. Transition state and mechanism

The geometrical characteristics for all stationary points at the CBS-QB3 theoretical level along the studied pathways are listed in Table 4. A molecular structure of the studied compounds with the atom-numbering is shown in Scheme 3. The transition state structures for the thermal decomposition of 2,2-difluoroethylsilanes and derivatives is the 4-membered ring structure. The most significant change is observed for the $C_1$–$F_3$ bond length, which is elongated by ~0.54 to ~0.61 Å indicating this bond breaking in the TSs. Similarly, the $C_2$–$Si_4$ bond distances only increase by ~0.18 to ~0.29 Å which implies the bond breaking in the TSs. The $F_3$–$Si_4$ bonds shrink by ~1.27 to ~1.42 Å in the TSs, compared with the reactant structures. Inspection of the $C_1$–$C_2$ bonds show changes from a single-bond to a double-bond character, with bond distances decrease from ~1.51 to ~1.40 Å in the TSs.

As can be seen in Table 4, dihedral angles for the pathways **1–4** in TSs are $51.47^\circ$ (−51.43 to $11.154^\circ$), $50.74^\circ$ (−49.98 to $0.76^\circ$), $68.31^\circ$ (−67.70 to $0.61^\circ$), and $59.69^\circ$ (−55.32 to $4.37^\circ$), respectively (Table 4). These results show that the TSs for the β-elimination of these compounds are nonplanar. Imaginary frequencies characterized for the TSs of 2,2-difluoroethyltrifluorosilane (**1**), 2,2-difluoroethylmethyldifluorosilane (**2**), 2,2-difluoroethyldimethylfluorosilane (**3**), and 2,2-difluoroethyltrimethylsilane (**4**) amount to $339.5i$, $406.9i$, $427.3i$ and $432.4i$ cm⁻¹, respectively at the CBS-QB3 level of theory.

Table 4. Optimized structures and partial structural parameters for stationary points along the pathways **1–4** at the CBS-QB3 approach method.∗

<table>
  <thead>
    <tr>
      <th rowspan="2">Bond</th>
      <th>Species</th>
      <th colspan="3">Pathway 1</th>
      <th colspan="3">Pathway 2</th>
      <th colspan="3">Pathway 3</th>
      <th colspan="3">Pathway 4</th>
    </tr>
    <tr>
      <th></th>
      <th>R</th>
      <th>TS</th>
      <th>P</th>
      <th>R</th>
      <th>TS</th>
      <th>P</th>
      <th>R</th>
      <th>TS</th>
      <th>P</th>
      <th>R</th>
      <th>TS</th>
      <th>P</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Bond lengths (Å)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">$r$ ($C_1$–$F_3$)</td>
      <td>1.373</td>
      <td>1.981</td>
      <td>–</td>
      <td>1.373</td>
      <td>1.924</td>
      <td>–</td>
      <td>1.378</td>
      <td>1.921</td>
      <td>–</td>
      <td>1.379</td>
      <td>1.939</td>
      <td>–</td>
    </tr>
    <tr>
      <td colspan="2">$r$ ($C_1$–$C_2$)</td>
      <td>1.514</td>
      <td>1.401</td>
      <td>1.320</td>
      <td>1.513</td>
      <td>1.399</td>
      <td>1.320</td>
      <td>1.508</td>
      <td>1.393</td>
      <td>1.320</td>
      <td>1.506</td>
      <td>1.386</td>
      <td>1.320</td>
    </tr>
    <tr>
      <td colspan="2">$r$ ($C_2$–$Si_4$)</td>
      <td>1.858</td>
      <td>2.036</td>
      <td>–</td>
      <td>1.878</td>
      <td>2.094</td>
      <td>–</td>
      <td>1.898</td>
      <td>2.148</td>
      <td>–</td>
      <td>1.914</td>
      <td>2.199</td>
      <td>–</td>
    </tr>
    <tr>
      <td colspan="2">$d$ ($F_3$–$Si_4$)</td>
      <td>3.083</td>
      <td>1.793</td>
      <td>1.569</td>
      <td>3.112</td>
      <td>1.840</td>
      <td>1.607</td>
      <td>3.302</td>
      <td>1.886</td>
      <td>1.588</td>
      <td>3.225</td>
      <td>1.936</td>
      <td>1.629</td>
    </tr>
    <tr>
      <td colspan="2">Dihedral angles ($^\circ$)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">$\varphi$($F_3$–$C_1$–$C_2$–$Si_4$)</td>
      <td>–51.43</td>
      <td>0.04</td>
      <td>–</td>
      <td>–49.98</td>
      <td>0.76</td>
      <td>–</td>
      <td>–67.70</td>
      <td>0.61</td>
      <td>–</td>
      <td>–55.32</td>
      <td>4.37</td>
      <td>–</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="14">∗Bond lengths are in angstrom (Å) unit and angles in degrees ($^\circ$).</td>
    </tr>
  </tfoot>
</table>

Based on the Hammond's postulate, TS structure of the pathway most closely resembles the stable species (**R** or **P**) that lies closest to it in energy [60], and the positions of the TS structure are intermediate between the **R** and **P** structures along the reaction coordinate. The $n_T$ parameter is defined by [61]:

$$
n_{\mathrm{T}}=\frac{1}{2-\left(\Delta G^{\circ} / \Delta G^{\ddagger}\right)}
\tag{7}
$$

$n_{\text{T}}$ values for the studied reactions $\mathbf{1 - 4}$ are 0.378, 0.365, 0.374, and 0.389, respectively which implies that the TS structures involved in the formation of the products $\mathbf{P1-P4}$ are more similar to the reactants than to its products (Table 4), and TSs are referred to as early (reactant-like). The similarity between the $\mathbf{TS}$ and $\mathbf{R}$ structures increase with respect to the reactions in the following order: $\mathbf{R2} > \mathbf{R3} > \mathbf{R1} > \mathbf{R4}$.

### 3.3. Bond Order Analysis

The further balanced measure of bond-breaking or bond-forming along the process is provided using bond order (BO) concepts [24,62,63]. Wiberg bond indices ($B_i$) [64] are calculated based on the natural bond orbital analysis [65]. There are several breaking/forming bonds occurs along with chemical reactions $\mathbf{1 - 4}$ that can be checked by synchronicity ($S_y$) index [66] as follows:

$$
S_{y}=1-\frac{\left[\sum_{i=1}^{n} \frac{\left|\delta B_{i}-\delta B_{a v}\right|}{\delta B_{a v}}\right]}{2 n-2}
\tag{8}
$$

where $\delta B_{av}$ is the average bond index variation, $\delta B_i$ denotes the relative variation of the bond index for bond $i$ at the TS structure, $\% EV$ is percentage evolution through the reaction coordinate, and $n$ represents the number of bonds which are directly involved in the process. The magnitude value for the synchronicity parameter varies between 0 and 1 [67].

Bond indices were determined for the $\mathrm{C_{1}-C_{2}}$, $\mathrm{C_{1}-F_{3}}$, $\mathrm{C_{2}-Si_{4}}$, and $\mathrm{F_{3}-Si_{4}}$ bonds which are involved in the $\beta$-elimination process, whereas the rest of the other bonds remain practically unchanged (see Scheme 3 and Table 5). The studied Wiberg bond indices $B_i$ for the stationary points $(\mathbf{R, TS, P})$ enable us to find the TS position between reactant and product as well as to study the reaction progress.

Chemical reactions $\mathbf{1 - 4}$ lead to the cleavage of $\mathrm{C_{1}-F_{3}}$ bond to yield the related products located at $13.02$–$17.48$ kcal mol⁻¹ below the studied compounds $\mathbf{1 - 4}$ at the CBS-QB3 theoretical level. Transition states (TS1–TS4) result are from a simple elongation of the breaking $\mathrm{C_{1}-F_{3}}$ and $\mathrm{C_{2}-Si_{4}}$ bond distances and the simultaneous shrinkage of the $\mathrm{F_{3}-Si_{4}}$ distance because of forming a carbon-carbon double bond. The $\mathrm{C_{1}-F_{3}}$ and $\mathrm{C_{2}-Si_{4}}$ bond are elongated by $1.391$–$1.404$ Å and $2.237$ Å, respectively (Table 4), and the $\mathrm{F_{3}-Si_{4}}$

bond formed is longer than the equilibrium bond lengths in reactants **1–4** species
(**R1–R4**). Moreover, for the studied reactions, Wiberg bond indices reveal more progress
in $C_1$–$F_3$ bond breaking ($\%EV = 69.41$–$73.62$ %), while the changes in $C_2$–$Si_4$ and $C_1$–$C_2$
bonds are intermediate ($\%EV = 37.32$–$46.66$ % and $\%EV = 35.35$–$41.84$ %, respectively).
On the other hand, the $C_1$–$C_2$ bond changes from single- to double-bond. Less progress is
observed in $C_1$–$C_2$ double bond formation ($\%EV = 35.35$–$41.84$ %) in the studied
compounds. The synchronicity values of the reactions **1–4** are 0.814, 0.826, 0.849 and
0.889, respectively, revealing that the studied reactions can be described as both concerted
and slightly asynchronous.

Table 5. Bond order analysis of all stationary points in the studied pathways at the CBS-
QB3 theoretical level.

<table>
  <thead>
    <tr>
      <th colspan="2">Bond<br>Reaction</th>
      <th>$C_1$–$C_2$</th>
      <th>$C_1$–$F_3$</th>
      <th>$C_2$–$Si_4$</th>
      <th>$F_3$–$Si_4$</th>
      <th>$\delta B_{av}$</th>
      <th>$S_y$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Pathway 1<br>$[\text{R1} \rightarrow \text{CH}_2\text{=CHF} + \text{SiF}_4]$</td>
      <td>$B_i(\text{R})$</td>
      <td>1.0228</td>
      <td>0.8522</td>
      <td>0.7452</td>
      <td>0.0102</td>
      <td>0.5043</td>
      <td>0.8136</td>
    </tr>
    <tr>
      <td>$B_i(\text{TS})$</td>
      <td>1.3534</td>
      <td>0.2248</td>
      <td>0.4671</td>
      <td>0.3879</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$B_i(\text{P})$</td>
      <td>1.9580</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.6915</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\%EV$</td>
      <td>35.351</td>
      <td>73.621</td>
      <td>37.319</td>
      <td>55.438</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">Pathway 2<br>$[\text{R2} \rightarrow \text{CH}_2\text{=CHF} + \text{MeSiF}_3]$</td>
      <td>$B_i(\text{R})$</td>
      <td>1.0269</td>
      <td>0.8518</td>
      <td>0.7425</td>
      <td>0.0105</td>
      <td>0.5152</td>
      <td>0.8262</td>
    </tr>
    <tr>
      <td>$B_i(\text{TS})$</td>
      <td>1.3612</td>
      <td>0.2577</td>
      <td>0.4435</td>
      <td>0.3691</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$B_i(\text{P})$</td>
      <td>1.9580</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.6066</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\%EV$</td>
      <td>35.904</td>
      <td>69.746</td>
      <td>40.269</td>
      <td>60.158</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">Pathway 3<br>$[\text{R3} \rightarrow \text{CH}_2\text{=CHF} + \text{Me}_2\text{SiF}_2]$</td>
      <td>$B_i(\text{R})$</td>
      <td>1.0346</td>
      <td>0.8427</td>
      <td>0.7510</td>
      <td>0.0033</td>
      <td>0.5286</td>
      <td>0.8490</td>
    </tr>
    <tr>
      <td>$B_i(\text{TS})$</td>
      <td>1.3891</td>
      <td>0.2578</td>
      <td>0.4252</td>
      <td>0.3396</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$B_i(\text{P})$</td>
      <td>1.9580</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.5914</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\%EV$</td>
      <td>38.391</td>
      <td>69.408</td>
      <td>43.382</td>
      <td>60.258</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">Pathway 4<br>$[\text{R4} \rightarrow \text{CH}_2\text{=CHF} + \text{Me}_3\text{SiF}]$</td>
      <td>$B_i(\text{R})$</td>
      <td>1.0378</td>
      <td>0.8397</td>
      <td>0.7705</td>
      <td>0.0065</td>
      <td>0.5289</td>
      <td>0.8894</td>
    </tr>
    <tr>
      <td>$B_i(\text{TS})$</td>
      <td>1.4228</td>
      <td>0.2482</td>
      <td>0.4110</td>
      <td>0.3062</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$B_i(\text{P})$</td>
      <td>1.9580</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.5761</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\%EV$</td>
      <td>41.839</td>
      <td>70.442</td>
      <td>46.658</td>
      <td>52.616</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

There is also a difference in the distribution of electrons at the silicon atom between
compound **1** ($\text{F–C}_2\text{H}_3\text{F–SiF}_3$) and compound **4** ($\text{F–C}_2\text{H}_3\text{F–SiMe}_3$) resulting from the
replacement of a $\text{Si–C}$ bond by a $\text{Si–F}$ bond [10]. Variations in electron distribution
during decomposition reactions **1–4** can be studied using NBO charges [68]. NBO charge
analysis demonstrates that the $C_1$–$F_3$ bond is polarized in the studied compounds in this
work ($C_1$ charge is 0.6517 to 0.6550 and $F_3$ is $-0.3795$ to $-0.3912$, charge separation $\Delta q =$
$1.0312$–$1.0462$) in the sense $C_1^{\delta +}$–$F_3^{\delta -}$. As the reaction proceeds from the reactants to

transition states, relative changes occur in partial charges as follows: an increase in negative charge $\delta^{-}$ in fluorine $F_{3}$ (-0.3795 to -0.3912 in the studied reactants compared to -0.5777 to -0.6043 in TS), and an increase in positive charges $\delta^{+}$ in carbon $C_{1}$ (0.6517-0.6550 in the studied reactants compared to 0.5673-0.6183 in TS) are presented in Table 6.

Table 6. NBO charges (in e) for reactants and transition states of the $\beta$-elimination processes 1-4 [results obtained using the CBS-QB3 approach].

<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Atom<br>C₁</th>
      <th>C₂</th>
      <th>F₃</th>
      <th>Si₄</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>R1</td>
      <td>0.65167</td>
      <td>-0.99321</td>
      <td>-0.37954</td>
      <td>2.32617</td>
    </tr>
    <tr>
      <td>TS1</td>
      <td>0.61826</td>
      <td>-0.90161</td>
      <td>-0.59470</td>
      <td>2.32645</td>
    </tr>
    <tr>
      <td>R2</td>
      <td>0.65450</td>
      <td>-0.96682</td>
      <td>-0.37991</td>
      <td>2.13171</td>
    </tr>
    <tr>
      <td>TS2</td>
      <td>0.60106</td>
      <td>-0.88048</td>
      <td>-0.57771</td>
      <td>2.16233</td>
    </tr>
    <tr>
      <td>R3</td>
      <td>0.65374</td>
      <td>-0.93504</td>
      <td>-0.38962</td>
      <td>1.89808</td>
    </tr>
    <tr>
      <td>TS3</td>
      <td>0.58524</td>
      <td>-0.84982</td>
      <td>-0.58610</td>
      <td>1.97677</td>
    </tr>
    <tr>
      <td>R4</td>
      <td>0.65502</td>
      <td>-0.89605</td>
      <td>-0.39118</td>
      <td>1.60377</td>
    </tr>
    <tr>
      <td>TS4</td>
      <td>0.56732</td>
      <td>-0.81428</td>
      <td>-0.60432</td>
      <td>1.76359</td>
    </tr>
  </tbody>
</table>

### 3.4. Natural Bond Orbital (NBO) Analysis

NBO analysis as a way of quantifying how resonance structure contributions to molecular systems are initially established. NBO analysis is carried out by examining all possible interactions between "filled" (donor) Lewis-type NBOs and "empty" (acceptor) non-Lewis NBOs, and estimating their energetic importance by 2nd-order perturbation theory [24,65]. Delocalization energy $(E_{2})$ related to $i \to j$ delocalization for each donor NBO($i$) and acceptor NBO($j$) is given by [65]:

$$
E_{2}=\Delta E_{i j}=q_{i}\left[\frac{F_{(i, j)}^{2}}{\varepsilon_{i}-\varepsilon_{j}}\right] \tag{9}
$$

where $F_{(i,j)}$ is the off-diagonal NBO Fock matrix element, $q_{i}$ is the orbital occupancy, and $\varepsilon_{i}$ and $\varepsilon_{j}$ are diagonal elements (orbital energies).

According to the optimized ground-state geometries using the B3LYP/6-311G(2d,d,p) theoretical method and electronic structure characteristics of the compounds 1-4, NBO analysis shows that, by increasing the number of fluorine atom attached to the silicon in the compounds 1-4, the occupancies of $\sigma_{\mathrm{C} 1-\mathrm{F} 3}$ bonds decrease as $\mathbf{4}<\mathbf{3}<\mathbf{2}<\mathbf{1}$, whereas the occupancies of $\sigma_{\mathrm{C} 1-\mathrm{F} 3}^{*}$ bonds increase in the opposite order $(\mathbf{4}>\mathbf{3}>\mathbf{2}>\mathbf{1})$ (Table 7). Furthermore, these results can reasonably explain an increase in the barrier heights $(\Delta E_{\mathrm{o}})$

of the $\beta$-elimination of 2,2-difluoroethyltrifluorosilane (compound $\boldsymbol{1}$) to 2,2-
difluoroethyltrimethylsilane (compound $\boldsymbol{4}$). This result revealed the easier breaking of
$\mathrm{C}_{1}-\mathrm{F}_{3}$ bond in compound $\boldsymbol{1}$ compared to other compounds.

Table 7. NBO occupancies and delocalization energies $(E_{2})$, based on the CBS-QB3
theoretical method calculated geometries, for $\sigma_{\mathrm{C} 1-\mathrm{F} 3}$ bonding and $\sigma^{*}_{\mathrm{C} 1-\mathrm{F} 3}$ antibonding
orbitals occupancies, and HOMO-LUMO gaps for compounds $\boldsymbol{1 - 4}$.

<table>
<thead>
<tr>
<th><span class="tabcolend"></span>Species<br>Parameters</th>
<th colspan="4">B3LYP/6-311G(2d,d,p)</th>
</tr>
<tr>
<th></th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><i>Occupancies</i></td>
</tr>
<tr>
<td>$\sigma_{\mathrm{C}1-\mathrm{F}3}$</td>
<td>1.99549</td>
<td>1.99544</td>
<td>1.99540</td>
<td>1.99537</td>
</tr>
<tr>
<td>$\sigma^{*}_{\mathrm{C}1-\mathrm{F}3}$</td>
<td>0.06608</td>
<td>0.06622</td>
<td>0.06685</td>
<td>0.06819</td>
</tr>
<tr>
<td colspan="5"><i>HOMO,LUMO energies (a.u.)</i></td>
</tr>
<tr>
<td>HOMO</td>
<td>−0.36214</td>
<td>−0.32681</td>
<td>−0.31366</td>
<td>−0.30320</td>
</tr>
<tr>
<td>LUMO</td>
<td>0.01450</td>
<td>0.02019</td>
<td>0.02724</td>
<td>0.02741</td>
</tr>
<tr>
<td>HOMO-LUMO gap (eV)</td>
<td>10.249</td>
<td>9.442</td>
<td>9.276</td>
<td>8.996</td>
</tr>
</tbody>
</table>

Further, by increasing the energy barrier from 2,2-difluoroethyltrifluorosilane $(\boldsymbol{1})$ to 2,2-
difluoroethyltrimethylsilane $(\boldsymbol{4})$ and replacing a $\mathrm{Si-C}$ bond with a $\mathrm{Si-F}$ bond in
compounds $\boldsymbol{1 - 4}$, the HOMO-LUMO energy gaps increase. The results show that the gap
values for compounds $\boldsymbol{1 - 4}$ are 10.25, 9.44, 9.28, and 8.99 eV, respectively.

### 3.5. Kinetic parameters
Unimolecular kinetic rate constants for the $\beta$-elimination processes of compounds $\boldsymbol{1 - 4}$
are supplied in Table 8 at the experimentally considered temperatures [5,6], considering a
pressure of 1 bar. These rate constants are the results of TST and RRKM calculations
performed upon the CBS-QB3 energy barriers and densities of states. Further RRKM data
achieved at higher and lower pressures are provided for the same temperatures in Tables
S1a–S1e of the Supplementary material. Theoretical values obtained at a pressure of 1 bar
do not differ by more than one order of magnitude from the available experimental data
[5,6].

Kinetics of the formation of $\mathrm{SiF}_{4}$ molecule is higher than that found for the $\mathrm{MeSiF}_{3}$,
$\mathrm{Me}_{2}\mathrm{SiF}_{2}$, and $\mathrm{Me}_{3}\mathrm{SiF}$ species which is in proportion to a reduction of the energy barrier by
5.07, 8.27, and 9.76 kcal mol⁻¹, respectively. The calculated TST data reveal that rate
coefficients for the 2,2-difluoroethyltrifluorosilane $\rightarrow \mathrm{CH}_{2=}\mathrm{CHF}+\mathrm{SiF}_{4}$ are more than the

obtained kinetics for the other reactions (Table 8). Because of the positive barrier heights involved, the kinetics increased regularly with increasing temperature.

Arrhenius plot of the calculated rate coefficients for chemical reactions **1–4** which measured at the experimental temperatures using RRKM theory is depicted in Figure 4. As can be seen in Figure 4, the production of the $\mathrm{CH_2=CHF+SiF_4 (P1)}$ species is most effective reaction at a pressure of 1 bar and over the temperature range 151–246 °C. Further RRKM data calculated at lower and higher pressures (from $10^{-12}$ to $10^2$ bars) are provided for the same temperatures in Tables S1$a$–S1$e$ of the Supplementary material. In line with larger activation energy barriers, the formation of the $\mathrm{MeSiF_3}$, $\mathrm{Me_2SiF_2}$, and $\mathrm{Me_3SiF}$ species is characterized by lower kinetics at an order of magnitude of at least 3–4 at the studied temperatures compared with the formation of the $\mathrm{CH_2=CHF+SiF_4}$ species (Pathway **1**).

Consistent with the calculated energy profile, the CBS-QB3 method and RRKM kinetic rate coefficients indicate that in temperature ranges 151–246 °C, the production of the $\mathrm{CH_2=CHF+SiF_4}$ species is the fastest process at all considered pressures down to around $10^{-12}$ bar. A similar observation can be made for pressure ranging from $10^{-12}$ to $10^2$ bars (Tables S1$a$–S1$e$ in the Supplementary material). The reader is referred further to Tables S1$a$–S1$e$ of the Supplementary material for a detailed study of the pressure dependence of the rate coefficients for the $\beta$-elimination processes of compounds **1–4**.

![](./images/812838135741284354_7.jpg)

Fig. 4. Arrhenius plot of the calculated rate coefficients [for $\mathrm{R_i{\to}Pi}$ ($i$=1–4)] by means of TST. ($P$ = 1 bar)

Table 8. TST and RRKM unimolecular rate coefficients (in s⁻¹) for the thermal decomposition of 2,2-difluoroethyltrifluorosilane (Reaction 1), 2,2-difluoroethylmethyldifluorosilane (Reaction 2), 2,2-difluoroethyldimethylfluorosilane (Reaction 3), and 2,2-difluoroethyltrimethylsilane (Reaction 4). ($P$ =1 bar)

<table>
<thead>
<tr>
<th rowspan="2">Pathway<br>$T$ (°C)</th>
<th colspan="4">TST</th>
<th colspan="4">RRKM</th>
</tr>
<tr>
<th>R1 → P1</th>
<th>R2 → P2</th>
<th>R3 → P3</th>
<th>R4 → P4</th>
<th>R1 → P1</th>
<th>R2 → P2</th>
<th>R3 → P3</th>
<th>R4 → P4</th>
</tr>
</thead>
<tbody>
<tr>
<td>151 [424 K]</td>
<td>$9.79×10^{-5}$ ($2.49×10^{-5}$)ᵃ</td>
<td>$2.57×10^{-7}$</td>
<td>$1.77×10^{-8}$</td>
<td>$2.05×10^{-9}$</td>
<td>$4.73×10^{-5}$ ($2.49×10^{-5}$)ᵃ</td>
<td>$2.42×10^{-7}$</td>
<td>$1.66×10^{-8}$</td>
<td>$1.91×10^{-9}$</td>
</tr>
<tr>
<td>161 [434 K]</td>
<td>$2.35×10^{-4}$ ($6.03×10^{-5}$)ᵃ</td>
<td>$7.09×10^{-7}$</td>
<td>$5.35×10^{-8}$</td>
<td>$6.44×10^{-9}$</td>
<td>$1.14×10^{-4}$ ($6.03×10^{-5}$)ᵃ</td>
<td>$6.71×10^{-7}$</td>
<td>$5.01×10^{-8}$</td>
<td>$6.01×10^{-9}$</td>
</tr>
<tr>
<td>171 [444 K]</td>
<td>$5.43×10^{-4}$ ($1.46×10^{-4}$)ᵃ</td>
<td>$1.87×10^{-6}$</td>
<td>$1.53×10^{-7}$</td>
<td>$1.92×10^{-8}$</td>
<td>$2.64×10^{-4}$ ($1.46×10^{-4}$)ᵃ</td>
<td>$1.78×10^{-6}$</td>
<td>$1.44×10^{-7}$</td>
<td>$1.80×10^{-8}$</td>
</tr>
<tr>
<td>181 [454 K]</td>
<td>$1.21×10^{-3}$ ($3.33×10^{-4}$)ᵃ</td>
<td>$4.74×10^{-6}$</td>
<td>$4.20×10^{-7}$</td>
<td>$5.45×10^{-8}$</td>
<td>$5.88×10^{-4}$ ($3.33×10^{-4}$)ᵃ</td>
<td>$4.50×10^{-6}$</td>
<td>$3.96×10^{-7}$</td>
<td>$5.12×10^{-8}$</td>
</tr>
<tr>
<td>181.6 [454.6 K]</td>
<td>$1.21×10^{-3}$</td>
<td>$5.00×10^{-6}$ ($4.98×10^{-5}$)ᵇ</td>
<td>$4.46×10^{-7}$</td>
<td>$5.80×10^{-8}$</td>
<td>$6.16×10^{-4}$</td>
<td>$4.75×10^{-6}$ ($4.98×10^{-5}$)ᵇ</td>
<td>$4.20×10^{-7}$</td>
<td>$5.45×10^{-8}$</td>
</tr>
<tr>
<td>191.7 [464.7 K]</td>
<td>$2.74×10^{-3}$</td>
<td>$1.22×10^{-5}$ ($1.01×10^{-4}$)ᵇ</td>
<td>$1.18×10^{-6}$</td>
<td>$1.59×10^{-7}$</td>
<td>$1.34×10^{-3}$</td>
<td>$1.17×10^{-5}$ ($1.01×10^{-4}$)ᵇ</td>
<td>$1.11×10^{-6}$</td>
<td>$1.50×10^{-7}$</td>
</tr>
<tr>
<td>201 [474 K]</td>
<td>$5.43×10^{-3}$ ($1.49×10^{-3}$)ᵃ</td>
<td>$2.70×10^{-5}$</td>
<td>$2.78×10^{-6}$</td>
<td>$3.86×10^{-7}$</td>
<td>$2.65×10^{-3}$ ($1.49×10^{-3}$)ᵃ</td>
<td>$2.58×10^{-5}$</td>
<td>$2.64×10^{-6}$</td>
<td>$3.65×10^{-7}$</td>
</tr>
<tr>
<td>204.2 [477 K]</td>
<td>$6.73×10^{-3}$</td>
<td>$3.46×10^{-5}$ ($2.78×10^{-4}$)ᵇ</td>
<td>$3.64×10^{-6}$</td>
<td>$5.11×10^{-7}$</td>
<td>$3.28×10^{-3}$</td>
<td>$3.31×10^{-5}$ ($2.78×10^{-4}$)ᵇ</td>
<td>$3.46×10^{-6}$</td>
<td>$4.83×10^{-7}$</td>
</tr>
<tr>
<td>211 [484 K]</td>
<td>$1.10×10^{-2}$ ($3.10×10^{-3}$)ᵃ</td>
<td>$6.11×10^{-5}$</td>
<td>$6.75×10^{-6}$</td>
<td>$9.68×10^{-7}$</td>
<td>$5.36×10^{-3}$ ($3.10×10^{-3}$)ᵃ</td>
<td>$5.84×10^{-5}$</td>
<td>$6.42×10^{-6}$</td>
<td>$9.17×10^{-7}$</td>
</tr>
<tr>
<td>212.6 [485.6 K]</td>
<td>$1.23×10^{-2}$</td>
<td>$6.94×10^{-5}$ ($4.94×10^{-4}$)ᵇ</td>
<td>$7.76×10^{-6}$</td>
<td>$1.12×10^{-6}$</td>
<td>$5.99×10^{-3}$</td>
<td>$6.64×10^{-5}$ ($4.94×10^{-4}$)ᵇ</td>
<td>$7.37×10^{-6}$</td>
<td>$1.06×10^{-6}$</td>
</tr>
<tr>
<td>221 [494 K]</td>
<td>$2.16×10^{-2}$ ($6.29×10^{-3}$)ᵃ</td>
<td>$1.34×10^{-4}$</td>
<td>$1.58×10^{-5}$</td>
<td>$2.34×10^{-6}$</td>
<td>$1.06×10^{-2}$ ($6.29×10^{-3}$)ᵃ</td>
<td>$1.28×10^{-4}$</td>
<td>$1.51×10^{-5}$</td>
<td>$2.22×10^{-6}$</td>
</tr>
<tr>
<td>225.3 [498.3 K]</td>
<td>$2.87×10^{-2}$</td>
<td>$1.86×10^{-4}$ ($1.15×10^{-3}$)ᵇ</td>
<td>$2.26×10^{-5}$</td>
<td>$3.38×10^{-6}$</td>
<td>$1.40×10^{-2}$</td>
<td>$1.78×10^{-4}$ ($1.15×10^{-3}$)ᵇ</td>
<td>$2.15×10^{-5}$</td>
<td>$3.21×10^{-6}$</td>
</tr>
<tr>
<td>235.3 [508.3 K]</td>
<td>$5.43×10^{-2}$</td>
<td>$3.89×10^{-4}$ ($2.00×10^{-3}$)ᵇ</td>
<td>$5.05×10^{-5}$</td>
<td>$7.78×10^{-6}$</td>
<td>$2.66×10^{-2}$</td>
<td>$3.74×10^{-4}$ ($2.00×10^{-3}$)ᵇ</td>
<td>$4.82×10^{-5}$</td>
<td>$7.41×10^{-6}$</td>
</tr>
<tr>
<td>246.4 [519.4 K]</td>
<td>$1.07×10^{-1}$</td>
<td>$8.57×10^{-4}$ ($4.40×10^{-3}$)ᵇ</td>
<td>$1.19×10^{-4}$</td>
<td>$1.89×10^{-5}$</td>
<td>$5.26×10^{-2}$</td>
<td>$8.25×10^{-4}$ ($4.40×10^{-3}$)ᵇ</td>
<td>$1.14×10^{-4}$</td>
<td>$1.80×10^{-5}$</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="9">- Experimental data: a) Ref [5]; b) Ref [6].</td>
</tr>
</tfoot>
</table>

Inspection of Table 8 and Figure 4 demonstrates that RRKM kinetic rate coefficients for the chemical reactions 1–4 increased with increasing temperature. Moreover, upon inspecting the RRKM data as shown in Figure 5, it seems obviously that according to higher activation energy barriers ranging from 33.05 to 42.81 kcal mol⁻¹, rather high pressures (>10⁻⁴ bar) are large enough to ensure a saturation of the calculated RRKM kinetics compared with the high-pressure limit (TST). Comparison with the RRKM results shows that the transition state theory approximation breaks down at pressures *P* <10⁻⁴ bar for the elimination process of compound 1 (i.e. 2,2-difluoroethyltrifluorosilane → CH₂=CHF+SiF₄).

![](./images/812838135741284354_8.jpg)

Fig. 5. A schematic fall-off plot for the unimolecular rate coefficient as the function of pressure for the β-elimination processes of 2,2-difluoroethyltrifluorosilane (Pathway 1: R1→P1), 2,2-difluoroethylmethyldifluorosilane (Pathway 2: R2→P2), 2,2-difluoroethyldimethylfluorosilane (Pathway 3: R3→P3), and 2,2-difluoroethyltrimethylsilane (Pathway 4: R4→P4).

Moreover, as can be seen in Table 8, the ratios between the TST and RRKM unimolecular rate coefficients for pathway **1** increase from ~1.96 to ~2.07 by increasing temperature from 151 to 246 °C. The differences are related to the applied tunneling correction on the rate coefficients which obtained using transition state theory in this study.

## 4. Conclusion

The β-elimination pathways of 2,2-difluoroethyltrifluorosilane (compound **1**), 2,2-difluoroethylmethyldifluorosilane (compound **2**), 2,2-difluoroethyldimethylfluorosilane (compound **3**), and 2,2-difluoroethyltrimethylsilane (compound **4**) in the gas-phase investigated computationally using M06-2*c* as and CBS-QB3 theoretical methods. The elimination energy barriers increased from 2,2-difluoroethyltrifluorosilane to 2,2-difluoroethyltrimethylsilane. The obtained data indicate that under kinetic reaction control, the production of vinyl fluoride and silicon tetrafluoride species *via* pathway **1** [R1→ CH₂=CHF + SiF₄] is more reactive than the products **P2–P4**. The calculated results show that the most abundant products derived from the β-elimination process of the 2,2-difluoroethylmethyldifluorosilane (**2**) are the vinyl fluoride and methyltrifluorosilane species from a thermodynamical viewpoint.

The most significant change is observed in the C₁–F₃ bond that is elongated in the transition states (1.921–1.981 Å), when compared to that in the reactant distances (1.373–1.379 Å). The transition state structure reveals more progress in the breaking of the C₁–F₃ bond compared to other changes in the process. NBO charge analysis suggests that the polarization of this bond is the determining factor here. The rate-determining step for pathways **1–4** proceed through the 4-membered transition state. Furthermore, NBO charge analysis reveals an increase in positive charge in carbon C₁ and fluorine F₃ more negatively charged in the TSs.

The achieved order of activation barrier heights could be described by the number of fluorine atoms attached to the silicon, as established by the natural bond orbital analysis. The results show that the occupancies of $\sigma_{\text{C1-F3}}$ bonding orbital decrease from compounds **1** to **4** in the following order: **1 > 2 > 3 > 4**, and the occupancies of $\sigma^{*}_{\text{C1-F3}}$ antibonding orbital increase in the opposite order. This fact reveals that easier of the C₁–F₃ bond breaking in compound **1** compared to compounds **2–4**. Further, the HOMO-LUMO energy gaps for compounds **1–4** decrease with increasing of energy barrier in the following order

as $\boldsymbol{4 < 3 < 2 < 1}$.

The calculated energy barriers and kinetics rate coefficients using the CBS-QB3 method yields good agreement with the available experimental measured values. RRKM calculations reveal that overwhelmingly high pressures where $P > 10^{-4}$ bar are required to ensure the validity of the transition state theory approximation for the reactions $\boldsymbol{1-4}$.

## Supplementary material
Supplementary data (Table S1) associated with this article can be found, in the online version. Figure S1. Energy profiles along the intrinsic reaction coordinate for the thermal decomposition of compounds $\boldsymbol{1-4}$ at the B3LYP/6-311G(2d,d,p) level of theory; Table S1: Unimolecular kinetics for the studied pathways (results obtained using RRKM theory at different pressures and temperatures, according to the computed CBS-QB3 energy profiles).

## References
[1] R.N. Haszeldine, M.J. Newlands, J.B. Plumb, Polyfluoroalkyl Polysiloxanes, Proc. Chem. Soc. (1960) 133-160.

[2] R.N. Haszeldine, J.C. Young, $\alpha$-elimination and carbene formation from silicon compounds, Proc. Chem. Soc. (1959) 377-414.

[3] W.I. Bevan, R.N. Haszeldine, J.C. Young, Chem. Ind. (London) (1961) 789.

[4] T.N. Bell, R.N. Haszeldine, M.J. Newlands, J.B. Plumb, Polyfluoroalkyl compounds of silicon. Part VII. The thermal and hydrolytic stabilities of $\alpha$-, $\beta$- and $\gamma$-fluorine-substituted alkyl-polysiloxanes, J. Chem. Soc. (1965) 2107-2111.

[5] R.N. Haszeldine, P.J. Robinson, R.F. Simmons, The kinetics of the reactions of silicon compounds. Part I. the gas-phase thermal decomposition of 2,2-difluoroethyltrifluorosilane, J. Chem. Soc. (1964) 1890-1894.

[6] D. Graham, R.N. Haszeldine, P.J. Robinson, The kinetics of the reactions of silicon compounds. part III. gas-phase unimolecular thermal decomposition of 2,2-difluoroethylmethyldifluorosilane, J. Chem. Soc. B (1969) 652-654.

[7] I.M.T. Davidson, C. Eaborn, M.N. Lilly, Gas-phase reactions of halogenoalkylsilanes. Part I. 2-chloroethyltrichlorosilane, J. Chem. Soc. (1964) 2624-2630.

[8] I.M.T. Davidson, C.J.L. Metcalfe, Gas-phase reactions of halogenoalkylsilanes. part

II. 2-chloroethylethyldichlorosilane, J. Chem. Soc. (1964) 2630–2633.

[9] I.M.T. Davidson, M.R. Jones, Gas-phase reactions of halogenoalkylsilanes. part III. 2-chloroethyldiethylchlorosilane, J. Chem. Soc. (1965) 5481–5485.

[10] I.M.T. Davidson, M.R. Jones, C. Pett, Gas-phase reactions of halogenoalkylsilanes. part IV. 1-chloroethyldiethylchlorosilane and 2-chloroethyltrialkylsilanes, J. Chem. Soc. B (1967) 937–940.

[11] G. Fishwick, R.N. Haszeldine, C. Parkinson, P.J. Robinson, R.F. Simmons, Kinetics of the thermal decomposition of Polyfluoroalkylsilicon compounds, Chem. Commun. (1965) 382–384.

[12] Y. Zhao, D.G. Truhlar, The M06 suite of density functionals for main group thermochemistry, thermochemical kinetics, noncovalent interactions, excited states, and transition elements: two new functionals and systematic testing of four M06-class functionals and 12 other functionals, Theor. Chem. Acc. 120 (2008) 215–241.

[13] T.H. Dunning Jr., Gaussian basis sets for use in correlated molecular calculations. I. the atoms boron through neon and hydrogen, J. Chem. Phys. 90 (1989) 1007–1023.

[14] H. Eyring, The activated complex in chemical reactions, J. Chem. Phys. 3 (1935) 107–115.

[15] H.S. Johnston, Gas Phase Reaction Rate Theory, Roland Press, New York, 1966.

[16] K.J. Laidler, Theories of Chemical Reaction Rates, McGraw-Hill, New York, 1969.

[17] R.E. Weston, H.A. Schwartz, Chemical Kinetics, Prentice-Hall, New York, 1972.

[18] D. Rapp, Statistical Mechanics, Holt, Rinehart, and Winston, New York, 1972.

[19] E.E. Nikitin, Theory of Elementary Atomic and Molecular Processes in Gases, Clarendon Press, Oxford, 1974.

[20] I.W.M. Smith, Kinetics and Dynamics of Elementary Gas Reactions, Butterworths, London, 1980.

[21] P.J. Robinson, K.A. Holbrook, Unimolecular Reactions, Wiley, New York, 1972.

[22] J.I. Steinfeld, J.S. Francisco, W.L. Hase, Chemical Kinetics and Dynamics, Prentice-Hall, Englewood Cliffs, New Jersey, 1999.

[23] H. Eyring, S.H. Lin, S.M. Lin, Basic Chemical Kinetics, Wiley, New York, 1980.

[24] A.E. Reed, R.B. Weinstock, F. Weinhold, Natural population analysis, J. Chem. Phys. 83 (1985) 735–746.

[25] J.K. Badenhoop, F. Weinhold, Natural steric analysis of internal rotation barriers, Int. J. Quantum. Chem. 72 (1999) 269–280.

[26] M.J. Frisch, G.W. Trucks, H.B. Schlegel, G.E. Scuseria, M.A. Robb, J.R.
Cheeseman, G. Scalmani, V. Barone, B. Mennucci, G.A. Petersson, H. Nakatsuji,
M. Caricato, X. Li, H.P. Hratchian, A.F. Izmaylov, J. Bloino, G. Zheng, J.L.
Sonnenberg, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T.
Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, J.A. Montgomery, J.E. Peralta,
F. Ogliaro, M. Bearpark, J.J. Heyd, E. Brothers, K.N. Kudin, V.N. Staroverov, R.
Kobayashi, J. Normand, K. Raghavachari, A. Rendell, J.C. Burant, S.S. Iyengar, J.
Tomasi, M. Cossi, N. Rega, J.M. Millam, M. Klene, J.E. Knox, J.B. Cross, V.
Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R.E. Stratmann, O. Yazyev, A.J.
Austin, R. Cammi, C. Pomelli, J.W. Ochterski, R.L. Martin, K. Morokuma, V.G.
Zakrzewski, G.A. Voth, P. Salvador, J.J. Dannenberg, S. Dapprich, A.D. Daniels,
Farkas, J.B. Foresman, J.V. Ortiz, J. Cioslowski, D.J. Fox, Gaussian 09, Revision
C.01, Wallingford CT (2010).

[27] S. Pan, L. Wang, Atmospheric oxidation mechanism of $m$-xylene initiated by OH
radical, J. Phys. Chem. A 118 (2014) 10778-10787.

[28] R.J. Bartlett, J.D. Watts, S.A. Kucharski, J. Noga, Non-iterative fifth-order triple and
quadruple excitation energy corrections in correlated methods, Chem. Phys. Lett.
165 (1990) 513-522.

[29] J.F. Stanton, Why CCSD(T) Works: a different perspective, Chem. Phys. Lett. 281
(1997) 130-134.

[30] A. Szabo, N.S. Ostlund, Modern Quantum Chemistry: Introduction to Advanced
Electronic Structure Theory, McGraw-Hill, New York, 1989.

[31] J.A. Sousa, P.P. Silva, A.E.H. Machado, M.H.M. Reis, L.L. Romanielo, C.E. Hori,
Application of computational chemistry methods to obtain thermodynamic data for
hydrogen production from liquefied petroleum gas, Braz. J. Chem. Eng. 30 (2013)
83-93.

[32] J.W. Ochterski, G.A. Peterson, J.A. Montgomery Jr., A complete basis set model
chemistry. V. extensions to six or more heavy atoms, J. Chem. Phys. 15 (1996)
2598-2619.

[33] J.A. Montgomery Jr., M.J. Frisch, J.W. Ochterski, G.A. Petersson, A complete basis
set model chemistry. VI. use of density functional geometries and frequencies, J.
Chem. Phys. 110 (1999) 2822-2827.

[34] M.R. Nyden, G.A. Petersson, Complete basis set correlation energies. I. the

asymptotic convergence of pair natural orbital expansions, J. Chem. Phys. 75 (1981)
1843-1862.

[35] G.A. Petersson, M.A. Al-Laham, A complete basis set model chemistry. II. open-
shell systems and the total energies of the first-row atoms, J. Chem. Phys. 94 (1991)
6081-6090.

[36] J.A. Montgomery Jr., M.J. Frisch, J.W. Ochterski, G.A. Petersson, A complete basis
set model chemistry. VII. use of the minimum population localization method, J.
Chem. Phys. 112 (2000) 6532-6542.

[37] A. Shiroudi, M.S. Deleuze, Theoretical study of the oxidation mechanisms of
thiophene initiated by hydroxyl radicals, J. Mol. Model. 21 (2015) 301.
https://doi.org/10.1007/s00894-015-2839-2

[38] E. Zahedi, S. Shaabani, A. Shiroudi, Following the molecular mechanism of
decarbonylation of unsaturated cyclic ketones using bonding evolution theory
coupled with NCI analysis, J. Phys. Chem. A. 121 (2017) 8504-8517.

[39] X. Li, M.J. Frisch, Energy-represented direct inversion in the iterative subspace
within a hybrid geometry optimization method, J. Chem. Theory Comput. 2 (2006)
835-839.

[40] F. Fukui, A formulation of the reaction coordinate, J. Phys. Chem. 74 (1970)
4161-4163.

[41] H.P. Hratchian, H.B. Schlegel, Accurate reaction paths using a Hessian based
predictor-corrector integrator, J. Chem. Phys. 120 (2004) 9918-9924.

[42] A.R. Oliaey, A. Shiroudi, E. Zahedi, M.S. Deleuze, Theoretical study on the
mechanisms and kinetics of the $\beta$-elimination of 2,2-dihaloethyltrihalosilanes
(X = F, Cl, Br) compounds: a DFT study along with a natural bond orbital analysis,
React. Kinet. Mech. Cat. 124 (2018) 27-44.

[43] S. Canneaux, F. Bohr, E. Henon, KiSThelP: a program to predict thermodynamic
properties and rate constants from quantum chemistry results, J. Comput. Chem. 35
(2014) 82-93.

[44] J.W. Moore, R.G. Pearson, Kinetics and Mechanism-The Study of Homogeneous
Chemical Reactions, Wiley, New York, 1981.

[45] H.H. Carstensen, A.M. Dean, O. Deutschmann, Rate constants for the H abstraction
from alkanes (R-H) by $R'O_2$ radicals: a systematic study on the impact of R and R',
Proc. Combust. Inst. 31 (2007) 149-157.

[46] (a) E. Wigner, Calculation of the rate of elementary association reactions, J. Chem. Phys. 5 (1937) 720–725; (b) E. Wigner, Uber das uberschreiten von potentialschwellen bei chemischen reaktionen, Z. Phys. Chem. B 19 (1932) 203–216.

[47] A. Shiroudi, E. Zahedi, A.R. Oliaey, M.S. Deleuze, Reaction mechanisms and kinetics of the elimination processes of 2-chloroethylsilane and derivatives: a DFT study using CTST, RRKM, and BET theories, Chem. Phys. 485–486 (2017) 140–148.

[48] A. Shiroudi, E. Zahedi, Understanding the kinetics of thermal decomposition of 2,3-epoxy-2,3-dimethylbutane using RRKM theory, RSC. Adv. 6 (2016) 91882–91892.

[49] R.G. Gilbert, S.C. Smith, Theory of unimolecular and recombination reactions, Blackwell Scientific Publications, Boston, MA, 1990.

[50] J. Troe, Theory of thermal unimolecular reactions at low pressures. II. strong collision rate constants: applications, J. Chem. Phys. 66 (1977) 4758–4775.

[51] R.J. Kee, F.M. Rupley, J.A. Miller, M.E. Coltrin, J.F. Grcar, E. Meeks, H.K. Moffat, A.E. Lutz, G. Dixon-Lewis, M.D. Smooke, J. Warnatz, G.H. Evans, R.S. Larson, R.E. Mitchell, L.R. Petzold, W.C. Reynolds, M. Caracotsios, W.E. Stewart, P. Glarborg, C. Wang, C.L. McLellan, O. Adigun, W.G. Houf, C.P. Chou, S.F. Miller, P. Ho, P.D. Young, D.J. Young, D.W. Hodgson, M.V. Petrova, K.V. Puduppakkam, CHEMKIN, Reaction Design, San Diego, CA, 2010.

[52] F.M. Mourits, H.A. Rummens, A critical evaluation of Lennard-Jones and Stockmayer potential parameters and of some correlation methods, Can J. Chem. 55 (1977) 3007–3020.

[53] A. Maccoll, Gas-phase eliminations. part I. the unimolecular gas-phase pyrolysis of some esters and analogous compounds, J. Chem. Soc. (1958) 3398–3402.

[54] C. Eaborn, Organosilicon compounds, Butterworths Scientific Publications, London, 1960.

[55] W. Sun, L. Yang, L. Yu, M. Saeys, Ab initio reaction path analysis for the initial hydrogen abstraction from organic acids by hydroxyl radicals, J. Phys. Chem. A 113 (2009) 7852–7860.

[56] A.F. Trotman-Dickenson, Gas Kinetics, Butterworths, London, 1955.

[57] B.G. Gowenlock, Arrhenius factors (frequency factors) in unimolecular reactions, Quart. Rev. Chem. Soc. 14 (1960) 133–145.

[58] S.W. Benson, W.B. DeMore, Ann. Rev. Phys. Chem. 16 (1965) 397–450.

[59] H.E. O'Neal and S.W. Benson, A method for estimating the Arrhenius a factors for four- and six-center unimolecular reactions, J. Phys. Chem. 71 (1967) 2903–2921

[60] G.S. Hammond, A correlation of reaction rates, J. Am. Chem. Soc. 77 (1953) 334–338.

[61] N. Agmon, R.D. Levine, Energy, entropy and the reaction coordinate: thermodynamic-like relations in chemical kinetics, Chem. Phys. Lett. 52 (1977) 197–201.

[62] G. Lendvay, Bond orders from ab initio calculations and a test of the principle of bond order conservation, J. Phys. Chem. 93 (1989) 4422–4429.

[63] A.E. Reed, L.A. Curtiss, F. Weinhold, Intermolecular interactions from a natural bond orbital, donor-acceptor viewpoint, Chem. Rev. 88 (1988) 899–926.

[64] K.B. Wiberg, Application of the pople-santry-segal CNDO method to the cyclopropylcarbinyl and cyclobutyl cation and to bicyclobutane, Tetrahedron. 24 (1968) 1083–1096.

[65] A.E. Reed, J.E. Carpenter, Weinhold F, NBO version 3.1, 2003.

[66] A. Moyano, M.A. Periclas, E. Valenti, A theoretical study on the mechanism of the thermal and the acid-catalyzed decarboxylation of 2-oxetanones (β-lactones), J. Org. Chem. 54 (1989) 573–582.

[67] F. Rosas, R.M. Dominguez, M. Tosta, J.R. Mora, E. Marquez, T. Cordova, G. Chuchani, The mechanism of the homogeneous, unimolecular gas-phase elimination kinetic of 1,1-dimethoxycyclohexane: experimental and theoretical studies, J. Phys. Org. Chem. 23 (2010) 743–750.

[68] E. Márquez, J.R. Mora, T. Cordova, G. Chuchani, DFT calculations of triethyl and trimethyl orthoacetate elimination kinetics in the gas phase, J. Phys. Chem. A, 113 (2009) 2600–2606.
