# H₂S Stability of Metal–Organic Frameworks: A Computational Assessment

Pengbo Lyu and Guillaume Maurin*

Cite This: ACS Appl. Mater. Interfaces 2021, 13, 4813−4822

ABSTRACT: The H₂S stability of a range of metal−organic frameworks (MOFs) was systematically assessed by first-principles calculations. The most likely degradation mechanism was first determined and we identified the rate constant of the degradation reaction as a reliable descriptor for characterizing the H₂S stability of MOFs. A qualitative H₂S stability ranking was thus established for the list of investigated materials. Structure−stability relationships were further envisaged considering several variables including the nature of the linkers and their grafted functional groups, the pore size, the nature of metal sites, and the presence/nature of coordinatively unsaturated sites. This knowledge enabled the anticipation of the H₂S stability of one prototypical MOF, e.g., MIL-91(Ti), which has been previously proposed as a good candidate for CO₂ capture. This computational strategy enables an accurate and easy handling assessment of the H₂S stability of MOFs and offers a solid alternative to experimental characterizations that require the manipulation of a highly toxic and corrosive molecule.

KEYWORDS: metal−organic frameworks, hydrogen disulfide, prediction of stability, understanding of degradation mechanism, density functional theory

![](./images/812515829491957761_1.jpg)

## 1. INTRODUCTION

Metal−organic frameworks (MOFs), a class of highly crystalline and tunable porous materials, have been envisaged over the past several years for a myriad of applications in the fields of catalysis,¹⁻² gas adsorption/separation,³⁻⁶ biomedicine,⁷⁻⁸ and sensing,⁹ among others.¹⁰⁻¹² While their performances sometimes outperform the well-established porous media such as zeolites, silica, and carbons, this family of hybrid materials is still not widely applied to industry since most of the studies rarely report their chemical stability under working conditions. Typically, the performances of MOFs are promising to solve challenges in critical industrial applications such as CO₂ capture,⁵,¹³,¹⁴ flue gas scrubbing,¹⁵⁻¹⁷ and natural gas (NG) and refinery off-gas (ROG) upgrading.¹⁸⁻²⁰ This critically calls for a systematic exploration of the stability of the best MOFs upon exposure to impurities present in the associated flue gas streams²¹,²² such as H₂O, H₂S, SOₓ, and NOₓ, among others to meet the industry's expectation in this field.²³ While the stability of MOFs upon water adsorption is routinely assessed from both experimental²⁴⁻²⁷ and modeling²⁸⁻³¹ standpoints, this is far to be the case under harsh conditions as for instance in the presence of acidic and basic species.³² Only a small fraction of MOFs promising for CO₂ capture and natural gas or biogas purification has been tested in terms of stability upon exposure to NOₓ, SOₓ, H₂S, and NH₃.³²⁻³⁶ Specifically, related to H₂S, while a series of MOFs have been envisaged for the capture of this highly toxic molecule,¹⁵,¹⁸,³³,³⁷⁻⁴⁴ such as MIL-53(Al, Cr) and MIL-47(V),³⁸,³⁹ soc-MOF,¹⁸ kag-MOF-1,¹⁵ MIL-125-(Ti),³⁷ UiO-66,⁴⁰ Mg-CUK-1,⁴¹ MIL-53(Al)-FA,⁴² MFM-300(Sc),³³ and MIL-53(Al)-TDC,⁴³ the H₂S stability of only a very few promising MOFs for the applications mentioned above, e.g., KAUST-7,⁴⁴ KAUST-8,⁴⁴ kag-MOF-1,¹⁵ soc-MOF,¹⁸ MIL-125(Ti),³⁷ and MOF-74(Ni),⁴⁵ has been verified. Beyond this observation, to the best of our knowledge, no systematic exploration of the H₂S stability of MOFs has been reported to date and an understanding of the H₂S degradation mechanism is still far from clear. Indeed, while standard experimental techniques such as X-ray diffraction and thermogravimetric analysis⁴⁰,⁴⁶⁻⁴⁹ have been used to characterize the stability of MOFs after exposure to H₂S, only a few in situ Fourier transform infrared (FT-IR) studies have been conducted to characterize the adsorption modes of H₂S in MOFs;³⁷⁻³⁹,⁴¹ however, without paying attention to the H₂S degradation mechanism. From a computational standpoint, while the H₂S physisorption mechanism has been elucidated for a range of MOFs using force field-based Monte Carlo (MC) simulations and density functional theory (DFT) calculations,¹⁸,¹⁹,³⁷,³⁹,⁴¹,⁴³ none of these studies have addressed the question of H₂S stability/degradation.

Received: November 30, 2020
Accepted: January 6, 2021
Published: January 15, 2021

![](./images/812515829491957761_2.jpg)

https://dx.doi.org/10.1021/acsami.0c21285
ACS Appl. Mater. Interfaces 2021, 13, 4813−4822

Herein, the driving step of the $H_2S$-induced MOF degradation reaction was explored systematically using periodic DFT calculations applied to a series of MOFs. To this purpose, we first evaluated different plausible degradation mechanisms with MIL-53(Al)-BDC$^{30}$ taken as our reference MOF material since it was already proved experimentally to be stable upon exposure to $H_2S$. This preliminary stage enabled us to identify the most probable degradation mechanism and to propose the rate constant of the degradation reaction as a reliable descriptor for characterizing the $H_2S$ stability of MOFs. We further explored a range of MOFs with the objective to evaluate how the stability of this family of materials is affected by the nature of the linkers with the consideration of several derivatives of MIL-53$^{42,43}$ and CAU-10,$^{50-52}$ the nature of the functional groups grafted to organic linkers with the use of functionalized MIL-53(Al)s,$^{53,54}$ the pore size with the comparison between the large pore (lp) and narrow pore (np) forms of MIL-53(Al)-BDC-NH$_2$,$^{54}$ the metal substitution with the cases of CAU-10(Al)$^{55}$ and MIL-160(Al)$^{56}$ and their Ti analogues, and the presence/nature of coordinatively unsaturated site (CUS) with the consideration of MOF-74 (Ni)$^{45}$ and MOF-74(Zn).$^{40,45}$ This systematic exploration led to a qualitative $H_2S$ stability ranking of all these MOFs based on the evaluation of their associated rate constants for the corresponding first-step degradation reaction. This allowed us to reveal the elemental structure-stability relationship that was further transferred to anticipate the $H_2S$ stability of the MOF MIL-91(Ti) as a showcase since this material has been proposed as a good candidate for the selective capture of CO$_2$ under flue gas conditions,$^{57}$ while its $H_2S$ stability was still unknown. We believe that this computational approach allows an accurate and easy handling assessment of the $H_2S$ stability of MOFs without the need to perform fastidious experiments due to the high toxicity and corrosive character of $H_2S$.

## 2. COMPUTATIONAL METHODS

The unit cells of all empty MOFs were first geometry optimized at the DFT level starting with their known crystal structures. Note that for all structures showing lattice parameters below 12 Å, supercells associated with a doubled cell parameter along the corresponding direction were constructed. These calculations used the projector augmented wave (PAW)$^{58}$ formalism within the generalized gradient approximation (GGA) method with the Perdew−Burke−Ernzerhof (PBE) exchange-correlation functional as implemented in Vienna ab initio simulation package (VASP).$^{59-61}$ The DFT-D3 method$^{62}$ was employed to include the dispersion correction. A cutoff energy of 900 eV for the plane-wave basis set was considered to ensure convergence with the following criteria of 0.01 eV Å$^{-1}$ and 10$^{-5}$ eV for the forces and energy, respectively. The Brillouin zone was sampled at the gamma point. Note that for Ni- and Ti-containing MOFs, spin polarization was considered together with the DFT + U approach$^{63}$ to accurately describe the 3d states, where $U_{\text{eff}}$ was selected to be 6.4 and 3.0 eV for Ni$^{64}$ and Ti,$^{65}$ respectively. In addition, unlike Ti-MOFs that have zero magnetic moment, we found for MOF-74(Ni) that ferromagnetic (FM) intrachain coupling is slightly more stable than the antiferromagnetic (AFM) one by 0.06 eV. Therefore, the FM configuration for MOF-74(Ni) was selected for geometry optimization and subsequent calculations described below. Regarding the functionalized MIL-53(Al)-BDC, we considered the narrow pore (np) structure of MIL-53(Al)-BDC-NH$_2$ as well as its large pore (lp) form known to exist in the presence of guest molecules,$^{54}$ while MIL-53(Al)-BDC-NO$_2$ was treated solely in its previous reported lp form since this material did not show any structure contraction upon adsorption.$^{53}$ The DFT-optimized lattice parameters of all empty MOFs are summarized in Table S1 along with the corresponding structures represented in Figures S1−S6. Starting with these DFT-optimized structures, one $H_2S$ molecule was introduced per unit cell and the resulting guest-loaded configurations (labeled IS for initial states) were further DFT geometry optimized using the same settings as mentioned above; their lattice parameters were maintained fixed. As a further stage, the $H_2S$ degradation mechanism was explored; the transition states (TS) and the products (called final states (FS)) were identified using the climbing image nudged elastic band method (CI-NEB)$^{66}$ as implemented in the Transition State Tools for VASP (VTST) module.$^{67}$ Frequency calculations were performed for all minima (IS and FS) and transition state (TS) structures to ensure no imaginary frequency for both IS and FS and only 1 imaginary frequency for TS. Only the positions of the atoms involved in the first-step degradation reaction were relaxed during frequency calculations.

The potential energy ($E$) profile was then constructed by considering the optimized MOF unit cell and $H_2S$ in the gas phase as zero-point potential energy. The reaction energy ($\Delta E$) and its associated energy barrier ($\Delta E^{\ddagger}$) at 0 K were calculated using eqs 1 and 2

$$
\Delta E = E(\text{FS}) - E(\text{IS}) \tag{1}
$$

$$
\Delta E^{\ddagger} = E(\text{TS}) - E(\text{IS}) \tag{2}
$$

where $E(X = \text{IS, TS, FS})$ is the relative energy of the corresponding X configurations.

The rate constant ($k$) of the first-step $H_2S$ degradation reaction was further considered as a more reliable descriptor than $\Delta E^{\ddagger}$ to quantitatively assess the stability of MOFs against $H_2S$ at room temperature (298 K). Indeed, $k$ explicitly reflects the chemical equilibrium between the three configurations (IS, TS, and FS), rather than simply comparing the reaction energy barrier, $\Delta E^{\ddagger}$, which is insufficient to assess the difference between MOFs in terms of stability.

The $k$ value was calculated using eq 3

$$
k = \exp\left(-\frac{\Delta G^{\ddagger}}{RT}\right) - \exp\left(-\frac{\Delta G_{\text{r}}^{\ddagger}}{RT}\right) \tag{3}
$$

where $\Delta G^{\ddagger}$ is the reaction free energy barrier, $\Delta G_{\text{r}}^{\ddagger}$ is the reversed reaction free energy barrier, and $T$ is the temperature (298 K). $\Delta G^{\ddagger}$ and $\Delta G_{\text{r}}^{\ddagger}$ were calculated as follows

$$
\Delta G^{\ddagger} = G(\text{TS}) - G(\text{IS}) \tag{4}
$$

$$
\Delta G_{\text{r}}^{\ddagger} = G(\text{TS}) - G(\text{FS}) \tag{5}
$$

where $G(X = \text{IS, TS, FS})$ is the free energy of the corresponding X configurations calculated as follows$^{8,68}$

$$
G = E_0 + F_{\text{vib}}(\nu_i, T) \tag{6}
$$

where $E_0$ is the energy of the X configuration and $F_{\text{vib}}(\nu_i, T)$ is its corresponding Helmholtz vibrational energy defined as follows

$$
F_{\text{vib}}(\nu_i, T) = \frac{1}{2} \sum_{i} \left\{ h\nu_i + 2k_{\text{b}}T \ln\left[1-\exp\left(-\frac{h\nu_i}{k_{\text{b}}T}\right)\right] \right\} \tag{7}
$$

where $h$ is Planck's constant, $k_{\text{b}}$ is Boltzmann's constant, $\nu_i$ is the harmonic vibrational frequency for relaxed atoms, and $T$ is set to 298 K.

According to the definition of $k$, a positive value indicates that the decomposition of the corresponding MOF is feasible upon exposure to $H_2S$, whereas a negative $k$ value is a sign that the degradation is less probable. Since the first step of the degradation reaction is assumed to be the predominant step in the reaction path, indeed, the more negative the $k$, the more stable the associated MOF against $H_2S$.

## 3. RESULTS

### 3.1. Exploration of the Plausible $H_2S$ Degradation Mechanism and Evaluation of the Rate Constant: MIL-53(Al)-BDC as a Showcase.
Referring to the mechanism proposed in the literature for the degradation of MOFs upon exposure to acid gas, e.g., SO$_2$,$^{69}$ we explored several possible $H_2S$ first-step degradation reaction paths, as shown in Scheme 1.

Scheme 1. Three Different Mechanisms of the First-Step Degradation Reaction between $H_2S$ and MOFs with MIL-53(Al)-BDC as a Model System

![](./images/812515829491957761_3.jpg)

(1) Mechanism 1: one of the metal-oxygen bonds breaks and the created unsaturated $\mu$-O atom is further coordinated by a hydrogen atom transferred from $H_2S$, while the remaining $-SH$ group combines with the created coordinatively unsaturated Al site to form a metal-sulfur bond.

(2) Mechanism 2: similar to mechanism 1, a hydrogen atom of $H_2S$ makes a bond with the created unsaturated $\mu$-O atom; however, the $-SH$ group coordinates to the carbon atom of the $-COO^-$ group.

(3) Mechanism 3: the $-SH$ group replaces the $\mu$-OH hydroxyl function of the MOF to form two Al-S bonds, while the other hydrogen atom of $H_2S$ combines with the released OH function to form a water molecule.

These three mechanisms were explored for MIL-53(Al)-BDC considered as a model MOF in our study and the different states along the reaction are illustrated in Figure 1. The most stable adsorption configurations of $H_2S$ (IS) correspond to the scenario where its S atom points toward the $\mu$-OH group with a separating $S(H_2S)-H(\mu-OH)$ distance of $2.33$ Å. For mechanism 1, one of the Al-O bonds breaks upon $H_2S$ adsorption and the Al-S distance shortens along the reaction path as follows: $4.36$ Å (IS)$\rightarrow$ $2.62$ Å (TS)$\rightarrow$ $2.46$ Å (FS) to finally form a bond, while the H-S bond of $H_2S$ dissociates (H-S distance: $1.35$ Å (IS)$\rightarrow$ $1.82$ Å (TS)$\rightarrow$$3.29$ Å (FS)). This mechanism is associated with a very high energy barrier $(\Delta E^{\ddagger})$ and a highly endothermic reaction energy $(\Delta E)$ of 169 and 115 kJ mol$^{-1}$, respectively. For mechanism 2, the reaction proceeds via a significant reduction in the S-C distance between $S(H_2S)$ and $C(COO-)$ from $4.70$ Å (IS) to $2.56$ Å (TS) prior to forming a S-C bond of $1.94$ Å (FS), while one of the H-S bonds of $H_2S$ breaks along the reaction path $1.35$ Å (IS) $\rightarrow$ $2.00$ Å (TS) $\rightarrow$ $2.64$ Å (FS). This degradation mechanism is also highly endothermic $(\Delta E = 117$ kJ mol$^{-1})$ and the associated energy barrier $(\Delta E^{\ddagger} = 146$ kJ mol$^{-1})$ is as high as the value obtained for mechanism 1. Considering the fact that the protonation of the oxygen atom of the carboxylate group does not lead to an uncoordinated Al site, this mechanism was excluded since no further degradation of the framework can be expected. For mechanism 3, similar to mechanism 1, there is formation of an Al-S bond along the reaction path as seen by the evolution of the corresponding Al-S distance ($4.36$ Å (IS) $\rightarrow$ $2.30$ Å (TS) $\rightarrow$ $2.38$ Å (FS)). Although the resulting reaction energy $\Delta E$ ($123$ kJ mol$^{-1}$) is only slightly higher than the value obtained for mechanism 1 ($115$ kJ mol$^{-1}$), its energy barrier $\Delta E^{\ddagger}$ is much higher (256 vs 169 kJ mol$^{-1}$). This trend is explained by the fact that mechanism 3 proceeds via the breaking of two metal-oxygen bonds. Therefore, this set of calculations demonstrates that mechanism 1, where only one of the metal-oxygen bonds breaks and one metal-sulfur bond forms, is the most likely first step of the MOF degradation upon exposure to $H_2S$. This mechanism 1 was thus systematically explored for all the investigated MOFs. We assumed a similar first-step degradation reaction mechanism for all the MOFs described above.

Furthermore, the calculated $k$ value for the degradation mechanism 1 was found to be $-4.9 \times 10^{-9}$. Indeed, since MIL-53(Al)-BDC was previously demonstrated to be stable against

![](./images/812515829491957761_4.jpg)

Figure 1. Potential energy profile for the three different $H_2S$ degradation mechanisms explored in the case of MIL-53(Al)-BDC with the associated relative energies for the initial states (IS), transition states (TS), and final states (FS). An illustration of the IS, TS, and FS configurations is also provided. Color codes are carbon (brown), oxygen (red), sulfur (yellow), hydrogen (white), and aluminum (green). The corresponding energies and distances are reported in kJ mol$^{-1}$ and Å, respectively.

![](./images/812515829491957761_5.jpg)

Figure 2. Potential energy profiles for the first-step H₂S degradation reaction by MIL-53(Al)-BDC (black line), -FA (red line), and -TDC (blue line). The color code is the same as in Figure 1. The corresponding energies and distances are reported in kJ mol⁻¹ and Å, respectively.

H₂S experimentally, this value was considered in the following sections as a reference to assess the stability of the series of MOFs. Indeed, all MOFs associated with similar or even more negative k values will be considered as stable materials upon exposure to H₂S. Therefore, this descriptor was used to rank qualitatively the H₂S stability of all MOFs described above.

3.2. Impact of the Nature of Linkers on the H₂S Stability of Al-MOFs. 3.2.1. MIL-53(Al) Frameworks. The first-step degradation reaction paths and the corresponding potential energy profiles for MIL-53(Al)-FA and MIL-53(Al)-TDC are compared with those for MIL-53(Al)-BDC in Figure 2. The most stable adsorption configurations of H₂S (IS) for both MIL-53(Al)-FA and MIL-53(Al)-TDC are similar to that observed for MIL-53(Al)-BDC with a predominant interaction between S(H₂S) and H(μ-OH). It is worth noting that the configurations of TS and FS along the reaction paths are also quite similar for the three different MOFs. The reaction energy barrier $\Delta E^{\ddagger}$ for MIL-53(Al)-FA (165 kJ mol⁻¹) is very close to that for MIL-53(Al)-BDC (169 kJ mol⁻¹), while the associated reaction energy $\Delta E$ is slightly lower (102 vs 115 kJ mol⁻¹). Interestingly, MIL-53(Al)-TDC shows a significantly lower $\Delta E^{\ddagger}$ value (126 kJ mol⁻¹) but a similar $\Delta E$ value (103 kJ mol⁻¹) as compared to the values found for the two other isoreticular forms.

Although MIL-53(Al)-TDC shows the lowest $\Delta E^{\ddagger}$, it does not mean that it is the least stable one out of the three MOFs. Indeed, Table 1, which reports the reaction free energy barriers ($\Delta G^{\ddagger}$), the reversed reaction free energy barriers ($\Delta G_{r}^{\ddagger}$) and the rate constant (k) values for the three isoreticular MOFs at 298 K, shows that MIL-53(Al)-TDC is by far the most stable one since its associated k value is much more negative $(-1.1 \times 10^{-3})$ as compared to the values obtained for both MIL-53(Al)-BDC $(-4.9 \times 10^{-9})$ and MIL-53(Al)-FA $(-1.4 \times 10^{-9})$. These calculations predict the following sequence in terms of stability: MIL-53(Al)-TDC $\gg$ MIL-53(Al)-BDC $\sim$ MIL-53(Al)-FA since the two last MOFs show k values of similar magnitudes. This trend is consistent with the very good H₂S adsorption/desorption cyclability of MIL-53(Al)-TDC previously re- ported⁴³ as well as similar stabilities of MIL-53(Al)-FA⁴² and MIL-53(Al)-BDC.³⁰ The combination of a lower $\Delta E^{\ddagger}$ value with a similar $\Delta E$ finally leads to a more negative k (and higher stability) for MIL-53(Al)-TDC. The resulting low $\Delta E^{\ddagger}$ value for this MOF comes from the lower energy for TS as compared to that for the MIL-53(BDC) analogues, which might be associated with the higher degree of flexibility of MIL-53(TDC) as demonstrated previously.⁷⁰ This whole observation confirms the reliability of the rate constant as a descriptor to assess the H₂S stability of MOFs.

<table>
<caption>Table 1. Reaction Free Energy ($\Delta G$), Reaction Free Energy Barrier ($\Delta G^{\ddagger}$), Reversed Free Energy Barrier ($\Delta G_{r}^{\ddagger}$), and Rate Constants of the First-Step H₂S Degradation Reaction (k) for all Investigated MOFs$^{a}$</caption>
<thead>
<tr>
<th></th>
<th>$\Delta G$</th>
<th>$\Delta G^{\ddagger}$</th>
<th>$\Delta G_{r}^{\ddagger}$</th>
<th>K</th>
</tr>
</thead>
<tbody>
<tr>
<td>MIL-53(Al)-BDC</td>
<td>133</td>
<td>180</td>
<td>47</td>
<td>$-4.9 \times 10^{-9}$</td>
</tr>
<tr>
<td>MIL-53(Al)-FA</td>
<td>117</td>
<td>168</td>
<td>50</td>
<td>$-1.4 \times 10^{-9}$</td>
</tr>
<tr>
<td>MIL-53(Al)-TDC</td>
<td>117</td>
<td>134</td>
<td>17</td>
<td>$-1.1 \times 10^{-3}$</td>
</tr>
<tr>
<td>MIL-160(Al)-furan</td>
<td>130</td>
<td>176</td>
<td>46</td>
<td>$-9.0 \times 10^{-9}$</td>
</tr>
<tr>
<td>CAU-10(Al)-BDC</td>
<td>118</td>
<td>178</td>
<td>60</td>
<td>$-3.3 \times 10^{-11}$</td>
</tr>
<tr>
<td>CAU-23(Al)-TDC</td>
<td>122</td>
<td>147</td>
<td>25</td>
<td>$-4.0 \times 10^{-5}$</td>
</tr>
<tr>
<td>lp-MIL-53(Al)-BDC-NO₂</td>
<td>141</td>
<td>183</td>
<td>42</td>
<td>$-4.3 \times 10^{-8}$</td>
</tr>
<tr>
<td>lp-MIL-53(Al)-BDC- NH₂</td>
<td>163</td>
<td>208</td>
<td>45</td>
<td>$-1.5 \times 10^{-8}$</td>
</tr>
<tr>
<td>np-MIL-53(Al)-BDC-NH₂</td>
<td>168</td>
<td>206</td>
<td>38</td>
<td>$-2.5 \times 10^{-7}$</td>
</tr>
<tr>
<td>CAU-10(Ti)-BDC</td>
<td>63</td>
<td>129</td>
<td>66</td>
<td>$-2.8 \times 10^{-12}$</td>
</tr>
<tr>
<td>MIL-160(Ti)-furan</td>
<td>74</td>
<td>122</td>
<td>48</td>
<td>$-4.4 \times 10^{-9}$</td>
</tr>
<tr>
<td>MOF-74(Ni)</td>
<td>87</td>
<td>118</td>
<td>31</td>
<td>$-5.5 \times 10^{-6}$</td>
</tr>
<tr>
<td>MOF-74(Zn)</td>
<td>13</td>
<td>75</td>
<td>61</td>
<td>$-2.0 \times 10^{-11}$</td>
</tr>
<tr>
<td>MIL-91(Ti)</td>
<td>145</td>
<td>163</td>
<td>18</td>
<td>$-8.3 \times 10^{-4}$</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">$^{a}$All of the energies are reported at 298 K in kJ mol⁻¹.</td>
</tr>
</tfoot>
</table>

3.2.2. CAU-10(Al)-BDC, MIL-160(Al)-Furan, and CAU-23(Al)-TDC Frameworks. In complement to Section 3.2.1, the H₂S stability of CAU-10(Al)-BDC, its furan derivative (MIL-160(Al)-Furan), and a similar structure integrating TDC linker (CAU-23(Al)-TDC) were explored.

![](./images/812515829491957761_6.jpg)

Figure 3. Potential energy profiles for the first-step $H_2S$ degradation reaction by CAU-10(Al)-BDC (red line), MIL-160(Al)-Furan (black line), and CAU-23(Al)-TDC (blue line). The color code is the same as in Figure 1. The corresponding energies and distances are reported in kJ mol⁻¹ and Å respectively.

![](./images/812515829491957761_7.jpg)

Figure 4. Potential energy profiles for the first-step $H_2S$ degradation reaction by MIL-53(Al)-BDC (black line), MIL-53(Al)-BDC-NO₂ (red line), and MIL-53(Al)-BDC-NH₂ (blue line). The color code is the same as in Figure 1 except for nitrogen (light blue). The corresponding energies and distances are reported in kJ mol⁻¹ and Å, respectively.

Compared to MIL-53 MOFs, while CAU-23(Al)-TDC shows the same adsorption mode with the interactions between $S(H_2S)$ and $H(\mu-OH)$, CAU-10 derivatives (CAU-10(Al)-BDC and MIL-160(Al)-Furan) show different $H_2S$ adsorption configurations because their $\mu$-OH sites are not sterically accessible to the guest. Indeed, $H_2S$ interacts with the oxygen atom of the carboxylate groups. Figure 3 and Table 1 reveal that despite the fact that CAU-23(Al)-TDC shows the lowest energy barrier $\Delta E^{\ddagger}$, its associated $k$ value is much more negative than that for CAU-10(Al)-BDC. This trend, which is the same as that observed between MIL-53(Al)-TDC and MIL-53(Al)-BDC, strongly suggests that the incorporation of the TDC linker tends to reinforce the $H_2S$ stability of the MOF architecture. MIL-160(Al)-Furan built with a heteroatom-containing linker is expected to be more stable than CAU-10(Al)-BDC since its associated $k$ value is more negative by 2 orders of magnitude, leading to the following sequence in terms of stability: CAU-23(Al)-TDC $\gg$ MIL-160(Al)-Furan $>$ CAU-10(Al)-BDC. Indeed, more generally, the inclusion of heteroatoms (sulfur and oxygen) in the linkers makes MIL-53 and CAU-10 structures more stable. On the other hand, by comparing the scenarios for MIL-53(Al)-TDC/CAU-23(Al)-TDC and MIL-53(Al)-BDC/CAU-10(Al)-TDC, we found that the rate constants of MIL-53 frameworks are always slightly more negative than those of CAU-10/CAU-23 MOFs containing the same linker. This suggests that MIL-53(Al) is expected to be slightly more stable than CAU-10 (Al)/CAU-23(Al). This is due to a slightly different reversed reaction barrier value ($\Delta E_{r}^{\ddagger}$, defined as $E(\text{TS}) - E(\text{FS})$) with similar vibrational contributions for MIL-53(Al) versus CAU-10 (Al)/CAU-23(Al),

![](./images/812515829491957761_8.jpg)

Figure 5. Potential energy profiles for the first-step $H_2S$ degradation reaction by lp-MIL-53(Al)-BDC-NH₂ (black line) and np- MIL-53(Al)-BDC- NH₂ (red line). The color code is the same as in Figure 4 except for nitrogen (light blue). The corresponding energies and distances are reported in kJ mol⁻¹ and Å, respectively.

![](./images/812515829491957761_9.jpg)

Figure 6. Potential energy profiles for the first-step $H_2S$ degradation reaction by CAU-10(Ti)-BDC (black line) and MIL-160(Ti)-Furan (red line). The color code is the same as in Figure 1 except for titanium (purple). The corresponding energies and distances are reported in kJ mol⁻¹ and Å, respectively.

leading to a small variation in the reversed free energies $(\Delta G_{r}^{\ddagger})$ and $k$ values.

### 3.3. Impact of the Nature of the Functional Groups Grafted to the Organic Linker on the $H_2S$ Stability of Al-MOFs.
The stability of MIL-53(Al)-BDC was further compared with those of its functionalized derivatives with $-NO_2$ and $-NH_2$ groups, considering in all cases, an lp structure.

Compared to the pristine MIL-53(Al)-BDC, the functionalization does not affect the predominant interactions between $H_2S$ and $\mu$-OH, as shown in Figure 4, since the separating distances between $H_2S$ and $-NH_2$/$-NO_2$ groups are longer than 3 Å. The potential energy profiles shift upward upon functionalization, while the structures of each state along the reaction paths remain similar, as shown in Figure 4. The higher energy barrier $\Delta E^{\ddagger}$ and reaction energy $\Delta E$ for MIL-53(Al)-NO₂ and MIL-53(Al)-BDC-NH₂ result from the introduction of relatively bulky functional groups, which causes higher energy penalty for the $H_2S$-induced structural changes. As shown in Table 1, the rate constants $k$ calculated for both functionalized forms are slightly more negative than the value obtained for MIL-53(Al)-BDC, suggesting the following stability sequence:
$$\text{MIL-53(Al)-BDC-NO}_2 \sim \text{MIL-53(Al)-BDC-NH}_2 > \text{MIL-53(Al)-BDC}$$
Indeed, this series of calculations predicts that the functionalization of the BDC linker, a strategy often employed to enhance the affinity of the MOF for a polar molecule,⁵⁴ does not play a detrimental role in the $H_2S$ stability of the framework.

### 3.4. Impact of the Pore Size on the $H_2S$ Stability of Al-MOFs.
MIL-53(Al)-BDC-NH₂ in both its lp and np forms was considered as a prototypical model to verify if the pore size can affect the MOF stability upon exposure to $H_2S$. The IS configuration for the np form corresponds to an interaction between $S(H_2S)$ and the $\mu$-OH group in a similar way as that in the lp version. Figure 5 shows that the potential energy profiles are very similar in both cases, while Table 1 evidences that the rate constant for np-NH₂-MIL-53(Al) is only slightly more negative than that for the lp structure. The relative energy of the FS configuration for the np structure is slightly higher than that for the lp version, while the relative energies of the IS and TS configurations for the lp and np structures are quite similar. This whole observation suggests that a higher degree of pore

![](./images/812515829491957761_10.jpg)

Figure 7. Potential energy profiles for the first-step $H_2S$ degradation reaction by MOF-74(Ni) (black line) and MOF-74(Zn) (blue line). The color code is the same as in Figure 1 except for nickel (silver) and zinc (orange). The corresponding energies and distances are reported in $kJ\ mol^{-1}$ and Å, respectively.

confinement is expected to induce only a tiny change in the stability of the MOF against $H_2S$.

### 3.5. Impact of the Substitution of $Al^{3+}$ by $Ti^{4+}$ Metal Sites on the $H_2S$ Stability of MOFs.
As a typical illustration, the $H_2S$ stabilities of CAU-10(Al)-BDC and MIL-160(Al)-Furan were compared with those of the hypothetical frameworks where $Al^{3+}$ was substituted by $Ti^{4+}$; the hydroxyl $\mu$-OH functions bridging the metal sites were replaced by $\mu$-O oxo functions to keep the framework neutral. Figure 6 shows that the $H_2S$ adsorption configurations (IS) for MIL-160(Ti)-Furan and CAU-10(Ti)-BDC correspond to an interaction between $H(H_2S)$ and $\mu$-O (see Figure 3).

The resulting potential energy profiles for Ti-MOFs shift downward and both the energy barriers and reaction energies are significantly lower as compared to their values for the aluminum analogues (see Figures 6 vs 3). Nevertheless, the rate constants calculated for MIL-160(Ti)-Furan and CAU-10(Ti)-BDC (see Table 1) are only slightly more negative than the values for their Al analogues, indicating that the substitution of $Al^{3+}$ by $Ti^{4+}$ in these MOFs, which is expected to make them more hydrophobic, will not deteriorate their stability against $H_2S$. Moreover, MIL-160 remains more stable than CAU-10 irrespective of the nature of the metal sites.

### 3.6. Impact of the Presence and Nature of CUS Sites on the $H_2S$ Stability of MOFs.
The influence of the presence and nature of CUS sites on the $H_2S$ stability of the MOF architecture was typically explored with the consideration of the well-known MOF-74 architecture in its $Ni^{45}$ and $Zn^{40}$ versions. Figure 7 shows that the most stable adsorption configuration of $H_2S$ in MOF-74(Ni) corresponds to a S-end coordination toward the metal site (IS). The reaction further proceeds as follows: one of the $Ni-O$ bonds breaks, the resulting $_3$-coordinated $O$ atom forms an oxo $\mu$-O species, and one of the $H$ atoms from $H_2S$ transfers to $\mu$-O to form a $\mu$-OH (FS). Ni becomes five-coordinated in FS, in comparison to its six-coordinated geometry in IS. The rate constant associated with this MOF is simulated to be more negative $(-5. \times 10^{-6})$ than our reference MIL-53(Al)-BDC $(-4.9 \times 10^{-9})$. Indeed, MOF-74(Ni) is predicted to be stable upon exposure to $H_2S$, which is in excellent agreement with the experimental observation. $^{45}$

Next, we considered MOF-74(Zn). The $H_2S$ adsorption geometry (IS) is similar to that observed for MOF-74(Ni) and associated with slightly lower energy (see Figure 7); however, the reaction proceeds in a slightly different manner. We can observe that TS shows that one of the $\mu$-O atoms remains unsaturated due to the breaking of the $Zn-O$ bond, while one of the $H$ atoms from $H_2S$ transfers to the unsaturated oxygen atom to form a OH group. Next, the $H$ atom further transfers to $\mu$-O formed by the breaking of the second $Zn-O$ bond, and the dangling oxygen atom makes a bond with $Zn$ again to form FS. The energy barrier and reaction energy are significantly lower than the values obtained for MOF-74(Ni), indicating that this reaction is more feasible than that involved in MOF-74(Zn). The resulting rate constant for MOF-74(Zn) $(-2.0 \times 10^{-11})$ is much less negative than those for MOF-74 (Ni) and our reference MIL-53(Al)-BDC. Therefore MOF-74(Zn) is predicted to be much less stable compared to its Ni analogue. This simulated trend is in excellent agreement with previous experimental observations, which reveals that MOF-74(Zn) is unstable upon $H_2S$ adsorption. $^{40,45}$ This computational work confirms that the $H_2S$ stability of CUS-containing MOFs can be tuned by adopting the adequate nature of metal sites.

## 4. DISCUSSION

Based on the rate constants of the first-step $H_2S$ degradation reaction reported in Table 1, the series of MOFs can be classified in terms of $H_2S$ stability as follows:

CAU-10(Ti)-BDC $\sim$ CAU-10(Al)-BDC $\sim$ MOF-74(Zn) < MIL-53(Al)-FA $\sim$ MIL-160(Ti)-Furan $\sim$ MIL-53(Al)-BDC $\sim$ MIL-160(Al)-Furan $\sim$ lp-MIL-53(Al)-BDC-$NO_2$ $\sim$ lp-MIL-53(Al)-BDC-$NH_2$ < np-MIL-53(Al)-BDC-$NH_2$ < MOF-74(Ni) < MIL-53(Al)-TDC

MIL-53(Al)-TDC is found to be the most stable MOF architecture upon exposure to $H_2S$. From this ranking, MIL-53 MOFs regardless of linkers/functional groups are expected to be rather stable since MIL-53(Al)-FA, predicted the least stable MIL-53, was already reported to be stable against $H_2S.^{42}$ Furthermore, the CAU-10 frameworks are expected to be unstable under exposure to $H_2S$ since a similar rate constant value was found to that for MOF-74(Zn), which was demonstrated to collapse upon $H_2S$ adsorption. As a further predictive stage, we extended our study to predict the $H_2S$ stability of the MIL-91(Ti) MOF, which demonstrated good promises for $CO_2$ capture. $^{57}$ Based on the stability ranking

revealed above, since this material does not exhibit CUS sites, shows a high degree of confinement, and its linker contains heteroatoms (N and P), it is expected to show good stability against $H_2S$. MIL-91(Ti) was then investigated with the consideration of the degradation reaction model defined above.

Figure 8 shows that the most stable adsorption configuration of $H_2S$ (IS) is a H-end configuration over the oxygen atom of the
![](./images/812515829491957761_11.jpg)

Figure 8. Potential energy profiles for the first-step $H_2S$ degradation reaction by MIL-91(Ti). Color codes: carbon (brown), oxygen (red), hydrogen (white), sulfur (yellow), nitrogen (blue), phosphorus (pink), and titanium (purple). The corresponding energies and distances are reported in $kJ\ mol^{-1}$ and Å, respectively.

phosphonate group of the MOF linker. The reaction proceeds via the breaking of one $Ti-O$ bond and the formation of a $Ti-S$ bond, while a $H$ atom of $H_2S$ transfers to the $PO_3^-$ group to form a $PO_3H$ group (FS). This process is associated with a very high energy barrier, which makes it kinetically and thermodynamically unfavorable. The resulting rate constant calculated is found to be highly negative $(-8.3 \times 10^{-4})$, indicating that MIL-91(Ti) is expected to be highly stable against $H_2S$.

## 5. CONCLUSIONS

In summary, this computational study delivers a systematic assessment of the $H_2S$ stability of a series of MOFs based on the exploration of the first-step degradation reaction. We first analyzed three plausible mechanisms using MIL-53(Al)-BDC as a model MOF and determined the most likely degradation mechanism. The rate constant of the first-step degradation reaction was proposed as a reliable descriptor for characterizing the $H_2S$ stability of MOFs and further used to assess the $H_2S$ stability of a wide range of MOFs to build up a qualitative $H_2S$ stability ranking. Interestingly, this allowed us to reveal that the incorporation of heteroatoms in the organic linkers of MIL-53 and CAU-10 reinforces their $H_2S$ stability, while grafting functional groups or changing the nature of metal sites leads to the similar $H_2S$ stability of the architecture. MOFs containing CUS sites were also found to show distinct behavior, depending on the nature of the metal sites. The MOF MIL-91 (Ti), a promising candidate for $CO_2$ capture, was further considered as a showcase to apply our methodology for the anticipation of its $H_2S$ stability. Our computational approach was demonstrated to allow an accurate and easy handling evaluation of the $H_2S$ stability of MOFs to avoid the use of a highly toxic and corrosive gas in experimental techniques. As a future outlook, we expect to extend our strategy to evaluate the stability of MOFs upon exposure to other corrosive molecules such as $SO_x$ and $NH_3$. These findings might pave the way toward the identification of key chemical and structural features to guide the development of highly stable MOFs.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acsami.0c21285.

All of the structural details of MOF systems; DFT optimized unit cell lattice parameters for all investigated MOFs (Table S1); DFT optimized structures of MIL-53(Al)-BDC, MIL-53(Al)-FA, and MIL-53(Al)-TDC (Figure S1); DFT optimized structures of CAU-10(Al)-BDC, MIL-160(Al)-Furan, and CAU-23(Al)-TDC (Figure S2); DFT optimized structures of lp-MIL-53(Al)-BDC-NO2, lp-MIL-53(Al)-BDC-NH2, and np-MIL-53(Al)-BDC-NH2 (Figure S3); DFT optimized structures of MIL-160(Ti)-Furan and CAU-10(Ti)-TDC (Figure S4); DFT optimized structures of MOF-74(Ni) and MOF-74(Zn) (Figure S5); and DFT optimized structure of MIL-91(Ti) (Figure S6) (PDF)

## AUTHOR INFORMATION

### Corresponding Author
Guillaume Maurin - ICGM, Univ. Montpellier, CNRS, ENSCM, Montpellier 34095, France; orcid.org/0000-0002-2096-0450; Email: guillaume.maurin1@umontpellier.fr

### Author
Pengbo Lyu - ICGM, Univ. Montpellier, CNRS, ENSCM, Montpellier 34095, France; orcid.org/0000-0002-1785-9861

Complete contact information is available at:
https://pubs.acs.org/10.1021/acsami.0c21285

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
This project received funding from the European Union's Horizon 2020 research and innovation programme under Grant Agreement No. 837975.

## REFERENCES
(1) Bavykina, A.; Kolobov, N.; Khan, I. S.; Bau, J. A.; Ramirez, A.; Gascon, J. Metal−Organic Frameworks in Heterogeneous Catalysis: Recent Progress, New Trends, and Future Perspectives. *Chem. Rev.* 2020, 120, 8468−8535.
(2) Wang, Q.; Astruc, D. State of the Art and Prospects in Metal− Organic Framework (MOF)-Based and MOF-Derived Nanocatalysis. *Chem. Rev.* 2020, 120, 1438−1511.
(3) Qian, Q.; Asinger, P. A.; Lee, M. J.; Han, G.; Mizrahi Rodriguez, K.; Lin, S.; Benedetti, F. M.; Wu, A. X.; Chi, W. S.; Smith, Z. P. MOF-Based Membranes for Gas Separations. *Chem. Rev.* 2020, 120, 8161−8266.
(4) Liu, X.; Wang, X.; Kapteijn, F. Water and Metal−Organic Frameworks: From Interaction toward Utilization. *Chem. Rev.* 2020, 120, 8303−8377.
(5) Adil, K.; Belmabkhout, Y.; Pillai, R. S.; Cadiau, A.; Bhatt, P. M.; Assen, A. H.; Maurin, G.; Eddaoudi, M. Gas/vapour separation using ultra-microporous metal−organic frameworks: insights into the

4820
https://dx.doi.org/10.1021/acsami.0c21285
ACS Appl. Mater. Interfaces 2021, 13, 4813−4822

structure/separation relationship. *Chem. Soc. Rev.* 2017, 46, 3402-3430.

(6) Maurin, G.; Serre, C.; Cooper, A.; Férey, G. The new age of MOFs and of their porous-related solids. *Chem. Soc. Rev.* 2017, 46, 3104-3107.

(7) Horcajada, P.; Gref, R.; Baati, T.; Allan, P. K.; Maurin, G.; Couvreur, P.; Férey, G.; Morris, R. E.; Serre, C. Metal-Organic Frameworks in Biomedicine. *Chem. Rev.* 2012, 112, 1232-1268.

(8) Terzopoulou, A.; Nicholas, J. D.; Chen, X.-Z.; Nelson, B. J.; Pané, S.; Puigmartí-Luis, J. Metal-Organic Frameworks in Motion. *Chem. Rev.* 2020, 120, 11175-11193.

(9) Lim, D.-W.; Kitagawa, H. Proton Transport in Metal-Organic Frameworks. *Chem. Rev.* 2020, 120, 8416-8467.

(10) Islamoglu, T.; Chen, Z.; Wasson, M. C.; Buru, C. T.; Kirlikovali, K. O.; Afrin, U.; Mian, M. R.; Farha, O. K. Metal-Organic Frameworks against Toxic Chemicals. *Chem. Rev.* 2020, 120, 8130-8160.

(11) Xie, L. S.; Skorupskii, G.; Dincă, M. Electrically Conductive Metal-Organic Frameworks. *Chem. Rev.* 2020, 120, 8536-8580.

(12) Thorarinsdottir, A. E.; Harris, T. D. Metal-Organic Framework Magnets. *Chem. Rev.* 2020, 120, 8716-8789.

(13) Avci, G.; Erucar, I.; Keskin, S. Do New MOFs Perform Better for CO2 Capture and H2 Purification? Computational Screening of the Updated MOF Database. *ACS Appl. Mater. Interfaces* 2020, 12, 41567-41579.

(14) Liang, W.; Bhatt, P. M.; Shkurenko, A.; Adil, K.; Mouchaham, G.; Aggarwal, H.; Mallick, A.; Jamal, A.; Belmabkhout, Y.; Eddaoudi, M. A Tailor-Made Interpenetrated MOF with Exceptional Carbon-Capture Performance from Flue Gas. *Chem* 2019, 5, 950-963.

(15) Mohideen, M. I. H.; Pillai, R. S.; Adil, K.; Bhatt, P. M.; Belmabkhout, Y.; Shkurenko, A.; Maurin, G.; Eddaoudi, M. A Fine- Tuned MOF for Gas and Vapor Separation: A Multipurpose Adsorbent for Acid Gas Removal, Dehydration, and BTX Sieving. *Chem* 2017, 3, 822-833.

(16) Tchalala, M. R.; Bhatt, P. M.; Chappanda, K. N.; Tavares, S. R.; Adil, K.; Belmabkhout, Y.; Shkurenko, A.; Cadiau, A.; Heymans, N.; De Weireld, G.; Maurin, G.; Salama, K. N.; Eddaoudi, M. Fluorinated MOF platform for selective removal and storage of SO2 from flue gas and air. *Nat. Commun.* 2019, 10, No. 1328.

(17) Brandt, P.; Nuhnen, A.; Lange, M.; Möllmer, J.; Weingart, O.; Janiak, C. Metal-Organic Frameworks with Potential Application for SO2 Separation and Flue Gas Desulfurization. *ACS Appl. Mater. Interfaces* 2019, 11, 17350-17358.

(18) Belmabkhout, Y.; Pillai, R. S.; Alezi, D.; Shekhah, O.; Bhatt, P. M.; Chen, Z.; Adil, K.; Vaesen, S.; De Weireld, G.; Pang, M.; Suetin, M.; Cairns, A. J.; Solovyeva, V.; Shkurenko, A.; El Tall, O.; Maurin, G.; Eddaoudi, M. Metal-organic frameworks to satisfy gas upgrading demands: fine-tuning the soc-MOF platform for the operative removal of H2S. *J. Mater. Chem. A* 2017, 5, 3293-3303.

(19) Belmabkhout, Y.; Bhatt, P. M.; Adil, K.; Pillai, R. S.; Cadiau, A.; Shkurenko, A.; Maurin, G.; Liu, G.; Koros, W. J.; Eddaoudi, M. Natural gas upgrading using a fluorinated MOF with tuned H2S and CO2 adsorption selectivity. *Nat. Energy* 2018, 3, 1059-1066.

(20) Yang, Q.; Wiersum, A. D.; Llewellyn, P. L.; Guillerm, V.; Serre, C.; Maurin, G. Functionalizing porous zirconium terephthalate UiO-66(Zr) for natural gas upgrading: a computational exploration. *Chem. Commun.* 2011, 47, 9603-9605.

(21) Martínez-Ahumada, E.; López-Olvera, A.; Jancik, V.; Sánchez- Bautista, J. E.; González-Zamora, E.; Martis, V.; Williams, D. R.; Ibarra, I. A. MOF Materials for the Capture of Highly Toxic H2S and SO2. *Organometallics* 2020, 39, 883-915.

(22) Daglar, H.; Keskin, S. Computational Screening of Metal- Organic Frameworks for Membrane-Based CO2/N2/H2O Separa- tions: Best Materials for Flue Gas Separation. *J. Phys. Chem. C* 2018, 122, 17347-17357.

(23) Sumida, K.; Rogow, D. L.; Mason, J. A.; McDonald, T. M.; Bloch, E. D.; Herm, Z. R.; Bae, T.-H.; Long, J. R. Carbon Dioxide Capture in Metal-Organic Frameworks. *Chem. Rev.* 2012, 112, 724-781.

(24) Qian, X.; Zhang, R.; Chen, L.; Lei, Y.; Xu, A. Surface Hydrophobic Treatment of Water-Sensitive DUT-4 Metal-Organic Framework To Enhance Water Stability for Hydrogen Storage. *ACS Sustainable Chem. Eng.* 2019, 7, 16007-16012.

(25) Lenzen, D.; Eggebrecht, J. G.; Mileo, P. G. M.; Fröhlich, D.; Henninger, S.; Atzori, C.; Bonino, F.; Lieb, A.; Maurin, G.; Stock, N. Unravelling the water adsorption in a robust iron carboxylate metal- organic framework. *Chem. Commun.* 2020, 56, 9628-9631.

(26) Karmakar, A.; Mileo, P. G. M.; Bok, I.; Peh, S. B.; Zhang, J.; Yuan, H.; Maurin, G.; Zhao, D. Thermo-Responsive MOF/Polymer Composites for Temperature-Mediated Water Capture and Release. *Angew. Chem., Int. Ed.* 2020, 59, 11003-11009.

(27) Nguyen, H. L.; Hanikel, N.; Lyle, S. J.; Zhu, C.; Proserpio, D. M.; Yaghi, O. M. A Porous Covalent Organic Framework with Voided Square Grid Topology for Atmospheric Water Harvesting. *J. Am. Chem. Soc.* 2020, 142, 2218-2221.

(28) Xue, W.; Zhang, Z.; Huang, H.; Zhong, C.; Mei, D. Theoretical Insights into the Initial Hydrolytic Breakdown of HKUST-1. *J. Phys. Chem. C* 2020, 124, 1991-2001.

(29) Tan, K.; Zuluaga, S.; Gong, Q.; Canepa, P.; Wang, H.; Li, J.; Chabal, Y. J.; Thonhauser, T. Water Reaction Mechanism in Metal Organic Frameworks with Coordinatively Unsaturated Metal Ions: MOF-74. *Chem. Mater.* 2014, 26, 6886-6895.

(30) Zhang, C.; Han, C.; Sholl, D. S.; Schmidt, J. R. Computational Characterization of Defects in Metal-Organic Frameworks: Sponta- neous and Water-Induced Point Defects in ZIF-8. *J. Phys. Chem. Lett.* 2016, 7, 459-464.

(31) Cui, K.; Schmidt, J. R. Enabling Efficient and Accurate Computational Studies of MOF Reactivity via QM/MM and QM/ QM Methods. *J. Phys. Chem. C* 2020, 124, 10550-10560.

(32) Feng, L.; Wang, K.-Y.; Day, G. S.; Ryder, M. R.; Zhou, H.-C. Destruction of Metal-Organic Frameworks: Positive and Negative Aspects of Stability and Lability. *Chem. Rev.* 2020, 120, 13087-13133.

(33) Flores, J. G.; Zárate-Colín, J. A.; Sánchez-González, E.; Valenzuela, J. R.; Gutiérrez-Alejandre, A.; Ramírez, J.; Jancik, V.; Aguilar-Pliego,J.; Zorrilla, M. C.; Lara-García, H. A.; González-Zamora, E.; Guzmán-González, G.; González, I.; Maurin, G.; Ibarra, I. A. Partially Reversible H2S Adsorption by MFM-300(Sc): Formation of Polysulfides. *ACS Appl. Mater. Interfaces* 2020, 12, 18885-18892.

(34) Carter, J. H.; Morris, C. G.; Godfrey, H. G. W.; Day, S. J.; Potter, J.; Thompson, S. P.; Tang, C. C.; Yang, S.; Schröder, M. Long-Term Stability of MFM-300(Al) toward Toxic Air Pollutants. *ACS Appl. Mater. Interfaces* 2020, 12, 42949-42954.

(35) Jiang, H.; Zhou, J.; Wang, C.; Li, Y.; Chen, Y.; Zhang, M. Effect of Cosolvent and Temperature on the Structures and Properties of Cu- MOF-74 in Low-temperature NH3-SCR. *Ind. Eng. Chem. Res.* 2017, 56, 3542-3550.

(36) Han, S.; Huang, Y.; Watanabe, T.; Nair, S.; Walton, K. S.; Sholl, D. S. Carson Meredith, J. MOF stability and gas adsorption as a function of exposure to water, humid air, SO2, and NO2. *Microporous Mesoporous Mater.* 2013, 173, 86-91.

(37) Vaesen, S.; Guillerm, V.; Yang, Q.; Wiersum, A. D.; Marszalek, B.; Gil, B.; Vimont, A.; Daturi, M.; Devic T, G.; Llewellyn, P. L.; Serre C, Maurin.; De Weireld, G. A robust amino-functionalized titanium(iv) based MOF for improved separation of acid gases. *Chem. Commun.* 2013, 49, 10082-10084.

(38) Hamon, L.; Serre, C.; Devic, T.; Loiseau, T.; Millange, F.; Férey, G.; Weireld, G. D. Comparative Study of Hydrogen Sulfide Adsorption in the MIL-53(Al, Cr, Fe), MIL-47(V), MIL-100(Cr), and MIL-101(Cr) Metal-Organic Frameworks at Room Temperature. *J. Am. Chem. Soc.* 2009, 131, 8775-8777.

(39) Hamon, L.; Leclerc, H.; Ghoufi, A.; Oliviero, L.; Travert, A.; Lavalley, J.-C.; Devic, T.; Serre, C.; Férey, G.; De Weireld, G.; Vimont, A.; Maurin, G. Molecular Insight into the Adsorption of H2S in the Flexible MIL-53(Cr) and Rigid MIL-47(V) MOFs: Infrared Spectros- copy Combined to Molecular Simulations. *J. Phys. Chem. C* 2011, 115, 2047-2056.

(40) Liu, J.; Wei, Y.; Li, P.; Zhao, Y.; Zou, R. Selective H2S/CO2 Separation by Metal-Organic Frameworks Based on Chemical- Physical Adsorption. *J. Phys. Chem. C* 2017, 121, 13249-13255.

(41) Sánchez-González, E.; Mileo, P. G. M.; Sagastuy-Breña, M.; Álvarez, J. R.; Reynolds, J. E.; Villarreal, A.; Gutiérrez-Alejandre, A.; Ramírez, J.; Balmaseda, J.; González-Zamora, E.; Maurin, G.; Humphrey, S. M.; Ibarra, I. A. Highly reversible sorption of H2S and CO2 by an environmentally friendly Mg-based MOF. J. Mater. Chem. A 2018, 6, 16900−16909.

(42) Shen, J.; Dailly, A.; Beckner, M. Natural gas sorption evaluation on microporous materials. Microporous Mesoporous Mater. 2016, 235, 170−177.

(43) Zárate, J. A.; Sánchez-González, E.; Jurado-Vázquez, T.; Gutiérrez-Alejandre, A.; González-Zamora, E.; Castillo, I.; Maurin, G.; Ibarra, I. A. Outstanding reversible H2S capture by an Al(iii)-based MOF. Chem. Commun. 2019, 55, 3049−3052.

(44) Liu, G.; Cadiau, A.; Liu, Y.; Adil, K.; Chernikova, V.; Carja, I.-D.; Belmabkhout, Y.; Karunakaran, M.; Shekhah, O.; Zhang, C.; Itta, A. K.; Yi, S.; Eddaoudi, M.; Koros, W. J. Enabling Fluorinated MOF-Based Membranes for Simultaneous Removal of H2S and CO2 from Natural Gas. Angew. Chem., Int. Ed. 2018, 57, 14811−14816.

(45) Allan, P. K.; Wheatley, P. S.; Aldous, D.; Mohideen, M. I.; Tang, C.; Hriljac, J. A.; Megson, I. L.; Chapman, K. W.; De Weireld, G.; Vaesen, S.; Morris, R. E. Metal−organic frameworks for the storage and delivery of biologically active hydrogen sulfide. Dalton Trans. 2012, 41, 4060−4066.

(46) Petit, C.; Mendoza, B.; Bandosz, T. J. Hydrogen Sulfide Adsorption on MOFs and MOF/Graphite Oxide Composites. ChemPhysChem 2010, 11, 3678−3684.

(47) Zheng, X.-X.; Shen, L.-J.; Chen, X.-P.; Zheng, X.-H.; Au, C.-T.; Jiang, L.-L. Amino-Modified Fe-Terephthalate Metal−Organic Frame- work as an Efficient Catalyst for the Selective Oxidation of H2S. Inorg. Chem. 2018, 57, 10081−10089.

(48) Zheng, X.-X.; Fang, Z.-P.; Dai, Z.-J.; Cai, J.-M.; Shen, L.-J.; Zhang, Y.-F.; Au, C.-T.; Jiang, L.-L. Iron-Based Metal−Organic Frameworks as Platform for H2S Selective Conversion: Structure- Dependent Desulfurization Activity. Inorg. Chem. 2020, 59, 4483−4492.

(49) Zhang, X.; Zhang, Q.; Yue, D.; Zhang, J.; Wang, J.; Li, B.; Yang, Y.; Cui, Y.; Qian, G. Flexible Metal−Organic Framework-Based Mixed- Matrix Membranes: A New Platform for H2S Sensors. Small 2018, 14, No. 1801563.

(50) Leubner, S.; Stäglich, R.; Franke, J.; Jacobsen, J.; Gosch, J.; Siegel, R.; Reinsch, H.; Maurin, G.; Senker, J.; Yot, P. G.; Stock, N. Solvent Impact on the Properties of Benchmark Metal−Organic Frameworks: Acetonitrile-Based Synthesis of CAU-10, Ce-UiO-66, and Al-MIL-53. Chem. - Eur. J. 2020, 26, 3877−3883.

(51) Lenzen, D.; Zhao, J.; Ernst, S.-J.; Wahiduzzaman, M.; Ken Inge, A.; Fröhlich, D.; Xu, H.; Bart, H.-J.; Janiak, C.; Henninger, S.; Maurin, G.; Zou, X.; Stock, N. A metal−organic framework for efficient water- based ultra-low-temperature-driven cooling. Nat. Commun. 2019, 10, No. 3025.

(52) Wahiduzzaman, M.; Lenzen, D.; Maurin, G.; Stock, N.; Wharmby, M. T. Rietveld Refinement of MIL-160 and Its Structural Flexibility Upon H2O and N2 Adsorption. Eur. J. Inorg. Chem. 2018, 2018, 3626−3632.

(53) Biswas, S.; Ahnfeldt, T.; Stock, N. New Functionalized Flexible Al-MIL-53-X (X = -Cl, -Br, -CH3, -NO2, -(OH)2) Solids: Syntheses, Characterization, Sorption, and Breathing Behavior. Inorg. Chem. 2011, 50, 9518−9526.

(54) Stavitski, E.; Pidko, E. A.; Couck, S.; Remy, T.; Hensen, E. J. M.; Weckhuysen, B. M.; Denayer, J.; Gascon, J.; Kapteijn, F. Complexity behind CO2 Capture on NH2-MIL-53(Al). Langmuir 2011, 27, 3970−3976.

(55) Wang, S.; Cabrero-Antonino, M.; Navalón, S.; Cao, C.-c.; Tissot, A.; Dovgaliuk, I.; Marrot, J.; Martineau-Corcos, C.; Yu, L.; Wang, H.; Shepard, W.; García, H.; Serre, C. A Robust Titanium Isophthalate Metal-Organic Framework for Visible-Light Photocatalytic CO2 Methanation. Chem 2020, 6, 3409−3427.

(56) Cadiau, A.; Lee, J. S.; Damasceno Borges, D.; Fabry, P.; Devic, T.; Wharmby, M. T.; Martineau, C.; Foucher, D.; Taulelle, F.; Jun, C.-H.; Hwang, Y. K.; Stock, N.; De Lange, M. F.; Kapteijn, F.; Gascon, J.; Maurin, G.; Chang, J.-S.; Serre, C. Design of Hydrophilic Metal Organic Framework Water Adsorbents for Heat Reallocation. Adv. Mater. 2015, 27, 4775−4780.

(57) Benoit, V.; Pillai, R. S.; Orsi, A.; Normand, P.; Jobic, H.; Nouar, F.; Billemont, P.; Bloch, E.; Bourrelly, S.; Devic, T.; Wright, P. A.; de Weireld, G.; Serre, C.; Maurin, G.; Llewellyn, P. L. MIL-91(Ti), a small pore metal−organic framework which fulfils several criteria: an upscaled green synthesis, excellent water stability, high CO2 selectivity and fast CO2 transport. J. Mater. Chem. A 2016, 4, 1383−1389.

(58) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 1996, 77, 3865−3868.

(59) Blöchl, P. E. Projector augmented-wave method. Phys. Rev. B 1994, 50, 17953−17979.

(60) Kresse, G.; Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. Comput. Mater. Sci. 1996, 6, 15−50.

(61) Kresse, G.; Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B 1999, 59, 1758−1775.

(62) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. J. Chem. Phys. 2010, 132, No. 154104.

(63) Dudarev, S. L.; Botton, G. A.; Savrasov, S. Y.; Humphreys, C. J.; Sutton, A. P. Electron-energy-loss spectra and the structural stability of nickel oxide: An LSDA+U study. Phys. Rev. B 1998, 57, 1505−1509.

(64) Wang, L.; Maxisch, T.; Ceder, G. Oxidation energies of transition metal oxides within the GGA + U framework. Phys. Rev. B 2006, 73, No. 195107.

(65) Hu, Z.; Metiu, H. Choice of U for DFT+U Calculations for Titanium Oxides. J. Phys. Chem. C 2011, 115, 5841−5845.

(66) Henkelman, G.; Uberuaga, B. P.; Jónsson, H. A climbing image nudged elastic band method for finding saddle points and minimum energy paths. J. Chem. Phys. 2000, 113, 9901−9904.

(67) Henkelman, G. Vasp TST Tools, 2020. http://theory.um.utexas.edu/vsttools/.

(68) Arevalo, R. L.; Escaño, M. C. S.; Kasai, H. Computational Mechanistic Study of Borohydride Electrochemical Oxidation on Au3Ni(111). J. Phys. Chem. C 2013, 117, 3818−3825.

(69) Mounfield, W. P.; Han, C.; Pang, S. H.; Tumuluri, U.; Jiao, Y.; Bhattacharyya, S.; Dutzer, M. R.; Nair, S.; Wu, Z.; Lively, R. P.; Sholl, D. S.; Walton, K. S. Synergistic Effects of Water and SO2 on Degradation of MIL-125 in the Presence of Acid Gases. J. Phys. Chem. C 2016, 120, 27230−27240.

(70) Wahiduzzaman, M.; Reimer, N.; Itié, J.-P.; Stock, N.; Maurin, G.; Yot, P. G. Mechanical-pressure induced response of the MOF Al-MIL- 53-TDC. Polyhedron 2018, 155, 144−148.